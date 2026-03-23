---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3GWHLCTH
type: document
short_title: "Evaluating Implicit Bias in Large Language Models"
year: 2025
first_author: "[[Yuchen Wen]]"
last_author: "[[Cheng, Xueqi]]"
authors: "Wen, Yuchen; Bi, Keping; Chen, Wei; Guo, Jiafeng; Cheng, Xueqi"
url: "https://aclanthology.org/2025.findings-acl.263/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/FKYPKPUS/2025 - Evaluating Implicit Bias in Large Language Models by Attacking From a Psychometric Perspective.pdf"
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
newtags: "Bias & Fairness"
key_contribution: "Proposed psychometric-inspired attack methods (Disguise, Deception, Teaching) to elicit implicit bias in LLMs, and released two benchmarks (2.7k and 12.7k instances)."
significance: "Shows that standard safety evaluations may miss 'implicit' biases that can be triggered by psychological framing, providing a more rigorous stress-test for model fairness."
tags: 
abstract: "As large language models (LLMs) become an important way of information access, there have been increasing concerns that LLMs may intensify the spread of unethical content, including implicit bias that hurts certain populations without explicit harmful words. In this paper, we conduct a rigorous evaluation of LLMs’ implicit bias towards certain demographics by attacking them from a psychometric perspective to elicit agreements to biased viewpoints."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4, Mistral, Llama-3, Qwen"
DATA_URL: "https://github.com/yuchenwen1/BUMBLE"
pdf_extract: "PDF Extracts/2025/2025-Wen-Evaluating Implicit Bias in Large Language Models.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Wen-Evaluating Implicit Bias in Large Language Models.pdf]]"
CONFERENCE: "ACL 2025"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning text corpus"
data_metrics: "2.7k instances; 12.7k instances"
ethics_perspective: "Bias & Fairness"
---
# Evaluating Implicit Bias in Large Language Models by Attacking From a Psychometric Perspective

## Authors

[[Yuchen Wen|Wen, Yuchen]], [[Keping Bi|Bi, Keping]], [[Wei Chen|Chen, Wei]], [[Jiafeng Guo|Guo, Jiafeng]], [[Cheng, Xueqi]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.findings-acl.263/

## Abstract

As large language models (LLMs) become an important way of information access, there have been increasing concerns that LLMs may intensify the spread of unethical content, including implicit bias that hurts certain populations without explicit harmful words. In this paper, we conduct a rigorous evaluation of LLMs’ implicit bias towards certain demographics by attacking them from a psychometric perspective to elicit agreements to biased viewpoints. Inspired by psychometric principles in cognitive and social psychology, we propose three attack approaches, i.e., Disguise, Deception, and Teaching. Incorporating the corresponding attack instructions, we built two benchmarks: (1) a bilingual dataset with biased statements covering four bias types (2.7K instances) for extensive comparative analysis, and (2) BUMBLE, a larger benchmark spanning nine common bias types (12.7K instances) for comprehensive evaluation. Extensive evaluation of popular commercial and open-source LLMs shows that our methods can elicit LLMs’ inner bias more effectively than competitive baselines. Our attack methodology and benchmarks offer an effective means of assessing the ethical risks of LLMs, driving progress toward greater accountability in their development.

## Data Description

BUMBLE (Bias Understanding and Measurement Benchmark for LLM Evaluation), a large benchmark built from BBQ spanning nine common bias categories with 12.7K items and 10 repeated tests per item. Also includes a bilingual (Chinese-English) bias statement dataset for psychometric-style bias elicitation.


## Notes

