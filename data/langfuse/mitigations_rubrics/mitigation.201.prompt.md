# Mitigation 201 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #201, which mitigates Failure Mode #15.
Source: data/mitigations/201.mdx and data/modes/15.mdx.
-->

## The mitigation under review

- **Mitigation number:** 201
- **Mitigates failure mode:** #15 — *"Prompts have known properties allowing for
  achieving an unrealistic (i.e., non-generalizing) performance. For example, prompts are
  of particular and known lengths."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark testing whether code
  generation models detect instructions for generating malware uses prompts that are
  consistently of a particular length, averaging 10 lines of code for malware and 8 lines
  for non-malicious code. The model performs well, as it has been explicitly optimized to
  hold a higher prior belief of malware for 10 lines vs. 8 lines. However, the difference
  in length is solely a statistical artifact of the evaluation and not representative of
  actual performance. A benchmark user, assuming the model's high score represents its
  ability to prevent malware generation, deploys it in a real-world software development
  environment, and the model then generates more malware than would otherwise have been
  generated.

**Criterion question (answer this for the benchmark under review):**
> Are the prompt outputs multi-step, inherently high dimensional, or possess some other
> property making the benchmarked task difficult to game on the basis of a
> non-generalizing input feature (e.g., prompt lengths)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language, defining the context, task, or question the system
  is expected to respond to.
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Subtasks isolate specific capabilities or dimensions; multi-step tasks composed
  of subtasks are harder to game on a single non-generalizing feature.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`gaming_resistant_property`** — The documents describe a property of the benchmark's
   prompts/outputs — multi-step structure, inherent high dimensionality, or an equivalent
   characteristic — that makes the task hard to solve via a non-generalizing input
   feature such as prompt length.
2. **`property_substantiated`** — That property is substantiated for the currently
   published benchmark (e.g., shown in the task design, or via analysis that no simple
   surface feature like length predicts the label), not merely asserted.

**Strong positive signals:** an explicit task design that is multi-step or
high-dimensional; analysis showing surface features (length, formatting) do not correlate
with the answer or are balanced across classes; deliberate controls to remove
length/format shortcuts; reported baselines confirming trivial features cannot achieve
high performance.

**Negative / disqualifying signals:** single-step prompts with no defense against surface
shortcuts; class labels confounded with length or other simple features; the claim of
gaming-resistance asserted without analysis; such controls described only for a future
release while the published prompts retain exploitable regularities.
