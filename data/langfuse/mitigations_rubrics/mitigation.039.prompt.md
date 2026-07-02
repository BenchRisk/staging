# Mitigation 039 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #39, which mitigates Failure Mode #41.
Source: data/mitigations/39.mdx and data/modes/41.mdx.
-->

## The mitigation under review

- **Mitigation number:** 39
- **Mitigates failure mode:** #41 — *"SUT developer tunes safety program to benchmark
  sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark releases a subset of its
  prompts for transparency and community analysis. A system developer then uses this
  released set during training by sampling its prompts directly. As a result, the
  developer's system performs exceptionally well on the benchmark due to closely aligned
  fine-tuning. However, the model lacks true generalization and performs poorly on tasks
  that deviate even slightly from the benchmark format. The benchmark user interprets the
  high score as evidence of broad competence and deploys the system in a new domain, only
  to discover critical failures when the prompts fall outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you have signed agreements with SUT developers that prohibit tuning systems using the
> provided sample set?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs — covering
  transparency, consistency, reproducibility, accountability, and update mechanisms.
  Prohibiting tuning on the sample set is one such integrity requirement an agreement can
  enforce.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`agreement_exists`** — There is a binding/signed agreement (e.g., a submission
   contract, terms of participation, or data-use agreement) governing SUT developers who
   are evaluated.
2. **`prohibits_tuning_on_sample_set`** — That agreement explicitly forbids using the
   provided sample set to train, fine-tune, or otherwise tune the submitted system.

**Strong positive signals:** a described signed submission/participation agreement; an
explicit clause barring training or tuning on the released sample prompts; a data-use
license requiring evaluation-only use and signed attestation; a stated enforcement or
attestation process tied to submission.

**Negative / disqualifying signals:** only an honor-system request or "please don't train
on this" with no signed agreement; a general license with no anti-tuning clause; reliance
on community good faith; agreements mentioned as planned but not in force for current
submissions; no governance of how the sample set may be used at all.
