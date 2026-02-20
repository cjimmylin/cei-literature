---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0509
type: conferencePaper
short_title: "AMI @ EVALITA2020: Automatic Misogyny Identification"
year: 2020
first_author: "[[Nozza, Debora]]"
last_author: "[[Debora Nozza]]"
authors: "[[Nozza, Debora]]"
authors_incomplete: true
url: "https://amievalita2020.github.io/"
external_pdf: "https://books.openedition.org/aaccademia/pdf/6732"
publication: "EVALITA 2020"
pdf_extract: "PDF Extracts/2020/2020-Nozza-AMI @ EVALITA2020 Automatic Misogyny Identification.md"
local_pdf: "[[PDFs/2020/2020-Nozza-AMI @ EVALITA2020 Automatic Misogyny Identification.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Italian"
cultures_nationalities_list: "Italian"
languages_list: Italian
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: BERT
DATA_URL: "http://github.com/vinid/cade"
tags: 
abstract: "Welcome to EVALITA 2020! EVALITA is the evaluation campaign of Natural Language Processing and Speech Tools for Italian. EVALITA is an initiative of the Italian Association for Computational Linguistics (AILC, http://www.ai-lc.it) and it is endorsed by the Italian Association for Artificial Intelligence (AIxIA, http://www.aixia.it) and the Italian Association for Speech Sciences (AISV, http://www.aisv.it)."
research_topic: "NLP & Representation Learning"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "Other Conference"
---
# AMI @ EVALITA2020: Automatic Misogyny Identification

## Authors

[[Debora Nozza]]

## Metadata

**Authors:** Debora Nozza et al.

**Year:** 2020

**Type:** conferencePaper

**Venue:** EVALITA 2020

**Languages:** Italian

**Benchmark:** AMI (Automatic Misogyny Identification)

## Links

- **URL:** https://amievalita2020.github.io/
- **Code/Data:** https://github.com/dnozza/ami2020

## Abstract

Shared task for automatically identifying misogynous content in Italian tweets. Two subtasks: (A) misogyny and aggressiveness identification, (B) fairness of the model. Annotated for misogyny categories: Discredit, Derailing, Dominance, Sexual Harassment, Stereotype & Objectification.

## Summary

This paper presents the AMI (Automatic Misogyny Identification) shared task at EVALITA 2020, which focuses on detecting misogynous content in Italian tweets across two subtasks: (A) identifying misogyny and aggressiveness, and (B) evaluating model fairness. The dataset includes fine-grained annotations for misogyny categories including Discredit, Derailing, Dominance, Sexual Harassment, and Stereotype & Objectification. Multiple teams participated using various approaches including BERT-based models, with Subtask B explicitly measuring fairness to address bias concerns in misogyny detection systems.

## Data Description

Automatic Misogyny Identification (AMI) shared task at EVALITA2020 for Italian. Tests systems for binary misogyny detection and misogyny category classification. Participating teams used various approaches including BERT-based models.


## Detailed Summary

This paper presents the AMI (Automatic Misogyny Identification) shared task at EVALITA 2020, which focuses on detecting misogynous content in Italian tweets. The task is organized into two subtasks: Subtask A addresses misogyny identification and aggressiveness detection, requiring systems to classify tweets as misogynous or not and to identify whether the content is aggressive. Subtask B introduces a novel fairness evaluation component, explicitly measuring whether misogyny detection models exhibit unintended biases. The dataset includes fine-grained annotations across misogyny categories: Discredit, Derailing, Dominance, Sexual Harassment, and Stereotype & Objectification.

The task is part of the broader EVALITA 2020 proceedings covering Italian NLP evaluation. Multiple teams participated using various approaches, with BERT-based models (including AlBERTo and XLM-RoBERTa) being the most popular architecture. The inclusion of Subtask B on model fairness is particularly notable, as it explicitly addresses the concern that hate speech detection systems can themselves encode biases, for example by disproportionately flagging content mentioning certain identity groups. This represents an early effort to systematically evaluate fairness alongside accuracy in Italian misogyny detection systems.

## Paper Outline

1. Task Description - AMI shared task definition and subtasks
2. Dataset - Italian tweet collection with misogyny annotations
3. Subtask A - Misogyny and aggressiveness identification
4. Subtask B - Model fairness evaluation
5. Participating Systems - Team approaches and architectures
6. Results - Performance comparison across teams

## Methods Summary

The shared task provides annotated Italian tweet datasets for training and evaluation. Subtask A uses standard binary and multi-class classification metrics for misogyny detection and aggressiveness identification. Subtask B introduces fairness metrics to evaluate whether systems exhibit bias in their predictions, measuring performance parity across different identity groups and content types. Participating teams employed approaches including fine-tuned BERT-based models (AlBERTo, XLM-RoBERTa), CNNs with word embeddings, ensemble methods, and sentence embedding approaches with misogyny lexicons.

## Results Summary

Multiple teams achieved competitive results on misogyny identification in Italian tweets, with transformer-based architectures generally outperforming traditional approaches. The fairness evaluation in Subtask B revealed that some high-accuracy systems exhibited notable biases in their predictions, demonstrating the importance of evaluating fairness alongside raw detection performance. The task highlighted that misogyny detection in Italian presents unique challenges related to linguistic and cultural context.

## Conclusions

The AMI shared task advances Italian misogyny detection research by introducing fairness evaluation alongside accuracy. Future work should expand the dataset, incorporate more nuanced misogyny categories, and develop bias mitigation strategies specific to Italian language models. The explicit fairness evaluation component sets a precedent for future hate speech detection shared tasks.

## Artifact Contributions

- **AMI 2020 Dataset and Code**: Italian misogyny identification task resources (https://github.com/dnozza/ami2020)
- **AMI Task Website**: Task description and results (https://amievalita2020.github.io/)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Directly evaluates fairness and bias in misogyny detection for Italian. Subtask B explicitly measures model fairness.

## Tags

