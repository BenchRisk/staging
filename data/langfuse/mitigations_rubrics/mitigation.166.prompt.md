# Mitigation 166 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #166, which mitigates Failure Mode #18.
Source: data/mitigations/166.mdx and data/modes/18.mdx.
-->

## The mitigation under review

- **Mitigation number:** 166
- **Mitigates failure mode:** #18 — *"No coverage for target language idiomatic
  expressions (including differences in functional expression, less common APIs, etc.,
  within programming languages) beyond those known to the benchmark authors"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~29.17%
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
> Does the task definition aim to avoid processing and expression of idioms?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`idiom_scope_excluded`** — The task definition explicitly aims to avoid the
   processing and expression of idioms (idiomatic natural-language expressions or
   language-/library-specific idiomatic code constructs), so the benchmark does not depend
   on idiom coverage the authors cannot fully enumerate.

**Strong positive signals:** an explicit task-scope statement that idiomatic expressions
are out of scope or deliberately controlled for; prompts constructed to use only literal,
canonical, or idiom-neutral phrasing/constructs; a stated rationale that idiom coverage is
avoided because it cannot be made comprehensive.

**Negative / disqualifying signals:** the task relies on or rewards idiomatic expression
without acknowledging coverage limits; no statement about idioms in the task definition,
leaving it implicit; idiom handling claimed only for a planned future revision while the
published task is silent.
