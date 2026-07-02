# Mitigation 164 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #164, which mitigates Failure Mode #8.
Source: data/mitigations/164.mdx and data/modes/8.mdx.
-->

## The mitigation under review

- **Mitigation number:** 164
- **Mitigates failure mode:** #8 — *"Prompt writers produce prompts with inadequate
  variability within the valid input space (e.g., a single prompt writer writes all the
  prompts)"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~50.0%
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
> Do you involve domain experts in producing the prompts to ensure all known forms of
> variation are covered by the inputs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task (e.g., ethicists
  for an ethics benchmark, a speaker of a low-resource language for a translation
  benchmark). A person without specialized knowledge in the benchmarked domain is not a
  domain expert; formal training is not required where significant experience exists.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`domain_experts_involved`** — The documents state that domain experts (people with
   specialized knowledge of the SUT task) participated in producing the prompts.
2. **`multiple_or_diverse_authors`** — Prompt authorship is plural/diverse rather than
   funneled through a single writer, reducing idiosyncratic structure and phrasing.
3. **`variation_coverage_addressed`** — The documents describe deliberately covering the
   known forms of variation within the valid input space (e.g., styles, jurisdictions,
   subpopulations, edge cases), not merely a uniform set of prompts.

**Strong positive signals:** named expert contributors or annotator panels with relevant
expertise; a described process for sampling across linguistic styles, subgroups, or edge
cases; multiple independent authors with diversity controls or coverage analysis.

**Negative / disqualifying signals:** all prompts written by one person or one narrow
team; no mention of domain expertise in prompt creation; no attention to covering the
range of valid inputs; expert involvement asserted only for a future revision.
