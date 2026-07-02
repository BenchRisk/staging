# Mitigation 053 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #53, which mitigates Failure Mode #24.
Source: data/mitigations/53.mdx and data/modes/24.mdx.
-->

## The mitigation under review

- **Mitigation number:** 53
- **Mitigates failure mode:** #24 — *"SUT is tested under conditions (e.g. temperature,
  iteration, context window settings) not matching deployment conditions or those
  conditions typically experienced by relying persons under default configurations"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~25.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark evaluates a system under
  optimal settings — low temperature for deterministic outputs, extended context windows,
  and multiple-shot prompting with carefully selected exemplars. However, real-world users
  typically interact with the system using default settings: higher temperature,
  single-shot prompts, and shorter contexts due to latency or cost constraints. As a
  result, the model's benchmark performance significantly overstates its real-world
  reliability and quality. A benchmark user assumes the model's benchmark score reflects
  the default configuration, deploys it in a customer-facing chatbot, and receives
  inconsistent, low-quality responses that degrade user trust and satisfaction.

**Criterion question (answer this for the benchmark under review):**
> Do you require that the system configuration (e.g., temperature, system prompts) used in
> benchmarking matches either the system's default user-facing settings or those clearly
> recommended in vendor guidelines for the intended use case?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be understood
  by intended users, ensuring they can accurately interpret and use the benchmark for
  real-world decisions. It asks, "will the relying user understand the LLM properties as
  evidenced by the benchmark?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system under
  test (SUT), ensuring conditions for testing accurately reflect intended operational
  contexts.
- **Temperature:** A parameter used in Large Language Models (LLMs) that controls the
  randomness of outputs during text generation. It influences how predictable or creative
  the model's responses will be.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`config_disclosed`** — The benchmark documents the system configuration used during
   benchmarking (e.g., temperature, system prompts, context window, shot count).
2. **`matches_default_or_recommended`** — That configuration is stated to match either the
   system's default user-facing settings or the vendor's clearly recommended settings for
   the intended use case, rather than tuned-for-benchmark optimal settings.

**Strong positive signals:** an explicit table of inference settings per SUT; a stated
policy to use each model's default or vendor-recommended configuration; justification
tying chosen settings to real deployment/use-case guidelines; default temperature and
standard prompting (e.g., single-shot) used when that reflects typical use.

**Negative / disqualifying signals:** undisclosed inference settings; settings hand-tuned
for best benchmark scores (e.g., temperature 0, many-shot, extended context) with no link
to default or recommended use; configuration matching described only as a future plan;
each SUT tuned differently with no stated default-matching rule.
