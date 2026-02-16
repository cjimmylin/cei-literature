---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0501
type: preprint
short_title: "Towards Multilingual LLM Evaluation for Baltic and Nordic Languages"
year: 2025
first_author: "[[Yevhen Kostiuk]]"
last_author: "[[Artur Kiulian]]"
authors: "[[Yevhen Kostiuk]]; [[Oxana Vitman]]; [[Łukasz Gagała]]; [[Artur Kiulian]]"
url: "https://arxiv.org/abs/2501.09154"
external_pdf: "https://arxiv.org/pdf/2501.09154.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages.md"
local_pdf: "[[PDFs/2025/2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Lithuanian, Baltic, Nordic"
languages_list: "Lithuanian, Nordic languages"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-4o, Llama-3.1, Qwen2"
DATA_URL: "https://github.com/ollama/ollama"
tags: 
abstract: "In this work, we evaluated Lithuanian and general history knowledge of multilingual Large Language Models (LLMs) on a multiple-choice question-answering task. The models were tested on a dataset of Lithuanian national and general history questions translated into Baltic, Nordic, and other languages (English, Ukrainian, Arabic) to assess the knowledge sharing from culturally and historically connected groups. We evaluated GPT-4o, LLaMa3.1 8b and 70b, QWEN2."
ethics_perspective: "AI Safety & Alignment"
authors_incomplete: false
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Translation"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# Towards Multilingual LLM Evaluation for Baltic and Nordic Languages

## Authors

[[Yevhen Kostiuk]], [[Oxana Vitman]], [[Łukasz Gagała]], [[Artur Kiulian]]

## Metadata

**Authors:** Yevhen Kostiuk, Oxana Vitman, Łukasz Gagała, Artur Kiulian

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Lithuanian, Nordic languages

## Links

- **arXiv:** https://arxiv.org/abs/2501.09154

## Abstract

Evaluates multilingual LLMs on Lithuanian and general history, exploring how LLMs perform when prompted in different languages within the Nordic and Baltic language group.

## Summary

This paper evaluates the Lithuanian and general history knowledge of multilingual LLMs (GPT-4o, Llama-3.1 8b/70b, Qwen2) using a multiple-choice question-answering task. The study translates Lithuanian national and general history questions into Baltic, Nordic, and other languages (English, Ukrainian, Arabic) to assess knowledge sharing from culturally and historically connected language groups. The cross-lingual evaluation approach investigates whether LLMs exhibit different performance when prompted in languages from related cultural and historical contexts versus more distant languages.

## Data Description

Evaluates multilingual LLMs on Lithuanian and general history knowledge using multiple-choice questions translated into Baltic, Nordic, and other languages to assess knowledge sharing across culturally connected language groups. Does not introduce a publicly available dataset.


## Detailed Summary

This paper evaluates the Lithuanian and general history knowledge of multilingual LLMs using a multiple-choice question-answering task, with the goal of assessing knowledge sharing from culturally and historically connected language groups. The study tests models on a dataset of Lithuanian national and general history questions translated into Baltic (Estonian, Latvian), Nordic (Danish, Finnish, Swedish), and other languages (English, Ukrainian, Arabic). Ten models are evaluated: GPT-4o, LLaMa3.1 8b and 70b, QWEN2.5 7b and 72b, Mistral Nemo 12b, LLaMa3 8b, Mistral 7b, LLaMa3.2 3b, and Nordic fine-tuned models (GPT-SW3 and LLaMa3 8b). The research investigates whether cultural or historical proximity between language groups translates to better performance on region-specific historical knowledge questions, finding that shared cultural context alone does not guarantee better performance.

## Paper Outline

1. Introduction - Motivation for multilingual LLM evaluation on historical knowledge
2. Related Work - Pre-trained LLMs and multilingual knowledge; benchmark dataset creation approaches
3. Dataset - Lithuanian history exam questions and translation methodology
4. Experimental Setup - Model selection and evaluation parameters
5. Results - Per-language and per-language-group accuracy analysis
6. Discussion - Cultural alignment vs. model performance
7. Conclusion

## Methods Summary

The study uses a publicly available Lithuanian history exam question-answering dataset, which is automatically translated into nine languages across three language groups using machine translation (DeepL), with partial manual quality evaluation. Models are tested on Lithuanian-specific and general history questions in each language. Accuracy scores are compared per language and averaged per language group (Baltic, Nordic, Other) to assess whether culturally and historically connected languages benefit from knowledge transfer.

## Results Summary

GPT-4o consistently outperforms all other models across all language groups, with slightly better results for Baltic and Nordic languages. Larger open-source models (QWEN2.5 72b, LLaMa3.1 70b) perform well but show weaker alignment specifically with Baltic languages. Smaller models (Mistral Nemo 12b, LLaMa3.2 3b, QWEN 7B, LLaMa3.1 8B, LLaMa3 8b) demonstrate gaps in Lithuanian-related knowledge for Baltic languages while performing better on Nordic and other languages. Notably, Nordic fine-tuned models (GPT-SW3, Nordic LLaMa3 8b) did not surpass general multilingual models, indicating that shared cultural or historical context alone does not ensure better performance.

## Conclusions

The study reveals that cultural and historical alignment between languages does not automatically translate to improved LLM performance on culturally specific knowledge tasks. General multilingual models outperform region-specific fine-tuned models, suggesting that scale and training data diversity remain more important factors than cultural proximity. The findings highlight the need for culturally aligned, high-quality datasets for evaluating LLMs on region-specific knowledge.

## Artifact Contributions

- **Dataset:** Lithuanian history exam questions translated into 9 languages across Baltic, Nordic, and other language groups
- **Evaluation Results:** Comprehensive cross-lingual comparison of 10 LLMs on historical knowledge tasks

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Cross-lingual LLM evaluation within Nordic and Baltic language families.

## Tags

