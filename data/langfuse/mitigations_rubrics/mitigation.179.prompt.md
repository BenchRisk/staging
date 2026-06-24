# Mitigation 179 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #179, which mitigates Failure Mode #18.
Source: data/mitigations/179.mdx and data/modes/18.mdx.
-->

## The mitigation under review

- **Mitigation number:** 179
- **Mitigates failure mode:** #18 — *"No coverage for target language idiomatic
  expressions (including differences in functional expression, less common APIs, etc.,
  within programming languages) beyond those known to the benchmark authors."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~25.0%
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
> Are the source prompts taken from systems under test (SUTs) deployed in real-world,
> non-experimental settings for the task under evaluation?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **SUT (System Under Test):** The specific system, model, or component being evaluated
  in a testing process.
- **SUT (System Under Test) Task:** The specific activity or objective the SUT is
  expected to perform in the real world; a well-defined SUT task gives the benchmark the
  capacity to measure and report properties related to that task.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`real_world_deployment_source`** — The source prompts are documented as drawn from
   SUTs deployed in real-world, non-experimental settings, rather than authored by the
   benchmark team or collected in a lab/experimental setup.
2. **`for_task_under_evaluation`** — Those real-world prompts pertain to the specific task
   being evaluated, so the prompt set captures idioms, APIs, and expressions beyond those
   known to the authors.

**Strong positive signals:** prompts sourced from production logs or real deployments of
the relevant systems; documentation that the data reflects genuine in-the-wild usage for
the evaluated task; coverage of less common or emerging idioms/APIs traceable to that
real-world origin; provenance tying prompts to non-experimental deployment.

**Negative / disqualifying signals:** prompts authored by the benchmark team from their
own familiarity; data gathered only in experimental or synthetic settings; coverage
limited to standard/common patterns with no real-world provenance; no statement of where
the source prompts came from.
