# Mitigation 036 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #36, which mitigates Failure Mode #37.
Source: data/mitigations/36.mdx and data/modes/37.mdx.
-->

## The mitigation under review

- **Mitigation number:** 36
- **Mitigates failure mode:** #37 — *"User does not read disclaimers"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for conversational AI
  prominently displays a red-bordered disclaimer at the top of its report and executive
  summary stating that it only evaluates basic financial concepts and explicitly warns
  against using the tested systems for real investment advice without professional
  oversight. Despite this clear warning, a financial technology startup focuses solely on
  the performance metrics and implements the highest-scoring SUT as an automated
  investment advisor. The startup's technical team notices but dismisses the disclaimer,
  assuming their minor customizations will address the limitations. They market the
  system as "benchmark-validated" to clients who make significant investment decisions
  based on the AI's recommendations. When market conditions change unexpectedly, the
  system fails to properly assess risk factors it was never benchmarked for, resulting in
  substantial client losses and subsequent lawsuits against the startup for
  misrepresenting the system's capabilities, despite the benchmark authors' clear and
  prominent warnings.

**Criterion question (answer this for the benchmark under review):**
> Do you prominently display disclaimers wherever the benchmark is presented?

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

1. **`disclaimer_exists`** — The benchmark carries a disclaimer that states its
   limitations and warns against misuse or over-reliance (e.g., what decisions the score
   should not be used to make).
2. **`displayed_everywhere`** — The disclaimer appears wherever the benchmark is
   presented — across the leaderboard, report, summary, dataset/model card, and landing
   page — not only in a single document or a one-time footnote.
3. **`prominent`** — It is placed and styled so a reasonable user encounters it
   alongside the results (e.g., near the top, visually distinct), rather than buried in
   fine print, an appendix, or terms-of-use only.

**Strong positive signals:** a clearly styled limitations/disclaimer block adjacent to
the scores in every surface where they appear; repetition of the warning on the
leaderboard, README, and card; a short scope-and-caution statement near the top of each
results page; explicit "do not use this for X" language placed with the numbers.

**Negative / disqualifying signals:** a disclaimer present in the paper but absent from
the leaderboard or card; caution text only in a license/terms file; warnings buried at
the bottom or in an appendix; a single document carrying the disclaimer while other
presentation surfaces omit it; disclaimers planned for a future release while current
surfaces show none.
