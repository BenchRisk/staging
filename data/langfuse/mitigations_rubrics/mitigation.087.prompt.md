# Mitigation 087 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #87, which mitigates Failure Mode #10.
Source: data/mitigations/87.mdx and data/modes/10.mdx.
-->

## The mitigation under review

- **Mitigation number:** 87
- **Mitigates failure mode:** #10 — *"Prompt perturbation bulking (increasing the number
  of prompts by making small changes to root prompts)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~45.83%
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
> Do you source prompts from multiple populations with distinct demographic attributes of
> the prompt writers?

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

1. **`multiple_populations`** — Prompts are sourced from more than one population of prompt
   writers rather than from a single author, team, template, or perturbation of a few root
   prompts.
2. **`distinct_demographic_attributes`** — Those populations have distinct demographic
   attributes (e.g., differing cultural, professional, educational, or linguistic
   backgrounds) documented as the basis for the sourcing.

**Strong positive signals:** a described contributor pool spanning multiple demographic
groups; reported demographic attributes of the prompt writers; a sourcing process that
recruits authors from distinct populations to broaden semantic coverage beyond
perturbations of a few base prompts; documentation linking writer diversity to wider
coverage.

**Negative / disqualifying signals:** prompts written by a single author, homogeneous
team, or generated purely by perturbing a small root set; coverage claimed solely through
large perturbed counts; no information on who wrote the prompts or their demographics; a
diversity claim with no description of the populations; multi-population sourcing planned
only for a future release.
