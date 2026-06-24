# Mitigation 199 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #199, which mitigates Failure Mode #3.
Source: data/mitigations/199.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 199
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with
  the aid of Llama4 in the crowd-worker interface to improve their performance.
  Consequently, the prompts are biased to the word usage of Llama4 and it performs higher
  on the benchmark than it otherwise would. The benchmark user selects Llama4 even though
  it is not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Was the benchmark produced before the widespread availability of LLMs capable of
> generating its prompts?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language, defining the context, task, or question the system
  is expected to respond to.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`creation_date_stated`** — The documents establish when the prompts were authored or
   the benchmark was produced (e.g., a dated publication, dataset release, or collection
   period).
2. **`predates_capable_llms`** — That date precedes the widespread availability of LLMs
   capable of generating the kind of prompts the benchmark uses, such that LLM-authored
   prompts are implausible for the published prompt set.

**Strong positive signals:** an explicit, verifiable creation/collection date clearly
prior to the relevant LLMs' release; provenance describing human authorship before
generative LLMs were available; a dataset history or changelog dating the prompts to a
pre-LLM period.

**Negative / disqualifying signals:** no creation date given; prompts authored or revised
contemporaneously with or after capable LLMs were widely available; only a recent
publication date with no evidence the prompts predate it; the timing claim asserted
without any dating evidence in the documents.
