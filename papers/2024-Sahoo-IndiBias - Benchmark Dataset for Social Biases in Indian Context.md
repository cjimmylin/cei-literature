---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0183
type: conferencePaper
short_title: "IndiBias -- Benchmark Dataset for Social Biases in Indian Context"
year: 2024
first_author: "[[Sahoo, Nihar Ranjan]]"
last_author: "[[Bhattacharyya, Pushpak]]"
authors: "[[Sahoo, Nihar Ranjan]]; [[Kulkarni, Pranamya Prashant]]; [[Asad, Narjis]]; [[Ahmad, Arif]]; [[Goyal, Tanu]]; [[Garimella, Aparna]]; [[Bhattacharyya, Pushpak]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2403.20147"
external_pdf: "https://arxiv.org/pdf/2403.20147.pdf"
pdf_extract: "PDF Extracts/2024/2024-Sahoo-IndiBias - Benchmark Dataset for Social Biases in Indian Context.md"
local_pdf: "[[PDFs/2024/2024-Sahoo-IndiBias - Benchmark Dataset for Social Biases in Indian Context.pdf]]"
publication: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "Indian"
cultures_nationalities_list: "Indian"
languages_list: "English, Hindi"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Warning: This paper contains examples and case studies that may be offensive. The pervasive influence of social biases in language data has sparked the need for benchmark datasets that capture and evaluate these biases in Large Language Models (LLMs). Existing efforts predominantly focus on English language and the Western context, leaving a void for a reliable dataset that encapsulates India’s unique socio-cultural nuances."
LLM_assessed: "Llama-2, Mistral, BLOOM, T5"
DATA_URL: "https://github.com/sahoonihar/IndiBias"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# IndiBias -- Benchmark Dataset for Social Biases in Indian Context

## Authors

[[Sahoo, Nihar Ranjan]], [[Kulkarni, Pranamya Prashant]], [[Asad, Narjis]], [[Ahmad, Arif]], [[Goyal, Tanu]], [[Garimella, Aparna]], [[Pushpak Bhattacharyya|Bhattacharyya, Pushpak]]

## Metadata

**Authors:** Sahoo, Nihar Ranjan; Kulkarni, Pranamya Prashant; Asad, Narjis; Ahmad, Arif; Goyal, Tanu; Garimella, Aparna; Bhattacharyya, Pushpak

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **arXiv:** https://arxiv.org/abs/2403.20147
- **Code/Data:** https://github.com/sahoonihar/IndiBias

## Abstract

Warning: This paper contains examples and case studies that may be offensive. The pervasive influence of social biases in language data has sparked the need for benchmark datasets that capture and evaluate these biases in Large Language Models (LLMs). Existing efforts predominantly focus on English language and the Western context, leaving a void for a reliable dataset that encapsulates India’s unique socio-cultural nuances. To bridge this gap, we introduce IndiBias, a comprehensive benchmarking dataset designed specifically for evaluating social biases in the Indian context. We filter and translate the existing CrowS-Pairs dataset to create a benchmark dataset suited to the Indian context in Hindi language. Additionally, we leverage LLMs including ChatGPT and InstructGPT to augment our dataset with diverse societal biases and stereotypes prevalent in India. The included bias dimensions encompass gender, religion, caste, age, region, physical appearance, and occupation. We also build a resource to address intersectional biases along three intersectional dimensions. Our dataset contains 800 sentence pairs and 300 tuples for bias measurement across different demographics. The dataset is available in English and Hindi, providing a size comparable to existing benchmark datasets. Furthermore, using IndiBias we compare ten different language models on multiple bias measurement metrics. We observed that the language models exhibit more bias across a majority of the intersectional groups. All the scripts utilized and datasets created in this study are publicly available1.

## Dataset Information

800 sentence pairs + 300 tuples for intersectional bias

## Data Description

IndiBias is a benchmark dataset for measuring social biases in language models in the Indian context. It contains 800 sentence pairs in English and Hindi (adapted from CrowS-Pairs and augmented via LLMs), 300 stereotypical attribute tuples across seven bias dimensions (gender, religion, caste, age, region, physical appearance, occupation), and approximately 1,000 bleached sentences for evaluating intersectional biases along gender-religion, gender-caste, and gender-age axes.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

