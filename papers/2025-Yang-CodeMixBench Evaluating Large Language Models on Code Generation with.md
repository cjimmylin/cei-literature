---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0848
type: preprint
short_title: "CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts"
year: 2025
first_author: "[[Yilun Yang]]"
last_author: "[[Yilun Yang]]"
authors: "Yilun Yang"
url: "https://arxiv.org/html/2505.05063v1"
external_pdf: "https://arxiv.org/pdf/2505.05063.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with.md"
local_pdf: "[[PDFs/2025/2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Chinese, Indian, Spanish"
cultures_nationalities_list: "Chinese, Indian, Spanish"
languages_list: "Code-switching, English, Hindi"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT, CodeLLaMA, Codex, DeepSeek, DeepSeek-Coder, DeepSeek-R1, Gemma-3, Llama, LLaMA-3.1, LLaMA-3.2, LLaMA3, Llama-3, Phi-4, Phi-4-multimodal, Qwen, Qwen-1.5B, Qwen-14B, Qwen2.5"
DATA_URL: "NA"
tags: 
abstract: "Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use codemixed language while interacting with LLMs."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark"
data_metrics: "Not specified"
---
# CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts

## Authors

[[Yilun Yang]]

## Metadata

**Authors:** Yilun Yang

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Code-switching, English, Hindi

**Benchmark:** CodeMixBench

## Links

- **arXiv:** https://arxiv.org/abs/2505.05063

## Abstract


Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use codemixed language while interacting with LLMs. To address this gap, we introduce CodeMixBench, a novel benchmark designed to evaluate the robustness of LLMs on code generation from code-mixed prompts. Built upon BigCodeBench, CodeMixBench introduces controlled code-mixing (CMD) into the natural language parts of prompts across three language pairs: Hinglish (Hindi-English), Spanish-English, and Chinese Pinyin-English. We comprehensively evaluate a diverse set of open-source code generation models ranging from 1.5B to 15B parameters. Our results show that code-mixed prompts consistently degrade Pass@1 performance compared to their English-only counterparts, with performance drops increasing under higher CMD levels for smaller models. CodeMixBench provides a realistic evaluation framework for studying multilingual code generation and highlights new challenges and directions for building robust code generation models that generalize well across diverse linguistic settings.

## Data Description

Backfill summary: Models assessed include BERT, CodeLLaMA, Codex, DeepSeek, DeepSeek-Coder, DeepSeek-R1, Gemma-3, Llama, LLaMA-3.1, LLaMA-3.2, LLaMA3, Llama-3, Phi-4, Phi-4-multimodal, Qwen, Qwen-1.5B, Qwen-14B, Qwen2.5. No high-confidence repository-style data URL was identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** CodeMixBench benchmark for Hindi, Code-switching, English

## Tags

