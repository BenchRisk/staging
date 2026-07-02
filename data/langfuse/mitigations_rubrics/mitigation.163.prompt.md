# Mitigation 163 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #163, which mitigates Failure Mode #3.
Source: data/mitigations/163.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 163
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~58.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with
  the aid of Llama4 in the crowd worker interface to improve their performance.
  Consequently, the prompts are biased to the word usage of Llama4 and it performs higher
  on the benchmark than it otherwise would. The benchmark user selects Llama4 even though
  it is not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you construct the task definition such that LLMs are of limited utility in producing
> the prompts?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically in
  natural language. Prompts define the context, task, or question the system is expected
  to respond to and are central to evaluating SUT performance.
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`task_resists_llm_authoring`** — The task is defined in a way that intentionally
   limits the usefulness of LLMs for producing the prompts (e.g., requiring novel,
   real-world, proprietary, or human-sourced material that an LLM could not credibly
   generate).
2. **`prompt_provenance_controlled`** — The documents describe how prompt provenance is
   controlled to keep LLM contributions limited (e.g., human authorship requirements, a
   prohibition on LLM-assisted writing, or detection/filtering of LLM-generated prompts).

**Strong positive signals:** a stated design choice that prompts must come from human
experts or real-world artifacts that defeat LLM authoring; an explicit no-LLM-assistance
policy for prompt writers; descriptions of tasks grounded in fresh, non-public, or
hard-to-synthesize content.

**Negative / disqualifying signals:** prompts openly generated or paraphrased with an LLM;
no policy or safeguard against LLM-authored prompts; a task framing so generic that an LLM
could trivially produce equivalent prompts; the safeguard described only as a future plan.
