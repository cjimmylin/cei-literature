---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KZRT6VY8
type: document
short_title: "The Multilingual Alignment Prism"
year: 2025
first_author: [[Aakanksha]]
last_author: "[[Sara Hooker]]"
authors: "Aakanksha; Arash Ahmadian; Beyza Ermis; Seraphina Goldfarb-Tarrant; Julia Kreutzer; Marzieh Fadaee; Sara Hooker"
url: "https://aclanthology.org/2024.emnlp-main.671/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/EMDAVPXV/2024 - The Multilingual Alignment Prism Aligning Global and Local Preferences to Reduce Harm.pdf"
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
languages_list: Multilingual
religious_values: Christianity
rv_islam: 0
rv_christianity: 50
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
religious_values_list: Christianity
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Collected the first human-annotated red teaming prompts across 6 languages to evaluate the cross-lingual generalization of safety alignment."
significance: "Reveals the 'anglocentric alignment' gap, showing that safety mechanisms trained on English often fail to transfer to other languages/cultures, necessitating multilingual safety data."
tags: 
abstract: "A key concern with the concept of alignment is the implicit question of alignment to what? AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and..."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: GPT-4
DATA_URL: "https://huggingface.co/datasets/CohereForAI/aya_redteaming"
pdf_extract: "PDF Extracts/2024/2024-Aakanksha-The Multilingual Alignment Prism.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Aakanksha-The Multilingual Alignment Prism.pdf]]"
CONFERENCE: "EMNLP 2024"
ethics_overall: No
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach annotated dataset"
data_metrics: "6 languages"
---
# The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm

## Authors

[[Aakanksha]], [[Arash Ahmadian]], [[Beyza Ermis]], [[Seraphina Goldfarb-Tarrant]], [[Julia Kreutzer]], [[Marzieh Fadaee]], [[Sara Hooker]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.emnlp-main.671/

## Abstract

A key concern with the concept of *“alignment”* is the implicit question of *“alignment to what?”*. AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and cultural preferences while minimizing both global and local harms. We collect the first human annotated red teaming prompts in different languages, distinguishing between global and local harm, which serve as a laboratory to understand the reliability of alignment techniques when faced with preference distributions that are non-stationary across geographies and languages. While this setting is seldom covered by the literature to date, which primarily centers on English harm mitigation, it captures real-world interactions with AI systems around the world. We establish a new precedent for state-of-the-art alignment techniques across 6 languages with minimal degradation in general performance. Our work provides important insights into cross-lingual transfer and novel optimization approaches to safeguard AI systems designed to serve global populations.

## Data Description

Aya Red-teaming dataset: first multilingual human-annotated red-teaming dataset across 8 languages with global vs. local harm distinctions, plus synthetic preference data for safety alignment.


## Notes

