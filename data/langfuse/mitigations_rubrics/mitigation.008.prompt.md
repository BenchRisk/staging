# Mitigation 008 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #8, which mitigates Failure Mode #5.
Source: data/mitigations/8.mdx and data/modes/5.mdx.
-->

## The mitigation under review

- **Mitigation number:** 8
- **Mitigates failure mode:** #5 — *"Data vendor licenses private data that is available
  to other parties"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~25.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A third-party vendor licenses a set of
  complex reasoning prompts without ensuring they are the sole organization with a right to
  license the data. As a result, the SUTs may have separately licensed the exact benchmark
  prompts during training or evaluation, inflating their performance and compromising the
  benchmark's validity as a measure of generalization or real-world capability. The
  benchmark user adopts the LLM whose developers also licensed the data despite it having
  poor generalization performance.

**Criterion question (answer this for the benchmark under review):**
> Do you include contractual prohibitions against providing data that might be available
> to other parties?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`exclusivity_prohibition`** — The documents describe a prohibition against the vendor
   providing data that might also be available to other parties (i.e., the data must be
   exclusive to this benchmark and not obtainable by SUT developers or others).
2. **`contractual`** — The prohibition is expressed as a contractual or agreement-level
   obligation binding the vendor, not merely an informal understanding.

**Strong positive signals:** quoted contract language requiring data exclusivity or barring
the vendor from supplying the same data to others; a warranty that the data is not and will
not be made available to third parties; a procurement requirement that the data be unique
to this benchmark.

**Negative / disqualifying signals:** no exclusivity or non-availability clause; data
licensed without any guarantee that other parties lack access; only an informal preference
for exclusive data; the safeguard described only as planned future contracting.
