# Mitigation 102 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #102, which mitigates Failure Mode #6.
Source: data/mitigations/102.mdx and data/modes/6.mdx.
-->

## The mitigation under review

- **Mitigation number:** 102
- **Mitigates failure mode:** #6 — *"Data vendor provides same prompts to multiple
  organizations including benchmark authors and SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses a proprietary dataset of
  customer service transcripts licensed from a call center vendor. Several major LLM
  developers also have access to this dataset through separate licensing deals, giving them
  an advantage on the benchmark that smaller labs or open-source developers cannot
  match—leading to unfair comparisons and undermining the benchmark's claims of
  generalization. Consequently, the benchmark user adopts a poor performing system that
  happened to license all the benchmark evaluation data.

**Criterion question (answer this for the benchmark under review):**
> Do you supervise prompt production by requiring that any external party generates only
> novel, previously unwritten, and undigitized prompts?

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

1. **`supervised_production`** — Prompt production by any external party is supervised by
   the benchmark team (a described oversight or contractual control over how prompts are
   generated).
2. **`novel_unwritten_undigitized`** — That supervision requires external parties to
   generate only novel, previously unwritten, and undigitized prompts — not reused or
   re-licensed existing material.

**Strong positive signals:** a described contributor agreement or workflow requiring
brand-new prompts; an explicit prohibition on reusing existing or digitized content; a
review/oversight step confirming prompt novelty; a statement that prompts were never
previously published or shared with other organizations.

**Negative / disqualifying signals:** prompts licensed from a vendor that also supplies
others; reuse of pre-existing or already-digitized datasets; no supervision or novelty
requirement over external prompt production; the novelty/supervision requirement described
only for a future version while the current set is vendor-sourced.
