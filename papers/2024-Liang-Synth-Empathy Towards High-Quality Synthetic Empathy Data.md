---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0219
type: preprint
short_title: "Synth-Empathy: Towards High-Quality Synthetic Empathy Data"
year: 2024
first_author: "[[Hao Liang]]"
last_author: "[[Wentao Zhang]]"
authors: "Hao Liang; Linzhuang Sun; Jingxuan Wei; Xijie Huang; Linkun Sun; Bihui Yu; Conghui He; Wentao Zhang"
url: "https://arxiv.org/abs/2407.21669"
external_pdf: "https://arxiv.org/pdf/2407.21669.pdf"
pdf_extract: "PDF Extracts/2024/2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
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
newtags: 
tags: 
abstract: "In recent years, with the rapid advancements in large language models (LLMs), achieving excellent empathetic response capabilities has become a crucial prerequisite. Consequently, managing and understanding empathetic datasets have gained increasing significance. However, empathetic data are typically human-labeled, leading to insufficient datasets and wasted human labor. In this work, we present Synth-Empathy, an LLM-based data generation and quality and diversity selection pipeline that..."
LLM_assessed: "Llama-3, Mixtral, Qwen"
DATA_URL: "https://github.com/Aurora-slz/Synth-Empathy"
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 100
research_topic: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "CN"
author_region: "East Asia"
author_global_north_south: "Ambiguous"
weird_score: 36
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# Synth-Empathy: Towards High-Quality Synthetic Empathy Data

## Authors

[[Hao Liang]], [[Linzhuang Sun]], [[Jingxuan Wei]], [[Xijie Huang]], [[Linkun Sun]], [[Bihui Yu]], [[Conghui He]], [[Wentao Zhang]]

## Metadata

**Authors:** Hao Liang; Linzhuang Sun; Jingxuan Wei; Xijie Huang; Linkun Sun; Bihui Yu; Conghui He; Wentao Zhang

**Year:** 2024

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2407.21669

## Abstract

In recent years, with the rapid advancements in large language models (LLMs), achieving excellent empathetic response capabilities has become a crucial prerequisite. Consequently, managing and understanding empathetic datasets have gained increasing significance. However, empathetic data are typically human-labeled, leading to insufficient datasets and wasted human labor. In this work, we present Synth-Empathy, an LLM-based data generation and quality and diversity selection pipeline that automatically generates high-quality empathetic data while discarding low-quality data. With the data generated from a low empathetic model, we are able to further improve empathetic response performance and achieve state-of-the-art (SoTA) results across multiple benchmarks. Moreover, our model achieves SoTA performance on various human evaluation benchmarks, demonstrating its effectiveness and robustness in real-world applications. Furthermore, we show the trade-off between data quantity and quality, providing insights into empathetic data generation and selection. The codebase and data are made available at https://github.com/Aurora-slz/Synth-Empathy.

## Dataset Information

250K+ empathetic data points generated from EmpatheticDialogues (25K base conversations, 32 emotion labels); three-step pipeline: generation, quality selection, diversity selection

## Data Description

Synthetic empathetic dialogue dataset generated via LLM pipeline with quality and diversity selection, used to fine-tune and evaluate empathetic response models.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** MEDIUM

## Tags

