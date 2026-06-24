# Mitigation 151 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #151, which mitigates Failure Mode #24.
Source: data/mitigations/151.mdx and data/modes/24.mdx.
-->

## The mitigation under review

- **Mitigation number:** 151
- **Mitigates failure mode:** #24 — *"SUT is tested under conditions (e.g. temperature,
  iteration, context window settings) not matching deployment conditions or those
  conditions typically experienced by relying persons under default configurations"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark evaluates a system under
  optimal settings — low temperature for deterministic outputs, extended context windows,
  and multiple-shot prompting with carefully selected exemplars. However, real-world
  users typically interact with the system using default settings: higher temperature,
  single-shot prompts, and shorter contexts due to latency or cost constraints. As a
  result, the model's benchmark performance significantly overstates its real-world
  reliability and quality. A benchmark user assumes the model's benchmark score reflects
  the default configuration, deploys it in a customer-facing chatbot, and receives
  inconsistent, low-quality responses that degrade user trust and satisfaction.

**Criterion question (answer this for the benchmark under review):**
> Do you allow SUT developers a very limited number of evaluations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs — covering
  transparency, consistency, reproducibility, accountability, and independence. Examples
  of SUT-developer violations include data snooping and benchmark overfitting.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluation_count_limited`** — The benchmark limits each SUT developer to a very
   small number of evaluation submissions/attempts against the scored set, rather than
   allowing unlimited or unmonitored runs.
2. **`limit_is_enforced`** — This limit is stated and operationalized as a rule of the
   published benchmark (e.g., enforced by a submission server or accounting), not merely
   suggested.

**Strong positive signals:** an explicit per-team or per-model submission cap (e.g., "N
submissions allowed"); a gated submission server that tracks and rate-limits attempts;
rules describing throttling, cooldowns, or quotas on evaluation against the held-out set;
documented rationale tying the cap to preventing test-set overfitting.

**Negative / disqualifying signals:** unlimited self-service evaluation; no stated cap on
attempts; the test set is downloadable so attempts cannot be limited; the limit described
only as a planned policy for a future release; "limit" mentioned without any enforcement
mechanism.
