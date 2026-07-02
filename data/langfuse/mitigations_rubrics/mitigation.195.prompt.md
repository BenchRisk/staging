# Mitigation 195 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #195, which mitigates Failure Mode #20.
Source: data/mitigations/195.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 195
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a model's performance
  in generating responses in French, but the prompts used are initially translated from
  English using an automatic translation tool. These translations introduce subtle
  idiomatic errors, misinterpretations of context, and shifts in tone. As a result, the
  model is evaluated on prompts that do not fully represent the original intent or
  phrasing in the source language. The benchmark user assumes the model performs well in
  French but encounters issues with unnatural or inaccurate language use when deployed in
  real-world French-speaking contexts, particularly where language nuance is critical.

**Criterion question (answer this for the benchmark under review):**
> Do you check whether back-translating from the target language to the source language
> yields expressions consistent with the original language?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language, defining the context, task, or question the system
  is expected to respond to.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide data interpretation. For
  benchmarks, a domain expert is someone who knows about the SUT's task — for instance, a
  speaker of a low-resource language for a translation benchmark.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`back_translation_performed`** — The documents describe back-translating the
   translated *prompts* from the target language to the source language as a validation
   step in producing the prompt set.
2. **`consistency_checked`** — The back-translation is compared against the original
   source-language expressions for consistency (semantic, idiomatic, or tone), with a
   stated criterion or review process.
3. **`results_acted_on`** — The outcome is reported and used to accept, correct, or
   discard prompts in the currently published benchmark.

**Strong positive signals:** an explicit back-translation validation step in the prompt
pipeline; a described comparison of back-translated vs. original text; reviewers (e.g.,
bilingual speakers or domain experts) confirming consistency; reported counts of prompts
revised or dropped after the check.

**Negative / disqualifying signals:** prompts translated once with no reverse-translation
check; only forward translation quality mentioned; back-translation named as an idea but
not performed; the check described only for a future release while the published prompts
were not validated this way.
