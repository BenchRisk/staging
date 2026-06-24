# Mitigation 122 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #122, which mitigates Failure Mode #39.
Source: data/mitigations/122.mdx and data/modes/39.mdx.
-->

## The mitigation under review

- **Mitigation number:** 122
- **Mitigates failure mode:** #39 — *"User misunderstands the scope of the benchmark"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark advertises itself as measuring
  "AI creativity" and showcases impressive image generation capabilities of a specific
  SUT. A user, believing this benchmark comprehensively assesses all forms of creativity,
  selects this SUT for a natural language generation task requiring creative storytelling.
  The user is then disappointed when the SUT produces bland and unoriginal narratives,
  realizing too late that the benchmark only evaluated visual creativity and provided no
  insight into the model's language generation abilities.

**Criterion question (answer this for the benchmark under review):**
> Is there an ongoing, maintained feedback channel available for benchmark users?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`channel_exists`** — A concrete feedback channel is provided for benchmark users
   (e.g., an issue tracker, discussion forum, mailing list, feedback form, or contact
   address for reporting problems and questions).
2. **`ongoing_and_maintained`** — The channel is ongoing and actively maintained — there
   is evidence it is monitored and responded to (e.g., recent activity, triaged issues,
   answered threads), not a dead link or abandoned inbox.

**Strong positive signals:** a linked, active issue tracker or discussion board with
recent maintainer responses; a stated commitment to monitor and respond; a changelog or
release notes showing user feedback being acted on; a feedback form or community channel
explicitly invited in user-facing docs.

**Negative / disqualifying signals:** no channel for users to raise questions or report
problems; a contact pointer that goes nowhere or is unmonitored; an archived/read-only
repository with no path for feedback; a feedback mechanism promised for a future release
while the current one offers none.
