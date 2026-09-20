# 06 · Install

[← Skills](05-skills.md) · [Documentation index](README.md) · [Next: FAQ →](07-faq.md)

---

## Before you start

Nothing here needs installing to be read. **Installation is for convenience.** If you only want the
reasoning, read [02 · The framework](02-framework.md).

Two asset types, **two different entry points**. Getting this wrong is the most common cause of
confusion:

| Asset | Entry point |
| :--- | :--- |
| Expert / Expert team | Release Management → **Experts** |
| Skill | Release Management → **Skills** |

Both need a one-off developer registration first. Personal accounts can publish experts, expert teams,
skills and connectors — **Buddy applications require a corporate account.**

---

## Option 1 · Download a packaged archive

Every installable asset is in [`../dist/`](../dist/).

```bash
curl -LO https://github.com/strongqiang100/ai-sociology/releases/latest/download/ai-sociology.zip
```

| Archive | Type |
| :--- | :--- |
| `ai-sociology.zip` | Main expert |
| `ai-sociology-roundtable.zip` | Expert team (1 lead + 6 members) |
| `ai-sociology-variables.zip` | The Variable Bureau |
| `ai-sociology-jobs.zip` | The Job Splitter |
| `ai-sociology-learn.zip` | The Right Question |
| `ai-sociology-verify.zip` | The Verifier |
| `ai-sociology-forecast.zip` | Two Years Out |
| `ai-sociology-attention.zip` | The Rememberer |
| `ai-sociology-variable-audit.zip` | Skill · Variable Audit |
| `ai-sociology-human-position.zip` | Skill · Where Humans Stand |
| `ai-sociology-human-nature.zip` | Skill · Human Constants |
| `ai-sociology-social-strata.zip` | Skill · Social Stratification |
| `ai-sociology-anxiety-decomp.zip` | Skill · Anxiety Decomposition |
| `ai-sociology-role-scan.zip` | Skill · Role Scan |

### Uploading

**Expert or expert team** — `Release Management → Experts → Create`, then drop the zip in.

> **For an expert team choose "Create Expert Team"**, not "Create Expert". On the open platform both
> share one entry point: the platform reads `expertType` from inside the package.

**Skill** — `Release Management → Skills → Create`, then drop the zip in.

---

## Option 2 · Use the source tree directly

`experts/` and `skills/` contain complete, installable sources. Copy a directory into your client's
asset folder:

```bash
git clone https://github.com/strongqiang100/ai-sociology.git
cp -r ai-sociology/experts/ai-sociology             <client-assets>/experts/
cp -r ai-sociology/skills/ai-sociology-variable-audit <client-assets>/skills/
```

---

## Step 3 · Configure on the platform

Three fields are configured **in the UI, not in the package**:

| Field | Notes |
| :--- | :--- |
| **Avatar** | 512×512, ≤ 500 KB, JPG or PNG. **Uploaded in the UI for skills** — a skill package has no `avatars/` directory |
| **Category (类目)** | **Required.** This is why the packages deliberately omit a `category` field — the enum is not published, and a wrong value fails parsing |
| **Marketplace display tags** | Skills accept 1–3; pick the closest 2 |

> **Skills and experts handle avatars differently, and this causes real confusion:**
>
> | | Expert | Skill |
> | :--- | :--- | :--- |
> | Where the avatar comes from | **Parsed from the package** (`avatars/expert.png`) | **Uploaded in the UI** |
> | Editable on the page | **No** — read-only preview | **Yes** — the field literally says "re-upload" |
>
> To change an expert's avatar you must re-upload the whole package. To change a skill's avatar you
> just upload the new image.

---

## Validation before you upload

```bash
python3 scripts/validate.py
```

This checks structure, fields, YAML parseability, naming, directory depth, filename encoding, archive
integrity and de-identification. **Run it before opening a pull request and before uploading.**

---

## Troubleshooting

### "The zip does not parse" / "name mismatch"

**The most common real cause: the package was uploaded into a pre-existing asset.**

**Each asset binds to the `name` inside its package at creation time.** If you previously created an
asset for `ai-sociology` and later upload a package whose `name` is `ai-sociology-roundtable` into
that same asset, it fails.

**Fix**: create a **new** asset. Do not edit an old one.

### The error message is a list of missing items

The platform reports missing fields item by item, and there is a **copy button** in the top right of
the error panel.

**Get the exact text before changing anything.** Guessing at a fix is more expensive than waiting for
one precise error message.

| Error mentions | Likely cause | Fix |
| :--- | :--- | :--- |
| `name` mismatch | Uploaded into a stale asset | Create a new asset |
| `missing xxx` / `invalid` / format | Field not compliant | Fix per the message, rebuild |
| `already exists` | Duplicate identifier or version | Bump `version` in `plugin.json`, or change the identifier |
| avatar | Size, dimensions or format | 512×512, ≤ 500 KB, PNG or JPG |
| `mapping values are not allowed here` | A colon followed by a space inside a YAML value | Rewrite the value without the colon |
| parse failure with quotes | Values wrapped in `"..."` | Remove the quotes |

### "Version already exists"

Bump `version` in the package's `plugin.json` (or `SKILL.md` frontmatter) by one — `1.0.0` → `1.0.1` —
and re-upload.

### "The category is required"

That is a UI field. Set it on the submission page; it is not in the package.

### Discrepancies in the official specification

Two places where the official documentation and the official template disagree. **Supply both and you
are safe either way:**

| Field | Documentation says | Template shows |
| :--- | :--- | :--- |
| Member name inside `members[]` | `name` | `displayName` |
| `author` | `{name, email}` | `{name, email}` — but packages with **only** `name` may fail |

`experts/ai-sociology-roundtable` ships with **both** `name` and `displayName` on every member, and
`author.email` on every package, for exactly this reason.

### Downloading the reference template

The fastest way to locate a parsing problem is to diff against the official template rather than read
the documentation:

```bash
curl -sL -o design-experts.zip \
  "https://codebuddy-platform-1258344699.cos.ap-beijing.myqcloud.com/open/static/files/design-experts.zip"
```

Note that the template itself contains a few errors (a wrong `categoryId` value, reversed `en`/`zh`
values). Use it to compare **structure**, not to copy values.

### What is *not* the cause

Verified by comparison with the official template — do not waste time here:

- **Zip root structure**: the official template also nests everything inside one top-level folder
- **Chinese filenames**: the official template contains them too, and even ships `__MACOSX/` and
  `.DS_Store`
- **Archive size**: the limit is 20 MB; the largest package here is ~2.2 MB

---

## Editing an asset after it is live

| Field | Changeable after release? |
| :--- | :--- |
| Expert ID | No — system generated |
| **Expert identifier (`name`)** | **No — locked at release.** Changing it requires creating a new expert |
| Display name, profession, description, tags, quick prompts | Yes |
| Avatar, version, introduction | Yes — re-upload the package |
| Marketplace tags, category | Yes — on the submission page |
| **Payment model (free / one-off / monthly)** | **No — locked at release** |

**Updating is not the same as recreating.** Expert ID, identifier and accumulated install count are
preserved across an update.

---

[← Skills](05-skills.md) · [Documentation index](README.md) · [Next: FAQ →](07-faq.md)
