# Mitigation 047 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #47, which mitigates Failure Mode #26.
Source: data/mitigations/47.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 47
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used in
  benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human or automated
  evaluators to score model outputs in a target language, such as Swahili or Thai.
  However, since evaluators are primarily English-speaking, the model outputs are
  translated into English for scoring. The translation process introduces semantic shifts,
  idiomatic inaccuracies, or tone distortions that obscure the original meaning. Evaluators
  rate these mistranslated outputs, leading to misleadingly low or high scores depending on
  the nature of the translation errors. A benchmark user relies on these scores to select a
  model for multilingual deployment, only to discover that the model performs poorly in the
  actual target language due to evaluation artifacts that masked critical failures.

**Criterion question (answer this for the benchmark under review):**
> Do you use 100% human evaluators for assessing system performance?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property. This mitigation asks
  whether that evaluator is 100% human.
- **Domain Expert:** An individual possessing specialized knowledge in a particular area
  or, for benchmarks, knowledge of the SUT task — for example a speaker of a low-resource
  language for a low-resource-language translation benchmark. Such expertise bears on
  whether human evaluators can judge target-language outputs without translation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_evaluation`** — The benchmark's outputs are scored by human evaluators.
2. **`fully_human_no_automated_judge`** — Evaluation is 100% human: there is no
   LLM-as-a-judge or other automated evaluator producing the published scores.

**Strong positive signals:** an explicit statement that all outputs are scored by human
raters; described human annotation protocols and rater qualifications; evaluators who
judge outputs in their original (e.g., target-language) form; no automated judge in the
scoring pipeline.

**Negative / disqualifying signals:** an LLM-as-a-judge or automated classifier producing
the scores; a hybrid setup where machines do most grading; humans used only to tune or
validate an automated evaluator that still produces the published scores; full human
evaluation described only as a future plan.
