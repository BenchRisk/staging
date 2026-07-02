# Mitigation 194 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #194, which mitigates Failure Mode #19.
Source: data/mitigations/194.mdx and data/modes/19.mdx.
-->

## The mitigation under review

- **Mitigation number:** 194
- **Mitigates failure mode:** #19 — *"Cultural norms do not translate between cultural
  contexts (languages, geographies, etc.)."*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~33.33%
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
> Do you tag prompts with their cultural context and explicitly disclaim contexts that
> are not covered?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Normative Properties:** Characteristics, standards, or criteria that define what is
  considered acceptable, desirable, or expected within a particular context or domain —
  e.g., which hand(s) a person may politely eat with at the dinner table. Such properties
  vary across cultural contexts.
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language, defining the context, task, or question the system
  is expected to respond to.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`cultural_tags_present`** — Prompts (or items) carry an explicit cultural-context
   tag or label — e.g., language, region, locale, or culture — recorded in the data or
   its metadata, not merely implied.
2. **`uncovered_contexts_disclaimed`** — The documents explicitly state which cultural
   contexts the benchmark does *not* cover, so users do not over-generalize the results.

**Strong positive signals:** a metadata field or column tagging each prompt's
language/region/culture; a stated taxonomy of cultural contexts represented; an explicit
"not covered / out of scope" statement for particular languages, geographies, or cultural
groups; a disclaimer warning against generalizing to untested cultural contexts.

**Negative / disqualifying signals:** prompts presented without any cultural-context
labeling; coverage of multiple cultures claimed but no per-prompt tags; no statement of
which contexts are excluded; cultural tagging or disclaimers described only for a planned
future release while the published benchmark omits them.
