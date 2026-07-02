# Mitigation 165 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #165, which mitigates Failure Mode #9.
Source: data/mitigations/165.mdx and data/modes/9.mdx.
-->

## The mitigation under review

- **Mitigation number:** 165
- **Mitigates failure mode:** #9 — *"Adversarial prompt bulking (increasing the number of
  prompts by multiplying them by the number of tactics)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~58.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate model
  robustness against jailbreaks creates 100 base adversarial prompts and then applies 10
  paraphrasing or obfuscation tactics to each, resulting in 1,000 prompts. While this
  gives the appearance of broad coverage, the underlying semantic space is still
  narrow—centered on just 100 scenarios. A model that learns to defend against these
  specific base prompts or common surface patterns scores highly, even though it remains
  vulnerable to novel or semantically different jailbreaks. A benchmark user assumes the
  model is robust and deploys it in a moderation tool, which is quickly circumvented by
  attacks not represented in the bloated prompt set.

**Criterion question (answer this for the benchmark under review):**
> Is the task defined in a way that does not examine adversarial performance, and are
> adversarial prompts excluded?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT)
  task, ensuring sufficient variability and representation. It asks, "will the relying
  user believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Adversarial Prompt Bulking:** The technique of increasing the number of prompts by
  multiplying them with various tactics (e.g., jailbreak templates) and root instances.
- **Tactics:** A transformation applied to a prompt to produce an altered prompt,
  typically for the purpose of jailbreaking a SUT.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling it to produce restricted, harmful, or unintended
  outputs. In benchmarking, jailbreaks test the robustness of safety measures.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`non_adversarial_task`** — The task definition is explicitly scoped so that it does
   *not* measure adversarial/jailbreak robustness (the benchmark's purpose is
   non-adversarial performance).
2. **`adversarial_prompts_excluded`** — Adversarial prompts — and tactic-multiplied
   bulking of them — are excluded from the prompt set, so coverage is not inflated by
   transformations of a few root scenarios.

**Strong positive signals:** an explicit statement that adversarial/robustness testing is
out of scope; a documented exclusion of jailbreak/tactic-derived prompts; a prompt-set
description showing distinct, non-adversarial scenarios rather than tactic-bulked
variants.

**Negative / disqualifying signals:** the benchmark measures jailbreak/adversarial
robustness via tactic-multiplied prompts; large prompt counts derived by applying tactics
to a small set of root prompts; no statement on whether adversarial prompts are included;
exclusion of adversarial prompts described only for a future version.
