---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0013
type: preprint
short_title: RedBench
year: 2025
first_author: "[[Quy-Anh Dang]]"
last_author: "[[Truong-Son Hy]]"
authors: "Quy-Anh Dang, Chris Ngo, Truong-Son Hy"
url: "https://arxiv.org/abs/2601.03699"
external_pdf: "https://arxiv.org/pdf/2601.03699.pdf"
pdf_extract: "PDF Extracts/0000/2026-Dang-RedBench.md"
local_pdf: "[[PDFs/2026/2026-Dang-RedBench.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "As large language models (LLMs) become integral to safety-critical applications, ensuring their robustness against adversarial prompts is paramount. However, existing red teaming datasets suffer from inconsistent risk categorizations, limited domain coverage, and outdated evaluations, hindering systematic vulnerability assessments. To address these challenges, we introduce RedBench, a universal dataset aggregating 37 benchmark datasets from leading conferences and repositories, comprising..."
LLM_assessed: "Llama-3, Gemma, Qwen, Mistral, GPT-4"
DATA_URL: "https://github.com/knoveleng/redeval"
research_topic: "Other"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "29,362 samples"
---
# RedBench

## Authors

[[Quy-Anh Dang]], [[Chris Ngo]], [[Truong-Son Hy]]

## Metadata

**Authors:** Quy-Anh Dang, Chris Ngo, Truong-Son Hy

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.03699
- **Code/Data:** https://github.com/knoveleng/redeval

## Abstract

As large language models (LLMs) become integral to safety-critical applications, ensuring their robustness against adversarial prompts is paramount. However, existing red teaming datasets suffer from inconsistent risk categorizations, limited domain coverage, and outdated evaluations, hindering systematic vulnerability assessments. To address these challenges, we introduce RedBench, a universal dataset aggregating 37 benchmark datasets from leading conferences and repositories, comprising 29,362 samples across attack and refusal prompts. RedBench employs a standardized taxonomy with 22 risk categories and 19 domains, enabling consistent and comprehensive evaluations of LLM vulnerabilities. We provide a detailed analysis of existing datasets, establish baselines for modern LLMs, and open-source the dataset and evaluation code1. Our contributions facilitate robust comparisons, foster future research, and promote the development of secure and reliable LLMs for real-world deployment. Code: https: //github.com/knoveleng/redeval Warning: This paper contains examples that may be offensive, harmful, or biased.

## Dataset Information

29,362 samples (attack and refusal prompts)

## Data Description

RedBench is a universal red teaming dataset aggregating 37 benchmark datasets from leading conferences and repositories, comprising 29,362 samples across attack and refusal prompts. It employs a standardized taxonomy with 22 risk categories and 19 domains, enabling consistent evaluation of LLM vulnerabilities. Six safety-aligned LLMs (Llama-3.1-8B-Instruct, Gemma-2-9B-It, Qwen2.5-7B-Instruct, Ministral-8B-Instruct-2410, GPT-4o Mini, GPT-4.1-Nano) are evaluated using attack success rate and rejection rate metrics.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

