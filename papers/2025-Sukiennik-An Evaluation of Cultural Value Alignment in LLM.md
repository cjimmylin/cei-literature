---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0023
type: preprint
short_title: "An Evaluation of Cultural Value Alignment in LLM"
year: 2025
first_author: "[[N. Sukiennik]]"
last_author: "[[Y & Li]]"
authors: "N. Sukiennik; Chen Gao; Felix Juefei-Xu; Y & Li"
url: "https://arxiv.org/abs/2504.08863"
external_pdf: "https://arxiv.org/pdf/2504.08863.pdf"
pdf_extract: "PDF Extracts/2025/2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM.md"
local_pdf: "[[PDFs/2025/2025-Sukiennik-An Evaluation of Cultural Value Alignment in LLM.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "LLMs as intelligent agents are being increasingly applied in scenarios where human interactions are involved, leading to a critical concern about whether LLMs are faithful to the variations in culture across regions. Several works have investigated this question in various ways, finding that there are biases present in the cultural representations of LLM outputs. To gain a more comprehensive view, in this work, we conduct the first large-scale evaluation of LLM culture assessing 20 countries’..."
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, Gemini, Llama-3, DeepSeek, ChatGLM, Qwen-2"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# An Evaluation of Cultural Value Alignment in LLM

## Authors

[[N. Sukiennik]], [[Chen Gao]], [[Felix Juefei-Xu]], [[Y & Li]]

## Metadata

**Authors:** Sukiennik, N., Gao, C., Xu, F., & Li, Y

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.08863

## Abstract

LLMs as intelligent agents are being increasingly applied in scenarios where human interactions are involved, leading to a critical concern about whether LLMs are faithful to the variations in culture across regions. Several works have investigated this question in various ways, finding that there are biases present in the cultural representations of LLM outputs. To gain a more comprehensive view, in this work, we conduct the first large-scale evaluation of LLM culture assessing 20 countries’ cultures and languages across ten LLMs. With a renowned cultural values questionnaire and by carefully analyzing LLM output with human ground truth scores, we thoroughly study LLMs’ cultural alignment across countries and among individual models. Our findings show that the output over all models represents a moderate cultural middle ground. Given the overall skew, we propose an alignment metric, revealing that the United States is the best-aligned country and GLM-4 has the best ability to align to cultural values. Deeper investigation sheds light on the influence of model origin, prompt language, and value dimensions on cultural output. Specifically, models, regardless of where they originate, align better with the US than they do with China. The conclusions provide insight to how LLMs can be better aligned to various cultures as well as provoke further discussion of the potential for LLMs to propagate cultural bias and the need for more culturally adaptable models.

## Dataset Information

Format: Validated cultural values questionnaire with human ground truth

## Data Description

The paper evaluates cultural value alignment across 10 LLMs (GPT-3.5-Turbo, GPT-4, GPT-4o, Gemini-1.5, LLaMA-3-70B, DeepSeek-v2.5, GLM-4, and three Qwen-2.5 variants) using Hofstede's Values Survey Module (VSM), a 24-item questionnaire covering six cultural dimensions. The evaluation spans 20 countries with their respective languages, with each country-language prompt called three times per model, resulting in 400 prompts per model and totaling approximately 12,000 survey completions.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** HIGH

## Tags

