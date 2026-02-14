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
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Collected the first human-annotated red teaming prompts across 6 languages to evaluate the cross-lingual generalization of safety alignment."
significance: "Reveals the 'anglocentric alignment' gap, showing that safety mechanisms trained on English often fail to transfer to other languages/cultures, necessitating multilingual safety data."
tags: 
abstract: "A key concern with the concept of *“alignment”* is the implicit question of *“alignment to what?”*. AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and cultural preferences while minimizing both global and local harms. We collect the first human annotated red teaming prompts in different languages, distinguishing between global and local harm, which serve as a laboratory to understand the reliability of alignment techniques when faced with preference distributions that are non-stationary across geographies and languages. While this setting is seldom covered by the literature to date, which primarily centers on English harm mitigation, it captures real-world interactions with AI systems around the world. We establish a new precedent for state-of-the-art alignment techniques across 6 languages with minimal degradation in general performance. Our work provides important insights into cross-lingual transfer and novel optimization approaches to safeguard AI systems designed to serve global populations."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach annotated dataset"
data_metrics: "6 languages"
LLM_assessed: GPT-4
DATA_URL: "https://huggingface.co/datasets/CohereForAI/aya_redteaming"
pdf_extract: "PDF Extracts/2024/2024-Aakanksha-The Multilingual Alignment Prism.md"
local_pdf: "[[PDFs/2024/2024-Aakanksha-The Multilingual Alignment Prism.pdf]]"
---
# The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm

## Authors

[[Aakanksha]], [[Arash Ahmadian]], [[Beyza Ermis]], [[Seraphina Goldfarb-Tarrant]], [[Julia Kreutzer]], [[Marzieh Fadaee]], [[Sara Hooker]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.emnlp-main.671/

## Abstract

A key concern with the concept of *“alignment”* is the implicit question of *“alignment to what?”*. AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and cultural preferences while minimizing both global and local harms. We collect the first human annotated red teaming prompts in different languages, distinguishing between global and local harm, which serve as a laboratory to understand the reliability of alignment techniques when faced with preference distributions that are non-stationary across geographies and languages. While this setting is seldom covered by the literature to date, which primarily centers on English harm mitigation, it captures real-world interactions with AI systems around the world. We establish a new precedent for state-of-the-art alignment techniques across 6 languages with minimal degradation in general performance. Our work provides important insights into cross-lingual transfer and novel optimization approaches to safeguard AI systems designed to serve global populations.

## Data Description

The paper introduces the Aya Red-teaming dataset, a first-of-its-kind multilingual red-teaming dataset with human-annotated harmful prompts across 8 languages (English, Hindi, French, Spanish, Russian, Arabic, Serbian, Filipino), distinguishing between global and local harms. The Aya 23 8B model was fine-tuned using SFT and DPO with safety and general-purpose preference data mixtures, and GPT-4 was used as an evaluator for preference labeling and safety classification.


## Notes

