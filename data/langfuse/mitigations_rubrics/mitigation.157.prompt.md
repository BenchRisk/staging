# Mitigation 157 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #157, which mitigates Failure Mode #32.
Source: data/mitigations/157.mdx and data/modes/32.mdx.
-->

## The mitigation under review

- **Mitigation number:** 157
- **Mitigates failure mode:** #32 — *"Evaluator(s) have a high false reject rate
  (acceptable outputs rated as unacceptable)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses human evaluators who are
  instructed to flag any potential safety concerns in SUT responses to medical questions.
  The evaluators, anxious about missing harmful content and lacking medical expertise,
  excessively reject valid medical information that mentions side effects or treatment
  risks, even when accurately presented with appropriate context. As a result, systems
  that provide thorough, nuanced medical information score poorly compared to those giving
  oversimplified but incomplete advice. The benchmark user selects a SUT that omits
  important risk information in its responses, leading to a telehealth platform where
  patients aren't properly informed about potential treatment complications, resulting in
  several adverse events that might have been avoided with more complete information.

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
   canonical string/value), not a subjective accept/reject judgment.
2. **`lookup_table_check`** — Grading is performed by checking the SUT output against a
   lookup table of exact answers, so an acceptable output cannot be erroneously rejected
   by a fallible evaluator (the high-false-reject-rate mechanism in the failure mode).

**Strong positive signals:** documentation that outputs are matched bit-exactly against a
lookup table or answer key; deterministic exact-match grading; explicit statement that
acceptance is decided solely by membership in the answer set, not by evaluator opinion;
reproducible automated comparison.

**Negative / disqualifying signals:** human raters or an LLM judge deciding
acceptability of open outputs; overly strict or risk-averse reviewers rejecting valid
responses; rubric or partial-credit scoring requiring judgment; the bit-exact/lookup-table
approach described only for a future version.
