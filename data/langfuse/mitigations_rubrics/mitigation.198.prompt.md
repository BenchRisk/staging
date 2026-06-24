# Mitigation 198 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #198, which mitigates Failure Mode #1.
Source: data/mitigations/198.mdx and data/modes/1.mdx.
-->

## The mitigation under review

- **Mitigation number:** 198
- **Mitigates failure mode:** #1 — *"The information provided by the benchmark does not
  match with the information the benchmark user believes is provided."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark presents a safety score for
  a SUT that does medical prescription dose recommendations and believes "safety"
  includes dose safety, but the safety benchmark only tests whether the model will help
  someone commit violent acts. The benchmark user gets a stomach ulcer from consuming too
  many NSAIDs.

**Criterion question (answer this for the benchmark under review):**
> Do you clearly, publicly, and prominently state the user information foraging task
> associated with the evaluation, even if only for sophisticated users such as LLM
> engineers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Information Foraging:** The process by which users search for, evaluate, and extract
  useful information within an environment, guided by perceived value relative to effort
  (information scent). In LLM benchmarking it refers to how people develop a mental model
  about SUTs. The *information foraging task* is the specific goal or question a user is
  trying to answer when engaging with the benchmark.
- **Sophisticated User:** An individual with advanced knowledge, experience, or technical
  skill supporting their understanding of information conveyed by the benchmark — e.g.,
  red-team members, researchers, adversarial prompt engineers, and domain experts.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`foraging_task_stated`** — The documents explicitly name the user information
   foraging task — the real-world goal/question a user brings to the benchmark, or
   equivalently the SUT task and what a relying user is meant to learn or decide.
2. **`public_and_prominent`** — That statement appears publicly and prominently where the
   benchmark is encountered (abstract/intro, README, card, landing page, or leaderboard
   description), not buried in an appendix or external material.

Note: per this criterion, stating the task in terms accessible only to *sophisticated
users* such as LLM engineers is acceptable; a plain-language framing for lay users is not
required for this mitigation.

**Strong positive signals:** an explicit statement of the question the score answers
("this benchmark measures whether a model can …, so a user deciding X can …"); a clearly
labeled intended-use or scope statement near the top of the primary docs; the foraging
task spelled out for the technical audience even if in technical terms.

**Negative / disqualifying signals:** only a technical metric description with no link to
a user's real-world information need; the goal left for the reader to infer; the task
stated only in a buried location or external source; the foraging task described only for
a future version while the published version omits it.
