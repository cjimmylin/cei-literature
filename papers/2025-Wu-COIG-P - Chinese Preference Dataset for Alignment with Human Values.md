---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0033
type: preprint
short_title: COIG-P -- Chinese Preference Dataset for Alignment with Human Values
year: 2025
first_author: "[[Siwei Wu]]"
authors: Siwei Wu; Jincheng Ren; Xinrun Du; Shuyue Guo; Xingwei Qu; Yiming Liang; Jie Liu; Yunwen Li; Tianyu Zheng; Boyu Feng; Huaqing Yuan; Zenith Wang; Jiaheng Liu; Wenhao Huang; Chenglin Cai; Haoran Que; Jian Yang; Yuelin Bai; Zekun Moore Wang; Zhouliang Yu; Qunshu Lin; Ding Pan; Yuchen Jiang; Tiannan Wang; Wangchunshu Zhou; Shenzhi Wang; Xingyuan Bu; Minghao Liu; Guoyin Wang; Ge Zhang; Chenghua Lin
url: "https://arxiv.org/abs/2504.05535"
external_pdf: "https://arxiv.org/pdf/2504.05535.pdf"
local_pdf: "[[PDFs/2025-Wu-COIG-P - Chinese Preference Dataset for Alignment with Human Values.pdf]]"
pdf_extract: "PDF Extracts/2025-Wu-COIG-P - Chinese Preference Dataset for Alignment with Human Values.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Chinese"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Aligning large language models (LLMs) with human preferences has achieved remarkable success. However, existing Chinese preference datasets are limited by small scale, narrow domain coverage, and lack of rigorous data validation. Additionally, the reliance on human annotators for instruction and response labeling significantly constrains the scalability of human preference datasets. To address these challenges, we design an LLM-based Chinese preference dataset annotation pipeline with no human..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark dataset"
data_metrics: "0 language"
---
# COIG-P -- Chinese Preference Dataset for Alignment with Human Values

## Authors

[[Siwei Wu]], [[Jincheng Ren]], [[Xinrun Du]], [[Shuyue Guo]], [[Xingwei Qu]], [[Yiming Liang]], [[Jie Liu]], [[Yunwen Li]], [[Tianyu Zheng]], [[Boyu Feng]], [[Huaqing Yuan]], [[Zenith Wang]], [[Jiaheng Liu]], [[Wenhao Huang]], [[Chenglin Cai]], [[Haoran Que]], [[Jian Yang]], [[Yuelin Bai]], [[Zekun Moore Wang]], [[Zhouliang Yu]], [[Qunshu Lin]], [[Ding Pan]], [[Yuchen Jiang]], [[Tiannan Wang]], [[Wangchunshu Zhou]], [[Shenzhi Wang]], [[Xingyuan Bu]], [[Minghao Liu]], [[Guoyin Wang]], [[Ge Zhang]], [[Chenghua Lin]]

## Metadata

**Authors:** Siwei Wu; Jincheng Ren; Xinrun Du; Shuyue Guo; Xingwei Qu; Yiming Liang; Jie Liu; Yunwen Li; Tianyu Zheng; Boyu Feng; Huaqing Yuan; Zenith Wang; Jiaheng Liu; Wenhao Huang; Chenglin Cai; Haoran Que; Jian Yang; Yuelin Bai; Zekun Moore Wang; Zhouliang Yu; Qunshu Lin; Ding Pan; Yuchen Jiang; Tiannan Wang; Wangchunshu Zhou; Shenzhi Wang; Xingyuan Bu; Minghao Liu; Guoyin Wang; Ge Zhang; Chenghua Lin

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.05535
- **Code/Data:** https://github.com/multimodal-art-projection/COIG-P; https://huggingface.co/datasets/m-a-p/COIG-P

## Abstract

Aligning large language models (LLMs) with human preferences has achieved remarkable success. However, existing Chinese preference datasets are limited by small scale, narrow domain coverage, and lack of rigorous data validation. Additionally, the reliance on human annotators for instruction and response labeling significantly constrains the scalability of human preference datasets. To address these challenges, we design an LLM-based Chinese preference dataset annotation pipeline with no human intervention. Specifically, we crawled and carefully filtered 92k high-quality Chinese queries and employed 15 mainstream LLMs to generate and score chosen-rejected response pairs. Based on it, we introduce COIG-P (Chinese Open Instruction Generalist - Preference), a high-quality, large-scale Chinese preference dataset, comprises 1,006k Chinese preference pairs spanning 6 diverse domains: Chat, Code, Math, Logic, Novel, and Role. Building upon COIG-P, to reduce the overhead of using LLMs for scoring, we trained a 8B-sized Chinese Reward Model (CRM) and meticulously constructed a Chinese Reward Benchmark (CRBench). Evaluation results based on AlignBench [Liu et al., 2024a] show that that COIG-P significantly outperforms other Chinese preference datasets, and it brings significant performance improvements ranging from 2% to 12% for the Qwen2/2.5 and Infinity-Instruct-3M-0625 model series, respectively. The results on CRBench demonstrate that our CRM has a strong and robust scoring ability. We apply it to filter chosen-rejected response pairs in a test split of COIG-P, and our experiments show that it is comparable to GPT-4o in identifying low-quality samples while maintaining efficiency and cost-effectiveness. Our codes and data are released in https://github.com/multimodal-art-projection/COIG-P. COIG-P ZAKE II-3M-Qwen2-7B Zhihu-Rlhf-3k Huozi RLHF-CN CVALUES 3.50 3.75 4.00 4.25 4.50 4.75 5.00 5.25 5.50 Overall COIG-P ZAKE II-3M-Qwen2-7B Zhihu-Rlhf-3k Huozi RLHF-CN CVALUES 3.5 4.0 4.5 5.0 5.5 6.0 Language COIG-P ZAKE II-3M-Qwen2-7B Zhihu-Rlhf-3k Huozi RLHF-CN CVALUES 3.00 3.25 3.50 3.75 4.00 4.25 4.50 4.75 5.00 Reasoning Figure 1. The results of different Chinese human preference datasets trained on Infinity-Instruct-3M-0625-Qwen2-7B. arXiv:2504.05535v1 [cs.CL] 7 Apr

## Dataset Information

1,009,000 Chinese preference pairs (very large scale)

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

