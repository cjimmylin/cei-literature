---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0537
type: conferencePaper
short_title: "GREEK-BERT: The Greeks visiting Sesame Street"
year: 2025
first_author: "[[John Koutsikakis]]"
last_author: "[[Ion Androutsopoulos Prodromos Malakasiotis]]"
authors: "John Koutsikakis, Ilias Chalkidis, Prodromos Malakasiotis, Ion Androutsopoulos"
doi: 10.1145/3411408.3411440
url: "https://dl.acm.org/doi/10.1145/3411408.3411440"
external_pdf: "https://arxiv.org/pdf/2008.12014"
publication: "ACM / 11th Hellenic Conference on AI"
pdf_extract: "PDF Extracts/2020/2020-Koutsikakis-GREEK-BERT The Greeks visiting Sesame Street.md"
local_pdf: "[[PDFs/2020/2020-Koutsikakis-GREEK-BERT The Greeks visiting Sesame Street.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Greek"
languages_list: Greek
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: BERT
DATA_URL: "https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1"
tags: 
abstract: "Transformer-based language models, such as BERT and its variants, have achieved state-of-the-art performance in several downstream natural language processing (NLP) tasks on generic benchmark datasets (e.g., GLUE, SQUAD, RACE). However, these models have mostly been applied to the resource-rich English language. In this paper, we present GREEK-BERT, a monolingual BERT-based language model for modern Greek. We evaluate its performance in three NLP tasks, i.e."
research_topic: "Bias & Fairness"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# GREEK-BERT: The Greeks visiting Sesame Street

## Authors

[[Ilias Chalkidis John Koutsikakis]], [[Ion Androutsopoulos Prodromos Malakasiotis]]

## Metadata

**Authors:** John Koutsikakis, Ilias Chalkidis, Prodromos Malakasiotis, Ion Androutsopoulos

**Year:** 2020

**Type:** conferencePaper

**Venue:** ACM / 11th Hellenic Conference on AI

**DOI:** [10.1145/3411408.3411440](https://doi.org/10.1145/3411408.3411440)

**Languages:** Greek

## Links

- **DOI:** https://doi.org/10.1145/3411408.3411440
- **URL:** https://dl.acm.org/doi/10.1145/3411408.3411440
- **Code/Data:** https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1

## Abstract

A monolingual BERT-based language model for modern Greek, evaluated on three NLP tasks including POS tagging, NER, and NLI. Foundation model for downstream Greek NLP tasks including bias evaluation.

## Summary

This paper introduces GREEK-BERT, a monolingual BERT-based language model for modern Greek trained on 29GB of Greek text with a 35,000 sub-word vocabulary. The model is evaluated on three downstream NLP tasks (part-of-speech tagging, named entity recognition, and natural language inference) and achieves state-of-the-art performance, outperforming multilingual models (M-BERT, XLM-R) by 5-10% on two benchmarks. The publicly released model and code serve as a foundation for Greek NLP research and applications, including subsequent bias and fairness evaluations.

## Data Description

GREEK-BERT, a monolingual BERT model for modern Greek trained on 29GB of Greek text from various sources including Wikipedia, news, and legal documents. Evaluated on NER, POS tagging, and UD parsing tasks for Greek NLP.


## Detailed Summary

This paper introduces GREEK-BERT, the first publicly available monolingual BERT-based language model for modern Greek, trained on 29 GB of Greek text with a 35,000 sub-word BPE vocabulary created from scratch. The model follows the BERT-BASE architecture (12 transformer layers, 768 hidden units, 12 attention heads, 110M parameters) and is pre-trained using Masked Language Modeling (MLM) and Next Sentence Prediction (NSP) objectives. The training data includes Greek Wikipedia, the European Parliament proceedings, Greek legislation, and Greek web-crawled data. The paper motivates the need for a dedicated Greek model by highlighting that multilingual models like M-BERT allocate only about 1% of their vocabulary (1,208 WordPieces) to Greek due to the unique Greek alphabet, compared to much larger shared vocabularies for Roman-alphabet languages.

GREEK-BERT is evaluated on three core downstream NLP tasks: Part-of-Speech (PoS) tagging, Named Entity Recognition (NER), and Natural Language Inference (NLI). Results demonstrate that GREEK-BERT achieves state-of-the-art performance across all benchmarks, outperforming multilingual models M-BERT and XLM-R by a significant margin of 5-10% on NER and NLI tasks, while showing competitive performance on PoS tagging. The model also outperforms shallower neural baselines using pre-trained word embeddings. Both the pre-trained model and fine-tuning code are publicly released to support Greek NLP research and applications.

## Paper Outline

1. Introduction - Motivation for Greek-specific language model
2. Related Work - BERT, multilingual models (M-BERT, XLM, XLM-R), monolingual models (CamemBERT, etc.)
3. GREEK-BERT - Pre-training details, data, vocabulary, hyperparameters
4. Experiments - PoS tagging, NER, NLI evaluations
5. Conclusion - Summary and future directions

## Methods Summary

GREEK-BERT uses the BERT-BASE-UNCASED architecture pre-trained on 29 GB of Greek text from four domains: Greek Wikipedia, European Parliament proceedings, Greek legislation, and web-crawled data. A custom 35k sub-word BPE vocabulary was created from the training corpus. The model was pre-trained with MLM and NSP objectives. For downstream evaluation, the model is fine-tuned on each task: PoS tagging and NER use the Universal Dependencies Greek-GDT treebank and additional NER annotations, while NLI uses the Greek portion of the XNLI dataset. Comparisons include M-BERT, XLM-R BASE, XLM-R LARGE, and BiLSTM baselines with pre-trained fastText word embeddings.

## Results Summary

GREEK-BERT achieves state-of-the-art results on all three evaluated tasks. On PoS tagging (UD Greek-GDT), it achieves competitive accuracy with multilingual models. On NER, GREEK-BERT outperforms M-BERT and XLM-R by 5-10% in F1 score, demonstrating the advantage of monolingual pre-training for token-level tasks where vocabulary coverage is critical. On NLI (XNLI Greek), GREEK-BERT similarly outperforms multilingual baselines by a significant margin. The results confirm that for languages with unique scripts like Greek, monolingual models that dedicate their full vocabulary capacity to the target language substantially outperform multilingual alternatives despite sharing the same base architecture.

## Conclusions

The authors note that GREEK-BERT fills a significant gap in Greek NLP resources. Future work includes training larger models (BERT-LARGE), exploring RoBERTa-style pre-training without NSP, and developing more comprehensive Greek NLP benchmarks. The limited availability of Greek NLP evaluation datasets remains a constraint for thorough model assessment.

## Artifact Contributions

- **GREEK-BERT Model**: Pre-trained BERT-BASE model for modern Greek (https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1)
- **GREEK-BERT Code**: Training and fine-tuning code (https://github.com/nlpaueb/greek-bert)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Foundation Greek language model used in downstream bias and fairness evaluations. Enables evaluation of social biases encoded in Greek language representations.

## Tags

