# Mitigation 014 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #14, which mitigates Failure Mode #11.
Source: data/mitigations/14.mdx and data/modes/11.mdx.
-->

## The mitigation under review

- **Mitigation number:** 14
- **Mitigates failure mode:** #11 — *"Prompts focus on adversarial users (e.g., users are
  attempting to circumvent a guard model)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~58.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluating the safety of a
  language model focuses exclusively on adversarial jailbreak attempts — e.g., users trying
  to trick the model into giving instructions for dangerous activities. It ignores benign
  but naive users who unintentionally elicit harmful responses due to ambiguous phrasing or
  lack of domain knowledge. A model is trained and evaluated solely on its ability to block
  adversarial attacks and scores highly. However, when deployed in a public helpdesk
  context, it frequently outputs unsafe or misleading content to sincere users with poorly
  worded or misunderstood queries. The benchmark user believes the model is safe and
  deploys it broadly, exposing end users to unanticipated risks.

**Criterion question (answer this for the benchmark under review):**
> Do you publicly state that the benchmark focuses on adversial testing or does the
> benchmark design sample beyond adversarial cases?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Adversarial Users:** Individuals or entities that intentionally interact with an AI
  system in ways designed to exploit its vulnerabilities or induce harmful behavior. They
  typically use jailbreaks to bypass guard mechanisms and intentionally move out of the
  task distribution contemplated by system developers.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling it to produce restricted, harmful, or unintended
  outputs. In benchmarking, jailbreaks are used to test the robustness of safety measures
  and to identify points of failure in content moderation or policy adherence.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **at least one** of the following for the *currently published*
benchmark (the criterion is satisfied by either disclosure or broader sampling). Each id
below is a `requirement` key in the output.

1. **`adversarial_focus_disclosed`** — The documents publicly and clearly state that the
   benchmark focuses on adversarial testing (e.g., jailbreaks / adversarial users), so a
   relying user is not misled into thinking it covers benign-user safety.
2. **`samples_beyond_adversarial`** — Alternatively, the benchmark design demonstrably
   samples beyond adversarial cases (e.g., includes benign or naive-user prompts), and the
   documents describe this non-adversarial coverage.

**Strong positive signals:** an explicit scope statement that the benchmark targets
adversarial/jailbreak behavior; a described prompt taxonomy that includes benign or
unintentional-misuse cases alongside adversarial ones; reported proportions of adversarial
vs. non-adversarial prompts; intended-use language clarifying that benign-user safety is
out of scope.

**Negative / disqualifying signals:** an adversarial-only prompt set presented as general
"safety" with no scope disclosure; no statement of focus and no benign-user coverage; the
adversarial framing left for the reader to infer; broader sampling described only as future
work.
