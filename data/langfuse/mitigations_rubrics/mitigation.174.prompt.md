# Mitigation 174 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #174, which mitigates Failure Mode #58.
Source: data/mitigations/174.mdx and data/modes/58.mdx.
-->

## The mitigation under review

- **Mitigation number:** 174
- **Mitigates failure mode:** #58 — *"Understanding the benchmark requires more resources
  (e.g., study, expertise, exploration) than the relying user has time to expend"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluates the nuanced safety
  profiles of large language models across a battery of complex, multi-turn adversarial
  prompts, utilizing sophisticated statistical analyses and presenting the results across
  a dozen different sub-scores and visualizations. The accompanying documentation is
  extensive and filled with technical jargon requiring a background in natural language
  processing and safety research to fully comprehend. A busy software engineer looking to
  quickly select a reasonably safe LLM for their application lacks the time and specialized
  knowledge to thoroughly study the benchmark methodology, interpret the various scores,
  and understand their implications for real-world deployment. They might then resort to
  simply looking at an overall "safety ranking" (if provided, and potentially misleadingly
  aggregated) or choose a model based on incomplete or superficial understanding of the
  benchmark results, potentially selecting a model that isn't actually the most suitable
  for their specific safety requirements.

**Criterion question (answer this for the benchmark under review):**
> Do you publish a FAQ along with the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Information Foraging:** The process by which users search for, evaluate, and extract
  useful information within an environment, guided by perceived value relative to effort
  (information scent). In LLM benchmarking, it refers to how people develop a mental model
  about SUTs, optimizing the trade-off between cognitive cost and informational gain.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`faq_published`** — The documents include a FAQ (a question-and-answer resource)
   published alongside the benchmark, lowering the effort a time-constrained user needs to
   understand and correctly use the results.

**Strong positive signals:** a clearly labeled FAQ section or page accompanying the
benchmark; common-question/answer pairs addressing scope, interpretation, and proper use;
the FAQ accessible where users encounter the benchmark (README, card, or landing page).

**Negative / disqualifying signals:** no FAQ provided; only dense methodology or jargon
with no plain-language Q&A; questions answered only scattered across an academic paper
rather than a dedicated FAQ; a FAQ promised for a future release while the published
benchmark has none.
