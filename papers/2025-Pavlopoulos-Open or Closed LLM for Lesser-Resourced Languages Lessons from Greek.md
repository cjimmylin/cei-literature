---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0533
type: preprint
short_title: "Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek"
year: 2025
first_author: "[[John Pavlopoulos]]"
last_author: "[[Maria Gavriilidou]]"
authors: John Pavlopoulos; Juli Bakagianni; Kanella Pouli; Maria Gavriilidou
url: "https://arxiv.org/abs/2501.12826"
external_pdf: "https://arxiv.org/pdf/2501.12826.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Pavlopoulos-Open or Closed LLM for Lesser-Resourced Languages Lessons from Greek.md"
local_pdf: "[[PDFs/2025/2025-Pavlopoulos-Open or Closed LLM for Lesser-Resourced Languages Lessons from Greek.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Greek"
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
LLM_assessed: "LLaMA, GPT-4o"
DATA_URL: "https://github.com/greek-nlp/benchmark"
tags: 
abstract: "Natural Language Processing (NLP) for lesserresourced languages faces persistent challenges, including limited datasets, inherited biases from high-resource languages, and the need for domain-specific solutions. This study addresses these gaps for Modern Greek through three key contributions. First, we evaluate the performance of open-source (Llama-70b) and closed-source (GPT-4o mini) large language models (LLMs) on seven core NLP tasks with dataset availability, revealing task-specific..."
CONFERENCE: "Preprint"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "General Ethics"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# Open or Closed LLM for Lesser-Resourced Languages? Lessons from Greek

## Authors

[[John Pavlopoulos]], [[Juli Bakagianni]], [[Kanella Pouli]], [[Maria Gavriilidou]]

## Metadata

**Authors:** John Pavlopoulos, Juli Bakagianni, Kanella Pouli, Maria Gavriilidou

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

## Links

- **arXiv:** https://arxiv.org/abs/2501.12826

## Abstract

Evaluates open-source (Llama-70b) and closed-source (GPT-4o mini) LLMs on seven core Greek NLP tasks. Reframes Authorship Attribution as a tool to assess potential data usage by LLMs in pre-training, with high 0-shot accuracy suggesting ethical implications for data provenance. Includes a legal NLP case study.

## Summary

This paper addresses NLP challenges for Modern Greek, a lesser-resourced language, through three contributions: benchmarking Llama-70b and GPT-4o mini on seven core tasks revealing task-specific strengths, reframing Authorship Attribution to assess potential data usage in pre-training with ethical implications for data provenance, and demonstrating a legal NLP case study where a Summarize-Translate-Embed methodology outperforms TF-IDF for clustering long legal texts. The work aggregates publicly available Greek datasets into a unified collection, providing a roadmap for advancing NLP in lesser-resourced languages while highlighting inherited biases from high-resource languages.

## Data Description

This paper evaluates open-source (Llama-70b) and closed-source (GPT-4o mini) LLMs on seven core Greek NLP tasks. It reframes Authorship Attribution as a tool to assess potential data usage by LLMs in pre-training, with high 0-shot accuracy suggesting ethical implications for data provenance. Includes a legal NLP case study for Greek.


## Detailed Summary

This paper addresses NLP challenges for Modern Greek, a lesser-resourced language, through three key contributions. First, based on a systematic literature review of 142 Greek NLP studies (2012-2023), the authors aggregate publicly available Greek datasets into a unified collection and benchmark seven core NLP tasks using both an open-source model (Llama-70b) and a closed-source model (GPT-4o mini). The tasks include Named Entity Recognition, Summarization, Grammatical Error Correction, Machine Translation (Greek to English, Farsi, and Japanese), Intent Classification, Part-of-Speech Tagging, and Toxicity Detection. The comparison reveals task-specific strengths: Llama performs better on NER and Summarization, GPT excels at GEC, MT (el-jpn), Intent Classification, and POS Tagging, while both perform comparably on Toxicity Detection and some MT pairs.

Second, the authors innovatively reframe Authorship Attribution as a tool to assess potential data usage by LLMs in pre-training. High zero-shot accuracy in authorship attribution suggests that the authored texts may have been included in the model's pre-training data, raising ethical implications for data provenance, particularly relevant for lesser-resourced languages where data availability is limited and unauthorized use is more impactful. Third, the paper introduces the first Text Clustering benchmark for Greek legal texts, demonstrating that a Summarize-Translate-Embed (STE) methodology outperforms traditional TF-IDF approaches for organizing long, complex legal documents.

## Paper Outline

1. Introduction - Challenges for lesser-resourced language NLP
2. The Data - Dataset availability, popularity, licensing analysis
3. NLP Task Benchmarks - Seven core tasks with open vs. closed model comparison
4. Authorship Attribution - Reframed as data provenance assessment
5. Legal Text Clustering - First Greek legal text clustering benchmark
6. Related Work
7. Conclusion

## Methods Summary

The study aggregates 94 Greek datasets identified from a systematic literature review, filtering for those with open-access licenses that permit derivatives. Seven NLP tasks are benchmarked using Llama-70b (open-source) and GPT-4o mini (closed-source) in various evaluation settings. Authorship Attribution uses zero-shot evaluation to test whether models can identify known Greek authors, with high accuracy hypothesized to indicate pre-training data inclusion. The legal text clustering benchmark uses the STE (Summarize, Translate, and Embed) methodology, which first summarizes long legal texts, translates summaries to English, then generates embeddings for clustering, compared against a TF-IDF baseline.

## Results Summary

Task-specific comparison shows Llama-70b excels at NER and Summarization while GPT-4o mini is better at GEC, MT (el-jpn), Intent Classification, and POS Tagging; both perform comparably on Toxicity Detection and some MT pairs. High zero-shot authorship attribution accuracy raises concerns about unauthorized data usage in pre-training, particularly relevant for lesser-resourced languages with limited data sources. The STE methodology significantly outperforms TF-IDF for Greek legal text clustering, demonstrating a practical solution for organizing complex legal documents in lesser-resourced language settings. The availability analysis reveals that most Greek NLP datasets are not publicly accessible, with studies providing available data attracting more citations.

## Conclusions

The paper provides a roadmap for advancing NLP in lesser-resourced languages through model evaluation, task innovation, and practical applications. Limitations include the focus on only two models (one open, one closed), the limited scope of the authorship attribution experiment as a proxy for data provenance, and the single-language focus. Future work includes expanding the benchmark to more models and tasks, developing more robust methods for detecting pre-training data inclusion, and extending the legal clustering methodology to other domains and languages.

## Artifact Contributions

- **Greek NLP Benchmark Code**: Unified evaluation code for Greek NLP tasks (https://github.com/greek-nlp/benchmark)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Directly addresses ethical implications of data provenance in Greek LLMs. Evaluates fairness between open and closed LLMs for low-resource Greek. Relevant to bias and ethics in LLM deployment for minority languages.

## Tags

