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
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Ubuntu Philosophy"
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
rv_ubuntu: 50
rv_indigenous: 0
religious_values_list: "Ubuntu Philosophy"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Value Pluralism / Schwartz, AI Safety & Alignment"
key_contribution: "Introduced OpenDeception, a framework and dataset for evaluating deceptive behaviors in LLM agents through open-ended multi-turn simulations."
significance: "Revealed that mainstream LLMs have a high propensity for deception (>80% intention) when incentivized to achieve a goal, even without explicit instructions to lie."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Wu-OpenDeception.md"
abstract: "As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective oversight. Unlike existing evaluation which uses simulated games or presents limited choices, we introduce OpenDecep- tion, a novel deception evaluation framework with an open-ended scenario dataset. OpenDeception jointly evaluates both the deception intention and capabilities of LLM-based agents by"
paper_summary: "Abstract: As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective o | Overview: OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Simulation Yichen Wu1, Xudong Pan1,2, Geng Hong1, Min Yang1 1Fudan University, 2Shanghai Innovation Institute (SII)  | Methodology: In this study, we use AI agents to simulate user-AI interactions, generating diverse conversational scenarios by varying roles and objectives. By anal | Key Findings: which uses simulated games or presents limited choices, we introduce OpenDecep- tion, a novel deception evaluation framework with an open-ended scenar"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Wu-OpenDeception.pdf]]"
LLM_assessed: "GPT-3.5, GPT-4o, Llama-3, Qwen, Qwen-2, DeepSeek"
DATA_URL: "https://anonymous.4open.science/r/OpenDeception-C187/"
DATE_ADDED: 20260207
research_topic: "Other"
CONFERENCE: "Other Conference"
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning dataset for conversational ai"
data_metrics: "Not specified"
---
# OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Interaction Simulation

## Metadata

**Authors:** Wu, Yichen; Pan, Xudong; Hong, Geng; Yang, Min

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2504.13707](https://doi.org/10.48550/arXiv.2504.13707)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2025/2025-Wu-OpenDeception.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2504.13707
- **DOI:** https://doi.org/10.48550/arXiv.2504.13707

## Abstract

As the general capabilities of large language models (LLMs) improve and agent applications become more widespread, the underlying deception risks urgently require systematic evaluation and effective oversight. Unlike existing evaluation which uses simulated games or presents limited choices, we introduce OpenDeception, a novel deception evaluation framework with an open-ended scenario dataset. OpenDeception jointly evaluates both the deception intention and capabilities of LLM-based agents by inspecting their internal reasoning process. Specifically, we construct five types of common use cases where LLMs intensively interact with the user, each consisting of ten diverse, concrete scenarios from the real world. To avoid ethical concerns and costs of high-risk deceptive interactions with human testers, we propose to simulate the multi-turn dialogue via agent simulation. Extensive evaluation of eleven mainstream LLMs on OpenDeception highlights the urgent need to address deception risks and security concerns in LLM-based agents: the deception intention ratio across the models exceeds 80%, while the deception success rate surpasses 50%. Furthermore, we observe that LLMs with stronger capabilities do exhibit a higher risk of deception, which calls for more alignment efforts on inhibiting deceptive behaviors.

## Authors

[[Yichen Wu]], [[Xudong Pan]], [[Geng Hong]], [[Min Yang]]

## Data Description

OpenDeception framework includes a manually constructed seed benchmark of 50 real-world deception scenarios, a supervised fine-tuning dataset (St) with 27k+ samples, and a contrastive learning dataset (Cu) with 61k+ samples for training deception intention and user trust models.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

730 citations (Semantic Scholar/DOI) [2025-08-27] 4 citations (Semantic Scholar/DOI) [2025-08-23]
