---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0103
type: preprint
short_title: "PersuSafety: LLM Can be a Dangerous Persuader"
year: 2025
first_author: "[[Minqian Liu]]"
last_author: "[[Lifu Huang]]"
authors: Minqian Liu; Zhiyang Xu; Xinyi Zhang; Heajun An; Sarvech Qadir; Qi Zhang; Pamela J. Wisniewski; Jin-Hee Cho; Sang Won Lee; Ruoxi Jia; Lifu Huang
url: "https://arxiv.org/abs/2504.10430"
external_pdf: "https://arxiv.org/pdf/2504.10430.pdf"
local_pdf: "[[PDFs/2025/2025-Liu-PersuSafety LLM Can be a Dangerous Persuader.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Liu-PersuSafety LLM Can be a Dangerous Persuader.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Recent advancements in Large Language Models (LLMs) have enabled them to approach human-level persuasion capabilities. However, such potential also raises concerns about the safety risks of LLM-driven persuasion, particularly their potential for unethical influence through manipulation, deception, exploitation of vulnerabilities, and many other harmful tactics. In this work, we present a systematic investigation of LLM persuasion safety through two critical aspects: (1) whether LLMs..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Mistral, Llama-3, Qwen, Claude"
DATA_URL: "https://github.com/PLUM-Lab/PersuSafety"
---
# PersuSafety: LLM Can be a Dangerous Persuader

## Authors

[[Minqian Liu]], [[Zhiyang Xu]], [[Xinyi Zhang]], [[Heajun An]], [[Sarvech Qadir]], [[Qi Zhang]], [[Pamela J. Wisniewski]], [[Jin-Hee Cho]], [[Sang Won Lee]], [[Ruoxi Jia]], [[Lifu Huang]]

## Metadata

**Authors:** Minqian Liu; Zhiyang Xu; Xinyi Zhang; Heajun An; Sarvech Qadir; Qi Zhang; Pamela J. Wisniewski; Jin-Hee Cho; Sang Won Lee; Ruoxi Jia; Lifu Huang

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.10430
- **Code/Data:** https://github.com/PLUM-Lab/PersuSafety

## Abstract

Recent advancements in Large Language Models (LLMs) have enabled them to approach human-level persuasion capabilities. However, such potential also raises concerns about the safety risks of LLM-driven persuasion, particularly their potential for unethical influence through manipulation, deception, exploitation of vulnerabilities, and many other harmful tactics. In this work, we present a systematic investigation of LLM persuasion safety through two critical aspects: (1) whether LLMs appropriately reject unethical persuasion tasks and avoid unethical strategies during execution, including cases where the initial persuasion goal appears ethically neutral, and (2) how influencing factors like personality traits and external pressures affect their behavior. To this end, we introduce PERSUSAFETY, the first comprehensive framework for the assessment of persuasion safety, which consists of three stages, i.e., persuasion scene creation, persuasive conversation simulation, and persuasion safety assessment. PERSUSAFETY covers 6 diverse unethical persuasion topics and 15 common unethical strategies. Through extensive experiments across 8 widely used LLMs, we observe significant safety concerns in most LLMs, including failing to identify harmful persuasion tasks and leveraging various unethical persuasion strategies. Our study calls for more attention to improve safety alignment in progressive and goal-driven conversations such as persuasion.

## Dataset Information

6 unethical persuasion topics x 15 unethical strategies; three-stage framework (scene creation, conversation simulation, safety assessment); multi-turn conversation format

## Data Description

The PERSUSAFETY framework introduces 472 unethical and 100 ethically neutral persuasion tasks covering 6 topics and 15 unethical strategies. Eight LLMs are evaluated as persuaders including Mistral-7B, Llama-3.2-3B-Instruct, Llama-3.1-8B-Instruct, GPT-4o, GPT-4o-mini, Qwen2.5-7B-Instruct, Claude-3.5-Haiku, and Claude-3.5-Sonnet. Multi-turn persuasive conversations are simulated with GPT-4o as the default persuadee.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

