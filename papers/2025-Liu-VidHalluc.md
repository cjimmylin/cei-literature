---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 22LP6BQW
type: document
short_title: VidHalluc
year: 2025
first_author: "[[Chaoyu Li]]"
last_author: "[[Pooyan Fazli]]"
authors: "Chaoyu Li; Eun Woo Im; Pooyan Fazli"
url: "https://arxiv.org/abs/2412.03735"
external_pdf: "https://arxiv.org/pdf/2412.03735.pdf"
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
pdf_extract: "PDF Extracts/2025/2025-Liu-VidHalluc.md"
abstract: "Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, where models generate inaccurate or misleading content, remains underexplored in the video domain. Building on the observation that MLLM visual encoders often fail to distinguish visually different yet semantically similar video pairs, we introduce VIDHALLUC, the largest benchmark designed to examine..."
paper_summary: "Abstract: Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, wh | Overview: VIDHALLUC: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding Chaoyu Li Eun Woo Im Pooyan Fazli Arizona State University {chaoyuli, eunwooim, pooyan}@asu.ed | Methodology: can be applied directly during inference without additional 2 --- Page 3 --- Benchmark # of Ques. / # of Videos Binary QA MCQ Open-Ended Ques. Sorting | Key Findings: metric, calculated in the same manner as in Equation 1."
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
local_pdf: "[[Lit-WS-PDFs/2025/2025-Liu-VidHalluc.pdf]]"
CONF-CC: "CVPR 2024"
DATE_ADDED: 20260208
LLM_assessed: "Gemini, GPT-4o, LLaVA"
DATA_URL: "https://people-robots.github.io/vidhalluc"
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for hallucination detection"
data_metrics: "Not specified"
---
# VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding

## Metadata

**Authors:** Li, Chaoyu; Im, Eun Woo; Fazli, Pooyan

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-PDFs/2025/2025-Liu-VidHalluc.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2412.03735

## Abstract

Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, where models generate inaccurate or misleading content, remains underexplored in the video domain. Building on the observation that MLLM visual encoders often fail to distinguish visually different yet semantically similar video pairs, we introduce VidHalluc, the largest benchmark designed to examine hallucinations in MLLMs for video understanding. It consists of 5,002 videos, paired to highlight cases prone to hallucinations. VidHalluc assesses hallucinations across three critical dimensions: (1) action, (2) temporal sequence, and (3) scene transition. Comprehensive testing shows that most MLLMs are vulnerable to hallucinations across these dimensions. Furthermore, we propose DINO-HEAL, a training-free method that reduces hallucinations by incorporating spatial saliency from DINOv2 to reweight visual features during inference. Our results show that DINO-HEAL consistently improves performance on VidHalluc, achieving an average improvement of 3.02% in mitigating hallucinations across all tasks. Both the VidHalluc benchmark and DINO-HEAL code are available at https://people-robots.github.io/vidhalluc.

## Authors

[[Chaoyu Li]], [[Eun Woo Im]], [[Pooyan Fazli]]

## Data Description

VidHalluc is the largest video hallucination benchmark comprising 5,002 video pairs and 9,295 QA pairs, evaluating action, temporal sequence, and scene transition hallucinations in multimodal LLMs.


## Notes


## Citation Info

10 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2412.03735
