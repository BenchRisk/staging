# Mitigation 135 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #135, which mitigates Failure Mode #27.
Source: data/mitigations/135.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 135
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data
  used to tune the evaluator"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~20.83%
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
> Is there evidence of high agreement between human annotation outputs and the evaluation
> model?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs, tasks, or
  behaviors. High interrater reliability indicates the evaluation criteria are
  well-defined and applied consistently; it is commonly quantified using statistical
  measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`agreement_measured`** — Agreement between the automated evaluation model's outputs
   and human annotation outputs is actually measured (e.g., reported as a correlation,
   Cohen's kappa, F1 against human labels, or accuracy versus human judgments).
2. **`agreement_high`** — The reported agreement is high — the evidence indicates the
   evaluation model tracks human judgments closely rather than diverging from them.

**Strong positive signals:** a reported human–model agreement statistic (kappa, Pearson
/ Spearman correlation, percent agreement, F1 against human labels) with a value
indicating strong concordance; a validation section comparing the automated evaluator
against held-out human annotations; description of the human–model agreement study and
its sample.

**Negative / disqualifying signals:** the evaluator is used with no comparison against
human judgments; agreement claimed qualitatively but never quantified; reported
agreement is low or marginal; only inter-human agreement is reported with no link to the
evaluation model; validation described as future work.
