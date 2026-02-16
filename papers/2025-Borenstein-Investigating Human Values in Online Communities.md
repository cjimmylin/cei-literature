---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0151
type: conferencePaper
short_title: Investigating Human Values in Online Communities
year: 2025
first_author: "[[Nadav Borenstein]]"
last_author: "[[Isabelle Augenstein]]"
authors: Nadav Borenstein, Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein
doi: 10.18653/v1/2025.naacl-long.77
url: "https://aclanthology.org/2025.naacl-long.77/"
external_pdf: "https://arxiv.org/pdf/2402.14177.pdf"
publication: NAACL 2025
local_pdf: "[[PDFs/2025-Borenstein-Investigating Human Values in Online Communities.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Borenstein-Investigating Human Values in Online Communities.md"
DATE_ADDED: 20260215
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American, Multicultural/Cross-cultural"
cultures_nationalities_list: "Cross-cultural, Various"
languages_list: 
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/copenlu/HumanValues"
tags: 
abstract: "Studying human values is instrumental for cross-cultural research, enabling a better understanding of preferences and behaviour of society at large and communities therein. To study the dynamics of communities online, we propose a method to computationally analyse values present on Reddit. Our method allows analysis at scale, complementing survey based approaches. We train a value relevance and a value polarity classifier, which we thoroughly evaluate using in-domain and out-of-domain human..."
ethics_perspective: "Moral Reasoning & Psychology"
---
# Investigating Human Values in Online Communities

## Authors

[[Nadav Borenstein, Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein]]

## Metadata

**Authors:** Nadav Borenstein, Arnav Arora, Lucie-Aimee Kaffee, Isabelle Augenstein

**Year:** 2025

**Type:** conferencePaper

**Venue:** NAACL 2025

**DOI:** [10.18653/v1/2025.naacl-long.77](https://doi.org/10.18653/v1/2025.naacl-long.77)

**Cultures:** Cross-cultural, Various

## Links

- **arXiv:** https://arxiv.org/abs/2402.14177
- **DOI:** https://doi.org/10.18653/v1/2025.naacl-long.77
- **URL:** https://aclanthology.org/2025.naacl-long.77/

## Abstract

Proposes computational method to analyse Schwartz values on Reddit at scale. Trains value relevance and polarity classifiers, automatically annotating 6 million+ posts across 12k subreddits with Schwartz values.

## Data Description

The paper creates a dataset of over 9 million Reddit posts across 12,000 subreddits annotated with Schwartz human values using trained DeBERTa classifiers for value relevance and stance detection. The value extraction models were trained on the ValueNet and ValueArg datasets, achieving macro-F1 of 0.76 for relevance and F1 of 0.72 for stance. No LLMs were benchmarked; the paper uses fine-tuned transformer classifiers.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_28
**Relevance:** Computational analysis of human values (Schwartz framework) in online communities; trains classifiers for value detection that could benchmark LLM value alignment.

## Tags

