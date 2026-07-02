# Mitigation 043 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #43, which mitigates Failure Mode #44.
Source: data/mitigations/43.mdx and data/modes/44.mdx.
-->

## The mitigation under review

- **Mitigation number:** 43
- **Mitigates failure mode:** #44 — *"Test set leaks out to the general internet"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~70.0% reduction in failure-mode likelihood; ~0.0%
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
> Do you intentionally avoid providing the test set publicly or to SUT developers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain benchmark
  reliability, including adjustments for evolving requirements, guarding against data
  leakage, and maintaining consistency of evaluation conditions.
- **Canary Data:** Specially crafted benchmark data used to detect developer or evaluation
  practices likely to compromise reliability, often planted to act as a warning signal
  (like a "canary in a coal mine") that the protected test set has leaked or been trained
  on.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`test_set_not_public`** — The full test set is not published or made openly
   downloadable.
2. **`test_set_withheld_from_developers`** — The test set is also not handed to SUT
   developers; evaluation is run such that developers do not receive the live test items
   (e.g., held-out, gated, or run by the benchmark operator).

**Strong positive signals:** an explicit statement that the test set is private/held out;
a gated or operator-run evaluation in which developers submit systems but never receive
test items; described access controls or embargo; canary strings planted to detect leakage
of a withheld set.

**Negative / disqualifying signals:** the full test set published on a repository or
dataset hub; test items shared with submitting developers; an open download of the
evaluation prompts; reliance on "please don't look" rather than actually withholding the
set; only a future intent to gate access while the current set is public.
