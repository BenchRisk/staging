# Mitigation 126 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #126, which mitigates Failure Mode #52.
Source: data/mitigations/126.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 126
- **Mitigates failure mode:** #52 — *"Benchmark production failed to account for an
  idiosyncratic failure mode"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark developer failed to read a
  recent research paper listing common failure modes and potential mitigations. As a
  result, the benchmark authors fail to publish integrity requirements at the time their
  benchmark is published. Subsequently, a SUT developer trains to the benchmark's sample
  set and overperforms relative to its actual performance. Consequently, a user adopts
  what would ordinarily be known as a poor performing SUT.

**Criterion question (answer this for the benchmark under review):**
> Are the test tasks and the rationale behind them documented?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **System Under Test (SUT) Task:** The specific activity or objective the SUT is
  expected to perform in the real world; a well-defined SUT task gives the benchmark the
  capacity to measure and report properties related to that task.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`test_tasks_documented`** — The test tasks the benchmark uses are documented: what
   the SUT is asked to do and the structure/scope of those tasks.
2. **`rationale_documented`** — The rationale behind the test tasks is documented — why
   these tasks were chosen and how they relate to the property the benchmark intends to
   measure, not just the tasks in isolation.

**Strong positive signals:** a description of each task or task category with its purpose;
an explicit justification linking tasks to the measured construct or real-world need; a
section explaining task-selection criteria and what was deliberately included or excluded.

**Negative / disqualifying signals:** tasks are listed with no explanation of why they
were chosen; rationale is absent or assumed; only example items are shown with no account
of the task design; the rationale is promised for a future version while the published
one omits it.
