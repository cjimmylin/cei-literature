---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KJ239R7X
type: document
short_title: BeHonest
year: 2025
first_author: "[[Steffi Chern]]"
last_author: "[[Pengfei Liu]]"
authors: "Steffi Chern; Zhulin Hu; Yuqing Yang; Ethan Chern; Yuan Guo; Jiahe Jin; Binjie Wang; Pengfei Liu"
url: "https://arxiv.org/abs/2406.13261"
external_pdf: "https://arxiv.org/pdf/2406.13261.pdf"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Introduced BeHonest, a benchmark for honesty covering 3 aspects: knowledge boundaries (refusal), deceit avoidance, and consistency."
significance: "Defines 'honesty' operationally for LLMs beyond just 'factuality', including the crucial ability to say 'I don't know' and resisting pressure to lie."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2024/2024-Chern-BeHonest.md"
abstract: "Previous works on Large Language Models (LLMs) have mainly focused on evaluating their helpfulness or harmlessness. However, honesty, another crucial alignment criterion, has received relatively less attention. Dishonest behaviors in LLMs, such as spreading misinformation and defrauding users, present severe risks that intensify as these models approach superintelligent levels. Enhancing honesty in LLMs addresses critical limitations and helps uncover latent capabilities that are not readily exp"
paper_summary: "Abstract: Previous works on Large Language Models (LLMs) have mainly focused on evaluating their helpfulness or harmlessness. However, honesty, another crucial alignment criterion, has received relatively less  | Overview: BEHONEST: Benchmarking Honesty in Large Language Models Steffi Chern2,5∗ Zhulin Hu1,5∗ Yuqing Yang3,5∗ Ethan Chern1,5† Yuan Guo1,5† Jiahe Jin1,5 Binjie Wang3,5 Pengfei Liu1,4,5‡ 1Shanghai Jiao Tong Un | Key Findings: details. To gain a global understanding of the progress made by current LLMs regarding honesty, we evaluate several popular models. These include the  | Conclusions: In this paper, we introduce BEHONEST, the first comprehensive benchmark for as- sessing honesty in LLMs. Our goal is to raise awareness about the capa"
local_pdf: "[[PDFs/2024/2024-Chern-BeHonest.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "10 scenarios"
LLM_assessed: "GPT-4, ChatGPT, Llama-2, Llama-3, Mistral, Qwen"
DATA_URL: "https://github.com/GAIR-NLP/BeHonest"
---
# BeHonest: Benchmarking Honesty in Large Language Models

## Metadata

**Authors:** Chern, Steffi; Hu, Zhulin; Yang, Yuqing; Chern, Ethan; Guo, Yuan; Jin, Jiahe; Wang, Binjie; Liu, Pengfei

**Year:** 2024

**Type:** document

## Links

- **Local PDF:** [[PDFs/2024/2024-Chern-BeHonest.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2406.13261

## Abstract

Previous works on Large Language Models (LLMs) have mainly focused on evaluating their helpfulness or harmlessness. However, honesty, another crucial alignment criterion, has received relatively less attention. Dishonest behaviors in LLMs, such as spreading misinformation and defrauding users, present severe risks that intensify as these models approach superintelligent levels. Enhancing honesty in LLMs addresses critical limitations and helps uncover latent capabilities that are not readily expressed. This underscores the urgent need for reliable methods and benchmarks to effectively ensure and evaluate the honesty of LLMs. In this paper, we introduce BeHonest, a pioneering benchmark specifically designed to assess honesty in LLMs comprehensively. BeHonest evaluates three essential aspects of honesty: awareness of knowledge boundaries, avoidance of deceit, and consistency in responses. Building on this foundation, we designed 10 scenarios to evaluate and analyze 9 popular LLMs on the market, including both closed-source and open-source models from different model families with varied model sizes. Our findings indicate that there is still significant room for improvement in the honesty of LLMs. We encourage the AI community to prioritize honesty alignment in these models, which can harness their full potential to benefit society while preventing them from causing harm through deception or inconsistency. Our benchmark and code can be found at: \url{https://github.com/GAIR-NLP/BeHonest}.

## Authors

[[Steffi Chern]], [[Zhiyuan Hu|Zhulin Hu]], [[Yuqing Yang]], [[Ethan Chern]], [[Yuan Guo]], [[Jing Jin|Jiahe Jin]], [[Binjie Wang]], [[Pengyuan Liu|Pengfei Liu]]

## Data Description

The paper introduces BeHonest, a benchmark for evaluating honesty in LLMs across three aspects: self-knowledge (awareness of knowledge boundaries), non-deceptiveness (avoidance of deceit), and consistency in responses. The benchmark comprises 10 evaluation scenarios using datasets totaling over 19,000 instances drawn from existing sources (SelfAware, UnknownBench, TrustLLM, TruthfulQA, CommonSenseQA, Big-Bench Hard) and synthetically generated data.


## Notes


## Citation Info

7 citations (Semantic Scholar/arXiv) [2025-08-27]
