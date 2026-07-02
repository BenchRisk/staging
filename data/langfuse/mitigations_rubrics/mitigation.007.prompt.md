# Mitigation 007 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #7, which mitigates Failure Mode #5.
Source: data/mitigations/7.mdx and data/modes/5.mdx.
-->

## The mitigation under review

- **Mitigation number:** 7
- **Mitigates failure mode:** #5 — *"Data vendor licenses private data that is available
  to other parties"*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~56.67% reduction in failure-mode likelihood; ~29.17%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A third-party vendor licenses a set of
  complex reasoning prompts without ensuring they are the sole organization with a right to
  license the data. As a result, the SUTs may have separately licensed the exact benchmark
  prompts during training or evaluation, inflating their performance and compromising the
  benchmark's validity as a measure of generalization or real-world capability. The
  benchmark user adopts the LLM whose developers also licensed the data despite it having
  poor generalization performance.

**Criterion question (answer this for the benchmark under review):**
> Do you prohibit data vendors from re-licensing to you any data that they originally
> licensed from a third party?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`relicensing_prohibited`** — The documents describe a prohibition preventing data
   vendors from re-licensing to the benchmark any data that the vendor had itself
   originally licensed from a third party.
2. **`contractual`** — The prohibition takes the form of a contractual or agreement-level
   obligation on the vendor, not merely an informal expectation or hope.

**Strong positive signals:** quoted vendor-agreement language barring pass-through or
third-party-originated data; a stated requirement that vendors warrant the data is their
own and not sub-licensed from elsewhere; a procurement clause requiring sole-source/origin
attestation from the vendor.

**Negative / disqualifying signals:** no restriction on the provenance of vendor-supplied
data; vendor relationships described without any re-licensing safeguard; the safeguard
described only as a preference or as future contracting; data acquired from vendors with no
provenance warranties.
