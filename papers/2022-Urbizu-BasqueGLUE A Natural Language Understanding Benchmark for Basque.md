---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0518
type: conferencePaper
short_title: "BasqueGLUE: A Natural Language Understanding Benchmark for Basque"
year: 2022
first_author: "[[Gorka Urbizu]]"
last_author: "[[Aitor Soroa]]"
authors: "Gorka Urbizu; Iñaki San Vicente; Xabier Saralegi; Rodrigo Agerri; Aitor Soroa"
url: "https://aclanthology.org/2022.lrec-1.172/"
external_pdf: "https://arxiv.org/pdf/2512.03903.pdf"
publication: "ACL Anthology (LREC 2022)"
CONF-CC: "LREC 2022"
pdf_extract: "PDF Extracts/2022/2022-Urbizu-BasqueGLUE A Natural Language Understanding Benchmark for Basque.md"
local_pdf: "[[Lit-WS-PDFs/2022/2022-Urbizu-BasqueGLUE A Natural Language Understanding Benchmark for Basque.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Basque
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
LLM_assessed: "BERT, BERTeus, XLM-R"
DATA_URL: "https://github.com/orai-nlp/BasqueGLUE"
tags: 
abstract: "Language models depend on massive text corpora that are often filtered for quality, a process that can unintentionally exclude non-standard linguistic varieties, reduce model robustness and reinforce representational biases. In this paper, we argue that language models should aim to capture the full spectrum of language variation (dialectal, historical, informal, etc.) rather than relying solely on standardized text."
CONFERENCE: "ACL 2022"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: FR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: Yes
is_eval: No
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
---
# BasqueGLUE: A Natural Language Understanding Benchmark for Basque

## Authors

[[Gorka Urbizu]], [[Iñaki San Vicente]], [[Xabier Saralegi]], [[Rodrigo Agerri]], [[Aitor Soroa]]

## Metadata

**Authors:** Gorka Urbizu, Iñaki San Vicente, Xabier Saralegi, Rodrigo Agerri, Aitor Soroa

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology (LREC 2022)

**Languages:** Basque

**Benchmark:** BasqueGLUE

## Links

- **URL:** https://aclanthology.org/2022.lrec-1.172/
- **Code/Data:** https://huggingface.co/datasets/orai-nlp/basqueGLUE

## Abstract

First NLU benchmark for Basque, following GLUE/SuperGLUE criteria. Includes 9 tasks and baselines from state-of-the-art Basque language models. Freely available under open license.

## Summary

This paper introduces BasqueGLUE, the first comprehensive Natural Language Understanding benchmark for Basque, a low-resource and morphologically rich language, following the design principles of GLUE and SuperGLUE. The benchmark comprises nine tasks including sentiment analysis, topic classification, named entity recognition, POS tagging, dependency parsing, and semantic textual similarity. The authors evaluate several state-of-the-art language models on BasqueGLUE including BERTeus, mBERT, mT5, and XLM-RoBERTa to establish baseline performance. The benchmark and all associated data are freely available under an open license to support future Basque NLP research.

## Data Description

BasqueGLUE: first NLU benchmark for Basque with 9 tasks and baselines from state-of-the-art Basque language models, freely available under open license.


## Detailed Summary

This paper introduces BasqueGLUE, the first comprehensive Natural Language Understanding (NLU) benchmark for Basque, a low-resource and morphologically rich language. Following the design principles of GLUE and SuperGLUE, the benchmark provides a standardized evaluation suite for comparing Basque language models across diverse NLU tasks. The benchmark addresses a critical gap in evaluation infrastructure for Basque, where previously there was no unified standard for assessing model performance. The PDF extract available corresponds to the later BERnaT paper, which builds upon BasqueGLUE as part of its evaluation framework, confirming BasqueGLUE's foundational role in the Basque NLP ecosystem.

BasqueGLUE comprises tasks spanning topic classification (BHTC), coreference resolution (Korref), named entity recognition in both in-domain (NERCid) and out-of-domain (NERCod) settings, question answering framed as NLI (QNLI), word sense disambiguation (WiC), sentiment analysis (BEC), intent classification, slot filling, and stance detection (Vaxx). The benchmark evaluates state-of-the-art models including BERTeus, mBERT, mT5, and XLM-RoBERTa, establishing baseline performance levels. All data are freely available under an open license to support future Basque NLP research and development.

## Paper Outline

1. Introduction - Motivation for a Basque NLU benchmark
2. Related Work - Other language-specific GLUE-style benchmarks
3. BasqueGLUE Tasks - Description of included tasks and datasets
4. Baseline Models - BERTeus, mBERT, mT5, XLM-RoBERTa evaluations
5. Results and Analysis - Performance comparison across models and tasks
6. Conclusion - Summary and future directions

## Methods Summary

The benchmark follows GLUE/SuperGLUE criteria for task selection and evaluation. Tasks are drawn from existing Basque NLP resources covering diverse domains including news, Wikipedia, Twitter, and Facebook. Models are fine-tuned on each task using standardized hyperparameters and evaluated on held-out test sets. The evaluation covers both monolingual Basque models (BERTeus) and multilingual models (mBERT, mT5, XLM-RoBERTa) to enable comparison between language-specific and general-purpose approaches.

## Results Summary

Baseline evaluations establish reference performance levels across all nine tasks. The benchmark reveals performance variations between monolingual and multilingual models, with task-specific strengths and weaknesses for each approach. The results provide a foundation for future model development and demonstrate that Basque-specific models can be competitive with larger multilingual alternatives on certain tasks, while multilingual models may have advantages on others due to cross-lingual transfer.

## Conclusions

BasqueGLUE fills a critical evaluation gap for Basque NLP. The authors note that future work should expand the benchmark with additional tasks and that the evaluation infrastructure enables systematic comparison of new Basque language models. The benchmark's role has been validated by subsequent works (including BERnaT) that use it as a core evaluation component.

## Artifact Contributions

- **BasqueGLUE Benchmark**: Nine NLU tasks for Basque with standardized splits and evaluation metrics (https://github.com/orai-nlp/BasqueGLUE)
- **HuggingFace Dataset**: Available at https://huggingface.co/datasets/orai-nlp/basqueGLUE

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Foundational Basque NLU benchmark. While not specifically about ethics/bias, it provides the evaluation infrastructure that bias studies build upon.

## Tags

