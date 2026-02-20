---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0138
type: conferencePaper
short_title: "Value Portrait"
year: 2025
first_author: "[[Jongwook Han]]"
last_author: "[[Yohan Jo]]"
authors: "Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo"
url: "https://arxiv.org/abs/2505.01015"
external_pdf: "https://arxiv.org/pdf/2505.01015.pdf"
pdf_extract: "PDF Extracts/2025/2025-Han-Value Portrait.md"
local_pdf: "[[PDFs/2025/2025-Han-Value Portrait.pdf]]"
publication: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "The importance of benchmarks for assessing the values of language models has been pronounced due to the growing need of more authentic, human-aligned responses. However, existing benchmarks rely on human or machine annotations that are vulnerable to value-related biases. Furthermore, the tested scenarios often diverge from real-world contexts in which models are commonly used to generate text and express values."
LLM_assessed: "GPT-4, Llama-3, Qwen, Gemma, Mistral, Claude"
DATA_URL: "https://github.com/holi-lab/ValuePortrait"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
CONFERENCE: "ACL 2025"
---
# Value Portrait

## Authors

[[Jiawei Han|Jongwook Han]], [[Dongmin Choi]], [[Woojung Song]], [[Eun-Ju Lee]], [[Yohan Jo]]

## Metadata

**Authors:** Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2505.01015

## Abstract

The importance of benchmarks for assessing the values of language models has been pronounced due to the growing need of more authentic, human-aligned responses. However, existing benchmarks rely on human or machine annotations that are vulnerable to value-related biases. Furthermore, the tested scenarios often diverge from real-world contexts in which models are commonly used to generate text and express values. To address these issues, we propose the Value Portrait benchmark, a reliable framework for evaluating LLMs’ value orientations with two key characteristics. First, the benchmark consists of items that capture real-life user-LLM interactions, enhancing the relevance of assessment results to real-world LLM usage. Second, each item is rated by human subjects based on its similarity to their own thoughts, and correlations between these ratings and the subjects’ actual value scores are derived. This psychometrically validated approach ensures that items strongly correlated with specific values serve as reliable items for assessing those values. Through evaluating 44 LLMs with our benchmark, we find that these models prioritize Benevolence, Security, and Self-Direction values while placing less emphasis on Tradition, Power, and Achievement values. Also, our analysis reveals biases in how LLMs perceive various demographic groups, deviating from real human data.

## Dataset Information

Psychometrically validated items with human-subject correlation data; evaluates 10 Schwartz value dimensions

## Data Description

Value Portrait is a psychometrically validated benchmark for evaluating LLM value orientations using 520 query-response pairs annotated with correlations to Schwartz's 10 basic values and Big Five personality traits. The benchmark was constructed using GPT-4o for response generation and validated via a Prolific survey with 681 participants. Forty-four LLMs were evaluated, revealing consistent prioritization of Benevolence, Security, and Self-Direction values, with analyses of demographic biases and value steering effectiveness.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 19, Agent 1
**Implementation Readiness:** HIGH

## Tags

