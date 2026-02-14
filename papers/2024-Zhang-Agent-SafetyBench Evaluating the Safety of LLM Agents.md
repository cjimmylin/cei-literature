---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0144
type: preprint
short_title: "Agent-SafetyBench: Evaluating the Safety of LLM Agents"
year: 2025
first_author: "[[Zhang, Zhexin]]"
last_author: "[[Huang, Minlie]]"
authors: "[[Zhang, Zhexin]]; [[Cui, Shiyao]]; [[Lu, Yida]]; [[Zhou, Jingzhuo]]; [[Yang, Junxiao]]; [[Wang, Hongning]]; [[Huang, Minlie]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2412.14470"
external_pdf: "https://arxiv.org/pdf/2412.14470.pdf"
local_pdf: "[[PDFs/2024/2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Zhang-Agent-SafetyBench Evaluating the Safety of LLM Agents.md"
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
is_dataset: No
tags: 
abstract: "As large language models (LLMs) are increasingly deployed as agents, their integration into interactive environments and tool use introduce new safety challenges beyond those associated with the models themselves. However, the absence of comprehensive benchmarks for evaluating agent safety presents a significant barrier to effective assessment and further improvement. In this paper, we introduce AGENTSAFETYBENCH, a comprehensive benchmark designed to evaluate the safety of LLM agents."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety"
data_metrics: "2,000 test cases; 8 categories"
LLM_assessed: "Claude, GPT-4, Gemini, Qwen, Llama-3, DeepSeek"
DATA_URL: "https://github.com/thu-coai/Agent-SafetyBench/"
---
# Agent-SafetyBench: Evaluating the Safety of LLM Agents

## Authors

[[Zhang, Zhexin]], [[Cui, Shiyao]], [[Lu, Yida]], [[Zhou, Jingzhuo]], [[Yang, Junxiao]], [[Wang, Hongning]], [[Huang, Minlie]]

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

AGENT-SAFETYBENCH is a comprehensive benchmark for evaluating the safety of LLM agents, encompassing 349 interaction environments and 2,000 test cases across 8 categories of safety risks and 10 common failure modes. The benchmark evaluates 16 popular LLM agents including Claude-3-Opus, Claude-3.5-Sonnet, GPT-4o, GPT-4-Turbo, Gemini-1.5-Pro/Flash, Llama-3.1 variants, Qwen2.5 variants, and DeepSeek-V2.5, revealing that none achieves a safety score above 60%.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8, Agent 16
**Implementation Readiness:** HIGH

## Tags

