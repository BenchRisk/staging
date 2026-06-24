# Mitigation 155 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #155, which mitigates Failure Mode #30.
Source: data/mitigations/155.mdx and data/modes/30.mdx.
-->

## The mitigation under review

- **Mitigation number:** 155
- **Mitigates failure mode:** #30 — *"Certain SUTs produce outputs with higher evaluator
  errors than other SUTs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~41.67%
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
> Does the benchmark use singular answers (i.e., bit-exact outputs) that are checked via a
> lookup table?

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

1. **`bit_exact_answers`** — Each item has a singular, bit-exact correct output (an exact
   canonical string/value), not a judgment of relative quality.
2. **`lookup_table_check`** — Grading is performed by checking the SUT output against a
   lookup table of exact answers, so scoring is identical across SUTs and not subject to
   evaluator error that varies by SUT (the failure mode's mechanism).

**Strong positive signals:** documentation that outputs are matched bit-exactly against a
lookup table or answer key; deterministic exact-match grading; no human or model judge
forming a quality opinion; explicit statement that all SUTs are scored by the same exact
comparison.

**Negative / disqualifying signals:** scoring via human raters or an LLM judge that can
be swayed by presentation/style; partial-credit or rubric scoring of open outputs;
approximate or fuzzy matching that admits judgment; the bit-exact/lookup-table approach
described only for a future version.
