---






























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0845
type: preprint
short_title: "TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks,"
year: 2025
first_author: "[[Chen, Xiuyuan]]"
last_author: "[[Li, Xuelong]]"
authors: "Chen, Xiuyuan; Zhao, Jian; He, Yuxiang; Xun, Yuan; Liu, Xinwei; Li, Yanshu; Zhou, Huilin; Cai, Wei; Shi, Ziyan; Yuan, Yuchen; Zhang, Tianle; Zhang, Chi; Li, Xuelong"
authors_incomplete: false
url: "https://www.arxiv.org/pdf/2512.05485"
external_pdf: "https://arxiv.org/pdf/2512.05485.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Chen-TeleAI-Safety A comprehensive LLM jailbreaking benchmark towards.md"
local_pdf: "[[PDFs/2025/2025-Chen-TeleAI-Safety A comprehensive LLM jailbreaking benchmark towards.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese, English"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Claude, DeepSeek, GPT-4, GPT-4o mini, GPT-5, Gemini, Grok, Llama-3, Qwen-1.5, Qwen-2, Vicuna"
DATA_URL: "https://github.com/yuanyc06/Tele-Safety"
tags: 
abstract: "While the deployment of large language models (LLMs) in high-value industries continues to expand, the systematic assessment of their safety against jailbreak and promptbased attacks remains insufficient. Existing safety evaluation benchmarks and frameworks are often limited by an imbalanced integration of core components (attack, defense, and evaluation methods) and an isolation between flexible evaluation frameworks and standardized benchmarking capabilities."
ethics_perspective: "AI Safety & Alignment"
CONFERENCE: "Preprint"
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety text corpus"
data_metrics: "342 samples"
---
# TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks,

## Authors

[[Chen, Xiuyuan]], [[Zhao, Jian]], [[He, Yuxiang]], [[Xun, Yuan]], [[Liu, Xinwei]], [[Li, Yanshu]], [[Zhou, Huilin]], [[Cai, Wei]], [[Shi, Ziyan]], [[Yuan, Yuchen]], [[Zhang, Tianle]], [[Zhang, Chi]], [[Li, Xuelong]]

## Metadata

**Authors:** Xiuyuan Chen; Jian Zhao; Yuxiang He; Yuan Xun; Xinwei Liu; Yanshu Li; Huilin Zhou; Wei Cai; Ziyan Shi; Yuchen Yuan; Tianle Zhang; Chi Zhang; Xuelong Li

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Arabic, English, Multilingual

**Benchmark:** TeleAI-Safety

## Links

- **arXiv:** https://arxiv.org/abs/2512.05485

## Abstract


While the deployment of large language models (LLMs) in high-value industries continues to expand, the systematic assessment of their safety against jailbreak and promptbased attacks remains insufficient. Existing safety evaluation benchmarks and frameworks are often limited by an imbalanced integration of core components (attack, defense, and evaluation methods) and an isolation between flexible evaluation frameworks and standardized benchmarking capabilities. These limitations hinder reliable cross-study comparisons and create unnecessary overhead for comprehensive risk assessment. To address these gaps, we present TeleAI-Safety, a modular and reproducible framework coupled with a systematic benchmark for rigorous LLM safety evaluation. Our framework integrates a broad collection of 19 attack methods (including one self-developed method), 29 defense methods, and 19 evaluation methods (including one self-developed method). With a curated attack corpus of 342 samples spanning 12 distinct risk categories, the TeleAI-Safety benchmark conducts extensive ∗Correspondence to Xuelong Li(xuelong_li@ieee.org). 1Work done during an internship at TeleAI. 2Equal Contribution. 1 arXiv:2512.05485v2 [cs.CR] 8 Dec 2025 evaluations across 14 target models. The results reveal systematic vulnerabilities and model-specific failure cases, highlighting critical trade-offs between safety and utility, and identifying potential defense patterns for future optimization. In practical scenarios, TeleAI-Safety can be flexibly adjusted with customized attack, defense, and evaluation combinations to meet specific demands. We release our complete code and evaluation results to facilitate reproducible research and establish unified safety baselines. @ TeleAI-Safety Code: https://github.com/yuanyc06/Tele-Safety

## Data Description

TeleAI-Safety includes a self-constructed attack dataset of 342 harmful prompts spanning 12 risk categories, used as a standardized testbed for jailbreak evaluation. The complete code, dataset, and evaluation results are released at the GitHub repository.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** TeleAI-Safety benchmark for Arabic, Multilingual, English; ethics/values focus

## Tags

