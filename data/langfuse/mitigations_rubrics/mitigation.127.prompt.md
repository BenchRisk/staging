# Mitigation 127 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #127, which mitigates Failure Mode #40.
Source: data/mitigations/127.mdx and data/modes/40.mdx.
-->

## The mitigation under review

- **Mitigation number:** 127
- **Mitigates failure mode:** #40 — *"Different demographic groups (cultural,
  professional, educational, etc.) viewing the benchmark have different interpretations of
  the information conveyed"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is produced by the American Bar
  Association detailing the legal appropriateness of a legal aid chatbot. A user that has
  not encountered lawyers before sees that all chatbots score poorly and believes the
  technology to be completely inaccurate, while lawyers understand that the low scores
  result more from an abundance of caution than an incapacity of the system to render
  useful advice. Consequently, lawyers are willing to use the legal aid chatbot while
  non-lawyers avoid it.

**Criterion question (answer this for the benchmark under review):**
> Are any assumptions about normative properties (e.g., how the benchmark should be
> interpreted within specific cultures or contexts) clearly documented?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Normative Properties:** Characteristics, standards, or criteria that define what is
  considered acceptable, desirable, or expected within a particular context or domain.
  These properties often guide behavior, decision-making, and evaluations, influencing
  how systems, individuals, or groups act or are assessed.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`normative_assumptions_stated`** — The benchmark identifies the normative
   assumptions embedded in its scoring or grading — the cultural, professional, or
   contextual standards that determine what counts as a good or bad result.
2. **`interpretation_context_documented`** — It documents clearly how results should be
   interpreted within those contexts (e.g., that low scores reflect a conservative
   standard rather than incapacity), so different audiences read the grade the same way.

**Strong positive signals:** an explicit "interpretation," "assumptions," or "normative
framing" section naming the standard applied; a note that scores reflect a particular
professional/cultural baseline; guidance on how a non-expert versus expert should read the
result; stated cultural or contextual scope of the grading criteria.

**Negative / disqualifying signals:** scores presented as context-free or universal with
no stated normative basis; assumptions about "good" behavior left implicit; no guidance
distinguishing how different audiences should interpret the grade; framing promised for a
future version while the published one omits it.
