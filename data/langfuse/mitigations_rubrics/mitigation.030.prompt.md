# Mitigation 030 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #30, which mitigates Failure Mode #27.
Source: data/mitigations/30.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 30
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data
  used to tune the evaluator."*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human annotators to
  generate ground truth labels or scores that are later used to train an automated
  evaluator. However, the annotators frequently disagree on task success criteria—such as
  what constitutes a "correct," "helpful," or "safe" response—due to vague instructions,
  subjective judgments, or cultural differences. This results in low interrater
  reliability, with inconsistent and noisy labels forming the basis of the evaluator's
  training data. As a result, the evaluator itself becomes unreliable, often reflecting
  annotator bias or randomness rather than objective quality. A benchmark user, unaware of
  this underlying inconsistency, trusts the evaluator's scores and selects a system that
  performs well on flawed metrics but poorly in actual deployment scenarios.

**Criterion question (answer this for the benchmark under review):**
> Do you measure and iterate on your methods until you achieve high interrater
> reliability for the human-labeled data used to train the evaluator, and ensure that any
> remaining uncertainty from disagreements is reflected in the confidence measures
> provided to users?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs, tasks, or
  behaviors. High interrater reliability indicates the evaluation criteria are
  well-defined and applied consistently; it is commonly quantified using measures such as
  Cohen's kappa.
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`irr_measured`** — Interrater reliability of the human-labeled data used to train
   the evaluator is **measured** and reported (e.g., a kappa or agreement statistic).
2. **`iterated_to_high`** — The documents show the labeling methods were iterated/refined
   until **high** interrater reliability was achieved (not merely measured once and left
   low).
3. **`uncertainty_in_confidence`** — Any remaining uncertainty from rater disagreement is
   reflected in confidence measures surfaced to users.

**Strong positive signals:** a reported interrater agreement statistic (e.g., Cohen's
kappa) meeting a stated high threshold; description of guideline revision rounds that
raised agreement; confidence intervals or uncertainty bands attributed in part to
labeling disagreement; an explicit account of how residual disagreement propagates to
reported scores.

**Negative / disqualifying signals:** no interrater reliability statistic reported;
agreement measured but low and unaddressed; single-annotator labels with no agreement
check; scores reported without any uncertainty/confidence measure; the IRR process
described only for a future version of the benchmark.
