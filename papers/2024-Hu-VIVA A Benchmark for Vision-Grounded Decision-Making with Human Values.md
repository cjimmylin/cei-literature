---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0277
type: conferencePaper
short_title: "VIVA: A Benchmark for Vision-Grounded Decision-Making with Human Values"
year: 2024
first_author: "[[Hu, Zhe]]"
last_author: "[[Yin, Yu]]"
authors: "[[Hu, Zhe]]; [[Ren, Yixiao]]; [[Li, Jing]]; [[Yin, Yu]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2407.03000"
external_pdf: "https://arxiv.org/pdf/2407.03000.pdf"
local_pdf: "[[PDFs/2024/2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Hu-VIVA A Benchmark for Vision-Grounded Decision-Making with Human Values.md"
publication: EMNLP
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Large vision language models (VLMs) have demonstrated significant potential for integration into daily life, making it crucial for them to incorporate human values when making decisions in real-world situations. This paper introduces VIVA, a benchmark for VIsiongrounded decision-making driven by human VAlues. While most large VLMs focus on physical-level skills, our work is the first to examine their multimodal capabilities in leveraging human values to make decisions under a vision-depicted..."
ethics_perspective: "Moral Reasoning & Psychology"
data_description: "Benchmark annotated dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude"
DATA_URL: "https://github.com/Derekkk/VIVA_EMNLP24"
---
# VIVA: A Benchmark for Vision-Grounded Decision-Making with Human Values

## Authors

[[Hu, Zhe]], [[Ren, Yixiao]], [[Li, Jing]], [[Yin, Yu]]

## Metadata

**Authors:** Hu, Zhe; Ren, Yixiao; Li, Jing; Yin, Yu

**Year:** 2024

**Type:** conferencePaper

**Venue:** EMNLP

## Links

- **arXiv:** https://arxiv.org/abs/2407.03000

## Abstract

Large vision language models (VLMs) have demonstrated significant potential for integration into daily life, making it crucial for them to incorporate human values when making decisions in real-world situations. This paper introduces VIVA, a benchmark for VIsiongrounded decision-making driven by human VAlues. While most large VLMs focus on physical-level skills, our work is the first to examine their multimodal capabilities in leveraging human values to make decisions under a vision-depicted situation. VIVA contains 1,240 images depicting diverse real-world situations and the manually annotated decisions grounded in them. Given an image there, the model should select the most appropriate action to address the situation and provide the relevant human values and reason underlying the decision. Extensive experiments based on VIVA show the limitation of VLMs in using human values to make multimodal decisions. Further analyses indicate the potential benefits of exploiting action consequences and predicted human values. Our code and dataset are available at https://github.com/Derekkk/ VIVA_EMNLP24.

## Dataset Information

1,062 images assessing vision-language models' capacity to leverage human values for decision-making

## Data Description

VIVA is a benchmark for vision-grounded decision-making driven by human values, containing 1,240 images depicting diverse real-world situations with manually annotated decisions. The benchmark includes two-level tasks: Level-1 action selection (multiple-choice) and Level-2 value inference and reason generation. It covers 10 situation categories including dangerous behavior, child safety, emergent situations, and assistance scenarios, with 8,610 unique annotated human values.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

