# Mitigation 077 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #77, which mitigates Failure Mode #42.
Source: data/mitigations/77.mdx and data/modes/42.mdx.
-->

## The mitigation under review

- **Mitigation number:** 77
- **Mitigates failure mode:** #42 — *"SUT developer trains SUT against sample set"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~70% reduction in failure-mode likelihood; ~0%
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
> Do you have signed agreements with SUT developers that explicitly prohibit training
> with the sample set?

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
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise benchmark reliability. It is often planted
  deliberately to act as a warning signal (like a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`signed_agreement`** — There exists an executed, signed agreement (contract, terms
   of access, data-use agreement, or equivalent legally binding instrument) between the
   benchmark operators and SUT developers, not merely an informal request or honor-system
   note.
2. **`prohibits_training`** — That agreement explicitly forbids using the sample set (or
   prompts derived from / closely aligned with it) for training, fine-tuning, or other
   model adaptation.
3. **`covers_sut_developers`** — The agreement binds the SUT developers who obtain access
   to the sample set, so any party that can score on the benchmark is contractually
   covered.

**Strong positive signals:** a referenced data-use or licensing agreement that submitters
must sign before access; explicit no-train / no-fine-tune clauses naming the sample set;
a described gating or registration process that records signatories; mention of
enforcement, audit, or canary mechanisms tied to the agreement.

**Negative / disqualifying signals:** the sample set is openly downloadable with no
agreement at all; only a polite "please do not train on this" note with no signature or
binding force; an agreement that governs redistribution but is silent on training; the
prohibition exists only as a future/planned policy for the published benchmark.
