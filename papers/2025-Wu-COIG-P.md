---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YFJKRWXR
type: document
short_title: COIG-P
year: 2025
first_author: "[[M-A-P Team]]"
last_author: "[[Chenghua Lin]]"
authors: "M-A-P Team; Siwei Wu; Jincheng Ren; Xinrun Du; Shuyue Guo; Xingwei Qu; Yiming Liang; Jie Liu; Yunwen Li; Tianyu Zheng; Boyu Feng; Huaqing Yuan; Zenith Wang; Jiaheng Liu; Wenhao Huang; Chenglin Cai; Haoran Que; Jian Yang; Yuelin Bai; Zekun Moore Wang; Zhouliang Yu; Qunshu Lin; Ding Pan; Yuchen Jiang; Tiannan Wang; Wangchunshu Zhou; Shenzhi Wang; Xingyuan Bu; Minghao Liu; Guoyin Wang; Ge Zhang; Chenghua Lin"
url: "https://arxiv.org/abs/2504.05535"
external_pdf: "https://arxiv.org/pdf/2504.05535.pdf"
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Introduced COIG-P, a large-scale Chinese preference dataset (1M+ pairs) across 6 domains, and CRBench, a reward model benchmark, created via a scalable LLM-only pipeline."
significance: "Enables high-quality value alignment for Chinese LLMs at a massive scale, bypassing the bottlenecks of human annotation and achieving significant performance boosts in alignment assessments."
tags: 
pdf_extract: "PDF Extracts/0000/2025-Wu-COIG-P.md"
abstract: "Aligning large language models (LLMs) with human preferences has achieved remarkable success. However, existing Chinese preference datasets are limited by small scale, narrow domain coverage, and lack of rigorous data validation. Additionally, the reliance on human annotators for instruction and response labeling significantly constrains the scalability of human preference datasets. To address these challenges, we design an LLM-based Chinese preference dataset annotation pipeline with no human i"
paper_summary: "Abstract: Aligning large language models (LLMs) with human preferences has achieved remarkable success. However, existing Chinese preference datasets are limited by small scale, narrow domain coverage, and lack | Overview: M-A-P COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values M-A-P, 2077AI Abstract Aligning large language models (LLMs) with human preferences has achieved | Key Findings: models may favor responses that resemble their own outputs [Li et al., 2024a, Liu et al., 2024b]. Furthermore, even in LLM-driven pipelines, certain s | Conclusions: 13 8 Contributions and Acknowledgments 15 A Prompts 21 B Open-source datasets 22 C Examples 24 2 --- Page 3 ---"
local_pdf: "[[PDFs/2025/2025-Wu-COIG-P.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-3.5, Claude, DeepSeek, Qwen, Gemini"
DATA_URL: "https://github.com/multimodal-art-projection/COIG-P"
publication: arXiv
DATE_ADDED: 20260207
---
# COIG-P: A High-Quality and Large-Scale Chinese Preference Dataset for Alignment with Human Values

## Metadata

**Authors:** Team, M-A-P; Wu, Siwei; Ren, Jincheng; Du, Xinrun; Guo, Shuyue; Qu, Xingwei; Liang, Yiming; Liu, Jie; Li, Yunwen; Zheng, Tianyu; Feng, Boyu; Yuan, Huaqing; Wang, Zenith; Liu, Jiaheng; Huang, Wenhao; Cai, Chenglin; Que, Haoran; Yang, Jian; Bai, Yuelin; Wang, Zekun Moore; Yu, Zhouliang; Lin, Qunshu; Pan, Ding; Jiang, Yuchen; Wang, Tiannan; Zhou, Wangchunshu; Wang, Shenzhi; Bu, Xingyuan; Liu, Minghao; Wang, Guoyin; Zhang, Ge; Lin, Chenghua

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Wu-COIG-P.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2504.05535

## Abstract

Aligning large language models (LLMs) with human preferences has achieved remarkable success. However, existing Chinese preference datasets are limited by small scale, narrow domain coverage, and lack of rigorous data validation. Additionally, the reliance on human annotators for instruction and response labeling significantly constrains the scalability of human preference datasets. To address these challenges, we design an LLM-based Chinese preference dataset annotation pipeline with no human intervention. Specifically, we crawled and carefully filtered 92k high-quality Chinese queries and employed 15 mainstream LLMs to generate and score chosen-rejected response pairs. Based on it, we introduce COIG-P (Chinese Open Instruction Generalist - Preference), a high-quality, large-scale Chinese preference dataset, comprises 1,009k Chinese preference pairs spanning 6 diverse domains: Chat, Code, Math, Logic, Novel, and Role. Building upon COIG-P, to reduce the overhead of using LLMs for scoring, we trained a 8B-sized Chinese Reward Model (CRM) and meticulously constructed a Chinese Reward Benchmark (CRBench). Evaluation results based on AlignBench \citep{liu2024alignbenchbenchmarkingchinesealignment} show that that COIG-P significantly outperforms other Chinese preference datasets, and it brings significant performance improvements ranging from 2% to 12% for the Qwen2/2.5 and Infinity-Instruct-3M-0625 model series, respectively. The results on CRBench demonstrate that our CRM has a strong and robust scoring ability. We apply it to filter chosen-rejected response pairs in a test split of COIG-P, and our experiments show that it is comparable to GPT-4o in identifying low-quality samples while maintaining efficiency and cost-effectiveness. Our codes and data are released in https://github.com/multimodal-art-projection/COIG-P.

## Authors

[[M-A-P Team]], [[Siwei Wu]], [[Jincheng Ren]], [[Xinrun Du]], [[Shuyue Guo]], [[Xingwei Qu]], [[Yiming Liang]], [[Jie Liu]], [[Yunwen Li]], [[Tianyu Zheng]], [[Boyu Feng]], [[Huaqing Yuan]], [[Zenith Wang]], [[Jiaheng Liu]], [[Wenhao Huang]], [[Chenglin Cai]], [[Haoran Que]], [[Jian Yang]], [[Yuelin Bai]], [[Zekun Moore Wang]], [[Zhouliang Yu]], [[Qunshu Lin]], [[Ding Pan]], [[Yuchen Jiang]], [[Tiannan Wang]], [[Wangchunshu Zhou]], [[Shenzhi Wang]], [[Xingyuan Bu]], [[Minghao Liu]], [[Guoyin Wang]], [[Ge Zhang]], [[Chenghua Lin]]

## Data Description

COIG-P (Chinese Open Instruction Generalist - Preference) is a large-scale Chinese preference dataset containing 1,006,949 chosen-rejected response pairs across six domains (Chat, Code, Math, Logic, Novel, Role). The dataset was constructed from 92,784 high-quality Chinese queries with responses generated by 15 mainstream LLMs and scored by 8 LLMs. It includes a Chinese Reward Model (CRM) and a manually curated Chinese Reward Benchmark (CRBench) for evaluating preference alignment.


## Notes


## Citation Info

2 citations (Semantic Scholar/arXiv) [2025-08-27]
