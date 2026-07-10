---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0479
type: preprint
short_title: "NorBench: A Benchmark for Norwegian Language Models"
year: 2025
first_author: "[[Various (LTG Oslo)]]"
last_author: "[[Various (LTG Oslo)]]"
authors: "Various (LTG Oslo)"
url: "https://arxiv.org/abs/2305.03880"
external_pdf: "https://arxiv.org/pdf/2305.03880.pdf"
publication: "arXiv / NoDaLiDa 2023"
CONF-CC: "NoDaLiDa 2023"
pdf_extract: "PDF Extracts/2023/2023-Oslo-NorBench A Benchmark for Norwegian Language Models.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Oslo-NorBench A Benchmark for Norwegian Language Models.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Norwegian
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
LLM_assessed: NA
DATA_URL: "https://github.com/ltgoslo/NorBench"
tags: 
abstract: "We present NorBench: a streamlined suite of NLP tasks and probes for evaluating Norwegian language models (LMs) on standardized data splits and evaluation metrics. We also introduce a range of new Norwegian language models (both encoder and encoder-decoder based). Finally, we compare and analyze their performance, along with other existing LMs, across the different benchmark tests of NorBench."
research_topic: "Machine Learning"
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
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
is_eval: Yes
is_dataset: No
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
---
# NorBench: A Benchmark for Norwegian Language Models

## Authors

[[Various (LTG Oslo)]]

## Metadata

**Authors:** Various (LTG Oslo)

**Year:** 2023

**Type:** preprint

**Venue:** arXiv / NoDaLiDa 2023

**Languages:** Norwegian

**Benchmark:** NorBench

## Links

- **arXiv:** https://arxiv.org/abs/2305.03880
- **Code/Data:** https://github.com/ltgoslo/norbench

## Abstract

Streamlined NLP benchmark suite for Norwegian LMs with standardized data splits and evaluation metrics. Includes diagnostic tasks probing gender-bias and toxic language affinity in language models.

## Summary

This paper introduces NorBench, a streamlined suite of NLP tasks and diagnostic probes for evaluating Norwegian language models on standardized data splits and metrics. The benchmark encompasses nine datasets covering morpho-syntactic tasks, named entity recognition, sentiment analysis, linguistic acceptability, question answering, and machine translation, along with diagnostic tasks that probe gender bias and toxic language affinity using the HONEST metric adapted for Norwegian. The authors develop new state-of-the-art Norwegian language models (NorBERT3 encoder and NorT5 encoder-decoder) and evaluate them alongside existing models (NB-BERT, ScandiBERT, mBERT, XLM-RoBERTa). Results show that training on curated Norwegian corpora outperforms simple concatenation of all available resources, and that joint modeling of both Norwegian written varieties (Bokmål and Nynorsk) works effectively.

## Data Description

NorBench benchmark suite for Norwegian language models with standardized data splits and evaluation metrics across multiple NLP tasks, including diagnostic probes for gender bias and toxic language.


## Detailed Summary

This paper presents NorBench, a streamlined suite of NLP tasks and diagnostic probes for systematically evaluating and comparing Norwegian language models on standardized data splits and evaluation metrics. Developed by the Language Technology Group at the University of Oslo, NorBench encompasses nine datasets covering morpho-syntactic token-level tasks (UPOS, UFeats, lemmatization, dependency parsing using Universal Dependencies treebanks), named entity recognition (NorNE dataset with 8 entity types), sentiment analysis at document, sentence, and target levels (using NoReC), linguistic acceptability (NoCoLA), question answering (NorQuAD with 4,752 manually created QA pairs), and Bokmal-Nynorsk machine translation. Critically, NorBench includes diagnostic tasks that probe gender bias in occupations using normative and descriptive bias scores, and assess harmfulness of sentence completions using the HONEST metric adapted for Norwegian. The authors also introduce NorBERT3 (encoder, 15M-353M parameters) and NorT5 (encoder-decoder) as new state-of-the-art Norwegian language models trained on approximately 25 billion word tokens from multiple Norwegian corpora.

