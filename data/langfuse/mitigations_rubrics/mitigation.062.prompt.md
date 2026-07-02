# Mitigation 062 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #62, which mitigates Failure Mode #7.
Source: data/mitigations/62.mdx and data/modes/7.mdx.
-->

## The mitigation under review

- **Mitigation number:** 62
- **Mitigates failure mode:** #7 — *"Singular prompts without a distributional tie lack a
  capacity for detecting distributional failings, harms, or impacts"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~58.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses only a handful of
  standalone prompts to test bias in medical diagnosis advice. The prompts are about heart
  attack symptoms in middle-aged men. The SUT passes the test. However, when deployed, the
  SUT systematically fails to recognize heart attack symptoms in women and younger
  patients due to underrepresentation in training and evaluation data. The benchmark user
  deploys the model in a clinical triage assistant, and it contributes to misdiagnosis and
  delayed care for several patients outside the narrow demographic tested in the
  benchmark.

**Criterion question (answer this for the benchmark under review):**
> Do you produce data with distributional associations when designing your benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances.
  An example is resume-screening software that may disproportionately reject candidates
  from a poor state; assessing such distributional harms is contingent on having data with
  a distributional association (i.e., annotations supporting distributional evaluation).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`distributional_data`** — The benchmark's prompt data carries distributional
   associations (e.g., annotations or grouping that tie prompts to demographic, subgroup,
   or other distributional dimensions) rather than only standalone, untied prompts.
2. **`distributional_evaluation`** — Those associations are usable for evaluating
   properties expressed in distribution (e.g., disparate performance across subgroups),
   not merely instance-by-instance pass/fail.

**Strong positive signals:** prompts annotated with demographic/subgroup or other
distributional attributes; reported analyses of performance across those groups;
deliberate coverage of subpopulations enabling distributional/bias measurement; a stated
methodology for distributional evaluation.

**Negative / disqualifying signals:** only a handful of standalone prompts with no
distributional tie; no subgroup/demographic annotations; results reported only as
aggregate pass/fail with no capacity to detect distributional harms; distributional data
described only as a future addition.
