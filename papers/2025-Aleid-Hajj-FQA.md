---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QBUKIZ9H
type: journalArticle
short_title: Hajj-FQA
year: 2025
first_author: "[[Hayfa A. Aleid]]"
last_author: "[[Aqil M. Azmi]]"
authors: "Hayfa A. Aleid; Aqil M. Azmi"
doi: 10.1007/s44443-025-00128-w
url: "https://link.springer.com/10.1007/s44443-025-00128-w"
external_pdf: "https://link.springer.com/content/pdf/10.1007/s44443-025-00128-w.pdf"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic"
languages_list: "Arabic"
religious_values: "Islam"
rv_islam: 100
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
religious_values_list: "Islam"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Arabic, Islam, Utilitarianism"
key_contribution: "Introduces Hajj-FQA, a benchmark Arabic dataset for question answering on Hajj fatwas to develop specialized religious chatbots"
significance: "Fills a critical gap in Arabic-language religious QA resources, enabling accurate, domain-specific responses for pilgrims"
tags: 
abstract: "Deep learning has signiﬁcantly advanced the question-answering (QA) systems across various sectors. However, Arabiclanguage systems for Hajj-related fatwas (non-binding Islamic legal opinions issued by muftis) remain underdeveloped. This paper introduces Hajj-FQA, a benchmark Arabic dataset speciﬁcally designed to develop HajjBot - a specialized chatbot for fatwas QA during the annual Hajj pilgrimage. The dataset captures the unique linguistic and jurisprudential characteristics of pilgrims' inq"
LLM_assessed: "BART, BERT, RoBERTa"
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Aleid-Hajj-FQA.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Aleid-Hajj-FQA.pdf]]"
CONF-CC: "Journal of King Saud University - Computer and Information Sciences"
DATE_ADDED: 20260207
CONFERENCE: "Journal"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset for question answering"
data_metrics: "Not specified"
---
# Hajj-FQA: A benchmark Arabic dataset for developing question-answering systems on Hajj fatwas

## Metadata

**Authors:** Aleid, Hayfa A.; Azmi, Aqil M.

**Year:** 2025

**Publication:** Journal of King Saud University Computer and Information Sciences

**Type:** journalArticle

