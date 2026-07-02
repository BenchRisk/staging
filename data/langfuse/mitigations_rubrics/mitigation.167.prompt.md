# Mitigation 167 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #167, which mitigates Failure Mode #55.
Source: data/mitigations/167.mdx and data/modes/55.mdx.
-->

## The mitigation under review

- **Mitigation number:** 167
- **Mitigates failure mode:** #55 — *"A SUT developer has disparate access to information
  about the benchmark **after** its release (i.e., information not provided to other SUT
  developers)"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~8.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The creators of a challenging reasoning
  benchmark privately share detailed information about the specific types of logical
  fallacies and linguistic ambiguities that the benchmark questions are designed to test
  with the developers of "CognitoMind" weeks after the official public release. Other SUT
  developers are only provided with the high-level task description at the time of launch.
  This privileged information allows the CognitoMind team to specifically tailor their
  model's architecture and training data to excel on these known weaknesses of other
  models. As a result, CognitoMind achieves a significantly higher score on the benchmark,
  not due to superior general reasoning capabilities, but because they had an unfair
  advantage in understanding the benchmark's intricacies. A benchmark user, unaware of
  this information asymmetry, might mistakenly conclude that CognitoMind is the most
  advanced reasoning engine available and choose it for critical applications, only to
  find its performance on real-world reasoning tasks is underwhelming compared to other
  models.

**Criterion question (answer this for the benchmark under review):**
> Do you publish the benchmark at an organization that does not develop SUTs (i.e., is it
> a third-party benchmark)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, consistency, reproducibility, accountability, and independence, so that
  benchmarks remain trustworthy.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`publishing_org_identified`** — The documents identify the organization that
   publishes/maintains the benchmark.
2. **`org_does_not_build_suts`** — That organization does not itself develop SUTs that are
   (or could be) evaluated by the benchmark — i.e., it is a genuinely third-party
   benchmark, removing the structural opportunity to favor an in-house SUT post-release.

**Strong positive signals:** a clearly named independent/third-party publisher (academic
lab, nonprofit, standards body) with no SUT product line; an explicit statement of
independence from model vendors; governance describing the benchmark as vendor-neutral.

**Negative / disqualifying signals:** the benchmark is published by an organization that
also ships evaluated SUTs (or its commercial affiliates); publisher identity is unstated
so independence cannot be established; independence claimed only aspirationally for the
future while the current publisher is a SUT developer.
