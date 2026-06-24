# Mitigation 109 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #109, which mitigates Failure Mode #48.
Source: data/mitigations/109.mdx and data/modes/48.mdx.
-->

## The mitigation under review

- **Mitigation number:** 109
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
> Is a performance level for random decision/output also provided in the benchmark?

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

1. **`random_level_reported`** — The benchmark states the random (chance) performance
   level for its metric — the score a SUT would obtain by guessing or producing random
   output.
2. **`presented_with_scores`** — The random performance level is presented alongside the
   SUT results so users can judge how far above chance a model actually is.

**Strong positive signals:** a stated "random baseline" or "chance level" (e.g., "random
guessing scores 25% on this 4-choice task"); a described derivation of the chance level;
model scores reported relative to chance; the random baseline shown in the
leaderboard/scorecard rather than only computed in code.

**Negative / disqualifying signals:** no chance/random reference reported; scores
presented with no indication of what guessing would yield; the random level mentioned in
prose but never quantified or shown with results; provided only for a future revision
while the published version omits it.
