# Mitigation 023 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #23, which mitigates Failure Mode #20.
Source: data/mitigations/23.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 23
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~37.5%
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
> Do you validate all machine-translated prompts using a highly qualified speaker fluent
> in both source and target languages?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the
  context, task, or question the system is expected to respond to and are central to
  evaluating SUT performance.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide interpretation. For a
  low-resource language translation benchmark, a domain expert includes a fluent speaker
  of the language in question.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`human_validation`** — Machine-translated prompts are validated by a human speaker
   who is highly qualified and fluent in **both** the source and the target languages
   (not relying on the automatic translation alone).
2. **`all_prompts_covered`** — The validation covers **all** machine-translated prompts
   used by the published benchmark, not just a spot-checked subset.

**Strong positive signals:** a stated human-validation or review step for every
translated prompt; named qualifications/fluency of the reviewers in both languages; a
correction/adjudication process for translation errors; documentation that 100% of
translated prompts were reviewed by bilingual speakers.

**Negative / disqualifying signals:** prompts are machine-translated with no human
review; only a sample or subset is checked; reviewers' bilingual fluency is unstated;
validation described as planned/future work; translation quality assumed from the tool
without any speaker verification.
