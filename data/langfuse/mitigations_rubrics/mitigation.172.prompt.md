# Mitigation 172 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #172, which mitigates Failure Mode #57.
Source: data/mitigations/172.mdx and data/modes/57.mdx.
-->

## The mitigation under review

- **Mitigation number:** 172
- **Mitigates failure mode:** #57 — *"Benchmark authors do not know how to propagate
  statistical uncertainty into a user presentation"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (6) Grade Presentation
- **Risk reduction if adopted:** ~66.67% reduction in failure-mode likelihood; ~20.83%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark reports the performance of
  several language models on a reading comprehension task, providing only single-point
  accuracy scores (e.g., Model A: 85%, Model B: 83%). However, the benchmark authors do
  not know how to conduct sufficient evaluations to determine the statistical significance
  of this 2% difference, nor do they present any confidence intervals or other measures of
  uncertainty. A user looking for the most reliable model might incorrectly assume that
  Model A is definitively superior to Model B. In reality, the observed difference could
  be due to random sampling variation, and with more data, the performance of the two
  models might be statistically indistinguishable. The user, lacking information about the
  uncertainty in the benchmark results, makes a potentially suboptimal decision based on a
  seemingly precise but statistically unreliable comparison.

**Criterion question (answer this for the benchmark under review):**
> Does at least one benchmark author have formal training in statistical methods?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Grade Presentation:** The visual representation of benchmark results, scores, or
  grades.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`author_with_statistical_training`** — The documents indicate that at least one
   benchmark author has formal training in statistical methods (e.g., stated
   credentials/affiliation in statistics, or demonstrated through sound statistical
   treatment such as reported confidence intervals or significance testing).

**Strong positive signals:** an author bio/affiliation indicating formal statistics
training; reported uncertainty measures (confidence intervals, error bars, significance
tests) consistent with statistical expertise; an acknowledged statistician contributor.

**Negative / disqualifying signals:** results presented as single-point scores with no
uncertainty and no indication of statistical expertise; no author background information
that would establish formal statistical training; statistical rigor promised for a future
release while the current presentation lacks it.
