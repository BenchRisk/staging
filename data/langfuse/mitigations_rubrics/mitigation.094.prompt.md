# Mitigation 094 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #94, which mitigates Failure Mode #26.
Source: data/mitigations/94.mdx and data/modes/26.mdx.
-->

## The mitigation under review

- **Mitigation number:** 94
- **Mitigates failure mode:** #26 — *"Evaluator (humans labeling the final outputs used in
  benchmarking or an LLM-as-a-judge) tuned on translated outputs with substantial errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~8.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human or automated
  evaluators to score model outputs in a target language, such as Swahili or Thai. However,
  since evaluators are primarily English-speaking, the model outputs are translated into
  English for scoring. The translation process introduces semantic shifts, idiomatic
  inaccuracies, or tone distortions that obscure the original meaning. Evaluators rate these
  mistranslated outputs, leading to misleadingly low or high scores depending on the nature
  of the translation errors. A benchmark user relies on these scores to select a model for
  multilingual deployment, only to discover that the model performs poorly in the actual
  target language due to evaluation artifacts that masked critical failures.

**Criterion question (answer this for the benchmark under review):**
> Can you confirm that no data vendors were used and that the evaluation data was not
> machine-translated, based on direct observation of practices?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For a low
  resource language benchmark, a domain expert includes a speaker of that language; a
  person need not have formal training where they have significant experience and knowledge
  within the domain.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_data_vendors`** — The documents confirm, based on direct observation of practice,
   that no third-party data vendors supplied the evaluation data.
2. **`not_machine_translated`** — The documents confirm the evaluation data (and outputs
   scored) were not machine-translated — evaluators assess outputs in the original test
   language rather than a translated rendering.
3. **`based_on_direct_observation`** — The confirmation rests on direct observation of
   practices (e.g., documented, audited, or first-hand procedure) rather than an
   unsupported assurance.

**Strong positive signals:** a documented evaluation procedure stating outputs were scored
in the original language by fluent evaluators; an explicit statement that no machine
translation was applied to evaluation data; an audit, log, or first-hand process
description of how evaluation data was produced; named in-language evaluators rather than
an outsourced vendor.

**Negative / disqualifying signals:** evaluation outputs translated (machine or otherwise)
before scoring; reliance on an unnamed data vendor for evaluation data; only a bare claim
with no procedure or observation backing it; in-language evaluation described only as a
planned improvement.
