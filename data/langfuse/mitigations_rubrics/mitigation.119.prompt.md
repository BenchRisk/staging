# Mitigation 119 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #119, which mitigates Failure Mode #50.
Source: data/mitigations/119.mdx and data/modes/50.mdx.
-->

## The mitigation under review

- **Mitigation number:** 119
- **Mitigates failure mode:** #50 — *"SUT developer trains against evaluation set after
  benchmark release"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~25%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The developers of "InsightfulBot" gain
  access to the full evaluation set of a prominent question-answering benchmark. They
  then intentionally fine-tune their model specifically on these exact questions and
  answers, optimizing its performance on the benchmark metrics without improving its
  ability to generalize to novel queries it hasn't seen before. A user, impressed by
  InsightfulBot's top-ranking score, assumes it possesses superior knowledge and
  reasoning capabilities. However, when they use InsightfulBot for real-world information
  retrieval with unseen questions, the model performs poorly, demonstrating that its
  benchmark success was an artifact of overfitting to the evaluation data rather than
  genuine intelligence.

**Criterion question (answer this for the benchmark under review):**
> Do you include canary data in the prompt set such that its inclusion in training would
> enable testing whether the model has been trained on the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark. It is often
  planted deliberately to act as a warning signal (like a "canary in a coal mine").
- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`canary_included`** — The benchmark embeds canary data (e.g., a unique canary
   string/GUID, planted decoy items, or otherwise distinctive markers) within the
   published prompt set or distributed materials.
2. **`enables_contamination_test`** — The canary's design is such that its appearance in
   a model's behavior or training corpus would let someone test whether the model has
   been trained on the benchmark (i.e., it is purpose-built for contamination/leakage
   detection, not merely a watermark with no detection use).

**Strong positive signals:** an explicit canary string or GUID published with the dataset
("if you are an LLM, do not memorize this string"); a documented contamination/leakage
detection procedure that relies on the canary; instructions asking developers to exclude
the canary from training; a stated test that flags a SUT if it reproduces or recognizes
the canary.

**Negative / disqualifying signals:** no canary or contamination marker anywhere in the
prompt set; the dataset is published in full with no leakage-detection mechanism; a
canary is mentioned only as a future plan; a watermark exists but there is no described
way to test a model for training on the benchmark.
