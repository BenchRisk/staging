# Mitigation 084 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #84, which mitigates Failure Mode #9.
Source: data/mitigations/84.mdx and data/modes/9.mdx.
-->

## The mitigation under review

- **Mitigation number:** 84
- **Mitigates failure mode:** #9 — *"Adversarial prompt bulking (increasing the number of
  prompts by multiplying them by the number of tactics)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate model
  robustness against jailbreaks creates 100 base adversarial prompts and then applies 10
  paraphrasing or obfuscation tactics to each, resulting in 1,000 prompts. While this
  gives the appearance of broad coverage, the underlying semantic space is still
  narrow—centered on just 100 scenarios. A model that learns to defend against these
  specific base prompts or common surface patterns scores highly, even though it remains
  vulnerable to novel or semantically different jailbreaks. A benchmark user assumes the
  model is robust and deploys it in a moderation tool, which is quickly circumvented by
  attacks not represented in the bloated prompt set.

**Criterion question (answer this for the benchmark under review):**
> Do you analyze prompt length and embedding space distribution visually to understand
> prompt variability?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the SUT task, ensuring sufficient
  variability and representation. It asks, "will the relying user believe the benchmark
  covers something impacting their LLM decisions that is not covered?"
- **Adversarial Prompt Bulking:** A technique of increasing the number of prompts by
  multiplying them with various tactics (e.g., jailbreak templates) and root instances.
  See also "Prompt Perturbation Bulking."
- **Tactics:** A transformation applied to a prompt to produce an altered prompt,
  typically for the purpose of jailbreaking a SUT.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to generate
  variations, expansions, or perturbations in data-driven processes.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`length_analysis`** — The documents report an analysis of prompt length across the
   benchmark's prompts.
2. **`embedding_distribution_analysis`** — They report an analysis of the prompts'
   embedding-space distribution.
3. **`visual_method`** — That analysis is done visually (e.g., length histograms,
   embedding scatter plots, UMAP/t-SNE projections) to surface the variability of the
   prompts.

**Strong positive signals:** length-distribution histograms; embedding-space scatter or
projection plots showing prompt spread; a visual demonstration that bulked prompts do not
collapse into a few tight clusters; figures characterizing how varied the prompts truly
are beyond raw count.

**Negative / disqualifying signals:** only a total prompt count with no distribution
analysis; bulking by tactics presented as evidence of coverage with no embedding/length
check; a claim of diversity unsupported by any visualization; the visual analysis
described only as planned rather than present in the published benchmark.
