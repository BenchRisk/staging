# Mitigation 181 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #181, which mitigates Failure Mode #20.
Source: data/mitigations/181.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 181
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~86.67% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a model's performance
  in generating responses in French, but the prompts are initially translated from
  English using an automatic translation tool. These translations introduce subtle
  idiomatic errors, misinterpretations of context, and shifts in tone, so the model is
  evaluated on prompts that do not fully represent the original intent or phrasing. The
  user assumes the model performs well in French but encounters unnatural or inaccurate
  language use when deploying it in real French-speaking contexts, particularly where
  language nuance is critical.

**Criterion question (answer this for the benchmark under review):**
> Is the benchmark data sourced entirely from a single language, and do you make no claims
> regarding its applicability to other languages?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically in
  natural language. Prompts define the context, task, or question the system is expected
  to respond to and are central to evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`single_language_source`** — The benchmark data is documented as sourced entirely
   from one language, with no translation pipeline used to produce prompts in another
   language.
2. **`no_cross_language_claims`** — The documents make no claims that the benchmark's
   results apply to, or generalize to, languages other than the single source language.

**Strong positive signals:** an explicit statement of a single source language for all
data; scope limited to that language with no translation step described; an explicit
disclaimer that results are not claimed to transfer to other languages; the prompts
described as natively authored, not translated.

**Negative / disqualifying signals:** prompts translated from another language (manually
or automatically); claims or implications of multilingual/cross-language applicability;
multiple languages mixed without describing native sourcing; silence on language
provenance combined with broad applicability claims.
