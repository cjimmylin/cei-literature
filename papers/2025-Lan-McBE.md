---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: RNDCEFC4
type: journalArticle
year: 2025
short_title: McBE
first_author: "[[Tian Lan]]"
last_author: "[[Guanglai Gao]]"
authors: "Tian Lan; Xiangdong Su; Xu Liu; Ruirui Wang; Ke Chang; Jiang Li; Guanglai Gao"
url: "https://aclanthology.org/2025.findings-acl.313/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/MNNLABM6/Lan et al. - McBE A Multi-task Chinese Bias Evaluation Benchmark for Large Language Models.pdf"
national_ethnic_cultural: "Chinese, American"
cultures_nationalities_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, American, Bias & Fairness"
key_contribution: "Created 'McBE' (Multi-task Chinese Bias Evaluation), a large benchmark (4k instances) for bias in *Chinese* LLMs across 12 categories, addressing the lack of non-Western bias datasets."
significance: "Highlights that 'Western bias' metrics don't map to Chinese culture (e.g., regional discrimination in China vs racial discrimination in US), requiring culturally specific bias benchmarks."
tags: 
abstract: ". Warning: This paper contains content that may be offensive or harmful As large language models (LLMs) are increasingly applied to various NLP tasks, their inherent biases are gradually disclosed. Therefore, measuring biases in LLMs is crucial to mitigate its ethical risks. However, most existing bias evaluation datasets are focus on English and North American culture, and their bias categories are not fully applicable to other cultures."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multi-task benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
LLM_assessed: "Qwen, Llama-2, Mistral, ChatGPT"
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Lan-McBE.md"
local_pdf: [[PDFs/2025/2025-Lan-McBE.pdf]]
---
# McBE: A Multi-task Chinese Bias Evaluation Benchmark for Large Language Models

## Metadata

**Authors:** Lan, Tian; Su, Xiangdong; Liu, Xu; Wang, Ruirui; Chang, Ke; Li, Jiang; Gao, Guanglai

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2507.02088
- **Acl:** https://aclanthology.org/2025.findings-acl.313/

## Abstract

As large language models (LLMs) are increasingly applied to various NLP tasks, their inherent biases are gradually disclosed. Therefore, measuring biases in LLMs is crucial to mitigate its ethical risks. However, most existing bias evaluation datasets are focus on English andNorth American culture, and their bias categories are not fully applicable to other cultures. The datasets grounded in the Chinese language and culture are scarce. More importantly, these datasets usually only support single evaluation task and cannot evaluate the bias from multiple aspects in LLMs. To address these issues, we present a Multi-task Chinese Bias Evaluation Benchmark (McBE) that includes 4,077 bias evaluation instances, covering 12 single bias categories, 82 subcategories and introducing 5 evaluation tasks, providing extensive category coverage, content diversity, and measuring comprehensiveness. Additionally, we evaluate several popular LLMs from different series and with parameter sizes. In general, all these LLMs demonstrated varying degrees of bias. We conduct an in-depth analysis of results, offering novel insights into bias in LLMs.

## Authors

[[Tian Lan]], [[Xiangdong Su]], [[Xu Liu]], [[Ruirui Wang]], [[Ke Chang]], [[Jiang Li]], [[Guanglai Gao]]

## Data Description

The paper introduces McBE (Multi-task Chinese Bias Evaluation Benchmark), comprising 4,077 bias evaluation instances covering 12 single bias categories (gender, religion, nationality, socioeconomic status, age, appearance, health, region, LGBTQ+, worldview, subculture, race) and 82 subcategories. The benchmark includes five evaluation tasks: preference computation, subcategory classification, scenario selection, bias analysis, and bias scoring. Multiple Chinese and multilingual LLMs were evaluated including Qwen2.5 series (0.5B to 32B), InternLM2.5-7B, Baichuan2-7B, GLM4-AIR, GLM4-0520, Llama2-7B, and Mistral-7B.


## Notes

