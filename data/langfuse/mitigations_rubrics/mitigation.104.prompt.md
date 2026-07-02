# Mitigation 104 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #104, which mitigates Failure Mode #47.
Source: data/mitigations/104.mdx and data/modes/47.mdx.
-->

## The mitigation under review

- **Mitigation number:** 104
- **Mitigates failure mode:** #47 — *"The benchmark does not measure a property of the SUT
  linked to the user task"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~76.67% reduction in failure-mode likelihood; ~0%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark rigorously evaluates the
  toxicity levels of a language model's responses, aiming to ensure it avoids generating
  hateful or offensive content. A user, however, is primarily concerned with whether the
  model exhibits kindness and empathy in its interactions, wanting it to provide supportive
  and understanding responses. They choose the model with the lowest toxicity score,
  assuming that a non-toxic model will automatically be kind and empathetic. However, they
  discover that the chosen model, while successfully avoiding harmful language, produces
  bland, emotionally neutral, and unhelpful responses that lack any genuine sense of care or
  consideration for the user's emotional state. The benchmark, by focusing solely on the
  absence of toxicity, failed to assess the positive qualities of kindness and empathy that
  were crucial for the user's desired application.

**Criterion question (answer this for the benchmark under review):**
> Are domain experts involved in the creation of the benchmark?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be understood
  by intended users, ensuring they can accurately interpret and use the benchmark for
  real-world decisions. It asks, "will the relying user understand the LLM properties as
  evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's parameters,
  requirements, and expectations, minimizing ambiguities that could lead to inconsistencies
  or errors.
- **Domain Expert:** An individual possessing specialized knowledge and skills in a
  particular area, leveraged to provide insights, guide data interpretation, and aid in
  decision-making. For a benchmark, a domain expert is someone who knows about the SUT's
  task (e.g., an ethicist for an ethics benchmark); a person need not have formal training
  where they have significant experience and knowledge within the domain.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`domain_experts_involved`** — The documents state that domain experts — people with
   specialized knowledge of the SUT's task — were involved in creating the benchmark.
2. **`involvement_described`** — The documents describe their involvement concretely enough
   to identify the relevant expertise and how it shaped the benchmark (e.g., who they were
   and which parts — task design, item authoring, label review — they contributed to).

**Strong positive signals:** named or described domain experts whose specialty matches the
benchmark's domain; a stated role for those experts in designing tasks, writing prompts, or
validating ground truth; an acknowledgments or methods section documenting expert
involvement; described expert review of items for domain validity.

**Negative / disqualifying signals:** no mention of domain experts, or only generic
non-expert contributors; experts named but with no described role in benchmark creation;
expert involvement promised only for a future version; reliance on people lacking
specialized knowledge of the benchmarked domain.
