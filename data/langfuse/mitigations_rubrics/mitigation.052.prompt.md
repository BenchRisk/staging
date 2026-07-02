# Mitigation 052 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #52, which mitigates Failure Mode #45.
Source: data/mitigations/52.mdx and data/modes/45.mdx.
-->

## The mitigation under review

- **Mitigation number:** 52
- **Mitigates failure mode:** #45 — *"SUT developers update the SUT without changing the
  name or version of the SUT"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates "Model X" in January
  2025 and publishes its results. Several months later, the developers of "Model X"
  release a significantly improved version of the model with architectural changes and
  updated training data, but they still refer to it as "Model X" without any version
  number change. A user consulting the benchmark results from January assumes the current
  "Model X" has the same capabilities and limitations as the one tested previously and
  fails to switch over to a new and better model.

**Criterion question (answer this for the benchmark under review):**
> Do you periodically re-test all systems under test (SUTs) to maintain up-to-date
> comparisons?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness, comprehensiveness,
  consistency, and intelligibility through time subject to gaming or changing
  circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`periodic_retest`** — The benchmark re-runs its evaluation on SUTs on a recurring
   basis rather than testing each SUT only once, so that results reflect the systems as
   they currently exist.
2. **`all_suts`** — Re-testing covers all SUTs in the comparison (not just newly added
   ones), keeping the published comparison consistent and up to date.

**Strong positive signals:** a stated re-evaluation cadence or refresh schedule; dated
result entries showing re-runs over time; a documented policy to re-test existing/listed
SUTs (e.g., when a vendor ships an update) and not only to append new models; a
"last evaluated" timestamp per SUT.

**Negative / disqualifying signals:** each SUT tested once with no refresh; stale dated
results with no re-run; only newly submitted models evaluated while previously listed SUTs
are never re-tested; periodic re-testing described only as a future intention.
