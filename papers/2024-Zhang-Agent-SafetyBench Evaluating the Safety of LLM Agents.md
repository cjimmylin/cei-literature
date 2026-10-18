---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0144
type: preprint
short_title: "Agent-SafetyBench: Evaluating the Safety of LLM Agents"
year: 2024
first_author: "[[Zhang, Zhexin]]"
last_author: "[[Huang, Minlie]]"
authors: "Zhang, Zhexin; Cui, Shiyao; Lu, Yida; Zhou, Jingzhuo; Yang, Junxiao; Wang, Hongning; Huang, Minlie"
authors_incomplete: false
url: "https://arxiv.org/abs/2412.14470"
external_pdf: "https://arxiv.org/pdf/2412.14470.pdf"
pdf_extract: "PDF Extracts/2024/2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents.pdf]]"
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
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
abstract: "As large language models (LLMs) are increasingly deployed as agents, their integration into interactive environments and tool use introduce new safety challenges beyond those associated with the models themselves. However, the absence of comprehensive benchmarks for evaluating agent safety presents a significant barrier to effective assessment and further improvement. In this paper, we introduce AGENTSAFETYBENCH, a comprehensive benchmark designed to evaluate the safety of LLM agents."
LLM_assessed: "Claude-3 Haiku, Claude-3 Opus, Claude-3 Sonnet, DeepSeek, GPT-4, GPT-4o, Gemini, Llama-3, Qwen-2"
DATA_URL: "https://github.com/thu-coai/Agent-SafetyBench/"
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
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: FR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "2,000 test cases; 8 categories"
---
# Agent-SafetyBench: Evaluating the Safety of LLM Agents

## Authors

[[Zhexin Zhang|Zhang, Zhexin]], [[Cui, Shiyao]], [[Lu, Yida]], [[Zhou, Jingzhuo]], [[Yang, Junxiao]], [[Hongning Wang|Wang, Hongning]], [[Minlie Huang|Huang, Minlie]]

## Metadata

**Authors:** Zhang, Zhexin; Cui, Shiyao; Lu, Yida; Zhou, Jingzhuo; Yang, Junxiao; Wang, Hongning; Huang, Minlie

**Year:** 2024

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2412.14470
- **Code/Data:** https://github.com/thu-coai/Agent-SafetyBench

## Abstract

As large language models (LLMs) are increasingly deployed as agents, their integration into interactive environments and tool use introduce new safety challenges beyond those associated with the models themselves. However, the absence of comprehensive benchmarks for evaluating agent safety presents a significant barrier to effective assessment and further improvement. In this paper, we introduce AGENTSAFETYBENCH, a comprehensive benchmark designed to evaluate the safety of LLM agents. AGENT-SAFETYBENCH encompasses 349 interaction environments and 2,000 test cases, evaluating 8 categories of safety risks and covering 10 common failure modes frequently encountered in unsafe interactions. Our evaluation of 16 popular LLM agents reveals a concerning result: none of the agents achieves a safety score above 60%. This highlights significant safety challenges in LLM agents and underscores the considerable need for improvement. Through failure mode and helpfulness analysis, we summarize two fundamental safety defects in current LLM agents: lack of robustness and lack of risk awareness. Furthermore, our findings suggest that reliance on defense prompts alone may be insufficient to address these safety issues, emphasizing the need for more advanced and robust strategies. To drive progress in this area, AGENT-SAFETYBENCH has been released 1 to facilitate further research in agent safety evaluation and improvement.

## Dataset Information

See report

## Data Description

AGENT-SAFETYBENCH is a comprehensive safety benchmark for LLM agents with 349 interaction environments and 2,000 test cases covering 8 categories of safety risks and 10 failure modes, evaluating 16 popular LLM agents.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8, Agent 16
**Implementation Readiness:** HIGH

## Tags

