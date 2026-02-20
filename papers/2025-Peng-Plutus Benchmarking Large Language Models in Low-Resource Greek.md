---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0530
type: preprint
short_title: "Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance"
year: 2025
first_author: "[[Xueqing Peng]]"
last_author: "[[Sophia Ananiadou Qianqian Xie]]"
authors: "Xueqing Peng, Triantafillos Papadopoulos, Efstathia Soufleri, Polydoros Giannouris, Ruoyu Xiang, Yan Wang, Lingfei Qian, Jimin Huang, Qianqian Xie, Sophia Ananiadou"
url: "https://arxiv.org/abs/2502.18772"
external_pdf: "https://arxiv.org/pdf/2502.18772.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Peng-Plutus Benchmarking Large Language Models in Low-Resource Greek.md"
local_pdf: "[[PDFs/2025/2025-Peng-Plutus Benchmarking Large Language Models in Low-Resource Greek.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Greek"
languages_list: Greek
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-4o, Claude-3.5-Sonnet, Gemini-Pro, Llama-3.1, Qwen-2.5, DeepSeek-V3, Mistral-Large, Command-R-Plus, Aya-Expanse, GLM-4, InternLM, EXAONE, Plutus-8B"
DATA_URL: "https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms-67bc718fb8d897c65f1e87db"
tags: 
abstract: "Despite Greece’s pivotal role in the global economy, large language models (LLMs) remain underexplored for Greek financial context due to the linguistic complexity of Greek and the scarcity of domainspecific datasets. Previous efforts in multilingual financial natural language processing (NLP) have exposed considerable performance disparities, yet no dedicated Greek financial benchmarks or Greekspecific financial LLMs have been developed until now."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "NLP & Representation Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# Plutus: Benchmarking Large Language Models in Low-Resource Greek Finance

## Authors

[[Triantafillos Papadopoulos Xueqing Peng]], [[Polydoros Giannouris Efstathia Soufleri]], [[Yang Xiang|Yan Wang Ruoyu Xiang]], [[Jing Qian|Jimin Huang Lingfei Qian]], [[Sang Michael Xie|Sophia Ananiadou Qianqian Xie]]

## Metadata

**Authors:** Xueqing Peng, Triantafillos Papadopoulos, Efstathia Soufleri, Polydoros Giannouris, Ruoyu Xiang, Yan Wang, Lingfei Qian, Jimin Huang, Qianqian Xie, Sophia Ananiadou

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

**Benchmark:** Plutus-ben

## Links

- **arXiv:** https://arxiv.org/abs/2502.18772
- **Code/Data:** https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms-67bc718fb8d897c65f1e87db

## Abstract

The first Greek Financial Evaluation Benchmark addressing five core financial NLP tasks: numeric and textual NER, QA, abstractive summarization, and topic classification. Comprehensive evaluation of 22 LLMs reveals that Greek financial NLP remains challenging. Includes Plutus-8B, the first Greek financial LLM.

## Summary

This paper introduces Plutus-ben, the first comprehensive benchmark for evaluating LLMs on Greek financial tasks, and Plutus-8B, the first Greek-specific financial LLM. The benchmark covers five core tasks including numeric and textual named entity recognition, question answering, abstractive summarization, and topic classification, using three novel datasets annotated by expert native Greek speakers plus two existing resources. Evaluation of 22 models including GPT-4o, Claude-3.5-Sonnet, and domain-specific models reveals that Greek financial NLP remains challenging due to linguistic complexity and domain-specific terminology, with Plutus-8B surpassing GPT-4 by 15.38% and Deepseek-V3 by 93.55%.

## Data Description

Plutus-ben is the first Greek Financial Evaluation Benchmark addressing five core financial NLP tasks: numeric and textual NER, QA, abstractive summarization, and topic classification. Comprehensive evaluation of 22 LLMs reveals that Greek financial NLP remains challenging. Includes Plutus-8B, the first Greek financial LLM, plus three novel human-annotated datasets by expert native Greek speakers.


## Detailed Summary

