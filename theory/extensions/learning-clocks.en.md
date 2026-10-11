# Learning clocks: when tools change faster than people learn

[中文](learning-clocks.zh-CN.md) · [Five-volume framework](../README.md) · [Foundations](../01-foundations.en.md) · [Models](../04-games-and-models.en.md)

Date: 2026-10-11. Extension namespace: LC. This topic develops P01, P08, P09, P13, P15, section 6.5 and M07. It is not a sixth volume and does not alter the counts or identifiers of the 16 principles, 128 variables, 64 pathways and eight core models. LC-D denotes definitions, LC-M conditional models, LC-H untested hypotheses and LC-N normative positions. All numerical examples are thought experiments, not estimates.

## 1. The problem

Suppose a powerful new tool takes a week to learn. After three days, an easier substitute can already perform the same task. The lost opportunity may be an advantage from mastering difficult operations, not all the knowledge acquired. Repeated disappointment may produce a sense that learning is pointless. Here, this is a proposed subjective response, not a clinical diagnosis or a universal outcome.

Learning itself does not detach people from reality. A mismatch between sustained investment and actual uses can crowd out practice, feedback and other options. The opposite is possible too: technological progress can reduce learning costs and make existing knowledge more useful. Claims that traditional software always changed annually, or that AI always replaces tools every three days, are not assumed. These intervals are scenario parameters.

## 2. Different clocks and different learning assets

### LC-D01: release, adoption, useful advantage and learning

A release clock measures when a product appears. An adoption clock measures when a person or organization can safely switch. A useful-advantage clock measures when learned content no longer adds enough value for a specified task. A learning clock measures time to an actual acceptance standard, not time to finish a tutorial.

Compare the last two, informed by deployment conditions. Publication is not replacement: quality, access, data, contracts, reliability and migration costs can preserve an older workflow. Hardware versions, control software, materials and safety procedures also have different clocks. Slow hardware turnover is not sufficient to make a particular course worthwhile.

### LC-D02: specific and transferable components

One learning episode may create version-specific procedural memory, transferable principles, task data and tests, troubleshooting records, collaboration experience or personally valued experiences. Each has different failure conditions. A disappeared menu does not erase process knowledge; an abstract theory is not automatically durable.

Connections to the existing atlas include V035 learning time, V037 skill updating, V038 problem definition, V047 deployment maturity, V048 alternative supply, V050 lifecycle cost, V088 transition cost and V099 exit cost. The parameters below are task-level refinements, not claims that the atlas already measures everything.

## 3. LC-M01: a screening ratio, not a return estimate

Measure calendar time from the decision to learn. Let d>0 be days to the acceptance standard, T days until the specific advantage relative to an accessible baseline disappears, W the remaining useful window, and rho its ratio. The baseline may be an existing tool, outside assistance or the current workflow, not necessarily inaction.

```math
W=\max(T-d,0),\qquad \rho=\frac{T}{d}.
```

When rho is at most one, there is no post-learning window under assumptions of no output during learning, no transferable value and advantage ending at T. A larger ratio means a longer window, not necessarily a worthwhile investment. A durable but unused skill can have no return. An urgent short-window task may repay its cost quickly. If d=0, skip the ratio. When horizons are uncertain, record ranges and their evidence rather than false precision.

## 4. LC-M02: incremental benefit and transfer value

For a specified task, quality standard and evaluation horizon, let b be net daily benefit after learning relative to the baseline; C learning and other costs not already deducted; and R transferable residual value after the useful window:

```math
N=bW+R-C.
```

Break-even requires bW+R>C. When b>0, this is W>(C-R)/b. If C-R<0, residual value alone covers costs, conditional on its validity. For b<=0, do not reuse that division threshold.

Use consistent units: money, or hour equivalents for a fixed-quality task. Actual learning hours, ell, are not calendar delay d. Do not deduct operating, rework or maintenance costs twice. R excludes value already in bW. Past costs belong in retrospective evaluation; continuation decisions compare future avoidable costs and benefits. Already acquired knowledge can change those future quantities, but sunk effort alone cannot justify continuing.

Respect, enjoyment, health, relationships and life meaning remain separate goals and constraints. A negative commercial return does not make an experience meaningless; personal enjoyment does not make a business calculation positive.

| Illustrative case | Calendar times | Common-unit inputs | Net result |
|---|---|---|---|
| Specific operations with a short useful life | d=7 days, T=10 days | b=2 hours/day, R=0 hours, C=30 hours | W=3; N=-24 hours; rho approximately 1.43 |
| Stable process with recurring demand | d=30 days, T=180 days | b=1 hour/day, R=0 hours, C=60 hours | W=150; N=90 hours |
| Short window, validated transferable assets | d=7 days, T=10 days | b=2 hours/day, R=35 hours, C=30 hours | N=11 hours |

These are assumptions, not product forecasts. Output during learning would require a separate term. The third case must be revised if later tasks do not validate the 35-hour residual.

## 5. LC-M03: uncertain decay and alternatives

Let H>=d be the horizon; S(t) probability the learned advantage remains usable at t; b(t) incremental benefit rate conditional on usability; and r the per-time discount rate:

```math
\mathbb{E}[N]=\int_d^H e^{-rt}S(t)b(t)\,dt
 +B_{\mathrm{during}}+R_H-C.
```

All remaining terms are valued at the same decision date and in the same units. B_during counts incremental output during learning; R_H counts value after H not already in the integral. Probabilities require data or explicit scenarios, not arbitrary percentages.

