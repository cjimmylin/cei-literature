---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0463
type: preprint
short_title: "AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection"
year: 2025
first_author: "[[Janis Goldzycher]]"
last_author: "[[Hanna Mahler]]"
authors: "Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler"
url: "https://arxiv.org/abs/2406.08080"
external_pdf: "https://arxiv.org/pdf/2406.08080.pdf"
publication: "arXiv / ACL Anthology"
local_pdf: "[[PDFs/2024/2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: German
languages_list: "German (Austrian)"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach annotated dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, mGPT, German BERT variants"
DATA_URL: "https://github.com/rafaelgoldzy/AustroTox"
tags: 
abstract: "Model interpretability in toxicity detection greatly profits from token-level annotations. However, currently such annotations are only available in English. We introduce a dataset annotated for offensive language detection sourced from a news forum, notable for its incorporation of the Austrian German dialect, comprising 4,562 user comments. In addition to binary offensiveness classification, we identify spans within each comment constituting vulgar language or representing targets of..."
ethics_perspective: "Toxicity & Hate Speech"
---
# AustroTox: A Dataset for Target-Based Austrian German Offensive Language Detection

## Authors

[[Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler]]

## Metadata

**Authors:** Janis Goldzycher, Anna Maria Planitzer, Claudia Pichler, Sebastian Pado, Hanna Mahler

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** German (Austrian)

**Benchmark:** AustroTox

## Links

- **arXiv:** https://arxiv.org/abs/2406.08080

## Abstract

Dataset of 4,562 Austrian German user comments annotated for offensive language detection with token-level spans for vulgarities and offensive targets. LLMs outperform fine-tuned models in detecting offensiveness while fine-tuned models excel at detecting dialect-specific vulgarities.

## Summary

This paper introduces AustroTox, the first offensive language detection dataset specifically for Austrian German dialect, comprising 4,562 user comments from news forums with token-level annotations for offensiveness, vulgar language spans, and offensive targets. The dataset addresses the critical gap in non-English token-level offensive language annotations and incorporates a target-based taxonomy (individual, group, other, none) to enhance model interpretability. The authors evaluate multiple models including GPT-3.5, GPT-4, mGPT, and German BERT variants, finding that large language models outperform fine-tuned models in detecting overall offensiveness while fine-tuned approaches excel at identifying dialect-specific vulgarities. This work provides essential resources for developing more robust and interpretable offensive language detection systems for Austrian German.

## Data Description

AustroTox dataset of 4,562 Austrian German Reddit comments annotated for offensive language with target-based taxonomy (individual, group, other, none). First offensive language dataset specifically for Austrian German dialect, comparing LLM performance vs. fine-tuned approaches.


## Detailed Summary

This paper introduces AustroTox, the first German-language offensive language detection dataset with token-level span annotations, comprising 4,562 user comments from the Austrian newspaper DerStandard's discussion forum, notable for incorporating the Austrian German dialect. Comments were collected from 532 articles and discussion forums posted between November 4-10, 2021, pre-filtered using stratified sampling based on Perspective API toxicity scores across four strata (0-0.3, 0.3-0.5, 0.5-0.7, 0.7-0.9) plus all comments scoring 0.9-1.0 from a pool of 123,108 posts. The annotation campaign involved master's students in Data Science and undergraduate Linguistics students, predominantly Austrian and aged 19-26, with German C1 level required. Each comment was annotated by 2-5 annotators (majority by 5) for binary offensiveness, with additional span-level annotations for vulgar language and offensive targets categorized as Individual, Group, or Other. A sensitivity-prioritizing aggregation approach labels comments as offensive with fewer votes than needed for non-offensive. The final dataset contains 2,744 non-offensive and 1,818 offensive comments, with 1,543 containing vulgarities (including 437 non-offensive vulgar comments) and targets split across Group (869), Individual (572), Other (275), and multi-target (68). Inter-annotator agreement reached Krippendorff's Alpha of 0.49, comparable to related crowdsourcing work. Published at Findings of ACL 2024.

## Paper Outline

