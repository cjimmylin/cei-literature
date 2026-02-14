---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: MPD3XLMS
type: journalArticle
short_title: JBB-Behaviours
year: 2025
first_author: "[[Patrick Chao]]"
last_author: "[[Eric Wong]]"
authors: "Patrick Chao; Edoardo Debenedetti; Alexander Robey; Maksym Andriushchenko; Francesco Croce; Vikash Sehwag; Edgar Dobriban; Nicolas Flammarion; George J. Pappas; Florian Tramer; Hamed Hassani; Eric Wong"
url: "https://arxiv.org/abs/2404.01318"
external_pdf: "https://arxiv.org/pdf/2404.01318.pdf"
national_ethnic_cultural: N/A
religious_values: Jainism
religious_values_list: Jainism
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Released JailbreakBench, an open-source benchmark and leaderboard comprising 100 distinct harmful behaviors and a standardized evaluation framework for jailbreak attacks."
significance: "Addresses the lack of reproducibility and standardization in adversarial attack research, providing a common ground for comparing attack success rates and defense robustness."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Chao-JBB-Behaviours.md"
abstract: "Jailbreak attacks cause large language models (LLMs) to generate harmful, un- ethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evalua- tion techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not re- producible, as they withh"
paper_summary: "Abstract: Jailbreak attacks cause large language models (LLMs) to generate harmful, un- ethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current c | Overview: JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models Patrick Chao∗1, Edoardo Debenedetti∗2, Alexander Robey∗1, Maksym Andriushchenko∗3, Francesco Croce3, Vikash Sehwag4, | Key Findings: framework at https://github.com/JailbreakBench/jailbreakbench that includes a clearly defined threat model, system prompts, chat templates, and scor-"
local_pdf: "[[PDFs/2024-Chao-JBB-Behaviours.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Llama-3, Vicuna, Mixtral"
DATA_URL: "https://github.com/JailbreakBench/jailbreakbench"
publication: "NeurIPS 2024"
DATE_ADDED: 20260207
---
# JBB-Behaviours: A Benchmark for Jailbreaking Bounded LLMs

## Metadata

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Chao-JBB-Behaviours.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2404.01318

## Abstract

Jailbreak attacks cause large language models (LLMs) to generate harmful, unethical, or otherwise objectionable content. Evaluating these attacks presents a number of challenges, which the current collection of benchmarks and evaluation techniques do not adequately address. First, there is no clear standard of practice regarding jailbreaking evaluation. Second, existing works compute costs and success rates in incomparable ways. And third, numerous works are not reproducible, as they withhold adversarial prompts, involve closed-source code, or rely on evolving proprietary APIs. To address these challenges, we introduce JailbreakBench, an open-sourced benchmark with the following components: (1) an evolving repository of state-of-the-art adversarial prompts, which we refer to as jailbreak artifacts; (2) a jailbreaking dataset comprising 100 behaviors -- both original and sourced from prior work (Zou et al., 2023; Mazeika et al., 2023, 2024) -- which align with OpenAI's usage policies; (3) a standardized evaluation framework at https://github.com/JailbreakBench/jailbreakbench that includes a clearly defined threat model, system prompts, chat templates, and scoring functions; and (4) a leaderboard at https://jailbreakbench.github.io/ that tracks the performance of attacks and defenses for various LLMs. We have carefully considered the potential ethical implications of releasing this benchmark, and believe that it will be a net positive for the community.

## Authors

[[Patrick Chao]], [[Edoardo Debenedetti]], [[Alexander Robey]], [[Maksym Andriushchenko]], [[Francesco Croce]], [[Vikash Sehwag]], [[Edgar Dobriban]], [[Nicolas Flammarion]], [[George J. Pappas]], [[Florian Tramer]], [[Hamed Hassani]], [[Eric Wong]]

## Data Description

The paper introduces JailbreakBench, an open-sourced jailbreaking benchmark comprising the JBB-Behaviors dataset of 100 distinct misuse behaviors divided into ten categories aligned with OpenAI's usage policies, along with 100 matching benign behaviors. The benchmark includes a repository of jailbreak artifacts, a standardized red-teaming pipeline, and a leaderboard tracking attack and defense performance across multiple LLMs.


## Notes


## Citation Info

171 citations (Semantic Scholar/arXiv) [2025-08-27]
