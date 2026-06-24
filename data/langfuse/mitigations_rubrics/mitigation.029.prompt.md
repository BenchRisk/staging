# Mitigation 029 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #29, which mitigates Failure Mode #26.
Source: data/mitigations/29.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 29
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used
  in benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial
  errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~25.0%
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
> Do you validate all machine-translated prompts using a highly qualified speaker fluent
> in both source and target languages?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide interpretation. For a
  low-resource language benchmark, a domain expert includes a fluent speaker of the
  language in question.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_validation`** — Machine-translated text feeding the evaluator (the translated
   outputs or prompts the evaluator is tuned on) is validated by a human speaker who is
   highly qualified and fluent in **both** the source and target languages.
2. **`all_translations_covered`** — That validation covers **all** machine-translated
   material used by the published benchmark's evaluation, not just a sampled subset.

**Strong positive signals:** a stated bilingual human-validation step for every
translated output/prompt used in scoring; named fluency/qualifications of the validators
in both languages; a correction or adjudication step for translation errors before
evaluation; documentation that the evaluator was tuned only on human-verified
translations.

**Negative / disqualifying signals:** the evaluator scores machine-translated text with
no human verification; only a subset of translations is checked; validators' bilingual
fluency unstated; validation described as planned/future; reliance on the translation
tool's quality without speaker review.
