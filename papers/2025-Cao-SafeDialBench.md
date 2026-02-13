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
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Proposed SafeDialBench, a fine-grained benchmark for evaluating LLM safety in multi-turn dialogues against 7 distinct jailbreak attack strategies."
significance: "moves beyond single-turn safety evaluation, assessing a model's ability to maintain safety consistency over prolonged interactions where context and adversarial pressure accumulate."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2025/2025-Cao-SafeDialBench.md"
abstract: "With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogues or a single jailbreak at- tack method to assess the safety. Additionally, these benchmarks have not taken into account the LLM’s capability to identify and handle unsafe information in detail. To address these issues, we propose a fine-grained benchmark SafeDialBench for evaluating the safety of"
paper_summary: "Abstract: With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogu | Overview: SafeDialBench: A Fine-Grained Safety Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks Hongye Cao *1, Yanming Wang *1, Sijia Jing *1, Ziyue Peng *1, Zhixin Bai | Key Findings: scope. First, they often rely on a single jailbreak attack strategy for dataset construction. Second, they focus narrowly on censoring aggressive lan- | Conclusions: This paper presents a comprehensive and fine- grained benchmark for evaluating LLMs safety in multi-turn dialogues, incorporating diverse jail- break"
local_pdf: "[[PDFs/2025/2025-Cao-SafeDialBench.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety dataset for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama-3, Mistral, Qwen, DeepSeek"
DATA_URL: "https://github.com/drivetosouth/SafeDialBench-Dataset"
---
# SafeDialBench: A Fine-Grained Safety Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks

## Metadata

**Authors:** Cao, Hongye; Wang, Yanming; Jing, Sijia; Peng, Ziyue; Bai, Zhixin; Cao, Zhe; Fang, Meng; Feng, Fan; Wang, Boyan; Liu, Jiaheng; Yang, Tianpei; Huo, Jing; Gao, Yang; Meng, Fanyu; Yang, Xi; Deng, Chao; Feng, Junlan

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Cao-SafeDialBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2502.11090

## Abstract

With the rapid advancement of Large Language Models (LLMs), the safety of LLMs has been a critical concern requiring precise assessment. Current benchmarks primarily concentrate on single-turn dialogues or a single jailbreak attack method to assess the safety. Additionally, these benchmarks have not taken into account the LLM's capability of identifying and handling unsafe information in detail. To address these issues, we propose a fine-grained benchmark SafeDialBench for evaluating the safety of LLMs across various jailbreak attacks in multi-turn dialogues. Specifically, we design a two-tier hierarchical safety taxonomy that considers 6 safety dimensions and generates more than 4000 multi-turn dialogues in both Chinese and English under 22 dialogue scenarios. We employ 7 jailbreak attack strategies, such as reference attack and purpose reverse, to enhance the dataset quality for dialogue generation. Notably, we construct an innovative assessment framework of LLMs, measuring capabilities in detecting, and handling unsafe information and maintaining consistency when facing jailbreak attacks. Experimental results across 17 LLMs reveal that Yi-34B-Chat and GLM4-9B-Chat demonstrate superior safety performance, while Llama3.1-8B-Instruct and o3-mini exhibit safety vulnerabilities.

## Authors

[[Hongye Cao]], [[Yanming Wang]], [[Shuangchen Jing|Sijia Jing]], [[Ziyue Peng]], [[Zeyu Bai|Zhixin Bai]], [[Zhicheng Cao|Zhe Cao]], [[Ming Fang|Meng Fang]], [[Fan Feng]], [[Boyan Wang]], [[Jiaheng Liu]], [[Tianpei Yang]], [[Jing Huo]], [[Yang Gao]], [[Fandong Meng|Fanyu Meng]], [[Xi Yang]], [[Chao Deng]], [[Jiashi Feng|Junlan Feng]]

## Data Description

SafeDialBench is a fine-grained safety benchmark evaluating LLMs in multi-turn dialogues under diverse jailbreak attacks. It comprises 4,053 dialogues in both Chinese and English across 22 scenarios and 6 safety dimensions, with 7 jailbreak attack strategies. The benchmark evaluates 17 LLMs (3 closed-source: ChatGPT-4o, o3-mini, MoonShot-v1; 14 open-source including Llama3.1-8B-Instruct, Mistral-7B-Instruct, Qwen variants, DeepSeek-7B-Chat, Yi, Baichuan2, ChatGLM, InternLM2) on three safety abilities: identifying unsafe risks, handling unsafe information, and maintaining consistency.


## Notes


## Citation Info

43 citations (Semantic Scholar/arXiv) [2025-08-27]
