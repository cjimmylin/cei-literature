---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: V6Q5Z2GT
type: journalArticle
short_title: AEGIS
year: 2024
first_author: "[[Shaona Ghosh]]"
last_author: "[[Christopher Parisien]]"
authors: "Shaona Ghosh; Prasoon Varshney; Erick Galinkin; Christopher Parisien"
url: "https://arxiv.org/abs/2404.05993"
external_pdf: "https://arxiv.org/pdf/2404.05993.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced the AEGIS taxonomy (13 critical/9 sparse risks) and the AEGISSAFETYDATASET (26k annotated human-LLM interactions), along with an online adaptive framework for content moderation."
significance: "Fills a gap in high-quality, comprehensive safety datasets and provides a way to adaptively moderate content at scale with strong theoretical guarantees, improving robustness against jailbreak attacks."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Ghosh-AEGIS.md"
abstract: "As Large Language Models (LLMs) and generative AI become more widespread, the content safety risks associated with their use also increase. We find a notable deficiency in high-quality content safety datasets and benchmarks that comprehensively cover a wide range of critical safety areas. To address this, we define a broad content safety risk taxonomy, comprising 13 critical risk and 9 sparse risk categories."
paper_summary: "Abstract: As Large Language Models (LLMs) and generative AI become more widespread, the content safety risks associated with their use also increase. We find a notable deficiency in high-quality content safety  | Overview: AEGIS: Online Adaptive AI Content Safety Moderation with Ensemble of LLM Experts Shaona Ghosh∗ shaonag@nvidia.com Prasoon Varshney prasoonv@nvidia.com Erick Galinkin egalinkin@nvidia.com Christopher P | Key Findings: setting as in the previous datasets. The test suite comprises 100 test prompts across five harm areas relevant for the majority of LLM applications. A | Conclusions: As large generative models undergo prolific adoption, it is imperative to build high quality safety systems to moderate LLM interactions. Towards this"
local_pdf: "[[PDFs/2024/2024-Ghosh-AEGIS.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Llama-2, GPT-4, Mistral"
DATA_URL: "https://github.com/meta-llama/llama-recipes"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# AEGIS: Online Adaptive AI Content Safety Moderation at Scale

## Metadata

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Ghosh-AEGIS.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2404.05993

## Abstract

As Large Language Models (LLMs) and generative AI become more widespread, the content safety risks associated with their use also increase. We find a notable deficiency in high-quality content safety datasets and benchmarks that comprehensively cover a wide range of critical safety areas. To address this, we define a broad content safety risk taxonomy, comprising 13 critical risk and 9 sparse risk categories. Additionally, we curate AEGISSAFETYDATASET, a new dataset of approximately 26, 000 human-LLM interaction instances, complete with human annotations adhering to the taxonomy. We plan to release this dataset to the community to further research and to help benchmark LLM models for safety. To demonstrate the effectiveness of the dataset, we instruction-tune multiple LLM-based safety models. We show that our models (named AEGISSAFETYEXPERTS), not only surpass or perform competitively with the state-of-the-art LLM-based safety models and general purpose LLMs, but also exhibit robustness across multiple jail-break attack categories. We also show how using AEGISSAFETYDATASET during the LLM alignment phase does not negatively impact the performance of the aligned models on MT Bench scores. Furthermore, we propose AEGIS, a novel application of a no-regret online adaptation framework with strong theoretical guarantees, to perform content moderation with an ensemble of LLM content safety experts in deployment

## Authors

[[Shaona Ghosh]], [[Prasoon Varshney]], [[Erick Galinkin]], [[Christopher Parisien]]

## Data Description

AEGISSAFETYDATASET is a content safety dataset of approximately 26,000 human-LLM interaction instances with human annotations across 13 critical risk and 9 sparse risk categories. The dataset was generated using Mistral to produce responses to prompts from the Anthropic hh-rlhf dataset, annotated by 12 annotators with 86,736 total annotations and approximately 74% inter-annotator agreement. AEGISSAFETYEXPERTS models were instruction-tuned on Llama Guard (Llama-2-7B based) and NEMO43B, and evaluated against GPT-4 and other baselines across multiple safety benchmarks.


## Notes


## Citation Info

60 citations (Semantic Scholar/arXiv) [2025-08-27]
