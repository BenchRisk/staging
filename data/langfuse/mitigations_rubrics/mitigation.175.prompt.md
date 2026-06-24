# Mitigation 175 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #175, which mitigates Failure Mode #58.
Source: data/mitigations/175.mdx and data/modes/58.mdx.
-->

## The mitigation under review

- **Mitigation number:** 175
- **Mitigates failure mode:** #58 — *"Understanding the benchmark requires more resources
  (e.g., study, expertise, exploration) than the relying user has time to expend."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~36.67% reduction in failure-mode likelihood; ~45.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates the nuanced safety
  profiles of LLMs across a battery of complex, multi-turn adversarial prompts, using
  sophisticated statistical analyses and presenting results across a dozen sub-scores and
  visualizations. The documentation is extensive and filled with technical jargon
  requiring an NLP and safety-research background to fully comprehend. A busy software
  engineer looking to quickly select a reasonably safe LLM lacks the time and specialized
  knowledge to study the methodology and interpret the various scores, so they resort to a
  single (possibly misleadingly aggregated) "safety ranking" and select a model that is
  not actually most suitable for their safety requirements.

**Criterion question (answer this for the benchmark under review):**
> Do you provide simple interpretative statements for scores in the user interface?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Lower-level Measures to Higher-level Grades:** The hierarchical structure used in
  evaluating and scoring SUTs, where lower-level measures (accuracy, precision, recall,
  error rates, user feedback scores) feed into higher-level grades (overall safety score,
  general performance rating, compliance rating).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`interpretive_statements_present`** — Each score (or score type) is accompanied by a
   short plain-language statement explaining what the number means and how to read it,
   not just the raw figure.
2. **`in_user_interface`** — The interpretive statements appear in the user-facing
   presentation surface (leaderboard, results page, dashboard, score card) where a user
   actually views scores — not only buried in a paper's methods section.
3. **`accessible_language`** — The statements use plain, concise language a *reasonable
   person* in the intended audience can understand without specialized study.

**Strong positive signals:** tooltips, captions, or inline blurbs next to each score
("a score of X means the model refused Y% of harmful requests"); a "how to read this
score" or "what this means" explainer beside results; thresholds or qualitative bands
(e.g., good/moderate/poor) attached to numeric scores in the UI.

**Negative / disqualifying signals:** the interface shows only bare numbers, ranks, or
charts with no narrative; interpretation is offered only in a separate technical paper or
appendix; the meaning of scores must be inferred by the reader; jargon-heavy labels with
no plain-language gloss.
