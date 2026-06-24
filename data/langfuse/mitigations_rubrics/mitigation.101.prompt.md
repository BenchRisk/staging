# Mitigation 101 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #101, which mitigates Failure Mode #5.
Source: data/mitigations/101.mdx and data/modes/5.mdx.
-->

## The mitigation under review

- **Mitigation number:** 101
- **Mitigates failure mode:** #5 — *"Data vendor licenses private data that is available
  to other parties"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~96.67% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A third-party vendor licenses a set of
  complex reasoning prompts without ensuring they are the sole organization with a right to
  license the data. As a result, the SUTs may have separately licensed the exact benchmark
  prompts during training or evaluation, inflating their performance and compromising the
  benchmark's validity as a measure of generalization or real-world capability. The
  benchmark user adopts the LLM whose developers also licensed the data despite it having
  poor generalization performance.

**Criterion question (answer this for the benchmark under review):**
> Do you ensure that all prompts are produced solely through original human effort without
> sourcing data from external sources?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Effective prompt design
  directly influences the reliability and interpretability of benchmark results.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to generate
  variations, expansions, or perturbations in data-driven processes.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`original_human_effort`** — All prompts are produced solely through original human
   effort (authored anew by the benchmark team or its contributors).
2. **`no_external_sourcing`** — No prompt data is sourced from external sources — in
   particular, no licensed or vendor-supplied datasets that could also be available to SUT
   developers.

**Strong positive signals:** a stated process of writing all prompts from scratch by named
authors or annotators; an explicit statement that no external/licensed datasets were used;
documentation of prompt authorship and provenance; a declaration that prompts are exclusive
to this benchmark.

**Negative / disqualifying signals:** prompts licensed from or sourced through a data
vendor; reuse of an existing public or third-party dataset; silence on prompt provenance;
original authorship promised only for a future version while the current set is externally
sourced.
