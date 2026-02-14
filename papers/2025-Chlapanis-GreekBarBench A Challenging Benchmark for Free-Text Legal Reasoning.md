---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0531
type: preprint
short_title: "GreekBarBench: A Challenging Benchmark for Free-Text Legal Reasoning and Citations"
year: 2025
first_author: "[[Odysseas S. Chlapanis]]"
last_author: "[[Ion Androutsopoulos]]"
authors: Odysseas S. Chlapanis, Dimitrios Galanis, Nikolaos Aletras, Ion Androutsopoulos
url: "https://arxiv.org/abs/2505.17267"
external_pdf: "https://arxiv.org/pdf/2505.17267.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "Greek"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-4o-mini, GPT-4-Turbo, Claude-3.5-Sonnet, Claude-3-Opus, Gemini-1.5-Pro, Llama-3.1-405B, Llama-3.1-70B, Llama-3.1-8B, Mistral-Large, Qwen2.5-72B, DeepSeek-V3, Command-R-Plus"
DATA_URL: "https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench"
tags: 
abstract: "We introduce GREEKBARBENCH, a benchmark that evaluates LLMs on legal questions across five different legal areas from the Greek Bar exams, requiring citations to statutory articles and case facts. To tackle the challenges of free-text evaluation, we propose a threedimensional scoring system combined with an LLM-as-a-judge approach. We also develop a meta-evaluation benchmark to assess the correlation between LLM-judges and human expert evaluations, revealing that simple, span-based rubrics..."
ethics_perspective: "AI Safety & Alignment"
---
# GreekBarBench: A Challenging Benchmark for Free-Text Legal Reasoning and Citations

## Authors

[[Odysseas S. Chlapanis, Dimitrios Galanis, Nikolaos Aletras, Ion Androutsopoulos]]

## Metadata

**Authors:** Odysseas S. Chlapanis, Dimitrios Galanis, Nikolaos Aletras, Ion Androutsopoulos

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

**Benchmark:** GreekBarBench

## Links

- **arXiv:** https://arxiv.org/abs/2505.17267
- **Code/Data:** https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench

## Abstract

A benchmark evaluating LLMs on legal questions from Greek Bar exams (2015-2024) across five legal areas, requiring citations to statutory articles and case facts. Uses a three-dimensional scoring system with LLM-as-a-judge approach. Evaluation of 13 proprietary and open-weight LLMs shows best models outperform average expert scores but fall short of 95th percentile.

## Summary

This paper introduces GreekBarBench, a benchmark derived from Greek Bar exam questions (2015-2024) covering five legal areas requiring free-text answers with citations to statutory articles and case facts. The authors develop a three-dimensional scoring system (Facts, Cited Articles, Analysis) and an LLM-as-a-judge framework using span-based rubrics. Evaluation of 13 models including GPT-4o, Claude-3.5-Sonnet, and Llama-3.1 reveals that top-performing models exceed average expert scores but remain susceptible to critical errors, particularly in identifying correct statutory articles.

## Data Description

GreekBarBench is a benchmark evaluating LLMs on legal questions from Greek Bar exams (2015-2024) across five legal areas, requiring citations to statutory articles and case facts. Uses a three-dimensional scoring system (Facts, Cited Articles, Analysis) with LLM-as-a-judge approach. Best models outperform average expert scores but fall short of 95th percentile.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Greek legal reasoning benchmark with cultural and jurisdictional specificity. Evaluates ethical and legal reasoning capabilities in Greek. Relevant to fairness and justice-related evaluation.

## Tags

