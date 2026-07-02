# Mitigation 034 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #34, which mitigates Failure Mode #35.
Source: data/mitigations/34.mdx and data/modes/35.mdx.
-->

## The mitigation under review

- **Mitigation number:** 34
- **Mitigates failure mode:** #35 — *"Failure to propagate uncertainty or confidence from
  lower level measures to higher level grades"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (5) Scoring
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~58.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates AI medical diagnosis
  capabilities across 50 different conditions and aggregates these results into a single
  "Medical Competency Score." Each condition assessment has different confidence intervals
  based on sample size and evaluator expertise, but these uncertainties are lost in the
  final score calculation. A particular SUT scores 98% overall due to strong performance
  on common conditions with large sample sizes, masking its poor performance on rare
  conditions where data is limited. The benchmark user implements this system in a rural
  hospital with different disease prevalence patterns than those emphasized in the
  benchmark. The system consistently misdiagnoses several locally common conditions that
  had wide confidence intervals in the original evaluation, leading to inappropriate
  treatments and delayed correct diagnoses for numerous patients before the pattern is
  recognized.

**Criterion question (answer this for the benchmark under review):**
> Do you prominently display uncertainty estimates alongside your benchmark results?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Lower-level Measures to Higher-level Grades:** The hierarchical structure used in
  scoring SUTs, in which lower-level measures (e.g., accuracy, error rates, per-condition
  scores) feed into higher-level grades (e.g., an overall safety or competency score).
  Uncertainty present in the lower-level measures should be carried through to the
  higher-level grade rather than discarded in aggregation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`uncertainty_reported`** — Each reported result is accompanied by an uncertainty
   estimate (e.g., confidence interval, standard error, variance, or credible interval),
   not just a point value.
2. **`propagated_to_aggregate`** — Uncertainty from the lower-level measures is carried
   through to any aggregate or headline grade, so the top-line score itself shows its
   uncertainty rather than discarding it during aggregation.
3. **`displayed_prominently`** — The uncertainty appears where users actually read the
   results (next to the score in tables, charts, or the leaderboard), not buried in an
   appendix or supplementary material.

**Strong positive signals:** error bars or ± intervals shown next to every headline
score; confidence intervals reported for the aggregate grade, not only per-item; methods
text describing how per-measure uncertainty is combined into the overall score; results
tables with a dedicated CI/std-error column; cautions that overlapping intervals mean
systems are not distinguishable.

**Negative / disqualifying signals:** a single point score per SUT with no interval;
uncertainty shown only for individual subtasks but dropped from the headline grade; CIs
mentioned in prose but absent from the user-facing leaderboard/figures; aggregation that
averages away per-condition variance without reporting it; uncertainty promised for a
future release while current results show bare numbers.
