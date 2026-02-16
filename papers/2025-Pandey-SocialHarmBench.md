---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0125
type: preprint
short_title: SocialHarmBench
year: 2025
first_author: "[[Punya Syon Pandey]]"
last_author: "[[Zhijing Jin]]"
authors: "Punya Syon Pandey, Hai Son Le, Devansh Bhardwaj, Rada Mihalcea, Zhijing Jin"
url: "https://arxiv.org/abs/2510.04891"
external_pdf: "https://arxiv.org/pdf/2510.04891.pdf"
pdf_extract: "PDF Extracts/0000/2025-Pandey-SocialHarmBench.md"
local_pdf: "[[PDFs/2025/2025-Pandey-SocialHarmBench.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "Large language models (LLMs) are increasingly deployed in contexts where their failures can have direct sociopolitical consequences. Yet, existing safety benchmarks rarely test vulnerabilities in domains such as political manipulation, propaganda and disinformation generation, or surveillance and information control. We introduce SOCIALHARMBENCH, a dataset of 585 prompts spanning 7 sociopolitical categories and 34 countries, designed to surface where LLMs most acutely fail in politically..."
ethics_perspective: "AI Safety & Alignment"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Gemini, Gemma, Llama-3, Mistral, Qwen, DeepSeek"
DATA_URL: "https://huggingface.co/datasets/psyonp/SocialHarmBench, https://github.com/psyonp/SocialHarmBench"
research_topic: "Other"
---
# SocialHarmBench

## Authors

[[Punya Syon Pandey]], [[Hai Son Le]], [[Devansh Bhardwaj]], [[Rada Mihalcea]], [[Zhijing Jin]]

## Metadata

**Authors:** Punya Syon Pandey, Hai Son Le, Devansh Bhardwaj, Rada Mihalcea, Zhijing Jin

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2510.04891
- **Code/Data:** https://huggingface.co/datasets/psyonp/SocialHarmBench

## Abstract

Large language models (LLMs) are increasingly deployed in contexts where their failures can have direct sociopolitical consequences. Yet, existing safety benchmarks rarely test vulnerabilities in domains such as political manipulation, propaganda and disinformation generation, or surveillance and information control. We introduce SOCIALHARMBENCH, a dataset of 585 prompts spanning 7 sociopolitical categories and 34 countries, designed to surface where LLMs most acutely fail in politically charged contexts. Our evaluations reveal several shortcomings: open-weight models exhibit high vulnerability to harmful compliance, with Mistral-7B reaching attack success rates as high as 97%–98% in domains such as historical revisionism, propaganda, and political manipulation. Moreover, temporal and geographic analyses show that LLMs are most fragile when confronted with 21st-century or pre-20th-century contexts, and when responding to prompts tied to regions such as Latin America, the USA, and the UK. These findings demonstrate that current safeguards fail to generalize to high-stakes sociopolitical settings, exposing systematic biases and raising concerns about the reliability of LLMs in preserving human rights and democratic values.

## Dataset Information

585 prompts across 7 sociopolitical categories, covering 34 countries

## Data Description

SocialHarmBench is a benchmark dataset of 585 prompts spanning 7 sociopolitical harm categories (censorship, historical revisionism, human rights violations, political manipulation, propaganda, surveillance, war crimes) across 34 countries and multiple centuries. The dataset includes three functional prompt types (standard, opinion elicitation, historical reference) and is evaluated using HarmBench and StrongREJECT classifiers to measure attack success rates.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

