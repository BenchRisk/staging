# Mitigation 197 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #197, which mitigates Failure Mode #38.
Source: data/mitigations/197.mdx and data/modes/38.mdx.
-->

## The mitigation under review

- **Mitigation number:** 197
- **Mitigates failure mode:** #38 — *"User does not understand visual representation of
  scores."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~29.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark presents model performance
  using a sophisticated radar chart with multiple axes, where larger area indicates
  better overall performance. The chart uses inverted scales for some metrics where lower
  values are better (like error rates), but does not clearly label this inversion. A
  company's CTO misinterprets the visualization, believing a particular SUT excels in
  every dimension when in fact it performs poorly on critical safety metrics where the
  scale was inverted. Based on this misunderstanding, they deploy the model for sensitive
  customer-service automation, only discovering the error when the system begins
  generating inappropriate responses, losing several major clients and facing public
  criticism for irresponsible AI deployment.

**Criterion question (answer this for the benchmark under review):**
> Have you implemented interactive tutorials or help sections that explain the visual
> representations used in the benchmarks?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`help_or_tutorial_exists`** — The benchmark provides an interactive tutorial, guided
   walkthrough, help section, tooltips, or equivalent explanatory aid attached to its
   results presentation.
2. **`explains_visualizations`** — That aid specifically explains how to read the visual
   representations used (e.g., what each axis/scale means, which direction is "better,"
   how to read the chart), not just general FAQ or methodology prose.
3. **`available_to_users`** — The aid is part of the currently published, user-facing
   presentation (leaderboard, results page, or card) where users actually view scores.

**Strong positive signals:** an interactive "how to read this chart" walkthrough;
tooltips or hover explanations on the visualization; a help/legend panel describing scale
direction and units; an onboarding tutorial for the results dashboard.

**Negative / disqualifying signals:** charts shown with no explanatory aid; only a static
methodology section unconnected to the visualization; help described as a future feature;
explanation buried in a separate paper rather than offered where the visuals appear.
