# Mitigation 134 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #134, which mitigates Failure Mode #19.
Source: data/mitigations/134.mdx and data/modes/19.mdx.
-->

## The mitigation under review

- **Mitigation number:** 134
- **Mitigates failure mode:** #19 — *"Cultural norms do not translate between cultural
  contexts (languages, geographies, etc.)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark tests a language model's
  ability to understand and generate appropriate responses to cultural references in a
  variety of languages. However, the evaluation is conducted primarily in English, using
  Western cultural norms and references. When the model is deployed in a different
  geographic or linguistic context, such as in Japan or Brazil, it fails to understand or
  appropriately respond to culturally specific references, phrases, and social nuances,
  leading to misunderstandings and alienation in non-Western audiences. The benchmark
  user assumes the model is universally adept at handling cultural nuances but encounters
  failures in real-world deployments across different regions.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark avoid processing human languages in its inputs and outputs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Normative Properties:** Characteristics, standards, or criteria that define what is
  considered acceptable, desirable, or expected within a particular context or domain.
  These properties guide behavior and evaluation (e.g., which hand(s) a person may
  politely eat with at the dinner table).
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`non_natural_language`** — The benchmark's inputs and outputs do not consist of
   human (natural) language whose meaning is culturally bound — for example, the task
   operates over code, structured data, mathematics, or other formal/non-linguistic
   representations.
2. **`scope_excludes_culture`** — The documents make clear that the task does not depend
   on processing natural-language inputs or producing natural-language outputs that would
   be subject to cross-cultural interpretation.

**Strong positive signals:** the task is defined over code, math, symbolic logic,
tabular/structured data, or other non-natural-language modalities; explicit statement
that the benchmark does not evaluate natural-language understanding or generation;
input/output examples that contain no culturally situated human-language content.

**Negative / disqualifying signals:** prompts or expected outputs are natural-language
text (questions, dialogue, summaries, instructions); the benchmark evaluates
comprehension or generation of human language; cultural or linguistic content appears in
the examples; the documents are silent on whether natural language is processed while
the examples plainly contain it.
