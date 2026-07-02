# Mitigation 055 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #55, which mitigates Failure Mode #31.
Source: data/mitigations/55.mdx and data/modes/31.mdx.
-->

## The mitigation under review

- **Mitigation number:** 55
- **Mitigates failure mode:** #31 — *"Evaluator(s) perform poorly across all SUTs"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark employs undergraduate
  psychology students with no technical background to evaluate advanced AI reasoning on
  complex mathematical proofs. These evaluators cannot distinguish between correct proofs
  and those with subtle errors, giving high scores to any response that looks
  sophisticated regardless of accuracy. As a result, all tested systems receive similarly
  high scores despite vast differences in actual mathematical reasoning capabilities. The
  benchmark user selects the cheapest SUT thinking it performs equivalently to premium
  options, then deploys it to verify critical engineering calculations for a bridge
  design, resulting in structural flaws being missed and necessitating costly redesigns
  when discovered by other verification methods.

**Criterion question (answer this for the benchmark under review):**
> Do you iteratively improve your evaluator model and validate its performance until it
> reaches a predefined performance threshold?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged here to validate that an evaluator correctly judges the SUT's
  task (e.g., a mathematician for mathematical reasoning). A person without specialized
  knowledge within the benchmarked domain is not a domain expert.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`evaluator_validated`** — The evaluator's performance is validated against ground
   truth or expert judgment, rather than assumed adequate.
2. **`predefined_threshold`** — Validation is held to a predefined performance threshold
   (e.g., a target accuracy/agreement level) that the evaluator must reach.
3. **`iterative_improvement`** — The evaluator is iteratively improved until it meets that
   threshold, with the improvement loop described.

**Strong positive signals:** reported evaluator accuracy/agreement against a gold or
expert-labeled set; a stated acceptance threshold the evaluator had to meet; described
iterations or refinements to the evaluator with before/after metrics; expert-validated
evaluation criteria.

**Negative / disqualifying signals:** evaluator quality unmeasured or asserted without
data; no stated threshold for acceptable evaluator performance; one-shot evaluator with no
validation or iteration; evaluators chosen by convenience/cost with no competence check;
validation described only as future work.
