# Mitigation 152 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #152, which mitigates Failure Mode #26.
Source: data/mitigations/152.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 152
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used
  in benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial
  errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~37.5%
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
> Does the benchmark avoid testing concepts related to language (i.e., inputs and outputs
> are not textual)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`non_textual_io`** — The benchmark does not test language-related concepts: its
   inputs and outputs are non-textual (e.g., numeric, symbolic, structural, or executable
   artifacts) rather than natural-language text.
2. **`evaluation_language_independent`** — Because the outputs are non-textual, scoring
   does not require any evaluator to read, translate, or interpret natural-language
   content, removing the translation-error pathway in the failure mode.

**Strong positive signals:** an explicit statement that inputs/outputs are non-textual
and that grading operates on non-language artifacts (exact match, execution result,
numeric comparison); no human or LLM judge interpreting natural-language meaning; no
translation step in the evaluation pipeline.

**Negative / disqualifying signals:** outputs are natural-language text that must be read
or judged for meaning; evaluators (human or LLM-as-judge) score textual responses; any
translation of outputs prior to scoring; the non-textual claim asserted only for a future
version while the current benchmark scores text.
