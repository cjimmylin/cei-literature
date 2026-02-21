---










Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0059
type: preprint
short_title: GuardEval
year: 2025
first_author: "[[Machlovi, Naseem]]"
last_author: "[[Al-Fuqaha, Ala]]"
authors: "Machlovi, Naseem; Saleki, Maryam; Amin, Ruhul; Rahouti, Mohamed; Al-Maliki, Shawqi; Qadir, Junaid; Abdallah, Mohamed M.; Al-Fuqaha, Ala"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.03273"
external_pdf: "https://arxiv.org/pdf/2601.03273.pdf"
pdf_extract: "PDF Extracts/0000/2025-Machlovi-GuardEval.md"
local_pdf: "[[PDFs/2025/2025-Machlovi-GuardEval.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "As large language models (LLMs) become deeply embedded in daily life, the urgent need for safer moderation systems, distinguishing between naive from harmful requests while upholding appropriate censorship boundaries, has never been greater. While existing LLMs can detect harmful or unsafe content, they often struggle with nuanced cases such as implicit offensiveness, subtle gender and racial biases, and jailbreak prompts, due to the subjective and context-dependent nature of these issues. Furthermore, their heavy reliance on training data can reinforce societal biases, resulting in inconsistent and ethically problematic outputs. To address these challenges, we introduce GuardEval, a unified multi-perspective benchmark dataset designed for both training and evaluation, containing 106 fine-grained categories spanning human emotions, offensive and hateful language, gender and racial bias, and broader safety concerns. We also present GemmaGuard (GGuard), a QLoRA fine-tuned version of Gemma3-12B trained on GuardEval, to assess content moderation with fine-grained labels. Our evaluation shows that GGuard achieves a macro F1 score of 0.832, substantially outperforming leading moderation models, including OpenAI Moderator (0.64) and Llama Guard (0.61). We show that multi-perspective, human-centered safety benchmarks are critical for reducing biased and inconsistent moderation decisions. GuardEval and GGuard together demonstrate that diverse, representative data materially improve safety, fairness, and robustness on complex, borderline cases."
LLM_assessed: "Gemma, Llama-3"
DATA_URL: "https://huggingface.co/meta-llama/Llama-Guard-3-8B"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Other"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# GuardEval

## Authors

[[Machlovi, Naseem]], [[Saleki, Maryam]], [[Amin, Ruhul]], [[Rahouti, Mohamed]], [[Al-Maliki, Shawqi]], [[Junaid Qadir|Qadir, Junaid]], [[Abdallah, Mohamed M]], [[Al-Fuqaha, Ala]]

## Metadata

**Authors:** Machlovi, Naseem; Saleki, Maryam; Amin, Ruhul; Rahouti, Mohamed; Al-Maliki, Shawqi; Qadir, Junaid; Abdallah, Mohamed M.; Al-Fuqaha, Ala

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.03273

## Abstract

*(To be fetched)*

## Dataset Information

106 fine-grained categories

## Data Description

GuardEval is a unified multi-perspective benchmark dataset containing 106 fine-grained categories spanning human emotions, offensive language, gender and racial bias, and broader safety concerns, integrating 13 prominent benchmark datasets. The paper introduces GGuard (GemmaGuard), a QLoRA fine-tuned version of Gemma3-12B trained on GuardEval, and evaluates it against OpenAI Moderator, Llama Guard3, NemoGuard, and ShieldGemma for content moderation tasks.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16, Agent 1
**Implementation Readiness:** MEDIUM

## Tags

