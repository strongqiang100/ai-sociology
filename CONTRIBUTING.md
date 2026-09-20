# Contributing

Thanks for considering a contribution. This project is a knowledge framework, so contributions are
judged by **whether they improve the reasoning**, not by volume.

- [Code of Conduct](#code-of-conduct)
- [Ways to contribute](#ways-to-contribute)
- [Before you start](#before-you-start)
- [Adding or editing a knowledge module](#adding-or-editing-a-knowledge-module)
- [Editing an expert or skill](#editing-an-expert-or-skill)
- [Validation](#validation)
- [Commit conventions](#commit-conventions)
- [Pull request process](#pull-request-process)

---

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating you agree to
uphold it. Report unacceptable behaviour per the contact in that document.

---

## Ways to contribute

| Direction | What it means |
| :--- | :--- |
| **New situation-oriented modules** | Work sites · city and daily life · language and expression · institutions and rules |
| **Data anchors** | Public figures **with source and year**, replacing "to be verified" placeholders |
| **Bugs in the framework** | Contradictions between modules, broken cross-references, unclear judgements |
| **Translations** | English and other languages |
| **Validation** | Extra checks in `scripts/validate.py` |
| **Documentation** | Clearer explanations, better examples, typo fixes |

---

## Before you start

```bash
git clone https://github.com/<your-name>/ai-sociology.git
cd ai-sociology
python3 --version      # 3.9+
python3 -m pip install pyyaml   # only needed for strict YAML checks
```

Open an issue first for anything larger than a typo fix — it is cheaper to agree on the shape before
writing.

---

## Adding or editing a knowledge module

Modules live under:

```text
experts/ai-sociology/skills/ai-sociology-framework/references/
```

### Required structure

Every module opens with a blockquote tying it back to the main conclusion:

```markdown
# 13 · Education and learning

> **Relation to the main conclusion**: knowledge is getting cheap, but "what I want to know" is not
> getting cheaper. AI can answer your question for you; it cannot ask it for you.
```

Then:

1. One classification or contrast table that separates things people habitually conflate
2. Two or three operational tools (criteria-based, not checklist-based)
3. A table of common misjudgements or failure diagnoses
4. **Hard boundaries** (compliance, psychological, investment, professional domains)
5. A closing line that hooks back to the main line

### Rules

| Rule | Why |
| :--- | :--- |
| **Never skip the opening "relation to the main conclusion"** | Without it the module degenerates into a general-purpose handbook, which is exactly what this project is not |
| **Never present speculation as law** | Mark it `[Assumption]` and give a verification condition |
| **Every forecast needs a falsification condition** | Otherwise it is a position, not a forecast |
| **Every number needs a source and a year** | If you cannot find one, write "to be verified" — **never estimate** |
| **State the boundaries** | The relevant boundary from the README must appear in the module |
| **Do not reduce structural problems to personal effort** | The project's most protected rule |

### Then register it — the step most often missed

```text
1. experts/ai-sociology/skills/ai-sociology-framework/SKILL.md   → add to the navigation table
2. experts/ai-sociology/agents/ai-sociology.md                   → add to the capability list
3. experts/ai-sociology/README.md                                → add to the library listing
4. docs/02-framework.md                                          → add to the overview
```

> **A module written into `references/` but not registered in the navigation table will never be read
> by the AI. The work is wasted.** If you only do one thing, do this.

---

## Editing an expert or skill

### Expert packages

```text
<expert-id>/
├── .codebuddy-plugin/plugin.json   # required fields, see below
├── agents/<expert-id>.md           # frontmatter + body
├── avatars/expert.png              # 512x512, <= 500 KB, PNG or JPG
├── settings.json                   # expert teams only: {"agent": "<lead agent id>"}
└── skills/<skill>/                 # built-in knowledge library
```

`plugin.json` required: `name` (kebab-case, lowercase) · `version` · `author{name,email}` ·
`agents` · `skills` · `expertType` · `agentName` · `displayName{en,zh}` · `profession{en,zh}` ·
`displayDescription{en,zh}` (Chinese 40-50 characters) · `avatar` · `categoryId` ·
`defaultInitPrompt` · `tags` (exactly 3) · `quickPrompts` (exactly 3).

**Expert teams additionally**: `teamInfo{leadAgent,memberAgents}` · `members[]` where **each member
carries both `name` and `displayName`** (the two official sources disagree, so supply both) ·
`profession` must **equal** `displayName`.

### Skill packages

```text
<skill-id>/
├── SKILL.md
├── references/     # optional
├── templates/      # optional
└── scripts/        # optional
```

**Only two directory levels are supported inside a skill package** — `skill/references/x.md` is the
deepest. Frontmatter:

```yaml
---
name: your-skill-name        # lowercase, hyphens only
display_name: AI Sociology · Your Skill
display_name_en: AI Sociology · Your Skill
description: what it does plus the trigger phrases
description_zh: short Chinese summary
description_en: short English summary
version: 1.0.0
author: AI 工作台
disable-model-invocation: false
user-invocable: true
---
```

### The three YAML traps that break uploads

| Trap | Result | Fix |
| :--- | :--- | :--- |
| `name:value` with no space after the colon | Parse failure | Always one space |
| Values wrapped in quotes `"..."` | Very often fails | Do not quote; Chinese punctuation needs none |
| **A colon followed by a space inside a value** (`... end with: a trend`) | `mapping values are not allowed here` | Rewrite as `— that ...` |

`scripts/validate.py` checks all three, but **always back it with a real `yaml.safe_load()` call** —
regex alone misses edge cases.

### Trigger boundaries

If you add a skill in an area already covered, **write mutually exclusive trigger phrases into each
`description`** and add a row to the routing table in the README. Two skills competing for the same
trigger means neither gets used.

---

## Validation

```bash
python3 scripts/validate.py            # all assets
python3 scripts/validate.py --quiet    # exit code only, for CI
```

Everything must be green before a pull request is opened. The same command runs in CI.

---

## Commit conventions

[Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>(<scope>): <subject>

type   feat | fix | docs | refactor | chore | ci | style
scope  framework | expert | skill | docs | ci
```

Examples:

```text
feat(framework): add module 17 on accountability at work sites
fix(skill): remove colon inside frontmatter value in social-strata
docs(expert): register module 16 in the main expert navigation table
```

If a change alters an asset that gets uploaded to the platform, **bump `version` in the package** and
note it in `CHANGELOG.md`.

---

## Pull request process

1. Rebase on the latest `main`
2. Run `python3 scripts/validate.py` — must pass
3. Fill in the pull request template
4. Keep one logical change per pull request

Reviewers check, in order:

- Does it improve the reasoning, or only add volume?
- Does it open with a relation to the main conclusion?
- Are facts, mechanisms, quotes and assumptions clearly separated?
- Are the boundaries carried along?
- Is it registered in every navigation table?
- Is it de-identified?

### De-identification checklist

Public builds must not contain:

- [ ] Real names, or company names in Chinese or English
- [ ] Employment history or employer names
- [ ] Local absolute paths
- [ ] Internal document names or private links
- [ ] Client, channel or pricing information
- [ ] Regional identifiers that narrow down a specific person

---

## Questions

Open a [discussion or issue](https://github.com/strongqiang100/ai-sociology/issues).
