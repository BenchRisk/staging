# Mitigation 021 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #21, which mitigates Failure Mode #18.
Source: data/mitigations/21.mdx and data/modes/18.mdx.
-->

## The mitigation under review

- **Mitigation number:** 21
- **Mitigates failure mode:** #18 — *"No coverage for target language idiomatic
  expressions (including differences in functional expression, less common APIs, etc.,
  within programming languages) beyond those known to the benchmark authors."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~16.67% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate a
  programming language model's ability to generate code for common tasks focuses on
  widely used APIs and standard coding conventions, as well as idiomatic expressions in a
  programming language (e.g., Python list comprehensions, JavaScript callbacks). However,
  the prompts used by the benchmark authors reflect only the patterns and libraries they
  are familiar with, leaving out less common or emerging idioms, libraries, or APIs that
  may become relevant in real-world usage. As a result, the SUT performs well on the
  benchmark, which primarily uses the most established coding patterns and libraries.
  However, when deployed to generate code for novel, less-standard tasks or new
  frameworks, the model produces inefficient or incorrect code. The benchmark user,
  assuming the model's high performance on the benchmark means general code generation
  ability, integrates it into production environments where it struggles with newer tools
  or approaches, leading to code inefficiencies and technical debt.

**Criterion question (answer this for the benchmark under review):**
> Do you prominently and publicly state the benchmark does not cover idioms within the
> languages supported by the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task — e.g., a speaker
  of a low-resource language for a translation benchmark.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`limitation_stated`** — The documents explicitly state that the benchmark does
   **not** cover idiomatic expressions (idioms, less common APIs, functional expression
   variants, etc.) within the languages it supports, rather than implying full coverage.
2. **`public_and_prominent`** — That limitation is stated publicly and prominently where
   users actually encounter the benchmark (e.g., abstract, README, scope/limitations
   section, dataset card), not buried in an appendix or omitted entirely.

**Strong positive signals:** a "limitations" or "scope" statement naming idiomatic
coverage gaps; an explicit caveat that only authors' known idioms/APIs are covered; a
clear statement near the top of primary docs that idiom coverage is partial; a coverage
table or scope note flagging excluded idioms or libraries.

**Negative / disqualifying signals:** no mention of idiom coverage limits anywhere;
language framed as comprehensive or representative of the whole language; the caveat
present only in a buried footnote or code comment; the limitation described only for a
planned version while the published version claims broad idiomatic coverage.