1. Introduction - Multidimensional content moderation, importance of targets in offensive statements, Austrian cultural/linguistic context
2. Related Work - English span-level annotations, comprehensive table of 14 German offensiveness datasets
3. Dataset Creation - DerStandard source, Perspective API pre-filtering, annotation campaign with students, class definitions (Offensive, Not Offensive, Vulgarity, Target Group/Individual/Other), data aggregation, inter-annotator agreement, cross-validation splits
4. Experiments - Fine-tuned language models (5 German BERT/Electra variants), prompted LLMs (GPT-3.5, GPT-4, LeoLM, Mistral) in zero-shot and five-shot scenarios
5. Conclusion - Summary of findings
6. Ethics Statement - Annotator risks, compensation, publication risks
7. Limitations - Time span, subjectivity, experimental scope

## Methods Summary

The evaluation compares fine-tuned smaller language models against LLMs in zero-shot and five-shot settings across three tasks: binary offensiveness classification (sequence classification), vulgarity extraction (token classification), and target extraction (token classification). Fine-tuned models include BERTde, BERT-dbmdz, GBERT-base, GELECTRA, and GBERT-large, all using default hyperparameters with learning rate 5e-5, weight decay 0.01, 200 warm-up steps, batch size 8, and early stopping at patience 3. For offensiveness classification, the article title is concatenated as context. LLM evaluation uses GPT-3.5 (gpt-3.5-turbo-1106), GPT-4 (gpt-4-1106-preview), LeoLM 7B Chat, and Mistral 7B in zero-shot and five-shot configurations. GPT models use JSON-format responses for multitask prediction; LeoLM and Mistral use binary logit comparison due to inability to produce consistent JSON. All results are reported as mean F1 scores with standard deviations from ten-fold cross-validation.

## Results Summary

GPT-4 in five-shot mode achieves the highest binary offensiveness F1 of 0.76 (macro 0.81), outperforming all fine-tuned models including GBERT-large at 0.73 (macro 0.75). For vulgarity detection at the token level, fine-tuned models substantially outperform LLMs, with GBERT-large achieving 0.71 binary F1 and 0.85 macro F1 compared to GPT-3.5's 0.43/0.70 and GPT-4's 0.41/0.70 in five-shot mode. This disparity is attributed to the lexical nature of vulgarity detection and the prevalence of Austrian dialect vulgarities rarely encountered in LLM training data. For target extraction, micro F1 scores are generally low (0.17-0.24) across all models due to high prevalence of the negative class, with fine-tuned models slightly outperforming LLMs. Open-source LLMs (LeoLM, Mistral) perform notably worse than GPT models, with Mistral achieving only 0.30 binary F1 in zero-shot mode. The results suggest a hybrid approach where fine-tuned models mark vulgarities and GPT-4 handles overall offensiveness classification could improve performance.

## Conclusions

AustroTox fills a critical gap as the first German dataset with token-level offensive language annotations, providing resources for more interpretable toxicity detection in the Austrian German dialect. The complementary strengths of LLMs (superior offensiveness detection) and fine-tuned models (superior dialect-specific vulgarity detection) suggest that hybrid approaches combining both may yield optimal performance. Key limitations include the narrow time window (one week in November 2021, with COVID-19 topic overrepresentation), moderate inter-annotator agreement (alpha=0.49), the subjective nature of offensiveness annotation with a large pool of minimally trained annotators, and the non-exhaustive experimental evaluation that excluded larger German-specific models like GELECTRA-large and did not conduct hyperparameter search. Future work aims to deliver more comprehensive evaluation and nuanced analysis of factors influencing the performance difference between fine-tuning and zero-shot classification.

## Artifact Contributions

- **AustroTox Dataset**: 4,562 Austrian German comments with binary offensiveness labels, token-level span annotations for vulgarities and offensive targets, disaggregated annotator labels, and predetermined cross-validation splits (https://www.pia.wien/austrotox/)
- **Evaluation Code**: Code for fine-tuned and LLM evaluation experiments (https://web.ds-ifs.tuwien.ac.at/austrotox/)
- **Annotation Guidelines**: Detailed guidelines with translated examples covering Offensive, Incite to Hate/Violence, and None classes with span annotation instructions

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First token-level offensive language annotations for non-English (Austrian German dialect), evaluating both LLMs and fine-tuned models.

## Tags

