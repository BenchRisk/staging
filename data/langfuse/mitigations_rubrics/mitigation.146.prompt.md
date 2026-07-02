# Mitigation 146 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #146, which mitigates Failure Mode #16.
Source: data/mitigations/146.mdx and data/modes/16.mdx.
-->

## The mitigation under review

- **Mitigation number:** 146
- **Mitigates failure mode:** #16 — *"An inadequate number of prompts are produced to
  identify rare critical events (i.e., tail risks)"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~23.33% reduction in failure-mode likelihood; ~50%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate a model's
  ability to detect financial fraud runs 500 prompts, including several fraud scenarios
  that must be detected with very high probability, such as coordinated international
  money laundering. However, the number of prompts focusing on these rare, high-impact
  events is too small to reliably determine when a system drops below the required 99.9
  percent detection rate. As a result, most models pass the benchmark with a high score.
  The benchmark user assumes a passing model meets requirements and deploys it,
  overlooking the fact that the benchmark may not detect coordinated money laundering at
  a sufficient rate.

**Criterion question (answer this for the benchmark under review):**
> Is it established in the task definition that rare events (i.e., tail risks) are not of
> interest to the benchmark-relying person?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Information Foraging:** The process by which users search for, evaluate, and extract
  useful information within an environment, guided by perceived value relative to effort.
  In LLM benchmarking it refers to how people develop a mental model about SUTs — here,
  what the benchmark-relying person needs to learn, and whether tail risks are part of
  that need.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`tail_risk_scope_stated`** — The task definition explicitly establishes that rare
   events / tail risks are out of scope — i.e., not of interest to the benchmark-relying
   person — so users do not mistakenly read the score as covering them.
2. **`stated_in_task_definition`** — This scope limitation appears in the benchmark's
   task definition / intended-use documentation where a relying user would encounter it,
   not only implied or buried.

**Strong positive signals:** an explicit scope statement that the benchmark does not
target rare / tail-risk events; an intended-use or limitations section disclaiming
detection of rare critical events; clear framing that the score concerns typical-case
performance and not low-frequency high-impact cases.

**Negative / disqualifying signals:** no statement about tail risks, leaving users to
assume coverage; the benchmark implies it measures rare critical events without adequate
sampling to do so; scope of rare-event coverage left ambiguous; the limitation noted only
in passing or in an appendix rather than the task definition; the disclaimer is planned
for a future release.
