---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: RLZC2E5T
type: preprint
short_title: "Towards Answering Open-ended Ethical Quandary"
year: 2023
first_author: "[[Yejin Bang]]"
last_author: "[[Pascale Fung]]"
authors: "Yejin Bang; Nayeon Lee; Tiezheng Yu; Leila Khalatbari; Yan Xu; Samuel Cahyawijaya; Dan Su; Bryan Wilie; Romain Barraud; Elham J. Barezi; Andrea Madotto; Hayden Kee; Pascale Fung"
doi: 10.48550/arXiv.2205.05989
url: "http://arxiv.org/abs/2205.05989"
external_pdf: "http://arxiv.org/pdf/2205.05989.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "Jainism"
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
religious_values_list: "Jainism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "Value Pluralism / Schwartz, Moral Reasoning & Psychology"
key_contribution: "Proposed the task of 'Ethical Quandary Generative Question Answering', prompting LLMs to provide deliberative, multi-perspective answers (Socratic method) rather than single-oracle verdicts."
significance: "Shifts the goal of ethical AI from 'giving the right answer' to 'facilitating moral deliberation', evaluating whether models can reason through conflicting principles (e.g., utilitarian vs. deontological) in open-ended scenarios."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Bang-Towards Answering Open-ended Ethical Quandary.md"
abstract: "Considerable advancements have been made in various NLP tasks based on the impressive power of large language models (LLMs) and many NLP applications are deployed in our daily lives. In this work, we challenge the capability of LLMs with the new task of ETHICAL QUANDARY GENERATIVE QUESTION ANSWERING. Ethical quandary questions are more challenging to address because multiple conﬂicting answers may exist to a single quandary."
paper_summary: "Abstract: Considerable advancements have been made in various NLP tasks based on the impressive power of large language models (LLMs) and many NLP applications are deployed in our daily lives. In this work, we  | Overview: Towards Answering Open-ended Ethical Quandary Questions Yejin Bang,1 Nayeon Lee,1 Tiezheng Yu,1 Leila Khalatbari,1 Yan Xu,1 Samuel Cahyawijaya,1 Dan Su,1 Bryan Wilie,1 Romain Barraud,1 Elham J. Barezi | Methodology: We conduct an experiment with LLMs with few-shot in- context prompt learning in ETHICAL QUANDARY GQA. Inspired by the characteristics of ethical quand | Key Findings: Q1: Can AISOCRATES answer from multiple perspec- tives? This aspect is of great interest in ETHICAL QUANDARY GQA. As shown in Figure 1, AISOCRATES pro | Conclusions: of responsible AI systems for open-ended questions by chal- lenging the capability of AI to provide relevant and nuanced answers to ethical quandary q"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Bang-Towards Answering Open-ended Ethical Quandary.pdf]]"
CONF-CC: "Preprint"
DATE_ADDED: 20260208
LLM_assessed: "BERT"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 45
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
ethics_perspective: "General Ethics"
---
# Towards Answering Open-ended Ethical Quandary Questions

## Metadata

**Authors:** Bang, Yejin; Lee, Nayeon; Yu, Tiezheng; Khalatbari, Leila; Xu, Yan; Cahyawijaya, Samuel; Su, Dan; Wilie, Bryan; Barraud, Romain; Barezi, Elham J.; Madotto, Andrea; Kee, Hayden; Fung, Pascale

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2205.05989](https://doi.org/10.48550/arXiv.2205.05989)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2023/2023-Bang-Towards Answering Open-ended Ethical Quandary.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2205.05989
- **DOI:** https://doi.org/10.48550/arXiv.2205.05989

## Abstract

Considerable advancements have been made in various NLP tasks based on the impressive power of large language models (LLMs) and many NLP applications are deployed in our daily lives. In this work, we challenge the capability of LLMs with the new task of ETHICAL QUANDARY GENERATIVE QUESTION ANSWERING. Ethical quandary questions are more challenging to address because multiple conﬂicting answers may exist to a single quandary. We explore the current capability of LLMs in providing an answer with a deliberative exchange of different perspectives to an ethical quandary, in the approach of Socratic philosophy, instead of providing a closed answer like an oracle. We propose a model that searches for different ethical principles applicable to the ethical quandary and generates an answer conditioned on the chosen principles through prompt-based few-shot learning. We also discuss the remaining challenges and ethical issues involved in this task and suggest the direction toward developing responsible NLP systems by incorporating human values explicitly.

## Authors

[[Yejin Bang]], [[Nayeon Lee]], [[Tiezheng Yu]], [[Leila Khalatbari]], [[Yan Xu]], [[Samuel Cahyawijaya]], [[Dan Su]], [[Bryan Wilie]], [[Romain Barraud]], [[Elham J. Barezi]], [[Andrea Madotto]], [[Hayden Kee]], [[Pascale Fung]]

## Data Description

The study uses the New York Times Ethicist Columns (NYT-Ethicist) dataset, consisting of 1,295 pairs of ethical quandary questions and philosopher-written answers collected from the NYT website. The AISOCRATES model, backboned by Jurassic-1 Jumbo (178B parameters), is evaluated on 130 test samples using human evaluation (A/B testing) across three criteria: multi-perspective provision, coherence, and justification, along with automatic metrics (ROUGE, SacreBLEU, BERTscore).


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

6 citations (Semantic Scholar/arXiv) [2025-08-27] 9 citations (Semantic Scholar/DOI) [2025-08-27] 9 citations (Semantic Scholar/DOI) [2025-08-23]
