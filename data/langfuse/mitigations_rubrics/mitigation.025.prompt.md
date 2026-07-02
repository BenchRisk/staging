# Mitigation 025 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #25, which mitigates Failure Mode #21.
Source: data/mitigations/25.mdx and data/modes/21.mdx.
-->

## The mitigation under review

- **Mitigation number:** 25
- **Mitigates failure mode:** #21 — *"Prompts are sent to model vendors when inferencing
  or all prompts are publicly available."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~20.83%
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
> (This mitigation may only be considered as applied when the prompts are only processed
> under contract) Do you include contractual prohibitions both against logging test runs
> and for allowing human review of test prompts?

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

1. **`no_logging_clause`** — A contractual agreement with the processor (e.g., the model
   vendor) prohibits logging or retaining the benchmark test runs/prompts.
2. **`no_human_review_clause`** — That same contractual arrangement prohibits human
   review of the test prompts by the processor.

Note: per the criterion's own qualifier, treat this mitigation as applicable only when
prompts are processed **under contract**; both the no-logging and no-human-review
prohibitions must be present for an **adopted** verdict.

**Strong positive signals:** an explicit data-processing or evaluation agreement citing
no-retention/no-logging terms; a contractual no-human-review or zero-retention clause for
the prompts; reference to a vendor's enterprise/no-training agreement covering the
benchmark runs; documentation that inferencing occurs only under such contractual terms.

**Negative / disqualifying signals:** prompts sent to a vendor with no stated contractual
protections; only one of the two prohibitions present (logging or human review, not
both); reliance on default API terms that permit logging or review; contractual terms
described as intended but not in force for the current benchmark.
