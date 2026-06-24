# Mitigation 063 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #63, which mitigates Failure Mode #20.
Source: data/mitigations/63.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 63
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~40.0% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a model's performance
  in generating responses in French, but the prompts used are initially translated from
  English using an automatic translation tool. These translations introduce subtle
  idiomatic errors, misinterpretations of context, and shifts in tone. As a result, the
  model is evaluated based on prompts that do not fully represent the original intent or
  phrasing in the source language. The benchmark user assumes the model performs well in
  French but encounters issues with unnatural or inaccurate language use when deployed in
  real-world French-speaking contexts, particularly where language nuance is critical.

**Criterion question (answer this for the benchmark under review):**
> Do you statistically validate the quality of translations and propagate uncertainty
> into the benchmark scores?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and aid interpretation. For benchmarks,
  a domain expert knows about the SUT task — for example, a speaker of a low-resource
  language for a low-resource language translation benchmark. Significant experience can
  substitute for formal training.
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language, defining the context,
  task, or question the system is expected to respond to.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`translation_quality_validated`** — The benchmark statistically validates the
   quality of any translated prompts (e.g., human/expert back-translation checks,
   inter-rater agreement on translation accuracy, or measured error rates), rather than
   trusting raw automatic translation.
2. **`uncertainty_propagated`** — The measured translation uncertainty/error is
   propagated into the reported benchmark scores (e.g., confidence intervals, error bars,
   or adjustments reflecting translation noise), not just reported as a side note.

**Strong positive signals:** a reported translation-quality study with statistics
(accuracy, agreement scores like Cohen's kappa, or human-rated fidelity); native-speaker
or domain-expert review of translated prompts; scores accompanied by uncertainty that is
explicitly attributed in part to translation quality; described methodology for combining
translation error into final score intervals.

**Negative / disqualifying signals:** prompts are machine-translated with no validation
described; translation quality mentioned only qualitatively ("we used a good translator")
without statistics; scores reported as point estimates with no uncertainty; translation
validation promised for a future version while the published scores omit it.
