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
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: Jainism
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: Jainism
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
pdf_extract: "PDF Extracts/2024/2024-Mazeika-HarmBench.md"
abstract: "Automated red teaming holds substantial promise for uncovering and mitigating the risks associated with the malicious use of large language models (LLMs), yet the field lacks a standardized evaluation framework to rigorously assess new methods. To address this issue, we introduce HarmBench, a standardized evaluation framework for automated red teaming. We identify several desirable properties previously unaccounted for in red teaming evaluations and systematically design HarmBench to meet these..."
paper_summary: "Abstract: Automated red teaming holds substantial promise for uncovering and mitigating the risks associ- ated with the malicious use of large language models (LLMs), yet the field lacks a standard- ized evalua | Overview: HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal Mantas Mazeika 1 Long Phan 2 Xuwang Yin 2 Andy Zou 3 2 Zifan Wang 2 Norman Mu 4 Elham Sakhaee 5 Nathaniel Li | Methodology: is no longer automated. Besides Mazeika et al. (2023), no prior automated red teaming evaluation has a canonical split of held-out behaviors. The vali | Key Findings: framework for automated red teaming. We iden- tify several desirable properties previously unac- counted for in red teaming evaluations and sys- temat | Conclusions: We introduced HarmBench, a standardized evaluation frame- work for automated red teaming. We described desirable properties of a red teaming evaluatio"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Mazeika-HarmBench.pdf]]"
CONF-CC: "ICML 2024"
DATE_ADDED: 20260208
LLM_assessed: "Claude, Gemini, GPT-3.5, GPT-4, Llama-2, Mistral, Mixtral, Vicuna"
DATA_URL: "https://github.com/centerforaisafety/HarmBench"
CONFERENCE: Journal
helm: incorporated
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "AI Safety & Alignment"
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal

## Metadata

**Authors:** Mazeika, M.

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Mazeika-HarmBench.pdf|Open PDF]]

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
