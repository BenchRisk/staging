# Mitigation 128 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #128, which mitigates Failure Mode #52.
Source: data/mitigations/128.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 128
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
> Is the design process for the test environment or prompts (e.g., how prompts are written
> and by whom) documented?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the context,
  task, or question the system is expected to respond to and are central to evaluating SUT
  performance in benchmarking.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`prompt_design_documented`** — The design process for the test environment or prompts
   is documented: how the prompts (or the evaluation environment) were written and
   constructed.
2. **`authorship_documented`** — It is documented by whom the prompts were written (e.g.,
   domain experts, crowdworkers, automated generation, the authors), so users can judge
   provenance and potential bias.

**Strong positive signals:** a section describing how prompts were authored, templated, or
generated; named roles/qualifications of prompt writers (e.g., domain experts vs.
crowdworkers); a described test-environment setup; a documented prompt-construction
methodology or guidelines used.

**Negative / disqualifying signals:** prompts are provided with no account of how or by
whom they were written; authorship and process left unstated; only sample prompts shown
with no methodology; the design process promised for a future version while the published
one omits it.
