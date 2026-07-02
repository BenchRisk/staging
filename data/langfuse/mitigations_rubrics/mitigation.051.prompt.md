# Mitigation 051 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #51, which mitigates Failure Mode #35.
Source: data/mitigations/51.mdx and data/modes/35.mdx.
-->

## The mitigation under review

- **Mitigation number:** 51
- **Mitigates failure mode:** #35 — *"Failure to propagate uncertainty or confidence from
  lower level measures to higher level grades"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (5) Scoring
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~33.33%
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
> Do you identify and call out specific qualities of prompt subpopulations where SUT
> performance is systematically worse?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be understood
  by intended users, ensuring they can accurately interpret and use the benchmark for
  real-world decisions. It asks, "will the relying user understand the LLM properties as
  evidenced by the benchmark?"
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Subtasks isolate specific capabilities or dimensions that contribute to overall
  benchmark performance, supporting modular scoring and improving the interpretability of
  results.
- **Lower-level Measures to Higher-level Grades:** The hierarchical structure used in
  scoring SUTs, where lower-level measures (e.g., accuracy, precision, recall on specific
  slices) feed into higher-level grades (e.g., an overall safety or competency score).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`subpopulation_breakdown`** — Results are reported per prompt subpopulation, slice,
   subtask, or category, not only as a single aggregate grade.
2. **`weak_slices_identified`** — The benchmark explicitly identifies and names the
   specific subpopulations where SUT performance is systematically worse, rather than
   leaving such gaps for the reader to infer.

**Strong positive signals:** a per-category/per-slice results table or breakdown;
explicit callouts of "areas where the model underperforms" or worst-performing subgroups;
reported confidence intervals or sample sizes per slice; narrative discussion of which
prompt qualities drive systematically lower scores.

**Negative / disqualifying signals:** only a single aggregate score reported; subgroup
performance buried with no callout of where it is systematically worse; uncertainty or
variance from low-sample slices collapsed into the headline number; weak slices mentioned
only as future analysis.
