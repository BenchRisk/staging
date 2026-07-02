# Mitigation 078 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #78, which mitigates Failure Mode #42.
Source: data/mitigations/78.mdx and data/modes/42.mdx.
-->

## The mitigation under review

- **Mitigation number:** 78
- **Mitigates failure mode:** #42 — *"SUT developer trains SUT against sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark releases a subset of its
  prompts for transparency and community analysis. A system developer then uses this
  released set during training by sampling prompts with similar structure, linguistic
  style, and distribution. As a result, the developer's system performs exceptionally
  well on the benchmark due to fine-tuning on closely aligned prompts. However, the model
  lacks true generalization and performs poorly on tasks that deviate even slightly from
  the benchmark format. The benchmark user interprets the high score as evidence of broad
  competence and deploys the system in a new domain, only to discover critical failures
  when the prompts fall outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Does your license prohibit tuning to the sample set?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs — maintaining
  trustworthiness through transparency, consistency, reproducibility, accountability,
  and update mechanisms. SUT developers can violate them through data snooping or
  benchmark overfitting, among others.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`has_license`** — The benchmark or its sample set is released under a stated license
   or terms of use that is identifiable in the documents.
2. **`prohibits_tuning`** — That license contains a clause that explicitly prohibits
   training, tuning, fine-tuning, or otherwise adapting a model on the sample set (as
   distinct from merely restricting redistribution or commercial use).

**Strong positive signals:** a license file or terms section with an explicit "no
training / no fine-tuning on this data" restriction; license text that names the sample
set and bars its use as training data; a custom benchmark license that conditions use on
not optimizing models against the prompts.

**Negative / disqualifying signals:** a permissive license (e.g., MIT, CC-BY, Apache)
with no anti-tuning clause; no license stated at all; a license that restricts
redistribution but is silent on training/tuning; the anti-tuning clause described only as
planned for a future release rather than applying to the currently published data.
