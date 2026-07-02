# Mitigation 066 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #66, which mitigates Failure Mode #40.
Source: data/mitigations/66.mdx and data/modes/40.mdx.
-->

## The mitigation under review

- **Mitigation number:** 66
- **Mitigates failure mode:** #40 — *"Different demographic groups (cultural,
  professional, educational, etc.) viewing the benchmark have different interpretations
  of the information conveyed"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is produced by the American
  Bar Association detailing the legal appropriateness of a legal aid chatbot. A user that
  has not encountered lawyers before sees that all chatbots score poorly and believes the
  technology to be completely inaccurate, while lawyers understand that the low scores
  result more from an abundance of caution than an incapacity of the system to render
  useful advice. Consequently, lawyers are willing to use the legal aid chatbot while
  non-lawyers avoid it.

**Criterion question (answer this for the benchmark under review):**
> Do you localize the presentation of benchmark results in consultation with individuals
> who have deep understanding of how such information is interpreted within specific
> demographic groups?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights and guide interpretation. For
  benchmarks, a domain expert knows about the SUT task or the audience interpreting it;
  significant experience can substitute for formal training.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`localized_presentation`** — The benchmark adapts (localizes) how results are
   presented for specific demographic groups so that each group is likely to interpret
   the scores correctly, rather than using a single one-size-fits-all presentation.
2. **`consulted_interpreters`** — This localization was developed in consultation with
   individuals who have deep understanding of how the information is interpreted within
   those groups (e.g., domain experts or community representatives).

**Strong positive signals:** distinct presentations, explanations, or framing tailored to
identified audiences (e.g., lay users vs. domain experts); documented consultation with
people who understand each group's interpretation; explanatory context that pre-empts
predictable misreadings by a particular group; described user/expert review of how each
group reads the results.

**Negative / disqualifying signals:** a single uniform presentation with no audience
adaptation; no evidence anyone with group-specific interpretive expertise was consulted;
the developer assumes all viewers read scores the same way; localization described only
as a future plan while the published presentation is unadapted.
