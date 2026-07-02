# Mitigation 074 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #74, which mitigates Failure Mode #44.
Source: data/mitigations/74.mdx and data/modes/44.mdx.
-->

## The mitigation under review

- **Mitigation number:** 74
- **Mitigates failure mode:** #44 — *"Test set leaks out to the general internet"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~40.0% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark of challenging multi-hop
  reasoning questions is leaked by a disgruntled former employee. Over time, these
  questions, or paraphrased versions of them, begin to appear on various online forums,
  study websites, and even in synthetic datasets used for pre-training language models.
  As a result, new models are inadvertently (or intentionally) trained on data that
  overlaps with the benchmark, leading to artificially inflated scores that don't reflect
  genuine reasoning ability. A benchmark user, unaware of this data contamination, might
  choose a seemingly high-performing model that simply memorized the leaked test set,
  only to find it performs poorly on novel reasoning tasks in real-world applications.

**Criterion question (answer this for the benchmark under review):**
> Do you periodically introduce new test set prompts and monitor for statistical
> differences in performance between new and old items?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`new_prompts_periodically_introduced`** — The benchmark periodically introduces new
   test-set prompts (refreshes the test set over time) rather than relying on a static,
   fixed set.
2. **`old_vs_new_performance_monitored`** — The developers monitor for statistical
   differences in performance between newly introduced items and older items, using such
   gaps as a contamination/leakage signal.

**Strong positive signals:** a stated refresh cadence for the test set; reported
comparisons of model performance on new vs. old items with statistics; an explicit
contamination-detection process keyed to performance gaps; versioned test sets with dated
additions.

**Negative / disqualifying signals:** a single static test set never refreshed; new items
added without any comparison of new- vs. old-item performance; leakage monitoring
mentioned only qualitatively; periodic refresh described only as a future plan while the
published benchmark uses a fixed set.
