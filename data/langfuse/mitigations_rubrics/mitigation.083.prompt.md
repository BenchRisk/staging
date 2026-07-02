# Mitigation 083 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #83, which mitigates Failure Mode #40.
Source: data/mitigations/83.mdx and data/modes/40.mdx.
-->

## The mitigation under review

- **Mitigation number:** 83
- **Mitigates failure mode:** #40 — *"Different demographic groups (cultural,
  professional, educational, etc.) viewing the benchmark have different interpretations of
  the information conveyed"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~25%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is produced by the American Bar
  Association detailing the legal appropriateness of a legal aid chatbot. A user that has
  not encountered lawyers before sees that all chatbots score poorly and believes the
  technology to be completely inaccurate, while lawyers understand that the low scores
  result more from an abundance of caution than an incapacity of the system to render
  useful advice. Consequently, lawyers are willing to use the legal aid chatbot while
  non-lawyers avoid it.

**Criterion question (answer this for the benchmark under review):**
> Do you publicly disclaim the benchmark as a tool intended for consumer use?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Sophisticated User:** An individual with advanced knowledge, experience, or technical
  skill supporting their understanding of information conveyed by the benchmark — for
  example red team members, researchers, adversarial prompt engineers, and domain
  experts.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`disclaimer_present`** — The documents contain an explicit disclaimer that the
   benchmark is not intended for consumer use (i.e., that its results should not be
   relied upon by lay/consumer audiences).
2. **`publicly_visible`** — That disclaimer appears in a public, user-facing location
   where readers actually encounter the benchmark (e.g., landing page, leaderboard, card,
   README), not buried in an appendix or internal note.

**Strong positive signals:** a clear "not intended for consumer use / for professional or
research audiences only" statement near the top of primary docs; a usage caveat tied to
the results; a prominent banner or note framing who should and should not rely on the
scores.

**Negative / disqualifying signals:** no consumer-use disclaimer anywhere; the limitation
implied but never stated; a disclaimer buried deep in an appendix or hidden in fine
print; the benchmark openly marketed to general/consumer audiences; the disclaimer
described only as planned for a future release.
