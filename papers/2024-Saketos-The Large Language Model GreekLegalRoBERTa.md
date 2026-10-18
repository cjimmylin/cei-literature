---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0532
type: preprint
short_title: "The Large Language Model GreekLegalRoBERTa"
year: 2024
first_author: "[[Saketos, Vasileios]]"
last_author: "[[Koubarakis, Manolis]]"
authors: "Saketos, Vasileios; Pantazi, Despina-Athanasia; Koubarakis, Manolis"
authors_incomplete: false
url: "https://arxiv.org/abs/2410.12852"
external_pdf: "https://arxiv.org/pdf/2410.12852.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2024/2024-Saketos-The Large Language Model GreekLegalRoBERTa.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Saketos-The Large Language Model GreekLegalRoBERTa.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Greek
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
newtags: 
LLM_assessed: BERT
DATA_URL: "https://github.com/AI-team-UoA/GreekLegalRoBERTa"
tags: 
abstract: "We develop four versions of GreekLegalRoBERTa, which are four large language models trained on Greek legal and nonlegal text. We show that our models surpass the performance of GreekLegalBERT, Greek- LegalBERT-v2, and GreekBERT in two tasks involving Greek legal documents: named entity recognition and multiclass legal topic classiﬁcation. We view our work as a contribution to the study of domain-speciﬁc NLP tasks in low-resource languages, like Greek, using modern NLP techniques and..."
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "NLP & Representation Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: SE
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# The Large Language Model GreekLegalRoBERTa

## Authors

[[Saketos, Vasileios]], [[Pantazi, Despina-Athanasia]], [[Koubarakis, Manolis]]

## Metadata

**Authors:** Saketos, Vasileios; Pantazi, Despina-Athanasia; Koubarakis, Manolis

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

## Links

- **arXiv:** https://arxiv.org/abs/2410.12852

## Abstract

Four versions of RoBERTa-based language models trained on Greek legal and non-legal text. Surpasses performance of GreekLegalBERT and GreekBERT in NER and multi-class legal topic classification. Contribution to domain-specific NLP tasks in low-resource languages using modern NLP techniques.

## Summary

This paper presents four versions of GreekLegalRoBERTa, domain-specific large language models trained on Greek legal and non-legal text for improving NLP performance in the low-resource Greek legal domain. The models are trained on diverse Greek legal sources including the Nomothesia platform, Greek Parliament Proceedings, European Parliament Proceedings, EU legislation, and general corpora (OSCAR). Evaluation on two key tasks (named entity recognition using GreekLegalNER dataset and multi-class legal topic classification using GreekLegalCode dataset) shows that the GreekLegalRoBERTa models surpass state-of-the-art GreekLegalBERT-v2, GreekLegalBERT, and GreekBERT, achieving improvements of 1.2 percentage points in NER micro average and 0.67-0.89 points across legal topic classification tasks.

## Data Description

Four versions of GreekLegalRoBERTa models trained on Greek legal text, with code, models, and datasets for NER and legal topic classification.


## Detailed Summary

This paper presents four versions of GreekLegalRoBERTa, domain-specific language models for the Greek legal domain built on the RoBERTa architecture. The models are trained on a combination of Greek legal text from the Nomothesia platform (Greek legislation as linked data), Greek Parliament Proceedings, the Greek portion of European Parliament Proceedings Parallel Corpus, Greek EU legislation, the Raptarchis legal collection, and general Greek text from OSCAR. The four model variants use different combinations of these training corpora to investigate the impact of domain-specific vs. general text on downstream performance. The work demonstrates that focused, language-specific models can outperform larger multilingual models on domain-specific tasks, contributing to NLP research for low-resource languages.

## Paper Outline

1. Introduction - Motivation for Greek legal domain LLMs
2. Related Work - Monolingual Greek models, generative models, legal benchmarks (LEGALBENCH, LEXTREME)
3. The GreekLegalRoBERTa Models - Four model configurations, training data sources
4. Evaluation - Named entity recognition (GreekLegalNER), multi-class legal topic classification (GreekLegalCode)
5. Conclusion - Limitations and future work

## Methods Summary

The authors develop four RoBERTa-based models using different training corpus combinations drawn from six sources: Nomothesia platform legislation, Greek Parliament Proceedings, European Parliament Proceedings (Greek portion), EU legislation (Greek part), Raptarchis legal collection, and OSCAR general corpus. The models are evaluated on two tasks from the LEXTREME benchmark: (1) GreekLegalNER for named entity recognition in Greek legal documents, originally constructed from Nomothesia platform data, and (2) GreekLegalCode for multi-class legal topic classification across three granularity levels (volume, chapter, subject) using 47k legal documents.

## Results Summary

GreekLegalRoBERTa models surpass all previous models including GreekLegalBERT, GreekLegalBERT-v2, and GreekBERT on both tasks. In NER, improvements of 1.2 points in micro average and 1.4 points in weighted average over GreekLegalBERT-v2 are achieved. In legal topic classification, improvements of 0.12 points (volume), 0.89 points (chapter), and 0.67 points (subject) are recorded. The results demonstrate that concentrating on a single language enables development of models more effective than the multilingual ones used in broader benchmarks like LEXTREME, where XLM-RoBERTa was previously the most effective model.

## Conclusions

Focused, language-specific models using the RoBERTa architecture can outperform both general-purpose monolingual models and multilingual models on domain-specific tasks for low-resource languages like Greek. The authors make models, datasets, and code publicly available, and note that the work complements the recent development of the generative Meltemi LLM for Greek. Future work includes exploring RAG architectures for legal question answering.

## Artifact Contributions

- **GreekLegalRoBERTa models**: Four RoBERTa variants trained on Greek legal and general text (available at https://huggingface.co/AI-team-UoA)
- **Code**: https://github.com/AI-team-UoA/GreekLegalRoBERTa
- **State-of-the-art results**: New best performance on GreekLegalNER and GreekLegalCode benchmarks

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Greek legal domain NLP model with evaluation on legal text processing tasks. Relevant to fairness in legal NLP and domain-specific evaluation for Greek.

## Tags

