# Mitigation 067 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #67, which mitigates Failure Mode #46.
Source: data/mitigations/67.mdx and data/modes/46.mdx.
-->

## The mitigation under review

- **Mitigation number:** 67
- **Mitigates failure mode:** #46 — *"SUT developers can run the benchmark an unlimited
  number of times"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark allows SUT developers to submit
  their models for evaluation as many times as they wish. The developers of "NovaMind"
  repeatedly run the benchmark, meticulously analyzing the failure cases after each run.
  They then fine-tune their model specifically to improve its performance on the exact
  prompts and evaluation metrics of the benchmark, without necessarily improving its
  generalization. A benchmark user, seeing the consistently high scores of "NovaMind,"
  selects it believing it to be a robust and generally capable model. However, in
  real-world applications with slightly different inputs or evaluation criteria,
  "NovaMind" underperforms significantly because its apparent success was largely due to
  overfitting to the specific nuances of the benchmark.

**Criterion question (answer this for the benchmark under review):**
> Do you restrict or avoid evaluation on demand to preserve benchmark integrity?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, consistency, reproducibility, accountability, and update mechanisms.
  Violations include data snooping and benchmark overfitting.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluation_access_restricted`** — The benchmark restricts or avoids on-demand,
   unlimited evaluation (e.g., submission rate limits, capped attempts per developer, a
   held-out test set evaluated by the maintainers, or gated submission) to prevent
   repeated tuning against it.

**Strong positive signals:** a stated submission limit or cooldown; a private/held-out
test set scored only by the maintainers; a documented submission policy that detects or
prevents repeated runs; controlled access rather than open self-service evaluation.

**Negative / disqualifying signals:** developers can self-submit or run the benchmark
without limit; the full test set and scoring are openly runnable any number of times; no
policy addressing repeated evaluation or overfitting; access restrictions described only
as a future plan while the published benchmark allows unlimited runs.
