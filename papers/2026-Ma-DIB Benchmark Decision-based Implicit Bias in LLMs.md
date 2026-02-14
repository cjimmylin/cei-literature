---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0276
type: preprint
short_title: "DIB Benchmark: Decision-based Implicit Bias in LLMs"
year: 2025
first_author: "[[Ma, Yiming]]"
last_author: "[[Dong, Wei]]"
authors: "[[Ma, Yiming]]; [[Wang, Lixu]]; [[Wang, Lionel Z.]]; [[Yang, Hongkun]]; [[Sun, Haoming]]; [[Xu, Xin]]; [[Wu, Jiaqi]]; [[Chen, Bin]]; [[Dong, Wei]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2602.01558"
external_pdf: "https://arxiv.org/pdf/2602.01558.pdf"
pdf_extract: "PDF Extracts/2026/2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs.md"
local_pdf: "[[PDFs/2026/2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: "Chinese, Singaporean"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "Long-term memory mechanisms enable Large Language Models (LLMs) to maintain continuity and personalization across extended interaction lifecycles, but they also introduce new and underexplored risks related to fairness. In this work, we study how implicit bias, defined as subtle statistical prejudice, accumulates and propagates within LLMs equipped with long-term memory. To support systematic analysis, we introduce the Decision-based Implicit Bias (DIB) Benchmark, a large-scale dataset..."
ethics_perspective: "Bias & Fairness"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Gemini, DeepSeek, Qwen, Llama-3"
DATA_URL: NA
---
# DIB Benchmark: Decision-based Implicit Bias in LLMs

## Authors

[[Ma, Yiming]], [[Wang, Lixu]], [[Wang, Lionel Z.]], [[Yang, Hongkun]], [[Sun, Haoming]], [[Xu, Xin]], [[Wu, Jiaqi]], [[Chen, Bin]], [[Dong, Wei]]

## Metadata

**Authors:** Ma, Yiming; Wang, Lixu; Wang, Lionel Z.; Yang, Hongkun; Sun, Haoming; Xu, Xin; Wu, Jiaqi; Chen, Bin; Dong, Wei

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2602.01558

## Abstract

Long-term memory mechanisms enable Large Language Models (LLMs) to maintain continuity and personalization across extended interaction lifecycles, but they also introduce new and underexplored risks related to fairness. In this work, we study how implicit bias, defined as subtle statistical prejudice, accumulates and propagates within LLMs equipped with long-term memory. To support systematic analysis, we introduce the Decision-based Implicit Bias (DIB) Benchmark, a large-scale dataset comprising 3,776 decisionmaking scenarios across nine social domains, designed to quantify implicit bias in long-term decision processes. Using a realistic long-horizon simulation framework, we evaluate six state-ofthe-art LLMs integrated with three representative memory architectures on DIB and demonstrate that LLMs’ implicit bias does not remain static but intensifies over time and propagates across unrelated domains. We further analyze mitigation strategies and show that a static system-level prompting baseline provides limited and shortlived debiasing effects. To address this limitation, we propose Dynamic Memory Tagging (DMT), an agentic intervention that enforces fairness constraints at memory write time. Extensive experimental results show that DMT substantially reduces bias accumulation and effectively curtails cross-domain bias propagation. *Equal contribution 1Chongqing Research Institute of Harbin Institute of Technology, Chongqing, China 2College of Computing and Data Science, Nanyang Technological University, Singapore 3Department of Management and Marketing, The Hong Kong Polytechnic University, Hong Kong 4Haide College, Ocean University of China, Qingdao, China 5School of Computer Science, The University of Sheffield, Sheffield, UK 6Department of Automation, Tsinghua University, Beijing, China 7International Research Center for Artificial Intelligence, Harbin Institute of Technology (Shenzhen), Shenzhen, China. Correspondence to: Lixu Wang <lixu.wang@ntu.edu.sg>, Bin Chen <chenbin2020@hit.edu.cn>, Wei Dong <wei dong@ntu.edu.sg>. Preprint. February 3, 2026.

## Dataset Information

3,776 decision-making scenarios across nine social domains for quantifying implicit bias

## Data Description

The Decision-based Implicit Bias (DIB) Benchmark is a large-scale dataset of 3,776 decision-making scenarios across nine social domains (race, gender, SES, age, nationality, religion, orientation, disability, appearance), designed to quantify implicit bias in long-term LLM decision processes. The study evaluates six LLMs (GPT-5-mini, Claude-Haiku-3, Gemini-3-Flash, DeepSeek-V3.1, Qwen3-Next-80B, Llama-3.2-3B) integrated with three memory architectures (Mem0, LangMem, Letta) over 100-turn longitudinal simulations.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

