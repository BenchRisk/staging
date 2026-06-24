# Mitigation 076 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #76, which mitigates Failure Mode #41.
Source: data/mitigations/76.mdx and data/modes/41.mdx.
-->

## The mitigation under review

- **Mitigation number:** 76
- **Mitigates failure mode:** #41 — *"SUT developer tunes safety program to benchmark
  sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~0.0%
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
> Does your license prohibit tuning to the sample set?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs. Violations
  include data snooping and benchmark overfitting (e.g., tuning a system to the benchmark
  sample set).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`license_prohibits_tuning`** — The benchmark's license (or equivalent published terms
   of use) explicitly prohibits tuning, training, or fine-tuning systems on the released
   sample set.

**Strong positive signals:** an explicit license or terms-of-use clause forbidding
training/fine-tuning on the sample prompts; a stated usage restriction tied to the
released subset; license text that distinguishes permitted evaluation use from prohibited
tuning use.

**Negative / disqualifying signals:** the sample set released under a permissive license
with no anti-tuning clause; no license or usage terms governing the released prompts;
only an informal request not to train on the data (no license prohibition); an anti-tuning
clause described as planned for a future license while the published release lacks it.
