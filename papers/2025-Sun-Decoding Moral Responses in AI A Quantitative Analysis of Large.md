---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0039
type: conferencePaper
short_title: "Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models"
year: 2025
first_author: "[[Chenkai Sun]]"
last_author: "[[Heng Ji]]"
authors: "Chenkai Sun; Jinning Li; Yi R. Fung; Hou Pong Chan; Tarek Abdelzaher; ChengXiang Zhai; Heng Ji"
doi: 10.1016/j.chbah.2025.100121
url: "https://doi.org/10.1016/j.chbah.2025.100121"
external_pdf: "https://arxiv.org/pdf/2310.13297.pdf"
pdf_extract: "PDF Extracts/2025/2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.md"
local_pdf: "[[PDFs/2025/2025-Sun-Decoding Moral Responses in AI A Quantitative Analysis of Large.pdf]]"
publication: Unknown
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Automatic response forecasting for news media plays a crucial role in enabling content producers to efficiently predict the impact of news releases and prevent unexpected negative outcomes such as social conflict and moral injury. To effectively forecast responses, it is essential to develop measures that leverage the social dynamics and contextual information surrounding individuals, especially in cases where explicit profiles or historical actions of the users are limited (referred to as..."
LLM_assessed: "ChatGPT, DeBERTa, RoBERTa"
DATA_URL: "https://github.com/chenkaisun/SocialSense"
normative_ethics_benchmark: Borderline
CONFERENCE: "Other Conference"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Decoding Moral Responses in AI: A Quantitative Analysis of Large Language Models

## Authors

[[Chenkai Sun]], [[Jinning Li]], [[Yi R. Fung]], [[Hou Pong Chan]], [[Tarek Abdelzaher]], [[ChengXiang Zhai]], [[Heng Ji]]

## Metadata

**Authors:** [Authors not fully extracted]

**Year:** 2025

**Type:** conferencePaper

**Venue:** Unknown

**DOI:** [10.1016/j.chbah.2025.100121](https://doi.org/10.1016/j.chbah.2025.100121)

## Links

- **DOI:** https://doi.org/10.1016/j.chbah.2025.100121

## Abstract

Automatic response forecasting for news media plays a crucial role in enabling content producers to efficiently predict the impact of news releases and prevent unexpected negative outcomes such as social conflict and moral injury. To effectively forecast responses, it is essential to develop measures that leverage the social dynamics and contextual information surrounding individuals, especially in cases where explicit profiles or historical actions of the users are limited (referred to as lurkers). As shown in a previous study, 97% of all tweets are produced by only the most active 25% of users. However, existing approaches have limited exploration of how to best process and utilize these important features. To address this gap, we propose a novel framework, named SOCIALSENSE, that leverages a large language model to induce a belief-centered graph on top of an existent social network, along with graph-based propagation to capture social dynamics. We hypothesize that the induced graph that bridges the gap between distant users who share similar beliefs allows the model to effectively capture the response patterns. Our method surpasses existing state-of-the-art in experimental evaluations for both zero-shot and supervised settings, demonstrating its effectiveness in response forecasting. Moreover, the analysis reveals the framework’s capability to effectively handle unseen user and lurker scenarios, further highlighting its robustness and practical applicability.

## Dataset Information

Series of moral dilemmas, both personal and impersonal

## Data Description

The paper uses a Twitter-based dataset (RFPN) consisting of 13,300 responses from 8,400 users to 3,800 news headlines, augmented with a curated social network of 18,634 users and 1,744,664 edges. The framework SOCIALSENSE leverages ChatGPT (gpt-3.5-turbo) for latent persona extraction and uses DeBERTa and RoBERTa as baselines for sentiment response forecasting tasks involving polarity and intensity prediction.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 6
**Implementation Readiness:** MEDIUM

## Tags

