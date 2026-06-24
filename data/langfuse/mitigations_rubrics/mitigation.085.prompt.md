# Mitigation 085 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #85, which mitigates Failure Mode #10.
Source: data/mitigations/85.mdx and data/modes/10.mdx.
-->

## The mitigation under review

- **Mitigation number:** 85
- **Mitigates failure mode:** #10 — *"Prompt perturbation bulking (increasing the number
  of prompts by making small changes to root prompts)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~40% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark aimed at evaluating factual
  accuracy in historical QA uses 100 base prompts and generates 5,000 total prompts by
  slightly altering dates, names, or phrasing (e.g., changing "When did the Berlin Wall
  fall?" to "Can you tell me the year the Berlin Wall was taken down?"). While the
  quantity of prompts appears large, the semantic diversity is minimal and fails to cover
  the broader landscape of historical questions. A model optimized on this benchmark
  appears highly performant, but when users ask genuinely diverse or nuanced historical
  questions, it frequently hallucinates or misinterprets. The benchmark user integrates
  the model into an educational tool, leading to the dissemination of confidently stated
  misinformation.

**Criterion question (answer this for the benchmark under review):**
> Do you analyze prompt length and embedding space distribution visually to understand
> prompt variability?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the SUT task, ensuring sufficient
  variability and representation. It asks, "will the relying user believe the benchmark
  covers something impacting their LLM decisions that is not covered?"
- **Prompt Perturbation Bulking:** A technique to increase the number of prompts used in
  a benchmark by making modifications to root prompts, helping evaluate how slight changes
  in wording, structure, or context affect SUT outputs. See also "Adversarial Prompt
  Bulking."
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
projection plots showing prompt spread; a visual demonstration that perturbed prompts do
not collapse into a few tight clusters around the root prompts; figures characterizing
how varied the prompts truly are beyond raw count.

**Negative / disqualifying signals:** only a total prompt count with no distribution
analysis; large prompt counts produced by perturbation presented as coverage with no
embedding/length check; a claim of diversity unsupported by any visualization; the visual
analysis described only as planned rather than present in the published benchmark.
