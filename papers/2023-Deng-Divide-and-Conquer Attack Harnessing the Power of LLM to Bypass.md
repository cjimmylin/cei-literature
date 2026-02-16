---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0842
type: preprint
short_title: "Divide-and-Conquer Attack: Harnessing the Power of LLM to Bypass Safety Filters of Text-to-Image Models"
year: 2025
first_author: "[[Deng, Yimo]]"
last_author: "[[Chen, Huangxun]]"
authors: "[[Deng, Yimo]]; [[Chen, Huangxun]]"
authors_incomplete: false
url: "https://arxiv.org/html/2312.07130v3"
external_pdf: "https://arxiv.org/pdf/2312.07130.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2023/2023-Deng-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.md"
local_pdf: "[[PDFs/2023/2023-Deng-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "N/A"
languages_list: "Arabic, English, Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT, ChatGLM-turbo, ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, Qwen-14B, Qwen-Max"
DATA_URL: "https://github.com/openai/CLIP"
tags: 
abstract: "To prevent Text-to-Image (T2I) models from generating unethical images, people deploy safety filters to block inappropriate drawing prompts. Previous works have employed token replacement to search adversarial prompts that attempt to bypass these filters, but they has become ineffective as nonsensical tokens fail semantic logic checks. In this paper, we approach adversarial prompts from a different perspective."
ethics_perspective: "AI Safety & Alignment"
---
# Divide-and-Conquer Attack: Harnessing the Power of LLM to Bypass Safety Filters of Text-to-Image Models

## Authors

[[Deng, Yimo]], [[Chen, Huangxun]]

## Metadata

**Authors:** Yimo Deng; Huangxun Chen

**Year:** 2023

**Type:** preprint

**Venue:** arXiv

**Languages:** Arabic, English, Multilingual

**Benchmark:** Divide-and-Conquer

## Links

- **arXiv:** https://arxiv.org/abs/2312.07130

## Abstract


To prevent Text-to-Image (T2I) models from generating unethical images, people deploy safety filters to block inappropriate drawing prompts. Previous works have employed token replacement to search adversarial prompts that attempt to bypass these filters, but they has become ineffective as nonsensical tokens fail semantic logic checks. In this paper, we approach adversarial prompts from a different perspective. We demonstrate that rephrasing a drawing intent into multiple benign descriptions of individual visual components can obtain an effective adversarial prompt. We propose a LLM-piloted multi-agent method named DACA to automatically complete intended rephrasing. Our method successfully bypasses the safety filters of DALL·E 3 and Midjourney to generate the intended images, achieving success rates of up to 76.7% and 64% in the one-time attack, and 98% and 84% in the re-use attack, respectively. We open-source our code and dataset on GitHub1. 1https://github.com/researchcode003/DACA

## Data Description

Backfill summary: Models assessed include BERT, ChatGLM-turbo, ChatGPT, GPT-3, GPT-3.5, GPT-3.5-turbo, GPT-4, Qwen-14B, Qwen-Max. Verified dataset/resource link: https://github.com/openai/CLIP.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** Divide-and-Conquer benchmark for Arabic, Multilingual, English; ethics/values focus

## Tags

