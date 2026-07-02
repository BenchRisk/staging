# Mitigation 191 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #191, which mitigates Failure Mode #2.
Source: data/mitigations/191.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 191
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~40% reduction in failure-mode likelihood; ~50%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock-market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life
  savings trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Have you red-teamed the evaluation to identify undercovered input space regions and
> generated additional data for those areas?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Sophisticated User:** An individual with advanced knowledge, experience, or technical
  skill supporting their understanding of information conveyed by the benchmark — e.g.,
  red-team members, researchers, and domain experts capable of systematically probing
  model and benchmark limitations.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`red_team_conducted`** — The documents describe a deliberate red-teaming or
   adversarial review of the *evaluation's coverage* aimed at finding under-covered or
   missing regions of the input/task space (not red-teaming of the SUT itself).
2. **`gaps_identified`** — That process surfaced specific under-covered regions, which
   the documents name or characterize.
3. **`data_generated_for_gaps`** — Additional benchmark data was created and incorporated
   to fill those identified gaps in the currently published benchmark.

**Strong positive signals:** a described coverage red-team or gap-analysis exercise; a
list of regions found to be thin or missing; a record of new prompts/items added to
address those regions; before/after coverage comparison showing the gaps filled.

**Negative / disqualifying signals:** no coverage red-teaming described; gaps identified
but no data generated to address them; red-teaming aimed only at SUT robustness, not at
benchmark coverage; the gap-filling described only as future work while the published
benchmark still omits the data.
