# Mitigation 121 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #121, which mitigates Failure Mode #51.
Source: data/mitigations/121.mdx and data/modes/51.mdx.
-->

## The mitigation under review

- **Mitigation number:** 121
- **Mitigates failure mode:** #51 — *"SUT developers are not bound to adhere to benchmark
  integrity requirements"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~8.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating the safety of
  language models prohibits the use of external knowledge during evaluation to ensure the
  model's responses are based solely on its training data. However, the developers of
  "GuardianAI," while submitting their model to the benchmark, secretly implement a
  retrieval mechanism that allows the model to access and incorporate real-time
  information from the internet during the evaluation process. This circumvents the
  benchmark's intended constraints and leads to inflated safety scores. A user, trusting
  the benchmark's results, selects GuardianAI believing it has robust internal safety
  mechanisms, only to discover in real-world use that it can still generate harmful
  content when disconnected from external resources or when faced with novel prompts not
  covered by its retrieval strategy.

**Criterion question (answer this for the benchmark under review):**
> Are SUT developers held legally and financially accountable for harms that might arise
> from violating benchmark release requirements (i.e., if training practices producing a
> benchmark score not representative of SUT performance in the real world)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for systems under test
  (SUTs), designed to maintain the trustworthiness of benchmarks. Examples of how SUT
  developers violate them include selective reporting, data snooping, cherry-picking
  metrics, modifying evaluation protocols, and benchmark overfitting.
- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`accountability_mechanism`** — There is a binding mechanism (e.g., a signed
   agreement, license terms, contract, or terms of participation) that exposes SUT
   developers to legal and/or financial accountability for violating the benchmark's
   release requirements.
2. **`tied_to_release_violations`** — That accountability is tied specifically to
   violations producing scores unrepresentative of real-world SUT performance (e.g.,
   training on the test set, breaching integrity requirements), not merely a generic
   disclaimer.

**Strong positive signals:** a binding submission agreement or license with enforcement
or penalty clauses; stated legal/financial consequences (liability, fines, forfeiture,
delisting with cause) for integrity violations; a contractual attestation developers must
sign before submission; reference to remedies for misrepresentation.

**Negative / disqualifying signals:** only voluntary or honor-system norms with no
consequence; a disclaimer that disclaims rather than imposes liability; rules without any
enforcement, penalty, or legal/financial mechanism; accountability mentioned only as a
future aspiration.
