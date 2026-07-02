# Mitigation 065 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #65, which mitigates Failure Mode #12.
Source: data/mitigations/65.mdx and data/modes/12.mdx.
-->

## The mitigation under review

- **Mitigation number:** 65
- **Mitigates failure mode:** #12 — *"Prompt writers bias the sample to their own
  demographically-aligned word use, topics of interest, or other dimensions that tend to
  not explore the entirety of supported input space for the benchmark's supported use
  case"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~33.33%
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
> Do you record the demographics of individuals generating prompts and make efforts to
> sample from underrepresented populations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances
  (e.g., annotations supporting evaluation of how outcomes differ across populations).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`demographics_recorded`** — The benchmark records and reports the demographic
   characteristics of the individuals who generated the prompts (e.g., region, language,
   education, or other relevant dimensions).
2. **`underrepresented_sampling_effort`** — The benchmark describes deliberate efforts to
   sample prompt writers from underrepresented populations, rather than relying on a
   convenience pool.

**Strong positive signals:** a reported breakdown of prompt-writer demographics; an
explicit recruiting strategy aimed at including underrepresented groups; documentation of
gaps in the writer population and steps taken to fill them; statistics comparing the
writer population against a target population.

**Negative / disqualifying signals:** no information on who wrote the prompts; prompts
written by a single convenience pool (e.g., one country's crowdworkers) with no
demographic accounting; demographic recording mentioned without any sampling effort to
broaden it; only a future intention to diversify writers while the published prompts come
from a narrow pool.
