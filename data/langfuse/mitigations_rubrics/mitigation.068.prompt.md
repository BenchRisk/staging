# Mitigation 068 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #68, which mitigates Failure Mode #2.
Source: data/mitigations/68.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 68
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you reduce the scope of the benchmark to ensure comprehensive coverage of the input
> space is achievable?

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
  tasks. Subtasks isolate specific capabilities and, by decomposing complex tasks,
  improve the interpretability of benchmark results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`scope_narrowed`** — The benchmark defines a deliberately narrowed, specific scope
   (a bounded SUT task or set of subtasks) rather than claiming a broad or "general"
   capability, so that comprehensive coverage of the input space is plausible.
2. **`coverage_achievable`** — The documents connect that narrowed scope to achievable
   coverage of its input space (e.g., the bounded task is shown to be substantially
   covered by the prompts).

**Strong positive signals:** an explicitly bounded task definition with stated in-scope
inputs; justification that the scope was chosen to make coverage attainable; evidence the
prompt set spans the declared (narrow) input space; decomposition into well-defined
subtasks each with its own coverage.

**Negative / disqualifying signals:** the benchmark claims broad/general capability with
no scope reduction; scope is described so broadly that full coverage is implausible; no
link between the declared scope and the prompts' actual coverage; scope reduction
described only as a future plan while the published version remains broad.
