# 02 · The framework

**Version scope:** This page describes the historical 1.0.0 applied modules. The [research edition](../theory/README.md) supersedes their unconditional theoretical formulations for new research. Its [compatibility notes](../theory/05-research-protocol.en.md) distinguish constraints, hypotheses and normative claims; research paths need not return to a fixed conclusion.

[← Getting started](01-getting-started.md) · [Documentation index](README.md) · [Next: Experts →](03-experts.md)

---

## Structure of a module

Every module follows the same shape, and the shape is load-bearing.

```text
1. Relation to the main conclusion   <- a blockquote. Never omitted.
2. One classification or contrast table  <- separates what people conflate
3. Two or three operational tools     <- criteria-based, not checklists
4. A table of common misjudgements    <- what goes wrong, and the fix
5. Hard boundaries                    <- investment / psychological / medical / political
6. A closing line that hooks back to the main line
```

**The first item is the one that matters most.** Without it a module degenerates into a
general-purpose handbook - and this framework's value is precisely *not* as a tool.

Every module answers one question before it ships:

> **What has this changed for ordinary people?**

If the answer is missing, the module has drifted.

---

## Core library (5 modules)

These five carry the reasoning. Everything else applies them.

### 01 · Axioms, theorems and the reasoning chain

[`01_公理定理与推演链.md`](../experts/ai-sociology/skills/ai-sociology-framework/references/01_公理定理与推演链.md)

Two base axioms (attention is finite; objectives diverge), four derived axioms, five theorems, the
physical constraint chain, two time horizons, three falsifiable predictions.

**Read it when** you want to check whether a judgement is standing on anything, or trace a claim back
to its premises.

### 02 · The eight-question variable checklist

[`02_变量盘查八问.md`](../experts/ai-sociology/skills/ai-sociology-framework/references/02_变量盘查八问.md)

The eight questions, the variable-mapping method, the three slow-down questions that separate fact
from condition from value judgement, and four reasoning functions.

**Read it when** someone hands you a judgement-shaped question ("will AI replace accounting?").

### 03 · Expression and topic standards

[`03_表达与选题规范.md`](../experts/ai-sociology/skills/ai-sociology-framework/references/03_表达与选题规范.md)

Four stances, copy structure, language rules, title rules, the first-frame hook library, and a
pre-publication checklist.

**Read it when** you need to turn a judgement into something that survives contact with an audience.

### 04 · Evidence grading and citation boundaries

[`04_证据分级与引用边界.md`](../experts/ai-sociology/skills/ai-sociology-framework/references/04_证据分级与引用边界.md)

The four-level evidence marking scheme (`Fact` / `Mechanism` / `Quotation` / `Assumption`), citation
discipline for borrowed material, and the data-anchor library.

**Read it when** you are about to assert a number, or to reuse someone else's framing.

### 05 · Practitioner profile

[`05_从业者经验画像.md`](../experts/ai-sociology/skills/ai-sociology-framework/references/05_从业者经验画像.md)

The observation stances available to the expert, the phrasing that can be used directly, the limits on
using them, and a plain-language glossary.

**Read it when** a judgement needs to be stated in the language of the industry it is about.

---

## Tool-oriented extensions (7 modules)

These cover **how to use things**. They are practical, and they age: product updates can date them.

| # | Module | Focus | Hooks back to |
| :--- | :--- | :--- | :--- |
| 06 | Tools and workflows | Six questions, full cost including exit cost, three-attribute process split, agent skeleton | Axiom five · access |
| 07 | Content and copy | Closing line, second-by-second structure, hook types, teardown, topic scoring, column system | A1 · attention |
| 08 | Video production | Pipeline, quality gate, prompt-block method, degradation path | Generation costs approach zero |
| 09 | Cross-border and industry | Four-stage sector reading, evidence chain, five-part benchmark card, gap attribution, compliance | Axioms three and four |
| 10 | Growth and training | 90-day cold start, platform mechanics, sales drills, three growth conclusions | Axiom five |
| 11 | Diagnosis and knowledge management | Four structural questions, three scaling preconditions, knowledge base and inbox mechanics | Axiom three |
| 12 | Industry and investment observation | Physical ceiling chain, three walls, bottleneck migration, topic constitution, verification list | Axiom four |

> **Module 12 carries a hard boundary and it must be carried along with it:**
> the material is a research frame. It is **not investment advice** and makes no judgement on any
> instrument. On money decisions, consult a licensed professional.

---

## Situation-oriented extensions (4 modules)

These cover **what has changed for people**. They do not age with products, because they describe
structural conditions rather than tools.

| # | Module | Core tool | Closing line |
| :--- | :--- | :--- | :--- |
| 13 | Education and learning | Three layers (knowledge / skill / judgement), four-stage route, four-way error attribution, four-grid delivery | Answers get cheaper, questions get dearer |
| 14 | Relationships and reality | Supply · cost · responsibility split, four verifiability conditions | Everything good it gives you is real; only the price is fake |
| 15 | Attention and judgement | Three non-properties of attention, aesthetic inflation, the outsourcing line, friction criteria | Attention is not taken, it is traded away |
| 16 | Evidence and facts | Six-step verification, five distortion families, three questions about a number, counterexample first | Is what you believe something you saw, or something you heard? |

**Why these four matter more over time**: the tool modules will be superseded by product changes.
These will not. The project's long-term position is *watch where AI is moving, find where humans
stand* - and that is what this group addresses.

---

## Templates (5)

Ready to fill in, in [`templates/`](../experts/ai-sociology/skills/ai-sociology-framework/templates/):

| Template | Use |
| :--- | :--- |
| Trend briefing | A structured forecast with criterion, horizon and falsification condition |
| Variable checklist | The eight-question table plus observation signals |
| Topic and script card | From closing line to second-by-second script |
| Claim verification sheet | Six-step verification with evidence grading |
| Learning diagnosis card | Where you are actually stuck, and the fix |

---

## Adding a module

See [CONTRIBUTING.md](../CONTRIBUTING.md). The short version:

1. Write it into `references/` with the six-part structure
2. **Register it in every navigation table** - this is the step that gets forgotten
3. Run `python3 scripts/validate.py`

> A module that exists in `references/` but is not in a navigation table will never be read by the AI.
> The work is wasted.

---

[← Getting started](01-getting-started.md) · [Documentation index](README.md) · [Next: Experts →](03-experts.md)
