# Mitigation 038 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #38, which mitigates Failure Mode #39.
Source: data/mitigations/38.mdx and data/modes/39.mdx.
-->

## The mitigation under review

- **Mitigation number:** 38
- **Mitigates failure mode:** #39 — *"User misunderstands the scope of the benchmark"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark advertises itself as measuring
  "AI creativity" and showcases impressive image generation capabilities of a specific
  SUT. A user, believing this benchmark comprehensively assesses all forms of creativity,
  selects this SUT for a natural language generation task requiring creative storytelling.
  The user is then disappointed when the SUT produces bland and unoriginal narratives,
  realizing too late that the benchmark only evaluated visual creativity and provided no
  insight into the model's language generation abilities.

**Criterion question (answer this for the benchmark under review):**
> Do you clearly and prominently display the scope of the benchmark, including guidance on
> what users should or should not rely on it for?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **SUT (System Under Test) Task:** The specific activity or objective the SUT is expected
  to perform in the real world; clearly bounding which task(s) the benchmark covers is
  what defines its scope.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`scope_stated`** — The benchmark explicitly states what it does and does not measure
   (the bounded task/domain it covers), so a user can tell whether it applies to their
   need.
2. **`use_guidance`** — It gives guidance on what users should or should not rely on the
   score for (intended uses and out-of-scope uses).
3. **`clear_and_prominent`** — This scope and guidance is placed where users encounter the
   results (title/abstract, README, card, leaderboard), not only inferable from a buried
   methods detail.

**Strong positive signals:** an explicit "scope" or "what this measures / does not
measure" section near the top of the primary docs; intended-use and out-of-scope
statements on the leaderboard or card; a precise task description that prevents
over-generalization (e.g., "visual creativity only, not text generation"); scope repeated
across the surfaces where the score appears.

**Negative / disqualifying signals:** a broad marketing label ("AI creativity") with no
bounding of what is actually tested; scope only inferable by reading the dataset
construction; no guidance on inappropriate uses; scope stated in the paper but absent from
the leaderboard/card; scope clarification deferred to a future version.
