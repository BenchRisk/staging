# Mitigation 130 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #130, which mitigates Failure Mode #52.
Source: data/mitigations/130.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 130
- **Mitigates failure mode:** #52 — *"Benchmark production failed to account for an
  idiosyncratic failure mode"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark developer failed to read a
  recent research paper listing common failure modes and potential mitigations. As a
  result, the benchmark authors fail to publish integrity requirements at the time their
  benchmark is published. Subsequently, a SUT developer trains to the benchmark's sample
  set and overperforms relative to its actual performance. Consequently, a user adopts
  what would ordinarily be known as a poor performing SUT.

**Criterion question (answer this for the benchmark under review):**
> Are any data preprocessing steps described or found to be non-relevant to benchmark
> users?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **at least one** of the following for the *currently published*
benchmark. Each id below is a `requirement` key in the output.

1. **`preprocessing_described`** — Any data preprocessing steps applied to the benchmark
   data are described (e.g., cleaning, filtering, normalization, deduplication,
   formatting), so users can understand how the raw data was transformed.
2. **`preprocessing_non_relevant`** — Alternatively, the documents establish that no
   preprocessing steps are relevant to benchmark users (e.g., data used as-is, or any
   preprocessing has no bearing on interpretation), making the description unnecessary.

**Strong positive signals:** a "preprocessing" or "data preparation" section listing each
transformation; described cleaning/filtering/deduplication choices; an explicit statement
that the data was used unmodified or that preprocessing does not affect interpretation.

**Negative / disqualifying signals:** preprocessing clearly occurred but is undescribed and
its relevance is left unaddressed; opaque transformations affecting results with no
account; the description promised for a future version while the published one omits it.
