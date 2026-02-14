---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0429
type: preprint
short_title: "ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection"
year: 2025
first_author: "[[Axel Delaville]]"
last_author: "[[Axel Delaville]]"
authors: Axel Delaville, et al.
url: "https://arxiv.org/abs/2508.11281"
external_pdf: "https://arxiv.org/pdf/2508.11281.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: "French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "Qwen3-4B, GPT-4o, Gemini-2.5, DeepSeek-R1, CamemBERT, BLOOM, Mistral"
DATA_URL: "https://huggingface.co/datasets/AxelDlv00/ToxiFrench"
tags: 
abstract: "Detecting toxic content using language models is crucial yet challenging. While substantial progress has been made in English, toxicity detection in French remains underdeveloped, primarily due to the lack of culturally relevant, human-annotated, large-scale datasets. In this work, we release TOXIFRENCH, a dataset of 53,622 French online comments together with a balanced benchmark split for systematic evaluation."
ethics_perspective: "Toxicity & Hate Speech"
---
# ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection

## Authors

[[Axel Delaville, et al.]]

## Metadata

**Authors:** Axel Delaville, et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French

**Benchmark:** ToxiFrench

## Links

- **arXiv:** https://arxiv.org/abs/2508.11281
- **Code/Data:** https://huggingface.co/datasets/AxelDlv00/ToxiFrench

## Abstract

Dataset of 53,622 native French online comments with a balanced benchmark split for systematic evaluation of toxicity detection. Constructed via semi-automated annotation pipeline reducing manual labeling to 10%. Largest high-quality public French toxicity dataset with Chain-of-Thought explanations for every label.

## Summary

This paper releases ToxiFrench, a dataset of 53,622 native French online comments for toxicity detection, constructed via a semi-automated annotation pipeline that reduces manual labeling to only 10% while maintaining statistical alignment with human-only annotation. The authors benchmark SLMs, BERT-style models, commercial APIs, and LLMs, revealing that small language models often surpass larger ones in robustness. They propose a novel Chain-of-Thought fine-tuning strategy with Dynamic Weighted Loss, achieving state-of-the-art performance with a fine-tuned Qwen3-4B model that outperforms GPT-4o and DeepSeek-R1 on their benchmark.

## Data Description

ToxiFrench is a dataset of 53,622 native French online comments with a balanced benchmark split for systematic toxicity detection evaluation. Constructed via semi-automated annotation pipeline reducing manual labeling to 10%. It is the largest high-quality public French toxicity dataset with Chain-of-Thought explanations for every label.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Largest French toxicity dataset. Benchmarks SLMs, BERT-style models, commercial moderation APIs, and LLMs. Finds small language models often surpass larger ones in robustness.

## Tags

