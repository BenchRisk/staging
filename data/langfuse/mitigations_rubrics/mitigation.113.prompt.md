# Mitigation 113 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #113, which mitigates Failure Mode #49.
Source: data/mitigations/113.mdx and data/modes/49.mdx.
-->

## The mitigation under review

- **Mitigation number:** 113
- **Mitigates failure mode:** #49 — *"SUT developer trains against evaluation set prior
  to benchmark release."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~70% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The developers of "InsightfulBot" develop
  a new question-answering benchmark. They then intentionally fine-tune InsightfulBot
  specifically on the exact questions and answers of the benchmark, optimizing performance
  on the metrics without improving its ability to generalize to novel queries. A user,
  impressed by InsightfulBot's top-ranking score posted on HuggingFace, assumes it
  possesses superior knowledge and reasoning. However, when they use it for real-world
  information retrieval with unseen questions, the model performs poorly, demonstrating
  that its benchmark success was an artifact of overfitting to the evaluation data rather
  than genuine intelligence.

**Criterion question (answer this for the benchmark under review):**
> Are there signed agreements with SUT developers that prohibit using the sample set for
> training?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Benchmark Integrity Requirements:** Standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, maintaining the
  trustworthiness of benchmarks. Violations include data snooping and benchmark
  overfitting (training on the evaluation set), among others.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`signed_agreement_exists`** — Access to the sample/evaluation set is governed by a
   signed agreement (contract, DUA, or equivalent) executed with SUT developers, not just
   an unsigned click-through or implicit terms.
2. **`prohibits_training_use`** — The agreement explicitly prohibits using the sample set
   for training the SUT.

**Strong positive signals:** a described data-use agreement or contract that recipients
must sign before access; explicit contractual language barring training on the items;
gated access conditioned on signing; a named process for executing agreements with
participating developers.

**Negative / disqualifying signals:** open access with no agreement at all; only an
unsigned license or terms-of-use (covered by a different mitigation); an agreement that
does not address training use; the agreement described as planned for a future release
while the current set is accessible without one.
