---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VH3SW4EV
type: document
short_title: "Evaluating Object Hallucination in Large"
year: 2023
first_author: "[[Yifan Li]]"
last_author: "[[Ji-Rong Wen]]"
authors: "Yifan Li; Yifan Du; Kun Zhou; Jinpeng Wang; Wayne Xin Zhao; Ji-Rong Wen"
url: "https://arxiv.org/abs/2305.10355"
external_pdf: "https://arxiv.org/pdf/2305.10355.pdf"
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
pdf_extract: "PDF Extracts/2023/2023-Li-Evaluating Object Hallucination in Large.md"
abstract: "Inspired by the superior language abilities of large language models (LLM), large visionlanguage models (LVLM) have been recently proposed by integrating powerful LLMs for improving the performance on complex multimodal tasks. Despite the promising progress on LVLMs, we find that they suffer from object hallucinations, i.e., they tend to generate objects inconsistent with the target images in the descriptions."
paper_summary: "Abstract: Inspired by the superior language abilities of large language models (LLM), large vision- language models (LVLM) have been recently proposed by integrating powerful LLMs for improving the performance  | Overview: Evaluating Object Hallucination in Large Vision-Language Models Yifan Li1,3∗, Yifan Du1,3∗, Kun Zhou2∗, Jinpeng Wang 4, Wayne Xin Zhao2,3† and Ji-Rong Wen1, 2,3 1Gaoling School of Artificial Intellige | Key Findings: Yes, there is a pear in the image. Is there a pear in the image? Adversarial settings POPE Yes, there is a knife in the image. Is there a knife in the | Conclusions: In this work, we conducted evaluation experiments on several LVLMs and examined how they suffer from the object hallucination issue. By investigat- in"
local_pdf: "[[Lit-WS-PDFs/2023/2023-Li-Evaluating Object Hallucination in Large.pdf]]"
CONF-CC: "EMNLP 2023"
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://github.com/RUCAIBox/POPE"
CONFERENCE: Preprint
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
author_country: CN
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 36
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation methodology"
data_metrics: "Not specified"
---
# Evaluating Object Hallucination in Large Vision-Language Models (POPE)

## Metadata

**Authors:** Li, Yifan; Du, Yifan; Zhou, Kun; Wang, Jinpeng; Zhao, Wayne Xin; Wen, Ji-Rong

**Year:** 2023

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-PDFs/2023/2023-Li-Evaluating Object Hallucination in Large.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2305.10355

## Abstract

Inspired by the superior language abilities of large language models (LLM), large vision-language models (LVLM) have been recently explored by integrating powerful LLMs for improving the performance on complex multimodal tasks. Despite the promising progress on LVLMs, we find that LVLMs suffer from the hallucination problem, i.e. they tend to generate objects that are inconsistent with the target images in the descriptions. To investigate it, this work presents the first systematic study on object hallucination of LVLMs. We conduct the evaluation experiments on several representative LVLMs, and show that they mostly suffer from severe object hallucination issue. We further discuss that the visual instructions may influence the hallucination, and find that: objects that frequently occur in the visual instructions or co-occur with the image objects, are obviously prone to be hallucinated by LVLMs. Besides, we find that existing evaluation methods might be affected by the input instructions and generation styles of LVLMs. Thus, we further design an improved evaluation method for object hallucination by proposing a polling-based query method called POPE. Experiment results demonstrate that our POPE can evaluate the object hallucination in a more stable and flexible way. Our codes and data are publicly available at https://github.com/RUCAIBox/POPE.

## Authors

[[Yifan Li]], [[Yifan Du]], [[Kun Zhou]], [[Jinpeng Wang]], [[Wayne Xin Zhao]], [[Ji-Rong Wen]]

## Data Description

POPE (Polling-based Object Probing Evaluation), a benchmark method for evaluating object hallucination in large vision-language models using Yes/No probing questions with random, popular, and adversarial sampling strategies.


## Notes


## Citation Info

926 citations (Semantic Scholar/arXiv) [2025-08-27]
