# Mitigation 037 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #37, which mitigates Failure Mode #38.
Source: data/mitigations/37.mdx and data/modes/38.mdx.
-->

## The mitigation under review

- **Mitigation number:** 37
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
> Do you conduct user evaluations with your target user group and iterate on the
> benchmark design based on their feedback?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **User Persona:** A representative archetype of the intended end user of a benchmark,
  defined by their goals, knowledge level, behaviors, and contextual needs. Identifying
  the target user group is a prerequisite to recruiting representative participants for a
  user evaluation.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`user_evaluation_conducted`** — The developer reports conducting an evaluation
   (e.g., usability testing, interviews, surveys) of how users read and interpret the
   benchmark's results or presentation.
2. **`with_target_users`** — Those participants are drawn from the benchmark's target
   user group, not just the authors or arbitrary convenience subjects.
3. **`iterated_on_feedback`** — The design or presentation was changed in response to
   that feedback, and the change is reflected in the currently published benchmark.

**Strong positive signals:** a described user study or usability test with target-audience
participants; reported feedback findings about confusing visuals or wording; a
before/after describing presentation changes made because of the feedback; an
acknowledgements or methods section naming the participant pool and how it matched the
intended users.

**Negative / disqualifying signals:** no mention of any user testing; "we designed it to
be clear" with no evidence users were consulted; feedback gathered only from the authors
or developers; a study described but no resulting design change; user evaluation listed as
future work while the current release reflects none.
