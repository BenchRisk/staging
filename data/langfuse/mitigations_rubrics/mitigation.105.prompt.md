# Mitigation 105 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #105, which mitigates Failure Mode #47.
Source: data/mitigations/105.mdx and data/modes/47.mdx.
-->

## The mitigation under review

- **Mitigation number:** 105
- **Mitigates failure mode:** #47 — *"The benchmark does not measure a property of the
  SUT linked to the user task."*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~60% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark rigorously evaluates the
  toxicity levels of a language model's responses, aiming to ensure it avoids generating
  hateful or offensive content. A user, however, is primarily concerned with whether the
  model exhibits kindness and empathy, wanting supportive and understanding responses.
  They choose the model with the lowest toxicity score, assuming a non-toxic model will
  automatically be kind and empathetic. They discover the chosen model, while avoiding
  harmful language, produces bland, emotionally neutral, unhelpful responses that lack any
  genuine sense of care. By focusing solely on the absence of toxicity, the benchmark
  failed to assess the kindness and empathy that were crucial for the user's application.

**Criterion question (answer this for the benchmark under review):**
> Do you integrate relevant domain literature into the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be
  understood by intended users, ensuring they can accurately interpret and use the
  benchmark for real-world decisions. It asks, "will the relying user understand the LLM
  properties as evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's
  parameters, requirements, and expectations, minimizing ambiguities that could lead to
  inconsistencies or errors.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area or industry, often leveraged to provide insights, guide data
  interpretation, and aid decision-making. For benchmarks, a domain expert is someone who
  knows about the SUT's task (e.g., ethicists for an ethics benchmark, social engineering
  specialists for security benchmarks). To be a domain expert, a person need not have
  formal training if they have significant experience and knowledge within the domain.
- **Normative Properties:** Characteristics, standards, or criteria that define what is
  considered acceptable, desirable, or expected within a particular context or domain.
  These properties guide behavior, decision-making, and evaluations.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`literature_cited`** — The benchmark documents cite or reference specific domain
   literature (peer-reviewed work, standards, regulatory guidance, prior art) relevant to
   the property being measured, not just generic ML/benchmarking references.
2. **`integrated_into_design`** — The cited literature visibly informs the benchmark's
   construction — its task definition, taxonomy, scoring criteria, or item selection are
   grounded in that literature, rather than being merely listed in a related-work section.

**Strong positive signals:** a section grounding the measured property in domain
scholarship or standards; a taxonomy/rubric explicitly derived from cited sources;
involvement of domain experts in defining what the benchmark measures; citations tied to
specific design choices ("we operationalize construct X following [ref]").

**Negative / disqualifying signals:** no citations beyond ML tooling; a related-work
section that does not connect to the actual measurement; the measured property defined
purely by author intuition or convenience; relevant established domain literature on the
construct is conspicuously ignored.
