# Mitigation 022 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #22, which mitigates Failure Mode #19.
Source: data/mitigations/22.mdx and data/modes/19.mdx.
-->

## The mitigation under review

- **Mitigation number:** 22
- **Mitigates failure mode:** #19 — *"Cultural norms do not translate between cultural
  contexts (languages, geographies, etc.)."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a language model's
  ability to understand and generate appropriate responses to cultural references in a
  variety of languages. However, the evaluation is conducted primarily in English, using
  Western cultural norms and references. When the model is deployed in a different
  geographic or linguistic context, such as in Japan or Brazil, it fails to understand or
  appropriately respond to culturally specific references, phrases, and social nuances,
  leading to misunderstandings and alienation in non-Western audiences. The benchmark
  user assumes the model is universally adept at handling cultural nuances but encounters
  failures in real-world deployments across different regions.

**Criterion question (answer this for the benchmark under review):**
> Do you clearly state the cultural or contextual limitations of your benchmark, such as
> noting that definitions of violating content reflect a specific cultural perspective?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Normative Properties:** Characteristics, standards, or criteria that define what is
  considered acceptable, desirable, or expected within a particular context or domain.
  These properties often guide behavior, decision-making, and evaluations (e.g., which
  hand a person may politely eat with at the dinner table).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`limitations_stated`** — The documents clearly state the cultural or contextual
   limitations of the benchmark — e.g., that the languages, geographies, or definitions
   of acceptable/violating content reflect a specific cultural perspective rather than a
   universal one.
2. **`clearly_communicated`** — That statement is communicated clearly to users where
   they encounter the benchmark (not implicit, and not contradicted by claims of
   universal cultural coverage).

**Strong positive signals:** an explicit note that norms/definitions reflect a particular
culture (e.g., "Western" or a named locale); a scope statement on which languages or
regions are represented; an acknowledgement that results may not transfer across cultural
contexts; a "cultural limitations" caveat near the benchmark description.

**Negative / disqualifying signals:** the benchmark is presented as culturally neutral or
universally applicable; no mention of the cultural basis of the norms used; limitations
buried far from the primary description or omitted; the caveat applies only to a future
multilingual/multicultural version rather than the published one.
