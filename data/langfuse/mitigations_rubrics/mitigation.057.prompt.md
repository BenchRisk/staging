# Mitigation 057 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #57, which mitigates Failure Mode #41.
Source: data/mitigations/57.mdx and data/modes/41.mdx.
-->

## The mitigation under review

- **Mitigation number:** 57
- **Mitigates failure mode:** #41 — *"SUT developer tunes safety program to benchmark
  sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~96.67% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark releases a subset of its
  prompts for transparency and community analysis. A system developer then uses this
  released set during training by sampling its prompts directly. As a result, the
  developer's system performs exceptionally well on the benchmark due to closely aligned
  fine-tuning. However, the model lacks true generalization and performs poorly on tasks
  that deviate even slightly from the benchmark format. The benchmark user interprets the
  high score as evidence of broad competence and deploys the system in a new domain, only
  to discover critical failures when the prompts fall outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you intentionally avoid providing a representative sample set (i.e., a dataset
> illustrative of the characteristics of the prompts included within the test set)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness, comprehensiveness,
  consistency, and intelligibility through time subject to gaming or changing
  circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Canary Data:** Specially crafted benchmark data used to detect developer or evaluation
  practices likely to compromise benchmark reliability. It is often planted deliberately
  to act as a warning signal (like a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_representative_sample_released`** — The benchmark intentionally does not publish a
   representative sample set illustrative of the test-set prompt characteristics, so SUT
   developers cannot tune to it.

**Strong positive signals:** an explicit statement that no representative/illustrative
sample of test prompts is released; a held-out or private test set with documented access
controls; canary data or contamination safeguards to detect training on the set; a stated
policy against publishing examples that reveal test-set characteristics.

**Negative / disqualifying signals:** a representative or illustrative sample of test
prompts is publicly released; the full or sampled test set is downloadable; example
prompts shared that disclose the test distribution; withholding described only as a future
intention while examples are currently public.
