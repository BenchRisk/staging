# Mitigation 019 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #19, which mitigates Failure Mode #16.
Source: data/mitigations/19.mdx and data/modes/16.mdx.
-->

## The mitigation under review

- **Mitigation number:** 19
- **Mitigates failure mode:** #16 — *"An inadequate number of prompts are produced to
  identify rare critical events (i.e., tail risks)."*
- **Affected reliability dimension:** Consistency
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~0.0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark designed to evaluate a
  model's ability to detect financial fraud runs 500 prompts, including several fraud
  scenarios that must be detected with very high probability, such as coordinated
  international money laundering. However, the number of prompts focusing on these rare,
  high-impact events is too small to reliably determine when a system drops below the
  required 99.9 percent detection rate. As a result, most models pass the benchmark with
  a high score. The benchmark user assumes a passing model meets requirements and deploys
  it, overlooking the fact that the benchmark may not detect coordinated money laundering
  at a sufficient rate.

**Criterion question (answer this for the benchmark under review):**
> Do you calibrate your prompt sample count to a statistical analysis indicating the
> number of samples required to identify the probability of rare events?

## Mitigation-specific glossary (adds to the shared glossary)

- **Consistency:** The degree to which a benchmark score is not subject to random noise
  (e.g., variability arising from probabilistic sampling). It asks, "does the score have
  unreasonably high variance?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the
  context, task, or question the system is expected to respond to and are central to
  evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`statistical_analysis`** — The documents describe a statistical analysis (e.g.,
   power analysis, confidence-interval or detection-rate calculation) that determines how
   many prompts are required to reliably identify the probability of the rare/tail events
   the benchmark targets.
2. **`sample_count_calibrated`** — The benchmark's actual prompt sample count is set to,
   or justified by, that analysis — i.e., the number of prompts (especially for rare
   events) is chosen because the analysis showed it is sufficient.

**Strong positive signals:** a reported power/sample-size analysis tied to a target
detection rate or false-negative rate for rare events; confidence intervals or minimum
detectable effect calculations for tail-risk categories; an explicit justification that
the prompt count was sized to detect events at a stated probability; per-category counts
selected from the statistical requirement.

**Negative / disqualifying signals:** a prompt count given with no statistical
justification; rare-event categories represented by a handful of prompts with no power
analysis; "we used N prompts" stated without reference to detection probability;
sample-size reasoning promised for a future release but absent from the current one.
