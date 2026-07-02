# Mitigation 176 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #176, which mitigates Failure Mode #58.
Source: data/mitigations/176.mdx and data/modes/58.mdx.
-->

## The mitigation under review

- **Mitigation number:** 176
- **Mitigates failure mode:** #58 — *"Understanding the benchmark requires more resources
  (e.g., study, expertise, exploration) than the relying user has time to expend."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~41.67%
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
> Have you simplified the task to reduce the mental effort required to understand it?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **SUT (System Under Test) Task:** The specific activity or objective the SUT is
  expected to perform in the real world; a well-defined SUT task gives the benchmark the
  capacity to measure and report properties related to that task.
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Decomposing complex tasks into subtasks lets evaluators diagnose strengths and
  weaknesses, support modular scoring, and improve the interpretability of results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`task_simplified`** — The benchmark task (and its results) has been deliberately
   scoped, narrowed, or decomposed to lower the cognitive effort required to understand
   what is measured and what a score means.
2. **`reduced_effort_evidenced`** — The documents show the simplification reduces mental
   effort for the intended user (e.g., a small set of clearly-named subtasks instead of
   one opaque composite, or a streamlined presentation rather than a dozen sub-scores).

**Strong positive signals:** an explicit statement that the task or reporting was
simplified for accessibility; a short, focused set of clearly-labeled subtasks; removal
of redundant or overly technical sub-scores in favor of a digestible summary; design
notes about reducing reader burden.

**Negative / disqualifying signals:** the task is described as broad, "general," or
multi-faceted with no simplification; results presented across many dense sub-scores and
visualizations; documentation that assumes specialized expertise; any simplification only
promised for a future version.
