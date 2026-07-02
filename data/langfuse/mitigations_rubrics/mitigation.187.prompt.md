# Mitigation 187 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #187, which mitigates Failure Mode #2.
Source: data/mitigations/187.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 187
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock-market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life savings
  trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Have you split the benchmark into smaller, focused subtasks and presented scores for
> those subtasks separately?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Decomposing complex tasks into subtasks lets evaluators diagnose strengths and
  weaknesses, support modular scoring, and improve the interpretability of results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`split_into_subtasks`** — The benchmark is split into smaller, focused subtasks
   rather than one broad/monolithic task, narrowing what each portion measures.
2. **`subtask_scores_separate`** — Scores for those subtasks are presented separately, so
   a user can read per-subtask performance and not just a single aggregate.

**Strong positive signals:** a defined set of named subtasks or categories, each scoped
to a specific capability; a results table/leaderboard reporting per-subtask scores
distinctly; documentation tying each subtask to a part of the use case; an explicit
rationale that decomposition improves coverage clarity.

**Negative / disqualifying signals:** a single broad task with one composite score and no
breakdown; subtasks defined but only an aggregate score reported; "general" framing with
no focused subdivisions; subtask reporting described only for a future version.
