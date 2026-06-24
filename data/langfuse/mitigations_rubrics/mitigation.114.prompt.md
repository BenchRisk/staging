# Mitigation 114 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #114, which mitigates Failure Mode #49.
Source: data/mitigations/114.mdx and data/modes/49.mdx.
-->

## The mitigation under review

- **Mitigation number:** 114
- **Mitigates failure mode:** #49 — *"SUT developer trains against evaluation set prior
  to benchmark release."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~4.17%
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
> Does the license explicitly prohibit using the sample set for training, even if the
> sample set is available without a signed agreement?

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

1. **`license_present`** — The sample/evaluation set is distributed under a stated license
   or terms of use that govern its permitted uses, even though access does not require a
   signed agreement.
2. **`license_prohibits_training`** — That license explicitly forbids using the sample set
   to train the SUT (e.g., a no-training / evaluation-only clause), not merely a generic
   open license.

**Strong positive signals:** an evaluation-only or no-derivatives/no-training clause in
the dataset license; license text on the dataset card stating items may not be used for
model training; a clearly labeled "for evaluation only" license attached to the openly
available set.

**Negative / disqualifying signals:** released under a permissive license (e.g., MIT,
CC-BY) that permits training; no license stated at all; the license is silent on training
use; the no-training license described as planned while the current release ships under a
permissive one.
