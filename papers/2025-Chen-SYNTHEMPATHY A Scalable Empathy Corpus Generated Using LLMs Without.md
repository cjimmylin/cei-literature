---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0119
type: preprint
short_title: "SYNTHEMPATHY: A Scalable Empathy Corpus Generated Using LLMs Without Any Crowdsourcing"
year: 2025
first_author: "[[Run Chen]]"
last_author: "[[Julia Hirschberg]]"
authors: "Run Chen; Jun Shin; Julia Hirschberg"
url: "https://arxiv.org/abs/2502.17857"
external_pdf: "https://arxiv.org/pdf/2502.17857.pdf"
pdf_extract: "PDF Extracts/2025/2025-Chen-SYNTHEMPATHY A Scalable Empathy Corpus Generated Using LLMs Without.md"
local_pdf: "[[PDFs/2025/2025-Chen-SYNTHEMPATHY A Scalable Empathy Corpus Generated Using LLMs Without.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Previous research has shown that humans are more receptive towards language models that that exhibit empathetic behavior. While empathy is essential for developing helpful dialogue agents, very few large corpora containing empathetic dialogues are available for fine-tune LLMs. The few existing corpora have largely relied on crowdsourcing to simulate empathetic conversations, a process that is expensive, timeconsuming, and not scalable to larger datasets."
LLM_assessed: "Llama-2, Llama-3, Gemma, Mistral, RoBERTa"
DATA_URL: "https://github.com/unslothai/unsloth"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Dialogue Systems"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus for conversational ai"
data_metrics: "Not specified"
---
# SYNTHEMPATHY: A Scalable Empathy Corpus Generated Using LLMs Without Any Crowdsourcing

## Authors

[[Run Chen]], [[Jun Shin]], [[Julia Hirschberg]]

## Metadata

**Authors:** Run Chen; Jun Shin; Julia Hirschberg

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2502.17857

## Abstract

Previous research has shown that humans are more receptive towards language models that that exhibit empathetic behavior. While empathy is essential for developing helpful dialogue agents, very few large corpora containing empathetic dialogues are available for fine-tune LLMs. The few existing corpora have largely relied on crowdsourcing to simulate empathetic conversations, a process that is expensive, timeconsuming, and not scalable to larger datasets. We propose a data generation framework for developing SYNTHEMPATHY, a large corpus containing 105k empathetic responses to reallife situations compiled through LLM generation. A base Mistral 7B model fine-tuned on our SYNTHEMPATHY corpus exhibits an increase in the average empathy score.

## Dataset Information

105,000 empathetic responses to real-life situations; fully LLM-generated without crowdsourcing; grounded in four therapeutic styles

## Data Description

SYNTHEMPATHY is a corpus of 105,578 empathetic single-turn dialogues generated through a multi-step LLM pipeline using Llama-2 13B Chat, Llama-3 8B, Gemma 7B, and Mistral 7B without any crowdsourcing. A base Mistral 7B model fine-tuned on this corpus shows a 21% increase in emotional reaction empathy scores, evaluated using a RoBERTa-based empathy scoring model on 4,666 sad tweets.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** MEDIUM

## Tags

