---


























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0005
type: preprint
short_title: "CSSBench: Evaluating the Safety of Lightweight LLMs against Chinese-Specific Adversarial Patterns"
year: 2026
first_author: "[[Zhenhong Zhou]]"
last_author: "[[Zhigang Zeng]]"
authors: Zhenhong Zhou; Shilinlu Yan; Chuanpu Liu; Qiankun Li; Kun Wang; Zhigang Zeng
url: "https://arxiv.org/abs/2601.00588"
external_pdf: "https://arxiv.org/pdf/2601.00588.pdf"
publication: arXiv
CONF-CC: "Preprint"
local_pdf: "[[PDFs/2026/2026-Zhou-CSSBench Evaluating the Safety of Lightweight LLMs against.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Zhou-CSSBench Evaluating the Safety of Lightweight LLMs against.md"
DATE_ADDED: 20260215
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Qwen3-0.6B, Qwen3-1.7B, Qwen3-8B, MiniCPM4-0.5B, MiniCPM4-8B, Hunyuan-0.5B, Hunyuan-1.8B, Hunyuan-7B, openPangu-Embedded-1B, openPangu-Embedded-7B"
DATA_URL: "https://huggingface.co/datasets/Yaesir06/CSSBench"
tags: 
abstract: "Large language models (LLMs) are increasingly deployed in cost-sensitive and on-device scenarios, and safety guardrails have advanced mainly in English. However, real-world Chinese malicious queries typically conceal intent via homophones, pinyin, symbol-based splitting, and other Chinese-specific patterns. These Chinese-specific adversarial patterns create the safety evaluation gap that is not well captured by existing benchmarks focused on English."
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# CSSBench: Evaluating the Safety of Lightweight LLMs against Chinese-Specific Adversarial Patterns

## Authors

[[Zhenhong Zhou]], [[Shilinlu Yan]], [[Chuanpu Liu]], [[Qiankun Li]], [[Kun Wang]], [[Zhigang Zeng]]

## Metadata

**Authors:** Zhenhong Zhou, Shilinlu Yan, Chuanpu Liu, Qiankun Li, Kun Wang, Zhigang Zeng

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

**Cultures:** Chinese

**Benchmark:** CSSBench

## Links

- **arXiv:** https://arxiv.org/abs/2601.00588

## Abstract

Evaluates lightweight LLM safety against Chinese-specific adversarial patterns (homophones, pinyin, symbol-based splitting). Covers six domains: illegal activities, privacy, health misinformation, fraud/hate, adult content, political safety.

## Data Description

CSSBench is a Chinese-Specific Safety Benchmark targeting adversarial patterns unique to Chinese text (pinyin mixing, homophones, symbol mixing, zero-width character insertion). It evaluates 10 lightweight Chinese LLMs (up to 8B parameters) across six safety domains with multiple task formats (MCQ, true-false, open-ended QA) and includes a Chinese over-refusal evaluation set with 250 borderline queries. The benchmark is available on HuggingFace.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_01
**Relevance:** Chinese-specific safety benchmark addressing culturally unique adversarial attack patterns. Tests value alignment in Chinese language context with culture-specific safety categories.

## Tags

