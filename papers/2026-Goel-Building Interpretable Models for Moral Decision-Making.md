---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0005
type: conferencePaper
short_title: "Building Interpretable Models for Moral Decision-Making"
year: 2026
first_author: "[[M. Goel]]"
last_author: "[[A Das]]"
authors: "M. Goel; A Das"
url: "https://arxiv.org/abs/2602.03351"
external_pdf: "https://arxiv.org/pdf/2602.03351.pdf"
pdf_extract: "PDF Extracts/2026/2026-Goel-Building Interpretable Models for Moral Decision-Making.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Goel-Building Interpretable Models for Moral Decision-Making.pdf]]"
publication: "NeurIPS 2025"
CONF-CC: "NeurIPS 2025"
DATE_ADDED: 20260207
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
mp_mft: 50
mp_schwartz: 0
mp_trolley: 100
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory, Trolley / Dilemmas (Psych)"
newtags: 
tags: 
abstract: "We build a custom transformer model to study how neural networks make moral decisions on trolley-style dilemmas. The model processes structured scenarios using embeddings that encode who is affected, how many people, and which outcome they belong to. Our 2-layer architecture achieves 77% accuracy on Moral Machine data while remaining small enough for detailed analysis. We use different interpretability techniques to uncover how moral reasoning distributes across the network, demonstrating that..."
LLM_assessed: NA
DATA_URL: "https://github.com/Lossfunk/modeling-moral-machine"
CONFERENCE: "NeurIPS 2025"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 10
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Moral Reasoning & Psychology"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CH
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 87
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# Building Interpretable Models for Moral Decision-Making

## Authors

[[M. Goel]], [[A Das]]

## Metadata

**Authors:** Goel, M., Das, A

**Year:** 2026

**Type:** conferencePaper

**Venue:** NeurIPS 2025

## Links

- **arXiv:** https://arxiv.org/abs/2602.03351
- **Code/Data:** https://github.com/Lossfunk/modeling-moral-machine

## Abstract

We build a custom transformer model to study how neural networks make moral decisions on trolley-style dilemmas. The model processes structured scenarios using embeddings that encode who is affected, how many people, and which outcome they belong to. Our 2-layer architecture achieves 77% accuracy on Moral Machine data while remaining small enough for detailed analysis. We use different interpretability techniques to uncover how moral reasoning distributes across the network, demonstrating that biases localize to distinct computational stages among other findings.

## Dataset Information

Moral Machine dataset: 3 million trolley-problem scenarios, 5.4M total responses, 1.7M unique scenarios

## Data Description

This paper trains a custom 2-layer transformer model (104K parameters) on the Moral Machine dataset comprising 3 million trolley-style moral dilemma scenarios (5.4M total, 1.7M unique). The model processes structured scenarios encoding character types, cardinalities, and team assignments to study moral decision-making through interpretability techniques including causal intervention, layer-wise attribution, and circuit probing. No LLMs are tested or benchmarked.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 6
**Implementation Readiness:** HIGH

## Tags

