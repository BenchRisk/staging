# Mitigation 044 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #44, which mitigates Failure Mode #43.
Source: data/mitigations/44.mdx and data/modes/43.mdx.
-->

## The mitigation under review

- **Mitigation number:** 44
- **Mitigates failure mode:** #43 — *"User behavior shifts through time"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark initially tests a language
  model's ability to answer factual questions about world history. Early users find the
  benchmark helpful in identifying models that are capable tutors of history. However, as
  time passes, user behavior evolves. They start using language models for new history
  classes with more comprehensive coverage of history in Asia and Africa, areas the
  original benchmark did not assess. Consequently, a user relying solely on the initial
  benchmark scores might select a model that excels at American or European history but
  performs poorly on the expanded considerations of world history.

**Criterion question (answer this for the benchmark under review):**
> Do you actively update your tests in response to changing user behaviors?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`tests_updated_over_time`** — The benchmark is actively revised/updated rather than
   frozen — there is evidence of an ongoing update process (versions, changelog, refresh
   cadence).
2. **`responsive_to_user_behavior`** — Those updates are driven by changing user
   behaviors or needs (e.g., new use cases, shifting usage patterns, expanded coverage),
   not just bug fixes.

**Strong positive signals:** a documented update cadence or versioned releases with a
changelog; described monitoring of how users actually use the benchmark/SUTs; coverage
expanded to follow emerging use cases; a stated process for incorporating evolving user
needs into new test items.

**Negative / disqualifying signals:** a static, one-time release with no updates; updates
limited to errata with no link to user behavior; "we may update in future" with no
realized revisions; no mechanism to detect or respond to shifting usage; the benchmark
unchanged since publication despite a moving domain.
