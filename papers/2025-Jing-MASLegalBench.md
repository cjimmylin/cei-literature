---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0080
type: preprint
short_title: MASLegalBench
year: 2025
first_author: "[[Huihao Jing]]"
last_author: "[[Yangqiu Song]]"
authors: "Huihao Jing; Wenbin Hu; Hongyu Luo; Jianhui Yang; Wei Fan; Haoran Li; Yangqiu Song"
url: "https://arxiv.org/abs/2509.24922"
external_pdf: "https://arxiv.org/pdf/2509.24922.pdf"
pdf_extract: "PDF Extracts/0000/2025-Jing-MASLegalBench.md"
local_pdf: "[[PDFs/2025/2025-Jing-MASLegalBench.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "Multi-agent systems (MAS), leveraging the remarkable capabilities of Large Language Models (LLMs), show great potential in addressing complex tasks. In this context, integrating MAS with legal tasks is a crucial step. While previous studies have developed legal benchmarks for LLM agents, none are specifically designed to consider the unique advantages of MAS, such as task decomposition, agent specialization, and flexible training."
research_topic: "Other"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, DeepSeek, Llama-3, Qwen"
DATA_URL: "https://github.com/HKUST-KnowComp/MASLegalBench"
---
# MASLegalBench

## Authors

[[Huihao Jing]], [[Wenbin Hu]], [[Hongyu Luo]], [[Jianhui Yang]], [[Wei Fan]], [[Haoran Li]], [[Yangqiu Song]]

## Metadata

**Authors:** Huihao Jing; Wenbin Hu; Hongyu Luo; Jianhui Yang; Wei Fan; Haoran Li; Yangqiu Song

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.24922
- **Code/Data:** https://github.com/HKUST-KnowComp/MASLegalBench](https://github.com/HKUST-KnowComp/MASLegalBench

## Abstract

Multi-agent systems (MAS), leveraging the remarkable capabilities of Large Language Models (LLMs), show great potential in addressing complex tasks. In this context, integrating MAS with legal tasks is a crucial step. While previous studies have developed legal benchmarks for LLM agents, none are specifically designed to consider the unique advantages of MAS, such as task decomposition, agent specialization, and flexible training. In fact, the lack of evaluation methods limits the potential of MAS in the legal domain. To address this gap, we propose MASLegalBench, a legal benchmark tailored for MAS and designed with a deductive reasoning approach. Our benchmark uses GDPR as the application scenario, encompassing extensive background knowledge and covering complex reasoning processes that effectively reflect the intricacies of real-world legal situations. Furthermore, we manually design various role-based MAS and conduct extensive experiments using different state-of-the-art LLMs. Our results highlight the strengths, limitations, and potential areas for improvement of existing models and MAS architectures1.

## Dataset Information

950 multiple-choice questions

## Data Description

The paper proposes MASLegalBench, a legal benchmark for multi-agent systems based on GDPR court cases, containing 950 multiple-choice questions (647 yes/no and 303 single-choice) derived from real UK enforcement reports. The benchmark follows an extended IRAC reasoning framework with four role-based agents (Facts, Rules, Application, Common Sense). Five Meta-LLMs were tested: Llama3.1-8B-Instruct, Qwen2.5-7B-Instruct, Qwen3-8B, DeepSeek-v3.1, and GPT-4o-mini, with DeepSeek-v3.1 as the sub-task agent.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

