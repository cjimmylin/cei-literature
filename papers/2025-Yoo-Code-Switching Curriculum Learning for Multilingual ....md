---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0826
type: conferencePaper
short_title: "Code-Switching Curriculum Learning for Multilingual ..."
year: 2025
first_author: "[[Haneul Yoo]]"
last_author: "[[Haneul Yoo]]"
authors: "Haneul Yoo"
url: "https://aclanthology.org/2025.findings-acl.407.pdf"
external_pdf: "https://arxiv.org/pdf/2411.02460v2.pdf"
publication: "ACL Anthology"
pdf_extract: "PDF Extracts/2025/2025-Yoo-Code-Switching Curriculum Learning for Multilingual ....md"
local_pdf: "[[PDFs/2025/2025-Yoo-Code-Switching Curriculum Learning for Multilingual ....pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Japanese, Korean, Indonesian"
languages_list: "Code-switching, Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "BERT, ChatGPT, GPT-4, GPT-4o, Gemma, Gemma 2, Llama, Llama 3.2, Phi 3, Qwen 2, Qwen MMMLU, Qwen 2.5, llama 3"
DATA_URL: "https://huggingface.co/datasets/openai/MMMLU"
tags: 
abstract: "Large language models (LLMs) now exhibit near human-level performance in various tasks, but their performance drops drastically after a handful of high-resource languages due to the imbalance in pre-training data. Inspired by the human process of second language acquisition, particularly code-switching—the practice of language alternation in a conversation— we propose code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs."
research_topic: "Machine Translation"
ethics_perspective: "AI Safety & Alignment"
---
# Code-Switching Curriculum Learning for Multilingual ...

## Authors

[[Haneul Yoo]]

## Metadata

**Authors:** Haneul Yoo

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** Code-switching, Multilingual

**Benchmark:** Code-Switching

## Links

- **URL:** https://aclanthology.org/2025.findings-acl.407.pdf

## Abstract


Large language models (LLMs) now exhibit near human-level performance in various tasks, but their performance drops drastically after a handful of high-resource languages due to the imbalance in pre-training data. Inspired by the human process of second language acquisition, particularly code-switching—the practice of language alternation in a conversation— we propose code-switching curriculum learning (CSCL) to enhance cross-lingual transfer for LLMs. CSCL mimics the stages of human language learning by progressively training models with a curriculum consisting of 1) token-level code-switching, 2) sentence-level code-switching, and 3) monolingual corpora. Using Qwen 2 as our underlying model, we demonstrate the efficacy of the CSCL in improving language transfer to Korean, achieving significant performance gains compared to monolingual continual pre-training methods. Ablation studies reveal that both token- and sentence-level code-switching significantly enhance cross-lingual transfer and that curriculum learning amplifies these effects. We also extend our findings into various languages, including Japanese (high-resource) and Indonesian (lowresource), and using two additional models (Gemma 2 and Phi 3.5). We further show that CSCL mitigates spurious correlations between language resources and safety alignment, presenting a robust, efficient framework for more equitable language transfer in LLMs. We observe that CSCL is effective for low-resource settings where high-quality, monolingual corpora for language transfer are hardly available.

## Data Description

Backfill summary: Models assessed include BERT, ChatGPT, GPT-4, GPT-4o, Gemma, Gemma 2, Llama, Llama 3.2, Phi 3, Qwen 2, Qwen MMMLU, Qwen 2.5, llama 3. Verified dataset/resource link: https://huggingface.co/datasets/openai/MMMLU.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** Code-Switching benchmark for Multilingual, Code-switching

## Tags

