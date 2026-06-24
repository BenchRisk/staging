# Mitigation 137 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #137, which mitigates Failure Mode #27.
Source: data/mitigations/137.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 137
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data
  used to tune the evaluator"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human annotators to
  generate ground truth labels or scores that are later used to train an automated
  evaluator. However, the annotators frequently disagree on task success criteria — such
  as what constitutes a "correct," "helpful," or "safe" response — due to vague
  instructions, subjective judgments, or cultural differences. This results in low
  interrater reliability, with inconsistent and noisy labels forming the basis of the
  evaluator's training data. As a result, the evaluator itself becomes unreliable, often
  reflecting annotator bias or randomness rather than objective quality. A benchmark
  user, unaware of this underlying inconsistency, trusts the evaluator's scores and
  selects a system that performs well on flawed metrics but poorly in actual deployment.

**Criterion question (answer this for the benchmark under review):**
> Do you measure and iterate on methods until high interrater reliability is achieved?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs, tasks, or
  behaviors. High interrater reliability indicates the evaluation criteria are
  well-defined, interpretable, and applied consistently; it is commonly quantified using
  statistical measures such as Cohen's kappa.
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`irr_measured`** — Interrater reliability of the annotators producing the ground
   truth is actually measured and reported (e.g., Cohen's / Fleiss' kappa, percent
   agreement, or another agreement statistic).
2. **`iterated_to_high`** — The methods (e.g., annotation guidelines, rater training,
   adjudication) were iterated on, and the process continued until a high level of
   interrater reliability was achieved — not merely measured once and accepted.

**Strong positive signals:** a reported IRR statistic with a value indicating strong
agreement; description of guideline refinement, pilot rounds, or rater calibration
performed to raise agreement; an account of iterating until a target agreement threshold
was met; before/after agreement figures.

**Negative / disqualifying signals:** annotation used with no agreement statistic
reported; IRR measured once and reported as low or marginal with no further action; no
mention of refining instructions or re-measuring; the iteration described only as future
work; agreement asserted qualitatively without numbers.
