# Mitigation 110 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #110, which mitigates Failure Mode #49.
Source: data/mitigations/110.mdx and data/modes/49.mdx.
-->

## The mitigation under review

- **Mitigation number:** 110
- **Mitigates failure mode:** #49 — *"SUT developer trains against evaluation set prior
  to benchmark release."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~12.5%
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
> Do you add a globally unique identifier or apply encryption to evaluation instances?

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

1. **`identifier_or_encryption_applied`** — The benchmark attaches a globally unique
   identifier (e.g., a canary string/GUID) to evaluation instances, or distributes/stores
   the evaluation instances in encrypted form.
2. **`contamination_detection_purpose`** — The identifier or encryption is described as
   serving to detect or prevent training on the evaluation set (data contamination), not
   merely as a generic bookkeeping or storage convenience.

**Strong positive signals:** a published canary GUID string with instructions to exclude
it from training; evaluation instances tagged with unique IDs to enable contamination
checks; encrypted distribution of the test set with a stated anti-leakage rationale;
documented procedure for detecting the identifier in model outputs.

**Negative / disqualifying signals:** evaluation instances released in plaintext with no
identifiers; IDs present only for internal indexing with no contamination purpose; the
canary/encryption described as planned for a future release; no mention of unique
identifiers or encryption anywhere in the documents.
