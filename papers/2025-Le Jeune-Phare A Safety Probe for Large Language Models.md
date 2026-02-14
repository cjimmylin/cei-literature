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
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Introduced Phare, a multilingual safety probe evaluating LLMs on Hallucination, Social Bias, and Harmful Content, finding systematic vulnerabilities like sycophancy."
significance: "A diagnostic tool that moves beyond 'score' ranking to identifying specific *failure modes* (e.g., is the model sycophantic? biased?), essential for targeted debugging."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Le Jeune-Phare A Safety Probe for Large Language Models.md"
abstract: "Ensuring the safety of large language models (LLMs) is critical for responsible deployment, yet existing evaluations often prioritize performance over identifying failure modes. We introduce Phare, a multilingual diagnostic framework to probe and evaluate LLM behavior across three critical dimensions: hallucination and reliability, social biases, and harmful content generation. Our evaluation of 17 state-of-the-art LLMs reveals patterns of systematic vulnerabilities across all safety dimensions,"
paper_summary: "Abstract: Ensuring the safety of large language models (LLMs) is critical for responsible deployment, yet existing evaluations often prioritize performance over identifying failure modes. We introduce Phare, a  | Overview: Phare: A Safety Probe for Large Language Models Pierre Le Jeune Giskard AI pierre@giskard.ai Benoît Malézieux Giskard AI benoit@giskard.ai Weixuan Xiao Giskard AI weixuan@giskard.ai Matteo Dora Giskar | Methodology: The high-level structure of our framework is as summarized in Figure 1. The dataset generation pipeline comprises three distinct steps: (1) collection | Key Findings: Figure 1: Phare dataset generation and LLMs evaluation methodology. offer insights for improving model safety. To ensure reproducibility, we provide a"
local_pdf: "[[PDFs/2025/2025-Le Jeune-Phare A Safety Probe for Large Language Models.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-4o mini, Gemini, Gemma, Claude, Mistral, Llama, Llama-3, Grok, Qwen, DeepSeek"
DATA_URL: "https://huggingface.co/datasets/giskardai/phare, https://github.com/giskard-ai/phare"
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

Phare is a multilingual diagnostic safety benchmark for LLMs covering three dimensions: hallucination and reliability, social biases and stereotypes, and harmful content generation. The dataset spans English, French, and Spanish, with tasks including factuality questions, debunking challenges, tool reliability tests, bias measurement via story generation, and misguidance detection. Seventeen state-of-the-art LLMs were evaluated across these dimensions. The public dataset and evaluation code are openly available.


## Notes


## Citation Info

12 citations (Semantic Scholar/arXiv) [2025-08-27]
