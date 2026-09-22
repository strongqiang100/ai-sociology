# Volume IV · Games and formal models

[中文](04-games-and-models.zh-CN.md) · [Foundations](01-foundations.en.md) · [Derivations](03-derivation-pool.en.md)

These eight models are conditional model propositions (M). Accounting identities, equilibrium deductions and empirical estimates are different activities. All numerical values are thought experiments, not estimates from platforms or populations. Utility units apply only within each model. M01–M08 correspond to the reproducible checks in the project script.

## M01 · Attention allocation and effective understanding

Consider n items encountered by an audience within a fixed horizon. Let tᵢ be minutes assigned to item i, A the available budget, and qᵢ an assumed comprehension return per minute. qᵢ is a conditional analytical parameter, not a substitute name for viewing duration.

```math
\max_{t_i\geq 0}\sum_{i=1}^{n}q_i t_i
\quad\text{subject to}\quad\sum_{i=1}^{n}t_i\leq A.
```

If attention is equal across items and the budget is exhausted, average time is A/n. With A=60, increasing n from 30 to 60 reduces the average from two minutes to one. This is conditional arithmetic, not evidence that recommendation systems allocate equally. If added content improves selection of higher-qᵢ material, understanding may rise with unchanged total time.

A linear objective without item-specific upper bounds assigns everything to the highest qᵢ. That extreme solution is unsuitable for many reading situations. Extensions can include diminishing utility uᵢ(tᵢ), completion thresholds, complementarity and switching costs. Recognizing the limitation prevents the model's solution becoming an unwarranted life prescription.

Hold audience and horizon fixed; measure supply, actual time and delayed comprehension separately. Better understanding after improved matching refutes the strong claim that more supply inevitably reduces learning. Related: D001, D033, D053; R01.

## M02 · A prisoner's dilemma of stimulation

Two producers compete for the same exposure. Strategies are restraint (R) and escalation (E). They act simultaneously with knowledge of the payoff structure. Payoffs are private utility net of production burdens within the horizon, not social welfare. Values are assumed.

| Producer 1 / Producer 2 | R | E |
|---|---|---|
| R | (3, 3) | (1, 4) |
| E | (4, 1) | (2, 2) |

Against R, E yields 4 rather than 3; against E, it yields 2 rather than 1. E strictly dominates for both, making (E,E) the unique Nash equilibrium. Both nevertheless prefer the payoff 3 at (R,R) to 2, so the equilibrium is Pareto-inferior in private-payoff terms. This does not establish the structure of every stimulation contest.

Suppose escalation incurs an additional private cost p. Its payoffs become 4−p against R and 2−p against E; restraint payoffs stay unchanged. For p>1, R strictly dominates. At p=1, each player is indifferent against either strategy: all pure profiles and all mixtures are equilibria. For p<1, E strictly dominates. Costs might arise from rules, production or reputation, but must be measured rather than assumed to exist.

Rules can therefore change an equilibrium in principle without being feasible in practice. Enforcement, externalities, displacement and rule-setting authority still need study. Repeated-game cooperation additionally requires discounting, monitoring and punishment assumptions. Related: D034, D054; R12.

## M03 · Coordination on an open standard

Two organizations choose a compatible open standard (O) or separate proprietary paths (P). Assume the following coordination payoffs.

| Organization 1 / Organization 2 | O | P |
|---|---|---|
| O | (4, 4) | (0, 2) |
| P | (2, 0) | (2, 2) |

Best responses produce two pure equilibria: (O,O) and (P,P). If the probability that the other adopts O is q, expected payoff from O is 4q, while P yields 2. O is preferred above q=1/2, P below it, and both are equivalent at the threshold. The symmetric mixed equilibrium has each choose O with probability 1/2.

Standards, commitments and migration support may alter beliefs or payoffs. But this model omits distributional conflict within openness. If one party loses even under mutual adoption, the problem is no longer pure coordination. The matrix does not determine market concentration. Related: D045, D048; R12, R13.

![Figure 3: Stimulation, changing incentives and coordination](figures/fig03-games.png)

**Figure 3 · Stimulation, changing incentives and coordination.** a, Assumed M02 payoffs yield mutual escalation as the unique Nash equilibrium. b, Restraint strictly dominates when added escalation cost exceeds 1; equality gives indifference. c, In M03, openness yields higher expected payoff when expected counterpart adoption exceeds one half. These are distinct illustrative games, not platform measurements.

## M04 · Audit incentives and substantive oversight

An actor chooses careful verification or omission. Omission supplies a private benefit b, is independently detected with probability p, and incurs cost F if detected. Normalize verification's net payoff to zero. Omission yields b−pF. Under risk neutrality, enforceability and no additional payoffs, pF>b induces strict preference for verification; equality produces indifference.

Let b=2 and F=10. At p=0.1 omission yields 1; at p=0.3 it yields −1. The threshold is p=0.2. b and F use the same private-utility scale, not mixed minutes and currency. Real penalties face limits, delays and due-process constraints; unlimited F is not a policy conclusion.

