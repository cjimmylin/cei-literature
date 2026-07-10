---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2P3AM8KD
type: document
short_title: SafeDialBench
year: 2025
first_author: "[[Hongye Cao]]"
last_author: "[[Junlan Feng]]"
authors: "Hongye Cao; Yanming Wang; Sijia Jing; Ziyue Peng; Zhixin Bai; Zhe Cao; Meng Fang; Fan Feng; Boyan Wang; Jiaheng Liu; Tianpei Yang; Jing Huo; Yang Gao; Fanyu Meng; Xi Yang; Chao Deng; Junlan Feng"
url: "https://arxiv.org/abs/2502.11090"
external_pdf: "https://arxiv.org/pdf/2502.11090.pdf"
national_ethnic_cultural: Chinese
cultures_nationalities_list: Chinese
languages_list: "Chinese, English"
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Proposed SafeDialBench, a fine-grained benchmark for evaluating LLM safety in multi-turn dialogues against 7 distinct jailbreak attack strategies."
significance: "moves beyond single-turn safety evaluation, assessing a model's ability to maintain safety consistency over prolonged interactions where context and adversarial pressure accumulate."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2025/2025-Cao-SafeDialBench.md"
abstract: "With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogues or a single jailbreak attack method to assess the safety. Additionally, these benchmarks have not taken into account the LLM’s capability to identify and handle unsafe information in detail. To address these issues, we propose a fine-grained benchmark SafeDialBench for evaluating the safety of..."
paper_summary: "Abstract: With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogu | Overview: SafeDialBench: A Fine-Grained Safety Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks Hongye Cao *1, Yanming Wang *1, Sijia Jing *1, Ziyue Peng *1, Zhixin Bai | Key Findings: scope. First, they often rely on a single jailbreak attack strategy for dataset construction. Second, they focus narrowly on censoring aggressive lan- | Conclusions: This paper presents a comprehensive and fine- grained benchmark for evaluating LLMs safety in multi-turn dialogues, incorporating diverse jail- break"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2025/2025-Cao-SafeDialBench.pdf]]
CONF-CC: Preprint
DATE_ADDED: 20260208
LLM_assessed: "ChatGLM, DeepSeek, GPT-3.5, GPT-4o, InternLM, Llama-3, Mistral, o3-mini, Qwen"
DATA_URL: "https://github.com/drivetosouth/SafeDialBench-Dataset"
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety dataset for conversational ai"
data_metrics: "Not specified"
---
# SafeDialBench: A Fine-Grained Safety Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks

## Metadata

**Authors:** Cao, Hongye; Wang, Yanming; Jing, Sijia; Peng, Ziyue; Bai, Zhixin; Cao, Zhe; Fang, Meng; Feng, Fan; Wang, Boyan; Liu, Jiaheng; Yang, Tianpei; Huo, Jing; Gao, Yang; Meng, Fanyu; Yang, Xi; Deng, Chao; Feng, Junlan

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Cao-SafeDialBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2502.11090

## Abstract

With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogues or a single jailbreak attack method to assess the safety. Additionally, these benchmarks have not taken into account the LLM's capability of identifying and handling unsafe information in detail. To address these issues, we propose a fine-grained benchmark SafeDialBench for evaluating the safety of LLMs across various jailbreak attacks in multi-turn dialogues. Specifically, we design a two-tier hierarchical safety taxonomy that considers 6 safety dimensions and generates more than 4000 multi-turn dialogues in both Chinese and English under 22 dialogue scenarios. We employ 7 jailbreak attack strategies, such as reference attack and purpose reverse, to enhance the dataset quality for dialogue generation. Notably, we construct an innovative assessment framework of LLMs, measuring capabilities in detecting, and handling unsafe information and maintaining consistency when facing jailbreak attacks. Experimental results across 17 LLMs reveal that Yi-34B-Chat and GLM4-9B-Chat demonstrate superior safety performance, while Llama3.1-8B-Instruct and o3-mini exhibit safety vulnerabilities.

## Authors

[[Hongye Cao]], [[Yanming Wang]], [[Sijia Jing]], [[Ziyue Peng]], [[Zhixin Bai]], [[Zhe Cao]], [[Meng Fang]], [[Fan Feng]], [[Boyan Wang]], [[Jiaheng Liu]], [[Tianpei Yang]], [[Jing Huo]], [[Yang Gao]], [[Fanyu Meng]], [[Xi Yang]], [[Chao Deng]], [[Junlan Feng]]

## Data Description

SafeDialBench is a fine-grained multi-turn dialogue safety benchmark with 4,053 bilingual (Chinese/English) dialogues across 22 scenarios, 6 safety dimensions, and 7 jailbreak attack methods.


## Notes


## Citation Info

43 citations (Semantic Scholar/arXiv) [2025-08-27]
