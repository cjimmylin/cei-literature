---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0266
type: preprint
short_title: "VideoNorms: Benchmarking Cultural Awareness of Video Language Models"
year: 2025
first_author: "[[Varimalla, Nikhil Reddy]]"
last_author: "[[Muresan, Smaranda]]"
authors: "Varimalla, Nikhil Reddy; Xu, Yunfei; Saakyan, Arkadiy; Wang, Meng Fan; Muresan, Smaranda"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.08543"
external_pdf: "https://arxiv.org/pdf/2510.08543.pdf"
pdf_extract: "PDF Extracts/2025/2025-Varimaldi-VideoNorms Benchmarking Cultural Awareness of Video Language Models.md"
local_pdf: "[[PDFs/2025/2025-Varimaldi-VideoNorms Benchmarking Cultural Awareness of Video Language Models.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese, American"
cultures_nationalities_list: "American, Chinese"
languages_list: "Chinese, English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "As Video Large Language Models (VideoLLMs) are deployed globally, they require understanding of and grounding in the relevant cultural background. To properly assess these models’ cultural awareness, adequate benchmarks are needed. We introduce VIDEONORMS, a benchmark of over 1000 (video clip, norm) pairs from US and Chinese cultures annotated with socio-cultural norms grounded in speech act theory, norm adherence and violations labels, and verbal and non-verbal evidence."
LLM_assessed: "Gemini, Qwen"
DATA_URL: "https://github.com/nikhilreddy3/VideoNorms"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Computer Vision & Multimodal"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# VideoNorms: Benchmarking Cultural Awareness of Video Language Models

## Authors

[[Varimalla, Nikhil Reddy]], [[Xu, Yunfei]], [[Saakyan, Arkadiy]], [[Wang, Meng Fan]], [[Muresan, Smaranda]]

## Metadata

**Authors:** Varimalla, Nikhil Reddy; Xu, Yunfei; Saakyan, Arkadiy; Wang, Meng Fan; Muresan, Smaranda

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.08543

## Abstract

As Video Large Language Models (VideoLLMs) are deployed globally, they require understanding of and grounding in the relevant cultural background. To properly assess these models’ cultural awareness, adequate benchmarks are needed. We introduce VIDEONORMS, a benchmark of over 1000 (video clip, norm) pairs from US and Chinese cultures annotated with socio-cultural norms grounded in speech act theory, norm adherence and violations labels, and verbal and non-verbal evidence. To build VIDEONORMS, we use a human-AI collaboration framework, where a teacher model using theoretically-grounded prompting provides candidate annotations and a set of trained human experts validate and correct the annotations. We benchmark a variety of open-weight VideoLLMs on the new dataset which highlight several common trends: 1) models performs worse on norm violation than adherence; 2) models perform worse w.r.t Chinese culture compared to the US culture; 3) models have more difficulty in providing non-verbal evidence compared to verbal for the norm adhere/violation label and struggle to identify the exact norm corresponding to a speech-act; and 4) unlike humans, models perform worse in formal, non-humorous contexts. Our findings emphasize the need for culturallygrounded video language model training — a gap our benchmark and framework begin to address.

## Dataset Information

1,000+ video-norm pairs from US and Chinese cultures annotated with socio-cultural norms

## Data Description

VIDEONORMS is a benchmark of over 1,000 (video clip, norm) pairs from US and Chinese cultures for evaluating cultural awareness of Video Language Models. The dataset contains 15-second clips from 8 TV shows (4 US, 4 Chinese) annotated with socio-cultural norms grounded in speech act theory, norm adherence/violation labels, and verbal/non-verbal evidence. The teacher model Gemini-2.0-Pro was used for initial annotation, with subsequent validation by 3 trained human annotators per instance. Seven open-weight VideoLLMs were benchmarked including LLaVA-Next-Video, LLaVA-OneVision, InternVL-3, InternVL-3.5, Qwen2-VL, Qwen2.5-VL, and VideoChatR1.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

