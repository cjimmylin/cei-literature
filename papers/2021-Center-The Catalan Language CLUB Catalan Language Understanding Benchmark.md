---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0520
type: preprint
short_title: The Catalan Language CLUB (Catalan Language Understanding Benchmark)
year: 2021
first_author: "[[Carlos Rodriguez-Penagos et al. (Barcelona Supercomputing Center)]]"
last_author: "[[Carlos Rodriguez-Penagos et al. (Barcelona Supercomputing Center)]]"
authors: Carlos Rodriguez-Penagos et al. (Barcelona Supercomputing Center)
url: "https://arxiv.org/abs/2112.01894"
external_pdf: "https://arxiv.org/pdf/2112.01894.pdf"
publication: arXiv
local_pdf: "[[PDFs/2021/2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark.pdf]]"
pdf_extract: "PDF Extracts/2021/2021-Center-The Catalan Language CLUB Catalan Language Understanding Benchmark.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "Catalan"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "https://github.com/TeMU-BSC/club"
tags: 
abstract: "The Catalan Language Understanding Benchmark (CLUB) encompasses various datasets representative of diﬀerent NLU tasks that enable accurate evaluations of language models, following the General Language Understanding Evaluation (GLUE) example. It is part of AINA and PlanTL, two public funding initiatives to empower the Catalan language in the Artiﬁcial Intelligence era."
research_topic: "Machine Learning"
---
# The Catalan Language CLUB (Catalan Language Understanding Benchmark)

## Authors

[[Carlos Rodriguez-Penagos et al. (Barcelona Supercomputing Center)]]

## Metadata

**Authors:** Carlos Rodriguez-Penagos et al. (Barcelona Supercomputing Center)

**Year:** 2021

**Type:** preprint

**Venue:** arXiv

**Languages:** Catalan

**Benchmark:** CLUB

## Links

- **arXiv:** https://arxiv.org/abs/2112.01894
- **Code/Data:** https://github.com/projecte-aina/club

## Abstract

Catalan Language Understanding Benchmark encompassing datasets for POS tagging, NER, text classification, textual entailment, and extracted QA. Part of AINA and PlanTL public funding initiatives to empower the Catalan language in AI.

## Summary

This paper presents the Catalan Language Understanding Benchmark (CLUB), a comprehensive NLU evaluation suite for Catalan following the GLUE model, comprising six tasks: text classification (153,265 news articles), textual entailment (20,000+ sentence pairs), question answering (three datasets including XQuAD-Ca, VilaQuAD, ViquiQuAD), named entity recognition, and POS tagging (from AnCora corpus). Developed under the AINA and PlanTL public funding initiatives, the benchmark evaluates Catalan BERT and RoBERTa models against multilingual baselines, with all datasets released under permissive licenses on Zenodo and HuggingFace to democratize Catalan AI language resources.

## Data Description

Catalan Language Understanding Benchmark (CLUB) consisting of six tasks: text classification, paraphrase detection, semantic textual similarity, question answering, NER, and POS tagging. Tests Catalan BERT and RoBERTa models against multilingual baselines.


## Detailed Summary

This paper presents the Catalan Language Understanding Benchmark (CLUB), a comprehensive NLU evaluation suite for Catalan modeled after the English GLUE benchmark. CLUB is developed as part of AINA and PlanTL, two public funding initiatives in Spain aimed at empowering the Catalan language in the AI era by providing high-quality resources and tools. The benchmark encompasses multiple NLU tasks including Part-of-Speech (POS) tagging and Named Entity Recognition (NERC) from the AnCora corpus projected onto Universal Dependencies, Textual Entailment for Catalan (TECa) with over 20,000 annotated sentence pairs, and Text Classification (TeCla) with 153,265 news articles across 30 categories from the Catalan News Agency.

The benchmark also includes three Question Answering datasets: XQuAD-Ca (Catalan translation of XQuAD), VilaQuAD (extractive QA from Vilaweb news), and ViquiQuAD (extractive QA from Catalan Wikipedia). All datasets are released under permissive licenses on Zenodo and HuggingFace, with training/evaluation/test splits provided. The datasets follow best practices for data statements (Bender and Friedman, 2018), noting that all annotators were native Catalan speakers with linguistic expertise. The benchmark evaluates Catalan-specific BERT and RoBERTa models against multilingual baselines, establishing evaluation infrastructure that democratizes access to Catalan AI language resources for institutions, organizations, and individuals.

## Paper Outline

1. Introduction - AINA and PlanTL initiatives for Catalan AI
2. Datasets - POS/NERC from AnCora, TECa textual entailment, TeCla text classification, QA datasets
3. Data Statements - Annotation quality and transparency
4. Evaluation - Catalan BERT/RoBERTa vs. multilingual baselines
5. Conclusion - Summary and availability

## Methods Summary

The benchmark datasets are constructed through multiple approaches: POS and NERC annotations are derived from the existing AnCora corpus projected onto Universal Dependencies format. TECa is created by commissioning native Catalan-speaking annotators (translators, philologists, linguists) to write three hypotheses (neutral, inference, contradiction) for each of 18,000 premise sentences from the Catalan Textual Corpus and Vilaweb newswire, achieving 83.57% inter-annotator agreement. TeCla crawls 219,586 articles from the Catalan News Agency archive. QA datasets include translations (XQuAD-Ca) and original extractive QA from news and Wikipedia sources. Evaluation uses Catalan-specific BERT and RoBERTa models compared against multilingual baselines.

## Results Summary

Catalan-specific BERT and RoBERTa models demonstrate competitive or superior performance compared to multilingual baselines across the CLUB tasks, validating the value of language-specific model development. The benchmark provides comprehensive evaluation across multiple NLU capabilities including syntactic analysis (POS), information extraction (NERC), semantic understanding (TECa, TeCla), and reading comprehension (QA datasets). The diversity of tasks ensures that model evaluation captures both low-level linguistic competency and higher-level language understanding abilities for Catalan.

## Conclusions

CLUB establishes a foundational evaluation infrastructure for Catalan NLP that enables systematic assessment and comparison of language models. Future work includes expanding the benchmark with additional tasks, developing larger and more diverse Catalan language models, and extending the evaluation to cover more advanced NLU capabilities. The open availability of all resources through HuggingFace and Zenodo supports community-driven development.

## Artifact Contributions

- **CLUB Benchmark**: Catalan Language Understanding Benchmark with multiple NLU task datasets (https://github.com/projecte-aina/club)
- **TECa Dataset**: Textual Entailment for Catalan with 20,000+ sentence pairs (https://doi.org/10.5281/zenodo.4761458)
- **TeCla Dataset**: Catalan text classification corpus with 153,265 news articles (https://doi.org/10.5281/zenodo.4627197)
- **HuggingFace Models**: Catalan BERT and RoBERTa models (https://huggingface.co/bsc)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Foundational Catalan NLU benchmark. Establishes evaluation infrastructure for Catalan that supports subsequent bias and cultural studies.

## Tags

