# Mitigation 200 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #200, which mitigates Failure Mode #36.
Source: data/mitigations/200.mdx and data/modes/36.mdx.
-->

## The mitigation under review

- **Mitigation number:** 200
- **Mitigates failure mode:** #36 — *"Presentation without uncertainty or confidence of
  the scores."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark report presents a single
  numerical "Stock Trading Ability" score for each SUT without any indication of
  statistical uncertainty, variance across test cases, or confidence intervals. The
  published results show two systems scoring 57% and 55%, implying the first is superior.
  The benchmark user selects the marginally higher-scoring system for critical financial
  analysis. In reality the scores had overlapping confidence intervals (± 10%) and the
  supposedly "better" system is materially worse under additional scrutiny. The
  organization discovers this only after months of operation when competitors deploying
  the other model place the company on the bad end of several multi-million-dollar trades.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark provide guidance or references on how to display or interpret
> statistics that communicate benchmark uncertainty?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`uncertainty_guidance_provided`** — The benchmark supplies guidance or references on
   how to display or interpret uncertainty statistics for its scores (e.g., how to read
   confidence intervals, variance, error bars, or significance of score differences).
2. **`tied_to_presentation`** — That guidance is connected to how the scores are actually
   shown — e.g., it accompanies the leaderboard/report and tells users how to interpret
   the displayed uncertainty — rather than being an unrelated general note.

**Strong positive signals:** explicit instructions on reading confidence intervals/error
bars on the scores; cited statistical references or a recommended method for assessing
whether two scores differ meaningfully; a "how to interpret uncertainty" note alongside
the results; documented display conventions for variance.

**Negative / disqualifying signals:** scores shown as bare point numbers with no
uncertainty guidance; uncertainty computed but no guidance on interpreting it; a generic
statistics reference unconnected to the benchmark's own presentation; such guidance
promised for a future release while the current presentation omits it.
