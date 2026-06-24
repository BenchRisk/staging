# Mitigation 192 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #192, which mitigates Failure Mode #3.
Source: data/mitigations/192.mdx and data/modes/3.mdx.
-->

## The mitigation under review

- **Mitigation number:** 192
- **Mitigates failure mode:** #3 — *"Input prompt writers produce prompts with LLMs."*
- **Affected reliability dimension:** Correctness
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~50% reduction in failure-mode likelihood; ~33.33%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** All benchmark prompts are produced with
  the aid of Llama4 in the crowd-worker interface to improve their performance.
  Consequently, the prompts are biased to the word usage of Llama4 and it performs higher
  on the benchmark than it otherwise would. The benchmark user selects Llama4 even though
  it is not actually the best language model for what the benchmark is measuring.

**Criterion question (answer this for the benchmark under review):**
> Do you audit test set prompts for issues such as signs of undisclosed use of LLMs in
> their generation?

## Mitigation-specific glossary (adds to the shared glossary)

- **Correctness:** The property of a benchmark being free from significant errors that
  could mislead or bias outcomes. It asks, "could the benchmark results be systematically
  wrong (e.g., biased) in some way?"
- **Prompt:** An input provided to a SUT to elicit a response or behavior, typically but
  not exclusively in natural language, defining the context, task, or question the system
  is expected to respond to.
- **Canary Data:** Specially crafted benchmark data used to detect developer or
  evaluation practices likely to compromise the reliability of a benchmark, often planted
  deliberately to act as a warning signal (a "canary in a coal mine").

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`audit_performed`** — The documents describe an audit of the test-set prompts
   specifically aimed at detecting quality or provenance issues, including signs that
   prompts were generated with an LLM rather than written by the intended authors.
2. **`llm_generation_signals_checked`** — The audit explicitly looks for signs of
   undisclosed LLM use (e.g., detector tools, statistical/stylistic checks, manual review
   for model-typical phrasing), not merely a generic spell/grammar pass.
3. **`results_reported`** — Findings of the audit are reported for the currently
   published prompt set (e.g., what was checked, what was found, what was removed or
   corrected).

**Strong positive signals:** a described prompt-provenance or authenticity audit; use of
an AI-text detector or stylometric analysis on prompts; manual screening with documented
criteria for LLM-typical text; reported counts of prompts flagged, reviewed, or removed.

**Negative / disqualifying signals:** prompts taken as-is with no provenance audit; only
generic quality control (formatting, deduplication) with nothing aimed at LLM-origin
detection; an audit mentioned but no results reported; the audit described only as
planned for a future release.
