---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0280
type: journalArticle
short_title: "Multimodal Understanding of Human Values in Videos"
year: 2025
first_author: "[[Y. Wang]]"
last_author: "[[Xiaofang Luo]]"
authors: "Yuchen Wang; Zhulin Tao; He Chang; Nanxin Huang; Libiao Jin; Xiaofang Luo"
doi: 10.1016/j.neucom.2025.130170
url: "https://doi.org/10.1016/j.neucom.2025.130170"
external_pdf: "https://arxiv.org/pdf/2501.11770.pdf"
pdf_extract: "PDF Extracts/2025/2025-Wang-Multimodal Understanding of Human Values in Videos.md"
local_pdf: "[[PDFs/2025/2025-Wang-Multimodal Understanding of Human Values in Videos.pdf]]"
publication: Neurocomputing
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Societal and personal values are transmitted to younger generations through interaction and exposure. Traditionally, children and adolescents learned values from parents, educators, or peers. Nowadays, social platforms serve as a significant channel through which youth (and adults) consume information, as the main medium of entertainment, and possibly the medium through which they learn different values."
ethics_perspective: "Moral Reasoning & Psychology"
data_description: "Annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "Mistral, RoBERTa, DeBERTa"
DATA_URL: "NA"
---
# Multimodal Understanding of Human Values in Videos

## Authors

[[Yuchen Wang]], [[Zhulin Tao]], [[He Chang]], [[Nanxin Huang]], [[Libiao Jin]], [[Xiaofang Luo]]

## Metadata

**Authors:** Wang, Y. et al.

**Year:** 2025

**Type:** journalArticle

**Venue:** Neurocomputing

**DOI:** [10.1016/j.neucom.2025.130170](https://doi.org/10.1016/j.neucom.2025.130170)

## Links

- **DOI:** https://doi.org/10.1016/j.neucom.2025.130170

## Abstract

Societal and personal values are transmitted to younger generations through interaction and exposure. Traditionally, children and adolescents learned values from parents, educators, or peers. Nowadays, social platforms serve as a significant channel through which youth (and adults) consume information, as the main medium of entertainment, and possibly the medium through which they learn different values. In this paper we extract implicit values from TikTok movies uploaded by online influencers targeting children and adolescents. We curated a dataset of hundreds of TikTok movies and annotated them according to the Schwartz Theory of Personal Values. We then experimented with an array of Masked and Large language model, exploring how values can be detected. Specifically, we considered two pipelines – direct extraction of values from video and a 2-step approach in which videos are first converted to elaborated scripts and then values are extracted. Achieving state-of-the-art results, we find that the 2-step approach performs significantly better than the direct approach and that using a trainable Masked Language Model as a second step significantly outperforms a few-shot application of a number of Large Language Models. We further discuss the impact of fine-tuning and compare the performance of the different models on identification of values present or contradicted in the TikTok. Finally, we share the first valuesannotated dataset of TikTok videos. Our results pave the way to further research on influence and value transmission in video-based social platforms.

## Dataset Information

First multimodal benchmark for human value understanding in video content

## Data Description

The paper curates and annotates a dataset of 890 TikTok videos from 89 influencers targeting children and adolescents, annotated according to the Schwartz Theory of Personal Values (19 values) with 2,968 total labels. Models tested include RoBERTa-large, DeBERTaV2-xlarge (both with and without fine-tuning), Gemini 1.5 Pro (direct video and 2-step transcript-based approaches), and Mistral 7B, comparing masked language model and LLM-based value extraction pipelines.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

