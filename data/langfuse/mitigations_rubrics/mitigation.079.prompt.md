# Mitigation 079 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #79, which mitigates Failure Mode #15.
Source: data/mitigations/79.mdx and data/modes/15.mdx.
-->

## The mitigation under review

- **Mitigation number:** 79
- **Mitigates failure mode:** #15 — *"Prompts have known properties allowing for
  achieving an unrealistic (i.e., non-generalizing) performance. For example, prompts are
  of particular and known lengths."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~53.33% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark testing whether code
  generation models detect instructions for generating malware uses prompts that are
  consistently of a particular length, averaging 10 lines of code for malware, and 8
  lines of code for non-malicious code. The model performs well on this benchmark, as it
  has been explicitly optimized to have a higher prior belief of malware for 10 lines of
  code vs 8 lines of code. However, the difference in length is solely a statistical
  artifact of the evaluation and not representative of the actual performance. A benchmark
  user, assuming the model's high score represents its ability to prevent malware
  generation, deploys it in a real-world software development environment. The model then
  generates more malware than would otherwise have been generated.

**Criterion question (answer this for the benchmark under review):**
> Do you analyze prompt properties—such as length and embedding space distribution—using
> visual or statistical methods?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language. Prompts define the context, task, or question the
  system is expected to respond to and are central to evaluating SUT performance; their
  design directly influences the reliability and interpretability of benchmark results.
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances
  (e.g., resume screening that disproportionately rejects candidates from a poor state).
  Assessing such distributional effects is contingent on having data annotated to support
  distributional evaluation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`analyzes_prompt_properties`** — The documents describe an actual analysis of prompt
   properties (e.g., length, token count, embedding-space distribution, clustering) of
   the benchmark's prompts, not merely a claim that prompts are diverse.
2. **`visual_or_statistical_method`** — That analysis uses a visual method (e.g.,
   embedding scatter/UMAP/t-SNE plots, length histograms) and/or statistical methods
   (e.g., distributional summaries, variance/spread measures) rather than an unsupported
   assertion.

**Strong positive signals:** reported prompt-length distributions or histograms;
embedding-space visualizations showing coverage/spread; statistics on lexical or semantic
diversity; explicit checks that no exploitable property (like a fixed length) correlates
with the label.

**Negative / disqualifying signals:** prompts presented with no characterization of their
distribution; only a raw prompt count with no property analysis; a vague claim of
"diverse prompts" unsupported by any visual or statistical evidence; such analysis
promised for a future version but absent from the published benchmark.
