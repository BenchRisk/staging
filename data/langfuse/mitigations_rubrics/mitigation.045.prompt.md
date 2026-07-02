# Mitigation 045 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #45, which mitigates Failure Mode #44.
Source: data/mitigations/45.mdx and data/modes/44.mdx.
-->

## The mitigation under review

- **Mitigation number:** 45
- **Mitigates failure mode:** #44 — *"Test set leaks out to the general internet"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~33.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark of challenging multi-hop
  reasoning questions is leaked by a disgruntled former employee. Over time, these
  questions, or paraphrased versions of them, begin to appear on various online forums,
  study websites, and even in synthetic datasets used for pre-training language models. As
  a result, new models are inadvertently (or intentionally) trained on data that overlaps
  with the benchmark, leading to artificially inflated scores that don't reflect genuine
  reasoning ability. A benchmark user, unaware of this data contamination, might choose a
  seemingly high-performing model that simply memorized the leaked test set, only to find
  it performs poorly on novel reasoning tasks in real-world applications.

**Criterion question (answer this for the benchmark under review):**
> Do you actively monitor the internet to check whether any test set samples have appeared
> online?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Canary Data:** Specially crafted benchmark data used to detect developer or evaluation
  practices likely to compromise reliability, often planted deliberately to act as a
  warning signal (like a "canary in a coal mine") that test items have leaked online.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`leak_monitoring_conducted`** — The developer actively monitors for whether test set
   samples (or paraphrases) have appeared online or been absorbed into training data.
2. **`ongoing_process`** — That monitoring is a continuing/repeated activity tied to
   upkeep, not a one-off check.

**Strong positive signals:** a described process for searching the web, forums, or model
training corpora for leaked items; planted canary strings used to detect contamination;
contamination/leakage checks reported and updated over time; a stated cadence for
re-checking exposure.

**Negative / disqualifying signals:** no mention of any leakage or contamination
monitoring; reliance solely on keeping the set private with no detection; a single
one-time contamination check with no ongoing process; monitoring described only as a
future intention; canaries mentioned but never checked.
