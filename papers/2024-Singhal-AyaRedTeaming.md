---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BKBB8NFZ
type: journalArticle
short_title: AyaRedTeaming
year: 2025
first_author: "[[Aakanksha]]"
last_author: "[[Sara Hooker]]"
authors: "Aakanksha; Arash Ahmadian; Beyza Ermis; Seraphina Goldfarb-Tarrant; Julia Kreutzer; Marzieh Fadaee; Sara Hooker"
url: "https://arxiv.org/abs/2406.18682"
external_pdf: "https://arxiv.org/pdf/2406.18682.pdf"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Released AyaRedTeaming, the first multilingual red-teaming dataset distinguishing between global harms (universal) and local harms (culture-specific) across 6 languages."
significance: "Criticizes the Western-centric focus of current safety alignment, showing that models need specific optimization to handle culture-variant safety preferences without degrading general performance."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Singhal-AyaRedTeaming.md"
abstract: "A key concern with the concept of alignment is the implicit question of alignment to what? AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monolingual settings. Additionally, preference training and safety measures often overfit to harms common in Western-centric datasets. Here, we explore the viability of different alignment approaches when balancing dual objectives: addressing and optimizing for a non-homogeneous set of languages and cult"
paper_summary: "Abstract: A key concern with the concept of alignment is the implicit question of alignment to what? AI systems are increasingly used across the world, yet safety alignment is often focused on homogeneous monol | Overview: The Multilingual Alignment Prism: Aligning Global and Local Preferences to Reduce Harm Aakanksha⋆ Cohere For AI Arash Ahmadian Cohere & Cohere For AI Beyza Ermis Cohere For AI Seraphina Goldfarb-Tarra | Methodology: DPO(IFT) SFT-Preferred DPO(SFT) SFT-Random Figure 1: Trade-off between general performance and safety performance of different mitigation techniques w | Key Findings: We use the LLM-as-an-evaluator setup with GPT-4 to classify the model generations as harmful or not and validate the reliability of this approach with | Conclusions: In this work, we demonstrate the importance of a wide variety of alignment methods to tackle the dual challenge of mitigating both local and global ha"
local_pdf: [[PDFs/2024/2024-Singhal-AyaRedTeaming.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety annotated dataset"
data_metrics: "6 languages"
LLM_assessed: "NA"
DATA_URL: "https://huggingface.co/datasets/CohereForAI/aya_redteaming"
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

The paper introduces the Aya Red-teaming dataset, a multilingual red-teaming dataset of 7,419 human-annotated harmful prompts across 8 languages (English, Hindi, French, Spanish, Russian, Arabic, Serbian, Filipino), distinguishing between global and local harms. The dataset includes synthetically expanded preference pairs for safety alignment training, along with a general-purpose multilingual preference dataset based on UltraFeedback Binarized translated into 6 target languages. Experiments evaluate SFT and DPO alignment techniques on an Aya 23 8B base model.


## Notes


## Citation Info

43 citations (Semantic Scholar/arXiv) [2025-08-27]
