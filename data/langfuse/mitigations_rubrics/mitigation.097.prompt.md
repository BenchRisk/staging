# Mitigation 097 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #97, which mitigates Failure Mode #30.
Source: data/mitigations/97.mdx and data/modes/30.mdx.
-->

## The mitigation under review

- **Mitigation number:** 97
- **Mitigates failure mode:** #30 — *"Certain SUTs produce outputs with higher evaluator
  errors than other SUTs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~50%
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
> Is the system-under-test required to produce outputs that conform to the evaluator's
> expected format (e.g., true/false, multiple choice)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Template:** A root prompt from which structured changes facilitate interrogation of a
  SUT property subject to benchmark. Templates can constrain the expected response form
  (e.g., a fixed answer format) without necessarily having adversarial intent.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`constrained_output_format`** — The SUT is required to produce outputs in a
   constrained format the evaluator expects (e.g., true/false, multiple choice, a single
   token or fixed structure), reducing reliance on subjective surface features.
2. **`format_enforced_in_scoring`** — The expected format is enforced at evaluation time
   (e.g., prompts request the format and scoring parses/expects it), not merely suggested.

**Strong positive signals:** prompts that instruct the SUT to answer with A/B/C/D,
true/false, or a fixed schema; a parser or answer-extraction step that depends on the
constrained format; documentation stating outputs are scored only in the required format;
example items showing the enforced response form.

**Negative / disqualifying signals:** free-form, open-ended responses scored holistically;
no required output format described; format conformance left optional or only encouraged;
the constrained-format requirement described only for a planned version while the current
benchmark scores free text.
