---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LEH5YGEV
type: conferencePaper
short_title: FFB
year: 2025
first_author: "[[Xiaotian Han]]"
last_author: "[[Xia Hu]]"
authors: "Xiaotian Han; Jianfeng Chi; Yu Chen; Qifan Wang; Han Zhao; Na Zou; Xia Hu"
doi: 10.48550/arXiv.2306.09468
url: "http://arxiv.org/abs/2306.09468"
external_pdf: "http://arxiv.org/pdf/2306.09468.pdf"
publication: "International Conference on Learning Representations"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Introduced the 'Fair Fairness Benchmark' (FFB), a standardized framework for evaluating *in-processing* fairness methods (algorithms that fix bias *during* training), conducting 45k experiments."
significance: "Addresses the reproducibility crisis in fairness research, providing a unified codebase to verify if methods like 'Adversarial Debiasing' actually work across different datasets."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Han-FFB.md"
abstract: "This paper introduces the Fair Fairness Benchmark (FFB), a benchmarking framework for in-processing group fairness methods. Ensuring fairness in machine learning is important for ethical compliance. However, there exist challenges in comparing and developing fairness methods due to inconsistencies in experimental settings, lack of accessible algorithmic implementations, and limited extensibility of current fairness packages and tools."
paper_summary: "Abstract: This paper introduces the Fair Fairness Benchmark (FFB), a benchmarking frame- work for in-processing group fairness methods. Ensuring fairness in machine learning is important for ethical compliance. | Overview: Published as a conference paper at ICLR 2024 FFB: A FAIR FAIRNESS BENCHMARK FOR IN- PROCESSING GROUP FAIRNESS METHODS Xiaotian Han1∗Jianfeng Chi2 Yu Chen3 Qifan Wang2 Han Zhao4 Na Zou5 Xia Hu6 1Texas  | Methodology: lacks a comprehensive comparison, such as the training curves and stability, the influence of the utility-fairness trade-off parameters, and how to se"
local_pdf: "[[PDFs/2023/2023-Han-FFB.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "BERT"
DATA_URL: "https://github.com/ahxt/fair_fairness_benchmark"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# FFB: A Fair Fairness Benchmark for In-Processing Group Fairness Methods

## Metadata

**Authors:** Han, Xiaotian; Chi, Jianfeng; Chen, Yu; Wang, Qifan; Zhao, Han; Zou, Na; Hu, Xia

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2306.09468](https://doi.org/10.48550/arXiv.2306.09468)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Han-FFB.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2306.09468
- **DOI:** https://doi.org/10.48550/arXiv.2306.09468

## Abstract

This paper introduces the Fair Fairness Benchmark (FFB), a benchmarking framework for in-processing group fairness methods. Ensuring fairness in machine learning is important for ethical compliance. However, there exist challenges in comparing and developing fairness methods due to inconsistencies in experimental settings, lack of accessible algorithmic implementations, and limited extensibility of current fairness packages and tools. To address these issues, we introduce an opensource standardized benchmark for evaluating in-processing group fairness methods and provide a comprehensive analysis of state-of-the-art methods to ensure different notions of group fairness. This work offers the following key contributions: the provision of flexible, extensible, minimalistic, and research-oriented open-source code; the establishment of unified fairness method benchmarking pipelines; and extensive benchmarking, which yields key insights from 45, 079 experiments, 14, 428 GPU hours. We believe that our work will significantly facilitate the growth and development of the fairness research community. The benchmark is available at https://github.com/ahxt/fair_fairness_benchmark.

## Authors

[[Xiaotian Han]], [[Jianfeng Chi]], [[Yu Chen]], [[Qifan Wang]], [[Han Zhao]], [[Na Zou]], [[Xia Hu]]

## Data Description

FFB (Fair Fairness Benchmark) is a standardized benchmarking framework for evaluating in-processing group fairness methods in machine learning. It encompasses 14 tabular and image datasets (including Adult, German, COMPAS, CelebA, UTKFace), 9 fairness metrics, and multiple bias mitigation algorithms across 45,079 experiments and 14,428 GPU hours. The benchmark focuses on binary classification with binary sensitive attributes, not LLM assessment.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 35 citations (Semantic Scholar/DOI) [2025-08-27]
