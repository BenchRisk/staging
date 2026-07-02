# Mitigation 018 — Rubric Component

<!--
COMPONENT 2 of 2 — MITIGATION-SPECIFIC. Fills the {{mitigation_rubric}} slot of
shared.prompt.md (Component 1). On its own this file is not a complete prompt; the
shared component supplies the role, universal glossary, verdict scale, rules, input
variables, and output schema.

Assesses BenchRisk Mitigation #18, which mitigates Failure Mode #15.
Source: data/mitigations/18.mdx and data/modes/15.mdx.
-->

## The mitigation under review

- **Mitigation number:** 18
- **Mitigates failure mode:** #15 — *"Prompts have known properties allowing for
  achieving an unrealistic (i.e., non-generalizing) performance. For example, prompts are
  of particular and known lengths."*
- **Affected reliability dimension:** Longevity
- **Benchmark production stage:** (2) Prompt Generation
- **Risk reduction if adopted:** ~60.0% reduction in failure-mode likelihood; ~16.67%
  reduction in severity (context only — do not let these numbers change your verdict).
- **Example realization of the failure mode:** A benchmark testing whether code
  generation models detect instructions for generating malware uses prompts that are
  consistently of a particular length, averaging 10 lines of code for malware and 8 lines
  of code for non-malicious code. The model performs well on this benchmark, as it has
  been explicitly optimized to have a higher prior belief of malware for 10 lines of code
  vs 8 lines of code. However, the difference in length is solely a statistical artifact
  of the evaluation and not representative of the actual performance. A benchmark user,
  assuming the model's high score represents its ability to prevent malware generation,
  deploys it in a real-world software development environment. The model then generates
  more malware than would otherwise have been generated.

**Criterion question (answer this for the benchmark under review):**
> Do you avoid releasing a representative sample of prompts to SUT developers?

## Mitigation-specific glossary (adds to the shared glossary)

- **Longevity:** The ability of a benchmark to maintain its correctness,
  comprehensiveness, consistency, and intelligibility through time subject to gaming or
  changing circumstances. It asks, "does the benchmark become less reliable through
  time?"
- **Prompt:** An input provided to a System Under Test (SUT) to elicit a response or
  behavior, typically but not exclusively in natural language. Prompts define the
  context, task, or question the system is expected to respond to and are central to
  evaluating SUT performance.
- **Root Prompts:** An initial set of foundational, seed, or base prompts used to
  generate variations, expansions, or perturbations in data-driven processes.

## What counts as evidence the mitigation is in place

The evidence indicates the developer would likely assert the mitigation is in place when
the documents show **all** of the following for the *currently published* benchmark.
Each id below is a `requirement` key in the output.

1. **`sample_withheld`** — The benchmark does **not** release to SUT developers a sample
   of prompts that is representative of the evaluation set — i.e., no published example
   set discloses the prompts' characteristic properties (such as length, structure, or
   format) that a developer could optimize against.
2. **`properties_protected`** — Where any examples are shown for illustration, the
   documents indicate the disclosed examples do not reveal the distinguishing statistical
   properties of the live prompts (e.g., lengths, templates) that would enable gaming.

**Strong positive signals:** an explicit statement that example/sample prompts are
withheld or held out; a private or held-out evaluation set with no representative public
sample; a note that only non-representative or deliberately atypical illustrations are
shared; documentation that prompt-length and other format properties are randomized or
not disclosed.

**Negative / disqualifying signals:** a full or representative sample of prompts is
published (in the paper, repo, or dataset card); released examples that match the live
set's length/format distribution; statements that developers may inspect example prompts
to understand the format; a public dataset whose sampled subset mirrors the test set's
characteristics.
