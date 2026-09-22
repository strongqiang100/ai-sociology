# Volume V · Evidence, identification and research protocol

[中文](05-research-protocol.zh-CN.md) · [Foundations](01-foundations.en.md) · [References](REFERENCES.md)

## 1. From source material to propositions

The source inventory covered 130 Markdown files in the existing repository, 11 notes in the local AI sociology knowledge base, and 30 online texts obtained through relevant titles and indexes. Counts include duplicates, navigation and peripheral tool material; they are not 171 independent studies. Existing course and report notes were inputs. The project does not claim a fresh page-by-page audit of every underlying PDF.

Processing involved deduplication and thematic mapping, separation of concepts and boundaries, mechanisms with opposing branches, and calibration against public original research. Product news, vendor statements, market forecasts and untraceable quotations were not promoted to established social laws. Practice supplied questions; unauthorized personal, client and institutional details were excluded from public text.

| Source family | Theoretical material retained | Research location |
|---|---|---|
| Core framework, manifestos and variable audits | Attention, goal differences, generation, delegation and exit | P01–P16; V001–V032, V097–V112 |
| Abundance, engineering and future scenarios | Digital supply, embodiment, energy, capacity and healthy life | V001–V008, V041–V056, V113–V128 |
| Introductory and generative AI course notes | Tasks, data, evaluation, deployment, learning and human review | V033–V056, V081–V088; M04, M05, M07 |
| Technology and industry report notes | Cost allocation, task restructuring, lock-in, security and physical deployment | V049–V056, V081–V120; M08 |
| Social and educational report notes | Evaluation, participation, rights, educational and intergenerational differences | V033–V040, V105–V112, V121–V128 |
| Content, truth, relationships and expression | Adaptation, narrative, evidence, reciprocity, meaning and communication | V017–V032, V057–V080; D034, D039–D040 |
| Expert and skill modules | Occupations, human motives, stratification, anxiety and physical limits | Cross-level structure and research protocol |

This maps conceptual provenance, not endorsement of every input claim. Operational tutorials, account-growth arrangements and duplicate installation instructions were not copied into theory chapters. Coverage means that relevant themes have a place, not that every old sentence survives or every real-world factor has been exhausted.

## 2. Compatibility with earlier formulations

| Potentially absolute earlier formulation | Research-edition treatment |
|---|---|
| Attention cannot be parallelized or stored | Distinguish attention, records, memory, switching and external assistance |
| Capability continuously improves and costs continuously fall | Conditional task- and horizon-specific trends permitting reversal |
| Goals do not align automatically | Preserve the logical distinction while permitting cooperation and alignment |
| Social desires never saturate | Study saturation by need, reference group, institution and culture |
| Emotion is a fixed consumable resource | Separate regulation, fatigue, motivation, recovery and adaptation |
| Responsibility makes signatories more valuable | Add information, competence, time, authority and bargaining conditions |
| Engineering changes speed but never direction | Allow changes in feasibility, costs and adoption direction |
| Inclusion necessarily deepens dependence | Separate access, portability, substitutes, objectives and actual exit |
| All reasoning must return to one conclusion | Use branches, rival explanations and admissible counterexamples |

Existing installable archives remain historical versions; this edition does not claim to rebuild every expert and skill package. New research should use the present evidence protocol and claim taxonomy. Earlier material can motivate questions but cannot bypass conditionality checks.

## 3. Evidence classification

| Source type | Appropriate use | Required context |
|---|---|---|
| Original theory | Concepts, assumptions and deductions | Original assumptions; not contemporary AI validation |
| Randomized experiments | Effects within studied samples and interventions | Randomization unit, adherence, attrition and intervals |
| Quasi-experimental and observational studies | Relations or effects under identification assumptions | Confounding, selection, time trends and sensitivity |
| Qualitative and historical studies | Processes, meaning, mechanisms and institutional differences | Case selection, sources, counterexamples and rivals |
| Official statistics and technical evaluations | Quantities or performance under stated definitions | Date, population, denominator, version and coverage |
| Vendor claims and industry forecasts | Claims, leads and scenarios | Interests, forecast status and methods |
| Notes and practitioner experience | Questions and candidate mechanisms | Secondary status, scope and unverified components |

There is no universal evidence ranking independent of the question. Experiments can be narrow, while interviews reveal mechanisms omitted by scales. Agreement across methods can be valuable, but multiple sources repeating one unverified claim are not independent corroboration.

## 4. Minimum study registration

