# Mitigation 011 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #11, which mitigates Failure Mode #8.
Source: data/mitigations/11.mdx and data/modes/8.mdx.
-->

## The mitigation under review

- **Mitigation number:** 11
- **Mitigates failure mode:** #8 — *"Prompt writers produce prompts with inadequate
  variability within the valid input space (e.g., a single prompt writer writes all the
  prompts)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to test reasoning over
  legal contracts uses 500 prompts, all written by a single legal expert. Although the
  expert is highly knowledgeable, their prompts all follow similar structures, phrasings,
  and assumptions. As a result, the SUT learns to pick up on these patterns and performs
  well. However, when deployed to assist general counsel teams, the model fails to handle
  real-world contract analysis tasks that involve diverse linguistic styles, jurisdictions,
  and edge cases. The benchmark user trusts the high benchmark score and integrates the
  model into a high-stakes legal review process, leading to costly misinterpretations.

**Criterion question (answer this for the benchmark under review):**
> Do you analyze the prompt length and/or the embedding space of prompts visually?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the context,
  task, or question the system is expected to respond to and are central to evaluating SUT
  performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`variability_analysis_performed`** — The documents report an analysis of prompt
   variability, examining prompt length and/or the embedding space of the prompts to
   characterize how diverse the prompt set is across the valid input space.
2. **`visual_presentation`** — The analysis is presented visually (e.g., a length
   distribution histogram or an embedding scatter/cluster plot), consistent with the
   criterion's call to analyze these "visually."

**Strong positive signals:** a figure showing the distribution of prompt lengths; a 2-D
embedding projection (e.g., UMAP/t-SNE/PCA) of the prompts with a description of coverage;
a stated diversity analysis used to confirm prompts span the input space; reported metrics
on embedding spread or clustering.

**Negative / disqualifying signals:** no analysis of prompt diversity, length, or
embeddings; diversity merely asserted without inspection; analysis described but with no
visualization; the analysis described only as planned future work.
