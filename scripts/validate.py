#!/usr/bin/env python3
"""Validate the AI Sociology asset packages against the platform conventions.

Checks three things:

1. Expert packages under ``experts/`` - structure, ``plugin.json`` fields, avatars,
   referenced agents and skills, and expert-team specifics.
2. Skill packages under ``skills/`` - ``SKILL.md`` frontmatter, naming, directory depth.
3. Repository-wide hygiene - de-identification, junk files, archive integrity.

Usage::

    python3 scripts/validate.py            # full report
    python3 scripts/validate.py --quiet    # exit code only (for CI)

Exit code is 0 when everything passes, 1 otherwise.
"""

from __future__ import annotations

import json
import os
import re
import struct
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

#: Expert identifiers may only use lowercase letters, digits and hyphens.
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

#: Chinese display descriptions must sit in this range.
DESC_ZH_MIN, DESC_ZH_MAX = 40, 50

#: Avatars: 512x512 PNG or JPG, at most 500 KB.
AVATAR_MAX_BYTES = 500 * 1024
AVATAR_SIZE = 512

#: Skill packages support at most two directory levels inside the package.
SKILL_MAX_DEPTH = 2

#: Category identifiers accepted by the platform (15 in total).
VALID_CATEGORY_IDS = {
    "01-ProductDesign", "02-DevTools", "03-MarketingGrowth", "04-DataAI",
    "05-OfficeEfficiency", "06-ContentCreative", "07-FinanceInvestment",
    "08-HRPeople", "09-LegalCompliance", "10-CustomerService",
    "11-SecurityCompliance", "12-IndustryConsultant",
    "13-TencentZone", "14-WorldWise", "15-Education",
}

EXPERT_REQUIRED = [
    "name", "version", "author", "agents", "skills", "expertType", "agentName",
    "displayName", "profession", "displayDescription", "avatar", "categoryId",
    "defaultInitPrompt", "tags", "quickPrompts",
]

SKILL_REQUIRED = [
    "name", "display_name", "display_name_en", "description",
    "description_zh", "description_en", "version", "author",
]

# Optional private terms are supplied at runtime, never stored in source.
BANNED_TERMS = json.loads(os.environ.get("PRIVATE_SCAN_TERMS_JSON", "[]"))

#: Content paths subject to optional private-term scanning.
CONTENT_PREFIXES = ("experts/", "skills/", "docs/", "theory/")
CONTENT_SUFFIXES = (".md", ".json", ".txt", ".yml", ".yaml", ".cff")

#: Files that must never be committed.
JUNK_NAMES = {".DS_Store", ".created-by-session", "Thumbs.db", "desktop.ini"}

PROBLEMS: list[str] = []
NOTES: list[str] = []
QUIET = "--quiet" in sys.argv


def fail(where: str, msg: str) -> None:
    PROBLEMS.append(f"{where}: {msg}")


def note(msg: str) -> None:
    NOTES.append(msg)


def say(msg: str = "") -> None:
    if not QUIET:
        print(msg)


# ---------------------------------------------------------------------------
# Image helpers (stdlib only, no Pillow dependency)
# ---------------------------------------------------------------------------


def png_size(path: Path) -> tuple[int, int] | None:
    """Return (width, height) for a PNG file, or None if it is not a valid PNG."""
    try:
        with path.open("rb") as fh:
            header = fh.read(24)
    except OSError:
        return None
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    try:
        width, height = struct.unpack(">II", header[16:24])
    except struct.error:
        return None
    return int(width), int(height)


