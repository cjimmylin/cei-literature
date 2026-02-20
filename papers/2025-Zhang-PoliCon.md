---










Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0107
type: preprint
short_title: PoliCon
year: 2025
first_author: "[[Zhaowei Zhang]]"
last_author: "[[Yaodong Yang]]"
authors: "Zhaowei Zhang; Xiaobo Wang; Minghua Yi; Mengmeng Wang; Fengshuo Bai; Zilong Zheng; Yipeng Kang; Yaodong Yang"
url: "https://arxiv.org/abs/2505.19558"
external_pdf: "https://arxiv.org/pdf/2505.19558.pdf"
pdf_extract: "PDF Extracts/0000/2025-Zhang-PoliCon.md"
local_pdf: "[[PDFs/2025/2025-Zhang-PoliCon.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "European"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Achieving political consensus is crucial yet challenging for the effective functioning of social governance. However, although frontier AI systems represented by large language models (LLMs) have developed rapidly in recent years, their capabilities in this scope are still understudied. In this paper, we introduce PoliCon, a novel benchmark constructed from 2,225 high-quality deliberation records of the European Parliament over 13 years, ranging from 2009 to 2022, to evaluate the ability of LLMs to draft consensus resolutions based on divergent party positions under varying collective decision-making contexts and political requirements. Specifically, PoliCon incorporates four factors to build each task environment for finding different political consensus: specific political issues, political goals, participating parties, and power structures based on seat distribution. We also developed an evaluation framework based on social choice theory for PoliCon, which simulates the real voting outcomes of different political parties to assess whether LLM-generated resolutions meet the requirements of the predetermined political consensus. Our experimental results demonstrate that even state-of-the-art models remain undersatisfied with complex tasks like passing resolutions by a two-thirds majority and addressing security issues, while uncovering their inherent partisan biases and revealing some behaviors LLMs show to achieve the consensus, such as prioritizing the stance of the dominant party instead of uniting smaller parties, which highlights PoliCon's promise as an effective platform for studying LLMs' ability to promote political consensus. The code and dataset are released at https://zowiezhang.github.io/projects/PoliCon."
LLM_assessed: "GPT-4, Qwen, Llama-3, DeepSeek"
DATA_URL: "NA"
normative_ethics_benchmark: Borderline
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Other"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# PoliCon

## Authors

[[Zhaowei Zhang]], [[Xiaobo Wang]], [[Minghua Yi]], [[Mengmeng Wang]], [[Fengshuo Bai]], [[Zilong Zheng]], [[Yipeng Kang]], [[Yaodong Yang]]

## Metadata

**Authors:** Zhaowei Zhang; Xiaobo Wang; Minghua Yi; Mengmeng Wang; Fengshuo Bai; Zilong Zheng; Yipeng Kang; Yaodong Yang

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2505.19558

## Abstract

*(To be fetched)*

## Dataset Information

2,225 high-quality deliberation records from European Parliament over 13 years (2009-2022); tasks vary by political issues, goals, parties, and power structures

## Data Description

PoliCon is a political consensus benchmark constructed from 2,225 high-quality deliberation records of the European Parliament spanning 13 years (2009-2022). The dataset incorporates four adjustable factors (political issues, political goals, participating parties, and power structures) to construct 28,620 distinct political scenarios across 5 coarse-grained and 19 fine-grained topic categories. Each data entry contains a sextuple of issue, topic, background, stances, resolution, and votes, cleaned and processed using DeepSeek-R1 and rule-based methods.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** MEDIUM

## Tags

