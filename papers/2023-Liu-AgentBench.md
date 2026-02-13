---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UE2C6FNV
type: conferencePaper
short_title: AgentBench
year: 2025
first_author: "[[Xiao Liu]]"
last_author: "[[Jie Tang]]"
authors: "Xiao Liu; Hao Yu; Hanchen Zhang; Yifan Xu; Xuanyu Lei; Hanyu Lai; Yu Gu; Hangliang Ding; Kaiwen Men; Kejuan Yang; Shudan Zhang; Xiang Deng; Aohan Zeng; Zhengxiao Du; Chenhui Zhang; Sheng Shen; Tianjun Zhang; Yu Su; Huan Sun; Minlie Huang; Yuxiao Dong; Jie Tang"
doi: 10.48550/arXiv.2308.03688
url: "http://arxiv.org/abs/2308.03688"
external_pdf: "http://arxiv.org/pdf/2308.03688.pdf"
publication: "International Conference on Learning Representations"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "A comprehensive benchmark for evaluating LLMs as *agents* in interactive environments (OS, Database, Knowledge Graph, etc.), measuring reasoning and decision-making."
significance: "Shifts evaluation from static text to dynamic agency, showing a huge gap between commercial models (GPT-4) and open models in dealing with multi-step, interactive tasks."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Liu-AgentBench.md"
abstract: "The potential of Large Language Model (LLM) as agents has been widely acknowl- edged recently. Thus, there is an urgent need to quantitatively evaluate LLMs as agents on challenging tasks in interactive environments. We present AGENTBENCH, a multi-dimensional benchmark that consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities. Our extensive test over 29 API-based and open-sourced (OSS) LLMs shows that, while top commercial LLMs present a strong abi"
paper_summary: "Abstract: The potential of Large Language Model (LLM) as agents has been widely acknowl- edged recently. Thus, there is an urgent need to quantitatively evaluate LLMs as agents on challenging tasks in interacti | Overview: Published as a conference paper at ICLR 2024 AGENTBENCH: EVALUATING LLMS AS AGENTS Xiao Liu1,*, Hao Yu1,*,†, Hanchen Zhang1,*, Yifan Xu1, Xuanyu Lei1, Hanyu Lai1, Yu Gu2,†, Hangliang Ding1, Kaiwen Men | Key Findings: scope rounds out to be codellama-34b, achieving an overall score of 0.96 but still presents a clear performance gap to gpt-3.5-turbo. Our community st | Conclusions: We present AGENTBENCH, a systematically designed multi-dimensional evolving benchmark for evaluating LLMs as agents, covering as many as 29 LLMs in th"
local_pdf: [[PDFs/2023/2023-Liu-AgentBench.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, text-davinci, Claude, Llama-2, CodeLlama, Vicuna"
DATA_URL: "https://github.com/THUDM/AgentBench"
---
# AgentBench: Evaluating LLMs as Agents

## Metadata

**Authors:** Liu, Xiao; Yu, Hao; Zhang, Hanchen; Xu, Yifan; Lei, Xuanyu; Lai, Hanyu; Gu, Yu; Ding, Hangliang; Men, Kaiwen; Yang, Kejuan; Zhang, Shudan; Deng, Xiang; Zeng, Aohan; Du, Zhengxiao; Zhang, Chenhui; Shen, Sheng; Zhang, Tianjun; Su, Yu; Sun, Huan; Huang, Minlie; Dong, Yuxiao; Tang, Jie

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2308.03688](https://doi.org/10.48550/arXiv.2308.03688)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Liu-AgentBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2308.03688
- **DOI:** https://doi.org/10.48550/arXiv.2308.03688

## Abstract

Large Language Models (LLMs) are becoming increasingly smart and autonomous, targeting real-world pragmatic missions beyond traditional NLP tasks. As a result, there has been an urgent need to evaluate LLMs as agents on challenging tasks in interactive environments. We present AGENTBENCH, a multi-dimensional evolving benchmark that currently consists of 8 distinct environments to assess LLM-as-Agent’s reasoning and decision-making abilities in a multi-turn openended generation setting. Our extensive test over 27 API-based and open-sourced (OSS) LLMs shows that, while top commercial LLMs present a strong ability of acting as agents in complex environments, there is a significant disparity in performance between them and OSS competitors. We identify the typical reasons of failures in environments and LLMs, showing that poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles for developing usable LLM agents. Training on code and high quality multi-turn alignment data could improve agent performance. Datasets, environments, and an integrated evaluation package for AGENTBENCH are released at https:// github.com/THUDM/AgentBench.

## Authors

[[Xiao Liu]], [[Hao Yu]], [[Hanchen Zhang]], [[Yifan Xu]], [[Xuanyu Lei]], [[Hanyu Lai]], [[Yu Gu]], [[Hangliang Ding]], [[Kaiwen Men]], [[Kejuan Yang]], [[Shudan Zhang]], [[Xiang Deng]], [[Aohan Zeng]], [[Zhengxiao Du]], [[Chenhui Zhang]], [[Sheng Shen]], [[Tianjun Zhang]], [[Yu Su]], [[Huan Sun]], [[Minlie Huang]], [[Yuxiao Dong]], [[Jie Tang]]

## Data Description

AgentBench is a multi-dimensional benchmark evaluating LLM-as-Agent capabilities across 8 distinct interactive environments: Operating System, Database, Knowledge Graph, Digital Card Game, Lateral Thinking Puzzles, House-Holding, Web Shopping, and Web Browsing. The benchmark tests 29 LLMs (both API-based commercial and open-source models up to 70B parameters) on reasoning, decision-making, and instruction-following abilities in real-world scenarios.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

353 citations (Semantic Scholar/DOI) [2025-08-27] 353 citations (Semantic Scholar/arXiv) [2025-08-27] 347 citations (Semantic Scholar/DOI) [2025-08-23]
