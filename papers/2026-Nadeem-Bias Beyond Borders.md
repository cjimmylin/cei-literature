---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0002
type: preprint
short_title: "Bias Beyond Borders"
year: 2025
first_author: "[[Afrozah Nadeem]]"
last_author: "[[Usman Naseem Mehwish Nasim]]"
authors: "Afrozah Nadeem, Agrima, Mehwish Nasim, Usman Naseem"
url: "https://arxiv.org/abs/2601.23001"
external_pdf: "https://arxiv.org/pdf/2601.23001.pdf"
local_pdf: "[[PDFs/2026/2026-Nadeem-Bias Beyond Borders.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Nadeem-Bias Beyond Borders.md"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: Multicultural/Cross-cultural
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: No
tags: 
abstract: "Large Language Models (LLMs) increasingly shape global discourse, making fairness and ideological neutrality essential for responsible AI deployment. Despite growing attention to political bias in LLMs, prior work largely focuses on high-resource, Western languages or narrow multilingual settings, leaving crosslingual consistency and safe post-hoc mitigation underexplored. To address this gap, we present a large-scale multilingual evaluation of political bias spanning 50 countries and 33..."
ethics_perspective: "Bias & Fairness"
data_description: "Evaluation framework"
data_metrics: "33 languages"
LLM_assessed: "Mistral, DeepSeek"
DATA_URL: NA
---
# Bias Beyond Borders

## Authors

[[Agrima Afrozah Nadeem]], [[Usman Naseem Mehwish Nasim]]

## Metadata

**Authors:** Afrozah Nadeem, Agrima, Mehwish Nasim, Usman Naseem

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.23001

## Abstract

Large Language Models (LLMs) increasingly shape global discourse, making fairness and ideological neutrality essential for responsible AI deployment. Despite growing attention to political bias in LLMs, prior work largely focuses on high-resource, Western languages or narrow multilingual settings, leaving crosslingual consistency and safe post-hoc mitigation underexplored. To address this gap, we present a large-scale multilingual evaluation of political bias spanning 50 countries and 33 languages. We introduce a complementary post-hoc mitigation framework, Cross-Lingual Alignment Steering (CLAS), designed to augment existing steering methods by aligning ideological representations across languages and dynamically regulating intervention strength. This method aligns latent ideological representations induced by political prompts into a shared ideological subspace, ensuring cross lingual consistency, with the adaptive mechanism prevents over correction and preserves coherence. Experiments demonstrate substantial bias reduction along both economic and social axes with minimal degradation in response quality. The proposed framework establishes a scalable and interpretable paradigm for fairness-aware multilingual LLM governance, balancing ideological neutrality with linguistic and cultural diversity.

## Dataset Information

Political Compass Test across 50 countries, 33 languages; introduces Cross-Lingual Alignment Steering (CLAS) mitigation framework

## Data Description

This study conducts a large-scale multilingual Political Compass Test (PCT) evaluation spanning 50 countries and 33 languages to assess political ideology bias in LLMs. Bias mitigation experiments are performed on Mistral-7B-Instruct and DeepSeek-LLM-7B-Chat using activation-space steering techniques (Individual Steering Vectors, Steering Vector Ensembles, and Cross-Lingual Alignment Steering). The evaluation measures stance polarity, intensity, and cross-lingual consistency across economic and social ideological axes.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** MEDIUM

## Tags

