# Mitigation 117 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #117, which mitigates Failure Mode #50.
Source: data/mitigations/117.mdx and data/modes/50.mdx.
-->

## The mitigation under review

- **Mitigation number:** 117
- **Mitigates failure mode:** #50 — *"SUT developer trains against evaluation set after
  benchmark release."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The developers of "InsightfulBot" gain
  access to the full evaluation set of a prominent question-answering benchmark. They then
  intentionally fine-tune their model specifically on these exact questions and answers,
  optimizing its performance on the benchmark metrics without improving its ability to
  generalize to novel queries. A user, impressed by InsightfulBot's top-ranking score,
  assumes it possesses superior knowledge and reasoning. However, when they use it for
  real-world information retrieval with unseen questions, the model performs poorly,
  demonstrating that its benchmark success was an artifact of overfitting to the
  evaluation data rather than genuine intelligence.

**Criterion question (answer this for the benchmark under review):**
> Does the license explicitly prohibit training with the evaluation set, even when it
> might be available without a signed agreement?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding against
  data leakage, and maintaining consistency of evaluation conditions.
- **Benchmark Integrity Requirements:** Standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, maintaining the
  trustworthiness of benchmarks. Violations include data snooping and benchmark
  overfitting (training on the evaluation set), among others.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`license_present`** — The evaluation set is distributed under a stated license or
   terms of use that govern its permitted uses, even though access does not require a
   signed agreement.
2. **`license_prohibits_training`** — That license explicitly forbids training the SUT
   with the evaluation set (e.g., a no-training / evaluation-only clause), not merely a
   generic open license.

**Strong positive signals:** an evaluation-only or no-training clause in the dataset
license; license text on the dataset card stating items may not be used for model
training; a clearly labeled "for evaluation only" license attached to the openly
available evaluation set.

**Negative / disqualifying signals:** released under a permissive license (e.g., MIT,
CC-BY) that permits training; no license stated at all; the license is silent on training
use; the no-training license described as planned while the current release ships under a
permissive one.
