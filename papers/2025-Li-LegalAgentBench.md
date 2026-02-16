---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0076
type: conferencePaper
short_title: LegalAgentBench
year: 2025
first_author: "[[Li, Haitao]]"
last_author: "[[Huang, Minlie]]"
authors: "[[Li, Haitao]]; [[Chen, Junjie]]; [[Yang, Jingli]]; [[Ai, Qingyao]]; [[Jia, Wei]]; [[Liu, Youfeng]]; [[Lin, Kai]]; [[Wu, Yueyue]]; [[Yuan, Guozhi]]; [[Hu, Yiran]]; [[Wang, Wuyue]]; [[Liu, Yiqun]]; [[Huang, Minlie]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2412.17259"
external_pdf: "https://arxiv.org/pdf/2412.17259.pdf"
pdf_extract: "PDF Extracts/0000/2025-Li-LegalAgentBench.md"
local_pdf: "[[PDFs/2025/2025-Li-LegalAgentBench.pdf]]"
publication: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "With the increasing intelligence and autonomy of LLM agents, their potential applications in the legal domain are becoming increasingly apparent. However, existing general-domain benchmarks cannot fully capture the complexity and subtle nuances of real-world judicial cognition and decision-making. Therefore, we propose LegalAgentBench, a comprehensive benchmark specifically designed to evaluate LLM Agents in the Chinese legal domain."
LLM_assessed: "GPT-4o, GPT-4o mini, GPT-3.5, Claude, Llama-3, Qwen"
DATA_URL: "https://github.com/CSHaitao/LegalAgentBench"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset"
data_metrics: "Not specified"
---
# LegalAgentBench

## Authors

[[Li, Haitao]], [[Chen, Junjie]], [[Yang, Jingli]], [[Ai, Qingyao]], [[Jia, Wei]], [[Youfeng Liu|Liu, Youfeng]], [[Lin, Kai]], [[Wu, Yueyue]], [[Yuan, Guozhi]], [[Hu, Yiran]], [[Wang, Wuyue]], [[Liu, Yiqun]], [[Minlie Huang|Huang, Minlie]]

## Metadata

**Authors:** Li, Haitao; Chen, Junjie; Yang, Jingli; Ai, Qingyao; Jia, Wei; Liu, Youfeng; Lin, Kai; Wu, Yueyue; Yuan, Guozhi; Hu, Yiran; Wang, Wuyue; Liu, Yiqun; Huang, Minlie

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2412.17259
- **Code/Data:** https://github.com/CSHaitao/LegalAgentBench](https://github.com/CSHaitao/LegalAgentBench

## Abstract

With the increasing intelligence and autonomy of LLM agents, their potential applications in the legal domain are becoming increasingly apparent. However, existing general-domain benchmarks cannot fully capture the complexity and subtle nuances of real-world judicial cognition and decision-making. Therefore, we propose LegalAgentBench, a comprehensive benchmark specifically designed to evaluate LLM Agents in the Chinese legal domain. LegalAgentBench includes 17 corpora from real-world legal scenarios and provides 37 tools for interacting with external knowledge. We designed a scalable task construction framework and carefully annotated 300 tasks. These tasks span various types, including multi-hop reasoning and writing, and range across different difficulty levels, effectively reflecting the complexity of real-world legal scenarios. Moreover, beyond evaluating final success, LegalAgentBench incorporates keyword analysis during intermediate processes to calculate progress rates, enabling more fine-grained evaluation. We evaluated eight popular LLMs, highlighting the strengths, limitations, and potential areas for improvement of existing models and methods. LegalAgentBench sets a new benchmark for the practical application of LLMs in the legal domain, with its code and data available at https://github.com/CSHaitao/ LegalAgentBench.

## Dataset Information

300 carefully annotated tasks

## Data Description

LegalAgentBench is a benchmark for evaluating LLM agents in the Chinese legal domain, comprising 17 real-world corpora (14 tabular databases and 3 document collections) and 37 specialized tools. It includes 300 carefully annotated tasks spanning multi-hop reasoning and legal writing at varying difficulty levels (1-hop to 5-hop). Eight LLMs were evaluated using three agent methods (Plan-and-Solve, Plan-and-Execute, ReAct), with both success rate and fine-grained progress rate metrics.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

