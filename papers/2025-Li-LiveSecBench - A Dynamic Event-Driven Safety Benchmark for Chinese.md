---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0077
type: preprint
short_title: "LiveSecBench -- A Dynamic Event-Driven Safety Benchmark for Chinese LLMs"
year: 2025
first_author: "[[Li, Yudong]]"
last_author: "[[Huang, Yongfeng]]"
authors: "[[Li, Yudong]]; [[Yang, Peiru]]; [[Huang, Feng]]; [[Yang, Zhongliang]]; [[Wang, Kecheng]]; [[Li, Haitian]]; [[Chen, Baocheng]]; [[An, Xingyu]]; [[Liu, Ziyu]]; [[Yang, Youdan]]; [[Chen, Kejiang]]; [[Wan, Sifang]]; [[Wang, Xu]]; [[Sun, Yufei]]; [[Wu, Liyan]]; [[Zhou, Ruiqi]]; [[Wen, Wenya]]; [[Gu, Xingchi]]; [[Zhang, Tianxin]]; [[Gao, Yue]]; [[Huang, Yongfeng]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2511.02366"
external_pdf: "https://arxiv.org/pdf/2511.02366.pdf"
pdf_extract: "PDF Extracts/2025/2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese.md"
local_pdf: "[[PDFs/2025/2025-Li-LiveSecBench - A Dynamic Event-Driven Safety Benchmark for Chinese.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "We introduce LiveSecBench, a continuously updated safety benchmark specifically for Chinese-language LLM application scenarios. LiveSecBench constructs a high-quality and unique dataset through a pipeline that combines automated generation with human verification. By periodically releasing new versions to expand the dataset and update evaluation metrics, LiveSecBench provides a robust and up-to-date standard for AI safety."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-5, GPT-4o, Claude, Qwen, Llama-3, Gemini, DeepSeek, Grok"
DATA_URL: "https://livesecbench.intokentech.cn/"
---
# LiveSecBench -- A Dynamic Event-Driven Safety Benchmark for Chinese LLMs

## Authors

[[Li, Yudong]], [[Yang, Peiru]], [[Huang, Feng]], [[Yang, Zhongliang]], [[Wang, Kecheng]], [[Li, Haitian]], [[Chen, Baocheng]], [[An, Xingyu]], [[Liu, Ziyu]], [[Yang, Youdan]], [[Chen, Kejiang]], [[Wan, Sifang]], [[Wang, Xu]], [[Sun, Yufei]], [[Wu, Liyan]], [[Zhou, Ruiqi]], [[Wen, Wenya]], [[Gu, Xingchi]], [[Zhang, Tianxin]], [[Gao, Yue]], [[Huang, Yongfeng]]

## Metadata

**Authors:** Li, Yudong; Yang, Peiru; Huang, Feng; Yang, Zhongliang; Wang, Kecheng; Li, Haitian; Chen, Baocheng; An, Xingyu; Liu, Ziyu; Yang, Youdan; Chen, Kejiang; Wan, Sifang; Wang, Xu; Sun, Yufei; Wu, Liyan; Zhou, Ruiqi; Wen, Wenya; Gu, Xingchi; Zhang, Tianxin; Gao, Yue; Huang, Yongfeng

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2511.02366

## Abstract

We introduce LiveSecBench, a continuously updated safety benchmark specifically for Chinese-language LLM application scenarios. LiveSecBench constructs a high-quality and unique dataset through a pipeline that combines automated generation with human verification. By periodically releasing new versions to expand the dataset and update evaluation metrics, LiveSecBench provides a robust and up-to-date standard for AI safety. In this report, we introduce our second release v251215, which evaluates across five dimensions (Public Safety, Fairness&Bias, Privacy, Truthfulness, and Mental Health Safety.) We evaluate 57 representative LLMs using an ELO rating system, offering a leaderboard of the current state of Chinese LLM safety. The result is available at https://livesecbench.intokentech.cn/.

## Dataset Information

Dynamic, continuously updated (latest version v251215)

## Data Description

LiveSecBench is a continuously updated safety benchmark for Chinese-language LLM applications, evaluating across five dimensions: Public Safety, Fairness & Bias, Privacy, Truthfulness, and Mental Health Safety. The dataset is constructed via a pipeline combining automated adversarial prompt generation with human verification, using strategies including wrapping, injection, and obfuscation. Fifty-seven representative LLMs were evaluated using an ELO rating system with Swiss-system tournament pairing, with DeepSeek-V3.2 serving as the judge model.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

