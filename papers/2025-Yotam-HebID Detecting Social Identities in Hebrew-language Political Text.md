---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0086
type: preprint
short_title: "HebID: Detecting Social Identities in Hebrew-language Political Text"
year: 2025
first_author: "[[Cohen, Yotam]]"
last_author: "[[Loewenthal, Alon]]"
authors: Cohen, Yotam; Shenhav, Shaul; Loewenthal, Alon
url: "https://arxiv.org/abs/2508.15483"
external_pdf: "https://arxiv.org/pdf/2508.15483.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025-Yotam-HebID Detecting Social Identities in Hebrew-language Political Text.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Yotam-HebID Detecting Social Identities in Hebrew-language Political Text.md"
DATE_ADDED: 20260215
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Hebrew/Israeli"
cultures_nationalities_list: "Israeli"
languages_list: "Hebrew"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "DictaLM2.0, AlephBERT, mBERT"
DATA_URL: "https://github.com/guymorlan/hebid/"
tags: 
abstract: "Political language is deeply intertwined with social identities. While social identities are often shaped by specific cultural contexts, existing NLP datasets are predominantly Englishcentric and focus on coarse-grained identity categories. We introduce HEBID, the first multilabel Hebrew corpus for social identity detection. The corpus contains 5,536 sentences from Israeli politicians’ Facebook posts (Dec 2018– Apr 2021), with each sentence manually annotated for twelve nuanced social..."
research_topic: "Bias & Fairness"
---
# HebID: Detecting Social Identities in Hebrew-language Political Text

## Authors

[[Cohen, Yotam]], [[Shenhav, Shaul]], [[Loewenthal, Alon]]

## Metadata

**Authors:** Cohen, Yotam; Shenhav, Shaul; Loewenthal, Alon

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Cultures:** Israeli

**Benchmark:** HebID

## Links

- **arXiv:** https://arxiv.org/abs/2508.15483

## Abstract

First publicly available multilabel Hebrew corpus for fine-grained social identity detection in political text. 5,536 sentences from Israeli politicians' Facebook posts annotated for 12 social identities (e.g., Rightist, Ultra-Orthodox, Socially-oriented). DictaLM2.0 achieves macro-F1 of 0.743.

## Data Description

This paper introduces HEBID, the first multilabel Hebrew corpus for social identity detection containing 5,536 sentences from Israeli politicians' Facebook posts (Dec 2018-Apr 2021), annotated for twelve nuanced social identities. The authors benchmark multilabel and single-label encoders alongside 2B-9B parameter decoder LLMs, finding that Hebrew-tuned LLMs (specifically DictaLM2.0) achieve the best results (macro-F1=0.74). The classifier is applied to politicians' Facebook posts and parliamentary speeches for sociolinguistic analysis.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_15
**Relevance:** Evaluates LLMs' ability to detect Israeli social/cultural identities in Hebrew text. While focused on NLP task, the 12 social identity categories are deeply rooted in Israeli cultural values and political norms.

## Tags

