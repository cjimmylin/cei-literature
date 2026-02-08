---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0032
type: conferencePaper
short_title: CASE-Bench (Context-Aware SafEty Benchmark)
year: 2025
first_author: "[[G. Sun]]"
authors: "Sun, G., Zhan, X., Feng, S., Woodland, P. C., & Such, J"
url: "https://arxiv.org/abs/2501.14940"
external_pdf: "https://arxiv.org/pdf/2501.14940.pdf"
local_pdf: "[[PDFs/2025-Sun-CASE-Bench Context-Aware SafEty Benchmark.pdf]]"
pdf_extract: "PDF Extracts/2025-Sun-CASE-Bench Context-Aware SafEty Benchmark.md"
publication: ICML 2025
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual problematic queries, which overlooks the importance of the context where the query occurs and may cause undesired refusal of queries under safe contexts that diminish user experience. Addressing this gap, we introduce CASE-Bench, a Context-Aware SafEty Benchmark that integrates context into safety..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# CASE-Bench (Context-Aware SafEty Benchmark)

## Authors

[[Sun, G., Zhan, X., Feng, S., Woodland, P. C., & Such, J]]

## Metadata

**Authors:** Sun, G., Zhan, X., Feng, S., Woodland, P. C., & Such, J

**Year:** 2025

**Type:** conferencePaper

**Venue:** ICML 2025

## Links

- **arXiv:** https://arxiv.org/abs/2501.14940
- **Code/Data:** https://github.com/BriansIDP/CASEBench

## Abstract

Aligning large language models (LLMs) with human values is essential for their safe deployment and widespread adoption. Current LLM safety benchmarks often focus solely on the refusal of individual problematic queries, which overlooks the importance of the context where the query occurs and may cause undesired refusal of queries under safe contexts that diminish user experience. Addressing this gap, we introduce CASE-Bench, a Context-Aware SafEty Benchmark that integrates context into safety assessments of LLMs. CASE-Bench assigns distinct, formally described contexts to categorized queries based on Contextual Integrity theory. Additionally, in contrast to previous studies which mainly rely on majority voting from just a few annotators, we recruited a sufficient number of annotators necessary to ensure the detection of statistically significant differences among the experimental conditions based on power analysis. Our extensive analysis using CASE-Bench on various open-source and commercial LLMs reveals a substantial and significant influence of context on human judgments (p <0.0001 from a z-test), underscoring the necessity of context in safety evaluations. We also identify notable mismatches between human judgments and LLM responses, particularly in commercial models within safe contexts.1 Code and data used in the paper are available at https://github.com/BriansIDP/CASEBench.

## Dataset Information

Size: 900 query-context pairs (450 queries x 2 contexts each)

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 5
**Implementation Readiness:** HIGH

## Tags

