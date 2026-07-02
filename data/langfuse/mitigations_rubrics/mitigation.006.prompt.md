# Mitigation 006 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #6, which mitigates Failure Mode #4.
Source: data/mitigations/6.mdx and data/modes/4.mdx.
-->

## The mitigation under review

- **Mitigation number:** 6
- **Mitigates failure mode:** #4 — *"Prompts are collected from publicly available
  sources that are also likely to be in the datasets of SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~33.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses Reddit posts,
  StackOverflow questions, and Quora queries to construct prompts. Since these sources are
  commonly included in pretraining corpora, models like GPT or Claude that have seen these
  prompts during training score significantly higher than models trained on different data
  distributions, leading to misleadingly inflated performance. The benchmark user never
  considers using a SUT not pre-trained with these sources as a result.

**Criterion question (answer this for the benchmark under review):**
> Do you search the web for data included in your prompt set to find undisclosed
> collection from publicly available sources?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Canary Data:** Specially crafted benchmark data used to detect developer or evaluation
  practices likely to compromise the reliability of a benchmark. It is often planted
  deliberately to act as a warning signal (like a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`web_search_performed`** — The documents report that the developers searched the web
   (or otherwise queried public sources/search engines) for the contents of their prompt
   set to detect prompts that originated from publicly available material.
2. **`undisclosed_collection_checked`** — The purpose of the search is to surface
   undisclosed collection from public sources (e.g., contamination/leakage of prompts that
   may also be in SUT training data), and the documents report what was checked or found.

**Strong positive signals:** a described contamination check that web-searched prompt text
to find public matches; a reported leakage/overlap analysis against public corpora or
search-engine results; a statement of how many prompts matched public sources and how they
were handled; use of n-gram/substring search against the open web.

**Negative / disqualifying signals:** no web search or contamination check described; only
a claim that data is original without any verification; provenance trusted without
auditing; the check described only as planned for a future release.
