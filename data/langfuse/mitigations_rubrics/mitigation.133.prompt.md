# Mitigation 133 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #133, which mitigates Failure Mode #53.
Source: data/mitigations/133.mdx and data/modes/53.mdx.
-->

## The mitigation under review

- **Mitigation number:** 133
- **Mitigates failure mode:** #53 — *"Linkage between the evaluation prompts and the
  information the prompts are meant to supply via the benchmark is not well understood by
  the benchmark user"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~63.33% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A user is examining a collection of
  example benchmark prompts to help them understand the benchmark. Through this process
  the benchmark user comes to misunderstand the scope of a safety benchmark, which
  establishes the scope of coverage (e.g., should it answer a medical question?) and not
  whether the medical question is correct. Consequently, a user believes the benchmark
  covers something that it does not.

**Criterion question (answer this for the benchmark under review):**
> Is the representativeness of the data explained (e.g., are the demographics of crowd
> workers collected and reported)?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area or industry, leveraged to provide insights, guide data interpretation,
  and aid in decision-making. For benchmarks, a domain expert is someone who knows about
  the SUT's task (e.g., ethicists for an ethics benchmark, a speaker of a low-resource
  language for translation).
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically in natural language. Prompts define the context, task, or question
  the system is expected to respond to and are central to evaluating SUT performance.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`representativeness_explained`** — The documents explain how representative the
   benchmark data is of the intended task or population, characterizing what the prompts
   and their sources do and do not cover.
2. **`source_composition_reported`** — The composition of the data is reported (e.g., the
   demographics of crowd workers, annotator backgrounds, source distributions, or other
   provenance that bears on representativeness), not merely asserted to exist.

**Strong positive signals:** a dataset card / datasheet section on data composition and
representativeness; reported demographics or backgrounds of crowd workers, authors, or
annotators; an explicit statement of what population, languages, or contexts the prompts
represent and which they do not; provenance and sampling methodology tied to coverage
claims.

**Negative / disqualifying signals:** prompts presented with no account of who produced
them or what they represent; representativeness merely asserted ("diverse", "broad")
without supporting composition data; demographics or source distributions absent;
representativeness discussed only as future work or in an external link with no detail
in the published materials.
