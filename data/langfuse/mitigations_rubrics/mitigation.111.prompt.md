# Mitigation 111 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #111, which mitigates Failure Mode #50.
Source: data/mitigations/111.mdx and data/modes/50.mdx.
-->

## The mitigation under review

- **Mitigation number:** 111
- **Mitigates failure mode:** #50 — *"SUT developer trains against evaluation set after
  benchmark release."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~0%
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
> Do you add a globally unique identifier or apply encryption to evaluation instances?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding against
  data leakage, and maintaining consistency of evaluation conditions.
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

1. **`identifier_or_encryption_applied`** — The benchmark attaches a globally unique
   identifier (e.g., a canary string/GUID) to evaluation instances, or distributes/stores
   the evaluation instances in encrypted form.
2. **`post_release_leakage_purpose`** — The identifier or encryption is described as
   guarding against post-release contamination — detecting or deterring training on the
   evaluation set after the benchmark has been published.

**Strong positive signals:** a published canary GUID string with instructions to exclude
it from training corpora; encrypted distribution of the live test set with a stated
anti-leakage rationale; a documented method for checking whether a post-release model has
ingested the identifier; ongoing-maintenance text describing leakage monitoring.

**Negative / disqualifying signals:** the full evaluation set released in plaintext with
no identifiers and no leakage safeguards; IDs used only for internal indexing; the
canary/encryption described as planned but not yet applied; no mention of unique
identifiers or encryption guarding against post-release data leakage.
