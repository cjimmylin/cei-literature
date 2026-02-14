---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0477
type: preprint
short_title: "LLaMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch"
year: 2024
first_author: "[[Jan Pfister]]"
last_author: "[[Andreas Hotho]]"
authors: Jan Pfister, Julia Wunderle, Andreas Hotho
url: "https://arxiv.org/abs/2411.11171"
external_pdf: "https://arxiv.org/pdf/2411.11171.pdf"
publication: arXiv
local_pdf: "[[PDFs/2024/2024-Pfister-LLaMmlein Transparent Compact and Competitive German-Only Language.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Pfister-LLaMmlein Transparent Compact and Competitive German-Only Language.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "LLäMmlein-120M, LLäMmlein-1B, bert-base-german-cased"
DATA_URL: "https://professor-x.de/lm/LLaMmlein"
tags: 
abstract: "We transparently create two German-only decoder models, LLäMmlein 120M and 1B1, from scratch and publish them, along with training data, for the (German) NLP research community to use2. The model training involved several key steps, including data preprocessing/filtering, the creation of a German tokenizer, the training itself, as well as the evaluation of the final models on various benchmarks, also against existing models."
research_topic: "Machine Learning"
---
# LLaMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch

## Authors

[[Jan Pfister, Julia Wunderle, Andreas Hotho]]

## Metadata

**Authors:** Jan Pfister, Julia Wunderle, Andreas Hotho

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** German

## Links

- **arXiv:** https://arxiv.org/abs/2411.11171
- **Code/Data:** https://professor-x.de/lm/LLaMmlein

## Abstract

German-only decoder models (120M and 1B params) trained from scratch with custom tokenizer. Evaluated on SuperGLEBer benchmark; 120M model outperforms bert-base-german-cased by 14% on NLI. Fully transparent training pipeline.

## Summary

This paper presents LLäMmlein, the first fully transparent German-only language model family (120M and 1B parameters) trained from scratch with complete documentation of data preprocessing, tokenizer creation, training process, and evaluation. The authors filter and clean German data from RedPajama V2, create a custom 32k-token German tokenizer, and pretrain two autoregressive models while releasing incremental checkpoints to enable analysis of learning dynamics. Evaluation on the SuperGLEBer benchmark shows competitive performance against state-of-the-art models, with the 120M model outperforming bert-base-german-cased by 14% on natural language inference tasks, demonstrating that smaller, transparent, German-only models can achieve strong performance.

## Data Description

German-only decoder models (120M and 1B params) trained from scratch with custom tokenizer. Evaluated on SuperGLEBer benchmark. The 120M model outperforms bert-base-german-cased by 14% on NLI tasks. Fully transparent training pipeline for German language model development.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** German-only LLMs evaluated on German benchmarks, contributing to understanding of German language model capabilities.

## Tags

