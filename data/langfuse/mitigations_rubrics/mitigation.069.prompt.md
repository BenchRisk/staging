# Mitigation 069 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #69, which mitigates Failure Mode #8.
Source: data/mitigations/69.mdx and data/modes/8.mdx.
-->

## The mitigation under review

- **Mitigation number:** 69
- **Mitigates failure mode:** #8 — *"Prompt writers produce prompts with inadequate
  variability within the valid input space (e.g., a single prompt writer writes all the
  prompts)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to test reasoning over
  legal contracts uses 500 prompts, all written by a single legal expert. Although the
  expert is highly knowledgeable, their prompts all follow similar structures, phrasings,
  and assumptions. As a result, the SUT learns to pick up on these patterns and performs
  well. However, when deployed to assist general counsel teams, the model fails to handle
  real-world contract analysis tasks that involve diverse linguistic styles,
  jurisdictions, and edge cases. The benchmark user trusts the high benchmark score and
  integrates the model into a high-stakes legal review process, leading to costly
  misinterpretations.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from multiple populations with clearly distinct demographic
> characteristics among prompt writers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances,
  contingent on having data that supports distributional evaluation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`multiple_writer_populations`** — The benchmark's prompts are sourced from multiple
   distinct populations of prompt writers, not a single author or homogeneous group.
2. **`distinct_demographics_documented`** — Those populations are documented as having
   clearly distinct demographic characteristics (e.g., differing regions, backgrounds, or
   professional profiles), establishing meaningful diversity among writers.

**Strong positive signals:** a described pool of prompt writers spanning several
populations; reported demographic distinctions among writer groups; evidence prompts were
contributed by writers of varied backgrounds rather than one expert/team; statistics on
the diversity of the writer population.

**Negative / disqualifying signals:** all prompts written by a single author or one
uniform group; no information about who wrote the prompts; multiple writers but no
evidence they differ demographically; diversification of writers described only as a
future plan while the published prompts come from one population.
