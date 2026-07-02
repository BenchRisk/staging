# Mitigation 193 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #193, which mitigates Failure Mode #14.
Source: data/mitigations/193.mdx and data/modes/14.mdx.
-->

## The mitigation under review

- **Mitigation number:** 193
- **Mitigates failure mode:** #14 — *"Benchmark does not capture the distribution or
  variability of the task in the real world."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~70% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating summarization
  quality uses a fixed set of short, well-structured news articles from a single outlet.
  All inputs are grammatically clean and follow similar structures. The scores suggest
  high summarization quality, but when the model is deployed on messy meeting
  transcripts, scientific papers, or user-generated content, it fails to produce coherent
  or accurate summaries. The benchmark user, trusting the strong results, integrates the
  model into a productivity suite, leading to summaries that are frequently misleading,
  incomplete, or incoherent in actual usage.

**Criterion question (answer this for the benchmark under review):**
> Were domain experts involved in benchmark construction with the goal of capturing the
> full variability of the task?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area or industry, leveraged to provide insights and guide data
  interpretation. For benchmarks, a domain expert is someone who knows about the SUT's
  task (e.g., ethicists for an ethics benchmark, a speaker of a low-resource language for
  a translation benchmark). A person without specialized knowledge in the benchmarked
  domain is not a domain expert.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`experts_involved`** — The documents state that domain experts (people with
   specialized knowledge of the SUT task, not generic crowd workers) took part in
   constructing the benchmark.
2. **`role_in_construction`** — Their involvement is in *benchmark construction* — e.g.,
   designing prompts, selecting or sourcing inputs, defining categories — and is
   described concretely enough to be checkable.
3. **`variability_goal`** — Their participation is tied to capturing the real-world
   distribution / variability of the task (e.g., ensuring diverse, representative, or
   edge-case inputs), not only to checking answer correctness.

**Strong positive signals:** named expert roles or qualifications relevant to the task; a
described process where experts contributed or curated inputs to broaden coverage;
explicit statements that experts were engaged to represent the full range of real-world
conditions; acknowledgements crediting domain specialists for diversity of the data.

**Negative / disqualifying signals:** prompts sourced only from a single narrow source or
generic crowd workers; experts mentioned only for answer grading with no role in shaping
input variability; "experts consulted" with no detail on who or how; expert involvement
described only for a future expansion of the benchmark.
