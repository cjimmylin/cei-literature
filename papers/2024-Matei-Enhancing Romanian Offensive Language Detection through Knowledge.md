---

































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0523
type: preprint
short_title: "Enhancing Romanian Offensive Language Detection through Knowledge Distillation, Multi-Task Learning, and Data Augmentation"
year: 2024
first_author: "[[Vlad-Cristian Matei]]"
last_author: "[[Dumitru-Clementin Cercel]]"
authors: Vlad-Cristian Matei; Iulian-Marius Tăiatu; Răzvan-Alexandru Smădu; Dumitru-Clementin Cercel
url: "https://arxiv.org/abs/2409.20498"
external_pdf: "https://arxiv.org/pdf/2409.20498.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge.md"
local_pdf: "[[PDFs/2024/2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Romanian"
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
LLM_assessed: "BERT, GPT-2"
DATA_URL: "https://huggingface.co/datasets/readerbench/ro-offense"
tags: 
abstract: "This paper highlights the significance of natural language processing (NLP) within artificial intelligence, underscoring its pivotal role in comprehending and modeling human language. Recent advancements in NLP, particularly in conversational bots, have garnered substantial attention and adoption among developers. This paper explores advanced methodologies for attaining smaller and more efficient NLP models."
CONFERENCE: "Preprint"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: No
data_description: "Annotated dataset"
data_metrics: "Not specified"
ethics_perspective: "Toxicity & Hate Speech"
---
# Enhancing Romanian Offensive Language Detection through Knowledge Distillation, Multi-Task Learning, and Data Augmentation

## Authors

[[Vlad-Cristian Matei]], [[Iulian-Marius Tăiatu]], [[Răzvan-Alexandru Smădu]], [[Dumitru-Clementin Cercel]]

## Metadata

**Authors:** Vlad-Cristian Matei, Iulian-Marius Tăiatu, Răzvan-Alexandru Smădu, Dumitru-Clementin Cercel

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** Romanian

**Benchmark:** RO-Offense

## Links

- **arXiv:** https://arxiv.org/abs/2409.20498
- **Code/Data:** https://huggingface.co/datasets/readerbench/ro-offense

## Abstract

Develops automatic offensive language detection for Romanian using Transformer-based models with knowledge distillation, data augmentation, and multi-task learning. Uses RO-Offense dataset (12,447 annotated records: Profanity 13%, Insult 23%, Abuse 28%, Other 36%).

## Summary

This paper develops advanced methods for automatic offensive language detection in Romanian, addressing the challenges of limited dataset availability and model efficiency for low-resource languages. The authors employ Transformer-based BERT models enhanced through three key approaches: knowledge distillation to transfer information from large models to smaller architectures, data augmentation using RoGPT-2 and techniques like ASDA and MixUp, and multi-task learning incorporating sentiment analysis, emotion analysis, and sexist language detection tasks. Experiments on the RO-Offense dataset (12,447 annotated records across four categories: Profanity, Insult, Abuse, and Other) demonstrate improved performance while maintaining model efficiency.

## Data Description

Develops automatic offensive language detection for Romanian using Transformer-based models with knowledge distillation, data augmentation, and multi-task learning. Uses RO-Offense dataset with 12,447 annotated records across four categories: Profanity (13%), Insult (23%), Abuse (28%), Other (36%).


## Detailed Summary

This paper develops advanced methodologies for automatic offensive language detection in Romanian, addressing challenges of limited dataset availability and computational efficiency for low-resource languages. The work systematically explores three optimization approaches: (1) knowledge distillation (KD) to transfer knowledge from larger BERT models to smaller architectures, (2) multiple data augmentation techniques including generative text via RoGPT-2, ASDA (Auxiliary Sentence-based Data Augmentation), MixUp at encoder and sentence levels, and Noisy Student training, and (3) multi-task learning (MTL) integrating three auxiliary tasks (sentiment analysis, emotion analysis, and sexist language detection) with KD and teacher annealing. The primary dataset is RO-Offense, containing 12,447 annotated Romanian text records with four categories: Insult, Profanity, Abuse, and Other.

## Paper Outline

1. Introduction - Challenges of offensive language detection in Romanian
2. Related Work - Offensive language detection, transfer learning, knowledge distillation
3. Method - Fine-tuning BERT, data augmentation, multi-task learning model, knowledge distillation with teacher annealing
4. Experiments - Datasets, experimental setup, results
5. Conclusion

## Methods Summary

The baseline is a fine-tuned Romanian BERT model for four-class offensive language classification. Knowledge distillation transfers information from a larger teacher model to a student model using soft label distributions with temperature scaling. Data augmentation employs four techniques: RoGPT-2 generative text (providing 70% context for controlled generation), ASDA using conditional masked language modeling, MixUp at encoder and sentence levels for interpolating representations, and Noisy Student with word-drop and sentence-drop. The MTL architecture uses shared BERT lower layers with task-specific classification heads for the primary task plus three auxiliary tasks (sentiment, emotion, sexist language), optimized jointly with a combined multi-task loss function.

## Results Summary

Combining knowledge distillation with multi-task learning and teacher annealing achieves the best overall performance for Romanian offensive language detection. Data augmentation techniques, particularly RoGPT-2 generative text and MixUp, improve model robustness by introducing controlled variations. The multi-task approach benefits from correlated auxiliary tasks (sentiment, emotion, sexist language), enabling the model to learn shared representations that capture nuanced aspects of offensive discourse. An ablation study demonstrates the individual and combined contributions of each method.

## Conclusions

The combination of knowledge distillation, multi-task learning, and data augmentation provides a viable approach for building efficient offensive language detection systems in low-resource languages like Romanian. The work demonstrates that leveraging multiple correlated datasets and transfer learning techniques can compensate for limited training data availability, and that model efficiency can be maintained while improving detection accuracy.

## Artifact Contributions

- **RO-Offense dataset**: 12,447 annotated Romanian offensive language records (available at https://huggingface.co/datasets/readerbench/ro-offense)
- **MTL+KD framework**: Combined multi-task learning and knowledge distillation architecture for Romanian offensive language detection
- **Data augmentation pipeline**: Integration of RoGPT-2, ASDA, MixUp, and Noisy Student techniques for Romanian text

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Advances Romanian offensive language detection. RO-Offense is the largest public Romanian dataset for offensive discourse analysis.

## Tags

