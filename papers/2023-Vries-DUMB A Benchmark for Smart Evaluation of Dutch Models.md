---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0482
type: preprint
short_title: "DUMB: A Benchmark for Smart Evaluation of Dutch Models"
year: 2025
first_author: "[[Wietse de Vries]]"
last_author: "[[Wietse de Vries]]"
authors: "Wietse de Vries et al."
url: "https://arxiv.org/abs/2305.13026"
external_pdf: "https://arxiv.org/pdf/2305.13026.pdf"
publication: "arXiv / EMNLP 2023"
pdf_extract: "PDF Extracts/2023/2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.md"
local_pdf: "[[PDFs/2023/2023-Vries-DUMB A Benchmark for Smart Evaluation of Dutch Models.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: Dutch
languages_list: Dutch
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multilingual benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "BERTje, RobBERT, mBERT, XLM-RoBERTa"
DATA_URL: "https://github.com/wjwillemse/dumb"
tags: 
abstract: "We introduce the Dutch Model Benchmark: DUMB. The benchmark includes a diverse set of datasets for low-, medium- and highresource tasks. The total set of nine tasks includes four tasks that were previously not available in Dutch. Instead of relying on a mean score across tasks, we propose Relative Error Reduction (RER), which compares the DUMB performance of language models to a strong baseline which can be referred to in the future even when assessing different sets of language models."
research_topic: "Machine Learning"
---
# DUMB: A Benchmark for Smart Evaluation of Dutch Models

## Authors

[[Wietse de Vries et al.]]

## Metadata

**Authors:** Wietse de Vries et al.

**Year:** 2023

**Type:** preprint

**Venue:** arXiv / EMNLP 2023

**Languages:** Dutch

**Benchmark:** DUMB

## Links

- **arXiv:** https://arxiv.org/abs/2305.13026
- **Code/Data:** https://github.com/wietsedv/dumb

## Abstract

Dutch Model Benchmark with 9 tasks including 4 new for Dutch. Evaluates 14 pre-trained LMs using Relative Error Reduction metric. Finds Dutch monolingual models under-perform compared to large multilingual models like DeBERTaV3. Published at EMNLP 2023.

## Summary

This paper introduces DUMB (Dutch Model Benchmark), a comprehensive evaluation suite comprising nine diverse tasks for Dutch language models, including four tasks previously unavailable in Dutch covering low-, medium-, and high-resource scenarios. Rather than using simple mean scores, the authors propose Relative Error Reduction (RER) as a more robust metric that compares model performance against a strong baseline. Evaluating 14 pre-trained models (both monolingual and multilingual of varying sizes), they find that current Dutch monolingual models (BERTje, RobBERT) underperform compared to large multilingual models, with DeBERTaV3-large, XLM-R-large, and mDeBERTaV3-base achieving the highest performance. The work suggests training larger Dutch models with alternative architectures and pre-training objectives, and provides a public leaderboard at dumbench.nl.

## Data Description

DUMB (Dutch Model Benchmark) suite containing 6 datasets for evaluating Dutch language models across sentiment analysis, topic classification, hate speech detection, and natural language inference tasks. Designed to provide comprehensive evaluation of Dutch NLP models.


## Detailed Summary

This paper introduces DUMB (Dutch Model Benchmark), a comprehensive evaluation suite comprising nine diverse tasks for Dutch language models, designed to address the lack of a standard benchmark for Dutch. The benchmark balances word-level, word-pair-level, sentence-pair-level, and document-level tasks across low-resource (hundreds of training examples), mid-resource (thousands), and high-resource (tens of thousands) scenarios. Four of the nine tasks were previously unavailable in Dutch: Word Sense Disambiguation (WiC-NL, constructed from DutchSemCor), Pronoun Resolution (DPR, from SemEval2010 coreference data), Causal Reasoning (COPA-NL, translated from COPA with manual correction), and Question Answering (SQuAD-NL, translated from SQuAD2.0). The remaining five tasks are Part-of-Speech tagging (Lassy Small with 218 fine-grained tags), Named Entity Recognition (SoNaR-1 with 7 entity types), Natural Language Inference (SICK-NL), Sentiment Analysis (DBRD book reviews), and Abusive Language Detection (DALC v2.0 with offensive/abusive/neutral tweets). Rather than using a mean score, the authors propose Relative Error Reduction (RER) as a more robust aggregate metric that compares model performance against a strong baseline, enabling future comparisons even when evaluating different model sets.

## Paper Outline

1. Introduction - Motivation, contributions, other benchmarks comparison
2. DUMB Tasks - Word tasks (POS, NER), word pair tasks (WSD, PR), sentence pair tasks (CR, NLI), document tasks (SA, ALD, QA)
3. Methods - Pre-trained models, fine-tuning, Relative Error Reduction metric
4. Results - Overall performance, task-level analysis, internal consistency
5. Discussion - Implications for Dutch model development
6. Conclusion

## Methods Summary

Fourteen pre-trained language models are evaluated: Dutch monolingual models (BERTje, RobBERT-v1/v2/2022), multilingual base models (mBERT, XLM-R-base, mDeBERTaV3-base), large multilingual models (XLM-R-large, DeBERTaV3-large), and English models (BERT-base, RoBERTa-base, DeBERTaV3-base/large) as reference points. Models are fine-tuned with task-specific hyperparameters. The Relative Error Reduction (RER) metric compares each model's performance against a strong baseline (DeBERTaV3-large), computed as the percentage reduction in error rate relative to that baseline. Cross-validation splits are used for datasets lacking standard splits, with careful attention to preventing data leakage between tasks sharing source corpora.

## Results Summary

DeBERTaV3-large achieves the best overall performance, followed by XLM-R-large and mDeBERTaV3-base. Current Dutch monolingual models (BERTje, RobBERT variants) significantly underperform compared to large multilingual models, with RobBERT2022 achieving RER of only 50.5% compared to DeBERTaV3-large's baseline. English-only DeBERTaV3-large surprisingly outperforms all Dutch monolingual models on Dutch tasks, suggesting that architecture and training objectives matter more than language-specific pre-training at current scales. The abusive language detection (DALC) task proves most challenging, with the best model achieving only 63.7% macro F1. Internal consistency analysis confirms that the benchmark tasks measure sufficiently distinct capabilities.

## Conclusions

The results strongly suggest that the Dutch NLP community should invest in training larger Dutch models with alternative architectures (e.g., DeBERTa-style disentangled attention) and pre-training objectives beyond standard masked language modeling. The current Dutch monolingual models, all based on BERT/RoBERTa-base architectures, are insufficient to compete with large multilingual alternatives. DUMB provides a public leaderboard at dumbench.nl and will foster further research on Dutch language models, with plans to extend to decoder-based generative model evaluation.

## Artifact Contributions

- **DUMB Benchmark**: Nine-task Dutch evaluation suite with standardized splits (https://github.com/wietsedv/dumb)
- **WiC-NL Dataset**: Dutch Word Sense Disambiguation dataset constructed from DutchSemCor
- **DPR Dataset**: Dutch Pronoun Resolution dataset from SemEval2010 coreference annotations
- **COPA-NL Dataset**: Dutch translation of COPA for causal reasoning
- **SQuAD-NL Dataset**: Dutch translation of SQuAD2.0 for extractive QA
- **Public Leaderboard**: Available at dumbench.nl

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Primary Dutch-language NLU benchmark, foundational for evaluating Dutch LLMs.

## Tags

