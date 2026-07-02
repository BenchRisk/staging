# Mitigation 050 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #50, which mitigates Failure Mode #29.
Source: data/mitigations/50.mdx and data/modes/29.mdx.
-->

## The mitigation under review

- **Mitigation number:** 50
- **Mitigates failure mode:** #29 — *"SUT developers produce training data from
  evaluator"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** Developers of a SUT gain access to the
  benchmark evaluator — either by reverse-engineering a public implementation or through a
  public API — and use it as a reward model or filtering mechanism during training or
  fine-tuning. This causes the model to optimize specifically for evaluator preferences,
  potentially learning to game the scoring mechanism through superficial alignment (e.g.,
  mimicking surface features that score well, like formality or verbosity) rather than
  achieving true task performance. As a result, the model performs exceptionally well on
  the benchmark but fails to generalize to tasks that aren't shaped by the evaluator's
  biases. A benchmark user, unaware of this overfitting loop, selects the system expecting
  robust general capabilities, only to encounter brittle outputs.

**Criterion question (answer this for the benchmark under review):**
> Do you use 100% human evaluators for assessing system performance?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, consistency, reproducibility, accountability, and independence. SUT
  developers can violate them through practices such as benchmark overfitting and data
  snooping.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_evaluation`** — The benchmark's scores are produced by human evaluators
   assessing SUT performance, rather than by an automated model or algorithmic evaluator
   that a SUT developer could distill or optimize against.
2. **`fully_human`** — Human evaluation covers 100% of the assessed outputs; scoring does
   not rely on a reusable model-based evaluator that could serve as a reward model or
   filter during SUT training.

**Strong positive signals:** an explicit statement that all assessment is performed by
human evaluators; no shipped or queryable model evaluator that a SUT developer could
optimize against; described human rater pools and adjudication for every assessed output.

**Negative / disqualifying signals:** scores produced by an automated/model-based
evaluator (LLM-as-judge, classifier, reward model), especially one exposed via a public
API or open implementation; only a sample of outputs human-reviewed while the rest are
auto-graded; human review described only as a future or spot-check measure.
