# Mitigation 070 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #70, which mitigates Failure Mode #3.
Source: data/mitigations/70.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 70
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~33.33% reduction in failure-mode likelihood; ~66.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with the
  aid of Llama4 in the crowd worker interface to improve their performance. Consequently,
  the prompts are biased to the word usage of Llama4 and it performs higher on the
  benchmark than it otherwise would. The benchmark user selects Llama4 even though it is
  not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you generate a sufficient number of human-written prompts to enable statistical
> comparison with LLM-generated prompts, and do you conduct a comparative study?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language, defining the context,
  task, or question the system is expected to respond to.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`sufficient_human_written_prompts`** — The benchmark generates a sufficient number of
   genuinely human-written prompts to enable statistically meaningful comparison against
   LLM-generated prompts.
2. **`comparative_study_conducted`** — The developers conduct and report a comparative
   study between human-written and LLM-generated prompts (e.g., testing for distributional
   or scoring differences attributable to prompt source).

**Strong positive signals:** a reported count of human-written prompts adequate for
statistical power; a described comparison of model performance or prompt characteristics
across human- vs. LLM-authored prompts; statistical tests for differences between the two
prompt sources; a conclusion about whether LLM authorship biased the benchmark.

**Negative / disqualifying signals:** prompts authored or assisted by LLMs with no
human-written counterpart; human-written prompts present but too few to compare; no
comparative study reported; the comparison promised for a future version while the
published scores rely on LLM-assisted prompts without it.
