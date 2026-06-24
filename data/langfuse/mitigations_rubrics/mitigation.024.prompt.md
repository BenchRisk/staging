# Mitigation 024 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #24, which mitigates Failure Mode #21.
Source: data/mitigations/24.mdx and data/modes/21.mdx.
-->

## The mitigation under review

- **Mitigation number:** 24
- **Mitigates failure mode:** #21 — *"Prompts are sent to model vendors when inferencing
  or all prompts are publicly available."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~100.0% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses an API-based
  evaluation pipeline where prompts are sent directly to model vendors (e.g., OpenAI,
  Anthropic) for inference, or all prompts are published openly online. Model vendors are
  thus able to log, analyze, and optimize performance specifically on these benchmark
  prompts, either intentionally or as part of routine monitoring. This leads to inflated
  scores that do not reflect the models' generalization to unseen tasks. A benchmark
  user, unaware of this dynamic, interprets the scores as indicative of broader
  capability and deploys a system that underperforms on genuinely novel or proprietary
  tasks.

**Criterion question (answer this for the benchmark under review):**
> (This mitigation may only be considered as applied when the prompts are never available
> to the SUT developer) Do you ensure that prompts are not shared with SUT developers
> during inferencing?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts are central to
  evaluating SUT performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`prompts_never_shared`** — The documents establish that the benchmark prompts are
   **never** made available to the SUT developer during inferencing — i.e., they are not
   sent to model vendors in a way that exposes them and are not published openly.
2. **`inference_isolation`** — Inferencing is run under an arrangement that keeps prompts
   inaccessible to the developer (e.g., the benchmark team controls execution, or prompts
   are protected/held out so the vendor cannot retain them).

Note: per the criterion's own qualifier, treat this mitigation as applicable only when
the documents support that prompts are *never* available to the SUT developer; any
exposure pathway should preclude an **adopted** verdict.

**Strong positive signals:** a held-out/private prompt set never disclosed to vendors;
benchmark-controlled inference that prevents the developer from accessing prompts;
explicit statements that prompts are not published and not shared with model providers;
an architecture that isolates prompts from SUT developers.

**Negative / disqualifying signals:** prompts sent to vendor APIs that may log or train
on them; all prompts published openly; any pathway by which the SUT developer can observe
the prompts; isolation described only as a future plan; silence about whether vendors
retain submitted prompts.
