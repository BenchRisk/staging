# Mitigation 188 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #188, which mitigates Failure Mode #2.
Source: data/mitigations/188.mdx and data/modes/2.mdx.
-->

## The mitigation under review

- **Mitigation number:** 188
- **Mitigates failure mode:** #2 — *"The task is defined too broadly to achieve any
  reasonable degree of coverage over the use case."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark represents itself as testing
  SUT "general intelligence." A user then believes a system with the maximum benchmark
  score is capable of giving stock-market trading advice, but the benchmark does not test
  anything related to finance. The user relies on the benchmark and loses his life savings
  trading derivatives.

**Criterion question (answer this for the benchmark under review):**
> Do you sample prompts from the input space according to their real-world likelihood of
> occurrence (e.g., based on analysis of deployed systems)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically in
  natural language. Prompts define the context, task, or question the system is expected
  to respond to and are central to evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`representative_sampling`** — Prompts are sampled from the input space according to
   their real-world likelihood of occurrence, rather than chosen arbitrarily or to make a
   broad task look covered.
2. **`grounded_in_deployment_analysis`** — The sampling distribution is grounded in
   evidence of real-world frequency (e.g., analysis of deployed systems, usage data, or a
   documented occurrence model), not merely asserted.

**Strong positive signals:** a described sampling methodology weighted by real-world
frequency; use of deployed-system logs, usage statistics, or a population/occurrence
analysis to set proportions; an explicit statement that the prompt mix reflects how often
inputs occur in practice; documentation of the source distribution used.

**Negative / disqualifying signals:** prompts chosen arbitrarily, by convenience, or to
fill a broad "general" task; no link between the prompt distribution and real-world
likelihood; uniform or undocumented sampling presented as representative; deployment-based
sampling described only as a future plan.