**DOI:** [10.1007/s44443-025-00128-w](https://doi.org/10.1007/s44443-025-00128-w)

**Pages:** 135

**Volume/Issue:** Vol. 37, Issue 6

## Links

- **URL:** https://link.springer.com/10.1007/s44443-025-00128-w
- **DOI:** https://doi.org/10.1007/s44443-025-00128-w

## Abstract

Deep learning has signiﬁcantly advanced the question-answering (QA) systems across various sectors. However, Arabiclanguage systems for Hajj-related fatwas (non-binding Islamic legal opinions issued by muftis) remain underdeveloped. This paper introduces Hajj-FQA, a benchmark Arabic dataset speciﬁcally designed to develop HajjBot - a specialized chatbot for fatwas QA during the annual Hajj pilgrimage. The dataset captures the unique linguistic and jurisprudential characteristics of pilgrims’ inquiries, enabling accurate, domain-speciﬁc responses. We present a comprehensive quantitative analysis of the dataset’s construction methodology and its distinctive question-answer patterns. Evaluation using multilingual and Arabicspeciﬁc language models across three tasks - machine reading comprehension (MRC), duplicate question detection (DQD), and duplicate answer detection (DAD) - with 10-fold cross-validation demonstrates the practical utility of Hajj-FQA. Results show exceptional performance in classiﬁcation tasks (AraBERTv0.2 achieved a precision score of 99.19% for DQD and 99.26% for DAD) and strong extractive answering capability with an F-score of 72.78%. While generative performance reached BERT-F score of 71.4% (AraBART), MRC variability highlights challenges in religious reasoning. These ﬁndings establish Hajj-FQA as both: (1) a critical resource for developing specialized fatwa chatbots like HajjBot, and (2) a benchmark for Arabic religious QA systems. The dataset directly addresses the urgent need for accurate, automated fatwa assistance during Hajj, while providing insights for future improvements in Islamic NLP applications.

## Authors

[[Hayfa A. Aleid]], [[Aqil M. Azmi]]

## Detailed Summary

This paper introduces Hajj-FQA, a benchmark Arabic dataset specifically designed for developing question-answering systems on Hajj fatwas (Islamic legal opinions). The dataset addresses the critical need for accurate automated fatwa assistance during the annual Hajj pilgrimage, when millions of pilgrims require guidance on religious obligations but access to qualified muftis is limited. The paper captures unique linguistic patterns and jurisprudential characteristics of pilgrims' inquiries.

The research provides comprehensive documentation of the dataset construction methodology, including source selection from authoritative fatwa repositories, preprocessing for Arabic NLP, and annotation procedures. The authors evaluate the dataset across three fundamental NLP tasks: machine reading comprehension (MRC), duplicate question detection (DQD), and duplicate answer detection (DAD). These tasks mirror real-world chatbot requirements for understanding queries, matching similar questions, and identifying equivalent answers.

The significance of this work lies in filling a critical gap in Arabic-language religious NLP resources. While general Arabic NLP has advanced, domain-specific applications for Islamic jurisprudence remain underdeveloped. Hajj-FQA enables development of HajjBot - a specialized chatbot providing accurate, contextually appropriate fatwa assistance to pilgrims in their native language.

## Paper Outline

1. Introduction - Motivation for Arabic Hajj fatwa QA systems
2. Related Work - Arabic NLP, religious text processing, QA systems
3. Dataset Construction - Source collection and preprocessing
4. Hajj-FQA Characteristics - Linguistic and jurisprudential analysis
5. Experimental Setup - Models, tasks, and evaluation methodology
6. Results - Performance across MRC, DQD, and DAD tasks
7. Discussion - Implications for religious NLP
8. Conclusion and Future Work

## Methods Summary

The methodology encompasses: (1) Dataset construction from authoritative Hajj fatwa sources with careful preprocessing for Arabic text normalization. (2) Annotation framework ensuring jurisprudential accuracy. (3) Evaluation using both multilingual models (mBERT, XLM-RoBERTa) and Arabic-specific models (AraBERT variants, AraBART, AraGPT2). (4) Three evaluation tasks: extractive MRC measuring answer span identification, DQD measuring question similarity detection, and DAD measuring answer equivalence recognition. (5) 10-fold cross-validation for robust performance estimates.

## Results Summary

Key quantitative findings: (1) Classification tasks achieved exceptional performance - AraBERTv0.2 reached 99.19% precision for DQD and 99.26% for DAD. (2) Extractive MRC achieved strong F-score of 72.78%. (3) Generative performance reached BERT-F score of 71.4% with AraBART. (4) Arabic-specific models consistently outperformed multilingual alternatives. (5) MRC variability highlights challenges in religious reasoning requiring domain knowledge. (6) Performance gaps indicate room for improvement in nuanced jurisprudential understanding.

## Conclusions

The authors conclude that Hajj-FQA provides both a critical resource for developing specialized fatwa chatbots and a benchmark for Arabic religious QA systems. Limitations include focus on Hajj-specific fatwas and particular jurisprudential schools. Future work should expand to other Islamic pillars (prayer, fasting, zakat), incorporate additional Arabic dialects spoken by pilgrims, and develop more sophisticated reasoning capabilities for complex jurisprudential questions.

## Artifact Contributions

- Hajj-FQA dataset: Benchmark Arabic dataset for Hajj fatwa question answering
- HajjBot: Prototype specialized chatbot for pilgrims (implied, development target)
- Evaluation framework: Standardized tasks and metrics for Arabic religious QA

## Data Description

Hajj-FQA: a benchmark Arabic dataset of expert-annotated Hajj-related fatwas for question-answering systems, supporting machine reading comprehension (MRC), duplicate question detection (DQD), and duplicate answer detection (DAD) tasks.


## Notes


## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23] 0 citations (Crossref/DOI) [2025-08-23]
