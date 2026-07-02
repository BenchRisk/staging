# Mitigation 141 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #141, which mitigates Failure Mode #6.
Source: data/mitigations/141.mdx and data/modes/6.mdx.
-->

## The mitigation under review

- **Mitigation number:** 141
- **Mitigates failure mode:** #6 — *"Data vendor provides same prompts to multiple
  organizations including benchmark authors and SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~93.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses a proprietary dataset of
  customer service transcripts licensed from a call center vendor. Several major LLM
  developers also have access to this dataset through separate licensing deals, giving
  them an advantage on the benchmark that smaller labs or open-source developers cannot
  match — leading to unfair comparisons and undermining the benchmark's claims of
  generalization. Consequently, the benchmark user adopts a poor-performing system that
  happened to license all the benchmark evaluation data.

**Criterion question (answer this for the benchmark under review):**
> Are all prompts entirely new and produced in-house by the benchmark developers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, consistency, reproducibility, accountability, comprehensiveness, and
  independence — guarding against advantages such as data snooping or benchmark
  overfitting.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`entirely_new`** — All prompts are entirely new — not licensed, purchased, or
   sourced from a third-party vendor whose data may also be held by SUT developers.
2. **`produced_in_house`** — The prompts were produced in-house by the benchmark
   developers themselves, so no external party shares privileged access to the same data.

**Strong positive signals:** an explicit statement that all prompts were created in-house
by the benchmark team; affirmation that no third-party / vendor-licensed data was used;
provenance showing the data exists only within the benchmark's control; a held-out,
non-distributed authoring process.

**Negative / disqualifying signals:** prompts licensed or purchased from a data vendor;
shared or third-party datasets used; any indication the same data is available to SUT
developers through separate deals; provenance unstated for some prompts; only a subset
authored in-house while others are externally sourced.
