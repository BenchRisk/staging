# Mitigation 081 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #81, which mitigates Failure Mode #26.
Source: data/mitigations/81.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 81
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used
  in benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial
  errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~50%
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
> For all languages benchmarked, do you validate evaluator versus native speaker response
> grading to ensure the error rate is consistent with the representations made to users?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to guide data interpretation and decision-making. For
  benchmarks, a domain expert knows about the SUT's task — for example, a speaker of a low
  resource language for a low resource language translation benchmark.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) assessing the same outputs. High interrater reliability
  indicates well-defined, consistently applied criteria and is commonly quantified using
  measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`native_speaker_validation`** — The evaluator's grading is validated against native
   speaker grading (or otherwise against trusted in-language reference judgments) for the
   benchmarked language(s).
2. **`error_rate_reported`** — A grading error rate or agreement measure between the
   evaluator and native speakers is quantified and reported.
3. **`consistent_with_representations`** — That error rate is shown to be consistent with
   the accuracy/quality claims represented to users about the scores.
4. **`all_languages_covered`** — The validation covers all languages the benchmark
   reports on, not just a single language or English-only.

**Strong positive signals:** a per-language comparison of evaluator vs. native-speaker
grades; reported agreement statistics (e.g., kappa, error rate) broken out by language; a
stated check that scoring is done in-language or that translation does not distort
grades; an explicit statement that measured error rates match the benchmark's accuracy
claims.

**Negative / disqualifying signals:** outputs translated to a single evaluator language
with no in-language validation; agreement reported for only one language while others go
unchecked; no error rate quantified at all; a generic claim of "expert annotators" with
no native-speaker comparison; validation promised for future languages but absent now.
