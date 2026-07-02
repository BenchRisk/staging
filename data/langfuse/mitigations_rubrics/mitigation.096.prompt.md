# Mitigation 096 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #96, which mitigates Failure Mode #29.
Source: data/mitigations/96.mdx and data/modes/29.mdx.
-->

## The mitigation under review

- **Mitigation number:** 96
- **Mitigates failure mode:** #29 — *"SUT developers produce training data from
  evaluator"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~60% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** Developers of a SUT gain access to the
  benchmark evaluator—either by reverse-engineering a public implementation or through a
  public API—and use it as a reward model or filtering mechanism during training or
  fine-tuning. This causes the model to optimize specifically for evaluator preferences,
  potentially learning to game the scoring mechanism through superficial alignment (e.g.,
  mimicking surface features that score well, like formality or verbosity) rather than
  achieving true task performance. As a result, the model performs exceptionally well on
  the benchmark but fails to generalize to tasks that aren't shaped by the evaluator's
  biases. A benchmark user, unaware of this overfitting loop, selects the system expecting
  robust general capabilities, only to encounter brittle outputs.

**Criterion question (answer this for the benchmark under review):**
> Does the evaluator apply an algorithm to compare model outputs against a list of correct
> answers to assess correctness or compliance?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, consistency, reproducibility, and independence. SUT developers violate them
  through practices such as benchmark overfitting and data snooping.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`algorithmic_evaluator`** — The evaluator applies a fixed algorithm (e.g.,
   exact/string match, programmatic checker) rather than a learned or generative model that
   could be repurposed as a reward model.
2. **`compares_against_answer_key`** — Scoring compares model outputs against a defined
   list of correct answers (a ground-truth key) to assess correctness or compliance.

**Strong positive signals:** an evaluation described as exact-match/regex/unit-test scoring
against a published or held-out answer key; a deterministic checker that confers no
gameable training signal; a stated separation preventing SUT developers from using the
evaluator as a reward model; an answer key not exposed via an open scoring API.

**Negative / disqualifying signals:** a model-based evaluator (LLM-as-a-judge or learned
scorer) that could be reverse-engineered or queried as a reward model; an openly callable
scoring service that returns gradients-equivalent signal; no answer key or correctness list
described; algorithmic scoring described only as a planned change.
