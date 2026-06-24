# Mitigation 147 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #147, which mitigates Failure Mode #18.
Source: data/mitigations/147.mdx and data/modes/18.mdx.
-->

## The mitigation under review

- **Mitigation number:** 147
- **Mitigates failure mode:** #18 — *"No coverage for target language idiomatic
  expressions (including differences in functional expression, less common APIs, etc.,
  within programming languages) beyond those known to the benchmark authors"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~93.33% reduction in failure-mode likelihood; ~37.5%
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
  assuming the model's high performance means general code generation ability, integrates
  it into production environments where it struggles with newer tools or approaches,
  leading to code inefficiencies and technical debt.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark avoid processing human languages in its inputs or outputs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the
  context, task, or question the system is expected to respond to and are central to
  evaluating SUT performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_human_language_io`** — The benchmark's inputs and outputs do not depend on
   processing any human (natural) language — i.e., the criterion is satisfied only when
   the task is language-agnostic (e.g., purely numeric, structural, or programmatic with
   exact checking that does not require interpreting idiomatic or natural-language
   content).
2. **`stated_in_scope`** — The document makes the language-agnostic nature of the
   inputs/outputs explicit (the task and grading do not hinge on parsing human-language
   idiom, phrasing, or comprehension), rather than leaving it for the reader to infer.

**Strong positive signals:** an explicit statement that the benchmark operates over
non-textual or formally specified inputs/outputs (e.g., numeric answers, symbolic forms,
exact code-execution results) that do not require interpreting human-language idiom;
grading by execution/equality rather than language understanding; documentation that the
task is independent of any human-language register or idiomatic variation.

**Negative / disqualifying signals:** prompts or expected outputs written in a natural
human language (English, French, etc.) whose idiom or phrasing matters; code-generation
or NLP tasks where success depends on interpreting natural-language instructions or
idiomatic API usage; any reliance on language-dependent comprehension in inputs or
outputs; the language-agnostic claim made only for a future version.
