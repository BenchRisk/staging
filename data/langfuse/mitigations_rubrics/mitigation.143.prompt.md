# Mitigation 143 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #143, which mitigates Failure Mode #14.
Source: data/mitigations/143.mdx and data/modes/14.mdx.
-->

## The mitigation under review

- **Mitigation number:** 143
- **Mitigates failure mode:** #14 — *"Benchmark does not capture the distribution or
  variability of the task in the real world"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~29.17%
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
> Do you source additional prompts through peer review and/or submissions from the
> broader community?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task — the kind of
  contributor peer review and community submission can draw on for broader coverage.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`external_sourcing`** — Additional prompts are sourced from outside the core author
   team, through peer review and/or open submissions from the broader community.
2. **`incorporated_in_release`** — Those externally sourced prompts are actually
   incorporated into the published benchmark (not merely solicited or planned).

**Strong positive signals:** a described peer-review or community-submission process for
contributing prompts; an open call, submission portal, or contributor list; prompts
credited to community contributors or external reviewers; a process showing externally
sourced prompts were vetted and added to the released set.

**Negative / disqualifying signals:** all prompts authored by the core team with no
external contribution channel; a submission mechanism announced but with no incorporated
contributions in the current release; community sourcing described only as future work;
external review mentioned but with no prompts actually added from it.
