---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0482
type: preprint
short_title: "DUMB: A Benchmark for Smart Evaluation of Dutch Models"
year: 2023
first_author: "[[Wietse de Vries]]"
last_author: "[[Wietse de Vries]]"
authors: Wietse de Vries et al.
url: "https://arxiv.org/abs/2305.13026"
external_pdf: "https://arxiv.org/pdf/2305.13026.pdf"
publication: arXiv / EMNLP 2023
local_pdf: "[[PDFs/2023/2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.pdf]]"
pdf_extract: "PDF Extracts/2023/2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Dutch"
languages_list: "Dutch"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "BERTje, RobBERT, mBERT, XLM-RoBERTa"
DATA_URL: "https://github.com/wjwillemse/dumb"
tags: 
abstract: "We introduce the Dutch Model Benchmark: DUMB. The benchmark includes a diverse set of datasets for low-, medium- and highresource tasks. The total set of nine tasks includes four tasks that were previously not available in Dutch. Instead of relying on a mean score across tasks, we propose Relative Error Reduction (RER), which compares the DUMB performance of language models to a strong baseline which can be referred to in the future even when assessing different sets of language models."
research_topic: "Machine Learning"
---
# DUMB: A Benchmark for Smart Evaluation of Dutch Models

## Authors

[[Wietse de Vries et al.]]

## Metadata

**Authors:** Wietse de Vries et al.

**Year:** 2023

**Type:** preprint

**Venue:** arXiv / EMNLP 2023

**Languages:** Dutch

**Benchmark:** DUMB

## Links

- **arXiv:** https://arxiv.org/abs/2305.13026
- **Code/Data:** https://github.com/wietsedv/dumb

## Abstract

Dutch Model Benchmark with 9 tasks including 4 new for Dutch. Evaluates 14 pre-trained LMs using Relative Error Reduction metric. Finds Dutch monolingual models under-perform compared to large multilingual models like DeBERTaV3. Published at EMNLP 2023.

## Summary

This paper introduces DUMB (Dutch Model Benchmark), a comprehensive evaluation suite comprising nine diverse tasks for Dutch language models, including four tasks previously unavailable in Dutch covering low-, medium-, and high-resource scenarios. Rather than using simple mean scores, the authors propose Relative Error Reduction (RER) as a more robust metric that compares model performance against a strong baseline. Evaluating 14 pre-trained models (both monolingual and multilingual of varying sizes), they find that current Dutch monolingual models (BERTje, RobBERT) underperform compared to large multilingual models, with DeBERTaV3-large, XLM-R-large, and mDeBERTaV3-base achieving the highest performance. The work suggests training larger Dutch models with alternative architectures and pre-training objectives, and provides a public leaderboard at dumbench.nl.

## Data Description

DUMB (Dutch Model Benchmark) suite containing 6 datasets for evaluating Dutch language models across sentiment analysis, topic classification, hate speech detection, and natural language inference tasks. Designed to provide comprehensive evaluation of Dutch NLP models.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Primary Dutch-language NLU benchmark, foundational for evaluating Dutch LLMs.

## Tags

