---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ARXIV_2510_05942
type: preprint
short_title: EvalMORAAL
year: 2025
first_author: "[[Mohammadi]]"
last_author: "[[Ayoub]]"
authors: Mohammadi; Hadi; Giachanou; Anastasia; Bagheri; Ayoub
doi: 10.48550/arXiv.2510.05942
tags: "Computer Science - AI Ethics"
url: "https://arxiv.org/abs/2510.05942"
pdf_extract: "PDF Extracts/2025/2025-Mohammadi-EvalMORAAL.md"
local_pdf: "[[PDFs/2025/2025-Mohammadi-EvalMORAAL.pdf]]"
external_pdf: "https://arxiv.org/pdf/2510.05942.pdf"
publication: arXiv
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Deontology, Cross-Cultural Ethics, LLM Evaluation, Moral Alignment"
key_contribution: "Transparent CoT framework evaluating moral alignment in 20 LLMs using World Values Survey and PEW data"
significance: "Reveals 21-point Western vs non-Western alignment gap; Claude-3-Opus achieves r=0.890 survey correlation"
abstract: "We present EvalMORAAL1, a transparent chain-of-thought (CoT) framework that uses two scoring methods (log-probabilities and direct ratings) plus a model-as-judge peer review to evaluate moral alignment in 20 large language models. We assess models on the World Values Survey (55 countries, 19 topics) and the PEW Global Attitudes Survey (39 countries, 8 topics). With EvalMORAAL, top models align closely with survey responses (Pearson’s 𝑟≈0.90 on WVS)."
DATE_ADDED: 20260208
LLM_assessed: "Claude-3, Command-R, DeepSeek, GPT-3.5, GPT-4, GPT-4o, GPT-4o mini, Gemini, Llama-3, Mistral, PaLM-2, Phi-3, Qwen-2"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# EvalMORAAL: Interpretable Chain-of-Thought and LLM-as-Judge Evaluation for Moral Alignment in Large Language Models

## Authors

[[Mohammadi]], [[Hadi]], [[Giachanou]], [[Anastasia]], [[Bagheri]], [[Ayoub]]

## Links

- **arXiv:** https://arxiv.org/abs/2510.05942
- **PDF:** https://arxiv.org/pdf/2510.05942.pdf

## Abstract

EvalMORAAL is a transparent chain-of-thought (CoT) framework that uses two scoring methods (log-probabilities and direct ratings) plus a model-as-judge peer review to evaluate moral alignment in 20 large language models. The researchers assess models on the World Values Survey (55 countries, 19 topics) and the PEW Global Attitudes Survey (39 countries, 8 topics). The framework adds three parts: (1) two scoring methods for all models to enable fair comparison, (2) a structured chain-of-thought protocol with self-consistency checks, and (3) a model-as-judge peer review that flags 348 conflicts using a data-driven threshold. Key findings include top models aligning closely with survey responses (Pearson's r approximately 0.90 on WVS), but a clear regional difference: Western regions average r=0.82 while non-Western regions average r=0.61 (a 0.21 absolute gap).

## Data Description

EvalMORAAL evaluates 20 large language models on moral alignment using the World Values Survey (55 countries, 19 topics) and the PEW Global Attitudes Survey (39 countries, 8 topics). The framework collects 135,700 chain-of-thought traces and 54,280 dual scores (log-probability and direct rating) across 1,357 country-topic pairs, employing two scoring methods and an LLM-as-judge peer review with 348 detected conflicts.


## Notes

Key finding: Persistent difficulty with violence-related topics (political violence, domestic violence, terrorism) shows struggles with exactly those moral questions requiring greatest cultural sensitivity.

## Tags

#MoralAlignment #LLMEvaluation #CrossCulturalEthics #WorldValuesSurvey

## Citation Info

arXiv:2510.05942 [cs.CL], October 2025
