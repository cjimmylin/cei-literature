---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JHYWDXIZ
type: journalArticle
short_title: WorldValuesBench
year: 2025
first_author: "[[Wenlong Zhao]]"
last_author: "[[Yuling Gu]]"
authors: "Wenlong Zhao; Debanjan Mondal; Niket Tandon; Danica Dillion; Kurt Gray; Yuling Gu"
url: "https://arxiv.org/abs/2404.16308"
external_pdf: "https://arxiv.org/pdf/2404.16308.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Social & Cultural Values"
key_contribution: "Constructed WorldValuesBench (20M examples) from the World Values Survey to test LLMs' 'value awareness' across diverse global demographics."
significance: "Shows that leading models (GPT-3.5, etc.) struggle to predict the values of non-Western demographics, highlighting a 'value alignment' failure for the global majority."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Wu-WorldValuesBench.md"
abstract: "The awareness of multi-cultural human values is critical to the ability of language models (LMs) to generate safe and personalized responses. However, this awareness of LMs has been insufficiently studied, since the computer science community lacks access to the large-scale real-world data about multi-cultural values. In this paper, we present WORLDVALUESBENCH, a globally diverse, large-scale benchmark dataset for the multi-cultural value prediction task, which requires a model to generate a rat"
paper_summary: "Abstract: The awareness of multi-cultural human values is critical to the ability of language models (LMs) to generate safe and personalized responses. However, this awareness of LMs has been insufficiently stu | Overview: WORLDVALUESBENCH: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models Wenlong Zhao1∗, Debanjan Mondal1∗, Niket Tandon2, Danica Dillion3, Kurt Gray3, Yuling Gu2 1Unive | Key Findings: method based on the Wasserstein 1-distance. • We exemplify the usage of our dataset with a case study and show that multi-cultural value awareness rem | Conclusions: We propose WORLDVALUESBENCH, an NLP adap- tation of an influential social science world values survey, that has more than 20 million examples of the t"
local_pdf: [[PDFs/2024/2024-Wu-WorldValuesBench.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Social & Cultural Values"
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, Alpaca, Vicuna, Mixtral"
DATA_URL: "https://github.com/Demon702/WorldValuesBench"
---
# WorldValuesBench: A Large-Scale Benchmark Dataset for Multi-Cultural Value Awareness of Language Models

## Metadata

**Authors:** Wu, Z.; Ethayarajh, K.

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Wu-WorldValuesBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2404.16308

## Abstract

The awareness of multi-cultural human values is critical to the ability of language models (LMs) to generate safe and personalized responses. However, this awareness of LMs has been insufficiently studied, since the computer science community lacks access to the large-scale real-world data about multi-cultural values. In this paper, we present WorldValuesBench, a globally diverse, large-scale benchmark dataset for the multi-cultural value prediction task, which requires a model to generate a rating response to a value question based on demographic contexts. Our dataset is derived from an influential social science project, World Values Survey (WVS), that has collected answers to hundreds of value questions (e.g., social, economic, ethical) from 94,728 participants worldwide. We have constructed more than 20 million examples of the type "(demographic attributes, value question) $\rightarrow$ answer" from the WVS responses. We perform a case study using our dataset and show that the task is challenging for strong open and closed-source models. On merely $11.1\%$, $25.0\%$, $72.2\%$, and $75.0\%$ of the questions, Alpaca-7B, Vicuna-7B-v1.5, Mixtral-8x7B-Instruct-v0.1, and GPT-3.5 Turbo can respectively achieve $<0.2$ Wasserstein 1-distance from the human normalized answer distributions. WorldValuesBench opens up new research avenues in studying limitations and opportunities in multi-cultural value awareness of LMs.

## Authors

[[Wenlong Zhao]], [[Debanjan Mondal]], [[Niket Tandon]], [[Danica Dillion]], [[Kurt Gray]], [[Yuling Gu]]

## Data Description

WorldValuesBench is a globally diverse, large-scale benchmark dataset for multi-cultural value prediction, derived from the World Values Survey Wave 7 with over 20 million examples from 94,728 participants worldwide. The benchmark evaluates whether language models can generate culturally appropriate rating answers to value questions conditioned on demographic attributes across 64 countries.


## Notes


## Citation Info

166 citations (Semantic Scholar/arXiv) [2025-08-27]
