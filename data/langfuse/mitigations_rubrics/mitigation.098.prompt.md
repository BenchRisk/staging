# Mitigation 098 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #98, which mitigates Failure Mode #31.
Source: data/mitigations/98.mdx and data/modes/31.mdx.
-->

## The mitigation under review

- **Mitigation number:** 98
- **Mitigates failure mode:** #31 — *"Evaluator(s) perform poorly across all SUTs"*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (4) Output Evaluation
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~37.5%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark employs undergraduate psychology
  students with no technical background to evaluate advanced AI reasoning on complex
  mathematical proofs. These evaluators cannot distinguish between correct proofs and those
  with subtle errors, giving high scores to any response that looks sophisticated
  regardless of accuracy. As a result, all tested systems receive similarly high scores
  despite vast differences in actual mathematical reasoning capabilities. The benchmark user
  selects the cheapest SUT thinking it performs equivalently to premium options, then
  deploys it to verify critical engineering calculations for a bridge design, resulting in
  structural flaws being missed and necessitating costly redesigns when discovered by other
  verification methods.

**Criterion question (answer this for the benchmark under review):**
> Is the system-under-test required to produce outputs that conform to the evaluator's
> expected format (e.g., true/false, multiple choice)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Evaluator:** A tool, algorithm, model, framework, or human checking the output of the
  System Under Test (SUT) for correctness, safety, or some other measurable property.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights, guide data interpretation, and aid in
  decision-making. For a benchmark, a domain expert is someone who knows about the SUT's
  task (e.g., a mathematician for mathematical reasoning), not a person lacking specialized
  knowledge in the domain.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`constrained_output_format`** — The SUT is required to produce outputs in a
   constrained format the evaluator expects (e.g., true/false, multiple choice, a fixed
   structure), so scoring does not depend on weak evaluator judgment of free text.
2. **`format_enforced_in_scoring`** — The expected format is enforced at evaluation time
   (e.g., prompts request the format and scoring parses/expects it), not merely suggested.

**Strong positive signals:** prompts that instruct the SUT to answer with A/B/C/D,
true/false, or a fixed schema; an answer-extraction or parsing step keyed to the required
format; documentation stating only the constrained format is scored; example items showing
the enforced response form.

**Negative / disqualifying signals:** free-form responses graded subjectively by evaluators
of uncertain competence; no required output format described; format conformance optional
or only encouraged; the constrained-format requirement described only for a planned version
while the current benchmark scores free text.
