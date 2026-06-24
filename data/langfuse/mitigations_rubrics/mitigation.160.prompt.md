# Mitigation 160 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #160, which mitigates Failure Mode #38.
Source: data/mitigations/160.mdx and data/modes/38.mdx.
-->

## The mitigation under review

- **Mitigation number:** 160
- **Mitigates failure mode:** #38 — *"User does not understand visual representation of
  scores"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark presents model performance
  results using a sophisticated radar chart with multiple axes representing different
  capabilities, where larger area indicates better overall performance. The chart uses
  inverted scales for some metrics where lower values are better (like error rates), but
  doesn't clearly label this inversion. A company's CTO misinterprets the visualization,
  believing that a particular SUT excels in every dimension when in fact it performs
  poorly on critical safety metrics where the scale was inverted. Based on this
  misunderstanding, they deploy this model for sensitive customer service automation, only
  discovering their error when the system begins generating inappropriate responses to
  difficult customer inquiries. By the time they correct their misunderstanding and
  replace the system, they've already lost several major clients and faced public
  criticism for their irresponsible AI deployment.

**Criterion question (answer this for the benchmark under review):**
> Do you limit the presentation and audience to sophisticated users who can be assumed to
> understand visual representations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Sophisticated User:** An individual with advanced knowledge, experience, or technical
  skill supporting their understanding of information conveyed by the benchmark, such as
  red team members, researchers, adversarial prompt engineers, and domain experts.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`audience_limited_to_sophisticated`** — The benchmark limits its intended audience to
   sophisticated users who can be assumed to understand the visual representations used,
   rather than presenting to a general/unsophisticated audience.
2. **`presentation_scoped_to_audience`** — The presentation (e.g., charts, dashboards,
   leaderboard) is correspondingly scoped/gated to that sophisticated audience, so the
   visualization is delivered to users assumed able to interpret it.

**Strong positive signals:** an explicit statement that results/visualizations are
intended for expert or sophisticated users (researchers, red-teamers, domain experts);
access restricted or scoped to such an audience; documentation that the presentation
assumes technical literacy in reading the chart types used; a stated intended-user
section naming sophisticated users.

**Negative / disqualifying signals:** results presented openly to a general or
non-expert audience with no audience restriction; public-facing visualizations aimed at
lay users; no statement limiting the audience; the audience limitation described only for
a future release while the current presentation is unrestricted.
