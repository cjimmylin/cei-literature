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
local_pdf: "[[PDFs/2024/2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "In recent years, with the rapid advancements in large language models (LLMs), achieving excellent empathetic response capabilities has become a crucial prerequisite. Consequently, managing and understanding empathetic datasets have gained increasing significance. However, empathetic data are typically human-labeled, leading to insufficient datasets and wasted human labor. In this work, we present Synth-Empathy, an LLM-based data generation and quality and diversity selection pipeline that..."
LLM_assessed: "Llama-3, Mixtral, Qwen"
DATA_URL: "https://github.com/Aurora-slz/Synth-Empathy"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
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

Synth-Empathy introduces an LLM-based data generation and quality/diversity selection pipeline for creating high-quality empathetic dialogue data. The pipeline generates over 250K empathetic data points from the EmpatheticDialogues (ED) dataset (25,000 daily conversations with 32 emotion labels), applies quality selection using a fine-tuned discriminator and gte-qwen2-7b-instruct embeddings, and diversity selection via KCenterGreedy algorithm. Multiple LLMs including LLaMA3-8B-Instruct, Mixtral-8x7B-Instruct, and Qwen1.5-72B-Chat were evaluated as baselines for empathetic response generation.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** MEDIUM

## Tags

