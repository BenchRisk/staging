# Mitigation 162 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #162, which mitigates Failure Mode #2.
Source: data/mitigations/162.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 162
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you list and make available a complete definition of what is and isn’t covered by
> the benchmark?

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
  tasks. Subtasks isolate specific capabilities or dimensions that contribute to overall
  benchmark performance and help delineate what the benchmark does and does not cover.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`scope_definition_published`** — The documents include an explicit definition of the
   benchmark's coverage — which tasks, capabilities, domains, or conditions fall within
   scope — rather than only a broad or aspirational label.
2. **`out_of_scope_stated`** — The definition also states what is *not* covered (explicit
   exclusions, limitations, or boundaries), so a user cannot over-generalize the score.
3. **`complete_and_available`** — This coverage definition is reasonably complete and
   publicly accessible where users encounter the benchmark, not partial or buried.

**Strong positive signals:** a "scope," "what this benchmark does/does not measure," or
"limitations" section; an enumerated list of covered subtasks/domains with explicit
exclusions; cautions against extrapolating the score beyond the tested use cases.

**Negative / disqualifying signals:** the benchmark is described only by a broad umbrella
term (e.g., "general intelligence," "reasoning") with no coverage map; no statement of
exclusions or boundaries; coverage left implicit so the reader must infer what is tested;
scope described only for a planned future expansion.
