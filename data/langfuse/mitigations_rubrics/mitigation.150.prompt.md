# Mitigation 150 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #150, which mitigates Failure Mode #24.
Source: data/mitigations/150.mdx and data/modes/24.mdx.
-->

## The mitigation under review

- **Mitigation number:** 150
- **Mitigates failure mode:** #24 — *"SUT is tested under conditions (e.g. temperature,
  iteration, context window settings) not matching deployment conditions or those
  conditions typically experienced by relying persons under default configurations"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~12.5%
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
> Do you avoid providing a sample set that would allow for tuning hyperparameters on the
> test set and do you avoid publishing the evaluation set?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark. It is often
  planted deliberately to act as a warning signal (like a "canary in a coal mine").
- **Temperature:** A parameter used in Large Language Models that controls the randomness
  of outputs during text generation. It influences how predictable or creative the
  model's responses will be.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_tunable_sample_set`** — The benchmark avoids providing a sample/development set
   that would let SUT developers tune hyperparameters (e.g., temperature, context window,
   shot count) on data representative of the test set.
2. **`evaluation_set_unpublished`** — The benchmark avoids publishing the evaluation
   (test) set, keeping the scored items held out rather than openly released.

**Strong positive signals:** an explicit held-out / private evaluation set; statement
that no public sample set is provided for tuning, or that any released examples are
deliberately non-representative; access to the test set gated through a submission
harness rather than open download; documented separation between any public examples and
the scored set.

**Negative / disqualifying signals:** the full evaluation set is published/downloadable;
a sample/dev set explicitly intended for tuning that mirrors the test distribution;
hyperparameters openly fit on released data; the held-out arrangement described only as a
planned future change.
