---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0521
type: preprint
short_title: "A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a Millionaire?' Videos"
year: 2025
first_author: "[[Alexandru-Gabriel Ganea]]"
last_author: "[[Adrian-Marius Dumitran]]"
authors: "[[Alexandru-Gabriel Ganea]]; [[Antonia-Adelina Popovici]]; [[Adrian-Marius Dumitran]]"
url: "https://arxiv.org/abs/2506.05991"
external_pdf: "https://arxiv.org/pdf/2506.05991.pdf"
publication: "arXiv / RANLP 2025"
pdf_extract: "PDF Extracts/2025/2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a.md"
local_pdf: "[[PDFs/2025/2025-Ganea-A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: Romanian
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "ALBERT, BERT, GPT-4, Gemini, Gemma, Gemma-2, Gemma2, Llama, LLaMA 3.3, LLaMA3, LLaMA3., Llama-3, Llama-3.1, Llama-3.3, Mistral 7b, Mistral-7B, PaLM, Phi-4, Phi-4 56, Qwen, Qwen2.5, RoBERTa, gemini-1.5-flash"
DATA_URL: "https://huggingface.co/datasets"
tags: 
abstract: "Large Language Models (LLMs) demonstrate varying performance across languages and cultural contexts. This study introduces a novel, culturally-rich, multilingual dataset derived from video recordings of the Romanian game show 'Who Wants to Be a Millionaire?' (Vrei să fii Milionar?). We employed an innovative process combining optical character recognition (OCR), automated text extraction, and manual verification to collect question-answer pairs, enriching them with metadata including question..."
research_topic: "Machine Translation"
authors_incomplete: false
---
# A Culturally-Rich Romanian NLP Dataset from 'Who Wants to Be a Millionaire?' Videos

## Authors

[[Alexandru-Gabriel Ganea]], [[Antonia-Adelina Popovici]], [[Adrian-Marius Dumitran]]

## Metadata

**Authors:** Alexandru-Gabriel Ganea, Antonia-Adelina Popovici, Adrian-Marius Dumitran

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / RANLP 2025

**Languages:** Romanian

**Benchmark:** WWTBM-RO

## Links

- **arXiv:** https://arxiv.org/abs/2506.05991
- **Code/Data:** https://huggingface.co/datasets

## Abstract

Novel culturally-rich dataset from Romanian 'Who Wants to Be a Millionaire?' videos for LLM evaluation. Reveals significant performance gap: models achieve 80-95% on international questions vs. 50-75% on Romanian-specific cultural questions. Romanian fine-tuning shows mixed effects on cultural knowledge.

## Summary

This paper introduces WWTBM-RO, a culturally-rich Romanian dataset derived from video recordings of 'Who Wants to Be a Millionaire?' (Vrei să fii Milionar?) using optical character recognition, automated text extraction, and manual verification. The dataset includes question-answer pairs enriched with metadata including difficulty levels and cultural specificity annotations. Evaluation of LLMs reveals a striking performance gap between international questions (80-95% accuracy) and Romanian-specific cultural questions (50-75% accuracy), highlighting significant deficits in cultural knowledge for low-resource languages despite Romanian fine-tuning.

## Data Description

Introduces WWTBM-RO, a culturally-rich dataset from Romanian 'Who Wants to Be a Millionaire?' videos for LLM evaluation. Reveals significant performance gap: models achieve 80-95% on international questions vs. 50-75% on Romanian-specific cultural questions, highlighting cultural knowledge deficits in current LLMs.


## Detailed Summary

This paper introduces a novel, culturally-rich multilingual dataset derived from video recordings of the Romanian game show "Who Wants to Be a Millionaire?" (Vrei sa fii Milionar?). Using an innovative pipeline combining optical character recognition (OCR), automated text extraction, and manual verification, the authors collect question-answer pairs from video recordings and enrich them with metadata including question domain (biology, history, etc.), cultural relevance (Romanian-specific vs. international), and difficulty level (easy, medium, hard). Benchmarking state-of-the-art LLMs including Romanian-adapted models reveals a striking performance disparity: models consistently achieve 80-95% accuracy on international questions but only 50-75% on Romanian-specific cultural questions. The study further investigates these differences through experiments involving machine translation of Romanian questions into English and cross-lingual tests using a comparable French dataset. The dataset is publicly available on Hugging Face and represents a valuable resource for studying cultural knowledge gaps in multilingual NLP systems.

## Paper Outline

1. Introduction - Need for culturally situated LLM evaluation in low-resource languages
2. Related Work - Linguistic and cultural diversity in LLM evaluation; Romanian NLP resources
3. Dataset Construction - OCR-based extraction from video recordings; metadata annotation
4. Experimental Setup - Model selection; evaluation methodology
5. Results - Performance gap between international and Romanian-specific questions
6. Cross-Lingual Analysis - Machine translation and French dataset comparison
7. Discussion - Implications for culturally-aware NLP systems
8. Conclusion

## Methods Summary

Data collection involves extracting question-answer pairs from video recordings of the Romanian "Who Wants to Be a Millionaire?" show using OCR and automated text extraction with manual verification. Each question is annotated for cultural relevance (Romanian-specific vs. international), difficulty, and domain. State-of-the-art LLMs including Romanian-adapted models are evaluated. Cross-lingual experiments translate Romanian questions to English to test whether performance gaps are due to language or cultural knowledge deficits. A comparable French dataset provides additional cross-cultural comparison.

## Results Summary

Models consistently achieve higher accuracy (80-95%) on international questions compared to Romanian-specific cultural questions (50-75%), representing a 15-25 percentage point gap. This disparity persists even with Romanian-adapted models, indicating that fine-tuning on Romanian text does not automatically confer cultural knowledge. Machine translation experiments suggest the gap is primarily due to missing cultural knowledge rather than language understanding limitations. Cross-lingual tests with a French dataset confirm similar patterns of cultural knowledge deficits across languages.

## Conclusions

The study demonstrates that current LLMs exhibit significant cultural knowledge deficits for underrepresented cultures like Romania, with performance gaps not resolved by language-specific fine-tuning alone. The findings underscore the need for culturally-grounded evaluation datasets and training approaches that go beyond language proficiency to encompass cultural knowledge, with implications for educational applications and inclusive NLP system development.

## Artifact Contributions

- **Dataset:** WWTBM-RO - culturally-rich Romanian question-answer dataset from "Who Wants to Be a Millionaire?" videos, publicly available on Hugging Face (https://huggingface.co/datasets/WWTBM/wwtbm)
- **Methodology:** OCR-based data extraction pipeline for creating culturally-grounded QA datasets from video content

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Directly evaluates LLM cultural knowledge for Romania. Performance gap between international and Romanian-specific questions highlights cultural bias.

## Tags

