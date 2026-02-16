---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KHHKT4GV
type: journalArticle
short_title: HarmBench
year: 2024
first_author: "[[Mantas Mazeika]]"
last_author: "[[Dan Hendrycks]]"
authors: "Mantas Mazeika; Long Phan; Xuwang Yin; Andy Zou; Zifan Wang; Norman Mu; Elham Sakhaee; Nathaniel Li; Steven Basart; Bo Li; David Forsyth; Dan Hendrycks"
url: "https://arxiv.org/abs/2402.04249"
external_pdf: "https://arxiv.org/pdf/2402.04249.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2024/2024-Mazeika-HarmBench.md"
abstract: "Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these..."
paper_summary: "Abstract: Automated red teaming holds substantial promise for uncovering and mitigating the risks associ- ated with the malicious use of large language models (LLMs), yet the field lacks a standard- ized evalua | Overview: HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal Mantas Mazeika 1 Long Phan 2 Xuwang Yin 2 Andy Zou 3 2 Zifan Wang 2 Norman Mu 4 Elham Sakhaee 5 Nathaniel Li | Methodology: is no longer automated. Besides Mazeika et al. (2023), no prior automated red teaming evaluation has a canonical split of held-out behaviors. The vali | Key Findings: framework for automated red teaming. We iden- tify several desirable properties previously unac- counted for in red teaming evaluations and sys- temat | Conclusions: We introduced HarmBench, a standardized evaluation frame- work for automated red teaming. We described desirable properties of a red teaming evaluatio"
local_pdf: "[[PDFs/2024/2024-Mazeika-HarmBench.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, Claude, Gemini, Llama-2, Vicuna, Mistral, Mixtral"
DATA_URL: "https://github.com/centerforaisafety/HarmBench"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

## Metadata

**Authors:** Mazeika, M.

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Mazeika-HarmBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2402.04249

## Abstract

Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these criteria. Using HarmBench, we conduct a large-scale comparison of 18 red teaming methods and 33 target LLMs and defenses, yielding novel insights. We also introduce a highly efficient adversarial training method that greatly enhances LLM robustness across a wide range of attacks, demonstrating how HarmBench enables codevelopment of attacks and defenses. We open source HarmBench at https://github.com/centerforaisafety/HarmBench.

## Authors

[[Mantas Mazeika]], [[Long Phan]], [[Xuwang Yin]], [[Andy Zou]], [[Zifan Wang]], [[Norman Mu]], [[Elham Sakhaee]], [[Nathaniel Li]], [[Steven Basart]], [[Bo Li]], [[David Forsyth]], [[Dan Hendrycks]]

## Data Description

HarmBench is a standardized evaluation framework for automated red teaming and robust refusal, containing 510 unique harmful behaviors across four functional categories (standard, copyright, contextual, and multimodal) and seven semantic categories. The benchmark includes a large-scale comparison of 18 red teaming attack methods against 33 target LLMs and defenses, including Llama 2 (7B, 13B, 70B), Vicuna (7B, 13B), Mistral 7B, Mixtral 8x7B, GPT-3.5 Turbo, GPT-4, Claude (1, 2, 2.1), and Gemini Pro.


## Notes


## Citation Info

495 citations (Semantic Scholar/arXiv) [2025-08-27]
