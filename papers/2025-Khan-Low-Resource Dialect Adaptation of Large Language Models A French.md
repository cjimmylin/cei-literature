---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0438
type: preprint
short_title: "Low-Resource Dialect Adaptation of Large Language Models: A French Dialect Case-Study"
year: 2025
first_author: "[[Eeham Khan]]"
last_author: "[[Unknown]]"
authors: Eeham Khan; Firas Saidani; Owen Van Esbroeck; Richard Khoury; Leila Kosseim
url: "https://arxiv.org/abs/2510.22747"
external_pdf: "https://arxiv.org/pdf/2510.22747.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-Khan-Low-Resource Dialect Adaptation of Large Language Models A French.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Khan-Low-Resource Dialect Adaptation of Large Language Models A French.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: "French, Quebecois French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
LLM_assessed: "CroissantLLM, Llama-3.1, Llama-3.2"
DATA_URL: "https://github.com/CLaC-Lab/QuebecLLM-CPT"
tags: 
abstract: "Despite the widespread adoption of large language models (LLMs), their strongest capabilities remain largely confined to a small number of high-resource languages for which there is abundant training data. Recently, continual pretraining (CPT) has emerged as a means to fine-tune these models to low-resource regional dialects. In this paper, we study the use of CPT for dialect learning under tight data and compute budgets."
research_topic: "Machine Learning"
---
# Low-Resource Dialect Adaptation of Large Language Models: A French Dialect Case-Study

## Authors

[[Eeham Khan]], [[Firas Saidani]], [[Owen Van Esbroeck]], [[Richard Khoury]], [[Leila Kosseim]]

## Metadata

**Authors:** Eeham Khan; Firas Saidani; Owen Van Esbroeck; Richard Khoury; Leila Kosseim

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** French, Quebecois French

## Links

- **arXiv:** https://arxiv.org/abs/2510.22747

## Abstract

Adapts three LLMs to Quebecois French dialect using a small dataset and benchmarks them on the COLE suite. Shows continued pre-training with LoRA achieves dialectal gains with minimal regression on prestige French. Highlights that systems defaulting to prestige French can normalize away regional features and reinforce linguistic hierarchies.

## Summary

This paper explores continual pre-training for dialect adaptation in low-resource settings, using Quebec French as a case study. The authors adapt three LLMs (CroissantLLM, Llama-3.2-1B, Llama-3.1-8B) using parameter-efficient fine-tuning with LoRA on a very small 86M token corpus, updating less than 1% of model parameters. Evaluation on the COLE benchmark suite demonstrates improved performance on Quebec French tasks with minimal regression on prestige French benchmarks, though gains are highly contingent on corpus composition, with the work highlighting how models defaulting to prestige variants can reinforce linguistic hierarchies by normalizing away regional features.

## Data Description

Introduces the first Quebecois French LLMs by adapting three base models (CroissantLLM, Llama-3.2-1B, Llama-3.1-8B) using continual pre-training with LoRA on a small 86M token corpus, evaluated on the COLE benchmark suite for both Quebec French and prestige French tasks.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Directly addresses Quebecois French LLM evaluation. Shows training on Quebec slang can strengthen stereotypes linking dialectal features to class, region, or demographics.

## Tags

