# Mitigation 112 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #112, which mitigates Failure Mode #49.
Source: data/mitigations/112.mdx and data/modes/49.mdx.
-->

## The mitigation under review

- **Mitigation number:** 112
- **Mitigates failure mode:** #49 — *"SUT developer trains against evaluation set prior
  to benchmark release."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~90% reduction in failure-mode likelihood; ~0%
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
> Do you refrain from providing the evaluation set to prevent potential misuse?

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

1. **`eval_set_withheld`** — The full evaluation set (the prompts and/or answers used for
   scoring) is not publicly released; it is held back rather than openly distributed.
2. **`withholding_to_prevent_misuse`** — The documents state that the evaluation set is
   withheld specifically to prevent misuse such as training on it / contamination, not
   merely for unrelated reasons (e.g., file size or licensing of source material).

**Strong positive signals:** a private/held-out test set with submission via an
evaluation server or harness; an explicit statement that test items are not released to
prevent overfitting/contamination; only a public dev/validation split released while the
test split is withheld; gated access controls described.

**Negative / disqualifying signals:** the entire evaluation set published openly (e.g.,
all questions and answers on HuggingFace); the test answers downloadable by anyone; no
statement that withholding is for misuse prevention; withholding described as a future
plan while the current release exposes the evaluation set.
