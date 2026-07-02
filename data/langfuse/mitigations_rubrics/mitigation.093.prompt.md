# Mitigation 093 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #93, which mitigates Failure Mode #25.
Source: data/mitigations/93.mdx and data/modes/25.mdx.
-->

## The mitigation under review

- **Mitigation number:** 93
- **Mitigates failure mode:** #25 — *"SUT developers place evaluator or other test ground
  truth within system chain"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** During a jailbreak benchmark evaluation, a
  SUT is configured with access to the benchmark's LLM-as-a-judge, which determines whether
  the outputs of the SUT have been jailbroken or not. With access to the LLM-as-a-judge,
  the LLM scores perfectly on the benchmark. However, the LLM-as-a-judge is not perfectly
  accurate so it obscures the true failures of the SUT. A SUT deployer adopts the
  non-perfect LLM thinking it is actually perfect and will not be jailbroken.

**Criterion question (answer this for the benchmark under review):**
> Is the evaluator strictly algorithmic (i.e., applying a list of correct answers) with no
> legitimate reason to be embedded in the system-under-test (SUT) chain?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling it to produce restricted, harmful, or unintended
  outputs. In benchmarking, jailbreaks test the robustness of safety measures and identify
  points of failure in content moderation or policy adherence.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`algorithmic_evaluator`** — The evaluator is strictly algorithmic, scoring outputs by
   applying a fixed list of correct answers (e.g., exact/string match against a key)
   rather than relying on a learned or generative judge model.
2. **`evaluator_separate_from_sut`** — The documents show no legitimate reason for the
   evaluator (or test ground truth) to be embedded in the SUT chain, and that it is kept
   outside the SUT's reach during evaluation.

**Strong positive signals:** an evaluation described as exact-match/regex/answer-key
scoring; an explicitly held-out answer key that the SUT cannot access; an architecture
diagram or description placing the evaluator outside the SUT pipeline; a stated rule that
the judge/ground truth is never exposed to the system being scored.

**Negative / disqualifying signals:** an LLM-as-a-judge or other model-based evaluator
used for scoring; the evaluator or answer key reachable by the SUT (e.g., via tool access
or shared context); no description of how evaluation is isolated from the SUT chain;
algorithmic scoring claimed only for a future version.
