---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0071
type: preprint
short_title: "FanarGuard: A Culturally-Aware Moderation Filter for Arabic Language Models"
year: 2025
first_author: "[[Masoomali Fatehkia]]"
last_author: "[[Husrev Taha Sencar]]"
authors: Masoomali Fatehkia, Enes Altinisik, Husrev Taha Sencar
doi: 10.48550/arXiv.2511.18852
url: "https://arxiv.org/abs/2511.18852"
external_pdf: "https://arxiv.org/pdf/2511.18852.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025-Fatehkia-FanarGuard A Culturally-Aware Moderation Filter for Arabic Language.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Fatehkia-FanarGuard A Culturally-Aware Moderation Filter for Arabic Language.md"
DATE_ADDED: 20260215
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic, Pan-Arab"
languages_list: "Arabic, English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Gemma-2B, Gemma-4B"
DATA_URL: "NA"
tags: 
abstract: "Content moderation filters are a critical safeguard against alignment failures in language models. Yet most existing filters focus narrowly on general safety and overlook cultural context. In this work, we introduce FanarGuard, a bilingual moderation filter that evaluates both safety and cultural alignment in Arabic and English. We construct a dataset of over 468K prompt and response pairs, drawn from synthetic and public datasets, scored by a panel of LLM judges on harmlessness and cultural..."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety annotated dataset"
data_metrics: "Not specified"
---
# FanarGuard: A Culturally-Aware Moderation Filter for Arabic Language Models

## Authors

[[Masoomali Fatehkia]], [[Enes Altinisik]], [[Husrev Taha Sencar]]

## Metadata

**Authors:** Masoomali Fatehkia, Enes Altinisik, Husrev Taha Sencar

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.48550/arXiv.2511.18852](https://doi.org/10.48550/arXiv.2511.18852)

**Cultures:** Arabic, Pan-Arab

**Benchmark:** FanarGuard

## Links

- **arXiv:** https://arxiv.org/abs/2511.18852
- **DOI:** https://doi.org/10.48550/arXiv.2511.18852

## Abstract

Bilingual moderation filter evaluating both safety and cultural alignment in Arabic/English. 468K+ prompt-response pairs dataset. First benchmark targeting Arabic cultural contexts with 1K+ norm-sensitive prompts annotated by human raters. Addresses Western-centric biases in LLMs that violate Arabic cultural or religious precepts.

## Data Description

The paper introduces FanarGuard, a bilingual (Arabic/English) content moderation filter that evaluates both safety and cultural alignment. It constructs a training dataset of over 468K prompt-response pairs scored by LLM judges on harmlessness and cultural awareness, and develops a new benchmark of over 1,000 culturally sensitive prompts targeting Arabic cultural contexts with human annotations. FanarGuard is trained as a regression model on RoBERTa-large, Gemma-2B, and Gemma-4B base models, achieving MAE of 0.79 on cultural alignment and F1 of 0.84 on safety benchmarks.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_11
**Relevance:** First culturally-aware moderation benchmark for Arabic. Specifically targets cultural norm violations in LLM outputs, not just safety.

## Tags

