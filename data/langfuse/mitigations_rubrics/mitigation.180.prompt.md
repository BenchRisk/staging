# Mitigation 180 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #180, which mitigates Failure Mode #18.
Source: data/mitigations/180.mdx and data/modes/18.mdx.
-->

## The mitigation under review

- **Mitigation number:** 180
- **Mitigates failure mode:** #18 — *"No coverage for target language idiomatic
  expressions (including differences in functional expression, less common APIs, etc.,
  within programming languages) beyond those known to the benchmark authors."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluating a programming
  language model's ability to generate code focuses on widely used APIs, standard coding
  conventions, and common idioms (e.g., Python list comprehensions, JavaScript
  callbacks). But the prompts reflect only the patterns and libraries the authors are
  familiar with, leaving out less common or emerging idioms, libraries, or APIs. The SUT
  performs well on the established patterns but, deployed for novel or non-standard tasks
  or new frameworks, produces inefficient or incorrect code. The user, assuming high
  benchmark performance implies general ability, integrates it into production where it
  struggles with newer tools, causing inefficiencies and technical debt.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from experimental settings that enable the collection of idioms?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically in
  natural language. Prompts define the context, task, or question the system is expected
  to respond to and are central to evaluating SUT performance.
- **Domain Expert:** An individual with specialized knowledge of the SUT's task (e.g., a
  speaker of a low-resource language for a translation benchmark). For idiomatic coverage,
  experienced practitioners can surface idioms, libraries, or APIs beyond those known to
  the benchmark authors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`experimental_collection_setting`** — The prompts are sourced via a deliberate
   experimental or elicitation setting (e.g., user studies, structured tasks, or
   practitioner sessions) designed to draw out language- or programming-idioms.
2. **`enables_idiom_collection`** — That setting is documented as capturing idioms, less
   common APIs, or functional-expression variants beyond those the authors already know.

**Strong positive signals:** a described study or elicitation protocol that surfaces
idiomatic usage; involvement of practitioners or domain experts to contribute idioms,
less common libraries, or emerging APIs; an explicit goal of broadening idiomatic
coverage in the data-collection design; documentation of how the setting captures
non-standard expressions.

**Negative / disqualifying signals:** prompts written only from the authors' own
familiarity; no elicitation or study designed to gather idioms; coverage limited to
common/standard patterns; idiom collection described only as a future plan.
