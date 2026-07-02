# Mitigation 004 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #4, which mitigates Failure Mode #3.
Source: data/mitigations/4.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 4
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with the
  aid of Llama4 in the crowd worker interface to improve their performance. Consequently,
  the prompts are biased to the word usage of Llama4 and it performs higher on the
  benchmark than it otherwise would. The benchmark user selects Llama4 even though it is
  not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you run a study on any system under test (SUT) that may have been privileged during
> prompt generation, and compare its performance to SUTs not involved in prompt
> generation? If an unfair advantage is found, do you drop the LLM-generated instances?

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

1. **`privilege_study_run`** — The documents report an actual study comparing the
   performance of SUTs that may have been privileged during prompt generation (e.g., the
   LLM used to write prompts) against SUTs not involved in prompt generation.
2. **`comparison_to_uninvolved_suts`** — The comparison explicitly contrasts the
   potentially privileged SUT(s) with one or more SUTs that played no role in generating
   the prompts, so an unfair advantage would be detectable.
3. **`remediation_on_advantage`** — If an unfair advantage is found, the documents show
   the LLM-generated instances were dropped (or report that the study found no advantage,
   so no removal was needed).

**Strong positive signals:** a reported experiment measuring whether the prompt-generating
model scores anomalously high; per-model results split by instance provenance
(LLM-generated vs. human-written); a stated rule that flagged instances were removed and a
count of how many were dropped; a fairness/leakage audit tied to prompt generation.

**Negative / disqualifying signals:** no contamination or advantage study reported; the
risk acknowledged but never tested; results not broken out by whether a SUT contributed to
prompt generation; an advantage found but the affected instances retained; the study
described only as future work.
