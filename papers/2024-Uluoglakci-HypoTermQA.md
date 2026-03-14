---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ZI532PK5
type: journalArticle
short_title: HypoTermQA
year: 2024
first_author: "[[Cem Uluoglakci]]"
last_author: "[[Temizel, Tugba]]"
authors: "Uluoglakci, Cem; Temizel, Tugba"
url: "https://aclanthology.org/2024.eacl-srw.9/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/N3YAM6Q3/2024 - HypoTermQA Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
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
newtags: "Hallucination & Truthfulness"
key_contribution: "Introduced 'HypoTermQA', a dataset of *hypothetical* terms (fake concepts) to test hallucination tendency – since the terms don't exist, any detailed explanation is a hallucination."
significance: "A clever way to measure 'intrinsic hallucination' without needing external knowledge bases, testing the model's epistemic humility (can it say 'I don't know'?)."
tags: 
abstract: "Hallucinations pose a significant challenge to the reliability and alignment of Large Language Models (LLMs), limiting their widespread acceptance beyond chat-bot applications. Despite ongoing efforts, hallucinations remain a prevalent challenge in LLMs. The detection of hallucinations itself is also a formidable task, frequently requiring manual labeling or constrained evaluations. This paper introduces an automated scalable framework that combines benchmarking LLMs’ hallucination tendencies..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, Llama-2"
DATA_URL: "https://github.com/cemuluoglakci/HypoTermQA"
pdf_extract: "PDF Extracts/2024/2024-Uluoglakci-HypoTermQA.md"
local_pdf: "[[PDFs/2024/2024-Uluoglakci-HypoTermQA.pdf]]"
CONFERENCE: "EACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Hallucination & Truthfulness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for hallucination detection dataset for question answering"
data_metrics: "Not specified"
---
# HypoTermQA: Hypothetical Terms Dataset for Benchmarking Hallucination Tendency of LLMs

## Authors

[[Cem Uluoglakci|Uluoglakci, Cem]], [[Tugba Temizel|Temizel, Tugba]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.eacl-srw.9/

## Abstract

Hallucinations pose a significant challenge to the reliability and alignment of Large Language Models (LLMs), limiting their widespread acceptance beyond chatbot applications. Despite ongoing efforts, hallucinations remain a prevalent challenge in LLMs. The detection of hallucinations itself is also a formidable task, frequently requiring manual labeling or constrained evaluations. This paper introduces an automated scalable framework that combines benchmarking LLMs’ hallucination tendencies with efficient hallucination detection. We leverage LLMs to generate challenging tasks related to hypothetical phenomena, subsequently employing them as agents for efficient hallucination detection. The framework is domain-agnostic, allowing the use of any language model for benchmark creation or evaluation in any domain. We introduce the publicly available HypoTermQA Benchmarking Dataset, on which state-of-the-art models’ performance ranged between 3% and 11%, and evaluator agents demonstrated a 6% error rate in hallucination prediction. The proposed framework provides opportunities to test and improve LLMs. Additionally, it has the potential to generate benchmarking datasets tailored to specific domains, such as law, health, and finance.

## Data Description

Introduces HypoTermQA, a hallucination benchmark dataset of questions about hypothetical non-existent terms across 20 topics, designed to benchmark LLMs' tendency to hallucinate content about fabricated concepts.


## Notes

