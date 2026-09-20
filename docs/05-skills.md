# 05 · Skills

[← The roundtable](04-roundtable.md) · [Documentation index](README.md) · [Next: Install →](06-install.md)

---

## Skills are not experts

This is the distinction people most often miss.

| | Expert / Expert team | **Skill** |
| :--- | :--- | :--- |
| Form | A role with an identity (an agent package) | **A method package that teaches the AI how to proceed** |
| Structure | `plugin.json` + `agents/` + `avatars/` | **`SKILL.md`** + `references/` + `templates/` |
| Who invokes it | The user summons the role | **The AI triggers it automatically**, or the user calls it |
| Nature | A persona | **A work instruction** |
| Entry point | Release Management → Experts | **Release Management → Skills** |

So skills contain **no persona and no avatar in the package** — only procedure.

---

## The six skills

| Skill | Identifier | Triggers on | Files |
| :--- | :--- | :--- | :--- |
| **Variable Audit** | `ai-sociology-variable-audit` | Will something happen? Is it worth it? | 5 |
| **Where Humans Stand** | `ai-sociology-human-position` | What is human worth? Where do I go? | 4 |
| **Human Constants** | `ai-sociology-human-nature` | Why do people behave this way? | 4 |
| **Social Stratification** | `ai-sociology-social-strata` | What happens to my generation? | 4 |
| **Anxiety Decomposition** | `ai-sociology-anxiety-decomp` | I am anxious / I am afraid | 4 |
| **Role Scan** | `ai-sociology-role-scan` | How safe is my job? | 4 |

The last three map one-to-one onto roundtable seats (Zhen Ben Zhen, Guan Zhi Ren, Jiang Guan Lan).
**Skills and experts are two delivery forms of the same framework** — one can be summoned, the other
runs automatically inside any conversation.

---

## Trigger boundaries

All six are about AI, so **without explicit boundaries they would compete for the same trigger**.
Each `description` therefore carries mutually exclusive trigger phrases.

| The user is asking | Triggers |
| :--- | :--- |
| Will something **happen** | Variable Audit |
| What **value** humans still have | Where Humans Stand |
| **Why** people behave this way | Human Constants |
| What happens to **my generation** | Social Stratification |
| **I feel bad** | Anxiety Decomposition |
| **How safe is my job** | Role Scan |

**When one message contains several, the order is:**

```text
structure (stratification / role scan) -> mechanism (human constants)
  -> feeling (anxiety) -> philosophy (where humans stand)
```

Handling the feeling first reads as being brushed off.

---

## What each skill actually does

### Variable Audit

Five steps. The two that carry the value are **normalising the question** (separating fact, condition
and value judgement, because most people fuse all three into one sentence) and **naming exactly one
bottleneck** (eight bottlenecks of equal importance means no bottleneck).

Then: signals to watch, and a falsification condition.

### Where Humans Stand

Three separations:

1. **Capability / sentience / purpose** — only the first can be answered by technology, and the third
   decides whether it acts *for you* or *for someone else*. Its sharpest corollary: a system can be
   perfectly obedient and extremely capable, and still push the future toward impoverishment if the
   objective it was given is impoverished. This matters far more than "will AI rebel".
2. **Two dignities** — competence dignity is compressed, positional dignity is raised.
3. **Two reasons** — instrumental (how, getting cheap) versus value (what for, getting dear).

**Hard constraint**: it gives no life answers, only a sharper question. Giving an answer would violate
its own first corollary — meaning is *chosen*, not produced.

### Human Constants

Four constants that shift the question from moral judgement to structural judgement:

1. **Two kinds of desire** — functional desires satiate; social desires never do. AI serves the first
   efficiently and the second barely at all.
2. **Comparison is zero-sum** — absolute levels rise hugely, relative position barely moves. Hence
   "everything got cheaper and I am more tired".
3. **Inertia is a friction structure, not a moral defect** — moral explanations lead to preaching and
   fail; structural explanations lead to design and work.
4. **Shame is not anxiety** — anxiety responds to increased control; shame only responds to
   de-shaming. Using "learn more skills" on shame makes it worse.

**Boundary**: de-shaming applies **only** to structural situations. Applied to a self-inflicted
problem it does harm.

### Social Stratification

Four structural lines: the basis of stratification is shifting toward *how much intelligence you can
mobilise* (and that loop is self-reinforcing) · trust has passed through three objects, and
unverifiable trust is more dangerous than distrust · occupational communities are dissolving, and what
replaces them lacks the compulsion that produced belonging · the 3–10 years of experience cohort is
the hardest position of all.

**Hard requirement**: it always closes with **"this is a structural trend, not a personal fate."**
Without that line the analysis becomes fatalism.

### Anxiety Decomposition

Separates four anxieties that get compressed into one lump, each needing a completely different fix.
See [01 · Getting started](01-getting-started.md#key-concepts).

**Two-column rule**: a complete delivery must contain both a watch-list (3–5 signals) and an action
list (**exactly one thing**, this week). Watch-list alone makes anxiety worse; action list alone
produces busywork.

**Two forbidden registers**: selling anxiety ("you have already been left behind") removes hope;
cheap comfort ("don't worry, AI is just a tool") removes alertness. They look opposite and both remove
the ability to act.

### Role Scan

Three layers plus four dimensions, and the most valuable output is spotting the **false-safe zone**:
high on-site presence but low on everything else. It looks safe and is the most exposed, because
slowness gets misread as immunity.

**Must always include** the part that gets *more* valuable, not only what is at risk. Danger alone is
anxiety-selling.

---

## Skill package specification

### Structure

```text
<skill-id>/
├── SKILL.md          # required: procedure, triggers, output rules, boundaries
├── references/       # optional: domain knowledge
├── templates/        # optional: fill-in sheets
└── scripts/          # optional: executable helpers
```

**Only two directory levels are supported** — `<skill-id>/references/file.md` is the deepest. Do not
nest further.

### Frontmatter

```yaml
---
name: your-skill-name
display_name: AI Sociology · Your Skill
display_name_en: AI Sociology · Your Skill
description: what it does, plus the trigger phrases
description_zh: short Chinese summary
description_en: short English summary
version: 1.0.0
author: AI 工作台
disable-model-invocation: false
user-invocable: true
---
```

### The three YAML traps that break uploads

| Trap | Result |
| :--- | :--- |
| `name:value` — no space after the colon | Parse failure |
| Values wrapped in `"..."` | Very often fails; Chinese punctuation needs no quotes |
| **A colon followed by a space inside a value** | `mapping values are not allowed here` |

The third one is real: it was hit during this project's own build, caught only because validation
included an actual `yaml.safe_load()` call. Regex alone missed it.

### SKILL.md should carry procedure, not content

Put the trigger conditions, the steps, the output rules and the boundaries in `SKILL.md` (aim for
3–6 KB). Put the domain knowledge in `references/` and the fill-in sheets in `templates/`.

> **Counter-example**: one published skill put 70,000 characters into `SKILL.md` alone. Every trigger
> loaded 70 KB of context; conversations that could have run 20 turns blew up in 5.

---

## Writing rules that apply to every skill

- **No persona.** Skills are procedure; leave personality to the experts.
- **Trigger phrases must be mutually exclusive** across skills.
- **Hard boundaries travel with the skill.** Investment, psychological and medical boundaries are not
  optional footnotes.
- **Never promise an outcome.** Skills deliver method.
- **State what the skill does not do.** Every skill here has an explicit "never does" list.

---

[← The roundtable](04-roundtable.md) · [Documentation index](README.md) · [Next: Install →](06-install.md)
