# Mitigation 010 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #10, which mitigates Failure Mode #7.
Source: data/mitigations/10.mdx and data/modes/7.mdx.
-->

## The mitigation under review

- **Mitigation number:** 10
- **Mitigates failure mode:** #7 — *"Singular prompts without a distributional tie lack a
  capacity for detecting distributional failings, harms, or impacts"*
- **Affected reliability dimension:** Comprehensiveness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~46.67% reduction in failure-mode likelihood; ~62.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark uses only a handful of
  standalone prompts to test bias in medical diagnosis advice. The prompts are about heart
  attack symptoms in middle-aged men. The SUT passes the test. However, when deployed, the
  SUT systematically fails to recognize heart attack symptoms in women and younger patients
  due to underrepresentation in training and evaluation data. The benchmark user deploys
  the model in a clinical triage assistant, and it contributes to misdiagnosis and delayed
  care for several patients outside the narrow demographic tested in the benchmark.

**Criterion question (answer this for the benchmark under review):**
> Do you disclose distributional limitations (e.g., that the benchmark does not provide
> information on distributional harms such as disparate impact) of the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Comprehensiveness:** The extent to which a benchmark fully represents or covers the
  range of inputs, use cases, or conditions relevant to the System Under Test (SUT) task,
  ensuring sufficient variability and representation. It asks, "will the relying user
  believe the benchmark covers something impacting their LLM decisions that is not
  covered?"
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances.
  An example includes resume screening software, which may disproportionately reject
  candidates from a poor state in favor of candidates from wealthy states. The ability to
  assess these distributional harms is contingent on having data with a distributional
  association (i.e., annotations supporting distributional evaluation).

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`distributional_limitations_disclosed`** — The documents explicitly disclose the
   benchmark's distributional limitations — e.g., that singular prompts without a
   distributional tie cannot detect distributional harms such as disparate impact.
2. **`user_facing`** — The disclosure appears where intended users encounter the benchmark
   (e.g., a limitations/intended-use section, README, or card), so a relying user is
   warned rather than having to infer the limitation.

**Strong positive signals:** an explicit limitations statement that the benchmark does not
measure distributional/disparate-impact harms; a caveat that prompts are singular and lack
distributional association; guidance that scores should not be read as evidence about
group-level or distributional behavior.

**Negative / disqualifying signals:** no acknowledgment of distributional limitations; the
benchmark implies broad coverage of harms it cannot actually detect; the caveat buried only
in code or absent from user-facing docs; the disclosure described only for a future
version.
