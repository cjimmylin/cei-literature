---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: GWVP7WKG
type: conferencePaper
short_title: tSMC
year: 2025
first_author: "[[Ziyi Zhou]]"
last_author: "[[Wei, Xuetao]]"
authors: "[[Zhou, Ziyi]]; [[Guo, Xinwei]]; [[Gao, Jiashi]]; [[Zhao, Xiangyu]]; [[Zhang, Shiyao]]; [[Yao, Xin]]; [[Wei, Xuetao]]"
url: "https://proceedings.neurips.cc/paper_files/paper/2024/hash/48726631f87322012c6be38e00c72a47-Abstract-Conference.html"
external_pdf: "file:///Users/jimmylin/Zotero/storage/MWSLHSCV/2024 - tSMC A Toolbox for Safety-Aware Multi-Agent Reinforcement Learning.pdf"
pdf_extract: "PDF Extracts/2024/2024-Zhou-tSMC.md"
local_pdf: [[PDFs/2024/2024-Zhou-tSMC.pdf]]
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Developed the tSMC framework to evaluate and mitigate position and selection biases in LLM moral consistency evaluations, allowing for a more accurate assessment of 'Intrinsic Symmetric Moral Consistency'."
significance: "Reveals that perceived moral inconsistencies in LLMs are often artifacts of measurement bias (position/selection) rather than intrinsic moral failure, providing a more robust methodology for evaluating whether LLMs actually 'understand' moral scenarios."
tags: 
abstract: "Large Language Models (LLMs) have demonstrated remarkable capabilities, surpassing human experts in various benchmark tests and playing a vital role in various industry sectors. Despite their effectiveness, a notable drawback of LLMs is their inconsistent moral behavior, which raises ethical concerns. This work delves into symmetric moral consistency in large language models and demonstrates that modern LLMs lack sufficient consistency ability in moral scenarios. Our extensive investigation of twelve popular LLMs reveals that their assessed consistency scores are influenced by position bias and selection bias rather than their intrinsic abilities. We propose a new framework tSMC, which gauges the effects of these biases and effectively mitigates the bias impact based on the Kullback–Leibler divergence to pinpoint LLMs' mitigated Symmetric Moral Consistency. We find that the ability of LLMs to maintain consistency varies across different moral scenarios. Specifically, LLMs show more consistency in scenarios with clear moral answers compared to those where no choice is morally perfect. The average consistency score of 12 LLMs ranges from 60.7% in high-ambiguity moral scenarios to 84.8% in low-ambiguity moral scenarios."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, Gemini, Llama-2, Llama-3, Mistral, Mixtral, Gemma, Phi"
DATA_URL: "https://huggingface.co/google/gemma-2b-it"
---
# Unveiling the Bias Impact on Symmetric Moral Consistency of Large Language Models

## Authors

[[Ziyi Zhou|Zhou, Ziyi]], [[Xinwei Guo|Guo, Xinwei]], [[Jiashi Gao|Gao, Jiashi]], [[Xiangyu Zhao|Zhao, Xiangyu]], [[Shiyao Zhang|Zhang, Shiyao]], [[Xin Yao|Yao, Xin]], [[Xuetao Wei|Wei, Xuetao]]

## Links

- **URL:** https://proceedings.neurips.cc/paper_files/paper/2024/hash/48726631f87322012c6be38e00c72a47-Abstract-Conference.html

## Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities, surpassing human experts in various benchmark tests and playing a vital role in various industry sectors. Despite their effectiveness, a notable drawback of LLMs is their inconsistent moral behavior, which raises ethical concerns. This work delves into symmetric moral consistency in large language models and demonstrates that modern LLMs lack sufficient consistency ability in moral scenarios. Our extensive investigation of twelve popular LLMs reveals that their assessed consistency scores are influenced by position bias and selection bias rather than their intrinsic abilities. We propose a new framework tSMC, which gauges the effects of these biases and effectively mitigates the bias impact based on the Kullback–Leibler divergence to pinpoint LLMs' mitigated Symmetric Moral Consistency. We find that the ability of LLMs to maintain consistency varies across different moral scenarios. Specifically, LLMs show more consistency in scenarios with clear moral answers compared to those where no choice is morally perfect. The average consistency score of 12 LLMs ranges from 60.7% in high-ambiguity moral scenarios to 84.8% in low-ambiguity moral scenarios.

## Data Description

The paper evaluates symmetric moral consistency across 12 LLMs (Phi-2, Gemma-2b/7b, Llama-2-7b/13b/70b, Llama-3-8b/70b, Mistral-7B, Mixtral-8x7B, GPT-3.5-turbo, and Gemini-1.0-pro) using the MoralChoice dataset containing 680 high-ambiguity and 687 low-ambiguity moral scenario questions. The tSMC framework measures consistency after mitigating position bias and selection bias via Kullback-Leibler divergence.


## Notes