## Paper Outline

1. Introduction - Motivation for standardized Norwegian LM benchmarking
2. NorBench Task Descriptions - Bokmal/Nynorsk varieties, morpho-syntactic tasks, sentiment analysis, linguistic acceptability, QA, machine translation, diagnostics for harmful predictions
3. NorBench Baseline Methodology - Joint UD model, text classification, sequence labeling, QA, MT, gender-bias and harmfulness probing
4. New Norwegian Language Models - Training corpora (Wikipedia, NBDigital, NAK, NCC, mC4 totaling ~25B words), NorBERT3 architecture, NorT5, pre-training details
5. Benchmarking Results - Model comparison, gender-bias evaluation, harmfulness scores, corpora comparison
6. Related Work - Comparison with ScandEval and other benchmarks
7. Future Work - Planned extensions
8. Summary

## Methods Summary

NorBERT3 models (x-small 15M, small 40M, base 123M, large 353M parameters) follow the LTG-BERT training recipe with span masking, NormFormer layer normalization, and disentangled attention. Pre-training uses 250,000 steps with batch size 8,192 on 16-512 AMD MI250X GPUs, trained on concatenated Norwegian corpora (~25B words) after paragraph-level deduplication. NorT5 extends the encoder-only architecture to full encoder-decoder for generative tasks. Fine-tuning uses task-specific hyperparameters (e.g., AdamW optimizer, cosine learning rate schedules). Gender bias is probed using templates with masked gendered head-words and occupation predicates, computing normative (equal representation target) and descriptive (real-world distribution alignment) scores. Harmfulness is measured via HONEST scores mapping top-k completions to the HurtLex offensive word lexicon.

## Results Summary

NorBERT3-large (353M parameters) achieves the highest scores across most NorBench tasks (99.1 UPOS accuracy, 91.4 NER F1, 79.2 Doc SA, 88.7 NorQuAD F1), outperforming NB-BERT-large, XLM-R-large, and all previous Norwegian models. Even the small 40M NorBERT3 is competitive with much larger models. For encoder-decoder models, NorT5-large outperforms mT5 and North-T5 variants across all tasks. On gender bias, all models show higher descriptive than normative scores, with models better at identifying female-dominated occupations but poor at gender-neutral ones. NorBERT3 and NorT5 models achieve very low HONEST harmfulness scores compared to older Norwegian models; XLM-R-base shows the worst top-1 harmfulness while NorBERT1 is worst across broader top-k. Corpora comparison reveals that simple concatenation is reasonable but not always optimal, with NAK-only training yielding improved sentiment analysis performance.

## Conclusions

NorBench provides a dynamic, publicly available benchmarking resource with standardized evaluation workflows, pre-defined data splits, and an online leaderboard. The NorBERT3 models demonstrate that curated Norwegian-specific training outperforms simple resource concatenation. Diagnostic probes reveal that smaller models tend to show more balanced gender representation normatively, and that training corpus composition significantly affects bias profiles. Future work includes adding coreference resolution (NARC), negation resolution (NoReCneg), and prompt-based few-shot evaluation for generative models.

## Artifact Contributions

- **NorBench Benchmark Suite**: Standardized Norwegian NLP benchmark with 9 datasets, evaluation scripts, and leaderboard (https://github.com/ltgoslo/norbench)
- **NorBERT3 Models**: Family of Norwegian masked LMs in 4 sizes (15M-353M parameters)
- **NorT5 Models**: Norwegian encoder-decoder models for generative tasks
- **NoCoLA Dataset**: Norwegian Corpus of Linguistic Acceptability
- **NorQuAD Dataset**: Norwegian extractive QA dataset with 4,752 question-answer pairs

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Norwegian LM benchmark that explicitly includes gender-bias and toxicity probing tasks.

## Tags