```text
Study ID and version:
Related P / V / D / M:
Question and target population:
Unit, region, task and horizon:
Treatment or input change:
Primary outcome and measurement:
Prespecified mediators, moderators and confounders:
Branch A conditions and prediction:
Branch B conditions and prediction:
Main rival explanation:
Identification strategy and necessary assumptions:
Sampling, missingness and attrition:
Primary tests, smallest meaningful effect and power:
Multiplicity and exploratory-analysis labels:
Results that would weaken or reject the explanation:
Ethics, consent, data minimization and withdrawal:
Findings, uncertainty, generalization limits and revisions:
```

Specify primary outcomes and subgroups before inspecting results. An underpowered nonsignificant result does not prove zero effect. Equivalence testing requires a prespecified negligible-effect interval. Affect and relationship measures should not be used to assign individual clinical diagnoses.

## 5. Three identification traps

**Selection and reverse causation.** A relationship between AI use U and loneliness may arise because prior loneliness L₀ affects both U and later loneliness L₁. Record baselines, randomize availability where appropriate, or use a suitable longitudinal design rather than simply subtracting users from nonusers.

```mermaid
flowchart LR
  L0[Baseline loneliness L0] --> U[Use U]
  L0 --> L1[Later loneliness L1]
  U --> L1
  S[Support and resources S] --> U
  S --> L1
```

Arrows express causal assumptions, not facts discovered from data. The graph allows U→L₁ while showing why correlation alone cannot estimate it. Arbitrarily controlling post-treatment mediators or colliders can introduce bias. [R14]

**Common shocks.** A tool launch accompanied by a recommendation change cannot isolate the tool's income effect through a simple before-and-after comparison. Difference designs also require assumptions such as parallel trends, comparable groups and no relevant concurrent interventions. A method's name does not establish causality.

**Levels and denominators.** Less time per task need not reduce total hours per person. Higher income among users need not be caused by tools. More content with a lower hit rate does not by itself establish a constant attention budget. Record totals, distributions, denominators and horizons together.

![Figure 4: Identification, delegation and feedback](figures/fig04-causality-governance.png)

**Figure 4 · Identification, delegation and feedback.** a, Baseline loneliness and support can affect both use and later loneliness, preventing simple correlation from identifying the target effect. b, Delegation requires usable audit, appeal and exit between authorization, service execution and consequences. c, Expanded supply can accompany better verification or greater unverified exposure; trust may affect subsequent adoption. Solid links are proposed relations; dashed links denote governance or feedback. All require empirical examination.

## 6. From a theory pool to auditable forecasts

A forecast should state: under conditions C, within horizon T and population G, outcome Y is expected to change relative to baseline B; observation Z would reduce confidence or trigger withdrawal. Probabilities require defined events, deadlines, data sources and resolution rules. Do not fabricate precision without grounds for calibration.

Scenarios can cover continuing conditions, relaxed constraints and changed institutions. Three scenarios do not imply three equally probable futures. Retain failed forecasts and distinguish factual, timing, mechanism and observability errors instead of extending deadlines indefinitely.

## 7. Candidate combinations and expansion

The 128 variables yield 11,017,504 unordered tuples of order two through four. The paginated enumerator can cover the entire candidate set. It does not establish independence, causal direction or identification. It enumerates distinct variables, not states, temporal orders, cycles or hidden variables.

```bash
python3 scripts/explore_theory.py --stats
python3 scripts/explore_theory.py --variables V009 V057 V098 V097 --order 3 --limit 4
python3 scripts/explore_theory.py --order 4 --offset 1000 --limit 20
```

A new card requires input changes, outcomes, assumptions, two branches and a challenge to the explanation. Four words do not constitute a derivation. A crucial fifth condition should be explicit, with a higher-order model where needed, rather than hidden inside “all else equal.” Religion, war, family institutions and gender structures require dedicated measurement and designs; broad variables do not claim to explain them fully.

## 8. Public expression and versioning

Introduce terms when first used. Difficult language does not replace evidence. Headlines and memorable formulations should survive the addition of their conditions. Literature, allegory and science fiction can construct thought experiments, but fictional premises are not empirical sociology or grounds for forecast credibility.

Chinese and English use identical P/V/D/M/R identifiers and should not differ in claim strength. Research edition 0.1.0 separates future additions of hypotheses, revisions of conditions and new empirical evidence. Corrections should record the original proposition, reason, scope and new grounds, rather than silently substituting conclusions.

Use the [research proposal template](templates/research-proposal.md). Passing code, schema and formatting checks means the material is usable; it does not validate the theory.
