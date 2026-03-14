---


































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0151
type: preprint
short_title: "ChineseSafe -- A Chinese Benchmark for Evaluating Safety in LLMs"
year: 2024
first_author: "[[Zhang, Hengxiang]]"
last_author: "[[Yang, Lei]]"
authors: "Zhang, Hengxiang; Gao, Hongfu; Hu, Qiang; Chen, Guanhua; Yang, Lili; Jing, Bingyi; Wei, Hongxin; Wang, Bing; Bai, Haifeng; Yang, Lei"
authors_incomplete: false
url: "https://arxiv.org/abs/2410.18491"
external_pdf: "https://arxiv.org/pdf/2410.18491.pdf"
pdf_extract: "PDF Extracts/2024/2024-Zhang-ChineseSafe - A Chinese Benchmark for Evaluating Safety in LLMs.md"
local_pdf: "[[PDFs/2024/2024-Zhang-ChineseSafe - A Chinese Benchmark for Evaluating Safety in LLMs.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
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
tags: 
abstract: "With the rapid development of Large language models (LLMs), understanding the capabilities of LLMs in identifying unsafe content has become increasingly important. While previous works have introduced several benchmarks to evaluate the safety risk of LLMs, the community still has a limited understanding of current LLMs’ capability to recognize illegal and unsafe content in Chinese contexts. In this work, we present a Chinese safety benchmark (ChineseSafe) to facilitate research on the content..."
LLM_assessed: "DeepSeek, GPT-3.5, GPT-4, GPT-4o, Gemma, Llama-3, Mistral, Qwen-1.5"
DATA_URL: "https://huggingface.co/datasets/SUSTech/ChineseSafe"
CONFERENCE: "Preprint"
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "205,034 examples; 20,000 examples"
---
# ChineseSafe -- A Chinese Benchmark for Evaluating Safety in LLMs

## Authors

[[Zhang, Hengxiang]], [[Gao, Hongfu]], [[Hu, Qiang]], [[Chen, Guanhua]], [[Yang, Lili]], [[Jing, Bingyi]], [[Wei, Hongxin]], [[Wang, Bing]], [[Bai, Haifeng]], [[Yang, Lei]]

## Metadata

**Authors:** Zhang, Hengxiang; Gao, Hongfu; Hu, Qiang; Chen, Guanhua; Yang, Lili; Jing, Bingyi; Wei, Hongxin; Wang, Bing; Bai, Haifeng; Yang, Lei

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2410.18491
- **Code/Data:** https://huggingface.co/papers/2410.18491

## Abstract

With the rapid development of Large language models (LLMs), understanding the capabilities of LLMs in identifying unsafe content has become increasingly important. While previous works have introduced several benchmarks to evaluate the safety risk of LLMs, the community still has a limited understanding of current LLMs’ capability to recognize illegal and unsafe content in Chinese contexts. In this work, we present a Chinese safety benchmark (ChineseSafe) to facilitate research on the content safety of large language models. To align with the regulations for Chinese Internet content moderation, our ChineseSafe contains 205,034 examples across 4 classes and 10 sub-classes of safety issues. For Chinese contexts, we add several special types of illegal content: political sensitivity, pornography, and variant/homophonic words. Moreover, we employ two methods to evaluate the legal risks of popular LLMs, including open-sourced models and APIs. The results reveal that many LLMs exhibit vulnerability to certain types of safety issues, leading to legal risks in China. Our work provides a guideline for developers and researchers to facilitate the safety of LLMs. Our results are also available at https: //huggingface.co/spaces/SUSTech/ChineseSafe-Benchmark. Additionally, we release a test set comprising 20,000 examples, which is publicly accessible at https://huggingface.co/datasets/SUSTech/ChineseSafe. Warning: this paper may contain potentially offensive content.

## Dataset Information

205,034 examples (very large-scale)

## Data Description

ChineseSafe is a Chinese safety benchmark with 205,034 examples across 4 classes and 10 sub-classes aligned with Chinese Internet content moderation regulations, used to evaluate 26 LLMs covering diverse scales and organizations.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

