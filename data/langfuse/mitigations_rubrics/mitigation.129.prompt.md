# Mitigation 129 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #129, which mitigates Failure Mode #52.
Source: data/mitigations/129.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 129
- **Mitigates failure mode:** #52 — *"Benchmark production failed to account for an
  idiosyncratic failure mode"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark developer failed to read a
  recent research paper listing common failure modes and potential mitigations. As a
  result, the benchmark authors fail to publish integrity requirements at the time their
  benchmark is published. Subsequently, a SUT developer trains to the benchmark's sample
  set and overperforms relative to its actual performance. Consequently, a user adopts
  what would ordinarily be known as a poor performing SUT.

**Criterion question (answer this for the benchmark under review):**
> Are the data sources and the data collection process explained?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`data_sources_explained`** — The data sources used to build the benchmark are
   explained (e.g., where the data came from, what corpora/origins, licensing or
   provenance).
2. **`collection_process_explained`** — The data collection process is explained — how the
   data was gathered, sampled, or assembled into the benchmark.

**Strong positive signals:** a "data sources" or "provenance" section naming origins; a
described collection or sampling procedure; a datasheet covering where and how the data was
obtained; stated inclusion/exclusion criteria for the collected data.

**Negative / disqualifying signals:** the dataset is shipped with no account of its
origins; collection methodology absent or vague ("scraped from the web" with no detail);
sources unattributed; the explanation promised for a future version while the published one
omits it.
