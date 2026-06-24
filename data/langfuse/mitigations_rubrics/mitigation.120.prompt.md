# Mitigation 120 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #120, which mitigates Failure Mode #51.
Source: data/mitigations/120.mdx and data/modes/51.mdx.
-->

## The mitigation under review

- **Mitigation number:** 120
- **Mitigates failure mode:** #51 — *"SUT developers are not bound to adhere to benchmark
  integrity requirements"*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (7) Upkeep
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark for evaluating the safety of
  language models prohibits the use of external knowledge during evaluation to ensure the
  model's responses are based solely on its training data. However, the developers of
  "GuardianAI," while submitting their model to the benchmark, secretly implement a
  retrieval mechanism that allows the model to access and incorporate real-time
  information from the internet during the evaluation process. This circumvents the
  benchmark's intended constraints and leads to inflated safety scores. A user, trusting
  the benchmark's results, selects GuardianAI believing it has robust internal safety
  mechanisms, only to discover in real-world use that it can still generate harmful
  content when disconnected from external resources or when faced with novel prompts not
  covered by its retrieval strategy.

**Criterion question (answer this for the benchmark under review):**
> Are the release requirements such as the practices and norms required to be followed by
> the SUT developer specified publicly?

## Mitigation-specific glossary (adds to the shared glossary)

- **Benchmark Integrity Requirements:** The standards and guidelines that ensure the
  reliability, validity, and fairness of the evaluation process for systems under test
  (SUTs), designed to maintain the trustworthiness of benchmarks. Key components may
  include transparency, consistency, reproducibility, accountability, comprehensiveness,
  independence, ethical compliance, and update mechanisms.
- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Upkeep:** The ongoing maintenance and revision processes required to sustain
  benchmark reliability, including adjustments for evolving requirements, guarding
  against data leakage, and maintaining consistency of evaluation conditions.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`requirements_exist`** — The benchmark defines release requirements: the practices
   and norms a SUT developer must follow when submitting to or being scored by the
   benchmark (e.g., no training on the test set, no external retrieval, allowed
   configurations, submission protocol).
2. **`specified_publicly`** — Those requirements are stated publicly where submitting
   developers and relying users can find them (e.g., README, submission guidelines,
   benchmark/leaderboard policy page), not held privately or implied.

**Strong positive signals:** a published "rules," "submission guidelines," or "integrity
policy" section enumerating what SUT developers may and may not do; explicit constraints
(e.g., "no fine-tuning on the test split," "no internet access during evaluation"); a
public code of conduct or terms for leaderboard participation.

**Negative / disqualifying signals:** no statement of any participation rules or norms;
requirements that exist only privately or by invitation; only a vague "use responsibly"
note with no concrete practices; rules described as forthcoming for a future release while
the published benchmark has none.
