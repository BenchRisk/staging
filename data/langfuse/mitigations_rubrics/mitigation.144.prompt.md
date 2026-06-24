# Mitigation 144 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #144, which mitigates Failure Mode #14.
Source: data/mitigations/144.mdx and data/modes/14.mdx.
-->

## The mitigation under review

- **Mitigation number:** 144
- **Mitigates failure mode:** #14 — *"Benchmark does not capture the distribution or
  variability of the task in the real world"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating summarization
  quality uses a fixed set of short, well-structured news articles from a single outlet.
  All inputs are grammatically clean, follow similar structures, and focus on
  non-technical content. The benchmark scores suggest high summarization quality.
  However, when the model is deployed to summarize real-world documents — such as messy
  meeting transcripts, scientific papers, or user-generated content with inconsistent
  formatting — it fails to produce coherent or accurate summaries. The benchmark user,
  trusting the strong results, integrates the model into a productivity suite, leading to
  summaries that are frequently misleading, incomplete, or incoherent in actual usage.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from SUTs deployed to real users under realistic laboratory
> conditions (i.e., the user is directed to do a real task)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.
- **System Under Test (SUT) Task:** The specific activity or objective the SUT is
  expected to perform in the real world; a well-defined SUT task gives the benchmark the
  capacity to measure and report properties related to that task.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`from_real_user_interactions`** — Prompts are sourced from real users interacting
   with deployed SUTs, rather than only being authored synthetically by the benchmark
   team.
2. **`realistic_real_task`** — Those interactions occurred under realistic laboratory
   conditions, with users directed to perform an actual task — so the prompts reflect the
   real-world distribution and variability of the SUT task.

**Strong positive signals:** a described collection of prompts from real-user sessions
with a deployed system; a study or logging setup where participants performed genuine
tasks; provenance tying prompts to in-the-wild or lab-realistic usage; a stated effort
to capture natural variability from actual users.

**Negative / disqualifying signals:** prompts entirely synthetic or author-written with
no real-user origin; "real-world" claimed without a described collection method; prompts
from artificial templates only; user-sourced data promised for a future version; users
in the collection not actually doing a real task (e.g., contrived or scripted inputs).
