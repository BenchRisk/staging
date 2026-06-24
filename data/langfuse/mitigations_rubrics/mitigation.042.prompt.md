# Mitigation 042 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #42, which mitigates Failure Mode #42.
Source: data/mitigations/42.mdx and data/modes/42.mdx.
-->

## The mitigation under review

- **Mitigation number:** 42
- **Mitigates failure mode:** #42 — *"SUT developer trains SUT against sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark releases a subset of its
  prompts for transparency and community analysis. A system developer then uses this
  released set during training by sampling prompts with similar structure, linguistic
  style, and distribution. As a result, the developer's system performs exceptionally well
  on the benchmark due to fine-tuning on closely aligned prompts. However, the model lacks
  true generalization and performs poorly on tasks that deviate even slightly from the
  benchmark format. The benchmark user interprets the high score as evidence of broad
  competence and deploys the system in a new domain, only to discover critical failures
  when the prompts fall outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you intentionally avoid providing a representative sample set (i.e., a dataset
> illustrative of the characteristics of the prompts included within the test set)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Distributional Association:** A property of prompt collections in which the items
  share characteristics representative of the broader test set. A released "representative
  sample set" is exactly such an illustrative dataset, and withholding it is what this
  mitigation asks about.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_representative_sample_released`** — The benchmark does not publish a sample set
   that is illustrative of the characteristics (structure, style, distribution) of the
   prompts in the test set.

**Strong positive signals:** an explicit statement that no representative or example
subset is released to avoid enabling tuning; only abstract/format documentation provided
without distribution-matching examples; a deliberate policy that any examples shown are
not drawn from or representative of the test distribution.

**Negative / disqualifying signals:** a published "sample," "dev," "example," or
"validation" set described as representative of the test prompts; released items matching
the test set's structure, style, and distribution; sample prompts shared for "community
analysis" or "transparency" that mirror the hidden set; a representative subset linked or
downloadable alongside the benchmark.
