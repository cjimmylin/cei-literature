---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: F7ATVX8K
type: journalArticle
short_title: StrongREJECT
year: 2024
first_author: "[[Alexandra Souly]]"
last_author: "[[Sam Toyer]]"
authors: "Alexandra Souly; Qingyuan Lu; Dillon Bowen; Tu Trinh; Elvis Hsieh; Sana Pandey; Pieter Abbeel; Justin Svegliato; Scott Emmons; Olivia Watkins; Sam Toyer"
url: "https://arxiv.org/abs/2402.10260"
external_pdf: "https://arxiv.org/pdf/2402.10260.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
key_contribution: "Introduced StrongREJECT, a jailbreak benchmark that uses 'strong rejection' (refusal) as the baseline and measures valid jailbreaks more rigorously than previous metrics."
significance: "Corrects the inflation in 'jailbreak success rates' in the literature, showing that many 'successful' attacks actually degrade model capabilities or produce gibberish rather than true harmful content."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Souly-StrongREJECT.md"
abstract: "Most jailbreak papers claim the jailbreaks they propose are highly effective, often boasting near-100% attack success rates. However, it is perhaps more common than not for jailbreak developers to substantially exaggerate the effectiveness of their jailbreaks. We suggest this problem arises because jailbreak researchers lack a standard, high-quality benchmark for evaluating jailbreak performance, leaving researchers to create their own."
paper_summary: "Abstract: Most jailbreak papers claim the jailbreaks they propose are highly effective, often boasting near-100% attack success rates. However, it is perhaps more common than not for jailbreak developers to sub | Overview: A STRONGREJECT for Empty Jailbreaks Alexandra Souly∗ Qingyuan Lu∗ Dillon Bowen∗ Tu Trinh† Elvis Hsieh† Sana Pandey Pieter Abbeel Justin Svegliato Scott Emmons‡ Olivia Watkins‡ Sam Toyer‡ Center for Hu | Methodology: Many automated evaluators use LLMs to score a forbidden prompt-victim model response pair. The LLM can be hosted remotely or on a user's GPU. For exam | Key Findings: 😈 Figure 1: StrongREJECT improves on existing jailbreak benchmarks using prompts that are spe- cific, answerable, and harmful across six categories of | Conclusions: Broader impacts. Research into LLM jailbreaks is useful for understanding the weaknesses of large language models and identifying vulnerabilities that"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Souly-StrongREJECT.pdf]]"
CONF-CC: "NeurIPS 2024"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-4o, GPT-3.5, Llama-2, Llama-3, Gemma, Mixtral"
DATA_URL: "https://strong-reject.readthedocs.io/"
CONFERENCE: "Journal"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# StrongREJECT: A Benchmark for Evaluating the Robustness of LLMs to Rejection Sampling

## Metadata

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Souly-StrongREJECT.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2402.10260

## Abstract

Most jailbreak papers claim the jailbreaks they propose are highly effective, often boasting near-100% attack success rates. However, it is perhaps more common than not for jailbreak developers to substantially exaggerate the effectiveness of their jailbreaks. We suggest this problem arises because jailbreak researchers lack a standard, high-quality benchmark for evaluating jailbreak performance, leaving researchers to create their own. To create a benchmark, researchers must choose a dataset of forbidden prompts to which a victim model will respond, along with an evaluation method that scores the harmfulness of the victim model's responses. We show that existing benchmarks suffer from significant shortcomings and introduce the StrongREJECT benchmark to address these issues. StrongREJECT's dataset contains prompts that victim models must answer with specific, harmful information, while its automated evaluator measures the extent to which a response gives useful information to forbidden prompts. In doing so, the StrongREJECT evaluator achieves state-of-the-art agreement with human judgments of jailbreak effectiveness. Notably, we find that existing evaluation methods significantly overstate jailbreak effectiveness compared to human judgments and the StrongREJECT evaluator. We describe a surprising and novel phenomenon that explains this discrepancy: jailbreaks bypassing a victim model's safety fine-tuning tend to reduce its capabilities. Together, our findings underscore the need for researchers to use a high-quality benchmark, such as StrongREJECT, when developing new jailbreak attacks. We release the StrongREJECT code and data at https://strong-reject.readthedocs.io/en/latest/.

## Authors

[[Alexandra Souly]], [[Qingyuan Lu]], [[Dillon Bowen]], [[Tu Trinh]], [[Elvis Hsieh]], [[Sana Pandey]], [[Pieter Abbeel]], [[Justin Svegliato]], [[Scott Emmons]], [[Olivia Watkins]], [[Sam Toyer]]

## Data Description

StrongREJECT is a benchmark consisting of 313 high-quality forbidden prompts across categories of harmful behavior, along with a rubric-based automated evaluator. The evaluator is available as a fine-tuned Gemma-2B classifier and a GPT-4o-mini prompt template.


## Notes


## Citation Info

124 citations (Semantic Scholar/arXiv) [2025-08-27]
