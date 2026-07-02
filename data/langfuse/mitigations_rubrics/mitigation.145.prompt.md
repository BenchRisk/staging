# Mitigation 145 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #145, which mitigates Failure Mode #15.
Source: data/mitigations/145.mdx and data/modes/15.mdx.
-->

## The mitigation under review

- **Mitigation number:** 145
- **Mitigates failure mode:** #15 — *"Prompts have known properties allowing for
  achieving an unrealistic (i.e., non-generalizing) performance. For example, prompts are
  of particular and known lengths."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark testing whether code
  generation models detect instructions for generating malware uses prompts that are
  consistently of a particular length, averaging 10 lines of code for malware and 8 lines
  of code for non-malicious code. The model performs well on this benchmark, as it has
  been explicitly optimized to have a higher prior belief of malware for 10 lines of code
  vs 8 lines of code. However, the difference in length is solely a statistical artifact
  of the evaluation and not representative of actual performance. A benchmark user,
  assuming the model's high score represents its ability to prevent malware generation,
  deploys it in a real-world software development environment. The model then generates
  more malware than would otherwise have been generated.

**Criterion question (answer this for the benchmark under review):**
> Do you avoid releasing the test set to SUT developers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark. It is often
  planted deliberately to act as a warning signal (like a "canary in a coal mine").
- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for SUTs, including
  transparency, reproducibility, and guarding against data snooping and benchmark
  overfitting.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`test_set_withheld`** — The test set used for scoring is not released to SUT
   developers — it is held out / private so it cannot be inspected or trained on.
2. **`access_controlled`** — Access to the held-out items is controlled (e.g., evaluation
   via a submission server, sealed split, or canary protections), preventing developers
   from learning exploitable known properties of the prompts.

**Strong positive signals:** an explicit statement that the test/evaluation set is
private or held out; evaluation conducted through a submission / leaderboard server
without exposing items; described separation of a public dev set from a hidden test set;
use of canary data or access controls to detect or prevent leakage.

**Negative / disqualifying signals:** the full test set is publicly downloadable by SUT
developers; no separation between visible and scored items; prompts with known,
inspectable properties released openly; "private test set" promised but not in place for
the current release; the documents are silent while the dataset is plainly fully
published.
