# Mitigation 064 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #64, which mitigates Failure Mode #2.
Source: data/mitigations/64.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 64
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~50.0% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you prominently state that the benchmark does not fully cover the input space, and
> clarify its limitations in coverage?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`coverage_limits_stated`** — The benchmark explicitly states that it does not fully
   cover the input space and describes what its coverage does and does not include (the
   bounds of the use case it actually tests).
2. **`prominent`** — This limitation statement appears where users actually encounter the
   benchmark (e.g., abstract/intro, README, benchmark/dataset card, landing page,
   leaderboard description), not only buried in an appendix or external material.

**Strong positive signals:** an explicit "limitations / scope / what this does not
measure" section near the top of primary docs; concrete enumeration of input types or
subdomains that are out of scope; cautionary language warning users against
over-generalizing the score; coverage caveats repeated on the leaderboard or card.

**Negative / disqualifying signals:** the benchmark is presented as measuring a broad or
"general" capability with no stated boundaries; limitations mentioned only deep in an
appendix or buried in code/comments; scope left implicit so the reader must infer it;
coverage caveats described only for a future version while the published version omits
them.
