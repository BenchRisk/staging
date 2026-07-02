# Mitigation 017 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #17, which mitigates Failure Mode #14.
Source: data/mitigations/17.mdx and data/modes/14.mdx.
-->

## The mitigation under review

- **Mitigation number:** 17
- **Mitigates failure mode:** #14 — *"Benchmark does not capture the distribution or
  variability of the task in the real world"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~29.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating summarization
  quality uses a fixed set of short, well-structured news articles from a single outlet.
  All inputs are grammatically clean, follow similar structures, and focus on non-technical
  content. The benchmark scores suggest high summarization quality. However, when the model
  is deployed to summarize real-world documents — such as messy meeting transcripts,
  scientific papers, or user-generated content with inconsistent formatting — it fails to
  produce coherent or accurate summaries. The benchmark user, trusting the strong results,
  integrates the model into a productivity suite, leading to summaries that are frequently
  misleading, incomplete, or incoherent in actual usage scenarios.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from SUTs deployed in a real world setting for the task under
> evaluation within the benchmark (i.e., a non-experimental setting)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the context,
  task, or question the system is expected to respond to and are central to evaluating SUT
  performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`real_world_sourced_prompts`** — The documents indicate the benchmark's prompts are
   sourced from SUTs deployed in a real-world (non-experimental) setting for the task under
   evaluation, rather than being authored only in a lab/experimental context.
2. **`task_matched_deployment`** — The deployment the prompts come from matches the task
   the benchmark evaluates, so the captured distribution reflects real-world variability of
   that task.

**Strong positive signals:** a statement that prompts were drawn from real production
traffic or live user interactions with a deployed system for the target task; described
provenance from a fielded/non-experimental deployment; evidence that the prompt
distribution reflects observed real-world usage rather than constructed scenarios.

**Negative / disqualifying signals:** prompts authored solely in an experimental or
synthetic setting; sourcing from a single narrow or artificial source unrepresentative of
real deployment; no description of where prompts came from; real-world sourcing described
only as planned future work.
