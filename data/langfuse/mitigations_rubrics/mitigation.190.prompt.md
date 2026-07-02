# Mitigation 190 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #190, which mitigates Failure Mode #2.
Source: data/mitigations/190.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 190
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~66.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock-market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you report metrics indicating coverage of the task space?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Subtasks isolate specific capabilities or dimensions; reporting counts or
  proportions per subtask is one way to quantify coverage of the task space.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`coverage_metric_defined`** — The documents define one or more quantitative metrics
   that measure how much of the intended task/input space the benchmark covers (e.g.,
   number of categories represented, proportion of a taxonomy populated, distribution of
   instances across subtasks, domains, languages, or difficulty bands).
2. **`metric_reported`** — Actual values of those coverage metrics are reported for the
   currently published benchmark, not merely named or proposed.

**Strong positive signals:** a table giving counts/percentages per category, domain, or
subtask; a stated proportion of a reference taxonomy that the benchmark instantiates;
diversity or coverage statistics (e.g., distribution across use cases) with numbers; an
explicit "coverage = X% of intended task space" figure.

**Negative / disqualifying signals:** coverage discussed only qualitatively ("broad,"
"diverse") with no metric; total instance counts given but nothing relating them to the
task space; a coverage metric defined but no values reported; coverage numbers promised
for a future version while the published version omits them.
