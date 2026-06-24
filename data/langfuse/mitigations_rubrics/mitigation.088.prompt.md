# Mitigation 088 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #88, which mitigates Failure Mode #40.
Source: data/mitigations/88.mdx and data/modes/40.mdx.
-->

## The mitigation under review

- **Mitigation number:** 88
- **Mitigates failure mode:** #40 — *"Different demographic groups (cultural,
  professional, educational, etc.) viewing the benchmark have different interpretations of
  the information conveyed"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is produced by the American Bar
  Association detailing the legal appropriateness of a legal aid chatbot. A user that has
  not encountered lawyers before sees that all chatbots score poorly and believes the
  technology to be completely inaccurate, while lawyers understand that the low scores
  result more from an abundance of caution than an incapacity of the system to render
  useful advice. Consequently, lawyers are willing to use the legal aid chatbot while
  non-lawyers avoid it.

**Criterion question (answer this for the benchmark under review):**
> Do you limit promotion of the benchmark to individuals with a sophisticated
> understanding of the task being benchmarked and its measurement implications?

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
  experts who can systematically probe model limitations.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to guide data interpretation and decision-making. For
  benchmarks, a domain expert knows about the SUT's task — for example a lawyer for a
  legal-aid chatbot benchmark.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`promotion_limited`** — The documents indicate that promotion/dissemination of the
   benchmark is deliberately limited or targeted (e.g., distributed through professional
   or expert channels) rather than broadly publicized to a general audience.
2. **`audience_is_sophisticated`** — The targeted recipients are individuals with a
   sophisticated understanding of the benchmarked task and its measurement implications
   (domain experts / sophisticated users), and this is stated.

**Strong positive signals:** a stated policy of restricting promotion to expert or
professional venues; framing that the benchmark is shared with researchers/domain experts
who understand its measurement implications; gated or audience-scoped dissemination;
explicit identification of the sophisticated audience for the results.

**Negative / disqualifying signals:** the benchmark broadly promoted to general/consumer
audiences (press, social media, marketing) with no audience limitation; no statement of a
targeted sophisticated audience; promotion strategy unaddressed; audience limitation
described only as a future intention rather than current practice.
