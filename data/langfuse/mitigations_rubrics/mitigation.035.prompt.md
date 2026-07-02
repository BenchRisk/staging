# Mitigation 035 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #35, which mitigates Failure Mode #36.
Source: data/mitigations/35.mdx and data/modes/36.mdx.
-->

## The mitigation under review

- **Mitigation number:** 35
- **Mitigates failure mode:** #36 — *"Presentation without uncertainty or confidence of
  the scores"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~90.0% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark report presents a single
  numerical "Stock Trading Ability" score for each SUT without any indication of
  statistical uncertainty, variance across test cases, or confidence intervals for the
  presented scores. The published results show two systems scoring 57% and 55%
  respectively, implying the first system is superior. The benchmark user selects the
  marginally higher-scoring system and implements it for critical financial analysis. In
  reality, the scores had overlapping confidence intervals (± 10%) and the supposedly
  "better" system is materially worse when subject to additional scrutiny. The
  organization discovers this only after several months of operation when market
  competitors deploying the other model place the company on the bad end of several
  multi-million dollar trades.

**Criterion question (answer this for the benchmark under review):**
> Do you prominently display uncertainty estimates alongside your benchmark results?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`uncertainty_reported`** — Each presented score is accompanied by an uncertainty
   estimate (e.g., confidence interval, standard error, variance across test cases), not
   just a bare point value.
2. **`displayed_prominently`** — The uncertainty appears directly alongside the scores
   where users read them (in the results table, the leaderboard, or the figure), so a
   user comparing two SUTs can see whether their intervals overlap.

**Strong positive signals:** ± intervals or error bars shown next to every published
score; a leaderboard column for confidence interval or standard error; explicit notes
that closely ranked systems are statistically indistinguishable; figures with visible
error bars rather than bare bars or points.

**Negative / disqualifying signals:** a single number per SUT with no spread; rankings
that imply ordering between scores whose intervals overlap; uncertainty discussed only in
prose or an appendix but absent from the headline table/figure; variance computed
internally but never surfaced to the user; uncertainty promised for a later version while
the current presentation shows only point scores.
