<div align="center">

# AI Sociology

**Watch where AI is moving. Find where humans stand.**

An open-source reasoning framework and agent-asset library about the human position under AI
<br>16 knowledge modules · 8 experts & expert teams · 6 installable skills

[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-111?style=flat-square)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/Platform-WorkBuddy-7c3aed?style=flat-square)](https://open.workbuddy.cn)
[![Experts](https://img.shields.io/badge/Experts-8-0ea5e9?style=flat-square)](docs/03-experts.md)
[![Skills](https://img.shields.io/badge/Skills-6-f59e0b?style=flat-square)](docs/05-skills.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff69b4?style=flat-square)](CONTRIBUTING.md)

[中文文档](README.md) ·
[Getting Started](#getting-started) ·
[Assets](#assets) ·
[Framework](#the-framework) ·
[Boundaries](#boundaries-and-disclaimer) ·
[License](#license)

</div>

---

## Table of Contents

- [What this is](#what-this-is)
- [What this is not](#what-this-is-not)
- [Core conclusion](#core-conclusion)
- [Getting Started](#getting-started)
- [Assets](#assets)
- [The Framework](#the-framework)
- [Repository Layout](#repository-layout)
- [Design Principles](#design-principles)
- [Boundaries and Disclaimer](#boundaries-and-disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## What this is

**An open-source project that delivers a method of judgement rather than a set of conclusions.**

Most AI content hands you answers: what will blow up, what will be replaced, which tool you must install.
This project does the opposite — it does not forecast outcomes. It delivers **a method for asking the
right question**, together with installable assets that carry that method.

Three layers:

| Layer | Content | Form |
| :--- | :--- | :--- |
| **Method** | 16 reasoning modules (axioms, theorems, variable mapping, structural judgement) | Markdown |
| **Role** | 8 experts / expert teams, each handling exactly one angle | Installable agent packages |
| **Tool** | 6 skills, auto-invoked inside any conversation | Installable skill packages |

The three layers have different durability. The method layer can be copied, the role layer can be
replaced — **only the judgement itself cannot be taken from you.** So the method layer is open-sourced
in full: the text can be copied, the judgement cannot.

> As generation costs approach zero, what becomes scarce is not content —
> it is **the one line worth repeating**. And more fundamentally:
> **as answers get cheaper, questions get more expensive.**

---

## What this is not

This section matters more than the previous one. **Drawing hard boundaries is what keeps this project
from becoming the thing it argues against.**

| It is not | Why |
| :--- | :--- |
| **Not a fact-checker** | It does not split claims into true / false. It judges **whether something is a fact or a story, and what it means for whom** |
| **Not investment advice** | The industry and compute material is a research frame only, **with no judgement on any instrument** |
| **Not therapy or diagnosis** | On persistent insomnia, impaired functioning or self-harm ideation, it **explicitly refers to professional help** |
| **Not growth hacking** | The content modules discuss what deserves to be remembered, **not how to go viral** |
| **Not résumé coaching** | Structural career judgement only, no CV polishing or interview coaching |
| **Sells neither comfort nor fear** | The two look opposite but **both strip people of the ability to act** |

> The last point is the project's central rule. Every output follows the same posture:
> **acknowledge the risk is real, and point out it has boundaries, variables and actionable parts.**

---

## Core conclusion

Two axioms, everything else derived.

| Axiom | Statement | What it yields |
| :--- | :--- | :--- |
| **A1 · Attention is finite** | Attention cannot be copied, parallelised or stored | Supply grows faster than filtering → the bottleneck moves from production to selection |
| **A2 · Objectives diverge** | "It understands me" is not "it acts for me" | Capability improves; **alignment with your interests does not improve automatically** |

> **AI's capability will keep improving. Whether it aligns with your interests will not improve
> automatically alongside it.**

Three immediately usable judgements follow:

| Judgement | One line |
| :--- | :--- |
| **Objective quality** | A system can be perfectly obedient and extremely capable, yet if the objective it is asked to pursue is impoverished, it will still push the future toward impoverishment. This matters far more than "will AI rebel" |
| **Two kinds of dignity** | **Competence dignity** (I am better than others) is compressed; **positional dignity** (nothing works without me) is raised — opposite directions |
| **Accountability cannot transfer** | You cannot fire it, punish it or make it pay. So **no matter how well AI writes, someone still has to sign. Whoever signs, gains value** |

Four standing formulations used across all assets:

```text
On-site work        Late is not never — only delayed
Structural hardship It is a speed problem, not your problem
Industry structure  Slow is not never; "physics has limits" must not be used as comfort
Occupation          What gets replaced is "work that can be fully written down", not "low-end work"
```

---

## Getting Started

### Option 1 — Install directly

Download a package from [`dist/`](dist/) and import it into your AI client.

```bash
curl -LO https://github.com/strongqiang100/ai-sociology/releases/latest/download/ai-sociology.zip
```

**Experts / Teams** — open the Expert Center, choose "My Experts", then create (for a team, choose
"Create Expert Team"); or sign in to the open platform and upload the zip under
`Release Management → Experts → Create`.

**Skills** — `Release Management → Skills → Create`, then configure the avatar, category and display
tags on the page.

> Each asset binds to the `name` inside its package at creation time.
> **Never upload a new package into a pre-existing asset.**

### Option 2 — Clone the source

```bash
git clone https://github.com/strongqiang100/ai-sociology.git
cd ai-sociology
```

`experts/` and `skills/` contain **complete, installable asset sources**.

### Option 3 — Read only

Nothing needs installing — all 16 modules are plain Markdown:

```bash
open docs/02-framework.md
ls experts/ai-sociology/skills/ai-sociology-framework/references/
```

### Local validation

```bash
python3 scripts/validate.py
```

Checks package structure, required fields, YAML parseability, naming rules, directory depth,
filename encoding and archive integrity.

---

## Assets

### Experts & expert teams (8)

| Asset | Identifier | Type | Positioning |
| :--- | :--- | :--- | :--- |
| **AI Sociology** | `ai-sociology` | Expert | The full system, 16 knowledge modules |
| **AI Sociology Roundtable** | `ai-sociology-roundtable` | **Expert Team** | Six disciplinary seats deliberate in stages; one lead assembles a single verdict |
| The Variable Bureau | `ai-sociology-variables` | Expert | Decomposes an AI claim into a trackable variable checklist |
| The Job Splitter | `ai-sociology-jobs` | Expert | Splits a job to task level and shows what goes first |
| The Right Question | `ai-sociology-learn` | Expert | Learning diagnosis and question-training for the AI era |
| The Verifier | `ai-sociology-verify` | Expert | Six-step verification with evidence grading |
| Two Years Out | `ai-sociology-forecast` | Expert | Every forecast carries a criterion, a horizon and a way to be wrong |
| The Rememberer | `ai-sociology-attention` | Expert | Structural judgement of attention and content |

<details>
<summary><b>The roundtable's 7 agents</b></summary>

<br>

| Name | Seat | Owns only | Never does |
| :--- | :--- | :--- | :--- |
| **He Zhiyan** (lead) | Chief Editor of the Roundtable | Routing, orchestration, assembling one line | Never writes a member's output for them |
| **Zhen Ben Zhen** | Philosophy & the Ground of the Human | Separating capability / sentience / purpose; two dignities; two reasons | Gives no life answers, rules on no consciousness |
| **Guan Zhi Ren** | Human Nature & the Structure of Desire | The constants: desire, comparison, shame, inertia | Judges no individual, preaches no morality |
| **Ren Zhong Zhi** | Occupational Structure & Accountability | Three layers plus a four-dimension score | No CV work, no judging named employers |
| **Jiang Guan Lan** | Social Trends & Stratification | Stratification, trust, community, generations | No political forecast, no regional comparison |
| **Ning Huai An** | Decomposing AI Anxiety | Four-anxiety separation plus a two-column list | No psychological diagnosis |
| **Qin You Jiang** | Physical Limits & the Pace of AI | The physical chain; fact versus story | No investment advice |

**Five preset workflows**: *Will I be replaced* · *I am anxious* · *What does this actually mean* ·
*What should I learn* · *Is this claim trustworthy*

</details>

### Skills (6)

A skill is **a method package that teaches the AI how to proceed** — auto-invoked in any conversation.

| Skill | Identifier | Triggers on |
| :--- | :--- | :--- |
| **Variable Audit** | `ai-sociology-variable-audit` | Will something happen? Is it worth it? |
| **Where Humans Stand** | `ai-sociology-human-position` | What is human worth? Where do I go? |
| **Human Constants** | `ai-sociology-human-nature` | Why do people behave this way? |
| **Social Stratification** | `ai-sociology-social-strata` | What happens to my generation? |
| **Anxiety Decomposition** | `ai-sociology-anxiety-decomp` | I am anxious / I am afraid |
| **Role Scan** | `ai-sociology-role-scan` | How safe is my job? |

**When one message contains several, the order is:**

```text
structure (stratification / role) → mechanism (human nature) → feeling (anxiety) → philosophy (position)
```

Handling the feeling first reads as being brushed off.

---

## The Framework

### Core modules (5)

| # | Module | Content |
| :--- | :--- | :--- |
| 01 | Axioms, theorems and the reasoning chain | Two axioms, four axioms, five theorems, physical constraint chain, two time horizons |
| 02 | The eight-question variable checklist | Checklist, variable mapping, three slow-down questions |
| 03 | Expression and topic standards | Four stances, structure, language rules, hook library |
| 04 | Evidence grading and citation boundaries | Four-level grading, citation discipline, data anchors |
| 05 | Practitioner profile | Usable phrasing, plain-language glossary |

### Extension modules (11)

<details>
<summary><b>Tool-oriented, 7 modules — "how to use"</b></summary>

<br>

| # | Module | Focus |
| :--- | :--- | :--- |
| 06 | Tools and workflows | Six questions, full cost including exit cost, three-attribute process split |
| 07 | Content and copy | Closing line, second-by-second structure, hook types, topic scoring |
| 08 | Video production | Pipeline, quality gate, prompt-block method, degradation path |
| 09 | Cross-border and industry | Four-stage sector reading, evidence chain, five-part benchmark card |
| 10 | Growth and training | 90-day cold start, platform differences, sales drills |
| 11 | Diagnosis and knowledge management | Four structural questions, three scaling preconditions |
| 12 | Industry and investment observation | Physical ceiling chain, three walls, bottleneck migration, topic constitution |

</details>

<details open>
<summary><b>Situation-oriented, 4 modules — "what has changed for people" (closer to this project's long-term theme)</b></summary>

<br>

| # | Module | Focus |
| :--- | :--- | :--- |
| 13 | Education and learning | Knowledge / skill / judgement, four-stage route, four-way error attribution |
| 14 | Relationships and reality | Risk-free relationships, memory personas, digital doubles; supply · cost · responsibility |
| 15 | Attention and judgement | Three non-properties of attention, aesthetic inflation, outsourced judgement |
| 16 | Evidence and facts | Six-step verification, five distortion families, three questions about a number |

</details>

### Templates (5)

`Trend briefing` · `Variable checklist` · `Topic and script card` · `Claim verification sheet` · `Learning diagnosis card`

---

## Repository Layout

```text
ai-sociology/
├── README.md / README.en.md
├── LICENSE  CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md  SECURITY.md  CITATION.cff
├── .github/                     # issue templates, PR template, CI validation
├── assets/avatar.png
├── docs/                        # 9 documents
├── experts/                     # 8 expert packages (installable sources)
├── skills/                      # 6 skill packages (installable sources)
├── scripts/validate.py
└── dist/                        # packaged archives, ready to install
```

### Inside the two package types

```text
Expert package (Agent)                  Skill package (Skill)
ai-sociology/                           ai-sociology-variable-audit/
├── .codebuddy-plugin/plugin.json       ├── SKILL.md
├── agents/ai-sociology.md              ├── references/
├── avatars/expert.png                  ├── templates/
├── settings.json   # teams only        └── scripts/
└── skills/         # built-in library
    └── ai-sociology-framework/
```

---

## Design Principles

**1. Every module must hook back to the main line.**
Before delivering anything from a module, answer: *what has this changed for ordinary people?*
If you cannot, it has drifted — it degenerates into a general-purpose handbook,
**and this framework's value is precisely not as a tool.**

**2. Give paths, not conclusions.** Conclusions expire and leave the user unable to judge next time.

**3. Always give falsification conditions.** A forecast without "how I would be proven wrong" is a
position, not a forecast.

**4. Always give both the cost and the actionable part.**

```text
Cost only       → sells fear, removes hope
Actions only    → cheap comfort, removes alertness
Both together   → a complete delivery
```

**5. Never reduce a structural problem to personal effort.** The most protected rule here.

**6. A structural trend is not a personal fate.** Say it every time, or the analysis becomes fatalism.

**7. Depth comes from enforced division of labour**, not from everyone saying a little about everything.

---

## Boundaries and Disclaimer

The following boundaries **must be carried along** whenever these assets are used:

| Situation | Boundary |
| :--- | :--- |
| Money decisions | **Not investment advice.** Consult a licensed professional |
| Persistent insomnia, impaired functioning, self-harm ideation | **Seek professional help.** This content does not replace counselling or medical care. This rule outranks any analysis |
| Politics, institutions, regions | No political forecast, no regional comparison |
| Medical, legal | Information quality only, no professional conclusion |
| Life choices | **Does not decide for the user** — it offers structure, not the choice |
| Outcomes | **Promises nothing.** Mechanisms yes, guarantees no |

**On attribution**: all packages are public-release builds signed with a neutral author name. They
contain no real names, company information, employment history, local paths, internal document names,
private links, or client and channel information.

> **On the project avatar**: `assets/avatar.png` is a portrait also used inside the expert packages as a
> unified visual identity. If you fork this project, replace it with your own image — it is a person's
> likeness and is **not** covered by the project licence.

---

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

```bash
git clone https://github.com/<your-name>/ai-sociology.git && cd ai-sociology
python3 scripts/validate.py
git checkout -b feat/your-change
```

**Before you open a PR:**

- [ ] `python3 scripts/validate.py` passes fully
- [ ] New modules are registered in `docs/02-framework.md` **and** in the relevant `SKILL.md` navigation table
- [ ] New module opens with a "relation to the main conclusion" section
- [ ] Nothing speculative is packaged as a law; forecasts carry falsification conditions
- [ ] No real names, companies, clients or channels introduced

**The most commonly missed step**: writing a module into `references/` without registering it in the
navigation table — the AI will never read it, **so the work is wasted.**

---

## License

Released under the [MIT License](LICENSE).

```text
Copyright (c) 2026 AI Sociology
```

> **One request (not a licence term)**: the value here is the method, not the conclusions.
> If you use it to reach better judgement, that is its purpose.
> **If it gets repackaged as a certain answer and sold, that runs the other way.**

---

<div align="center">

**Watch where AI is moving. Find where humans stand.**

<sub>A star is the most concrete way to support this if it was useful.</sub>

</div>
