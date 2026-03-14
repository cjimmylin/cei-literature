---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: U64LR39D
type: document
short_title: "Phare: A Safety Probe for Large Language Models"
year: 2025
first_author: "[[Pierre Le Jeune]]"
last_author: "[[Matteo Dora]]"
authors: "Pierre Le Jeune; Benoît Malézieux; Weixuan Xiao; Matteo Dora"
url: "https://arxiv.org/abs/2505.11365"
external_pdf: "https://arxiv.org/pdf/2505.11365.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English, French, Spanish"
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
newtags: "AI Safety & Alignment"
key_contribution: "Introduced Phare, a multilingual safety probe evaluating LLMs on Hallucination, Social Bias, and Harmful Content, finding systematic vulnerabilities like sycophancy."
significance: "A diagnostic tool that moves beyond 'score' ranking to identifying specific *failure modes* (e.g., is the model sycophantic? biased?), essential for targeted debugging."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Le Jeune-Phare A Safety Probe for Large Language Models.md"
abstract: "Ensuring the safety of large language models (LLMs) is critical for responsible deployment, yet existing evaluations often prioritize performance over identifying failure modes. We introduce Phare, a multilingual diagnostic framework to probe and evaluate LLM behavior across three critical dimensions: hallucination and reliability, social biases, and harmful content generation. Our evaluation of 17 state-of-the-art LLMs reveals patterns of systematic vulnerabilities across all safety..."
paper_summary: "Abstract: Ensuring the safety of large language models (LLMs) is critical for responsible deployment, yet existing evaluations often prioritize performance over identifying failure modes. We introduce Phare, a  | Overview: Phare: A Safety Probe for Large Language Models Pierre Le Jeune Giskard AI pierre@giskard.ai Benoît Malézieux Giskard AI benoit@giskard.ai Weixuan Xiao Giskard AI weixuan@giskard.ai Matteo Dora Giskar | Methodology: The high-level structure of our framework is as summarized in Figure 1. The dataset generation pipeline comprises three distinct steps: (1) collection | Key Findings: Figure 1: Phare dataset generation and LLMs evaluation methodology. offer insights for improving model safety. To ensure reproducibility, we provide a"
local_pdf: "[[PDFs/2025/2025-Le Jeune-Phare A Safety Probe for Large Language Models.pdf]]"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "Claude, DeepSeek, GPT-4o, GPT-4o mini, Gemini, Gemma, Grok, LLaMA, Llama-3, Mistral, Qwen"
DATA_URL: "https://huggingface.co/datasets/giskardai/phare, https://github.com/giskard-ai/phare"
CONFERENCE: "Preprint"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: Yes
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Phare: A Safety Probe for Large Language Models

## Metadata

**Authors:** Le Jeune, Pierre; Malézieux, Benoît; Xiao, Weixuan; Dora, Matteo

**Year:** 2025

**Type:** document

## Links

- **Local PDF:** [[PDFs/2025/2025-Le Jeune-Phare A Safety Probe for Large Language Models.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2505.11365

## Abstract

Ensuring the safety of large language models (LLMs) is critical for responsible deployment, yet existing evaluations often prioritize performance over identifying failure modes. We introduce Phare, a multilingual diagnostic framework to probe and evaluate LLM behavior across three critical dimensions: hallucination and reliability, social biases, and harmful content generation. Our evaluation of 17 state-of-the-art LLMs reveals patterns of systematic vulnerabilities across all safety dimensions, including sycophancy, prompt sensitivity, and stereotype reproduction. By highlighting these specific failure modes rather than simply ranking models, Phare provides researchers and practitioners with actionable insights to build more robust, aligned, and trustworthy language systems.

## Authors

[[Pierre Le Jeune]], [[Benoît Malézieux]], [[Weixuan Xiao]], [[Matteo Dora]]

## Data Description

Phare: multilingual (EN/FR/ES) safety diagnostic dataset with three modules — hallucination/reliability (factuality, misinformation, debunking, tool reliability), social biases/stereotypes, and harmful content — publicly released with evaluation code.


## Notes


## Citation Info

12 citations (Semantic Scholar/arXiv) [2025-08-27]