This paper introduces Plutus-ben, the first comprehensive benchmark for evaluating LLMs on Greek financial tasks, alongside Plutus-8B, the pioneering Greek financial LLM. Despite Greece's significant role in the global economy (controlling over 20% of the world's merchant fleet), Greek financial NLP has been largely unexplored due to the language's complex morphology, inflectional system, and unique orthographic structures. Plutus-ben addresses five core financial NLP tasks: numeric named entity recognition, textual named entity recognition, question answering, abstractive summarization, and topic classification.

Three novel high-quality Greek financial datasets (GRFinNUM, GRFinNER, GRFinQA) are developed, each carefully annotated by expert native Greek speakers with deep financial and linguistic expertise, supplemented by two existing resources (GRFNS-2023 and GRMultiFin). The comprehensive evaluation of 22 LLMs -- including general-purpose models (GPT-4o, GPT-4, DeepSeek-V3, Llama-3-70B, Qwen2.5-72B), financial-specific models (Finma-7B, FinLLaMA-8B), and Greek-specific models (Meltemi-7B, Llama-Krikri-8B) -- reveals that Greek financial NLP remains challenging. Plutus-8B, fine-tuned on Greek domain-specific data, achieves the best overall performance, surpassing GPT-4 by 15.38%, GPT-4o by 46.34%, and DeepSeek-V3 by 93.55%, demonstrating the necessity of domain-specific adaptation for Greek financial tasks.

## Paper Outline

1. Introduction - Greek's role in global finance and the absence of dedicated benchmarks
2. Related Work - Financial LLMs and benchmarks for other languages
3. Plutus-ben Benchmark - Five tasks, dataset construction, and annotation
4. Plutus-8B - Greek financial LLM development
5. Experimental Setup - Models evaluated and evaluation metrics
6. Results - Comprehensive model comparison
7. Conclusion

## Methods Summary

Three novel datasets are annotated by expert native Greek speakers following strict standardized guidelines: GRFinNUM (numeric NER from financial reports), GRFinNER (textual NER from financial documents), and GRFinQA (financial question answering from university exams and reports). These are supplemented by GRFNS-2023 (financial news summarization) and GRMultiFin (topic classification). Twenty-two LLMs are evaluated spanning general-purpose models (various sizes from 1B to 72B), financial-specific English models, and Greek-specific models. Plutus-8B is developed by fine-tuning on curated Greek domain-specific financial data. Evaluation metrics include standard NER metrics, QA accuracy, summarization quality measures, and classification F1.

## Results Summary

Plutus-8B achieves the best overall performance across the five tasks, surpassing GPT-4 by 15.38%, GPT-4o by 46.34%, and DeepSeek-V3 by 93.55%. Greek-specific models (Meltemi-7B, Llama-Krikri-8B) outperform general multilingual models of similar size, confirming the importance of language-specific pre-training. English financial LLMs (Finma-7B, FinLLaMA-8B) show poor transfer to Greek financial tasks, underscoring the limitations of cross-lingual transfer for domain-specific applications. Larger general-purpose models (GPT-4, Qwen2.5-72B) show moderate performance but are consistently outperformed by the smaller domain-adapted Plutus-8B. The results demonstrate that both language-specific and domain-specific adaptation are necessary for Greek financial NLP.

## Conclusions

The study demonstrates that Greek financial NLP remains challenging due to linguistic complexity, domain-specific terminology, and financial reasoning gaps. Limitations include the relatively small size of the annotated datasets and the focus on five specific financial tasks. Future work includes expanding the benchmark with additional tasks (e.g., financial sentiment analysis, risk assessment), creating larger annotated datasets, and developing more sophisticated Greek financial LLMs through continued pre-training on larger financial corpora.

## Artifact Contributions

- **Plutus-ben**: First Greek Financial Evaluation Benchmark with five core tasks (https://huggingface.co/collections/TheFinAI/plutus-benchmarking-greek-financial-llms-67bc718fb8d897c65f1e87db)
- **Plutus-8B**: First Greek Financial LLM fine-tuned on domain-specific data
- **GRFinNUM, GRFinNER, GRFinQA**: Three novel high-quality Greek financial datasets annotated by expert native speakers

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Domain-specific Greek benchmark for financial NLP. Evaluates fairness and accuracy of LLMs in Greek financial context. Three novel human-annotated datasets by expert native Greek speakers.

## Tags

