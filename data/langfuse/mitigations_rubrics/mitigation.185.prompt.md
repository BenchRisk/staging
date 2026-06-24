# Mitigation 185 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #185, which mitigates Failure Mode #20.
Source: data/mitigations/185.mdx and data/modes/20.mdx.
-->

## The mitigation under review

- **Mitigation number:** 185
- **Mitigates failure mode:** #20 — *"Producing prompts in a language from prompts
  translated from another language introduces errors."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~83.33% reduction in failure-mode likelihood; ~16.67%
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
> Is all the data of naturalistic origin (e.g., collected from public forums)?

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

1. **`naturalistic_origin`** — All of the benchmark data is documented as naturalistic in
   origin — authored or collected in its native language from genuine usage (e.g., public
   forums) — rather than translated from another language.
2. **`provenance_documented`** — The naturalistic origin is stated for the data as a whole
   (the "all the data" qualifier), so no translated subset slips in undocumented.

**Strong positive signals:** data described as collected from public forums or other
naturally occurring, native-language sources; explicit confirmation that the entire
dataset (not just part) is naturalistic; no translation pipeline in the data-generation
description; provenance/attribution to real-world text in the target language.

**Negative / disqualifying signals:** any portion of the data translated from another
language (manually or automatically); synthetic or templated prompts substituted for
naturalistic ones; provenance stated for only some of the data; silence on where the data
came from.
