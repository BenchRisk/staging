# Mitigation 027 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #27, which mitigates Failure Mode #23.
Source: data/mitigations/27.mdx and data/modes/23.mdx.
-->

## The mitigation under review

- **Mitigation number:** 27
- **Mitigates failure mode:** #23 — *"SUT developer trains against sample prompt set."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A company preparing to release a new
  model with new capabilities also produces a new benchmark to evaluate those
  capabilities. The organization maintains a separation between the benchmark team and
  the SUT development team, but the benchmark team provides a sample test early in the
  development process. The SUT team then uses this released set during training by
  sampling prompts with similar structure, linguistic style, and distribution. As a
  result, the developer's system performs exceptionally well on the benchmark due to
  fine-tuning on closely aligned prompts. However, the model lacks true generalization
  and performs poorly on tasks that deviate even slightly from the benchmark format. The
  benchmark user interprets the high score as evidence of broad competence and deploys
  the system in a new domain, only to discover critical failures when the prompts fall
  outside the trained distribution.

**Criterion question (answer this for the benchmark under review):**
> Do you provide sample prompts under a license that explicitly prohibits their use in
> model training?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark, often planted
  deliberately to act as a warning signal (like a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`license_present`** — Any sample prompts provided come with a stated license or
   terms of use governing how they may be used.
2. **`training_prohibited`** — That license **explicitly** prohibits use of the sample
   prompts in model training (not merely a generic license silent on training).

**Strong positive signals:** a license or usage clause stating sample prompts may not be
used for training/fine-tuning; an explicit "evaluation only / no training" term attached
to released samples; a data-use agreement forbidding inclusion in training corpora;
canary strings paired with a no-training prohibition.

**Negative / disqualifying signals:** sample prompts released with no license, or under a
permissive license that does not address training; terms that allow any reuse; the
no-training restriction stated only as an informal request rather than a license term;
the prohibition planned for a future dataset version but absent now.
