# Mitigation 182 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #182, which mitigates Failure Mode #27.
Source: data/mitigations/182.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 182
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data used
  to tune the evaluator."*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human annotators to
  generate ground-truth labels later used to train an automated evaluator. The annotators
  frequently disagree on task-success criteria — what counts as "correct," "helpful," or
  "safe" — due to vague instructions, subjective judgments, or cultural differences. This
  low interrater reliability produces inconsistent, noisy labels that form the evaluator's
  training data, so the evaluator reflects annotator bias or randomness rather than
  objective quality. A user, unaware of this inconsistency, trusts the evaluator's scores
  and selects a system that performs well on flawed metrics but poorly in deployment.

**Criterion question (answer this for the benchmark under review):**
> Did you use an off-the-shelf evaluator model without tuning, while ensuring the
> evaluation program demonstrates adequate reliability for the task?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators when assessing the same outputs, tasks, or behaviors. High
  interrater reliability indicates well-defined, interpretable criteria applied
  consistently, and is commonly quantified with measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`off_the_shelf_untuned`** — The evaluator is an off-the-shelf model used without
   tuning on the benchmark's own ground-truth labels, so noisy/low-agreement labels never
   shape the evaluator.
2. **`reliability_demonstrated`** — The documents show the evaluation program nonetheless
   demonstrates adequate reliability for the task (e.g., reported agreement with humans or
   another reliability measure).

**Strong positive signals:** a statement that a standard/off-the-shelf evaluator model is
used as-is, without fine-tuning on annotator labels; reported validation of the
evaluator's reliability (e.g., agreement with human judgments, a kappa or accuracy figure
on a check set); an explicit rationale that avoiding tuning sidesteps low-interrater-
reliability label noise.

**Negative / disqualifying signals:** the evaluator is tuned/trained on the benchmark's
own ground-truth labels; no evidence the evaluation program's reliability was measured;
reliance on an evaluator whose quality is merely asserted; reliability validation
promised for a future version.
