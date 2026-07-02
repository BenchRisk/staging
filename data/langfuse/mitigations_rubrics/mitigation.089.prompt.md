# Mitigation 089 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #89, which mitigates Failure Mode #3.
Source: data/mitigations/89.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 89
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~62.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with the
  aid of Llama4 in the crowd worker interface to improve their performance. Consequently,
  the prompts are biased to the word usage of Llama4 and it performs higher on the
  benchmark than it otherwise would. The benchmark user selects Llama4 even though it is
  not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Are all prompts authored by the benchmark creators themselves, without using data
> vendors, LLMs, or crowd workers whose identities are unknown to the authors?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language. Prompts define the context, task, or question the
  system is expected to respond to and are central to evaluating SUT performance; their
  design directly influences the reliability and interpretability of benchmark results.
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances.
  Assessing such effects is contingent on having data annotated to support distributional
  evaluation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`authored_by_creators`** — The documents state that all prompts were authored by the
   benchmark creators themselves.
2. **`no_llm_authoring`** — No LLM was used to write or assist in writing the prompts.
3. **`no_unknown_third_parties`** — Prompts were not produced via data vendors or crowd
   workers whose identities are unknown to the authors (i.e., authorship is attributable
   and known to the creators).

**Strong positive signals:** an explicit statement that the authors wrote every prompt
themselves; a stated policy against LLM assistance in prompt creation; a documented,
known set of contributors with no anonymous vendor/crowd sourcing; a process description
that excludes model-generated prompts.

**Negative / disqualifying signals:** prompts generated or "improved" with an LLM; prompts
sourced from data vendors or anonymous crowd workers; no statement of who authored the
prompts or how; only partial creator authorship while some prompts come from unknown
third parties; a "human-only authorship" policy described as planned rather than applied
to the published prompts.
