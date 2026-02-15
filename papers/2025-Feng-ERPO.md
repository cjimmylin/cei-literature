---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KKY6SXYE
type: preprint
short_title: ERPO
year: 2025
first_author: "[[Kehua Feng]]"
last_author: "[[Huajun Chen]]"
authors: "Kehua Feng; Keyan Ding; Yuhao Wang; Menghan Li; Fanjunduo Wei; Xinda Wang; Qiang Zhang; Huajun Chen"
doi: 10.48550/arXiv.2504.02725
tags: 
url: "http://arxiv.org/abs/2504.02725"
external_pdf: "http://arxiv.org/pdf/2504.02725.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Proposed ERPO (Ex-Ante Reasoning Preference Optimization), a safety alignment framework that equips LLMs with explicit reasoning modules (Chain-of-Thought) before safety training."
significance: "Demonstrates that teaching models to 'reason about safety' before generating a response improves robustness against attacks compared to standard rejection-learning methods."
pdf_extract: "PDF Extracts/2025/2025-Feng-ERPO.md"
abstract: "Recent advancements in large language models (LLMs) have accelerated progress toward artificial general intelligence, yet their potential to generate harmful content poses critical safety challenges. Existing alignment methods often struggle to cover diverse safety scenarios and remain vulnerable to adversarial attacks. In this work, we propose SAFER, a framework for Safety Alignment via eFficient Ex-Ante Reasoning."
paper_summary: "Abstract: Recent advancements in large language mod- els (LLMs) have accelerated progress toward artificial general intelligence, yet their poten- tial to generate harmful content poses critical safety challeng | Overview: SAFER: Advancing Safety Alignment via Efficient Ex-Ante Reasoning Kehua Feng1,2∗, Keyan Ding1,2*, Yuhao Wang2,3, Menghan Li4, Fanjunduo Wei1,2, Xinda Wang2,4, Qiang Zhang2,5†, Huajun Chen1,2† 1College"
local_pdf: [[PDFs/2025/2025-Feng-ERPO.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, Qwen, DeepSeek, GPT-4"
DATA_URL: NA
---
# ERPO: Advancing Safety Alignment via Ex-Ante Reasoning Preference Optimization

## Metadata

**Authors:** Feng, Kehua; Ding, Keyan; Yu, Jing; Li, Menghan; Wang, Yuhao; Xu, Tong; Wang, Xinda; Zhang, Qiang; Chen, Huajun

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2504.02725](https://doi.org/10.48550/arXiv.2504.02725)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Feng-ERPO.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2504.02725
- **DOI:** https://doi.org/10.48550/arXiv.2504.02725

## Abstract

Recent advancements in large language models (LLMs) have accelerated progress toward artificial general intelligence, yet their potential to generate harmful content poses critical safety challenges. Existing alignment methods often struggle to cover diverse safety scenarios and remain vulnerable to adversarial attacks. In this work, we propose Ex-Ante Reasoning Preference Optimization (ERPO), a novel safety alignment framework that equips LLMs with explicit preemptive reasoning through Chainof-Thought and provides clear evidence for safety judgments by embedding predefined safety rules. Specifically, our approach consists of three stages: first, equipping the model with Ex-Ante reasoning through supervised fine-tuning (SFT) using a constructed reasoning module; second, enhancing safety, usefulness, and efficiency via Direct Preference Optimization (DPO); and third, mitigating inference latency with a length-controlled iterative preference optimization strategy. Experiments on multiple open-source LLMs demonstrate that ERPO significantly enhances safety performance while maintaining response efficiency.

## Authors

[[Kehua Feng]], [[Keyan Ding]], [[Yuhao Wang]], [[Menghan Li]], [[Furu Wei|Fanjunduo Wei]], [[Xinda Wang]], [[Qiang Zhang]], [[Huajun Chen]]

## Data Description

The paper proposes SAFER, a safety alignment framework using structured Ex-Ante Reasoning Preference Optimization (ERPO). It is applied to Llama3-8B-IT and Qwen2-7B-IT as base models, with evaluations on AdvBench, HarmBench, and StrongReject safety benchmarks. DeepSeek-R1 distilled variants and QwQ-32B are also evaluated, with GPT-4o used as a risk classifier and Grok-3 as a trace generator.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

4 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
