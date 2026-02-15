---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0271
type: preprint
short_title: "AdAEM: Adaptively and Automated Extensible Measurement for Value Alignment"
year: 2025
first_author: "[[Duan, Shitong]]"
last_author: "[[Xie, Xing]]"
authors: "[[Duan, Shitong]]; [[Yi, Xiaoyuan]]; [[Zhang, Peng]]; [[Xu, Dongkuan]]; [[Yao, Jing]]; [[Lu, Tun]]; [[Gu, Ning]]; [[Xie, Xing]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2505.13531"
external_pdf: "https://arxiv.org/pdf/2505.13531.pdf"
pdf_extract: "PDF Extracts/2025/2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value.md"
local_pdf: "[[PDFs/2025/2025-Duan-AdAEM Adaptively and Automated Extensible Measurement for Value.pdf]]"
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
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Assessing Large Language Models (LLMs)’ underlying value differences enables comprehensive comparison of their misalignment, cultural adaptability, and biases. Nevertheless, current value measurement datasets face the informativeness challenge: with often outdated, contaminated, or generic test questions, they can only capture the shared value orientations among different LLMs, leading to saturated and thus uninformative results."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "12,310 questions"
LLM_assessed: "GPT-4, GPT-3.5, Claude, Llama-3, Mistral, Qwen, DeepSeek"
DATA_URL: NA
---
# AdAEM: Adaptively and Automated Extensible Measurement for Value Alignment

## Authors

[[Duan, Shitong]], [[Yi, Xiaoyuan]], [[Zhang, Peng]], [[Xu, Dongkuan]], [[Yao, Jing]], [[Lu, Tun]], [[Gu, Ning]], [[Xie, Xing]]

## Metadata

**Authors:** Duan, Shitong; Yi, Xiaoyuan; Zhang, Peng; Xu, Dongkuan; Yao, Jing; Lu, Tun; Gu, Ning; Xie, Xing

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2505.13531

## Abstract

Assessing Large Language Models (LLMs)’ underlying value differences enables comprehensive comparison of their misalignment, cultural adaptability, and biases. Nevertheless, current value measurement datasets face the informativeness challenge: with often outdated, contaminated, or generic test questions, they can only capture the shared value orientations among different LLMs, leading to saturated and thus uninformative results. To address this problem, we introduce AdAEM, a novel, self-extensible assessment framework for revealing LLMs’ inclinations. Distinct from previous static benchmarks, AdAEM can automatically and adaptively generate and extend its test questions. This is achieved by probing the internal value boundaries of a diverse set of LLMs developed across cultures and time periods in an in-context optimization manner. The optimization process theoretically maximizes an information-theoretic objective to extract the latest or culturally controversial topics, providing more distinguishable and informative insights about models’ value differences. In this way, AdAEM is able to co-evolve with the development of LLMs, consistently tracking their value dynamics. Using AdAEM, we generate 12,310 questions grounded in Schwartz Value Theory, conduct an extensive analysis to manifest our method’s validity and effectiveness, and benchmark the values of 16 LLMs, laying the groundwork for better value research.

## Dataset Information

12,310 self-generated questions grounded in Schwartz Value Theory, auto-adapting to reveal value differences

## Data Description

The paper introduces AdAEM, a self-extensible value evaluation framework that generates 12,310 test questions grounded in Schwartz Value Theory to measure LLM value differences. It benchmarks 16 LLMs including GPT-4-Turbo, GPT-3.5-Turbo, o3-mini, Claude-3.5-Sonnet, Gemini-1.5, Gemini-2.0, Llama-3.1 (8B/70B/405B), Mistral-7B, Mistral-Large, Qwen2.5-7B, Qwen-Max, DeepSeek-V2.5, DeepSeek-V3, DeepSeek-R1, and GLM-4, using Jensen-Shannon divergence optimization to expose underlying value orientations.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

