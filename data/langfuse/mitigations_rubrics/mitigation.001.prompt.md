# Mitigation 001 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #1, which mitigates Failure Mode #1.
Source: data/mitigations/1.mdx and data/modes/1.mdx.
-->

## The mitigation under review

- **Mitigation number:** 1
- **Mitigates failure mode:** #1 — *"The information provided by the benchmark does not
  match with the information the benchmark user believes is provided."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~80% reduction in failure-mode likelihood; ~25%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark presents a safety score for
  a SUT that does medical prescription dose recommendations, and the user believes
  "safety" includes dose safety, but the safety benchmark only tests whether the model
  will help someone commit violent acts; the user gets a stomach ulcer from consuming too
  many NSAIDs.

**Criterion question (answer this for the benchmark under review):**
> Do you clearly, publicly, and prominently state the user information foraging task
> associated with your benchmark evaluation—using plain and concise language that is
> accessible to the intended users? By 'information foraging task,' we mean the specific
> goal or question that a user is trying to answer or learn about when engaging with the
> benchmark, reflecting their real-world information needs.

## Mitigation-specific glossary (adds to the shared glossary)

- **Information Foraging:** The process by which users search for, evaluate, and extract
  useful information within an environment, guided by perceived value relative to effort
  (information scent). In LLM benchmarking, it refers to how people develop a mental
  model about SUTs, optimizing the trade-off between cognitive cost and informational
  gain. The *information foraging task* is the specific goal or question a user is trying
  to answer when engaging with the benchmark, reflecting their real-world information
  needs.
- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **User Persona:** A representative archetype of the intended end user of a benchmark,
  defined by their goals, knowledge level, behaviors, and contextual needs. Stating some
  form of target user publicly helps users identify whether the benchmark serves their
  information needs.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`stated`** — The benchmark explicitly names the user information foraging task — the
   real-world goal/question a user brings to the benchmark, or equivalently the SUT task
   and what a relying user is meant to learn or decide from the score.
2. **`user_facing_and_accessible`** — It is expressed in plain, concise language an
   intended user (judged as a *reasonable person* in the target audience) can understand
   — not buried in jargon, equations, or implementation detail only.
3. **`public_and_prominent`** — It appears where users actually encounter the benchmark
   (e.g., abstract/intro, README, benchmark/dataset card, landing page, leaderboard
   description), not only deep in an appendix, code comments, or external material.

**Strong positive signals:** an explicit "intended use / intended users / who this is
for" section; a clear statement of the question the score answers ("this benchmark
measures whether a model can …, so a user deciding X can …"); described user personas or
use cases tied to the task; a plain-language scope statement near the top of primary docs.

**Negative / disqualifying signals:** only a technical task description with no link to a
user's real-world information need; the goal must be inferred by the reader; scope stated
only in buried locations; the audience or purpose left implicit; the task is described
only for a *future* version while the published version omits it.
