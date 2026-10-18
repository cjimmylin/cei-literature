---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2RX5Z8PS
type: conferencePaper
short_title: AGENTIF
year: 2025
first_author: "[[Yunjia Qi]]"
last_author: "[[Juanzi Li]]"
authors: "Yunjia Qi; Hao Peng; Xiaozhi Wang; Amy Xin; Youfeng Liu; Bin Xu; Lei Hou; Juanzi Li"
doi: 10.48550/arXiv.2505.16944
url: "http://arxiv.org/abs/2505.16944"
external_pdf: "http://arxiv.org/pdf/2505.16944.pdf"
publication: arXiv.org
CONF-CC: Preprint
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Qi-AGENTIF.md"
abstract: "Large Language Models (LLMs) have demonstrated advanced capabilities in realworld agentic applications. Growing research efforts aim to develop LLM-based agents to address practical demands, introducing a new challenge: agentic scenarios often involve lengthy instructions with complex constraints, such as extended system prompts and detailed tool specifications. While adherence to such instructions is crucial for agentic applications, whether LLMs can reliably follow them remains underexplored."
paper_summary: "Abstract: Large Language Models (LLMs) have demonstrated advanced capabilities in real- world agentic applications. Growing research efforts aim to develop LLM-based agents to address practical demands, introdu | Overview: arXiv:2505.16944v1 [cs.AI] 22 May 2025 AGENTIF: Benchmarking Instruction Following of Large Language Models in Agentic Scenarios Yunjia Qi1∗, Hao Peng1∗, Xiaozhi Wang1, Amy Xin1, Youfeng Liu2, Bin Xu1 | Methodology: Evaluation Generation Evaluation Method Figure 3: The data construction process and evaluation workflow of AGENTIF. The detailed descrip- tions of dif | Key Findings: protocol (§ 3.4). Figure 3 illustrates the dataset construction and evaluation workflow of AGENTIF. 3 --- Page 4 --- STEP1: Instruction Collection STE | Conclusions: topics, prioritize maintaining the time-boxed structure."
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
local_pdf: "[[Lit-WS-PDFs/2025/2025-Qi-AGENTIF.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Claude-3, DeepSeek, GPT-4o, Llama-3, Mistral, Qwen, o1"
DATA_URL: "https://github.com/THU-KEG/AgentIF"
CONFERENCE: "Other Conference"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: Benchmark
data_metrics: "723 words; 630 words"
---
# AGENTIF: Benchmarking Instruction Following of Large Language Models in Agentic Scenarios

## Metadata

**Authors:** Qi, Yunjia; Peng, Hao; Wang, Xiaozhi; Xin, Amy; Liu, Youfeng; Xu, Bin; Hou, Lei; Li, Juanzi

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.16944](https://doi.org/10.48550/arXiv.2505.16944)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2025/2025-Qi-AGENTIF.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.16944
- **DOI:** https://doi.org/10.48550/arXiv.2505.16944

## Abstract

Large Language Models (LLMs) have demonstrated advanced capabilities in realworld agentic applications. Growing research efforts aim to develop LLM-based agents to address practical demands, introducing a new challenge: agentic scenarios often involve lengthy instructions with complex constraints, such as extended system prompts and detailed tool specifications. While adherence to such instructions is crucial for agentic applications, whether LLMs can reliably follow them remains underexplored. In this paper, we introduce AGENTIF, the first benchmark for systematically evaluating LLM instruction following ability in agentic scenarios. AGENTIF features three key characteristics: (1) Realistic, constructed from 50 real-world agentic applications. (2) Long, averaging 1, 723 words with a maximum of 15, 630 words. (3) Complex, averaging 11.9 constraints per instruction, covering diverse constraint types, such as tool specifications and condition constraints. To construct AGENTIF, we collect 707 human-annotated instructions across 50 agentic tasks from industrial application agents and open-source agentic systems. For each instruction, we annotate the associated constraints and corresponding evaluation metrics, including code-based evaluation, LLM-based evaluation, and hybrid code-LLM evaluation. We use AGENTIF to systematically evaluate existing advanced LLMs. We observe that current models generally perform poorly, especially in handling complex constraint structures and tool specifications. We further conduct error analysis and analytical experiments on instruction length and meta constraints, providing some findings about the failure modes of existing LLMs. We have released the code2 and data3 to facilitate future research.

## Authors

[[Yunjia Qi]], [[Hao Peng]], [[Xiaozhi Wang]], [[Amy Xin]], [[Youfeng Liu]], [[Bin Xu]], [[Lei Hou]], [[Juanzi Li]]

## Data Description

AGENTIF is a benchmark of 707 human-annotated instructions across 50 real-world agentic tasks, averaging 1,723 words per instruction with complex constraints; the dataset is also released on HuggingFace at https://huggingface.co/datasets/THU-KEG/AgentIF.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

3 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23]
