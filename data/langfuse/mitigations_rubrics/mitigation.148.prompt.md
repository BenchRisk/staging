# Mitigation 148 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #148, which mitigates Failure Mode #20.
Source: data/mitigations/148.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 148
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~8.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a model's performance
  in generating responses in French, but the prompts used are initially translated from
  English using an automatic translation tool. These translations introduce subtle
  idiomatic errors, misinterpretations of context, and shifts in tone. As a result, the
  model is evaluated based on prompts that do not fully represent the original intent or
  phrasing in the source language. The benchmark user assumes the model performs well in
  French but encounters issues with unnatural or inaccurate language use when deployed in
  real-world French-speaking contexts, particularly in areas where language nuance is
  critical.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark avoid processing human languages in its inputs or outputs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the
  context, task, or question the system is expected to respond to and are central to
  evaluating SUT performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`no_human_language_io`** — The benchmark's inputs and outputs do not depend on
   processing any human (natural) language — the task is satisfied only when prompts and
   expected outputs are language-agnostic rather than written in, or translated between,
   natural languages.
2. **`no_translated_prompts`** — Specifically, the documentation makes clear there are no
   prompts produced by translating from one human language into another (the failure
   mode's mechanism), because the benchmark does not process human language at all.

**Strong positive signals:** explicit statement that inputs/outputs are non-textual or
formally specified (numeric, symbolic, executable) and not derived from any human
language; no translation step anywhere in prompt construction; grading independent of
natural-language interpretation.

**Negative / disqualifying signals:** prompts authored in one human language and rendered
into another (machine- or human-translated); evaluation of natural-language generation,
translation, or comprehension; any input or output whose correctness depends on idiom,
tone, or phrasing in a human language; language coverage claimed only for a future
release.
