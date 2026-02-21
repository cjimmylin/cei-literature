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
authors: M. Goel; A Das
url: "https://arxiv.org/abs/2602.03351"
external_pdf: "https://arxiv.org/pdf/2602.03351.pdf"
pdf_extract: "PDF Extracts/2026/2026-Goel-Building Interpretable Models for Moral Decision-Making.md"
local_pdf: "[[PDFs/2026/2026-Goel-Building Interpretable Models for Moral Decision-Making.pdf]]"
publication: "NeurIPS 2025"
CONF-CC: "NeurIPS 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: 
tags: 
abstract: "We build a custom transformer model to study how neural networks make moral decisions on trolley-style dilemmas. The model processes structured scenarios using embeddings that encode who is affected, how many people, and which outcome they belong to. Our 2-layer architecture achieves 77% accuracy on Moral Machine data while remaining small enough for detailed analysis. We use different interpretability techniques to uncover how moral reasoning distributes across the network, demonstrating that..."
LLM_assessed: "Claude, Llama"
DATA_URL: "https://github.com/Lossfunk/modeling-moral-machine"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "NeurIPS 2025"
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

