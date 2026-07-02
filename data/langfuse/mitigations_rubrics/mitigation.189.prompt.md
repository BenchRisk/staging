# Mitigation 189 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #189, which mitigates Failure Mode #2.
Source: data/mitigations/189.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 189
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock-market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you visualize and share what parts of the input space are covered versus missing?

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
  tasks. Subtasks isolate specific capabilities or dimensions; decomposing complex tasks
  into subtasks helps describe and chart what the benchmark does and does not cover.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`coverage_visualized`** — The documents present a visualization (e.g., a map, chart,
   matrix, taxonomy diagram, or coverage table) that depicts the input space / task space
   the benchmark targets, rather than only describing scope in prose.
2. **`covered_vs_missing_marked`** — The visualization (or its accompanying text)
   explicitly distinguishes regions that are covered from regions that are not covered or
   under-represented, so a user can see the gaps.
3. **`publicly_shared`** — This coverage artifact is published where users encounter the
   benchmark (paper, README, dataset/benchmark card, or leaderboard), not held internally
   or only promised.

**Strong positive signals:** a figure or table mapping categories/dimensions of the input
space with cells marked present/absent; an explicit taxonomy with counts per region and
called-out empty regions; a "what this benchmark does not cover" panel tied to the
visualization; a coverage heatmap over use cases, languages, domains, or difficulty.

**Negative / disqualifying signals:** scope described only in narrative prose with no
visualization; a visualization of *results* (scores) but nothing about input-space
coverage; coverage gaps acknowledged in text but no shared artifact showing covered vs.
missing; the coverage map described only for a planned future release.
