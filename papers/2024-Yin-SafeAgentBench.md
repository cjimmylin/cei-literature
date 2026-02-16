---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0215
type: preprint
short_title: SafeAgentBench
year: 2024
first_author: "[[Yin, Sheng]]"
last_author: "[[Chen, Siheng]]"
authors: "[[Yin, Sheng]]; [[Pang, Xianghe]]; [[Ding, Yuanzhuo]]; [[Chen, Menglan]]; [[Bi, Yutong]]; [[Xiong, Yichen]]; [[Huang, Wenhao]]; [[Xiang, Zhen]]; [[Shao, Jing]]; [[Chen, Siheng]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2412.13178"
external_pdf: "https://arxiv.org/pdf/2412.13178.pdf"
pdf_extract: "PDF Extracts/0000/2024-Yin-SafeAgentBench.md"
local_pdf: "[[PDFs/2024/2024-Yin-SafeAgentBench.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "With the integration of large language models (LLMs), embodied agents have strong capabilities to understand and plan complicated natural language instructions. However, a foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in the real world. Existing benchmarks predominantly overlook critical safety risks, focusing solely on planning performance, while a few evaluate LLMs' safety awareness only on non-interactive..."
LLM_assessed: "GPT-4, Gemini, Llama-3, Qwen, DeepSeek"
DATA_URL: "https://github.com/shengyin1224/SafeAgentBench"
research_topic: "Other"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# SafeAgentBench

## Authors

[[Yin, Sheng]], [[Pang, Xianghe]], [[Ding, Yuanzhuo]], [[Chen, Menglan]], [[Bi, Yutong]], [[Xiong, Yichen]], [[Huang, Wenhao]], [[Xiang, Zhen]], [[Jing Shao|Shao, Jing]], [[Chen, Siheng]]

## Metadata

**Authors:** Yin, Sheng; Pang, Xianghe; Ding, Yuanzhuo; Chen, Menglan; Bi, Yutong; Xiong, Yichen; Huang, Wenhao; Xiang, Zhen; Shao, Jing; Chen, Siheng

**Year:** 2024

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2412.13178
- **Code/Data:** https://github.com/shengyin1224/SafeAgentBench; https://huggingface.co/datasets/safeagentbench/SafeAgentBench

## Abstract

With the integration of large language models (LLMs), embodied agents have strong capabilities to understand and plan complicated natural language instructions. However, a foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in the real world. Existing benchmarks predominantly overlook critical safety risks, focusing solely on planning performance, while a few evaluate LLMs’ safety awareness only on non-interactive image-text data. To address this gap, we present SafeAgentBench—the first comprehensive benchmark for safety-aware task planning of embodied LLM agents in interactive simulation environments, covering both explicit and implicit hazards. SafeAgentBench includes: (1) an executable, diverse, and high-quality dataset of 750 tasks, rigorously curated to cover 10 potential hazards and 3 task types; (2) SafeAgentEnv, a universal embodied environment with a low-level controller, supporting multi-agent execution with 17 high-level actions for 9 state-of-the-art baselines; and (3) reliable evaluation methods from both execution and semantic perspectives. Experimental results show that, although agents based on different design frameworks exhibit substantial differences in task success rates, their overall safety awareness remains weak. The most safety-conscious baseline achieves only a 10% rejection rate for detailed hazardous tasks. Moreover, simply replacing the LLM driving the agent does not lead to notable improvements in safety awareness. Dataset and codes are available in https://github.com/shengyin1224/SafeAgentBench and https://huggingface.co/datasets/safeagentbench/SafeAgentBench.

## Dataset Information

750 tasks

## Data Description

SafeAgentBench is the first comprehensive benchmark for safety-aware task planning of embodied LLM agents, featuring 750 executable tasks (450 hazardous, 300 safe) covering 10 potential hazards and 3 task types (detailed, abstract, long-horizon) in interactive simulation environments based on AI2-THOR. Nine representative embodied LLM agent baselines were evaluated, each driven by GPT-4, Gemini-2.5-Pro, Llama3-8B, Qwen2-7B, and DeepSeek-V2.5, with results showing that even the best baseline achieved only a 10% rejection rate for detailed hazardous tasks.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