For r=0, constant b, S(t)=exp(-lambda t), lambda>0 and an infinite horizon, expected window benefit is b exp(-lambda d)/lambda. Lambda is the hazard of advantage loss, not the number of daily product announcements. Increasing lambda or d lowers this component. Better AI can also reduce d and raise b or transfer value, so decay alone does not determine outcomes.

Compare deep learning, task-sufficient learning, a mature solution and bounded waiting. Positive expected net benefit from deep learning does not prove it beats light learning or waiting. Waiting has opportunity costs and requires a review date. Safety-critical knowledge cannot be postponed solely because the short-term return is small.

## 6. Conditional propositions and opposing hypotheses

### LC-M04: four propositions within the assumptions

1. Holding b, R, C and d fixed, shortening T cannot raise simplified N when b>=0. With b>0 and T>d, each day lost reduces N by b. Below d, the window is zero, never negative.
2. Holding other inputs fixed, greater validated R can offset loss of tool-specific benefit. This does not prove that any foundational skill is immune to change.
3. A qualified lower-barrier substitute can reduce b or T associated with difficult operations. It can also reduce learning costs or complement domain knowledge. Both effects may occur together.
4. Sunk effort alone cannot justify further learning. Acquired assets affect future costs and benefits, which remain relevant.

These are algebraic or decision propositions, not empirically proven sociological laws.

### LC-H01: a possible mechanism for learning futility

Repeated failure to realize expected uses may weaken confidence in learning and reduce exploration. Visible transferable progress and useful feedback may instead redirect learning toward fewer, deeper tasks. Fatigue, resource constraints, income pressure and misleading promotion are competing explanations.

### LC-H02: who bears adaptation costs

If employers require continuous updates while workers train and troubleshoot in private time, cheap organizational upgrading may impose higher personal costs. Paid training, stable workflows and shared evaluation assets may change this. Early research and engineering can also produce sufficient returns to justify deliberate experimentation. The outcome is not simply a test of individual effort.

## 7. Knowledge categories are guides, not a hierarchy

Version-specific procedures warrant task-sufficient learning when there is actual demand; avoid memorizing every transient button without a use. Engineering principles, data structures, permissions, testing and fault handling can transfer, but commands and frameworks are not permanent advantages. Concepts and domain knowledge are useful when they change a decision and survive application to different problems, not when they merely rename them.

Mathematics, causal reasoning and measurement require applications and feedback; abstract vocabulary alone does not accumulate value. Practical experience and relationships should be assessed by outcomes and ongoing trust, not years or contact lists. Interest and meaning may justify learning on their own terms, subject to affordable costs and life constraints. Researchers, maintainers, business users and hobbyists can legitimately choose different depths.

## 8. Durable accumulation is a process

Candidate assets include explicit acceptance standards, authorized portable data, reusable tests and failure records, workflow understanding, decisions validated by results, and sustainable collaboration. Their value comes from reuse and feedback, not a prestigious label. AI may complement or replace parts of these activities; no asset receives permanent immunity.

For assets measured on a fixed usable-asset or task-performance scale, a bookkeeping illustration is:

```math
A_{t+1}=(1-\delta)A_t+g_t-m_t.
```

Delta denotes forgetting or mismatch; g validated additions; m same-scale damage or maintenance burden, not time expenses subtracted from knowledge units. The stock grows only when g exceeds delta A+m; growth need not be exponential. Meaning and dignity are not folded into A. This is consistent with M07, not a ninth core model.

## 9. Six practical principles

Specify a use before choosing depth. Estimate task-specific useful life, not release frequency. Run a bounded small test before major investment. Check what survives a tool switch. Reassess future costs and benefits rather than chasing sunk effort. Preserve the right to stop, delegate, consult documentation and pursue noncommercial goals. Necessary safety knowledge is a constraint, not an optional ROI shortcut.

A minimal diagnostic records the goal, baseline, calendar learning delay, actual hours, useful-life estimate and rationale, expected tasks, validation of residual value, cost bearer and stop/review date.

## 10. Tests and refutation

The unit is person x task x tool version. Track acceptance delay, learning hours, fixed-quality outputs, transfer performance, cost distribution and motivation. Comparing learning strategies requires addressing prior ability, task difficulty and time access if assignment is not randomized.

Faster releases with stable old-workflow returns do not confirm faster skill obsolescence. Failed transfer weakens a high-R explanation. Better long-term outcomes among deep learners require examining immediate returns, selection and principle acquisition rather than insisting tool learning always loses. Assisted output is not independent learning: retain unaided and transfer tests.

## 11. Sources and contribution

- [Deming and Noray, STEM Careers and the Changing Skill Requirements of Work](https://www.nber.org/papers/w25065), 2018, revised 2019; subsequently published in QJE in 2020. The study motivates investigation of technology-specific skill mismatch and career returns, not three-day AI replacement claims. Public abstracts and metadata were checked; underlying data were not reanalyzed.
- [Brynjolfsson, Li and Raymond, Generative AI at Work](https://www.nber.org/papers/w31161), 2023 working paper, published 2025. Customer-support evidence offers an opposing pathway: less-experienced workers may benefit from assistance. Effect sizes differ across versions; none are mixed here. Assisted gains do not alone prove unaided retention.
- Existing [foundations](../01-foundations.en.md), [M07 and M08](../04-games-and-models.en.md) and [research protocol](../05-research-protocol.en.md) provide the framework.

The LC definitions, screening ratio, task-level accounting, scenarios and stopping/waiting strategies develop the author's discussion of 2026-10-11. They are not attributed as formulas from these papers, nor asserted to be novel across the entire literature.

The guiding idea: not every learning target deserves exhaustive pursuit. What matters is repeatedly connecting learning to one's actual questions and life.
