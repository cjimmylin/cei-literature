---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0212
type: conferencePaper
short_title: SG-Bench -- Evaluating LLM Safety Generalization
year: 2024
first_author: "[[M. Tom]]"
authors: Tom, M., et al
url: "https://arxiv.org/abs/2410.21965"
external_pdf: "https://arxiv.org/pdf/2410.21965.pdf"
local_pdf: "[[PDFs/2024/2024-Tom-SG-Bench - Evaluating LLM Safety Generalization.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Tom-SG-Bench - Evaluating LLM Safety Generalization.md"
publication: NeurIPS 2024
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
is_dataset: "No"
tags: 
abstract: "Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# SG-Bench -- Evaluating LLM Safety Generalization

## Authors

[[Tom, M., et al]]

## Metadata

**Authors:** Tom, M., et al

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2410.21965
- **Code/Data:** https://github.com/MurrayTom/SG-Bench

## Abstract

Ensuring the safety of large language model (LLM) applications is essential for developing trustworthy artificial intelligence. Current LLM safety benchmarks have two limitations. First, they focus solely on either discriminative or generative evaluation paradigms while ignoring their interconnection. Second, they rely on standardized inputs, overlooking the effects of widespread prompting techniques, such as system prompts, few-shot demonstrations, and chain-of-thought prompting. To overcome these issues, we developed SG-Bench, a novel benchmark to assess the generalization of LLM safety across various tasks and prompt types. This benchmark integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak on LLM safety. Our assessment of 3 advanced proprietary LLMs and 10 opensource LLMs with the benchmark reveals that most LLMs perform worse on discriminative tasks than generative ones, and are highly susceptible to prompts, indicating poor generalization in safety alignment. We also explain these findings quantitatively and qualitatively to provide insights for future research.2 Warning: this paper includes examples that may be offensive or harmful.

## Dataset Information

Entries sampled from AdvBench, HarmfulQA, BeaverTails, SaladBench

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4, Agent 16
**Implementation Readiness:** HIGH

## Tags

