# Mitigation 131 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #131, which mitigates Failure Mode #52.
Source: data/mitigations/131.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 131
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
> Are any data annotation steps described or found to be non-relevant to benchmark users?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Interrater Reliability:** The degree of agreement or consistency among multiple
  independent evaluators (raters) when assessing the same set of outputs, tasks, or
  behaviors. High interrater reliability indicates the evaluation criteria are
  well-defined, interpretable, and applied consistently.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **at least one** of the following for the *currently published*
benchmark. Each id below is a `requirement` key in the output.

1. **`annotation_described`** — Any data annotation steps are described (e.g., who
   annotated the data, the labeling guidelines used, the annotation procedure, and any
   agreement/quality measures such as interrater reliability).
2. **`annotation_non_relevant`** — Alternatively, the documents establish that no
   annotation steps are relevant to benchmark users (e.g., the data carries no annotations,
   or any labeling has no bearing on interpretation), making the description unnecessary.

**Strong positive signals:** an "annotation" or "labeling" section describing annotators,
guidelines, and process; reported annotator qualifications or training; reported
agreement/quality measures (e.g., interrater reliability); an explicit statement that the
data is unannotated or that annotation does not affect interpretation.

**Negative / disqualifying signals:** the benchmark clearly relies on human labels but the
annotation process is undescribed and its relevance unaddressed; labels with no account of
who produced them or how; the description promised for a future version while the published
one omits it.
