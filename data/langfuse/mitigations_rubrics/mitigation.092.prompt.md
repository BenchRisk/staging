# Mitigation 092 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #92, which mitigates Failure Mode #20.
Source: data/mitigations/92.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 92
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~25%
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
> Do you avoid using data vendors and machine translation in prompt generation, ensuring
> all prompts originate in the language of the test?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Effective prompt design
  directly influences the reliability and interpretability of benchmark results.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For a low
  resource language translation benchmark, a domain expert includes a speaker of that
  language; a person need not have formal training where they have significant experience
  and knowledge within the domain.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`native_origin`** — Prompts in the tested language are stated to originate in that
   language (e.g., authored by native or fluent speakers of the test language), not
   produced by translating from a source language.
2. **`no_machine_translation`** — Machine / automatic translation is explicitly not used
   to produce the prompt set in the tested language.
3. **`no_data_vendors`** — Prompt generation does not rely on third-party data vendors
   whose provenance and language origin are unverified.

**Strong positive signals:** a stated process of authoring prompts directly by native
speakers or in-language domain experts; an explicit policy that no machine translation was
applied to prompts; documentation of who wrote the prompts and in which language;
per-language provenance notes confirming native origin.

**Negative / disqualifying signals:** prompts described as translated (machine or
otherwise) from another language; reliance on an unnamed data vendor or scraped/translated
corpus; silence on prompt-language provenance; native authoring promised only for a future
multilingual release while the current set is translated.
