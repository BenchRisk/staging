# Mitigation 124 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #124, which mitigates Failure Mode #52.
Source: data/mitigations/124.mdx and data/modes/52.mdx.
-->

## The mitigation under review

- **Mitigation number:** 124
- **Mitigates failure mode:** #52 — *"Benchmark production failed to account for an
  idiosyncratic failure mode"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~43.33% reduction in failure-mode likelihood; ~4.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark developer failed to read a
  recent research paper listing common failure modes and potential mitigations. As a
  result, the benchmark authors fail to publish integrity requirements at the time their
  benchmark is published. Subsequently, a SUT developer trains to the benchmark's sample
  set and overperforms relative to its actual performance. Consequently, a user adopts
  what would ordinarily be known as a poor performing SUT.

**Criterion question (answer this for the benchmark under review):**
> Has the accompanying paper been accepted at a peer-reviewed venue, or is there a
> preprint version that is highly cited?

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
the documents show **at least one** of the following for the *currently published*
benchmark. Each id below is a `requirement` key in the output.

1. **`peer_reviewed`** — The accompanying paper has been accepted at a peer-reviewed
   venue (e.g., a named conference or journal with stated acceptance), establishing
   external scrutiny of the benchmark's design.
2. **`highly_cited_preprint`** — Alternatively, a preprint version exists and is highly
   cited (e.g., a venue/DOI/arXiv identifier with a substantial, documented citation
   count), indicating broad community vetting.

**Strong positive signals:** a stated acceptance at a named peer-reviewed venue
(conference/journal) with proceedings; a DOI or proceedings citation; a preprint with a
documented, substantial citation count from independent works.

**Negative / disqualifying signals:** no accompanying paper at all; an unreviewed
preprint with little or no citation; only a claim of "under review" or "to appear"; a
venue with no peer review (e.g., a workshop abstract with no scrutiny) presented as
equivalent.
