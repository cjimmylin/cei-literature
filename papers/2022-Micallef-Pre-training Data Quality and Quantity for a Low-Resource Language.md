---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0548
type: conferencePaper
short_title: "Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and BERT Models for Maltese"
year: 2022
first_author: "[[Micallef, Kurt]]"
last_author: "[[Borg, Claudia]]"
authors: "[[Micallef, Kurt]]; [[Gatt, Albert]]; [[Tanti, Marc]]; [[Plas, Lonneke van der]]; [[Borg, Claudia]]"
authors_incomplete: false
url: "https://aclanthology.org/2022.deeplo-1.10/"
external_pdf: "https://arxiv.org/pdf/2205.10517.pdf"
publication: "ACL Anthology / DeepLo 2022"
pdf_extract: "PDF Extracts/2022/2022-Micallef-Pre-training Data Quality and Quantity for a Low-Resource Language.md"
local_pdf: "[[PDFs/2022/2022-Micallef-Pre-training Data Quality and Quantity for a Low-Resource Language.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Maltese"
languages_list: Maltese
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT, mBERT"
DATA_URL: "https://huggingface.co/MLRS/BERTu"
tags: 
abstract: "Multilingual language models such as mBERT have seen impressive cross-lingual transfer to a variety of languages, but many languages remain excluded from these models. In this paper, we analyse the effect of pre-training with monolingual data for a low-resource language that is not included in mBERT – Maltese – with a range of pre-training set ups. We conduct evaluations with the newly pretrained models on three morphosyntactic tasks – dependency parsing, part-of-speech tagging, and..."
research_topic: "NLP & Representation Learning"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach text corpus"
data_metrics: "Not specified"
CONFERENCE: "ACL 2022"
---
# Pre-training Data Quality and Quantity for a Low-Resource Language: New Corpus and BERT Models for Maltese

## Authors

[[Micallef, Kurt]], [[Gatt, Albert]], [[Tanti, Marc]], [[Plas, Lonneke van der]], [[Borg, Claudia]]

## Metadata

**Authors:** Micallef, Kurt; Gatt, Albert; Tanti, Marc; Plas, Lonneke van der; Borg, Claudia

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology / DeepLo 2022

**Languages:** Maltese

## Links

- **arXiv:** https://arxiv.org/abs/2205.10517
- **URL:** https://aclanthology.org/2022.deeplo-1.10/
- **Code/Data:** https://huggingface.co/MLRS/BERTu

## Abstract

Develops BERTu, a monolingual BERT model for Maltese, and mBERTu. Trained on Korpus Malti v4.0. Achieves state-of-the-art despite smaller corpus. Foundation for downstream bias evaluation in Maltese.

## Summary

This paper presents BERTu, a monolingual BERT model for Maltese (a low-resource Semitic language not included in mBERT), and mBERTu (a further pre-trained multilingual BERT variant), both trained on the newly created Korpus Malti v4.0 corpus. The authors systematically investigate the effects of pre-training data quality, quantity, and domain diversity on downstream task performance across dependency parsing, POS tagging, named entity recognition, and sentiment analysis. Results show that using a mixture of domains outperforms Wikipedia-only training, and that BERTu achieves state-of-the-art performance despite the corpus being considerably smaller than those used for high-resource languages, with BERTu generally outperforming mBERTu especially on higher-level tasks.

## Data Description

BERTu and mBERTu models for Maltese trained on Korpus Malti v4.0 corpus. Evaluates monolingual BERT (BERTu) trained from scratch versus further pre-trained multilingual BERT (mBERTu) on dependency parsing, POS tagging, NER, and sentiment analysis for low-resource Maltese language.


## Detailed Summary

This paper presents BERTu, a monolingual BERT model for Maltese -- a low-resource Semitic language not included in multilingual BERT (mBERT) -- along with mBERTu, a further pre-trained variant of mBERT adapted for Maltese. Both models are trained on the newly created Korpus Malti v4.0, a Maltese text corpus compiled from multiple domains. The study systematically investigates how pre-training data quality (domain diversity), quantity, and source affect downstream task performance. The authors find that using a mixture of pre-training domains is often superior to using Wikipedia text alone, and that even a fraction of the full corpus produces significant performance gains over Wikipedia-only models.

The models are evaluated on four downstream tasks: dependency parsing, part-of-speech tagging, named entity recognition, and sentiment analysis. Despite the Maltese corpus being considerably smaller than those typically used for high-resource languages, BERTu achieves state-of-the-art performance across all tasks. On average, BERTu outperforms or performs competitively with mBERTu, with the largest gains observed for higher-level semantic tasks like sentiment analysis. The paper addresses the "curse of multilinguality" -- the phenomenon where multilingual models must share their limited capacity across many languages, resulting in sub-optimal representations for each individual language. For Maltese, which uses a unique writing system (Latin-based with Semitic-origin characters), multilingual models are particularly disadvantaged due to poor tokenization coverage.

## Paper Outline

1. Introduction - Low-resource language model challenges
2. Related Work - Monolingual vs. multilingual models, low-resource NLP
3. Data - Korpus Malti v4.0 creation and characteristics
4. Pre-training Setup - BERTu and mBERTu configurations
5. Experiments - Evaluation on four downstream tasks
6. Results - Data quality, quantity, and domain effects
7. Conclusion

## Methods Summary

BERTu is a monolingual BERT-BASE model trained from scratch on Korpus Malti v4.0 with a custom Maltese-specific WordPiece vocabulary. mBERTu extends the existing multilingual BERT with additional pre-training on the Maltese corpus. The study conducts ablation experiments varying: (1) training data size (from small fractions to the full corpus), (2) domain composition (Wikipedia-only vs. mixed domains including news, government documents, and web text), and (3) pre-training from scratch vs. continued pre-training. Evaluation tasks include dependency parsing and POS tagging (UD Maltese-MUDT treebank), NER (custom Maltese NER annotations), and sentiment analysis (Maltese sentiment dataset). Performance is measured using task-specific metrics (LAS/UAS for parsing, F1 for NER, accuracy for sentiment).

## Results Summary

BERTu achieves state-of-the-art results across all four Maltese NLP tasks despite the relatively small training corpus. Mixed-domain pre-training consistently outperforms Wikipedia-only pre-training, with the advantage being most pronounced for higher-level tasks like sentiment analysis. A relatively small fraction (approximately 25-50%) of the full corpus is sufficient to achieve the majority of the performance gains over Wikipedia-only models. BERTu outperforms mBERTu on most tasks, with the gap being largest for semantic tasks, confirming that dedicated monolingual models with appropriate vocabulary are preferable to adapted multilingual models for languages with unique scripts. The results demonstrate that data quality and domain diversity matter more than sheer quantity for low-resource language model pre-training.

## Conclusions

The study demonstrates that high-quality monolingual models can be trained even for very low-resource languages with limited corpora, provided the training data has sufficient domain diversity. Future work includes extending the Maltese corpus, developing more comprehensive Maltese NLP benchmarks, and investigating cross-lingual transfer from related Semitic languages (especially Arabic) to further improve Maltese model performance. The findings have implications for other low-resource languages considering whether to develop dedicated monolingual models or rely on multilingual alternatives.

## Artifact Contributions

- **BERTu Model**: Monolingual BERT model for Maltese (https://huggingface.co/MLRS/BERTu)
- **Korpus Malti v4.0**: Multi-domain Maltese text corpus for language model pre-training

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Foundation Maltese language model enabling bias and fairness evaluation. Addresses data quality challenges for low-resource languages. Used as basis for gender bias studies in Maltese.

## Tags

