---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0038
type: preprint
short_title: "DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios"
year: 2025
first_author: "[[Yao Huang]]"
last_author: "[[Xingxing Wei]]"
authors: "Yao Huang; Yitong Sun; Yichi Zhang; Ruochen Zhang; Yinpeng Dong; Xingxing Wei"
url: "https://arxiv.org/abs/2510.15501"
external_pdf: "https://arxiv.org/pdf/2510.15501.pdf"
pdf_extract: "PDF Extracts/2025/2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors.md"
local_pdf: "[[PDFs/2025/2025-Huang-DeceptionBench A Comprehensive Benchmark for AI Deception Behaviors.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
abstract: "Despite the remarkable advances of Large Language Models (LLMs) across diverse cognitive tasks, the rapid enhancement of these capabilities also introduces emergent deception behaviors that may induce severe risks in high-stakes deployments. More critically, the characterization of deception across realistic real-world scenarios remains underexplored. To bridge this gap, we establish DeceptionBench, the first benchmark that systematically evaluates how deceptive tendencies manifest across..."
LLM_assessed: "Claude, DeepSeek, GPT-3.5, GPT-4o, Gemini, Grok, Qwen, Qwen-2"
DATA_URL: "https://github.com/Aries-iai/DeceptionBench"
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark"
data_metrics: "1,000 samples; over 1,000 samples"
---
# DeceptionBench: A Comprehensive Benchmark for AI Deception Behaviors in Real-world Scenarios

## Authors

[[Yao Huang]], [[Yitong Sun]], [[Yichi Zhang]], [[Ruochen Zhang]], [[Yinpeng Dong]], [[Xingxing Wei]]

## Metadata

**Authors:** Yao Huang; Yitong Sun; Yichi Zhang; Ruochen Zhang; Yinpeng Dong; Xingxing Wei

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2510.15501
- **Code/Data:** https://github.com/Aries-iai/DeceptionBench; https://huggingface.co/datasets/PKU-Alignment/DeceptionBench

## Abstract

Despite the remarkable advances of Large Language Models (LLMs) across diverse cognitive tasks, the rapid enhancement of these capabilities also introduces emergent deception behaviors that may induce severe risks in high-stakes deployments. More critically, the characterization of deception across realistic real-world scenarios remains underexplored. To bridge this gap, we establish DeceptionBench, the first benchmark that systematically evaluates how deceptive tendencies manifest across different societal domains, what their intrinsic behavioral patterns are, and how extrinsic factors affect them. Specifically, on the static count, the benchmark encompasses 150 meticulously designed scenarios in five domains, i.e., Economy, Healthcare, Education, Social Interaction, and Entertainment, with over 1,000 samples, providing sufficient empirical foundations for deception analysis. On the intrinsic dimension, we explore whether models exhibit self-interested egoistic tendencies or sycophantic behaviors that prioritize user appeasement. On the extrinsic dimension, we investigate how contextual factors modulate deceptive outputs under neutral conditions, reward-based incentivization, and coercive pressures. Moreover, we incorporate sustained multi-turn interaction loops to construct a more realistic simulation of real-world feedback dynamics. Extensive experiments across LLMs and Large Reasoning Models (LRMs) reveal critical vulnerabilities, particularly amplified deception under reinforcement dynamics, demonstrating that current models lack robust resistance to manipulative contextual cues and the urgent need for advanced safeguards against various deception behaviors. Code and resources are publicly available at https://github.com/Aries-iai/DeceptionBench.

## Dataset Information

150 scenarios with 1,000+ evaluation samples across 5 domains; single-turn and multi-turn interactions; thought + response evaluation

## Data Description

DeceptionBench provides 150 deception scenarios across 5 domains (Economy, Healthcare, Education, Social Interaction, Entertainment) with 1,000+ evaluation samples including multi-turn variants. The dataset is publicly available along with code.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

