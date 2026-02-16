---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0446
type: preprint
short_title: "MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs"
year: 2025
first_author: "[[Scale AI research team]]"
last_author: "[[Scale AI research team]]"
authors: "Scale AI research team"
url: "https://arxiv.org/abs/2507.17476"
external_pdf: "https://arxiv.org/pdf/2507.17476.pdf"
publication: "arXiv / Scale AI"
pdf_extract: "PDF Extracts/2025/2025-team-MultiNRC A Challenging and Native Multilingual Reasoning Evaluation.md"
local_pdf: "[[PDFs/2025/2025-team-MultiNRC A Challenging and Native Multilingual Reasoning Evaluation.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Chinese, French, Spanish"
cultures_nationalities_list: "Chinese, French, Spanish"
languages_list: "Chinese, French, Spanish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
LLM_assessed: "o3-pro, multiple LLMs"
DATA_URL: "https://scale.com/leaderboard/multinrc"
tags: 
abstract: "Although recent Large Language Models (LLMs) have shown rapid improvement on reasoning benchmarks in English, the evaluation of such LLMs’ multilingual reasoning capability across diverse languages and cultural contexts remains limited. Existing multilingual reasoning benchmarks are typically constructed by translating existing English reasoning benchmarks, biasing these benchmarks towards reasoning problems with context in English language/cultures."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Translation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark"
data_metrics: "Not specified"
---
# MultiNRC: A Challenging and Native Multilingual Reasoning Evaluation Benchmark for LLMs

## Authors

[[Scale AI research team]]

## Metadata

**Authors:** Scale AI research team

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / Scale AI

**Languages:** Chinese, French, Spanish

**Benchmark:** MultiNRC

## Links

- **arXiv:** https://arxiv.org/abs/2507.17476
- **Code/Data:** https://scale.com/leaderboard/multinrc

## Abstract

Native multilingual reasoning benchmark with 1,000+ questions authored by native speakers in French, Spanish, and Chinese. Covers linguistic reasoning, wordplay, cultural/tradition reasoning, and math with cultural relevance. Best LLM (o3-pro) achieves only 49% accuracy. Published July 2025.

## Summary

This paper introduces MultiNRC, a challenging native multilingual reasoning benchmark comprising over 1,000 questions authored by native speakers in French, Spanish, and Chinese to avoid the cultural biases inherent in machine-translated benchmarks. Covering linguistic reasoning, wordplay, cultural and tradition reasoning, and culturally relevant mathematics, the benchmark reveals significant performance gaps even for frontier models, with the best-performing LLM (o3-pro) achieving only 49% accuracy. The native-sourced approach ensures questions reflect authentic cultural contexts and linguistic nuances that are lost in translation-based benchmarks.

## Data Description

Introduces MultiNRC, a native multilingual reasoning benchmark with 1,000+ questions authored by native speakers in French, Spanish, and Chinese, covering linguistic reasoning, wordplay, cultural/tradition reasoning, and culturally relevant math. Best LLM (o3-pro) achieves only 49% accuracy, revealing performance gaps.


## Detailed Summary

This paper from Scale AI introduces MultiNRC (Multilingual Native Reasoning Challenge), a benchmark designed to assess LLMs on more than 1,000 native, linguistically and culturally grounded reasoning questions written by native speakers in French, Spanish, and Chinese. The benchmark covers four core reasoning categories: language-specific linguistic reasoning (e.g., French grammatical gender puzzles), wordplay and riddles (e.g., Chinese homophone-based idiom questions), cultural and tradition reasoning (e.g., Spanish holiday date calculations), and mathematical reasoning with cultural relevance (e.g., French real estate viager calculations). Only questions that cause at least 3 out of 5 state-of-the-art LLMs to fail are accepted, ensuring high difficulty. Automatic evaluation uses LLM-as-a-judge with over 95% alignment with human judgment. The systematic evaluation of 14 leading LLMs reveals that no model scores above 50% on MultiNRC -- the best-performing model, o3-pro, achieves only 49% accuracy. English equivalent translations of cultural and math questions are provided for direct cross-lingual comparison, revealing that LLMs perform approximately 10% better on English math reasoning than on original-language versions, suggesting cultural knowledge retrieval is easier in English.

## Paper Outline

1. Introduction - Gap in native multilingual reasoning benchmarks
2. Related Work - English and multilingual reasoning benchmarks
3. Benchmark Construction - Native speaker annotation; quality control; category definitions
4. Automatic Evaluation - LLM-as-a-judge methodology
5. Experimental Results - 14 LLM evaluation across categories and languages
6. English Equivalent Analysis - Cross-lingual performance comparison
7. Ablation Studies - Language, translation, and cultural context effects
8. Conclusion

## Methods Summary

Native speakers create challenging reasoning questions with objective short answers in their respective languages. Quality control requires that at least 3 of 5 SOTA LLMs fail each question. Four categories are defined: linguistic reasoning (untranslatable language-specific puzzles), wordplay/riddles (language-specific phonetic and semantic play), cultural/tradition reasoning (culturally grounded knowledge questions), and math with cultural relevance (computation requiring cultural context). English equivalent translations are manually created by bilingual annotators for cultural and math categories only (linguistic and wordplay categories cannot meaningfully be translated). Automatic evaluation with LLM-as-a-judge achieves >95% human alignment.

## Results Summary

The best-performing model, o3-pro, achieves only 49% accuracy, with o3 variants and Gemini-2.5-Pro substantially outperforming other models. LLMs rank differently across reasoning categories -- Gemini-2.5-Pro ranks third overall but first in culturally relevant math. On English equivalent translations, LLMs achieve approximately 10% higher accuracy on math reasoning compared to original-language versions, indicating cultural context retrieval is more effective in English. For cultural/tradition reasoning, no significant performance improvement is seen with English translations, suggesting this knowledge is equally absent in both English and native language representations. Different models show distinct strengths across linguistic, cultural, and logical reasoning dimensions.

## Conclusions

MultiNRC demonstrates that current SOTA LLMs remain far from mastering native multilingual reasoning, with none exceeding 50% accuracy. The benchmark provides a more informative evaluation taxonomy than aggregate scores by revealing model-specific strengths and weaknesses across reasoning categories. The English equivalent analysis shows persistent challenges with culturally grounded knowledge regardless of language, while math reasoning benefits from English-language prompting.

## Artifact Contributions

- **Benchmark:** MultiNRC - 1,000+ native reasoning questions in French, Spanish, and Chinese with English equivalents
- **Leaderboard:** https://scale.com/leaderboard/multinrc
- **Evaluation Framework:** LLM-as-a-judge with >95% human alignment for automatic scoring

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** French-native reasoning benchmark with culturally grounded questions. Reveals LLMs still perform poorly on native French reasoning tasks.

## Tags

