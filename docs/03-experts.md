# 03 · Experts

[← The framework](02-framework.md) · [Documentation index](README.md) · [Next: The roundtable →](04-roundtable.md)

---

## What an expert is

An **expert** is a package that gives the AI a stable role: an identity, a fixed scope, a body of
knowledge and a set of hard boundaries. You summon it, and it answers *as that role*.

Two field types do the work:

| Field | Job |
| :--- | :--- |
| **Display name** (花名) | Gets remembered. Short and distinctive. |
| **Profession** (职称) | Gets found. Descriptive, and carries the series prefix. |

Every expert here uses the series prefix `AI Sociology ·` in its profession field, which does three
things at once: it picks up the series search term, forms a recognisable family, and routes users
toward the main expert from the card itself.

---

## The eight assets

| Asset | Identifier | Type | Best for |
| :--- | :--- | :--- | :--- |
| **AI Sociology** | `ai-sociology` | Expert | The full system. Use when the question is broad or you need the reasoning chain |
| **AI Sociology Roundtable** | `ai-sociology-roundtable` | Expert Team | Hard questions needing several angles at once |
| **The Variable Bureau** | `ai-sociology-variables` | Expert | "Will this happen?" "Is it too late to start?" |
| **The Job Splitter** | `ai-sociology-jobs` | Expert | "Is my job safe?" "Should I change careers?" |
| **The Right Question** | `ai-sociology-learn` | Expert | "I keep stalling while learning." "What should I practise?" |
| **The Verifier** | `ai-sociology-verify` | Expert | "Is this claim worth believing?" |
| **Two Years Out** | `ai-sociology-forecast` | Expert | "What should I believe about the next two years?" |
| **The Rememberer** | `ai-sociology-attention` | Expert | "Why does good content leave no trace?" |

### Choosing between them

```text
Will this happen?            -> The Variable Bureau
Is my job safe?              -> The Job Splitter
What should I learn?         -> The Right Question
Can I trust this claim?      -> The Verifier
What should I believe?       -> Two Years Out
Why was it not remembered?   -> The Rememberer
Several of the above at once -> The Roundtable
Something philosophical      -> AI Sociology (main)
```

---

## The main expert · AI Sociology

`experts/ai-sociology`

The only asset carrying the complete 16-module library. Everything else in this repository is a
narrower cut of it.

**Capability list**

1. Variable mapping and trend assessment
2. Falsifiable forecasting
3. Career and skill judgement
4. Structural and social reasoning
5. Anxiety decomposition
6. Extension modules (11), each hooked back to the main line
7. Expression and topic generation

**Use it when** the question is philosophical, spans several domains, or needs the derivation rather
than the conclusion.

> **One internal rule it enforces**: never jump a level. Variable mapping is step one, axiom
> derivation is step two. Skipping to a conclusion is how industry facts get mistaken for social
> insight.

---

## The six sub-experts

Each handles **one question**, and the scopes are deliberately non-overlapping. Overlap is fatal here:
if two experts answer the same question, a user does not know which to install, and both lose.

### The Variable Bureau · `ai-sociology-variables`

*"I do not give conclusions. I map variables."*

Takes a judgement-shaped question and decomposes it into a trackable checklist, marking what is known,
what is unknown, and which variable is actually binding.

**Core tools**: the eight questions · the three slow-down questions · the variable-list technique for
judging someone else's forecast · rewriting "will it happen" into something monthly-checkable.

**Boundary**: no investment advice; no specific years; never uses *disrupt*, *inevitable* or
*only a matter of time*.

### The Job Splitter · `ai-sociology-jobs`

*"AI does not cut your job. It splits it."*

Takes a job down to task level and shows which tasks go first and which get more valuable.

**Core tools**: the three layers (task / relationship / accountability) · the screen-inside-outside
impact order · the accountability-loop audit · three skill-safety questions · three transition routes.

**Boundary**: no career-safety promises; never reduces structural shock to insufficient effort; always
names what gets *more* valuable, not only what is at risk.

### The Right Question · `ai-sociology-learn`

*"Answers get cheaper. Questions get dearer."*

Diagnoses where a learner is actually stuck and converts a vague "I don't get it" into a precise
location.

**Core tools**: three-layer diagnosis (knowledge / skill / judgement) · four-way error attribution
that forbids "careless" · three levels of question rewriting · the four-stage learning route.

**Boundary**: does not replace professional teaching judgement; promises no speed; does not turn
resource gaps into personal failings.

### The Verifier · `ai-sociology-verify`

*"Is what you believe something you saw, or something you heard?"*

Six-step verification and an evidence grade for every conclusion. Note what it does *not* do: it does
not split claims into true and false. Most claims are not false — they are simply not qualified to be
cited.

**Core tools**: the six steps (who said it / fact or judgement / where is the primary source / what
does the number count / look for counterexamples / who is harmed if it is wrong) · five distortion
families · three questions about a number · four-level evidence grading.

**Boundary**: "cannot verify" is not "false" — it can only be downgraded. No professional conclusions
in medicine, law or investment.

### Two Years Out · `ai-sociology-forecast`

*"Judgements written for you two years from now."*

Every forecast ships with a criterion, a time horizon and an explicit way to be wrong. A forecast
without a falsification condition is a position, not a forecast.

**Core tools**: the falsification quartet · four-level material separation · two distinct time
horizons (24 months for role change, 3–7 years for structural change) · the four traits that mark a
topic as story rather than fact · forecast post-mortems.

**Boundary**: not investment advice, carried on every output. No accuracy promises. No political
forecasting.

### The Rememberer · `ai-sociology-attention`

*"Impressive, but you cannot recall a single shot."*

Structural judgement of content and attention. It does not teach growth tactics — it explains why
something impressive can still leave no trace.

**Core tools**: the three non-properties of attention · three simultaneous effects of aesthetic
inflation · the line where judgement gets outsourced · where saved time actually goes · three criteria
for keeping friction.

**Boundary**: promises no traffic; writes no moral exhortation (*"just use your phone less"* is a
failed construction — it turns a mechanism problem into a willpower problem); makes no psychological
diagnosis.

---

## The series pattern

These six are **spinoffs of one IP**, not six unrelated products. Three design rules make that work:

1. **Names come from the framework's own lines**, not from generic job titles. *The Variable Bureau*
   comes from "the future is not an opinion, it is variables". Generic titles can be copied; a line
   from the framework cannot.
2. **The profession field carries the series prefix**, forming a family and routing to the main expert.
3. **Each agent states its place in the series** in its own body text, and points to the main expert
   for the full derivation.

---

## Installing

See [06 · Install](06-install.md).

---

[← The framework](02-framework.md) · [Documentation index](README.md) · [Next: The roundtable →](04-roundtable.md)
