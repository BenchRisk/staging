# Mitigation 177 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #177, which mitigates Failure Mode #58.
Source: data/mitigations/177.mdx and data/modes/58.mdx.
-->

## The mitigation under review

- **Mitigation number:** 177
- **Mitigates failure mode:** #58 — *"Understanding the benchmark requires more resources
  (e.g., study, expertise, exploration) than the relying user has time to expend."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~40.0% reduction in failure-mode likelihood; ~41.67%
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
> Do you include example prompts for the task?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically in
  natural language. Prompts define the context, task, or question the system is expected
  to respond to and are central to evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`example_prompts_included`** — The documents present one or more concrete example
   prompts drawn from (or representative of) the benchmark's task, so a reader can see
   what the benchmark actually asks the SUT.
2. **`accessible_to_user`** — The examples are placed where an intended user encounters
   them (paper, README, card, leaderboard, or UI) so they can quickly grasp the task
   without studying the full methodology.

**Strong positive signals:** a "sample prompts" / "examples" section or table; verbatim
prompt text with (optionally) sample responses or expected behavior; illustrative items
shown alongside the score so users see what is being measured; an interactive sample or
demo of representative items.

**Negative / disqualifying signals:** only an abstract description of the task with no
shown examples; example prompts withheld entirely (e.g., to prevent leakage) without any
illustrative substitute; examples present only in private code or held-out data the user
cannot view; examples promised for a future release.
