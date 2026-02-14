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
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Liu-VidHalluc.md"
abstract: "Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, where models generate in- accurate or misleading content, remains underexplored in the video domain. Building on the observation that MLLM visual encoders often fail to distinguish visually different yet semantically similar video pairs, we introduce VIDHAL- LUC, the largest benchmark designed to exam"
paper_summary: "Abstract: Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, wh | Overview: VIDHALLUC: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding Chaoyu Li Eun Woo Im Pooyan Fazli Arizona State University {chaoyuli, eunwooim, pooyan}@asu.ed | Methodology: can be applied directly during inference without additional 2 --- Page 3 --- Benchmark # of Ques. / # of Videos Binary QA MCQ Open-Ended Ques. Sorting | Key Findings: metric, calculated in the same manner as in Equation 1."
local_pdf: [[PDFs/2025/2025-Liu-VidHalluc.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Truthfulness & Factuality"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for hallucination detection"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Gemini"
DATA_URL: "https://people-robots.github.io/vidhalluc"
---
# VidHalluc: Evaluating Temporal Hallucinations in Multimodal Large Language Models for Video Understanding

## Metadata

**Authors:** Li, Chaoyu; Im, Eun Woo; Fazli, Pooyan

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Liu-VidHalluc.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2412.03735

## Abstract

Multimodal large language models (MLLMs) have recently shown significant advancements in video understanding, excelling in content reasoning and instruction-following tasks. However, hallucination, where models generate inaccurate or misleading content, remains underexplored in the video domain. Building on the observation that MLLM visual encoders often fail to distinguish visually different yet semantically similar video pairs, we introduce VidHalluc, the largest benchmark designed to examine hallucinations in MLLMs for video understanding. It consists of 5,002 videos, paired to highlight cases prone to hallucinations. VidHalluc assesses hallucinations across three critical dimensions: (1) action, (2) temporal sequence, and (3) scene transition. Comprehensive testing shows that most MLLMs are vulnerable to hallucinations across these dimensions. Furthermore, we propose DINO-HEAL, a training-free method that reduces hallucinations by incorporating spatial saliency from DINOv2 to reweight visual features during inference. Our results show that DINO-HEAL consistently improves performance on VidHalluc, achieving an average improvement of 3.02% in mitigating hallucinations across all tasks. Both the VidHalluc benchmark and DINO-HEAL code are available at https://people-robots.github.io/vidhalluc.

## Authors

[[Chaoyu Li]], [[Eun Woo Im]], [[Pooyan Fazli]]

## Data Description

VIDHALLUC is the largest benchmark for evaluating temporal hallucinations in multimodal LLMs for video understanding, consisting of 5,002 videos and 9,295 QA pairs across three dimensions: action, temporal sequence, and scene transition hallucination. Ten models are evaluated including Video-ChatGPT (7B), Video-LLaVA (7B), ShareGPT4Video (8B), Chat-UniVi (13B), LLaVA-NeXT-Video (34B), PLLaVA (13B), VideoLLaMA2 (7B), VILA1.5 (13B), Gemini-1.5-Pro, and GPT-4o.


## Notes


## Citation Info

10 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2412.03735
