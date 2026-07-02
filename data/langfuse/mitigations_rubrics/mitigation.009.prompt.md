# Mitigation 009 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #9, which mitigates Failure Mode #6.
Source: data/mitigations/9.mdx and data/modes/6.mdx.
-->

## The mitigation under review

- **Mitigation number:** 9
- **Mitigates failure mode:** #6 — *"Data vendor provides same prompts to multiple
  organizations including benchmark authors and SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses a proprietary dataset of
  customer service transcripts licensed from a call center vendor. Several major LLM
  developers also have access to this dataset through separate licensing deals, giving them
  an advantage on the benchmark that smaller labs or open-source developers cannot match —
  leading to unfair comparisons and undermining the benchmark's claims of generalization.
  Consequently, the benchmark user adopts a poor performing system that happened to license
  all the benchmark evaluation data.

**Criterion question (answer this for the benchmark under review):**
> Do you include contractual prohibitions against reselling licensed data to unrelated
> parties in your agreements with data vendors?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`resale_prohibition`** — The documents describe a prohibition preventing the data
   vendor from reselling or otherwise providing the licensed benchmark data to unrelated
   parties (e.g., SUT developers).
2. **`contractual`** — The prohibition is part of the agreement with the data vendor (a
   contractual obligation), not merely an informal expectation.

**Strong positive signals:** quoted vendor-agreement language barring resale or
redistribution of the licensed data to other parties; an exclusivity or non-resale clause
in the data procurement terms; a stated requirement that the vendor not provide the same
data to LLM developers.

**Negative / disqualifying signals:** no anti-resale or non-redistribution clause
described; vendor data acquired without restriction on who else may obtain it; only an
informal expectation of exclusivity; the clause described only as future contracting.
