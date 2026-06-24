# Mitigation 003 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #3, which mitigates Failure Mode #3.
Source: data/mitigations/3.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 3
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with the
  aid of Llama4 in the crowd worker interface to improve their performance. Consequently,
  the prompts are biased to the word usage of Llama4 and it performs higher on the
  benchmark than it otherwise would. The benchmark user selects Llama4 even though it is
  not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you record the specification of the LLM used for every prompt that was produced with
> the aid of an LLM?

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

1. **`llm_specification_recorded`** — For prompts produced with the aid of an LLM, the
   documents record the specific LLM used (e.g., model name and version), not merely that
   "an LLM" was involved.
2. **`per_prompt_coverage`** — The record is maintained for *every* LLM-assisted prompt
   (e.g., a per-instance field or provenance log), not only a global statement that some
   model was used somewhere.

**Strong positive signals:** a provenance/metadata column recording the generating model
and version for each LLM-assisted prompt; a dataset schema documenting an "LLM used" field;
an explicit statement that any prompt touched by an LLM is annotated with the model
specification; release of a manifest tying instances to the model that produced them.

**Negative / disqualifying signals:** LLM assistance acknowledged but with no record of
which model was used; only an aggregate note ("we used some commercial models") without
per-prompt attribution; provenance promised for a future release; no mechanism described
for tracking model identity at the prompt level.
