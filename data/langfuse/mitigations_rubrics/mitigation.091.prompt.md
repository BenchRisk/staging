# Mitigation 091 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #91, which mitigates Failure Mode #23.
Source: data/mitigations/91.mdx and data/modes/23.mdx.
-->

## The mitigation under review

- **Mitigation number:** 91
- **Mitigates failure mode:** #23 — *"SUT developer trains against sample prompt set"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~25%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A company preparing to release a new model
  with new capabilities also produces a new benchmark to evaluate those capabilities. The
  organization maintains a separation between the benchmark team and the SUT development
  team, but the benchmark team provides a sample test early in the development process. The
  SUT team then uses this released set during training by sampling prompts with similar
  structure, linguistic style, and distribution. As a result, the developer's system
  performs exceptionally well on the benchmark due to fine-tuning on closely aligned
  prompts. However, the model lacks true generalization and performs poorly on tasks that
  deviate even slightly from the benchmark format. The benchmark user interprets the high
  score as evidence of broad competence and deploys the system in a new domain, only to
  discover critical failures when the prompts fall outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you include canary data in the prompt set that would reveal if the benchmark was used
> in model training, enabling detection of training contamination?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system under
  test (SUT), ensuring conditions for testing accurately reflect intended operational
  contexts.
- **Canary Data:** Specially crafted benchmark data used to detect developer or evaluation
  practices likely to compromise the reliability of a benchmark. It is often planted
  deliberately to act as a warning signal (like a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`canary_present`** — The benchmark embeds canary data (e.g., a unique canary GUID,
   marker strings, or deliberately planted distinctive items) within or alongside the
   prompt set.
2. **`detects_contamination`** — The documents explain that this canary data is intended
   to reveal whether the benchmark was used in model training — i.e., it enables detection
   of training contamination, not merely tracking provenance for unrelated reasons.

**Strong positive signals:** an explicit canary string / canary GUID published with the
dataset; instructions asking developers to exclude the canary from training corpora; a
described procedure for checking whether a SUT reproduces or recognizes the canary; a
stated contamination-detection or data-leakage protocol tied to the prompt set.

**Negative / disqualifying signals:** no mention of canaries, markers, or contamination
detection; only a generic request "please do not train on this data" with no detectable
signal embedded; canary or contamination handling described only for a future release;
the prompt set is fully public with no mechanism to detect that it leaked into training.
