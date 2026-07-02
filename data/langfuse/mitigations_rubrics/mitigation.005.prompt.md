# Mitigation 005 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #5, which mitigates Failure Mode #4.
Source: data/mitigations/5.mdx and data/modes/4.mdx.
-->

## The mitigation under review

- **Mitigation number:** 5
- **Mitigates failure mode:** #4 — *"Prompts are collected from publicly available
  sources that are also likely to be in the datasets of SUT developers"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~54.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark uses Reddit posts,
  StackOverflow questions, and Quora queries to construct prompts. Since these sources are
  commonly included in pretraining corpora, models like GPT or Claude that have seen these
  prompts during training score significantly higher than models trained on different data
  distributions, leading to misleadingly inflated performance. The benchmark user never
  considers using a SUT not pre-trained with these sources as a result.

**Criterion question (answer this for the benchmark under review):**
> Do you avoid sourcing data from publicly available information when constructing your
> benchmark?

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

1. **`avoids_public_sources`** — The documents indicate the benchmark's prompts/data are
   not drawn from publicly available information (e.g., they are newly authored, privately
   held, or otherwise not scraped from the open web), so they are unlikely to be in SUT
   developers' training corpora.
2. **`provenance_described`** — The documents describe the data's origin clearly enough to
   support the claim that public sources were avoided, rather than leaving the provenance
   unstated.

**Strong positive signals:** an explicit statement that prompts were freshly written for
the benchmark and not taken from the web; a data-provenance section affirming no public
corpora (Reddit, StackOverflow, Wikipedia, Common Crawl, etc.) were used; held-out/private
data kept off the public internet; use of canary strings to detect any later leakage.

**Negative / disqualifying signals:** prompts sourced from public websites, forums, or
existing public datasets; provenance unstated so public sourcing cannot be ruled out; only
a future plan to use private data; reliance on well-known public benchmarks as the prompt
source.
