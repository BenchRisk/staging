# Mitigation 013 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #13, which mitigates Failure Mode #10.
Source: data/mitigations/13.mdx and data/modes/10.mdx.
-->

## The mitigation under review

- **Mitigation number:** 13
- **Mitigates failure mode:** #10 — *"Prompt perturbation bulking (increasing the number
  of prompts by making small changes to root prompts)"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~50.0% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark aimed at evaluating factual
  accuracy in historical QA uses 100 base prompts and generates 5,000 total prompts by
  slightly altering dates, names, or phrasing (e.g., changing "When did the Berlin Wall
  fall?" to "Can you tell me the year the Berlin Wall was taken down?"). While the quantity
  of prompts appears large, the semantic diversity is minimal and fails to cover the
  broader landscape of historical questions. A model optimized on this benchmark appears
  highly performant, but when users ask genuinely diverse or nuanced historical questions,
  it frequently hallucinates or misinterprets. The benchmark user integrates the model into
  an educational tool, leading to the dissemination of confidently stated misinformation.

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
- **Prompt Perturbation Bulking:** A technique to increase the number of prompts used in
  the production of a benchmark by making modifications to root prompts. It helps in
  evaluating how slight changes in wording, structure, or context can affect the outputs of
  a SUT, particularly in understanding model behavior and identifying vulnerabilities.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to generate
  variations, expansions, or perturbations in data-driven processes.
- **Template:** A root prompt from which structured changes facilitate interrogation of a
  SUT property subject to benchmark. Templates do not necessarily produce jailbreaks since
  they do not necessarily have an adversarial intent.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`root_sample_count_stated`** — The documents state sample counts in terms of *root
   samples* (the underlying base prompts before perturbation), so the reader sees the true
   unbulked size rather than only the perturbation-inflated total.
2. **`template_count_stated`** — The documents also state the count of
   templates/perturbations applied to the root samples — or make clear that templates are
   excluded from the design entirely (an explicitly acceptable answer per the criterion).

**Strong positive signals:** counts reported as "N root prompts expanded by perturbation to
total"; a table separating base prompts from perturbed variants; an explicit statement that
no perturbation/templating was used; clear disclosure of how many distinct prompts underlie
the headline count.

**Negative / disqualifying signals:** only a single inflated total reported with no
breakdown into roots and perturbations; perturbation bulking hidden so coverage looks
broader than it is; the breakdown described only as future work; counts that conflate
perturbed variants with distinct root samples.
