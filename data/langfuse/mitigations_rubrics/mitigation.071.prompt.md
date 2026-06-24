# Mitigation 071 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #71, which mitigates Failure Mode #12.
Source: data/mitigations/71.mdx and data/modes/12.mdx.
-->

## The mitigation under review

- **Mitigation number:** 71
- **Mitigates failure mode:** #12 — *"Prompt writers bias the sample to their own
  demographically-aligned word use, topics of interest, or other dimensions that tend to
  not explore the entirety of supported input space for the benchmark's supported use
  case"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating open-domain
  question answering is written by a small group of university-educated crowdworkers in
  the U.S. Their prompts disproportionately reflect Western pop culture, academic
  language, and topics of interest like sports, entertainment, and politics from a U.S.
  perspective. The SUT performs well on the benchmark, but when deployed globally, it
  struggles to handle queries about regional histories, idioms, or culturally specific
  contexts. A benchmark user in a multinational organization selects this SUT based on
  its top score, only to discover it performs poorly in non-Western markets and erodes
  user trust due to its perceived cultural bias.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from a range of different geographic regions to increase
> representativeness?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances,
  contingent on having data that supports distributional evaluation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`multiple_geographic_regions`** — The benchmark sources its prompts from a range of
   different geographic regions, rather than from a single region or locale.
2. **`representativeness_documented`** — The documents describe how this geographic spread
   was achieved and how it increases representativeness of the supported input space
   (e.g., a breakdown of prompts or writers by region).

**Strong positive signals:** a reported distribution of prompts or prompt writers across
multiple countries/regions; an explicit recruiting or sourcing strategy spanning regions;
discussion of regional/cultural coverage tied to representativeness; statistics comparing
regional representation against the target population.

**Negative / disqualifying signals:** prompts sourced from a single region or locale; no
information about the geographic origin of prompts; multiple regions claimed without any
supporting breakdown; geographic diversification described only as a future plan while
the published prompts come from one region.
