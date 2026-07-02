# Mitigation 196 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #196, which mitigates Failure Mode #26.
Source: data/mitigations/196.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 196
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used
  in benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial
  errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human or automated
  evaluators to score model outputs in a target language, such as Swahili or Thai.
  However, since evaluators are primarily English-speaking, the model outputs are
  translated into English for scoring. The translation process introduces semantic
  shifts, idiomatic inaccuracies, or tone distortions that obscure the original meaning.
  Evaluators rate these mistranslated outputs, leading to misleadingly low or high scores
  depending on the nature of the translation errors. A benchmark user relies on these
  scores to select a model for multilingual deployment, only to discover that the model
  performs poorly in the actual target language due to evaluation artifacts that masked
  critical failures.

**Criterion question (answer this for the benchmark under review):**
> Do you check whether back-translating from the target language to the source language
> yields expressions consistent with the original language?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task — for instance, a
  speaker of a low-resource language for a translation benchmark.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`back_translation_performed`** — The documents describe back-translating the
   target-language *outputs presented to evaluators* (or the evaluation material) into
   the source language as a validation step.
2. **`consistency_checked`** — The back-translation is compared against the original
   target-language text for consistency (semantic, idiomatic, or tone), with a stated
   criterion or review process, to confirm evaluators scored faithful representations.
3. **`results_acted_on`** — The outcome is reported and used to validate or correct the
   evaluation material the evaluators were tuned/calibrated on in the currently published
   benchmark.

**Strong positive signals:** an explicit back-translation check on the material shown to
evaluators; comparison of back-translated vs. original output text; bilingual reviewers
or domain experts confirming evaluators saw faithful renderings; reported evaluator
calibration or scoring adjustments after the check.

**Negative / disqualifying signals:** outputs translated for scoring with no
reverse-translation validation; evaluators noted as non-native with no safeguard;
back-translation mentioned but not performed on the evaluation material; the check
described only for a future release while the published evaluation lacked it.
