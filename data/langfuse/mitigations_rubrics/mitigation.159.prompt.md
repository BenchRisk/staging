# Mitigation 159 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #159, which mitigates Failure Mode #35.
Source: data/mitigations/159.mdx and data/modes/35.mdx.
-->

## The mitigation under review

- **Mitigation number:** 159
- **Mitigates failure mode:** #35 — *"Failure to propagate uncertainty or confidence from
  lower level measures to higher level grades"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (5) Scoring
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~58.33%
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
> Is the property of interest appropriately measurable without aggregating across
> different subpopulations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Lower-level Measures to Higher-level Grades:** The hierarchical structure used in
  scoring SUTs, where lower-level measures (e.g., accuracy, precision, recall, error
  rates) feed into higher-level grades (e.g., an overall safety score or general
  performance rating).
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Subtasks isolate specific capabilities or dimensions, supporting modular scoring
  and improving the interpretability of benchmark results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`measurable_without_aggregation`** — The property of interest is appropriately
   measurable on its own without collapsing distinct subpopulations into a single score —
   i.e., the benchmark does not require aggregating across heterogeneous subpopulations to
   report the property.
2. **`subpopulation_resolution`** — Results are reported at the subpopulation/subtask
   level (rather than only as one aggregate grade), so per-subpopulation measurement is
   preserved and the uncertainty of each is not hidden by a single roll-up.

**Strong positive signals:** documentation that the property is reported per
subpopulation/subtask rather than as a single aggregate; explicit per-condition or
per-slice scores; a stated decision not to combine heterogeneous subpopulations into one
grade; uncertainty/confidence reported alongside each subpopulation result.

**Negative / disqualifying signals:** a single headline grade aggregated across diverse
subpopulations with no breakdown; per-slice uncertainty dropped on the way to the overall
score; subpopulation differences acknowledged but not separately measured/reported;
subpopulation reporting described only for a future version.
