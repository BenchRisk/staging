# Mitigation 048 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #48, which mitigates Failure Mode #27.
Source: data/mitigations/48.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 48
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data used
  to tune the evaluator"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~45.83%
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
> Do you use 100% human evaluators for assessing system performance?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property. This mitigation asks
  whether that evaluator is 100% human rather than an automated model tuned on ground-truth
  labels.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs. High interrater
  reliability indicates the evaluation criteria are well-defined and applied consistently;
  it is commonly quantified using statistics such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_evaluation`** — The benchmark's outputs are scored by human evaluators.
2. **`fully_human_no_automated_judge`** — Evaluation is 100% human: there is no automated
   evaluator (e.g., a model tuned on human ground-truth labels) producing the published
   scores.

**Strong positive signals:** an explicit statement that all outputs are scored by human
raters; described human annotation protocols and rater pools; no automated evaluator
trained on labels in the scoring pipeline; humans applying the criteria directly to each
output rather than to a model's behalf.

**Negative / disqualifying signals:** an automated evaluator trained on human-labeled
ground truth producing the scores; a hybrid setup where machines do most grading; human
labels used only to tune a model that issues the published scores; full human evaluation
described only as a future plan.
