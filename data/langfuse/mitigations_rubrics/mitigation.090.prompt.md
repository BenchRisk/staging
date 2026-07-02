# Mitigation 090 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #90, which mitigates Failure Mode #11.
Source: data/mitigations/90.mdx and data/modes/11.mdx.
-->

## The mitigation under review

- **Mitigation number:** 90
- **Mitigates failure mode:** #11 — *"Prompts focus on adversarial users (e.g., users are
  attempting to circumvent a guard model)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark evaluating the safety of a
  language model focuses exclusively on adversarial jailbreak attempts—e.g., users trying
  to trick the model into giving instructions for dangerous activities. It ignores benign
  but naive users who unintentionally elicit harmful responses due to ambiguous phrasing
  or lack of domain knowledge. A model is trained and evaluated solely on its ability to
  block adversarial attacks and scores highly. However, when deployed in a public helpdesk
  context, it frequently outputs unsafe or misleading content to sincere users with poorly
  worded or misunderstood queries. The benchmark user believes the model is safe and
  deploys it broadly, exposing end users to unanticipated risks.

**Criterion question (answer this for the benchmark under review):**
> Does the benchmark avoid presenting results for adversarial prompts or scenarios where
> adversarial users are not applicable?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the SUT task, ensuring sufficient
  variability and representation. It asks, "will the relying user believe the benchmark
  covers something impacting their LLM decisions that is not covered?"
- **Adversarial Users:** Individuals or entities that intentionally interact with an AI
  system in ways designed to exploit its vulnerabilities or induce harmful behavior. They
  typically use jailbreaks to bypass guard mechanisms and intentionally move out of the
  task distribution contemplated by system developers.
- **Jailbreak:** A prompt designed to bypass the safety, content, or behavioral
  constraints of an AI system, enabling it to produce restricted, harmful, or unintended
  outputs. In benchmarking, jailbreaks test the robustness of safety measures.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`scopes_applicability`** — The documents identify the scenarios or deployment
   contexts to which adversarial-user results apply and distinguish them from contexts
   (e.g., benign/naive users) where adversarial framing is not applicable.
2. **`withholds_inapplicable_results`** — The benchmark avoids presenting adversarial
   results for scenarios where adversarial users are not applicable, so users are not
   shown adversarial scores as if they characterized non-adversarial use.

**Strong positive signals:** a clear statement of when adversarial results do and do not
apply; results segmented by user type (adversarial vs. benign) rather than a single
conflated safety score; an explicit caveat that adversarial scores should not be read as
covering naive-user safety; suppression or clear labeling of adversarial results outside
their applicable scenarios.

**Negative / disqualifying signals:** a single adversarial-only safety score presented as
general safety; adversarial results shown for contexts where they do not apply with no
scoping caveat; no distinction drawn between adversarial and non-adversarial use; the
applicability scoping described only as planned for a future release.
