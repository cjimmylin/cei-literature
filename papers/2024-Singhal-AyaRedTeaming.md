---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BKBB8NFZ
type: journalArticle
short_title: AyaRedTeaming
year: 2024
first_author: "[[Aakanksha]]"
last_author: "[[Sara Hooker]]"
authors: "Aakanksha; Arash Ahmadian; Beyza Ermis; Seraphina Goldfarb-Tarrant; Julia Kreutzer; Marzieh Fadaee; Sara Hooker"
url: "https://arxiv.org/abs/2406.18682"
external_pdf: "https://arxiv.org/pdf/2406.18682.pdf"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Multilingual"
religious_values: "Christianity"
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
religious_values_list: "Christianity"
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
key_contribution: "Released AyaRedTeaming, the first multilingual red-teaming dataset distinguishing between global harms (universal) and local harms (culture-specific) across 6 languages."
significance: "Criticizes the Western-centric focus of current safety alignment, showing that models need specific optimization to handle culture-variant safety preferences without degrading general performance."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Singhal-AyaRedTeaming.md"
abstract: "A key concern with the concept of alignment is the implicit question of alignment to what? AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and..."
paper_summary: "Abstract: A key concern with the concept of alignment is the implicit question of alignment to what? AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monol | Overview: The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm Aakanksha⋆ Cohere For AI Arash Ahmadian Cohere & Cohere For AI Beyza Ermis Cohere For AI Seraphina Goldfarb-Tarra | Methodology: DPO(IFT) SFT-Preferred DPO(SFT) SFT-Random Figure 1: Trade-off between general performance and safety performance of different mitigation techniques w | Key Findings: We use the LLM-as-an-evaluator setup with GPT-4 to classify the model generations as harmful or not and validate the reliability of this approach with | Conclusions: In this work, we demonstrate the importance of a wide variety of alignment methods to tackle the dual challenge of mitigating both local and global ha"
local_pdf: "[[PDFs/2024/2024-Singhal-AyaRedTeaming.pdf]]"
CONF-CC: "EMNLP 2024"
DATE_ADDED: 20260208
LLM_assessed: "Aya, Command R+, GPT-4"
DATA_URL: "https://huggingface.co/datasets/CohereForAI/aya_redteaming"
CONFERENCE: "Journal"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety annotated dataset"
data_metrics: "6 languages"
---
# AyaRedTeaming: A Benchmark for Exploring Alignment Across Global and Local Preferences

## Metadata

**Authors:** Singhal, A.; Mas-Tur, A.

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Singhal-AyaRedTeaming.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2406.18682

## Abstract

A key concern with the concept of "alignment" is the implicit question of "alignment to what?". AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and cultural preferences while minimizing both global and local harms. We collect the first set of human annotated red-teaming prompts in different languages distinguishing between global and local harm, which serve as a laboratory for understanding the reliability of alignment techniques when faced with preference distributions that are non-stationary across geographies and languages. While this setting is seldom covered by the literature to date, which primarily centers on English harm mitigation, it captures real-world interactions with AI systems around the world. We establish a new precedent for state-of-the-art alignment techniques across 6 languages with minimal degradation in general performance. Our work provides important insights into cross-lingual transfer and novel optimization approaches to safeguard AI systems designed to serve global populations.

## Authors

[[Aakanksha]], [[Arash Ahmadian]], [[Beyza Ermis]], [[Seraphina Goldfarb-Tarrant]], [[Julia Kreutzer]], [[Marzieh Fadaee]], [[Sara Hooker]]

## Data Description

Releases the Aya Red-teaming dataset: 7,419 human-annotated multilingual red-teaming prompts across 8 languages (English, Hindi, French, Spanish, Russian, Arabic, Serbian, Filipino) distinguishing global vs. local harms, used to study multilingual safety alignment.


## Notes


## Citation Info

43 citations (Semantic Scholar/arXiv) [2025-08-27]
