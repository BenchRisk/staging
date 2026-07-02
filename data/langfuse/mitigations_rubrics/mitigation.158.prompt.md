# Mitigation 158 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #158, which mitigates Failure Mode #33.
Source: data/mitigations/158.mdx and data/modes/33.mdx.
-->

## The mitigation under review

- **Mitigation number:** 158
- **Mitigates failure mode:** #33 — *"Evaluator(s) have a high false accept rate
  (unacceptable outputs rated as acceptable)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark employs evaluators to assess AI
  responses for misinformation in scientific explanations. The evaluators, who lack
  expertise in specialized scientific domains, consistently fail to identify subtle but
  significant inaccuracies in SUT outputs, particularly when presented with confident,
  authoritative-sounding language and plausible-seeming explanations. All systems receive
  artificially high accuracy scores, with the most persuasive but factually flawed system
  scoring highest. The benchmark user deploys this system in an educational platform for
  medical students, where it convincingly teaches incorrect mechanisms of drug
  interactions that go undetected for months until graduates apply this misinformation in
  clinical settings, leading to several serious medication errors and a subsequent
  investigation that reveals the systematic flaws in the benchmark's evaluation process.

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
   lookup table of exact answers, so an unacceptable output cannot be erroneously accepted
   by a fallible evaluator (the high-false-accept-rate mechanism in the failure mode).

**Strong positive signals:** documentation that outputs are matched bit-exactly against a
lookup table or answer key; deterministic exact-match grading; explicit statement that
acceptance requires an exact match to the answer set rather than evaluator approval;
reproducible automated comparison resistant to confident-but-wrong outputs.

**Negative / disqualifying signals:** human raters or an LLM judge approving open outputs
they cannot fully verify; persuasive-but-incorrect responses passing review; rubric or
partial-credit scoring requiring domain judgment; the bit-exact/lookup-table approach
described only for a future release.
