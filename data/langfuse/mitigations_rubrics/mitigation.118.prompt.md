# Mitigation 118 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #118, which mitigates Failure Mode #49.
Source: data/mitigations/118.mdx and data/modes/49.mdx.
-->

## The mitigation under review

- **Mitigation number:** 118
- **Mitigates failure mode:** #49 — *"SUT developer trains against evaluation set prior
  to benchmark release."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~25%
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
> Do you include canary data in the prompt set such that its inclusion in training would
> enable testing whether the model has been trained on the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark. It is often
  planted deliberately to act as a warning signal (like a "canary in a coal mine").
- **Benchmark Integrity Requirements:** Standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, maintaining the
  trustworthiness of benchmarks. Violations include data snooping and benchmark
  overfitting (training on the evaluation set), among others.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`canary_included`** — The prompt set includes canary data (e.g., a unique canary
   string/GUID or planted marker items) embedded in the published benchmark.
2. **`enables_contamination_test`** — The canary is described such that its appearance in
   a model's training or outputs would let one test whether the SUT was trained on the
   benchmark (a stated detection mechanism), not merely a generic identifier.

**Strong positive signals:** a published canary GUID string with instructions to exclude
it from training; planted unique marker items whose recall by a model signals
contamination; a documented method for probing whether a model has ingested the canary;
explicit framing of the canary as a leakage/contamination detector.

**Negative / disqualifying signals:** no canary or planted markers anywhere; unique IDs
present only for indexing with no detection purpose; the canary described as planned for a
future release; the contamination-test mechanism not described, so the marker could not
actually reveal training on the benchmark.
