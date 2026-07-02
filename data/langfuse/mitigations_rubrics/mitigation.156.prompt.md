# Mitigation 156 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #156, which mitigates Failure Mode #31.
Source: data/mitigations/156.mdx and data/modes/31.mdx.
-->

## The mitigation under review

- **Mitigation number:** 156
- **Mitigates failure mode:** #31 — *"Evaluator(s) perform poorly across all SUTs"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark employs undergraduate
  psychology students with no technical background to evaluate advanced AI reasoning on
  complex mathematical proofs. These evaluators cannot distinguish between correct proofs
  and those with subtle errors, giving high scores to any response that looks
  sophisticated regardless of accuracy. As a result, all tested systems receive similarly
  high scores despite vast differences in actual mathematical reasoning capabilities. The
  benchmark user selects the cheapest SUT thinking it performs equivalently to premium
  options, then deploys it to verify critical engineering calculations for a bridge
  design, resulting in structural flaws being missed and necessitating costly redesigns
  when discovered by other verification methods.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark use singular answers (i.e., bit-exact outputs) that are checked via a
> lookup table?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to guide data interpretation and decision-making. For
  benchmarks, a domain expert knows about the SUT's task; someone without specialized
  knowledge in the benchmarked domain is not a domain expert.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`bit_exact_answers`** — Each item has a singular, bit-exact correct output (an exact
   canonical string/value), not a quality judgment requiring evaluator expertise.
2. **`lookup_table_check`** — Grading is performed by checking the SUT output against a
   lookup table of exact answers, so scoring does not depend on the competence of human or
   model evaluators that could perform poorly across all SUTs (the failure mode's
   mechanism).

**Strong positive signals:** documentation that outputs are matched bit-exactly against a
lookup table or answer key; deterministic exact-match grading with no rater judgment;
explicit statement that scoring requires no domain-expert evaluation; reproducible
automated comparison.

**Negative / disqualifying signals:** scoring relies on human raters or an LLM judge whose
competence bounds reliability; under-qualified evaluators judging open outputs; rubric or
partial-credit scoring of free text; the bit-exact/lookup-table approach described only
for a future release.