Sufficient incentives do not ensure competence. Let d be error-detection probability under suitable load and ℓ the proportion prevented from actual interception by workload or authority constraints. The stylized interception probability d(1−ℓ) is an assumed function, not an estimated law. Even high pF cannot compensate for d near zero or ℓ near one. Separate responsibility, incentives, capacity and authority.

Use blinded known-error reviews, actual stopping records and workload measures. Signature rates are not error-detection rates. Related: D021, D044, D055; R07.

## M05 · Task substitution, demand expansion and labor hours

Let task price be p, demand Q=Kp^(−ε), and labor hours per task h. Total labor is L=hQ. If the demand form and K remain fixed across two periods:

```math
\frac{L_1}{L_0}=\frac{h_1}{h_0}\left(\frac{p_1}{p_0}\right)^{-\varepsilon}.
```

Suppose h and p both halve. For ε=0.5, L₁/L₀≈0.707; for ε=1 it equals 1; for ε=2 it equals 2. Halved labor per task can therefore coexist with lower, unchanged or higher total labor. Price pass-through, saturation and new tasks require separate identification.

Hours are neither job counts nor individual wages. Allocation of hours, skills, location and compensation shape personal outcomes. The model cannot predict aggregate unemployment or guarantee new demand reaches those displaced. Related: D023, D036, D056; R09.

![Figure 2: Why labor demand can diverge after automation](figures/fig02-conditional-labor.png)

**Figure 2 · Why labor demand can diverge after automation.** Calculated from M05 with labor per task halved and demand form fixed. a, Price ratios and elasticity determine total labor hours; the black line marks no change and color is logarithmic. b, Three elasticities; markers indicate halved prices. Hours are not job counts or wages. Display ranges are limited as shown; all values come from the assumed model.

## M06 · Surplus creation and bargaining allocation

Let cooperation create transferable surplus S≥0 above both parties' outside options. A worker receives x and the other party S−x. Under known surplus, voluntary participation and bargaining parameter β∈(0,1), the generalized Nash bargaining solution maximizes:

```math
\max_{0<x<S}x^{\beta}(S-x)^{1-\beta}.
```

Log differentiation gives β/x−(1−β)/(S−x)=0, hence x=βS. With S=100, β=0.2 gives x=20 and β=0.6 gives x=60. Outside options have already been deducted; changes to them require recalculating both the surplus and baselines.

The **Nash bargaining solution** differs from **Nash equilibrium** and has a distinct theoretical source. β is not an empirical estimate obtained by casually scoring “influence.” The model does not cover nontransferable dignity or rights and does not establish that real bargaining satisfies its assumptions. Related: D024, D037, D056; R15.

## M07 · Skill stocks and assisted performance

Let Kₜ denote skill on a fixed measurement scale, δ∈[0,1] the period's forgetting or mismatch rate, Pₜ effective practice, Fₜ standardized feedback quality, and a a unit-conversion coefficient. A candidate model is:

```math
K_{t+1}=(1-\delta)K_t+aP_tF_t.
```

For δ=0.1, a=1 and constant PF=2, the steady state is K*=20; PF=4 gives 40. This requires stable parameters and δ>0; the finite steady-state formula does not apply at δ=0. AI may raise P by freeing time, lower it by replacing practice, or alter F. Direction is not predetermined.

Assisted performance needs a separate outcome Yₜ=g(Kₜ, tool capability, task conditions). Higher Y does not imply higher K. Studies should measure unaided retention and transfer while checking measurement equivalence, practice effects and ceilings. Related: D015, D038, D057; R11.

## M08 · Full costs and resource rebound

At fixed quality and horizon, monetary costs can be recorded as:

```math
C=F+N(c_g+c_v)+E[L_f]+C_m.
```

F is fixed setup cost, N task volume, c_g and c_v generation and verification costs per task, E[L_f] expected failure loss over the horizon, and C_m migration cost. Avoid counting the same labor in both c_v and F. Nonmonetary harms remain separate.

Ignoring other terms, N=100, c_g=1 and c_v=0.2 yield 120. Later, N=1000, c_g=0.1 and c_v=0.2 yield 300. Generation prices fall 90% while totals rise. This arithmetic counterexample is not an industry forecast.

Physical resources use separate units: R=eN, with intensity e. Thus R₁/R₀=(e₁/e₀)(N₁/N₀). Intensity falling to 0.6 with volume doubling produces a total ratio of 1.2. Calling this causally a rebound additionally requires evidence that efficiency or prices induced the demand change. Independent demand growth satisfies the accounting identity without proving rebound.

Related: D019, D020, D046, D061. This is the project's accounting decomposition, not an appeal to a named theory in place of derivation.

## How models can fail

Record units, horizon, strategies, information, parameter sources and exclusions. When evidence differs, inspect measurement and assumptions, then compare alternatives rather than treating every deviation as generic complexity. Run `python3 scripts/check_theory.py` to reproduce arithmetic examples and structural checks. It does not validate social hypotheses.
