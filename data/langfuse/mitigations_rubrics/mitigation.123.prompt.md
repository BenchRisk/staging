# Mitigation 123 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #123, which mitigates Failure Mode #39.
Source: data/mitigations/123.mdx and data/modes/39.mdx.
-->

## The mitigation under review

- **Mitigation number:** 123
- **Mitigates failure mode:** #39 — *"User misunderstands the scope of the benchmark"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~60% reduction in failure-mode likelihood; ~12.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark advertises itself as measuring
  "AI creativity" and showcases impressive image generation capabilities of a specific
  SUT. A user, believing this benchmark comprehensively assesses all forms of creativity,
  selects this SUT for a natural language generation task requiring creative storytelling.
  The user is then disappointed when the SUT produces bland and unoriginal narratives,
  realizing too late that the benchmark only evaluated visual creativity and provided no
  insight into the model's language generation abilities.

**Criterion question (answer this for the benchmark under review):**
> Is a contact person listed for the benchmark, and is that person responsive to
> inquiries?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`contact_listed`** — A specific contact person (or clearly identified maintainer
   role) is listed for the benchmark, with a means of reaching them (e.g., named author
   with email, corresponding-author block, maintainer handle).
2. **`responsive`** — There is evidence the contact is responsive to inquiries (e.g.,
   answered issues/threads attributed to that person, a stated response commitment, or
   other documentary signs of active engagement).

**Strong positive signals:** a corresponding-author or "contact / maintainer" block with
an email or handle; the same named person visibly answering questions in an issue tracker
or forum; an explicit invitation to reach out with a stated response expectation.

**Negative / disqualifying signals:** no contact person named (only an organization with
no point of contact); a listed contact with no evidence of responsiveness and visibly
ignored inquiries; a stale address; a contact promised for a future release while the
current one lists none.
