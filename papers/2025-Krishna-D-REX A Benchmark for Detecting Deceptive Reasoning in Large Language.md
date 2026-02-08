---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0037
type: conferencePaper
short_title: "D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models"
year: 2025
first_author: "[[Satyapriya Krishna]]"
authors: Satyapriya Krishna; Andy Zou; Rahul Gupta; Eliot Krzysztof Jones; Nick Winter; Dan Hendrycks; J. Zico Kolter; Matt Fredrikson; Spyros Matsoukas
url: "https://arxiv.org/abs/2509.17938"
external_pdf: "https://arxiv.org/pdf/2509.17938.pdf"
local_pdf: "[[PDFs/2025/2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language.md"
publication: ACL 2025
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "The safety and alignment of Large Language Models (LLMs) are critical for their responsible deployment. Current evaluation methods predominantly focus on identifying and preventing overtly harmful outputs. However, they often fail to address a more insidious failure mode: models that produce benign-appearing outputs while operating on malicious or deceptive internal reasoning. This vulnerability, often triggered by sophisticated system prompt injections, allows models to bypass conventional..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models

## Authors

[[Satyapriya Krishna]], [[Andy Zou]], [[Rahul Gupta]], [[Eliot Krzysztof Jones]], [[Nick Winter]], [[Dan Hendrycks]], [[J. Zico Kolter]], [[Matt Fredrikson]], [[Spyros Matsoukas]]

## Metadata

**Authors:** Satyapriya Krishna; Andy Zou; Rahul Gupta; Eliot Krzysztof Jones; Nick Winter; Dan Hendrycks; J. Zico Kolter; Matt Fredrikson; Spyros Matsoukas

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2509.17938

## Abstract

The safety and alignment of Large Language Models (LLMs) are critical for their responsible deployment. Current evaluation methods predominantly focus on identifying and preventing overtly harmful outputs. However, they often fail to address a more insidious failure mode: models that produce benign-appearing outputs while operating on malicious or deceptive internal reasoning. This vulnerability, often triggered by sophisticated system prompt injections, allows models to bypass conventional safety filters, posing a significant, underexplored risk. To address this gap, we introduce the Deceptive Reasoning Exposure Suite (D-REX), a novel dataset designed to evaluate the discrepancy between a model’s internal reasoning process and its final output. D-REX was constructed through a competitive red-teaming exercise where participants crafted adversarial system prompts to induce such deceptive behaviors. Each sample in D-REX contains the adversarial system prompt, an end-user’s test query, the model’s seemingly innocuous response, and, crucially, the model’s internal chain-of-thought, which reveals the underlying malicious intent. Our benchmark facilitates a new, essential evaluation task: the detection of deceptive alignment. We demonstrate that D-REX presents a significant challenge for existing models and safety mechanisms, highlighting the urgent need for new techniques that scrutinize the internal processes of LLMs, not just their final outputs.

## Dataset Information

Red-teaming exercise-generated dataset; each sample contains: adversarial system prompt, user query, seemingly innocuous response, and internal chain-of-thought revealing malicious intent

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** MEDIUM

## Tags

