# Mitigation 161 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #161, which mitigates Failure Mode #45.
Source: data/mitigations/161.mdx and data/modes/45.mdx.
-->

## The mitigation under review

- **Mitigation number:** 161
- **Mitigates failure mode:** #45 — *"SUT developers update the SUT without changing the
  name or version of the SUT"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates "Model X" in January
  2025 and publishes its results. Several months later, the developers of "Model X"
  release a significantly improved version of the model with architectural changes and
  updated training data, but they still refer to it as "Model X" without any version
  number change. A user consulting the benchmark results from January assumes the current
  "Model X" has the same capabilities and limitations as the one tested previously and
  fails to switch over to a new and better model.

**Criterion question (answer this for the benchmark under review):**
> Do you only test SUTs with well-known version identifiers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`version_identifiers_recorded`** — Each evaluated SUT is reported with a specific,
   resolvable version identifier (e.g., an exact model id, version tag, snapshot date, or
   API/release string), not just a bare product name.
2. **`only_versioned_suts_tested`** — The benchmark restricts itself to SUTs that expose
   well-known/stable version identifiers, or otherwise pins each result to the precise SUT
   build it was produced against (excluding or flagging unversioned, mutable endpoints).

**Strong positive signals:** a results table or leaderboard listing exact model versions,
snapshot dates, or API revision strings for every SUT; an explicit policy that only
version-pinned models are accepted; pinned API parameters (e.g., dated model snapshots)
documented alongside scores.

**Negative / disqualifying signals:** SUTs identified only by a bare brand or product
name with no version, date, or snapshot; results tied to a mutable "latest" endpoint;
no statement of which model build produced a score; version identifiers promised for a
future release but absent from the published results.
