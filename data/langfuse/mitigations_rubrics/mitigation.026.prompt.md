# Mitigation 026 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #26, which mitigates Failure Mode #22.
Source: data/mitigations/26.mdx and data/modes/22.mdx.
-->

## The mitigation under review

- **Mitigation number:** 26
- **Mitigates failure mode:** #22 — *"Distribution of SUT inputs within the real world
  are substantially different in distribution from those within the benchmark (e.g., SUT
  users ask different questions from those posed by the benchmark authors)."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (3) Prompt Inferencing
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark is designed by academic
  researchers to test a model's ability to answer philosophical, scientific, and
  analytical questions with precise factual grounding. However, in a commercial
  deployment—such as a virtual assistant—users primarily ask casual, personal, or
  goal-directed questions (e.g., "What should I wear today?" or "Can you draft a message
  to my boss?") that differ drastically in tone, content, and structure from the
  benchmark prompts. As a result, the model excels in benchmark evaluations but performs
  poorly in production. The benchmark user misinterprets the high benchmark scores as a
  signal of general utility and deploys the system in an environment where it routinely
  fails to meet user expectations.

**Criterion question (answer this for the benchmark under review):**
> Do you perform a characteristic analysis comparing prompts collected from a production
> system to those in your test set, and do you publicly disclose any significant
> variations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt Inferencing:** The stage during which prompts are delivered to the system
  under test (SUT), ensuring conditions for testing accurately reflect intended
  operational contexts.
- **Distributional Association:** A property of prompt collections desirable for
  benchmarking properties expressed in distribution rather than in individual instances;
  assessing such properties is contingent on having data with a distributional
  association.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`characteristic_analysis`** — The documents describe a characteristic analysis that
   compares prompts collected from a real production system against the benchmark's test
   set (e.g., distribution of topics, tone, structure, length).
2. **`variations_disclosed`** — Any significant variations found between the production
   distribution and the test set are publicly disclosed to users.

**Strong positive signals:** a reported comparison of production prompts vs. test
prompts (distributions, examples, statistics); a section describing how the test set
matches or diverges from real usage; published findings of distribution gaps with caveats
for users; a methodology citing a real-world prompt sample as the comparison baseline.

**Negative / disqualifying signals:** no comparison to production/real-world prompts; the
test set assumed representative without analysis; an internal analysis whose results are
not disclosed publicly; the comparison promised but absent from the current release; only
author-generated prompts with no production reference.
