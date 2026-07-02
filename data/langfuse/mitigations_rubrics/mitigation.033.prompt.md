# Mitigation 033 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #33, which mitigates Failure Mode #34.
Source: data/mitigations/33.mdx and data/modes/34.mdx.
-->

## The mitigation under review

- **Mitigation number:** 33
- **Mitigates failure mode:** #34 — *"Inadequate sample size for identifying
  performance"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (5) Scoring
- **Risk reduction if adopted:** ~80.0% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating toxicity
  filtering in content moderation systems tests each SUT on only 20 prompts designed to
  elicit harmful content. Due to this small sample size, the benchmark fails to capture
  the true distribution of harmful content, edge cases, and adversarial examples. One
  SUT randomly performs well on these specific 20 cases but has serious weaknesses with
  other toxic content patterns. The benchmark user selects this SUT for moderating a
  large online community platform, confident in its high score. Within weeks of
  deployment, users discover numerous ways to bypass the filters, resulting in
  widespread policy violations, user harassment, and significant brand damage before the
  system's actual limitations are fully understood.

**Criterion question (answer this for the benchmark under review):**
> Do you calibrate the number of prompts used according to statistical analysis, or
> otherwise ensure that the sample count is sufficient to produce consistent and reliable
> measures?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Random Performance Level:** The baseline performance metric achieved by a SUT when it
  makes predictions purely at random, without using any learned information or strategy.
  It serves as a reference point grounding user expectations and helps interpret whether
  a score is distinguishable from chance.
- **Subtask:** A narrowly defined SUT Task within a broader collection of benchmarked
  tasks. Decomposing into subtasks affects how many samples fall into each measured
  category, and thus the reliability of each per-subtask score.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`sample_count_reported`** — The benchmark states how many prompts/items are used to
   produce each reported score (overall and, where scores are broken out by subtask or
   category, per breakdown).
2. **`sufficiency_justified`** — The developer justifies that the sample count is
   adequate to produce consistent and reliable measures — via statistical analysis
   (e.g., power analysis, confidence-interval width, variance estimates) or an equivalent
   documented rationale, not merely an unargued count.

**Strong positive signals:** a stated power analysis or sample-size calculation; reported
confidence intervals or standard errors that the count is chosen to bound; explicit
discussion that N is large enough to distinguish systems above noise; per-category counts
shown so thin slices are visible; a statement that small subsets were merged or excluded
because they were too small to be reliable.

**Negative / disqualifying signals:** scores presented with no item count at all; tiny
per-task Ns with no acknowledgement of their unreliability; a count chosen for cost or
convenience with no statistical justification; aggregate N reported but per-subtask
scores derived from a handful of items each; sufficiency only asserted ("we use enough
prompts") without any analysis.
