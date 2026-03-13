---






























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0120
type: conferencePaper
short_title: SafeToolBench
year: 2025
first_author: "[[Hongfei Xia]]"
last_author: "[[Haifeng Wang]]"
authors: Hongfei Xia; Hongru Wang; Zeming Liu; Qian Yu; Yuhang Guo; Haifeng Wang
url: "https://arxiv.org/abs/2509.07315"
external_pdf: "https://arxiv.org/pdf/2509.07315.pdf"
pdf_extract: "PDF Extracts/2025/2025-Xia-SafeToolBench.md"
local_pdf: "[[PDFs/2025/2025-Xia-SafeToolBench.pdf]]"
publication: "EMNLP 2025"
CONF-CC: "EMNLP 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Large Language Models (LLMs) have exhibited great performance in autonomously calling various tools in external environments, leading to better problem solving and task automation capabilities. However, these external tools also amplify potential risks such as financial loss or privacy leakage with ambiguous or malicious user instructions. Compared to previous studies, which mainly assess the safety awareness of LLMs after obtaining the tool execution results (i.e."
LLM_assessed: "GPT-4o, Llama-3, Qwen-2"
DATA_URL: "https://github.com/BITHLP/SafeToolBench"
research_topic: "Other"
CONFERENCE: "EMNLP 2025"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# SafeToolBench

## Authors

[[Hongfei Xia]], [[Hongru Wang]], [[Zeming Liu]], [[Qian Yu]], [[Yuhang Guo]], [[Haifeng Wang]]

## Metadata

**Authors:** Hongfei Xia, Hongru Wang, Zeming Liu, Qian Yu, Yuhang Guo, Haifeng Wang

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2509.07315

## Abstract

Large Language Models (LLMs) have exhibited great performance in autonomously calling various tools in external environments, leading to better problem solving and task automation capabilities. However, these external tools also amplify potential risks such as financial loss or privacy leakage with ambiguous or malicious user instructions. Compared to previous studies, which mainly assess the safety awareness of LLMs after obtaining the tool execution results (i.e., retrospective evaluation), this paper focuses on prospective ways to assess the safety of LLM tool utilization, aiming to avoid irreversible harm caused by directly executing tools. To this end, we propose SafeToolBench, the first benchmark to comprehensively assess tool utilization security in a prospective manner, covering malicious user instructions and diverse practical toolsets. Additionally, we propose a novel framework, SafeInstructTool, which aims to enhance LLMs’ awareness of tool utilization security from three perspectives (i.e., User Instruction, Tool Itself, and Joint InstructionTool), leading to nine detailed dimensions in total. We experiment with four LLMs using different methods, revealing that existing approaches fail to capture all risks in tool utilization. In contrast, our framework significantly enhances LLMs’ self-awareness, enabling a more safe and trustworthy tool utilization. Our code and data are publicly available at https: //github.com/BITHLP/SafeToolBench.

## Dataset Information

16 everyday domains

## Data Description

SafeToolBench: 1,200 high-quality tool-use safety evaluation samples covering 4 risk categories (Privacy Leak, Property Damage, Physical Injury, Bias & Offensiveness) across 16 real-world application domains, with prospective risk assessment before tool execution.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** MEDIUM

## Tags

