# Mitigation 054 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #54, which mitigates Failure Mode #30.
Source: data/mitigations/54.mdx and data/modes/30.mdx.
-->

## The mitigation under review

- **Mitigation number:** 54
- **Mitigates failure mode:** #30 — *"Certain SUTs produce outputs with higher evaluator
  errors than other SUTs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates AI coding assistants
  using human evaluators to judge solution correctness. One SUT generates visually clean,
  well-commented code with excellent formatting that appears professional but contains
  subtle logical errors. Another SUT produces messier but functionally correct code.
  Evaluators consistently rate the first SUT's visually appealing but buggy code higher,
  leading to inflated scores. The benchmark user selects this SUT for a critical software
  development project, resulting in deployed code with hidden bugs that only manifest in
  production environments, causing system failures and data corruption that take months to
  diagnose and fix.

**Criterion question (answer this for the benchmark under review):**
> Do you conduct statistical analysis of evaluator (human, model, or algorithm) failures
> and prominently disclose any detected biases across all SUTs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators when assessing the same set of outputs. High interrater
  reliability indicates the evaluation criteria are well-defined and applied consistently;
  it is commonly quantified using measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluator_error_analysis`** — The benchmark conducts a statistical analysis of
   evaluator failures/errors (whether the evaluator is human, model, or algorithm).
2. **`per_sut_bias`** — The analysis examines evaluator error across all SUTs, surfacing
   whether certain SUTs incur systematically higher evaluator error or bias.
3. **`prominent_disclosure`** — Any detected evaluator biases are prominently disclosed
   where users encounter the results, not buried or omitted.

**Strong positive signals:** reported evaluator error rates or confusion analysis,
interrater reliability statistics (e.g., Cohen's kappa); a breakdown of evaluator
agreement/error by SUT; an explicit "evaluator limitations / known biases" section near
the results; calibration or audit of evaluators against ground truth.

**Negative / disqualifying signals:** no analysis of evaluator reliability; evaluator
error reported only in aggregate with no per-SUT view; biases acknowledged only vaguely or
buried in an appendix; bias analysis described only as future work.
