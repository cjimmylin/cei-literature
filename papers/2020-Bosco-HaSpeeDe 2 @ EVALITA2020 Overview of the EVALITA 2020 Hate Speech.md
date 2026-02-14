---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0508
type: conferencePaper
short_title: "HaSpeeDe 2 @ EVALITA2020: Overview of the EVALITA 2020 Hate Speech Detection Task"
year: 2025
first_author: "[[Cristina Bosco]]"
last_author: "[[Cristina Bosco]]"
authors: "Cristina Bosco et al."
url: "https://www.researchgate.net/publication/346997652_HaSpeeDe_2_EVALITA2020_Overview_of_the_EVALITA_2020_Hate_Speech_Detection_Task"
external_pdf: "https://books.openedition.org/aaccademia/pdf/6732"
publication: "EVALITA 2020"
local_pdf: "[[PDFs/2020/2020-Bosco-HaSpeeDe 2 @ EVALITA2020 Overview of the EVALITA 2020 Hate Speech.pdf]]"
pdf_extract: "PDF Extracts/2020/2020-Bosco-HaSpeeDe 2 @ EVALITA2020 Overview of the EVALITA 2020 Hate Speech.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: Italian
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/msang/haspeede/tree/master/2020"
tags: 
abstract: 
ethics_perspective: "Toxicity & Hate Speech"
---
# HaSpeeDe 2 @ EVALITA2020: Overview of the EVALITA 2020 Hate Speech Detection Task

## Authors

[[Cristina Bosco et al.]]

## Metadata

**Authors:** Cristina Bosco et al.

**Year:** 2020

**Type:** conferencePaper

**Venue:** EVALITA 2020

**Languages:** Italian

**Benchmark:** HaSpeeDe 2

## Links

- **URL:** https://www.researchgate.net/publication/346997652_HaSpeeDe_2_EVALITA2020_Overview_of_the_EVALITA_2020_Hate_Speech_Detection_Task
- **Code/Data:** https://github.com/msang/haspeede/tree/master/2020

## Abstract

Second edition shared task on detection of hateful content in Italian Twitter messages. Composed of main task (hate speech detection) and pilot tasks (stereotype detection, nominal utterance detection). 14 teams participated; best macro F1 of 0.8088.

## Summary

This paper presents HaSpeeDe 2, the second edition of the EVALITA shared task on hate speech detection in Italian Twitter messages and news headlines. The task includes a main hate speech detection track and two pilot tasks for stereotype detection and nominal utterance detection, with 14 participating teams employing various approaches including BERT-based models. The best-performing system achieved a macro F1 score of 0.8088, and the shared task provides cross-domain evaluation between Twitter and news domains to assess model robustness.

## Data Description

Second edition shared task on detecting hateful content in Italian Twitter messages. Includes main task (hate speech detection) and pilot tasks (stereotype detection, nominal utterance detection). 14 teams participated with various approaches including BERT models, achieving best macro F1 of 0.8088.


## Detailed Summary

This paper presents HaSpeeDe 2, the second edition of the shared task on hate speech detection within the EVALITA 2020 evaluation campaign for Italian NLP. The task is part of the broader EVALITA proceedings (523 pages) covering multiple tracks including hate speech detection, automatic misogyny identification, stance detection, and other NLP tasks for the Italian language. HaSpeeDe 2 includes a main hate speech detection task on Italian Twitter messages and news headlines, along with pilot tasks for stereotype detection and nominal utterance detection. The shared task attracted 14 participating teams who employed various approaches, predominantly BERT-based transformer models including AlBERTo and XLM-RoBERTa.

The task provides cross-domain evaluation between Twitter and news headline domains to assess model robustness and generalization. The best-performing system achieved a macro F1 score of 0.8088. The proceedings also include detailed system descriptions from participating teams, covering approaches ranging from fine-tuned pre-trained language models to convolutional neural networks and ensemble methods. The shared task contributes to the growing body of Italian-language hate speech detection research and provides benchmark datasets and evaluation standards for the Italian NLP community.

## Paper Outline

1. EVALITA 2020 Overview - Seventh evaluation campaign for Italian NLP
2. Track: Affect, Hate, and Stance - AMI, HaSpeeDe 2, SardiStance tasks
3. HaSpeeDe 2 - Main hate speech detection task and pilot tasks
4. System Descriptions - 14 participating teams and their approaches
5. Additional Tracks - Other EVALITA 2020 evaluation tasks

## Methods Summary

The shared task follows a standard evaluation campaign format with provided training and test data for Italian hate speech detection. Participating teams employed diverse approaches including fine-tuned BERT-based models (AlBERTo, XLM-RoBERTa), convolutional neural networks, ensemble methods combining transformer architectures with transfer learning, and traditional classifiers enhanced with linguistic features. Cross-domain evaluation between Twitter and news headline datasets tests model generalization across text genres. The annotation scheme captures both hate speech presence and stereotype detection.

## Results Summary

The best-performing system achieved a macro F1 score of 0.8088 on the main hate speech detection task. Fourteen teams participated in the shared task, with transformer-based approaches (particularly BERT-based models) dominating the top results. The cross-domain evaluation revealed challenges in transferring hate speech detection capabilities between Twitter and news headline domains, highlighting the importance of domain-robust approaches. The stereotype detection pilot task provided initial baselines for this relatively unexplored dimension of Italian hate speech analysis.

## Conclusions

The shared task represents the continued maturation of Italian hate speech detection research, building on the first HaSpeeDe edition. The inclusion of cross-domain evaluation and pilot tasks for stereotype detection extends the scope beyond binary hate speech classification. Future editions are expected to incorporate additional annotation dimensions and larger, more diverse datasets for Italian hate speech evaluation.

## Artifact Contributions

- **HaSpeeDe 2 Dataset**: Italian hate speech detection dataset from Twitter and news headlines (https://github.com/msang/haspeede/tree/master/2020)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Major Italian hate speech evaluation campaign with stereotype detection pilot task. Includes cross-domain evaluation (Twitter and news headlines).

## Tags

