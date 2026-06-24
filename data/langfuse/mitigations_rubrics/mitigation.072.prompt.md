# Mitigation 072 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #72, which mitigates Failure Mode #21.
Source: data/mitigations/72.mdx and data/modes/21.mdx.
-->

## The mitigation under review

- **Mitigation number:** 72
- **Mitigates failure mode:** #21 — *"Prompts are sent to model vendors when inferencing
  or all prompts are publicly available"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~29.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses an API-based evaluation
  pipeline where prompts are sent directly to model vendors (e.g., OpenAI, Anthropic) for
  inference, or all prompts are published openly online. Model vendors are thus able to
  log, analyze, and optimize performance specifically on these benchmark prompts, either
  intentionally or as part of routine monitoring. This leads to inflated scores that do
  not reflect the models' generalization to unseen tasks. A benchmark user, unaware of
  this dynamic, interprets the scores as indicative of broader capability and deploys a
  system that underperforms on genuinely novel or proprietary tasks.

**Criterion question (answer this for the benchmark under review):**
> Do you verify with engineering staff of SUT developers that prompts will not be
> recorded? You may only consider this mitigation as applied when all relevant SUT
> engineering staffs affirm this.

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark, often planted
  deliberately to act as a warning signal.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`non_recording_verified`** — The benchmark verifies with the engineering staff of the
   SUT developers that benchmark prompts will not be recorded or retained for training.
2. **`all_relevant_staffs_affirm`** — Documents indicate that all relevant SUT
   engineering staffs affirmed this (per the criterion, the mitigation only counts when
   every relevant developer has affirmed non-recording).

**Strong positive signals:** a documented confirmation or agreement from each SUT
vendor's engineering staff that prompts are not logged/retained; an enumerated list of
SUTs with their respective affirmations; contractual or written assurances of
non-recording covering all evaluated systems.

**Negative / disqualifying signals:** prompts sent to vendor APIs with no non-recording
assurance; assurance obtained from only some vendors but not all evaluated SUTs; reliance
on vendors' default terms without explicit engineering confirmation; non-recording
verification described only as a future intention while published scores were collected
without it.
