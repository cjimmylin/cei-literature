---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0519
type: preprint
short_title: "Latxa: An Open Language Model and Evaluation Suite for Basque"
year: 2025
first_author: "[[Julen Etxaniz]]"
last_author: "[[Oscar Sainz]]"
authors: "Julen Etxaniz, Oscar Sainz et al."
url: "https://arxiv.org/abs/2403.20266"
external_pdf: "https://arxiv.org/pdf/2403.20266.pdf"
publication: "arXiv / ACL 2024"
pdf_extract: "PDF Extracts/2024/2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque.md"
local_pdf: "[[PDFs/2024/2024-Etxaniz-Latxa An Open Language Model and Evaluation Suite for Basque.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: Basque
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark text corpus"
data_metrics: "5,169 questions; 16,774 questions; 4.3m documents"
LLM_assessed: "Latxa (LLaMa-based), Irati, Llama-2, Mistral"
DATA_URL: "https://github.com/hitz-zentroa/latxa"
tags: 
abstract: "We introduce Latxa, a family of large language models for Basque ranging from 7 to 70 billion parameters. Latxa is based on Llama 2, which we continue pretraining on a new Basque corpus comprising 4.3M documents and 4.2B tokens. Addressing the scarcity of high-quality benchmarks for Basque, we further introduce 4 multiple choice evaluation datasets: EusProficiency, comprising 5,169 questions from official language proficiency exams; EusReading, comprising 352 reading comprehension questions;..."
research_topic: "Question Answering"
---
# Latxa: An Open Language Model and Evaluation Suite for Basque

## Authors

[[Julen Etxaniz, Oscar Sainz et al.]]

## Metadata

**Authors:** Julen Etxaniz, Oscar Sainz et al.

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL 2024

**Languages:** Basque

**Benchmark:** Latxa / EusProficiency / EusReading / EusTrivia / EusExams

## Links

- **arXiv:** https://arxiv.org/abs/2403.20266

## Abstract

Family of LLMs for Basque (7B-70B parameters) with 4 evaluation datasets: EusProficiency (5,169 questions), EusReading (352 questions), EusTrivia (1,715 questions), EusExams (16,774 questions). Latxa outperforms all previous open models and is competitive with GPT-4 Turbo.

## Summary

This paper introduces Latxa, a family of open large language models for Basque ranging from 7 to 70 billion parameters, based on Llama 2 and further pre-trained on a new Basque corpus comprising 4.3 million documents and 4.2 billion tokens. To address the scarcity of high-quality benchmarks for Basque, the authors create four multiple-choice evaluation datasets: EusProficiency (5,169 questions from official language proficiency exams), EusReading (352 reading comprehension questions), EusTrivia (1,715 trivia questions), and EusExams (16,774 exam questions). Latxa outperforms all previous open Basque models and achieves competitive performance with GPT-4 Turbo, while the comprehensive evaluation suite establishes a foundation for subsequent bias and fairness studies in Basque NLP.

## Data Description

Latxa language model family and evaluation suite for Basque, based on LLaMa-2 architecture with continued pre-training and instruction tuning on Basque text. Includes EusKaliBench evaluation benchmark testing question answering, sentiment analysis, named entity recognition, and linguistic tasks.


## Detailed Summary

This paper introduces Latxa, a family of open large language models for Basque ranging from 7 to 70 billion parameters, developed by the HiTZ Center at the University of the Basque Country. Latxa is based on Llama 2, which the authors continue pre-training on a carefully curated Basque corpus comprising 4.3 million documents and 4.2 billion tokens from 7 sources: EusCrawl v1.1 (1.94M documents of high-quality news text, newly updated), Egunkaria (176K newspaper articles, new), Booktegi (166 EPUB books, new), Wikipedia (550K documents), CulturaX, Colossal OSCAR, and HPLT v1. The corpus undergoes thorough deduplication (reducing HPLT from 2.29M to 370K documents) and quality filtering. To address the scarcity of evaluation resources for Basque, the authors create four multiple-choice evaluation datasets totaling 23,282 questions: EusProficiency (5,169 questions from official Basque language proficiency exams), EusReading (352 reading comprehension questions), EusTrivia (1,715 trivia questions across 5 knowledge areas), and EusExams (16,774 questions from public examinations). Basque, the 52nd language in Common Crawl with only 0.035% of total content, represents a particularly challenging low-resource case.

## Paper Outline

1. Introduction - Motivation for low-resource Basque LLMs, contributions overview
2. Training Corpora - Data sources (EusCrawl v1.1, Egunkaria, Booktegi, Wikipedia, CulturaX, OSCAR, HPLT), preprocessing pipeline, corpus statistics
3. Model Training - Continued pre-training from Llama 2, vocabulary adaptation, training details
4. Evaluation Benchmarks - EusProficiency, EusReading, EusTrivia, EusExams descriptions
5. Experiments - Main results, comparison with open and closed models, analysis
6. Conclusion

## Methods Summary

Latxa models (7B, 13B, 70B) are obtained by continuing Llama 2 pre-training on the Basque corpus. The tokenizer vocabulary is expanded with Basque-specific tokens to improve tokenization efficiency. Training uses standard causal language modeling with carefully tuned learning rates and batch sizes appropriate for each model size. The four evaluation datasets use multiple-choice format evaluated via log-likelihood scoring (selecting the answer with highest probability). Comparison includes open models (XGLM 7B, BLOOM 7B, Mistral 7B, mGPT 13B, Mixtral 8x7B, Yi 34B, base Llama 2 models) and closed models (GPT-3.5 Turbo, GPT-4 Turbo). Existing benchmarks (XStoryCloze, Belebele, BasqueGLUE) are also used for evaluation.

## Results Summary

Latxa-70B achieves an average score of 61.08 across all benchmarks, outperforming the previous best open model (Yi 34B at 42.13) by 18.95 points and its base Llama 2-70B by 25.18 points. Latxa-70B surpasses GPT-3.5 Turbo on all datasets and is competitive with GPT-4 Turbo, even outperforming it on language proficiency (EusProficiency: 60.65 vs. 56.70). However, GPT-4 Turbo leads on reading comprehension (EusReading: 75.85 vs. 62.45) and knowledge-intensive tasks (EusExams: 73.12 vs. 51.90), suggesting that linguistic competence alone does not determine all capabilities. Scaling effects are substantial: Latxa-7B (40.94) to 13B (50.08) to 70B (61.08) shows consistent improvement. The 13B model already outperforms all non-Latxa open models.

## Conclusions

The results demonstrate that continuing pre-training of existing open models on language-specific data can dramatically improve performance for low-resource languages, and that linguistic competence in a language does not determine all LLM capabilities in that language. Key limitations include the relatively small Basque training corpus (4.2B tokens) compared to English pre-training data, and the multiple-choice evaluation format which may not capture generative capabilities. The separation between language proficiency (where Latxa excels) and world knowledge (where GPT-4 leads) opens doors to further improvements as stronger base English models become available.

## Artifact Contributions

- **Latxa Models**: Family of Basque LLMs (7B, 13B, 70B parameters) under open licenses (https://github.com/hitz-zentroa/latxa)
- **Basque Training Corpus**: 4.3M documents, 4.2B tokens from 7 curated sources
- **EusProficiency**: 5,169 official language proficiency exam questions
- **EusReading**: 352 reading comprehension questions
- **EusTrivia**: 1,715 trivia questions across 5 knowledge areas
- **EusExams**: 16,774 public examination questions

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Primary Basque language model with comprehensive evaluation suite. Foundation for subsequent bias and fairness evaluations in Basque.

## Tags

