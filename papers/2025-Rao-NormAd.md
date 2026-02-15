---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QU2HEQDA
type: conferencePaper
short_title: NormAd
year: 2025
first_author: "[[Abhinav Rao]]"
last_author: "[[Maarten Sap]]"
authors: "Abhinav Rao; Akhila Yerukola; Vishwa Shah; Katharina Reinecke; Maarten Sap"
doi: 10.18653/v1/2025.naacl-long.120
tags: 
url: "http://arxiv.org/abs/2404.12464"
external_pdf: "http://arxiv.org/pdf/2404.12464.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Social & Cultural Values"
key_contribution: "Introduced 'NormAd' and the 'NormAd-Eti' benchmark (2.6k norms from 75 countries) to test LLMs' *cultural adaptability* – can the model switch etiquette based on the country?"
significance: "Shows that while models know *facts* about countries, they fail to *apply* them in judgment (e.g., judging a French greeting by American norms), especially for the Global South."
pdf_extract: "PDF Extracts/2025/2025-Rao-NormAd.md"
abstract: "To be effectively and safely deployed to global user populations, large language models (LLMs) may need to adapt outputs to user values and cultures, not just know about them. We introduce NORMAD, an evaluation framework to assess LLMs’ cultural adaptability, specifically measuring their ability to judge social acceptability across varying levels of cultural norm specificity, from abstract values to explicit social norms."
paper_summary: "Abstract: To be effectively and safely deployed to global user populations, large language models (LLMs) may need to adapt outputs to user val- ues and cultures, not just know about them. We introduce NORMAD, a | Overview: NORMAD: A Framework for Measuring the Cultural Adaptability of Large Language Models Abhinav Rao*† Akhila Yerukola*† Vishwa Shah† Katharina Reinecke‡ Maarten Sap† †Language Technologies Institute, Car | Key Findings: As a pragmatic way for approaching culture, much research, in- cluding our own through NORMAD-ETI, often treats the dynamic and multifaceted nature of | Conclusions: In this work, we introduce a novel hierarchical evaluation framework, NORMAD, to assess the contextual adaptability of LLMs, a departure from most pri"
local_pdf: [[PDFs/2025/2025-Rao-NormAd.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama, Llama-2, Mistral"
DATA_URL: "https://github.com/Akhila-Yerukola/NormAd"
---
# NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models

## Metadata

**Authors:** Rao, Abhinav; Yerukola, Akhila; Shah, Vishwa; Reinecke, Katharina; Sap, Maarten

**Year:** 2025

**Publication:** Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2025.naacl-long.120](https://doi.org/10.18653/v1/2025.naacl-long.120)

**Pages:** 2373-2403

## Links

- **Local PDF:** [[PDFs/2025/2025-Rao-NormAd.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2404.12464
- **DOI:** https://doi.org/10.18653/v1/2025.naacl-long.120

## Abstract

To be effectively and safely deployed to global user populations, large language models (LLMs) may need to adapt outputs to user values and cultures, not just know about them. We introduce NormAd, an evaluation framework to assess LLMs' cultural adaptability, specifically measuring their ability to judge social acceptability across varying levels of cultural norm specificity, from abstract values to explicit social norms. As an instantiation of our framework, we create NormAd-Eti, a benchmark of 2.6k situational descriptions representing social-etiquette related cultural norms from 75 countries. Through comprehensive experiments on NormAd-Eti, we find that LLMs struggle to accurately judge social acceptability across these varying degrees of cultural contexts and show stronger adaptability to English-centric cultures over those from the Global South. Even in the simplest setting where the relevant social norms are provided, the best LLMs' performance (< 82\%) lags behind humans (> 95\%). In settings with abstract values and country information, model performance drops substantially (< 60\%), while human accuracy remains high (> 90\%). Furthermore, we find that models are better at recognizing socially acceptable versus unacceptable situations. Our findings showcase the current pitfalls in socio-cultural reasoning of LLMs which hinder their adaptability for global audiences.

## Authors

[[Abhinav Rao]], [[Akhila Yerukola]], [[Vishwa Shah]], [[Katharina Reinecke]], [[Maarten Sap]]

## Data Description

NormAd-ETI is a benchmark of 2,633 situational descriptions representing social etiquette-related cultural norms from 75 countries, sourced from the Cultural Atlas resource. Each situation includes a question-answer pair for evaluating social acceptability under three levels of cultural context specificity: Rule-of-Thumb, Country+Value, and Country alone. The dataset spans four subcategories (Basic Etiquette, Eating, Visiting, Gift-Giving) with three label types (Yes, No, Neutral).


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

72 citations (Semantic Scholar/DOI) [2025-08-27] 7 citations (Semantic Scholar/arXiv) [2025-08-23] 1 citations (Crossref/DOI) [2025-08-23]
