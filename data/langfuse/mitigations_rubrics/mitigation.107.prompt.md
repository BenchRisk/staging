# Mitigation 107 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #107, which mitigates Failure Mode #48.
Source: data/mitigations/107.mdx and data/modes/48.mdx.
-->

## The mitigation under review

- **Mitigation number:** 107
- **Mitigates failure mode:** #48 — *"Users cannot map the scores to a mental model of
  likely SUT behavior in the real world."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark provides a highly abstract
  "coherence score" for a language model's long-form generation, calculated using a
  complex combination of statistical metrics like perplexity and cosine similarity of
  embeddings. While Model A achieves a score of 0.92 and Model B scores 0.88, a user
  struggles to understand what these numbers practically mean for generating a business
  report or a creative short story. They have no intuitive sense of the difference in
  quality, so their decision between Model A and Model B feels arbitrary, lacking a
  grounded understanding of how the scores translate to tangible output differences.

**Criterion question (answer this for the benchmark under review):**
> Are metric floors and ceilings included as part of the benchmark methodology?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Random Performance Level:** The baseline performance metric achieved by a SUT when it
  makes predictions or decisions purely at random, without using any learned information
  or strategy. It serves as a reference point grounding user expectations to help
  interpret benchmark results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`floor_defined`** — The methodology states the metric's floor (minimum / worst
   attainable value, or the score corresponding to no capability) for the reported score.
2. **`ceiling_defined`** — The methodology states the metric's ceiling (maximum / best
   attainable value, or the score corresponding to perfect performance) for the reported
   score.

**Strong positive signals:** explicit statements of the minimum and maximum possible
score; a stated worst-case/best-case reference (e.g., "0 = all wrong, 1 = all correct");
score ranges presented alongside results so users can locate a model within the
attainable band; floors/ceilings noted in the leaderboard or scorecard, not only in code.

**Negative / disqualifying signals:** scores reported as bare numbers with no stated
bounds; an unbounded or open-ended metric with no maximum; the user must guess what a
"good" or "bad" value is; floors/ceilings discussed only for a future revision while the
published methodology omits them.
