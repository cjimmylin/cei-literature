---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0082
type: conferencePaper
short_title: MSLR-Bench (Multi-Step Legal Reasoning)
year: 2025
first_author: "[[Wenhan Yu]]"
authors: Wenhan Yu, Xinbo Lin, Lanxin Ni, Jinhua Cheng, and Lei Sha
url: "https://arxiv.org/abs/2511.07979"
external_pdf: "https://arxiv.org/pdf/2511.07979.pdf"
local_pdf: "[[PDFs/2025/2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.md"
publication: AAAI 2026
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Chinese"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "As large language models (LLMs) exhibit advanced reasoning capabilities in different specialized domains, their application to legal reasoning tasks is actively being explored. The pursuit of justice in legal contexts demands not only correct outcomes but also reasoned elaboration, which necessitates deriving conclusions through logically justified and transparent argumentation. Current legal benchmarks, despite being cited as reasoning-focused, suffer from three critical limitations:..."
ethics_perspective: "Hallucination & Truthfulness"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# MSLR-Bench (Multi-Step Legal Reasoning)

## Authors

[[Wenhan Yu, Xinbo Lin, Lanxin Ni, Jinhua Cheng, and Lei Sha]]

## Metadata

**Authors:** Wenhan Yu, Xinbo Lin, Lanxin Ni, Jinhua Cheng, and Lei Sha

**Year:** 2025

**Type:** conferencePaper

**Venue:** AAAI 2026

## Links

- **arXiv:** https://arxiv.org/abs/2511.07979
- **Code/Data:** https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench

## Abstract

As large language models (LLMs) exhibit advanced reasoning capabilities in different specialized domains, their application to legal reasoning tasks is actively being explored. The pursuit of justice in legal contexts demands not only correct outcomes but also reasoned elaboration, which necessitates deriving conclusions through logically justified and transparent argumentation. Current legal benchmarks, despite being cited as reasoning-focused, suffer from three critical limitations: conflation of factual recall with genuine inference, fragmentation of holistic reasoning processes, and neglect of reasoning process quality. To bridge these gaps, we construct MSLR, the first Chinese multi-step legal reasoning dataset centered on legal decision-making. To align with real-world legal reasoning trajectories, MSLR employs the IRAC framework (Issue-Rule-Application-Conclusion) to capture expert reasoning traces from official legal decisions. In parallel, we design a scalable Human-LLM collaborative annotation pipeline that efficiently generates fine-grained step-level annotations while establishing a reusable methodological framework for multi-step reasoning datasets. Evaluation of a range of LLMs on MSLR reveals only modest performance, highlighting substantial challenges in adapting to complex legal reasoning. Further experiments show that Self-Initiated CoT prompts—created autonomously by the models—consistently improve reasoning coherence and output quality, outperforming Human-Designed CoT prompts, which often yield ambiguous results. This work contributes to the broader discourse on LLM reasoning and CoT strategies, offering practical insights and resources for future research. The dataset and code are publicly available at https://github.com/yuwenhan07/MSLR-Bench and https://law.sjtu.edu.cn/flszyjzx/index.html.

## Dataset Information

~1,400 cases with 60,000 step-level annotations

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

