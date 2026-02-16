---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0546
type: preprint
short_title: "MELABenchv1: Benchmarking Large Language Models against Smaller Fine-Tuned Models for Low-Resource Maltese NLP"
year: 2025
first_author: "[[Kurt Micallef]]"
last_author: "[[Claudia Borg Kurt Micallef]]"
authors: "Kurt Micallef, Claudia Borg"
url: "https://arxiv.org/abs/2506.04385"
external_pdf: "https://arxiv.org/pdf/2506.04385.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Micallef-MELABenchv1 Benchmarking Large Language Models against Smaller.md"
local_pdf: "[[PDFs/2025/2025-Micallef-MELABenchv1 Benchmarking Large Language Models against Smaller.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Maltese"
languages_list: Maltese
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Llama-3.1, Gemma, Qwen, Mistral, Aya, mBERT, XLM-RoBERTa"
DATA_URL: "https://huggingface.co/MLRS"
tags: 
abstract: "Large Language Models (LLMs) have demonstrated remarkable performance across various Natural Language Processing (NLP) tasks, largely due to their generalisability and ability to perform tasks without additional training. However, their effectiveness for low-resource languages remains limited. In this study, we evaluate the performance of 55 publicly available LLMs on Maltese, a low-resource language, using a newly introduced benchmark covering 11 discriminative and generative tasks."
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
---
# MELABenchv1: Benchmarking Large Language Models against Smaller Fine-Tuned Models for Low-Resource Maltese NLP

## Authors

[[Claudia Borg Kurt Micallef]]

## Metadata

**Authors:** Kurt Micallef, Claudia Borg

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Maltese

**Benchmark:** MELABenchv1

## Links

- **arXiv:** https://arxiv.org/abs/2506.04385
- **Code/Data:** https://huggingface.co/MLRS

## Abstract

Evaluates 55 LLMs on Maltese using 11 discriminative and generative tasks including sentiment, SIB-200, Taxi1500, Belebele, news categories, and MultiEURLEX. Finds many models perform poorly, especially on generative tasks. Smaller fine-tuned models often outperform larger LLMs across all tasks.

## Summary

This paper introduces MELABenchv1, a comprehensive benchmark evaluating 55 publicly available LLMs on Maltese, a low-resource EU language, across 11 discriminative and generative tasks. The authors test models including Llama-3.1, Gemma, Qwen, Mistral, and fine-tuned models like mBERT and XLM-RoBERTa using both zero-shot and one-shot prompting. Results reveal that many LLMs perform poorly on Maltese, particularly on generative tasks, with smaller fine-tuned models often outperforming much larger LLMs, highlighting that prior exposure to Maltese during pre-training emerges as the most important factor for performance.

## Data Description

MELABenchv1 is a comprehensive benchmark evaluating 55 LLMs on Maltese using 11 discriminative and generative tasks including sentiment, SIB-200, Taxi1500, Belebele, news categories, and MultiEURLEX. Finds many models perform poorly, especially on generative tasks. Smaller fine-tuned models often outperform larger LLMs across all tasks, highlighting the importance of prior exposure to Maltese during pre-training.


## Detailed Summary

This paper introduces MELABenchv1, a comprehensive evaluation benchmark for Maltese, an official EU language that ranks lowest on the Digital Language Equality score. The benchmark covers 11 discriminative and generative tasks including sentiment analysis, topic classification (SIB-200, Taxi1500), reading comprehension (Belebele), news categorization, legal classification (MultiEURLEX), machine translation (OPUS-100, Flores-200), data-to-text generation (WebNLG), summarization (EUR-Lex-Sum), and headline generation (Maltese News Headlines). The authors evaluate 55 publicly available LLMs ranging from 300M to 15B parameters, with varying language coverage and training stages.

The study reveals that many LLMs perform poorly on Maltese, particularly on generative tasks, and that smaller fine-tuned models (BERTu, mT5-Small) often outperform much larger LLMs across all tasks. Through multidimensional analysis, the authors find that prior exposure to Maltese during pre-training and instruction-tuning emerges as the most important factor for downstream task performance. The work also examines trade-offs between fine-tuning and prompting: while fine-tuning requires a higher initial cost, it yields better performance and lower inference costs. The benchmark and best-performing fine-tuned models are made publicly available to promote development of more inclusive language technologies for Maltese.

## Paper Outline

1. Introduction - Motivation and research questions
2. Experimental Setup - Evaluation benchmark, models, and evaluation methodology
3. Results - LLM performance analysis, factor analysis, and fine-tuning comparison
4. Related Work - Prior multilingual and low-resource language evaluations
5. Conclusion - Recommendations for low-resource language researchers

## Methods Summary

The evaluation uses the Language Model Evaluation Harness framework with task-specific templates and instructions. Fifty-five LLMs are tested in zero-shot and one-shot settings with both English and Maltese instructions. Models span various sizes (300M-15B), language coverages (18-511 languages), and training stages (pre-trained vs. instruction-tuned). Fine-tuned baselines include BERTu (Maltese BERT) and mT5-Small. Evaluation metrics include macro-averaged F1 for classification tasks, accuracy for Belebele, ChrF scores for translation tasks, and Rouge-L for summarization. The analysis examines correlations between model properties (size, language coverage, Maltese exposure during training) and downstream task performance.

## Results Summary

Smaller fine-tuned models (BERTu, mT5-Small) consistently outperform or match the best LLMs across all 11 tasks, despite having orders of magnitude fewer parameters. Among LLMs, models with explicit Maltese exposure during pre-training or instruction-tuning perform significantly better than those without it. Model size alone does not guarantee strong performance for Maltese -- larger models without Maltese training data can perform worse than smaller models with it. Instruction-tuned models generally outperform pre-trained-only models, and one-shot prompting improves performance over zero-shot for most tasks. The analysis recommends that researchers working with low-resource languages consider more "traditional" language modeling approaches.

## Conclusions

The study concludes that the LLM paradigm, while powerful for high-resource languages, does not straightforwardly transfer to low-resource languages like Maltese. The most critical factor for performance is prior language exposure during training, not model scale. Limitations include the focus on publicly available models only and the exclusion of very large proprietary models from the main evaluation. Future work includes expanding the benchmark with additional Maltese tasks, evaluating newer models as they become available, and investigating methods to improve Maltese performance without requiring Maltese-specific training data.

## Artifact Contributions

- **MELABenchv1**: Comprehensive Maltese NLP benchmark with 11 tasks (https://huggingface.co/spaces/MLRS/MELABench)
- **Fine-tuned BERTu Models**: Best-performing fine-tuned models for Maltese tasks (https://huggingface.co/collections/MLRS/bertu-683ac54c1b6ab3ae715cb43d)
- **Fine-tuned mT5-Small Models**: Best-performing generative models for Maltese tasks (https://huggingface.co/collections/MLRS/mt5-small-683eecd001179a722c98298b)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** First comprehensive Maltese LLM benchmark. Evaluates equitable AI performance for low-resource Maltese. Directly relevant to fairness in multilingual LLM deployment.

## Tags

