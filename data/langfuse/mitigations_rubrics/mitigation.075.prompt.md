# Mitigation 075 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #75, which mitigates Failure Mode #38.
Source: data/mitigations/75.mdx and data/modes/38.mdx.
-->

## The mitigation under review

- **Mitigation number:** 75
- **Mitigates failure mode:** #38 — *"User does not understand visual representation of
  scores"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark presents model performance
  results using a sophisticated radar chart with multiple axes representing different
  capabilities, where larger area indicates better overall performance. The chart uses
  inverted scales for some metrics where lower values are better (like error rates), but
  doesn't clearly label this inversion. A company's CTO misinterprets the visualization,
  believing that a particular SUT excels in every dimension when in fact it performs
  poorly on critical safety metrics where the scale was inverted. Based on this
  misunderstanding, they deploy this model for sensitive customer service automation,
  only discovering their error when the system begins generating inappropriate responses
  to difficult customer inquiries, after losing several major clients.

**Criterion question (answer this for the benchmark under review):**
> Do you perform design studies with potential users to understand presentation
> requirements for benchmark outputs?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **User Persona:** A representative archetype of the intended end user of a benchmark,
  defined by their goals, knowledge level, behaviors, and contextual needs. Incorporating
  user personas helps ensure evaluations and presentations reflect the information needs
  of the benchmark user.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`design_studies_with_users`** — The developers performed design studies (e.g.,
   usability testing, user interviews, or comprehension studies) with potential users to
   determine how benchmark outputs should be presented.
2. **`presentation_requirements_derived`** — Those studies were used to derive the
   presentation requirements actually reflected in the published results (the findings
   informed how scores are shown).

**Strong positive signals:** a described user study or usability test of the result
presentation; reported findings about how users interpret the visuals and resulting
design changes; involvement of representative target users/personas; evidence the
published charts/tables were shaped by study outcomes.

**Negative / disqualifying signals:** the presentation was designed without any user
input; visuals chosen by the developers' intuition with no testing; a study mentioned but
not connected to the actual presentation; design studies described only as a future plan
while the published presentation is untested.
