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
authors: "Yin, Sheng; Pang, Xianghe; Ding, Yuanzhuo; Chen, Menglan; Bi, Yutong; Xiong, Yichen; Huang, Wenhao; Xiang, Zhen; Shao, Jing; Chen, Siheng"
authors_incomplete: false
url: "https://arxiv.org/abs/2412.13178"
external_pdf: "https://arxiv.org/pdf/2412.13178.pdf"
pdf_extract: "PDF Extracts/2024/2024-Yin-SafeAgentBench.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Yin-SafeAgentBench.pdf]]"
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 5
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
tags: 
abstract: "With the integration of large language models (LLMs), embodied agents have strong capabilities to understand and plan complicated natural language instructions. However, a foreseeable issue is that those embodied agents can also flawlessly execute some hazardous tasks, potentially causing damages in the real world. Existing benchmarks predominantly overlook critical safety risks, focusing solely on planning performance, while a few evaluate LLMs' safety awareness only on non-interactive..."
LLM_assessed: "DeepSeek, GPT-4, Gemini, Llama-3, Qwen"
DATA_URL: "https://github.com/shengyin1224/SafeAgentBench"
research_topic: Other
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 5
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CN
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 36
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
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

SafeAgentBench is a benchmark dataset of 750 embodied tasks (450 hazardous, 300 safe) covering 10 hazard types and 3 task types (detailed, abstract, long-horizon) for safety-aware task planning of embodied LLM agents in an interactive simulation environment. Also available at https://huggingface.co/datasets/safeagentbench/SafeAgentBench.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

