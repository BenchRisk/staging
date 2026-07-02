# Mitigation 140 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #140, which mitigates Failure Mode #4.
Source: data/mitigations/140.mdx and data/modes/4.mdx.
-->

## The mitigation under review

- **Mitigation number:** 140
- **Mitigates failure mode:** #4 — *"Prompts are collected from publicly available
  sources that are also likely to be in the datasets of SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses Reddit posts,
  StackOverflow questions, and Quora queries to construct prompts. Since these sources
  are commonly included in pretraining corpora, models like GPT or Claude that have seen
  these prompts during training score significantly higher than models trained on
  different data distributions, leading to misleadingly inflated performance. The
  benchmark user never considers using a SUT not pre-trained with these sources as a
  result.

**Criterion question (answer this for the benchmark under review):**
> Do you produce entirely new prompts with the aid of humans?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to generate
  variations, expansions, or perturbations in data-driven processes.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`newly_authored`** — The prompts are entirely new — purpose-written for the
   benchmark rather than collected, scraped, or reused from publicly available sources
   likely present in SUT training data.
2. **`human_authored`** — Human authors produced (or substantively aided in producing)
   the prompts, as opposed to harvesting them from existing public corpora.

**Strong positive signals:** an explicit statement that prompts were written from scratch
by the authors / contributors; a described human authoring or expert-writing process;
prompts created to be novel and not present in public datasets; provenance making clear
no scraped public-source content was used.

**Negative / disqualifying signals:** prompts drawn from web sources, public Q&A sites,
existing datasets, or scraped corpora; reuse of pre-existing benchmark items; no account
of how prompts were created; prompts auto-generated solely from public material without
human authorship; "new prompts" promised for a future release while the current one
reuses public data.
