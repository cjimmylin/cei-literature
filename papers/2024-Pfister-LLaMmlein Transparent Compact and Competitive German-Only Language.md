---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0477
type: preprint
short_title: "LLaMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch"
year: 2024
first_author: "[[Jan Pfister]]"
last_author: "[[Andreas Hotho]]"
authors: Jan Pfister; Julia Wunderle; Andreas Hotho
url: "https://arxiv.org/abs/2411.11171"
external_pdf: "https://arxiv.org/pdf/2411.11171.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Pfister-LLaMmlein Transparent Compact and Competitive German-Only Language.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Pfister-LLaMmlein Transparent Compact and Competitive German-Only Language.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT"
DATA_URL: "https://professor-x.de/lm/LLaMmlein"
tags: 
abstract: "We transparently create two German-only decoder models, LLäMmlein 120M and 1B1, from scratch and publish them, along with training data, for the (German) NLP research community to use2. The model training involved several key steps, including data preprocessing/filtering, the creation of a German tokenizer, the training itself, as well as the evaluation of the final models on various benchmarks, also against existing models."
CONFERENCE: "Preprint"
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
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# LLaMmlein: Transparent, Compact and Competitive German-Only Language Models from Scratch

## Authors

[[Jan Pfister]], [[Julia Wunderle]], [[Andreas Hotho]]

## Metadata

**Authors:** Jan Pfister, Julia Wunderle, Andreas Hotho

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** German

## Links

- **arXiv:** https://arxiv.org/abs/2411.11171
- **Code/Data:** https://professor-x.de/lm/LLaMmlein

## Abstract

German-only decoder models (120M and 1B params) trained from scratch with custom tokenizer. Evaluated on SuperGLEBer benchmark; 120M model outperforms bert-base-german-cased by 14% on NLI. Fully transparent training pipeline.

## Summary

This paper presents LLäMmlein, the first fully transparent German-only language model family (120M and 1B parameters) trained from scratch with complete documentation of data preprocessing, tokenizer creation, training process, and evaluation. The authors filter and clean German data from RedPajama V2, create a custom 32k-token German tokenizer, and pretrain two autoregressive models while releasing incremental checkpoints to enable analysis of learning dynamics. Evaluation on the SuperGLEBer benchmark shows competitive performance against state-of-the-art models, with the 120M model outperforming bert-base-german-cased by 14% on natural language inference tasks, demonstrating that smaller, transparent, German-only models can achieve strong performance.

## Data Description

Releases two German-only decoder models (LLäMmlein 120M and 1B) trained from scratch, along with the filtered German training dataset derived from RedPajama V2. All training data, code, and intermediate checkpoints are made publicly available.


## Detailed Summary

This paper presents LLäMmlein, the first German-only language model family trained entirely from scratch with full transparency, comprising 120M and 1B parameter decoder models. The authors address the lack of reproducible, well-documented German LLMs by providing complete access to training data, code, model weights, and incremental checkpoints. The training pipeline involves cleaning and filtering German text from RedPajama V2 (yielding approximately 2.7 trillion tokens from head and middle quality partitions), creating a dedicated 32k-token German tokenizer optimized for fertility, and pretraining autoregressive models. Multiple checkpoints are evaluated on the SuperGLEBer benchmark throughout training to analyze learning dynamics and scaling effects, providing insights into when performance plateaus occur for different task types.

## Paper Outline

1. Introduction - Need for transparent German-only LLMs
2. Methodology - Dataset preprocessing, tokenizer fitting, model pretraining, evaluation
3. Tokenizer - German tokenizer creation and comparison with existing tokenizers
4. Training - Pre-training procedure, hyperparameters, checkpoint saving
5. Evaluation - SuperGLEBer benchmark, lm-evaluation-harness-de, downstream adaptations
6. Conclusion

## Methods Summary

The training data is derived from the German portion of RedPajama V2, filtered to head and middle quality partitions (approximately 2.7 trillion tokens before deduplication). A custom 32k-token German tokenizer is fitted on varying data amounts and compared against existing German tokenizers. Two autoregressive decoder models (120M and 1B parameters) are pretrained from scratch, with incremental checkpoints saved at equal intervals and analyzed using the SuperGLEBer benchmark. Models are evaluated on both the SuperGLEBer benchmark (29 German NLU tasks) and the lm-evaluation-harness-de (translated prompt-based few-shot QA tasks), and compared against existing German-capable models including multilingual and adapted models.

## Results Summary

Both LLäMmlein models perform competitively on the SuperGLEBer benchmark, consistently matching or surpassing models with similar parameter sizes. The 120M model notably outperforms bert-base-german-cased by 14% on natural language inference tasks. Model quality scales with size as expected, but performance improvements on some tasks plateau early during training, offering valuable insights into resource allocation for future models. The checkpoint analysis reveals task-specific learning dynamics, showing that some capabilities emerge early while others continue improving throughout training.

## Conclusions

LLäMmlein establishes a transparent foundation for understanding, improving, and expanding the German LLM ecosystem. By releasing all components (model weights, training data, code, incremental checkpoints), the work enables systematic analysis of the relationship between training data and model outputs, addressing the critical lack of traceability in existing German-capable models. The authors subsequently released a 7B model as well.

## Artifact Contributions

- **LLäMmlein models**: 120M and 1B (and later 7B) German-only decoder models
- **German tokenizer**: Custom 32k-token tokenizer optimized for German text fertility
- **Training data**: Cleaned and filtered German subset of RedPajama V2
- **Incremental checkpoints**: Full checkpoint history for learning dynamics analysis
- **Code and documentation**: https://professor-x.de/lm/LLaMmlein

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** German-only LLMs evaluated on German benchmarks, contributing to understanding of German language model capabilities.

## Tags

