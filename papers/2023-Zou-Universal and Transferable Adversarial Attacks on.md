---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7A2F2V7E
type: document
short_title: "Universal and Transferable Adversarial Attacks on"
year: 2025
first_author: "[[Andy Zou]]"
last_author: "[[Matt Fredrikson]]"
authors: "Andy Zou; Zifan Wang; Nicholas Carlini; Milad Nasr; J. Zico Kolter; Matt Fredrikson"
url: "https://arxiv.org/abs/2307.15043"
external_pdf: "https://arxiv.org/pdf/2307.15043.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: Utilitarianism
key_contribution: "Develops an automated method to generate 'adversarial suffixes' that universally bypass alignment protections in LLMs (ChatGPT, Claude, LLaMA) with high transferability"
significance: "Demonstrates the fragility of current alignment techniques ('jailbreaking' via gradient-based search), posing a critical safety challenge for deploying aligned systems"
tags: 
pdf_extract: "PDF Extracts/2023/2023-Zou-Universal and Transferable Adversarial Attacks on.md"
abstract: "Because “out-of-the-box” large language models are capable of generating a great deal of objectionable content, recent work has focused on aligning these models in an attempt to prevent undesirable generation. While there has been some success at circumventing these measures—so-called “jailbreaks” against LLMs—these attacks have required significant human ingenuity and are brittle in practice. Attempts at automatic adversarial prompt generation have also achieved limited success."
paper_summary: "Abstract: Because 'out-of-the-box' large language models are capable of generating a great deal of objectionable content, recent work has focused on aligning these models in an attempt to prevent undesirable ge | Overview: Universal and Transferable Adversarial Attacks on Aligned Language Models Andy Zou1,2, Zifan Wang2, Nicholas Carlini3, Milad Nasr3, J. Zico Kolter1,4, Matt Fredrikson1 1Carnegie Mellon University, 2Ce | Methodology: improves substantially upon existing attack methods, is able to reliably break the target (white box) model, and the resulting attacks can even demons | Conclusions: At a high level, we believe that the implications of this work are quite broad, and raise substantial questions regarding current methods for the alig"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Zou-Universal and Transferable Adversarial Attacks on.pdf]]"
CONF-CC: Preprint
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, Claude, Falcon, GPT-3.5, GPT-4, Llama-2, PaLM, Pythia, Vicuna"
DATA_URL: "https://github.com/llm-attacks/llm-attacks"
CONFERENCE: Preprint
ethics_overall: No
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
data_description: "Evaluation methodology"
data_metrics: "Not specified"
---
# Universal and Transferable Adversarial Attacks on Aligned Language Models

## Metadata

**Authors:** Zou, Andy; Wang, Zifan; Carlini, Nicholas; Nasr, Milad; Kolter, J. Zico; Fredrikson, Matt

**Year:** 2023

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2023/2023-Zou-Universal and Transferable Adversarial Attacks on.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2307.15043

## Abstract

Because "out-of-the-box" large language models are capable of generating a great deal of objectionable content, recent work has focused on aligning these models in an attempt to prevent undesirable generation. While there has been some success at circumventing these measures -- so-called "jailbreaks" against LLMs -- these attacks have required significant human ingenuity and are brittle in practice. In this paper, we propose a simple and effective attack method that causes aligned language models to generate objectionable behaviors. Specifically, our approach finds a suffix that, when attached to a wide range of queries for an LLM to produce objectionable content, aims to maximize the probability that the model produces an affirmative response (rather than refusing to answer). However, instead of relying on manual engineering, our approach automatically produces these adversarial suffixes by a combination of greedy and gradient-based search techniques, and also improves over past automatic prompt generation methods. Surprisingly, we find that the adversarial prompts generated by our approach are quite transferable, including to black-box, publicly released LLMs. Specifically, we train an adversarial attack suffix on multiple prompts (i.e., queries asking for many different types of objectionable content), as well as multiple models (in our case, Vicuna-7B and 13B). When doing so, the resulting attack suffix is able to induce objectionable content in the public interfaces to ChatGPT, Bard, and Claude, as well as open source LLMs such as LLaMA-2-Chat, Pythia, Falcon, and others. In total, this work significantly advances the state-of-the-art in adversarial attacks against aligned language models, raising important questions about how such systems can be prevented from producing objectionable information. Code is available at github.com/llm-attacks/llm-attacks.

## Authors

[[Andy Zou]], [[Zifan Wang]], [[Nicholas Carlini]], [[Milad Nasr]], [[J. Zico Kolter]], [[Matt Fredrikson]]

## Data Description

Code and adversarial attack methodology for generating universal transferable adversarial suffixes against aligned LLMs.


## Notes


## Citation Info

1714 citations (Semantic Scholar/arXiv) [2025-08-27]
