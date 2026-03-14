---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: MQ33Y2XN
type: journalArticle
short_title: "Evaluating Prompt Injection Attacks with"
year: 2025
first_author: "[[Sharaf Rashid]]"
last_author: "[[Amar Gupta]]"
authors: "Sharaf Rashid; Edson Bollis; Lucas Pellicer; Darian Rabbani; Rafael Palacios; Aneesh Gupta; Amar Gupta"
doi: 10.3390/make7030077
url: "https://www.mdpi.com/2504-4990/7/3/77"
external_pdf: "file:///Users/jimmylin/Zotero/storage/L5X24WSS/Rashid et al. - 2025 - Evaluating Prompt Injection Attacks with LSTM-Based Generative Adversarial Networks A Lightweight A.pdf"
pdf_extract: "PDF Extracts/2025/2025-Rashid-Evaluating Prompt Injection Attacks with.md"
local_pdf: "[[PDFs/2025/2025-Rashid-Evaluating Prompt Injection Attacks with.pdf]]"
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
newtags: 
tags: 
abstract: "Generative Adversarial Networks (GANs) using Long Short-Term Memory (LSTM) provide a computationally cheaper approach for text generation compared to large language models (LLMs). The low hardware barrier of training GANs poses a threat because it means more bad actors may use them to mass-produce prompt attack messages against LLM systems. Thus, to better understand the threat of GANs being used for prompt attack generation, we train two well-known GAN architectures, SeqGAN and RelGAN, on..."
CONF-CC: "Machine Learning"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4o"
DATA_URL: NA
CONFERENCE: "Journal"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: No
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Evaluating Prompt Injection Attacks with LSTM-Based Generative Adversarial Networks: A Lightweight Alternative to Large Language Models

## Metadata

**Authors:** Rashid, Sharaf; Bollis, Edson; Pellicer, Lucas; Rabbani, Darian; Palacios, Rafael; Gupta, Aneesh; Gupta, Amar

**Year:** 2025

**Publication:** Machine Learning and Knowledge Extraction

**Type:** journalArticle

**DOI:** [10.3390/make7030077](https://doi.org/10.3390/make7030077)

**Pages:** 77

**Volume/Issue:** Vol. 7, Issue 3

## Links

- **URL:** https://www.mdpi.com/2504-4990/7/3/77
- **DOI:** https://doi.org/10.3390/make7030077

## Abstract

Generative Adversarial Networks (GANs) using Long Short-Term Memory (LSTM) provide a computationally cheaper approach for text generation compared to large language models (LLMs). The low hardware barrier of training GANs poses a threat because it means more bad actors may use them to mass-produce prompt attack messages against LLM systems. Thus, to better understand the threat of GANs being used for prompt attack generation, we train two well-known GAN architectures, SeqGAN and RelGAN, on prompt attack messages. For each architecture, we evaluate generated prompt attack messages, comparing results with each other, with generated attacks from another computationally cheap approach, a 1-billion-parameter Llama 3.2 small language model (SLM), and with messages from the original dataset. This evaluation suggests that GAN architectures like SeqGAN and RelGAN have the potential to be used in conjunction with SLMs to readily generate malicious prompts that impose new threats against LLM-based systems such as chatbots. Analyzing the effectiveness of state-of-the-art defenses against prompt attacks, we also find that GAN-generated attacks can deceive most of these defenses with varying levels of success with the exception of Meta’s PromptGuard. Further, we suggest an improvement of prompt attack defenses based on the analysis of the language quality of the prompts, which we found to be the weakest point of GAN-generated messages.

## Authors

[[Sharaf Rashid]], [[Edson Bollis]], [[Lucas Pellicer]], [[Darian Rabbani]], [[Rafael Palacios]], [[Aneesh Gupta]], [[Amar Gupta]]

## Data Description

The study uses Lakera's Mosscap dataset of 278,945 adversarial prompt injection messages, pre-processed to 52,316 training and 15,732 test messages. LSTM-based GANs (SeqGAN, RelGAN) and a Llama 3.2 1B model are trained on these prompts to generate new attack messages, which are tested against Gandalf, GPT-4o, and Meta's PromptGuard defense systems.


## Notes


## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27]
