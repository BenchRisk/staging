# Mitigation 046 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #46, which mitigates Failure Mode #25.
Source: data/mitigations/46.mdx and data/modes/25.mdx.
-->

## The mitigation under review

- **Mitigation number:** 46
- **Mitigates failure mode:** #25 — *"SUT developers place evaluator or other test ground
  truth within system chain"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** During a jailbreak benchmark evaluation, a
  SUT is configured with access to the benchmark's LLM-as-a-judge, which determines
  whether the outputs of the SUT have been jailbroken or not. With access to the
  LLM-as-a-judge, the LLM scores perfectly on the benchmark. However, the LLM-as-a-judge
  is not perfectly accurate so it obscures the true failures of the SUT. A SUT deployer
  adopts the non-perfect LLM thinking it is actually perfect and will not be jailbroken.

**Criterion question (answer this for the benchmark under review):**
> Do you use 100% human evaluators for assessing system performance?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  SUT for correctness, safety, or some other measurable property. This mitigation asks
  whether that evaluator is 100% human.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling restricted, harmful, or unintended outputs. In
  benchmarking, jailbreaks test the robustness of safety measures and identify points of
  failure that the evaluator must correctly judge.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_evaluation`** — The benchmark's outputs are scored by human evaluators.
2. **`fully_human_no_automated_judge`** — Evaluation is 100% human: there is no
   LLM-as-a-judge or other automated evaluator producing the scores (and thus no judge a
   SUT could be wired to or game).

**Strong positive signals:** an explicit statement that all outputs are scored by human
raters; described human annotation protocols, rater pools, or guidelines; no
LLM-as-a-judge in the scoring pipeline; human review used even where automation would be
cheaper.

**Negative / disqualifying signals:** an LLM-as-a-judge or automated classifier producing
the scores; a "hybrid" or human-spot-check setup where machines do most grading; humans
used only to validate an automated evaluator that still produces the published scores; the
evaluator model accessible to or embedded with the SUT; full human evaluation described
only as a future plan.
