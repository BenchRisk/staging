# Mitigation 032 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #32, which mitigates Failure Mode #29.
Source: data/mitigations/32.mdx and data/modes/29.mdx.
-->

## The mitigation under review

- **Mitigation number:** 32
- **Mitigates failure mode:** #29 — *"SUT developers produce training data from
  evaluator."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** Developers of a SUT gain access to the
  benchmark evaluator—either by reverse-engineering a public implementation or through a
  public API—and use it as a reward model or filtering mechanism during training or
  fine-tuning. This causes the model to optimize specifically for evaluator preferences,
  potentially learning to game the scoring mechanism through superficial alignment (e.g.,
  mimicking surface features that score well, like formality or verbosity) rather than
  achieving true task performance. As a result, the model performs exceptionally well on
  the benchmark but fails to generalize to tasks that aren't shaped by the evaluator's
  biases. A benchmark user, unaware of this overfitting loop, selects the system expecting
  robust general capabilities, only to encounter brittle outputs.

**Criterion question (answer this for the benchmark under review):**
> Do you avoid making the evaluator or its answers publicly available?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs (e.g.,
  transparency, consistency, reproducibility, independence), guarding against practices
  such as benchmark overfitting and data snooping.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluator_not_public`** — The benchmark's evaluator (judge model, scoring model, or
   scoring code) is **not** made publicly available in a form a SUT developer could use as
   a reward model or training signal.
2. **`answers_not_public`** — The evaluator's answers/outputs (its labels or scores that
   could be harvested as training data) are likewise not made publicly available.

**Strong positive signals:** an explicit statement that the evaluator is kept private or
gated; no public API or downloadable implementation of the judge; scores/answers not
released in a harvestable form; access mediated by the benchmark team to prevent reuse as
a reward model.

**Negative / disqualifying signals:** the evaluator model or code is published or exposed
via an open API; the evaluator's per-item answers/scores are released wholesale; the judge
can be queried freely by developers; withholding described only as a future plan; the
evaluator distributed alongside the benchmark for self-scoring.
