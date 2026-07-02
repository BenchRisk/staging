# Mitigation 136 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #136, which mitigates Failure Mode #54.
Source: data/mitigations/136.mdx and data/modes/54.mdx.
-->

## The mitigation under review

- **Mitigation number:** 136
- **Mitigates failure mode:** #54 — *"New requirements emerge that would reasonably be
  interpreted as being covered in the task definition"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~73.33% reduction in failure-mode likelihood; ~8.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is designed to evaluate a
  language model's ability to generate "helpful and informative" summaries of news
  articles. Initially, users focus on the conciseness and factual accuracy of the
  summaries. However, over time a new requirement emerges: users increasingly need
  summaries that also highlight potential biases or different perspectives in the
  original articles. A model that scores highly on the original benchmark by producing
  brief, accurate summaries might fail to meet this new requirement by presenting a
  single, seemingly objective viewpoint. Consequently, a user who relied on the initial
  benchmark scores might select a model that is no longer truly "helpful" for their
  evolving needs.

**Criterion question (answer this for the benchmark under review):**
> Is the benchmark periodically reviewed to ensure the SUT task aligns with current user
> expectations, including updating prompts, sourcing new ones for better coverage, and
> releasing versioned updates?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`periodic_review`** — There is a periodic / recurring review process that checks
   whether the SUT task still aligns with current user expectations, rather than a
   one-time release.
2. **`prompts_updated_and_sourced`** — That review feeds prompt maintenance: existing
   prompts are updated and new prompts are sourced to improve coverage as requirements
   evolve.
3. **`versioned_releases`** — Updates are shipped as versioned releases so users can tell
   which revision of the task definition a given score corresponds to.

**Strong positive signals:** a documented review cadence or maintenance policy; a
changelog / release-notes history showing dated versioned updates; descriptions of
prompts being added or revised to track new user needs; explicit versioning scheme tied
to task-definition changes.

**Negative / disqualifying signals:** a single static release with no revision history;
"we plan to update" stated without any realized updates; prompts frozen since launch; no
versioning so users cannot distinguish releases; review or maintenance mentioned only
as future intent.
