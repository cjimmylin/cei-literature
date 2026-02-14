---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0115
type: preprint
short_title: "SI-Bench: Benchmarking Social Intelligence of Large Language Models in Human-to-Human Conversations"
year: 2025
first_author: "[[Shuai Huang]]"
last_author: "[[Jun Gao]]"
authors: "Shuai Huang; Wenxuan Zhao; Jun Gao"
url: "https://arxiv.org/abs/2510.23182"
external_pdf: "https://arxiv.org/pdf/2510.23182.pdf"
pdf_extract: "PDF Extracts/2025/2025-Huang-SI-Bench Benchmarking Social Intelligence of Large Language Models in.md"
local_pdf: "[[PDFs/2025/2025-Huang-SI-Bench Benchmarking Social Intelligence of Large Language Models in.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "As large language models (LLMs) develop anthropomorphic abilities, they are increasingly being deployed as autonomous agents to interact with humans. However, evaluating their performance in realistic and complex social interactions remains a significant challenge. Most previous research built datasets through simulated agent-to-agent interactions, which fails to capture the authentic linguistic styles and relational dynamics found in real human conversations."
research_topic: "Dialogue Systems"
data_description: "Benchmark dataset for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "Claude, GPT-4o, Gemini, Qwen"
DATA_URL: "https://github.com/SI-Bench/SI-Bench.git"
---
# SI-Bench: Benchmarking Social Intelligence of Large Language Models in Human-to-Human Conversations

## Authors

[[Shuai Huang]], [[Wenxuan Zhao]], [[Jun Gao]]

## Metadata

**Authors:** Shuai Huang; Wenxuan Zhao; Jun Gao

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2510.23182
- **Code/Data:** https://github.com/SI-Bench/SI-Bench.git](https://github.com/SI-Bench/SI-Bench.git

## Abstract

As large language models (LLMs) develop anthropomorphic abilities, they are increasingly being deployed as autonomous agents to interact with humans. However, evaluating their performance in realistic and complex social interactions remains a significant challenge. Most previous research built datasets through simulated agent-to-agent interactions, which fails to capture the authentic linguistic styles and relational dynamics found in real human conversations. To address this gap, we introduce SI-Bench, a novel benchmark designed to evaluate aspects of social intelligence in LLMs. Grounded in broad social science theories, SIBench contains 2,221 authentic multi-turn dialogues collected from a social networking application. We further selected a subset of 312 dialogues for manual annotation across 8 major models. The experiments show that SOTA models have surpassed the human expert in process reasoning under complex social situations, yet they still fall behind humans in reply quality. Moreover, introducing Chain-of-Thought (CoT) reasoning may degrade the performance of LLMs in social dialogue tasks. All datasets are openly available at https://github.com/SIBench/SI-Bench.git.

## Dataset Information

2,221 authentic multi-turn dialogues from social networking platform; 312 manually annotated dialogues across 8 models; Chinese language; anonymized

## Data Description

SI-Bench is a social intelligence benchmark containing 2,221 authentic multi-turn dialogues collected from a Chinese social networking application, covering 12 types of complex social situations. A subset of 312 dialogues was manually annotated across 8 leading LLMs (Claude-4-Opus, Claude-4-Sonnet, GPT-4o, Gemini-2.5-Pro, Gemini-2.5-Flash, Doubao-1.6-Thinking, Doubao-1.5-Pro-Character, and Qwen-2.5-Max), evaluating both reasoning process quality and reply quality in social dialogue tasks.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15, Agent 1
**Implementation Readiness:** HIGH

## Tags

