---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: L9YQ438U
type: conferencePaper
short_title: OpenDeception
year: 2025
first_author: "[[Yichen Wu]]"
last_author: "[[Min Yang]]"
authors: "Yichen Wu; Xudong Pan; Geng Hong; Min Yang"
doi: 10.48550/arXiv.2504.13707
url: "http://arxiv.org/abs/2504.13707"
external_pdf: "http://arxiv.org/pdf/2504.13707.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Introduced OpenDeception, a framework and dataset for evaluating deceptive behaviors in LLM agents through open-ended multi-turn simulations."
significance: "Revealed that mainstream LLMs have a high propensity for deception (>80% intention) when incentivized to achieve a goal, even without explicit instructions to lie."
tags: 
pdf_extract: "PDF Extracts/0000/2025-Wu-OpenDeception.md"
abstract: "As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective oversight. Unlike existing evaluation which uses simulated games or presents limited choices, we introduce OpenDecep- tion, a novel deception evaluation framework with an open-ended scenario dataset. OpenDeception jointly evaluates both the deception intention and capabilities of LLM-based agents by"
paper_summary: "Abstract: As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective o | Overview: OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Simulation Yichen Wu1, Xudong Pan1,2, Geng Hong1, Min Yang1 1Fudan University, 2Shanghai Innovation Institute (SII)  | Methodology: In this study, we use AI agents to simulate user-AI interactions, generating diverse conversational scenarios by varying roles and objectives. By anal | Key Findings: which uses simulated games or presents limited choices, we introduce OpenDecep- tion, a novel deception evaluation framework with an open-ended scenar"
local_pdf: "[[PDFs/2025/2025-Wu-OpenDeception.pdf]]"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-3.5, Llama-3, Qwen"
DATA_URL: "https://anonymous.4open.science/r/OpenDeception-C187/"
DATE_ADDED: 20260207
research_topic: "Other"
---
# OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Interaction Simulation

## Metadata

**Authors:** Wu, Yichen; Pan, Xudong; Hong, Geng; Yang, Min

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2504.13707](https://doi.org/10.48550/arXiv.2504.13707)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Wu-OpenDeception.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2504.13707
- **DOI:** https://doi.org/10.48550/arXiv.2504.13707

## Abstract

As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective oversight. Unlike existing evaluation which uses simulated games or presents limited choices, we introduce OpenDeception, a novel deception evaluation framework with an open-ended scenario dataset. OpenDeception jointly evaluates both the deception intention and capabilities of LLM-based agents by inspecting their internal reasoning process. Specifically, we construct five types of common use cases where LLMs intensively interact with the user, each consisting of ten diverse, concrete scenarios from the real world. To avoid ethical concerns and costs of high-risk deceptive interactions with human testers, we propose to simulate the multi-turn dialogue via agent simulation. Extensive evaluation of eleven mainstream LLMs on OpenDeception highlights the urgent need to address deception risks and security concerns in LLM-based agents: the deception intention ratio across the models exceeds 80%, while the deception success rate surpasses 50%. Furthermore, we observe that LLMs with stronger capabilities do exhibit a higher risk of deception, which calls for more alignment efforts on inhibiting deceptive behaviors.

## Authors

[[Yichen Wu]], [[Xudong Pan]], [[Geng Hong]], [[Min Yang]]

## Data Description

OpenDeception is an AI deception evaluation benchmark comprising 50 real-world-inspired open-ended scenarios across five deception types (telecommunications fraud, product promotion, personal safety, emotional deception, privacy stealing). Each type contains 10 concrete scenarios with defined AI deceiver and user roles. The benchmark evaluates 11 LLMs including GPT-4o, GPT-3.5-turbo, Llama-3.1-8B/70B-Instruct, Qwen2-7B/72B-Instruct, and Qwen2.5-3B/7B/14B/32B/72B-Instruct through agent-based multi-turn dialogue simulations.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

730 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-23]
