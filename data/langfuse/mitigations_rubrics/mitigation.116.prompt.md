# Mitigation 116 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #116, which mitigates Failure Mode #50.
Source: data/mitigations/116.mdx and data/modes/50.mdx.
-->

## The mitigation under review

- **Mitigation number:** 116
- **Mitigates failure mode:** #50 — *"SUT developer trains against evaluation set after
  benchmark release."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~20.83%
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
> Are there signed agreements with SUT developers that specifically prohibit training
> with the evaluation set?

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

1. **`signed_agreement_exists`** — Access to the evaluation set is governed by a signed
   agreement (contract, DUA, or equivalent) executed with SUT developers, not just an
   unsigned click-through or implicit terms.
2. **`prohibits_training_use`** — The agreement specifically prohibits training the SUT
   with the evaluation set.

**Strong positive signals:** a described data-use agreement or contract that recipients
must sign before access; explicit contractual language barring training on the evaluation
items; gated access conditioned on signing; a named process for executing agreements with
participating developers and enforcing the no-training term over time.

**Negative / disqualifying signals:** open access with no agreement at all; only an
unsigned license or terms-of-use (covered by a different mitigation); an agreement silent
on training use; the agreement described as planned for a future release while the current
set is accessible without one.
