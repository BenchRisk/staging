# Mitigation 153 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #153, which mitigates Failure Mode #27.
Source: data/mitigations/153.mdx and data/modes/27.mdx.
-->

## The mitigation under review

- **Mitigation number:** 153
- **Mitigates failure mode:** #27 — *"Low interrater reliability of ground truth data
  used to tune the evaluator"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~96.67% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses human annotators to
  generate ground truth labels or scores that are later used to train an automated
  evaluator. However, the annotators frequently disagree on task success criteria — such
  as what constitutes a "correct," "helpful," or "safe" response — due to vague
  instructions, subjective judgments, or cultural differences. This results in low
  interrater reliability, with inconsistent and noisy labels forming the basis of the
  evaluator's training data. As a result, the evaluator itself becomes unreliable, often
  reflecting annotator bias or randomness rather than objective quality. A benchmark user,
  unaware of this underlying inconsistency, trusts the evaluator's scores and selects a
  system that performs well on flawed metrics but poorly in actual deployment scenarios.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark use singular answers that are checked against a list?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs, tasks, or
  behaviors. High interrater reliability indicates the evaluation criteria are
  well-defined, interpretable, and applied consistently. It is commonly quantified using
  measures such as Cohen's kappa.
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`singular_answers`** — Each item has a singular, well-defined correct answer rather
   than a subjective or open-ended judgment.
2. **`checked_against_list`** — Grading is performed by checking the SUT output against a
   fixed list/set of accepted answers, removing reliance on subjective rater judgment (and
   thus the interrater-reliability concern in the failure mode).

**Strong positive signals:** documentation that answers are single, canonical values
graded by membership in an answer key or accepted-answer list; multiple-choice or exact
short-answer formats; a published answer list or lookup against which outputs are matched;
no human/LLM subjective scoring of open responses.

**Negative / disqualifying signals:** open-ended responses scored by human raters or an
LLM judge; subjective rubric criteria ("helpful," "safe," "correct") requiring
interpretation; answers tuned from disputed annotations rather than checked against a
fixed list; the singular-answer/list approach described only for a future version.
