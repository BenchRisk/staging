# Mitigation 171 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #171, which mitigates Failure Mode #56.
Source: data/mitigations/171.mdx and data/modes/56.mdx.
-->

## The mitigation under review

- **Mitigation number:** 171
- **Mitigates failure mode:** #56 — *"The benchmark authors do not know how to formulate
  the problem as prompts that are illustrative to the user relying on the benchmark"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark aims to evaluate a language
  model's ability to assist with complex project planning. However, the benchmark authors,
  lacking deep expertise in project management (i.e., they are not domain experts), create
  prompts that are overly simplistic, focusing on isolated sub-tasks with clear,
  unambiguous instructions. A user looking to employ an LLM for real-world project
  planning faces messy, ill-defined problems with conflicting priorities and the need for
  nuanced decision-making. The top-performing model on the benchmark excels at the
  straightforward tasks presented but falters significantly when confronted with the
  ambiguity and complexity of real-world project scenarios. The user, misled by the
  benchmark's seemingly relevant task, selects a model that ultimately proves unhelpful
  for their actual needs because the benchmark prompts failed to capture the essential
  challenges of project planning as experienced in practice.

**Criterion question (answer this for the benchmark under review):**
> Do you involve domain experts in defining the task and prompts?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task (e.g., a project
  management expert for a project-planning benchmark). A person without specialized
  knowledge in the benchmarked domain is not a domain expert; formal training is not
  required where significant experience exists.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`experts_in_task_definition`** — The documents state that domain experts participated
   in defining the benchmark task (its scope, framing, and what counts as success).
2. **`experts_in_prompt_design`** — The documents state that domain experts participated
   in producing or vetting the prompts, so the prompts illustrate the real-world problem
   the relying user faces.

**Strong positive signals:** named domain-expert contributors or advisory involvement in
task and prompt design; a described process where experts reviewed prompts for real-world
fidelity; prompts shown to reflect messy, realistic problem framings rather than
simplified toy cases.

**Negative / disqualifying signals:** task and prompts authored without relevant domain
expertise; only generalists or annotators with no domain knowledge involved; expert
involvement claimed for the task but not the prompts (or vice versa); expert review
described only as a future plan.
