# Mitigation 086 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #86, which mitigates Failure Mode #9.
Source: data/mitigations/86.mdx and data/modes/9.mdx.
-->

## The mitigation under review

- **Mitigation number:** 86
- **Mitigates failure mode:** #9 — *"Adversarial prompt bulking (increasing the number of
  prompts by multiplying them by the number of tactics)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate model
  robustness against jailbreaks creates 100 base adversarial prompts and then applies 10
  paraphrasing or obfuscation tactics to each, resulting in 1,000 prompts. While this
  gives the appearance of broad coverage, the underlying semantic space is still
  narrow—centered on just 100 scenarios. A model that learns to defend against these
  specific base prompts or common surface patterns scores highly, even though it remains
  vulnerable to novel or semantically different jailbreaks. A benchmark user assumes the
  model is robust and deploys it in a moderation tool, which is quickly circumvented by
  attacks not represented in the bloated prompt set.

**Criterion question (answer this for the benchmark under review):**
> Do you source prompts from multiple populations with distinct demographic attributes of
> the prompt writers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the SUT task, ensuring sufficient
  variability and representation. It asks, "will the relying user believe the benchmark
  covers something impacting their LLM decisions that is not covered?"
- **Adversarial Prompt Bulking:** A technique of increasing the number of prompts by
  multiplying them with various tactics (e.g., jailbreak templates) and root instances.
  See also "Prompt Perturbation Bulking."
- **Tactics:** A transformation applied to a prompt to produce an altered prompt,
  typically for the purpose of jailbreaking a SUT.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`multiple_populations`** — Prompts are sourced from more than one population of prompt
   writers rather than from a single author, team, template, or model.
2. **`distinct_demographic_attributes`** — Those populations have distinct demographic
   attributes (e.g., differing cultural, professional, educational, or linguistic
   backgrounds) documented as the basis for the sourcing.

**Strong positive signals:** a described contributor pool spanning multiple demographic
groups; reported demographic attributes of the prompt writers; a sourcing process that
recruits authors from distinct populations to broaden the semantic space beyond a few
base scenarios; documentation linking writer diversity to wider coverage.

**Negative / disqualifying signals:** prompts written by a single author, homogeneous
team, or one model; coverage claimed solely through tactic-based bulking of a few base
prompts; no information on who wrote the prompts or their demographics; a diversity claim
with no description of the populations; multi-population sourcing planned only for a
future release.
