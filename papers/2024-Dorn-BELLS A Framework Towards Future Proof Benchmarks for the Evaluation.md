---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0145
type: conferencePaper
short_title: "BELLS: A Framework Towards Future Proof Benchmarks for the Evaluation of LLM Safeguards"
year: 2024
first_author: "[[Diego Dorn]]"
last_author: "[[Vincent Corruble]]"
authors: "Diego Dorn; Alexandre Variengien; Charbel-Raphaël Segerie; Vincent Corruble"
url: "https://arxiv.org/abs/2406.01364"
external_pdf: "https://arxiv.org/pdf/2406.01364.pdf"
pdf_extract: "PDF Extracts/2024/2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation.md"
local_pdf: "[[PDFs/2024/2024-Dorn-BELLS A Framework Towards Future Proof Benchmarks for the Evaluation.pdf]]"
publication: "ICML 2024"
CONF-CC: "ICML 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Input-output safeguards are used to detect anomalies in the traces produced by Large Language Models (LLMs) systems. These detectors are at the core of diverse safety-critical applications such as real-time monitoring, offline evaluation of traces, and content moderation. However, there is no widely recognized methodology to evaluate them. To fill this gap, we introduce the Benchmarks for the Evaluation of LLM Safeguards (BELLS), a structured collection of tests, organized in three categories:..."
LLM_assessed: GPT-4
DATA_URL: "https://github.com/CentreSecuriteIA/BELLS"
CONFERENCE: "ICML 2024"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset for conversational ai"
data_metrics: "Not specified"
---
# BELLS: A Framework Towards Future Proof Benchmarks for the Evaluation of LLM Safeguards

## Authors

[[Diego Dorn]], [[Alexandre Variengien]], [[Charbel-Raphaël Segerie]], [[Vincent Corruble]]

## Metadata

**Authors:** Diego Dorn; Alexandre Variengien; Charbel-Raphaël Segerie; Vincent Corruble

**Year:** 2024

**Type:** conferencePaper

**Venue:** ICML 2024

## Links

- **arXiv:** https://arxiv.org/abs/2406.01364
- **Code/Data:** https://github.com/CentreSecuriteIA/BELLS

## Abstract

Input-output safeguards are used to detect anomalies in the traces produced by Large Language Models (LLMs) systems. These detectors are at the core of diverse safety-critical applications such as real-time monitoring, offline evaluation of traces, and content moderation. However, there is no widely recognized methodology to evaluate them. To fill this gap, we introduce the Benchmarks for the Evaluation of LLM Safeguards (BELLS), a structured collection of tests, organized in three categories: (1) established failure tests, based on already-existing benchmarks for well-defined failure modes, aiming to compare the performance of current input-output safeguards; (2) emerging failure tests, to measure generalization to never-seen-before failure modes and encourage the development of more general safeguards; (3) next-gen architecture tests, for more complex scaffolding (such as LLM-agents and multi-agent systems), aiming to foster the development of safeguards that could adapt to future applications for which no safeguard currently exists. Furthermore, we implement and share the first next-gen architecture test, using the MACHIAVELLI environment, along with an interactive visualization of the dataset. 1. Context Developers of LLM-based applications compete for innovation and create products of ever-increasing complexity and reach. While applications such as ChatGPT, Microsoft Copilot, or agents such as Devin and AutoGPT become more capable and are more integrated with other systems, the number of ways those systems can fail increases, and new failure modes are discovered after every release of a *Equal contribution 1 ´Ecole Polytechnique F´ed´erale de Lausanne, Lausanne, Switzerland 2Centre pour la S´ecurit´e de l’IA (CeSIA), Paris, France 3Sorbonne Universit´e, CNRS, LIP6, Paris, France. Correspondence to: Diego Dorn <diego@securite-ia.fr>. System Complexity Range of Failure Types Detected Unknown Types Multiple Types Single Type Chat Agents Empty... LlamaGuard Lakera LLM App Multi-agent Text Generation 1 2 3 Figure 1. The landscape of input-output safeguards systems. We show two neglected axes of generality across the complexity of systems supervised (safeguard inputs) and across the range of failure types detected (safeguard outputs). new product. Previously observed failure modes include harmful model behaviour, such as Bing Chat threatening users (Vincent, 2023) and trying to manipulate them during normal conversation; lack of robustness to attacks such as universal adversarial attacks (Zou et al., 2023), which are specific strings that can generate objectionable behavior that generalizes across models and prompts; indirect prompt injection (Greshake et al., 2023), where attackers take control of an LLM through the output of tools. There can also be unforeseen technical bugs, such as ChatGPT glitch tokens (Rumbelow & Watkins, 2023) which are tokens that ChatGPT could not repeat and made it produce incoherent responses or insult the user. Such fa...

## Dataset Information

See report

## Data Description

BELLS is a structured benchmark framework for evaluating LLM input-output safeguards, including 200 agent traces from the MACHIAVELLI environment with 33.6K API calls for detecting ethical vs. unethical agent behavior.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8
**Implementation Readiness:** HIGH

## Tags

