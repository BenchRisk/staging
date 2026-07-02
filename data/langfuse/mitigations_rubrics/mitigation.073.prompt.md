# Mitigation 073 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #73, which mitigates Failure Mode #25.
Source: data/mitigations/73.mdx and data/modes/25.mdx.
-->

## The mitigation under review

- **Mitigation number:** 73
- **Mitigates failure mode:** #25 — *"SUT developers place evaluator or other test ground
  truth within system chain"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** During a jailbreak benchmark evaluation, a
  SUT is configured with access to the benchmark's LLM-as-a-judge, which determines
  whether the outputs of the SUT have been jailbroken or not. With access to the
  LLM-as-a-judge, the LLM scores perfectly on the benchmark. However, the LLM-as-a-judge
  is not perfectly accurate, so it obscures the true failures of the SUT. A SUT deployer
  adopts the imperfect LLM thinking it is actually perfect and will not be jailbroken.

**Criterion question (answer this for the benchmark under review):**
> Do you employ a backup evaluator with human validation of sampled outputs to ensure
> evaluation reliability?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators when assessing the same outputs. High interrater reliability
  indicates well-defined, consistently applied criteria; it is commonly quantified with
  measures such as Cohen's kappa.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`backup_evaluator`** — The benchmark employs a backup (secondary) evaluator that
   serves as an independent check on the primary evaluator's judgments.
2. **`human_validation_of_sampled_outputs`** — Humans validate a sample of the evaluated
   outputs to confirm evaluation reliability, rather than trusting an automated evaluator
   alone.

**Strong positive signals:** a described secondary/backup evaluator distinct from the
primary one; reported human review of a sample of outputs with agreement statistics
(e.g., interrater reliability); a documented process for catching and correcting
evaluator errors; sampling methodology for the human-validated subset.

**Negative / disqualifying signals:** a single automated evaluator (e.g., one
LLM-as-a-judge) with no backup; no human validation of any outputs; human review
mentioned without sampling or agreement reporting; backup evaluation or human validation
described only as a future plan while published scores rely on a single evaluator.
