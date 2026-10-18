---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0469
type: preprint
short_title: "Digital Guardians: Can GPT-4, Perspective API, and Moderation API reliably detect hate speech in reader comments of German online newspapers?"
year: 2025
first_author: "[[Weber, Manuel]]"
last_author: "[[Mandl, Peter]]"
authors: "Weber, Manuel; Huber, Moritz; Auch, Maximilian; Döschl, Alexander; Keller, Max-Emanuel; Mandl, Peter"
authors_incomplete: false
url: "https://arxiv.org/abs/2501.01256"
external_pdf: "https://arxiv.org/pdf/2501.01256.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: German
cultures_nationalities_list: German
languages_list: German
religious_values: N/A
rv_islam: 10
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
newtags: 
LLM_assessed: GPT-4o
DATA_URL: NA
tags: 
abstract: "In recent years, toxic content and hate speech have become widespread phenomena on the internet. Moderators of online newspapers and forums are now required, partly due to legal regulations, to carefully review and, if necessary, delete reader comments. This is a labor-intensive process. Some providers of large language models already offer solutions for automated hate speech detection or the identification of toxic content."
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: DE
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Dataset for hate speech detection"
data_metrics: "Not specified"
---
# Digital Guardians: Can GPT-4, Perspective API, and Moderation API reliably detect hate speech in reader comments of German online newspapers?

## Authors

[[Weber, Manuel]], [[Huber, Moritz]], [[Auch, Maximilian]], [[Döschl, Alexander]], [[Keller, Max-Emanuel]], [[Mandl, Peter]]

## Metadata

**Authors:** Weber, Manuel; Huber, Moritz; Auch, Maximilian; Döschl, Alexander; Keller, Max-Emanuel; Mandl, Peter

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** German

## Links

- **arXiv:** https://arxiv.org/abs/2501.01256

## Abstract

Compares GPT-4o, Perspective API, and Moderation API for detecting hate speech in German newspaper comments using HOCON34k dataset. GPT-4o outperforms both other tools across zero-shot, one-shot, and few-shot prompting.

## Summary

This paper evaluates three automated hate speech detection systems—GPT-4o, Google's Perspective API, and OpenAI's Moderation API—on German newspaper reader comments using the HOCON34k dataset. Testing across zero-shot, one-shot, and few-shot prompting scenarios, the study finds that GPT-4o consistently outperforms both commercial APIs in detecting hate speech in German content. The research addresses the practical need for automated content moderation in German online newspapers where manual review is labor-intensive and legally required.

## Data Description

Compares GPT-4o, Perspective API, and Moderation API for detecting hate speech in German newspaper reader comments using the HOCON34k dataset. GPT-4o outperforms both commercial APIs across zero-shot, one-shot, and few-shot prompting. Evaluates existing models on existing dataset rather than introducing new data.


## Detailed Summary

This paper compares the effectiveness of three automated hate speech detection solutions -- OpenAI's GPT-4o, Google Jigsaw's Perspective API, and OpenAI's Moderation API -- on German online newspaper reader comments using the HOCON34k dataset. The HOCON34k dataset contains 34,223 annotated reader comments from German online newspapers, of which a 1,592-sample annotated test set is used for evaluation. Each solution uses a pretrained model with no fine-tuning or additional training. For GPT-4o, three different prompting strategies are tested: Zero-Shot, One-Shot, and Few-Shot approaches. The study uses a combined metric of Matthews Correlation Coefficient (MCC) and F2-score for comparison, with a fine-tuned GBERT model from the HOCON34k project serving as the baseline. The comprehensive hate speech definition follows guidelines from online newspaper behavior codes, covering racist, sexist, homophobic, antisemitic, extremist, vulgar, and threatening content.

## Paper Outline

1. Introduction - Need for automated hate speech detection in German online newspapers
2. Related Work - LLM-based hate speech detection; Perspective API and Moderation API evaluations
3. Methodology - Test setup, prompting strategies, evaluation metrics
4. Dataset - HOCON34k description and test set selection
5. Experiments - GPT-4o (Zero/One/Few-Shot), Perspective API, Moderation API
6. Results - Performance comparison using MCC, F2-score, and combined metric
7. Discussion - Practical implications for content moderation
8. Conclusion

## Methods Summary

The evaluation uses a 1,592-sample annotated test set from HOCON34k. GPT-4o is tested with three prompting strategies: Zero-Shot (no examples), One-Shot (one example), and Few-Shot (multiple examples). The Perspective API and Moderation API are queried with their default configurations. A fine-tuned GBERT model serves as the baseline. Performance is measured using F2-score (emphasizing recall over precision for hate speech detection), MCC (handling class imbalance), and a combined metric of both. All solutions use pretrained models as of June 2024 with no additional fine-tuning.

## Results Summary

GPT-4o outperforms both the Perspective API and Moderation API across all prompting configurations. GPT-4o also exceeds the HOCON34k fine-tuned GBERT baseline by approximately 5 percentage points on the combined MCC/F2-score metric. Few-Shot prompting generally improves performance over Zero-Shot approaches. The Perspective API and Moderation API, while convenient commercial solutions, do not match GPT-4o's performance on German-language hate speech detection, though previous studies noted the Perspective API performed relatively better for German compared to other tools.

## Conclusions

The study demonstrates that GPT-4o represents a viable and effective tool for automated hate speech detection in German online newspaper comments, outperforming both specialized commercial APIs and fine-tuned baseline models without any task-specific training. The findings have practical implications for content moderation in compliance with EU Digital Services Act requirements, suggesting that general-purpose LLMs with appropriate prompting can serve as effective digital guardians for German-language content.

## Artifact Contributions

- **Evaluation Results:** Comprehensive comparison of GPT-4o, Perspective API, and Moderation API on German hate speech detection using the HOCON34k benchmark

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Evaluates commercial LLM and API-based hate speech detection capabilities specifically for German content.

## Tags

