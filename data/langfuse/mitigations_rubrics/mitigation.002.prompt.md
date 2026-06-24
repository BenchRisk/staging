# Mitigation 002 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #2, which mitigates Failure Mode #3.
Source: data/mitigations/2.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 2
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with the
  aid of Llama4 in the crowd worker interface to improve their performance. Consequently,
  the prompts are biased to the word usage of Llama4 and it performs higher on the
  benchmark than it otherwise would. The benchmark user selects Llama4 even though it is
  not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you contractually prohibit the use of large language models (LLMs) in the production
> of test data for your benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the context,
  task, or question the system is expected to respond to and are central to evaluating SUT
  performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`prohibition_exists`** — The documents describe a binding prohibition on using LLMs
   to produce, draft, or assist in producing the benchmark's test data (prompts), as
   opposed to merely a preference or an aspiration.
2. **`contractual`** — The prohibition is expressed as a contractual or agreement-level
   obligation binding the data producers (e.g., crowd workers, annotators, vendors), not
   only an informal guideline or internal note.

**Strong positive signals:** quoted contract, worker-agreement, terms-of-engagement, or
vendor-agreement language forbidding LLM use when writing prompts; a data-collection
protocol stating annotators contractually agreed not to use generative models; an explicit
statement that prompt production was restricted to human-authored content by contract.

**Negative / disqualifying signals:** no mention of any LLM-use restriction on data
producers; only a soft recommendation or "we encouraged human writing" with no binding
force; the prohibition described only as planned for a future round; documents indicate
LLMs were in fact used to assist prompt writing.
