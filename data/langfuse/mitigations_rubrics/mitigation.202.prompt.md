# Mitigation 202 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #202, which mitigates Failure Mode #31.
Source: data/mitigations/202.mdx and data/modes/31.mdx.
-->

## The mitigation under review

- **Mitigation number:** 202
- **Mitigates failure mode:** #31 — *"Evaluator(s) perform poorly across all SUTs."*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~0% reduction in failure-mode likelihood; ~0% reduction
  in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark employs undergraduate
  psychology students with no technical background to evaluate advanced AI reasoning on
  complex mathematical proofs. These evaluators cannot distinguish between correct proofs
  and those with subtle errors, giving high scores to any response that looks
  sophisticated regardless of accuracy. As a result, all tested systems receive similarly
  high scores despite vast differences in actual mathematical reasoning capabilities. The
  benchmark user selects the cheapest SUT thinking it performs equivalently to premium
  options, then deploys it to verify critical engineering calculations for a bridge
  design, resulting in structural flaws being missed and necessitating costly redesigns
  when discovered by other verification methods.

**Criterion question (answer this for the benchmark under review):**
> Did you use an off-the-shelf evaluator model without tuning, but with an evaluation
> program that finds its reliability to be adequate for the evaluation task?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators when assessing the same set of outputs, tasks, or behaviors.
  High interrater reliability indicates the criteria are well-defined and applied
  consistently; it is commonly quantified with measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`off_the_shelf_untuned_evaluator`** — The documents state that the evaluator is an
   off-the-shelf model used without fine-tuning or task-specific tuning for this
   benchmark.
2. **`reliability_assessment_run`** — An explicit evaluation program / validation
   procedure was run to assess that evaluator's reliability on this evaluation task (e.g.,
   agreement with human/gold labels, interrater reliability, accuracy on a validation
   set).
3. **`found_adequate`** — That assessment reports the evaluator's reliability to be
   adequate for the task, with results given for the currently published benchmark.

**Strong positive signals:** a named off-the-shelf evaluator model with an explicit
statement that no tuning was applied; reported agreement statistics (e.g., kappa,
correlation, or accuracy vs. human labels) on a validation set; a documented threshold or
criterion for "adequate" reliability that the evaluator meets.

**Negative / disqualifying signals:** the evaluator was fine-tuned/tuned for the task (a
different path); an off-the-shelf evaluator used with no reliability assessment at all;
reliability checked but found inadequate or not reported; the validation described only
as planned while the published scores rely on an unvalidated evaluator.
