# Mitigation 149 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #149, which mitigates Failure Mode #23.
Source: data/mitigations/149.mdx and data/modes/23.mdx.
-->

## The mitigation under review

- **Mitigation number:** 149
- **Mitigates failure mode:** #23 — *"SUT developer trains against sample prompt set"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~40.0% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A company preparing to release a new model
  with new capabilities also produces a new benchmark to evaluate those capabilities. The
  organization maintains a separation between the benchmark team and the SUT development
  team, but the benchmark team provides a sample test early in the development process.
  The SUT team then uses this released set during training by sampling prompts with
  similar structure, linguistic style, and distribution. As a result, the developer's
  system performs exceptionally well on the benchmark due to fine-tuning on closely
  aligned prompts. However, the model lacks true generalization and performs poorly on
  tasks that deviate even slightly from the benchmark format. The benchmark user
  interprets the high score as evidence of broad competence and deploys the system in a
  new domain, only to discover critical failures when the prompts fall outside the
  trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you require SUT developers to disclose their training practices when attempting to
> maximize their scores, including any training or engineering done to specifically
> target the sample set? And do you require them to disclaim results in such cases?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs — covering
  transparency, consistency, reproducibility, accountability, and independence. Examples
  of SUT-developer violations include data snooping and benchmark overfitting.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to
  generate variations, expansions, or perturbations in data-driven processes.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`disclosure_required`** — The benchmark requires SUT developers to disclose their
   training practices when maximizing scores, including any training or engineering done
   to specifically target the sample/test set.
2. **`disclaim_required`** — The benchmark requires developers to disclaim (flag/caveat)
   results in cases where such targeting occurred.
3. **`enforced_as_policy`** — These disclosure and disclaimer obligations are stated as a
   submission rule or policy of the published benchmark, not merely encouraged or
   described aspirationally.

**Strong positive signals:** a submission/leaderboard policy requiring contributors to
report training data and any sample-set-targeted tuning; a required attestation or
checkbox; an explicit rule that results tuned to the sample set must be marked/disclaimed
or are otherwise flagged on the leaderboard; documented consequences for nondisclosure.

**Negative / disqualifying signals:** no stated disclosure requirement; disclosure
described as optional or "recommended"; the policy mentions disclosure but not the
disclaimer requirement (or vice versa); the requirement applies only to a future version
while current results carry no such obligation.
