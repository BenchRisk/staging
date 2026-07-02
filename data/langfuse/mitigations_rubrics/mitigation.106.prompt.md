# Mitigation 106 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #106, which mitigates Failure Mode #1.
Source: data/mitigations/106.mdx and data/modes/1.mdx.
-->

## The mitigation under review

- **Mitigation number:** 106
- **Mitigates failure mode:** #1 — *"The information provided by the benchmark does not
  match with the information the benchmark user believes is provided."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~25%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** The benchmark presents a safety score for
  a SUT that does medical prescription dose recommendations and believes "safety"
  includes dose safety, but the safety benchmark only tests whether the model will help
  someone commit violent acts. The benchmark user gets a stomach ulcer from consuming too
  many NSAIDs.

**Criterion question (answer this for the benchmark under review):**
> Do you describe the use cases or the user personas of those who will rely on the
> benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **User Persona:** A representative archetype that models the intended end user of a
  benchmark, defined by their goals, knowledge level, behaviors, and contextual needs.
  Incorporating user personas into benchmark design helps ensure evaluations reflect the
  information needs of the benchmark user. Stating some form of target user publicly helps
  users identify whether the benchmark serves their information needs.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`described`** — The benchmark documents explicitly describe the intended use
   case(s) the benchmark supports, the user persona(s) expected to rely on it, or both.
2. **`relied_on_users_identified`** — The description identifies *who relies on the
   benchmark* and what decision they are making with it, so a reader can tell whether the
   benchmark serves their own information needs.

**Strong positive signals:** an "intended use" or "who this is for" section; named user
personas with goals/knowledge level; concrete use-case scenarios describing the decision
the score informs; explicit scope of who should and should not rely on the benchmark.

**Negative / disqualifying signals:** only a technical capability description with no
named audience or use case; the intended user left implicit; use cases described only for
a future version while the published version omits them; audience description buried in an
appendix rather than where users encounter the benchmark.
