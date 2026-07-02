# Mitigation 028 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #28, which mitigates Failure Mode #25.
Source: data/mitigations/28.mdx and data/modes/25.mdx.
-->

## The mitigation under review

- **Mitigation number:** 28
- **Mitigates failure mode:** #25 — *"SUT developers place evaluator or other test
  ground truth within system chain."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** During a jailbreak benchmark evaluation, a
  SUT is configured with access to the benchmark's LLM-as-a-judge, which determines
  whether the outputs of the SUT have been jailbroken or not. With access to the
  LLM-as-a-judge, the LLM scores perfectly on the benchmark. However, the LLM-as-a-judge
  is not perfectly accurate, so it obscures the true failures of the SUT. A SUT deployer
  adopts the non-perfect LLM thinking it is actually perfect and will not be jailbroken.

**Criterion question (answer this for the benchmark under review):**
> Do you refrain from making the evaluator or ground truth publicly available?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling it to produce restricted, harmful, or unintended
  outputs; in benchmarking, jailbreaks test the robustness of safety measures.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluator_withheld`** — The benchmark's evaluator (e.g., the LLM-as-a-judge or
   scoring model/code) is **not** made publicly available in a way that lets a SUT
   developer place it within their system chain.
2. **`ground_truth_withheld`** — The benchmark's ground-truth answers/labels are likewise
   not made publicly available.

**Strong positive signals:** an explicit statement that the evaluator/judge is kept
private or held out; ground-truth labels withheld or available only through a controlled
submission; access to scoring mediated by the benchmark team rather than distributed;
documentation that the judge model and answer keys are not released.

**Negative / disqualifying signals:** the evaluator/judge model or code is published or
downloadable; ground-truth answers are public; the SUT can query the judge directly;
withholding mentioned only as a future intention; the answer key shipped alongside the
prompts.
