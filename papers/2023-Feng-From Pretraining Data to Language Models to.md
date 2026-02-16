---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UMMN7MU2
type: conferencePaper
short_title: "From Pretraining Data to Language Models to"
year: 2025
first_author: "[[Shangbin Feng]]"
last_author: "[[Yulia Tsvetkov]]"
authors: "Shangbin Feng; Chan Young Park; Yuhan Liu; Yulia Tsvetkov"
doi: 10.48550/arXiv.2305.08283
tags: 
url: "http://arxiv.org/abs/2305.08283"
external_pdf: "http://arxiv.org/pdf/2305.08283.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Traces the propagation of political biases (social/economic) from pretraining corpora through LMs to downstream tasks (hate speech, misinformation detection)."
significance: "Empirically quantifies the 'pipeline of bias', showing that 'neutral' downstream models inherit political leanings from pretraining data that reinforce polarization and unfairness in high-stakes applications."
pdf_extract: "PDF Extracts/2023/2023-Feng-From Pretraining Data to Language Models to.md"
abstract: "Language models (LMs) are pretrained on diverse data sources, including news, discussion forums, books, and online encyclopedias. A significant portion of this data includes opinions and perspectives which, on one hand, celebrate democracy and diversity of ideas, and on the other hand are inherently socially biased. Our work develops new methods to (1) measure political biases in LMs trained on such corpora, along social and economic axes, and (2) measure the fairness of downstream NLP models..."
paper_summary: "Abstract: Language models (LMs) are pretrained on di- verse data sources, including news, discussion forums, books, and online encyclopedias. A sig- nificant portion of this data includes opinions and perspecti | Overview: From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models Shangbin Feng1 Chan Young Park2 Yuhan Liu3 Yulia Tsvetkov1 1Universit | Methodology: We propose a two-step methodology to establish the effect of political biases in pretraining corpora on the fairness of downstream tasks: (1) we devel | Key Findings: framework, we investigate the impact of these bi- ases on downstream tasks with social implications such as hate speech detection and misinformation i | Conclusions: forums, books, and online encyclopedias. A sig- nificant portion of this data includes opinions and perspectives which, on one hand, celebrate democra"
local_pdf: "[[PDFs/2023/2023-Feng-From Pretraining Data to Language Models to.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology text corpus for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: "BERT, RoBERTa, ALBERT, BART, GPT-2, GPT-3, GPT-4, ChatGPT, Alpaca, Llama"
DATA_URL: "https://github.com/BunsenFeng/PoliLean"
---
# From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models

## Metadata

**Authors:** Feng, Shangbin; Park, Chan Young; Liu, Yuhan; Tsvetkov, Yulia

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2305.08283](https://doi.org/10.48550/arXiv.2305.08283)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Feng-From Pretraining Data to Language Models to.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2305.08283
- **DOI:** https://doi.org/10.48550/arXiv.2305.08283

## Abstract

Language models (LMs) are pretrained on diverse data sources, including news, discussion forums, books, and online encyclopedias. A significant portion of this data includes opinions and perspectives which, on one hand, celebrate democracy and diversity of ideas, and on the other hand are inherently socially biased. Our work develops new methods to (1) measure political biases in LMs trained on such corpora, along social and economic axes, and (2) measure the fairness of downstream NLP models trained on top of politically biased LMs. We focus on hate speech and misinformation detection, aiming to empirically quantify the effects of political (social, economic) biases in pretraining data on the fairness of high-stakes social-oriented tasks. Our findings reveal that pretrained LMs do have political leanings that reinforce the polarization present in pretraining corpora, propagating social biases into hate speech predictions and misinformation detectors. We discuss the implications of our findings for NLP research and propose future directions to mitigate unfairness.

## Authors

[[Shangbin Feng]], [[Chan Young Park]], [[Yuhan Liu]], [[Yulia Tsvetkov]]

## Data Description

The study uses the PoliLean framework to measure political biases in 14 language models along social and economic axes using a political compass test with 62 political statements. Downstream evaluation uses three datasets: HATE-IDENTITY (159,872 datapoints), HATE-DEMOGRAPHIC (276,872 datapoints) for hate speech detection with identity group annotations, and a MISINFORMATION dataset (29,556 datapoints) from PolitiFact. The partisan pretraining corpora span six categories combining domain (Reddit, News) and political leaning (Left, Center, Right).


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

271 citations (Semantic Scholar/DOI) [2025-08-27] 271 citations (Semantic Scholar/arXiv) [2025-08-27] 268 citations (Semantic Scholar/DOI) [2025-08-23]
