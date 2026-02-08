---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0253
type: preprint
short_title: "VAL-Bench: Belief Consistency as a Measure for Value Alignment"
year: 2025
first_author: "[[A. Gupta]]"
authors: Gupta, A. et al.
url: "https://arxiv.org/abs/2510.05465"
external_pdf: "https://arxiv.org/pdf/2510.05465.pdf"
local_pdf: "[[PDFs/2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment.pdf]]"
pdf_extract: "PDF Extracts/2025-Gupta-VAL-Bench Belief Consistency as a Measure for Value Alignment.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large language models (LLMs) are increasingly being used for tasks where outputs shape human decisions, so it is critical to verify that their responses consistently reflect desired human values. Humans, as individuals or groups, don’t agree on a universal set of values, which makes evaluating value alignment difficult. Existing benchmarks often use hypothetical or commonsensical situations, which don’t capture the complexity and ambiguity of real-life debates."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# VAL-Bench: Belief Consistency as a Measure for Value Alignment

## Authors

[[Gupta, A. et al.]]

## Metadata

**Authors:** Gupta, A. et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.05465

## Abstract

Large language models (LLMs) are increasingly being used for tasks where outputs shape human decisions, so it is critical to verify that their responses consistently reflect desired human values. Humans, as individuals or groups, don’t agree on a universal set of values, which makes evaluating value alignment difficult. Existing benchmarks often use hypothetical or commonsensical situations, which don’t capture the complexity and ambiguity of real-life debates. We introduce the Value ALignment Benchmark (VAL-Bench1), which measures the consistency in language model belief expressions in response to real-life valueladen prompts. VAL-Bench consists of 115K pairs of prompts designed to elicit opposing stances on a controversial issue, extracted from Wikipedia. We use an LLM-as-a-judge, validated against human annotations, to evaluate if the pair of responses consistently expresses either a neutral or a specific stance on the issue. Applied across leading open- and closed-source models, the benchmark shows considerable variation in consistency rates (ranging from ∼10% to ∼80%), with Claude models the only ones to achieve high levels of consistency. Lack of consistency in this manner risks epistemic harm by making user beliefs dependent on how questions are framed rather than on underlying evidence, and undermines LLM reliability in trust-critical applications. Therefore, we stress the importance of research towards training belief consistency in modern LLMs. By providing a scalable, reproducible benchmark, VAL-Bench enables systematic measurement of necessary conditions for value alignment.

## Dataset Information

115K pairs of prompts from Wikipedia eliciting opposing stances on controversial issues

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

