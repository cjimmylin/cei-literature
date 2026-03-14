---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XTHGVLPS
type: conferencePaper
short_title: "Can Language Models Reason about Individualistic"
year: 2024
first_author: "[[Liwei Jiang]]"
last_author: "[[Yejin Choi]]"
authors: "Liwei Jiang; Taylor Sorensen; Sydney Levine; Yejin Choi"
doi: 10.48550/arXiv.2410.03868
tags: 
url: "http://arxiv.org/abs/2410.03868"
external_pdf: "http://arxiv.org/pdf/2410.03868.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
CONF-CC: "ACL 2024"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced INDIEVALUECATALOG to test whether LLMs can reason about *individualistic* values (predicting a specific person's values from their other statements), finding modest accuracy (55-65%)."
significance: "Argues for 'individualistic alignment'—modeling the specific, unique value profile of a user—demonstrating that current models rely too much on broad group demographics rather than individual coherence."
pdf_extract: "PDF Extracts/2024/2024-Jiang-Can Language Models Reason about Individualistic.md"
abstract: "Recent calls for pluralistic alignment emphasize that AI systems should address the diverse needs of all people. Yet, efforts in this space often require sorting people into fixed buckets of pre-specified diversity-defining dimensions (e.g., demographics), risking smoothing out individualistic variations or even stereotyping. To achieve an authentic representation of diversity that respects individuality, we propose individualistic alignment."
paper_summary: "Abstract: Recent calls for pluralistic alignment empha- size that AI systems should address the diverse needs of all people. Yet, efforts in this space often require sorting people into fixed buck- ets of pre-s | Overview: arXiv:2410.03868v2 [cs.CL] 31 May 2025 Can Language Models Reason about Individualistic Human Values and Preferences? Liwei Jiang♠* Taylor Sorensen♠ Sydney Levine♣∗ Yejin Choi♡ University of Washingto | Methodology: The rich data in INDIEVALUECATALOG allows us to train a series of Individualistic Value Rea- soner models (INDIEVALUEREASONER) based on Llama-3.1-8B.  | Key Findings: Population Figure 6: Continent-specific INDIEVALUEREASONER evaluated with continent-specific test sets. Similar value demonstration trajectories can h | Conclusions: We propose a bottom-up approach to pluralistic value learning by inducing individualistic values bottom-up. We harvest the well-established social sci"
local_pdf: "[[PDFs/2024/2024-Jiang-Can Language Models Reason about Individualistic.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Claude-3.5-Sonnet, GPT-4, GPT-4o, GPT-4o mini, Llama-3, Mixtral, Qwen-2"
DATA_URL: "https://github.com/liweijiang/indievalue"
CONFERENCE: "ACL 2024"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Can Language Models Reason about Individualistic Human Values and Preferences?

## Metadata

**Authors:** Jiang, Liwei; Sorensen, Taylor; Levine, Sydney; Choi, Yejin

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.03868](https://doi.org/10.48550/arXiv.2410.03868)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Jiang-Can Language Models Reason about Individualistic.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.03868
- **DOI:** https://doi.org/10.48550/arXiv.2410.03868

## Abstract

Recent calls for pluralistic alignment emphasize that AI systems should address the diverse needs of all people. Yet, efforts in this space often require sorting people into fixed buckets of pre-specified diversity-defining dimensions (e.g., demographics), risking smoothing out individualistic variations or even stereotyping. To achieve an authentic representation of diversity that respects individuality, we propose individualistic alignment.1 While individualistic alignment can take various forms, we introduce INDIEVALUECATALOG, a dataset transformed from the influential World Values Survey (WVS), to study language models (LMs) on the specific challenge of individualistic value reasoning. Given a sample of an individual’s value-expressing statements, models are tasked with predicting this person’s value judgments in novel cases. With INDIEVALUECATALOG, we reveal critical limitations in frontier LMs, which achieve only 55 % to 65% accuracy in predicting individualistic values. Moreover, our results highlight that a precise description of individualistic values cannot be approximated only with demographic information. We also identify a partiality of LMs in reasoning about global individualistic values, as measured by our proposed VALUE INEQUITY INDEX (σINEQUITY). Finally, we train a series of INDIEVALUEREASONERS to reveal new patterns and dynamics into global human values.

## Authors

[[Liwei Jiang]], [[Taylor Sorensen]], [[Sydney Levine]], [[Yejin Choi]]

## Data Description

IndieValueCatalog dataset transformed from the World Values Survey (WVS) containing value-expressing statements from 93K real humans across 70+ countries, for evaluating LMs on individualistic value reasoning.


## Notes


## Tags

#Computer-Science---Computation-and-Language
