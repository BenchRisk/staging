# Mitigation 056 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #56, which mitigates Failure Mode #37.
Source: data/mitigations/56.mdx and data/modes/37.mdx.
-->

## The mitigation under review

- **Mitigation number:** 56
- **Mitigates failure mode:** #37 — *"User does not read disclaimers"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for conversational AI
  prominently displays a red-bordered disclaimer at the top of its report and executive
  summary stating that it only evaluates basic financial concepts and explicitly warns
  against using the tested systems for real investment advice without professional
  oversight. Despite this clear warning, a financial technology startup focuses solely on
  the performance metrics and implements the highest-scoring SUT as an automated
  investment advisor. The startup's technical team notices but dismisses the disclaimer,
  assuming their minor customizations will address the limitations. They market the system
  as "benchmark-validated" to clients who make significant investment decisions based on
  the AI's recommendations. When market conditions change unexpectedly, the system fails
  to properly assess risk factors it was never benchmarked for, resulting in substantial
  client losses and subsequent lawsuits.

**Criterion question (answer this for the benchmark under review):**
> Do you iteratively improve how disclaimers are displayed via UX research until users
> demonstrate understanding of the benchmark's limitations?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be understood
  by intended users, ensuring they can accurately interpret and use the benchmark for
  real-world decisions. It asks, "will the relying user understand the LLM properties as
  evidenced by the benchmark?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.
- **Reasonable Person:** An informed, rational, fair-minded user who is neither unusually
  sensitive nor malicious — used here to calibrate whether a typical user would actually
  notice and understand the benchmark's disclaimed limitations.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`disclaimers_present`** — Limitations/disclaimers are displayed with the benchmark
   results where users encounter them.
2. **`ux_research`** — The display of those disclaimers was studied with UX research (user
   testing, comprehension studies) rather than just authored and posted.
3. **`iterated_to_understanding`** — Presentation was iteratively improved until users
   demonstrably understood the limitations (an evidenced comprehension outcome, not just
   prominence).

**Strong positive signals:** reported user-comprehension testing of the
disclaimer/limitations display; described iterations to wording or placement driven by UX
findings; a stated comprehension criterion users had to meet; before/after evidence that
understanding improved.

**Negative / disqualifying signals:** a disclaimer that is merely present or "prominent"
with no evidence users understood it; no UX research on the presentation; comprehension
assumed rather than measured; UX iteration described only as a future plan.
