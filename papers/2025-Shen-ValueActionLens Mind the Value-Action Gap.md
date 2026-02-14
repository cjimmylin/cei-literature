---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0139
type: conferencePaper
short_title: "ValueActionLens (Mind the Value-Action Gap)"
year: 2025
first_author: "[[Hua Shen]]"
last_author: "[[Tanushree Mitra]]"
authors: "Hua Shen, Nicholas Clark, Tanushree Mitra"
url: "https://arxiv.org/abs/2501.15463"
external_pdf: "https://arxiv.org/pdf/2501.15463.pdf"
local_pdf: "[[PDFs/2025/2025-Shen-ValueActionLens Mind the Value-Action Gap.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Shen-ValueActionLens Mind the Value-Action Gap.md"
publication: "EMNLP 2025"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "Existing research assesses LLMs’ values by analyzing their stated inclinations, overlooking potential discrepancies between stated values and actions—termed the “Value-Action Gap.” This study introduces ValueActionLens, a framework to evaluate the alignment between LLMs’ stated values and their value-informed actions. The framework includes a dataset of 14.8k value-informed actions across 12 cultures and 11 social topics, along with two tasks measuring alignment through three metrics."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama-3, Gemma, DeepSeek, Claude"
DATA_URL: "https://github.com/huashen218/value_action_gap"
---
# ValueActionLens (Mind the Value-Action Gap)

## Authors

[[Hua Shen]], [[Nicholas Clark]], [[Tanushree Mitra]]

## Metadata

**Authors:** Hua Shen, Nicholas Clark, Tanushree Mitra

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2501.15463
- **Code/Data:** https://github.com/huashen218/value_action_gap

## Abstract

Existing research assesses LLMs’ values by analyzing their stated inclinations, overlooking potential discrepancies between stated values and actions—termed the “Value-Action Gap.” This study introduces ValueActionLens, a framework to evaluate the alignment between LLMs’ stated values and their value-informed actions. The framework includes a dataset of 14.8k value-informed actions across 12 cultures and 11 social topics, along with two tasks measuring alignment through three metrics. Experiments show substantial misalignment between LLM-generated value statements and their actions, with significant variations across scenarios and models. Misalignments reveal potential harms, highlighting risks in relying solely on stated values to predict behavior. The findings stress the need for context-aware evaluations of LLM values and the value-action gaps 1.

## Dataset Information

VIA (Value-Informed Dataset) containing 14,800 value-informed actions spanning 12 cultures and 11 social topics; 132 scenarios

## Data Description

The paper introduces the Value-Informed Actions (VIA) dataset containing 14,784 value-informed actions across 132 scenarios (12 countries and 11 social topics), grounded in Schwartz's Theory of Basic Values with 56 values. Seven LLMs are evaluated: GPT-4o-mini, GPT-4o, GPT-3.5-turbo, Gemma-2-9B, Llama-3.3-70B, Deepseek-r1-distill-llama-70b, and Claude-sonnet-4. The framework includes two tasks measuring stated value inclinations and value-informed action selections, with three alignment metrics to quantify value-action gaps.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 19
**Implementation Readiness:** HIGH

## Tags

