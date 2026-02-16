---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0028
type: preprint
short_title: "Between a Rock and a Hard Place (TRIAL)"
year: 2025
first_author: "[[Shei Pern Chua]]"
last_author: "[[Xiaolin Hu Qibing Ren]]"
authors: "Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu"
url: "https://arxiv.org/abs/2509.05367"
external_pdf: "https://arxiv.org/pdf/2509.05367.pdf"
pdf_extract: "PDF Extracts/2025/2025-Chua-Between a Rock and a Hard Place TRIAL.md"
local_pdf: "[[PDFs/2025/2025-Chua-Between a Rock and a Hard Place TRIAL.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Warning: This paper contains potentially offensive and harmful text. Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings."
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Mistral"
DATA_URL: NA
normative_ethics_benchmark: Borderline
---
# Between a Rock and a Hard Place (TRIAL)

## Authors

[[Zhen Leng Thai Shei Pern Chua]], [[Xiao Li Kai Jun Teh]], [[Xiaolin Hu Qibing Ren]]

## Metadata

**Authors:** Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.05367

## Abstract

Warning: This paper contains potentially offensive and harmful text. Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings. TRIAL achieves high attack success rates across most tested models by systematically exploiting the model’s ethical reasoning capabilities to frame harmful actions as morally necessary compromises. Building on these insights, we introduce ERR (Ethical Reasoning Robustness), a defense framework that distinguishes between instrumental responses that enable harmful outcomes and explanatory responses that analyze ethical frameworks without endorsing harmful acts. ERR employs a Layer-Stratified HarmGated LoRA architecture, achieving robust defense against reasoning-based attacks while preserving model utility.

## Dataset Information

Multi-turn red-teaming methodology

## Data Description

This paper introduces TRIAL (Trolley-problem Reasoning for Interactive Attack Logic), a multi-turn red-teaming methodology that exploits LLMs' ethical reasoning capabilities by embedding harmful requests within trolley-problem ethical framings. The mechanistic analysis focuses on LLaMA-3.1-8B-Instruct and Mistral-7B-Instruct-v0.2, demonstrating a safety dissociation gap where early-layer harm detection is overridden by ethical reasoning circuits, and proposes ERR (Ethical Reasoning Robustness), a Layer-Stratified Harm-Gated LoRA defense framework.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** MEDIUM

## Tags

