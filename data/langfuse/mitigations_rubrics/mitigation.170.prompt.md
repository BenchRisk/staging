# Mitigation 170 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #170, which mitigates Failure Mode #55.
Source: data/mitigations/170.mdx and data/modes/55.mdx.
-->

## The mitigation under review

- **Mitigation number:** 170
- **Mitigates failure mode:** #55 — *"A SUT developer has disparate access to information
  about the benchmark **after** its release (i.e., information not provided to other SUT
  developers)"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~12.5%
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
> Is your organization a SUT developer and do you maintain an information barrier protocol
> (e.g., Chinese wall) between benchmark authors/prompt writers and SUT developers within
> the same organization?

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

1. **`org_is_sut_developer`** — The documents establish that the publishing organization
   is itself a SUT developer (this is the situation the barrier addresses).
2. **`information_barrier_maintained`** — The documents describe an information barrier
   protocol (e.g., a Chinese wall) that separates benchmark authors/prompt writers from
   the organization's SUT developers, preventing non-public benchmark information from
   reaching the in-house model teams.

**Strong positive signals:** a documented Chinese-wall/information-barrier policy with
described controls (access restrictions, separated teams, audited boundaries); explicit
acknowledgment that the org builds SUTs and how the boundary is enforced.

**Negative / disqualifying signals:** the org develops SUTs but no barrier is described;
benchmark authors and model teams overlap with no separation; the barrier mentioned only
as a future plan; the question is inapplicable yet documents still imply shared access
without safeguards.
