---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y3C82YLH
type: journalArticle
short_title: "The Hallucination Tax of Reinforcement Finetuning"
year: 2025
first_author: "[[Linxin Song]]"
last_author: "[[Jieyu Zhao]]"
authors: "Linxin Song; Taiwei Shi; Jieyu Zhao"
url: "https://arxiv.org/abs/2505.13988"
external_pdf: "https://arxiv.org/pdf/2505.13988.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Song-The Hallucination Tax of Reinforcement Finetuning.md"
abstract: "Reinforcement finetuning (RFT) has become a standard approach for enhancing the reasoning capabilities of large language models (LLMs). However, its impact on model trustworthiness remains underexplored. In this work, we identify and systematically study a critical side effect of RFT, which we term the hallucination tax: a degradation in refusal behavior causing models to produce hallucinated answers to unanswerable questions confidently."
paper_summary: "Abstract: Reinforcement finetuning (RFT) has become a standard approach for enhancing the reasoning capabilities of large language models (LLMs). However, its impact on model trustworthiness remains underexplor | Overview: arXiv:2505.13988v1 [cs.CL] 20 May 2025 The Hallucination Tax of Reinforcement Finetuning Linxin Song* Taiwei Shi* Jieyu Zhao University of Southern California {linxinso, taiweish, jieyuz}@usc.edu Data | Key Findings: Datasets. We aim to evaluate the hallucination tax and the overall performance of LLMs on logi- cal reasoning tasks after RFT using a mixed train- ing | Conclusions: Our results highlight a key unintended consequence of RFT: the erosion of refusal behavior when faced with unanswerable questions—a phenomenon we term"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Song-The Hallucination Tax of Reinforcement Finetuning.pdf]]"
CONF-CC: "EMNLP 2025"
DATE_ADDED: 20260208
LLM_assessed: "Llama-3, Qwen"
DATA_URL: "https://huggingface.co/datasets/lime-nlp/Synthetic_Unanswerable_Math"
CONFERENCE: Journal
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Text corpus for question answering"
data_metrics: "Not specified"
---
# The Hallucination Tax of Reinforcement Finetuning

## Metadata

**Authors:** Song, Linxin; Shi, Taiwei; Zhao, Jieyu

**Year:** 2025

**Publication:** arXiv preprint arXiv:2505.13988

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Song-The Hallucination Tax of Reinforcement Finetuning.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2505.13988

## Abstract

Reinforcement finetuning (RFT) has become a standard approach for enhancing the reasoning capabilities of large language models (LLMs). However, its impact on model trustworthiness remains underexplored. In this work, we identify and systematically study a critical side effect of RFT, which we term the hallucination tax: a degradation in refusal behavior causing models to produce hallucinated answers to unanswerable questions confidently. To investigate this, we introduce SUM (Synthetic Unanswerable Math), a high-quality dataset of unanswerable math problems designed to probe models' ability to recognize an unanswerable question by reasoning from the insufficient or ambiguous information. Our results show that standard RFT training could reduce model refusal rates by more than 80%, which significantly increases model's tendency to hallucinate. We further demonstrate that incorporating just 10% SUM during RFT substantially restores appropriate refusal behavior, with minimal accuracy trade-offs on solvable tasks. Crucially, this approach enables LLMs to leverage inference-time compute to reason about their own uncertainty and knowledge boundaries, improving generalization not only to out-of-domain math problems but also to factual question answering tasks.

## Authors

[[Linxin Song]], [[Taiwei Shi]], [[Jieyu Zhao]]

## Data Description

SUM (Synthetic Unanswerable Math): a high-quality dataset of unanswerable math problems designed to probe models' ability to recognize insufficient or ambiguous information, used to study hallucination tax from reinforcement finetuning.


## Notes


## Citation Info

47 citations (Semantic Scholar/arXiv) [2025-08-27]
