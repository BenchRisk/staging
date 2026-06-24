# Mitigation 142 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #142, which mitigates Failure Mode #8.
Source: data/mitigations/142.mdx and data/modes/8.mdx.
-->

## The mitigation under review

- **Mitigation number:** 142
- **Mitigates failure mode:** #8 — *"Prompt writers produce prompts with inadequate
  variability within the valid input space (e.g., a single prompt writer writes all the
  prompts)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to test reasoning
  over legal contracts uses 500 prompts, all written by a single legal expert. Although
  the expert is highly knowledgeable, their prompts all follow similar structures,
  phrasings, and assumptions. As a result, the SUT learns to pick up on these patterns
  and performs well. However, when deployed to assist general counsel teams, the model
  fails to handle real-world contract analysis tasks that involve diverse linguistic
  styles, jurisdictions, and edge cases. The benchmark user trusts the high benchmark
  score and integrates the model into a high-stakes legal review process, leading to
  costly misinterpretations.

**Criterion question (answer this for the benchmark under review):**
> Do you define the information foraging task of the benchmark-relying user in a way that
> allows for sampling over the input space rather than requiring comprehensive coverage?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Information Foraging:** The process by which users search for, evaluate, and extract
  useful information within an environment, guided by perceived value relative to effort
  (information scent). In LLM benchmarking it refers to how people develop a mental model
  about SUTs. The *information foraging task* is the specific goal or question a user is
  trying to answer when engaging with the benchmark.
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`foraging_task_defined`** — The information foraging task of the benchmark-relying
   user is defined — what real-world goal/question the benchmark is meant to inform.
2. **`sampling_framing`** — That definition is framed so the input space can be *sampled*
   (statistical inference from a sample to the broader space) rather than requiring
   exhaustive, comprehensive coverage of every case.

**Strong positive signals:** an explicit statement of the user's information foraging
task / decision the score informs; framing of the prompt set as a sample drawn from a
defined input distribution; a described sampling strategy or population the prompts are
meant to represent; acknowledgment that coverage is by sampling, not enumeration.

**Negative / disqualifying signals:** no statement of the user's foraging task; the
benchmark implicitly claims comprehensive coverage rather than sampling; the input space
and its distribution are undefined; prompts presented as an exhaustive checklist with no
sampling rationale; task framing left to the reader to infer.
