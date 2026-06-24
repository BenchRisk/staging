# Mitigation 103 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #103, which mitigates Failure Mode #47.
Source: data/mitigations/103.mdx and data/modes/47.mdx.
-->

## The mitigation under review

- **Mitigation number:** 103
- **Mitigates failure mode:** #47 — *"The benchmark does not measure a property of the SUT
  linked to the user task"*
- **Affected reliability dimension:** Intelligibility
- **Benchmark production stage:** (1) Task Definition
- **Risk reduction if adopted:** ~70% reduction in failure-mode likelihood; ~29.17%
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
> Do you describe how the tested capability or concept is translated into the benchmarked
> task?

## Mitigation-specific glossary (adds to the shared glossary)

- **Intelligibility:** The clarity and ease with which benchmark results can be understood
  by intended users, ensuring they can accurately interpret and use the benchmark for
  real-world decisions. It asks, "will the relying user understand the LLM properties as
  evidenced by the benchmark?"
- **Task Definition:** The explicit and detailed specification of a SUT Task's parameters,
  requirements, and expectations, minimizing ambiguities that could lead to inconsistencies
  or errors.
- **Subtask:** A narrowly defined System Under Test (SUT) Task within a broader collection
  of benchmarked tasks. Subtasks isolate specific capabilities or dimensions that
  contribute to overall benchmark performance and improve the interpretability of results.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`capability_named`** — The documents identify the capability or concept the benchmark
   intends to measure.
2. **`translation_described`** — The documents describe how that capability or concept is
   translated into the concrete benchmarked task (the mapping from the abstract property to
   the prompts/items and scoring that operationalize it).

**Strong positive signals:** a "construct" or "what we measure" section linking the target
capability to the task design; an explicit rationale for why the chosen items operationalize
the concept; a described mapping from concept → subtasks → scored items; worked examples
illustrating the capability-to-task translation.

**Negative / disqualifying signals:** only the task mechanics described with no link to the
underlying capability; the intended property named but not connected to how it is measured;
the reader must infer the construct-to-task mapping themselves; the explanation present only
for a future version while the published benchmark omits it.