def jpeg_size(path: Path) -> tuple[int, int] | None:
    """Return (width, height) for a JPEG file by walking its markers."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) < 4 or data[:2] != b"\xff\xd8":
        return None
    idx = 2
    while idx < len(data) - 9:
        if data[idx] != 0xFF:
            idx += 1
            continue
        marker = data[idx + 1]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height, width = struct.unpack(">HH", data[idx + 5:idx + 9])
            return int(width), int(height)
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            idx += 2
            continue
        seg = struct.unpack(">H", data[idx + 2:idx + 4])[0]
        idx += 2 + seg
    return None


def image_size(path: Path) -> tuple[int, int] | None:
    return png_size(path) or jpeg_size(path)


# ---------------------------------------------------------------------------
# YAML frontmatter
# ---------------------------------------------------------------------------


def split_frontmatter(text: str) -> str | None:
    """Return the raw frontmatter block of a Markdown file, or None."""
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    return match.group(1) if match else None


def check_frontmatter_syntax(where: str, fm: str) -> dict:
    """Regex-level checks plus a real YAML parse when PyYAML is available."""
    data: dict = {}

    for line in fm.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(.*)$", line)
        if not match:
            if not line.startswith((" ", "\t", "-")):
                fail(where, f"malformed frontmatter line: {line[:70]!r}")
            continue
        key, raw = match.group(1), match.group(2)
        # Colon must be followed by a space (or nothing).
        if raw and not raw.startswith(" "):
            fail(where, f"missing space after colon on key '{key}'")
        value = raw.strip()
        if value and value[:1] in ("'", '"'):
            fail(where, f"quoted value on key '{key}' - quotes often break parsing")
        # A colon followed by a space inside a value is the classic parse breaker.
        if ": " in value:
            fail(where, f"value of '{key}' contains ': ' - rewrite without the colon")
        if value[:1] in ("[", "{", "#", "&", "*", "!", "|", ">", "%", "@", "`"):
            fail(where, f"value of '{key}' starts with a reserved character")
        data[key] = value

    try:
        import yaml  # type: ignore

        try:
            parsed = yaml.safe_load(fm)
            if not isinstance(parsed, dict):
                fail(where, "frontmatter did not parse into a mapping")
            else:
                data = {k: v for k, v in parsed.items() if v is not None}
        except yaml.YAMLError as exc:
            fail(where, f"YAML parse failed: {str(exc).splitlines()[0]}")
    except ImportError:
        note("PyYAML not installed - strict YAML parsing skipped")

    return data


# ---------------------------------------------------------------------------
# Expert packages
# ---------------------------------------------------------------------------


def check_expert(pkg: Path) -> dict | None:
    where = f"experts/{pkg.name}"
    say(f"\n[expert] {pkg.name}")

    manifest = pkg / ".codebuddy-plugin" / "plugin.json"
    if not manifest.is_file():
        fail(where, "missing .codebuddy-plugin/plugin.json")
        return None

    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(where, f"plugin.json is not valid JSON: {exc}")
        return None

    for field in EXPERT_REQUIRED:
        if field not in data or data[field] in (None, "", [], {}):
            fail(where, f"plugin.json missing required field '{field}'")

    # name
    name = data.get("name", "")
    if not NAME_RE.match(name):
        fail(where, f"name '{name}' must be lowercase kebab-case")
    if name != pkg.name:
        fail(where, f"name '{name}' does not match directory '{pkg.name}'")

    # author
    author = data.get("author") or {}
    if not isinstance(author, dict):
        fail(where, "author must be an object")
    else:
        for key in ("name", "email"):
            if not author.get(key):
                fail(where, f"author missing '{key}'")

    # bilingual fields
    for field in ("displayName", "profession", "displayDescription"):
        value = data.get(field)
        if not isinstance(value, dict):
            fail(where, f"{field} must be an object with en/zh")
            continue
        for lang in ("en", "zh"):
            if not value.get(lang):
                fail(where, f"{field}.{lang} is empty")

    desc_zh = (data.get("displayDescription") or {}).get("zh", "")
    if desc_zh and not (DESC_ZH_MIN <= len(desc_zh) <= DESC_ZH_MAX):
        fail(where, f"displayDescription.zh is {len(desc_zh)} chars, "
                    f"must be {DESC_ZH_MIN}-{DESC_ZH_MAX}")

    # tags and quick prompts
    for field, count in (("tags", 3), ("quickPrompts", 3)):
        value = data.get(field)
        if isinstance(value, list) and len(value) != count:
            fail(where, f"{field} has {len(value)} entries, expected exactly {count}")

    # category
    category = data.get("categoryId", "")
    if category and category not in VALID_CATEGORY_IDS:
        fail(where, f"categoryId '{category}' is not one of the known categories")

    # expert type
    expert_type = data.get("expertType")
    is_team = expert_type == "team"
    if expert_type not in ("agent", "team"):
        fail(where, f"expertType '{expert_type}' must be 'agent' or 'team'")

    if is_team:
        if (data.get("displayName") or {}).get("zh") != (data.get("profession") or {}).get("zh"):
            fail(where, "for expert teams, profession must equal displayName")
        settings = pkg / "settings.json"
        if not settings.is_file():
            fail(where, "expert team must have settings.json")
        else:
            try:
                cfg = json.loads(settings.read_text(encoding="utf-8"))
                if cfg.get("agent") != data.get("agentName"):
                    fail(where, "settings.json 'agent' must equal agentName")
            except json.JSONDecodeError:
                fail(where, "settings.json is not valid JSON")
        info = data.get("teamInfo") or {}
        if info.get("leadAgent") != data.get("agentName"):
            fail(where, "teamInfo.leadAgent must equal agentName")
        members = data.get("members")
        if not isinstance(members, list) or not members:
            fail(where, "expert team must declare members[]")
        else:
            leads = [m for m in members if m.get("role") == "lead"]
            if len(leads) != 1:
                fail(where, f"members[] must have exactly one lead, found {len(leads)}")
            for member in members:
                mid = member.get("id", "?")
                if not member.get("name"):
                    fail(where, f"member '{mid}' is missing 'name'")
                if not member.get("displayName"):
                    fail(where, f"member '{mid}' is missing 'displayName'")

    # agents
    for rel in data.get("agents", []):
        target = pkg / rel.lstrip("./")
        if not target.is_file():
            fail(where, f"declared agent file missing: {rel}")

    # skills
    for rel in data.get("skills", []):
        target = pkg / rel.lstrip("./")
        if not target.is_dir():
            fail(where, f"declared skill directory missing: {rel}")
        elif not (target / "SKILL.md").is_file():
            fail(where, f"skill '{rel}' has no SKILL.md")

    # avatar
    avatar = pkg / str(data.get("avatar", ""))
    if not avatar.is_file():
        fail(where, f"avatar missing: {data.get('avatar')}")
    else:
        size_bytes = avatar.stat().st_size
        if size_bytes > AVATAR_MAX_BYTES:
            fail(where, f"avatar is {size_bytes // 1024} KB, limit is "
                        f"{AVATAR_MAX_BYTES // 1024} KB")
        dims = image_size(avatar)
        if dims is None:
            fail(where, "avatar is not a readable PNG or JPG")
        elif dims != (AVATAR_SIZE, AVATAR_SIZE):
            fail(where, f"avatar is {dims[0]}x{dims[1]}, expected "
                        f"{AVATAR_SIZE}x{AVATAR_SIZE}")

    # extra avatars (team members)
    avatars_dir = pkg / "avatars"
    if avatars_dir.is_dir():
        for img in sorted(avatars_dir.iterdir()):
            if img.is_file() and img.suffix.lower() in (".png", ".jpg", ".jpeg"):
                if img.stat().st_size > AVATAR_MAX_BYTES:
                    fail(where, f"avatar {img.name} exceeds the size limit")
                if image_size(img) != (AVATAR_SIZE, AVATAR_SIZE):
                    fail(where, f"avatar {img.name} is not {AVATAR_SIZE}x{AVATAR_SIZE}")

    say(f"  type={expert_type}  category={category}  "
        f"agents={len(data.get('agents', []))}  skills={len(data.get('skills', []))}  "
        f"desc_zh={len(desc_zh)} chars")
    return data


# ---------------------------------------------------------------------------
# Skill packages
# ---------------------------------------------------------------------------


def check_skill(pkg: Path) -> dict | None:
    where = f"skills/{pkg.name}"
    say(f"\n[skill] {pkg.name}")

    skill_md = pkg / "SKILL.md"
    if not skill_md.is_file():
        fail(where, "missing SKILL.md")
        return None

    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("\ufeff"):
        fail(where, "SKILL.md starts with a UTF-8 BOM")
        text = text.lstrip("\ufeff")

    fm = split_frontmatter(text)
    if fm is None:
        fail(where, "SKILL.md has no YAML frontmatter block")
        return None

    data = check_frontmatter_syntax(where, fm)

    for field in SKILL_REQUIRED:
        if not data.get(field) and field not in ("author",):
            fail(where, f"frontmatter missing required field '{field}'")

    name = str(data.get("name", ""))
    if name and not NAME_RE.match(name):
        fail(where, f"name '{name}' must be lowercase kebab-case")
    if name and name != pkg.name:
        fail(where, f"name '{name}' does not match directory '{pkg.name}'")

    # Directory depth: SKILL.md at level 1, anything else at most level 2.
    depth = max((len(f.relative_to(pkg).parts) for f in pkg.rglob("*") if f.is_file()),
                default=1)
    if depth > SKILL_MAX_DEPTH:
        fail(where, f"contains files {depth} levels deep, only {SKILL_MAX_DEPTH} supported")

    # A skill package must not carry an avatar - avatars are uploaded in the UI.
    if (pkg / "avatars").is_dir():
        fail(where, "skill packages must not contain an avatars/ directory")

    say(f"  display_name={data.get('display_name')!r}  depth={depth}  "
        f"files={sum(1 for f in pkg.rglob('*') if f.is_file())}")
    return data


# ---------------------------------------------------------------------------
# Repository hygiene
# ---------------------------------------------------------------------------


def check_hygiene() -> None:
    say("\n[hygiene] scanning for junk files and identifying information")

    for path in sorted(REPO.rglob("*")):
        if ".git/" in str(path.relative_to(REPO)):
            continue
        if path.name in JUNK_NAMES:
            fail(str(path.relative_to(REPO)), "junk file must not be committed")

    if not BANNED_TERMS:
        note("Private-term scanning skipped: no runtime terms supplied.")

    scanned = 0
    for path in sorted(REPO.rglob("*")):
        rel = path.relative_to(REPO)
        if not path.is_file() or ".git/" in str(rel):
            continue
        if path.suffix.lower() in (".png", ".jpg", ".jpeg", ".zip", ".ico", ".pdf"):
            continue
        # Only content that ships publicly is scanned for identifying information.
        in_content_path = str(rel).startswith(CONTENT_PREFIXES)
        is_root_doc = len(rel.parts) == 1 and path.suffix.lower() == ".md"
        if not (in_content_path or is_root_doc):
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="strict")
        except (OSError, UnicodeDecodeError):
            fail(str(rel), "file is not valid UTF-8 text")
            continue
        scanned += 1
        for term in BANNED_TERMS:
            if term in content:
                fail(str(rel), "contains a restricted term")

    say(f"  scanned {scanned} content files")


def check_archives_for_leaks() -> None:
    """Scan the text entries inside every packaged archive."""
    dist = REPO / "dist"
    if not dist.is_dir():
        return

    scanned = 0
    for archive in sorted(dist.glob("*.zip")):
        rel = f"dist/{archive.name}"
        try:
            with zipfile.ZipFile(archive) as zf:
                for info in zf.infolist():
                    if info.is_dir() or info.file_size > 2_000_000:
                        continue
                    if not info.filename.lower().endswith(CONTENT_SUFFIXES):
                        continue
                    try:
                        text = zf.read(info).decode("utf-8")
                    except (UnicodeDecodeError, OSError):
                        continue
                    scanned += 1
                    for term in BANNED_TERMS:
                        if term in text:
                            fail(rel, f"{info.filename} contains a restricted term")
        except (OSError, zipfile.BadZipFile):
            continue

    say(f"  scanned {scanned} entries inside archives")


def check_dist() -> None:
    dist = REPO / "dist"
    if not dist.is_dir():
        note("dist/ directory not found - skipping archive checks")
        return

    say("\n[dist] verifying packaged archives")
    archives = sorted(dist.glob("*.zip"))
    if not archives:
        note("no archives found in dist/")
        return

    for archive in archives:
        rel = f"dist/{archive.name}"
        try:
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                if bad:
                    fail(rel, f"corrupt entry: {bad}")
                for info in zf.infolist():
                    if not (info.flag_bits & 0x800) and not info.filename.isascii():
                        fail(rel, f"non-UTF-8 filename flag on {info.filename!r}")
                roots = {n.split("/")[0] for n in zf.namelist() if n.strip("/")}
                if len(roots) != 1:
                    fail(rel, f"archive must contain a single top-level folder, found {sorted(roots)}")
        except (OSError, zipfile.BadZipFile) as exc:
            fail(rel, f"unreadable archive: {exc}")
            continue
        say(f"  {archive.name:44s} {len(zipfile.ZipFile(archive).infolist()):3d} entries "
            f"{archive.stat().st_size // 1024:5d} KB")


def check_required_files() -> None:
    say("\n[repo] required community files")
    required = [
        "README.md", "README.en.md", "LICENSE", "CHANGELOG.md",
        "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "CITATION.cff",
        ".gitignore", ".gitattributes", ".editorconfig",
        ".github/PULL_REQUEST_TEMPLATE.md", ".github/workflows/validate.yml",
    ]
    for rel in required:
        if not (REPO / rel).exists():
            fail("repository", f"missing required file: {rel}")
    say(f"  checked {len(required)} files")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> int:
    say("AI Sociology - asset validation")
    say("=" * 62)

    experts_dir = REPO / "experts"
    skills_dir = REPO / "skills"

    expert_count = skill_count = 0

    if experts_dir.is_dir():
        say("\n" + "-" * 62)
        say("EXPERT PACKAGES")
        say("-" * 62)
        for pkg in sorted(p for p in experts_dir.iterdir() if p.is_dir()):
            if check_expert(pkg):
                expert_count += 1
    else:
        fail("repository", "experts/ directory not found")

    if skills_dir.is_dir():
        say("\n" + "-" * 62)
        say("SKILL PACKAGES")
        say("-" * 62)
        for pkg in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            if check_skill(pkg):
                skill_count += 1
    else:
        fail("repository", "skills/ directory not found")

    say("\n" + "-" * 62)
    say("REPOSITORY CHECKS")
    say("-" * 62)
    check_hygiene()
    check_dist()
    check_archives_for_leaks()
    check_required_files()

    say("\n" + "=" * 62)
    if NOTES:
        for item in NOTES:
            say(f"note: {item}")
        say("")
    if PROBLEMS:
        print(f"FAILED - {len(PROBLEMS)} problem(s):\n")
        for item in PROBLEMS:
            print(f"  x {item}")
        print()
        return 1

    print(f"PASSED - {expert_count} expert packages, {skill_count} skill packages, "
          f"no problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
