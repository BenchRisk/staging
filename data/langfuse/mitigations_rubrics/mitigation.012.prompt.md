# Mitigation 012 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #12, which mitigates Failure Mode #9.
Source: data/mitigations/12.mdx and data/modes/9.mdx.
-->

## The mitigation under review

- **Mitigation number:** 12
- **Mitigates failure mode:** #9 — *"Adversarial prompt bulking (increasing the number of
  prompts by multiplying them by the number of tactics)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~41.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate model
  robustness against jailbreaks creates 100 base adversarial prompts and then applies 10
  paraphrasing or obfuscation tactics to each, resulting in 1,000 prompts. While this gives
  the appearance of broad coverage, the underlying semantic space is still narrow —
  centered on just 100 scenarios. A model that learns to defend against these specific base
  prompts or common surface patterns scores highly, even though it remains vulnerable to
  novel or semantically different jailbreaks. A benchmark user assumes the model is robust
  and deploys it in a moderation tool, which is quickly circumvented by attacks not
  represented in the bloated prompt set.

**Criterion question (answer this for the benchmark under review):**
> Do you state sample counts in terms of root samples and templates (i.e., structured
> expressions of inputs subject to perturbation or instantiation)? Templates may be
> excluded entirely from the design.

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Adversarial Prompt Bulking:** A technique of increasing the number of prompts by
  multiplying them with various tactics (e.g., jailbreak templates) and root instances.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to generate
  variations, expansions, or perturbations in data-driven processes.
- **Template:** A root prompt from which structured changes facilitate interrogation of a
  SUT property subject to benchmark. Templates do not necessarily produce jailbreaks since
  they do not necessarily have an adversarial intent.
- **Tactics:** A transformation applied to a prompt to produce an altered prompt, typically
  for the purpose of jailbreaking a SUT.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`root_sample_count_stated`** — The documents state sample counts in terms of *root
   samples* (the underlying base instances), so the reader can see the true unbulked size
   rather than only the inflated total.
2. **`template_count_stated`** — The documents also state the count of templates/tactics
   used to expand the root samples — or make clear that templates are excluded from the
   design entirely (an explicitly acceptable answer per the criterion).

**Strong positive signals:** counts reported as "N root prompts × M tactics/templates =
total"; a table separating base instances from generated variants; an explicit statement
that no templating/bulking was used; clear disclosure of how many distinct scenarios
underlie the headline prompt count.

**Negative / disqualifying signals:** only a single inflated total reported with no
breakdown into roots and templates; the multiplication by tactics hidden so coverage looks
broader than it is; the breakdown described only as future work; counts that conflate
bulked variants with distinct root samples.
