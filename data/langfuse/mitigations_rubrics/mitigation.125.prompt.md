# Mitigation 125 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #125, which mitigates Failure Mode #52.
Source: data/mitigations/125.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 125
- **Mitigates failure mode:** #52 — *"Benchmark production failed to account for an
  idiosyncratic failure mode"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark developer failed to read a
  recent research paper listing common failure modes and potential mitigations. As a
  result, the benchmark authors fail to publish integrity requirements at the time their
  benchmark is published. Subsequently, a SUT developer trains to the benchmark's sample
  set and overperforms relative to its actual performance. Consequently, a user adopts
  what would ordinarily be known as a poor performing SUT.

**Criterion question (answer this for the benchmark under review):**
> Is the benchmark design process documented?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Idiosyncratic Failure Mode:** A unique or unusual type of failure that occurs in a
  specific benchmark, which may not be present in other benchmarks. These failure modes
  are often influenced by particular characteristics of the benchmarking methodology,
  such as its design, implementation, or the data.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`design_process_documented`** — The benchmark's design process is documented: how
   the benchmark was conceived and constructed, including the decisions, methodology, and
   rationale that shaped it (not just the final artifact).

**Strong positive signals:** a methodology or "how we built this" section describing
design decisions and their rationale; a documented set of design choices, scope decisions,
and tradeoffs; a datasheet or methods section walking through the construction process.

**Negative / disqualifying signals:** only the finished benchmark is published with no
account of how it was designed; design rationale is absent or left implicit; the process
is described only for a future version while the published one omits it.
