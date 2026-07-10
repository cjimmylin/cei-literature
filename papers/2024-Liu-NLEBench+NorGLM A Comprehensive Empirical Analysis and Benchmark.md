---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0480
type: preprint
short_title: "NLEBench+NorGLM: A Comprehensive Empirical Analysis and Benchmark Dataset for Generative Language Models in Norwegian"
year: 2025
first_author: "[[Liu, Peng]]"
last_author: "[[Yang, Zhirong]]"
authors: "Liu, Peng; Zhang, Lemei; Farup, Terje; Even W. Lauvrak; Ingvaldsen, Jon Espen; Eide, Simen; Gulla, Jon Atle; Yang, Zhirong"
authors_incomplete: false
url: "https://arxiv.org/abs/2312.01314"
external_pdf: "https://arxiv.org/pdf/2312.01314.pdf"
publication: "arXiv / EMNLP 2024"
CONF-CC: "EMNLP 2024"
pdf_extract: "PDF Extracts/2024/2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Norwegian
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: GPT-3.5
DATA_URL: "https://github.com/Smartmedia-AI/NorGLM"
tags: 
abstract: "Norwegian, spoken by only 5 million population, is under-representative within the most impressive breakthroughs in NLP tasks. To the best of our knowledge, there has not yet been a comprehensive evaluation of the existing language models (LMs) on Norwegian generation tasks during the article writing process. To fill this gap, we 1) compiled the existing Norwegian dataset and pre-trained 4 Norwegian Open Language Models varied from parameter scales and architectures, collectively called NorGLM;..."
research_topic: "Machine Learning"
CONFERENCE: "EMNLP 2024"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness annotated dataset for toxicity detection"
data_metrics: "Not specified"
---
# NLEBench+NorGLM: A Comprehensive Empirical Analysis and Benchmark Dataset for Generative Language Models in Norwegian

## Authors

[[Liu, Peng]], [[Zhang, Lemei]], [[Farup, Terje]], [[Lauvrak, Even W]], [[Ingvaldsen, Jon Espen]], [[Eide, Simen]], [[Gulla, Jon Atle]], [[Yang, Zhirong]]

## Metadata

**Authors:** Liu, Peng; Zhang, Lemei; Farup, Terje; Lauvrak, Even W.; Ingvaldsen, Jon Espen; Eide, Simen; Gulla, Jon Atle; Yang, Zhirong

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / EMNLP 2024

**Languages:** Norwegian

**Benchmark:** NLEBench

## Links

- **arXiv:** https://arxiv.org/abs/2312.01314
- **Code/Data:** https://github.com/Smartmedia-AI/NorGLM

## Abstract

Comprehensive Norwegian generative LM benchmark including toxicity and bias evaluation, instruction fine-tuning, and Chain-of-Thought investigation. Includes human-annotated datasets covering Norwegian culture, idioms, and expressions. Published at EMNLP 2024.

## Summary

This paper presents NLEBench, a comprehensive benchmark for evaluating generative language models in Norwegian, alongside NorGLM, a family of four Norwegian open language models (varying from 369M to 23B parameters) pre-trained on Norwegian data. The benchmark encompasses multiple natural language generation tasks including translation, toxicity and bias evaluation, instruction fine-tuning, and Chain-of-Thought reasoning, with human-annotated datasets specifically covering Norwegian culture, idioms, and expressions. Key findings include that GPT-3.5 has limited Norwegian understanding, parameter scaling shows limited impact when pre-training data is constrained, and smaller models can demonstrate reasoning capability through Chain-of-Thought prompting.

## Data Description

NLEBench: a comprehensive Norwegian NLG benchmark covering translation, summarization, dialogue generation, and instruction following; includes human-annotated datasets on Norwegian culture, idioms, and expressions. Also introduces four Norwegian open language models (NorGPT-369M, NorGPT-3B, NorGPT-23B, NorLlama-3B) collectively called NorGLM.


## Detailed Summary

This paper presents NLEBench, the first comprehensive benchmark for evaluating generative language models in Norwegian, alongside NorGLM, a family of four Norwegian open language models based on GPT-2 and Llama architectures (369M to 23B parameters). The benchmark is designed to probe Norwegian-specific capabilities including cultural knowledge, idiomatic expressions, and multi-task reasoning, going beyond translated English datasets. The NorGLM models are trained from scratch on a multi-source corpus including mC4, OSCAR, Norwegian National Library materials, Schibsted news articles, tweets, and Reddit posts, supplemented with Danish, Swedish, German, and English text for robustness. The work addresses the gap in evaluation resources for Norwegian, a low-resource language with only 5 million speakers.

## Paper Outline

1. Introduction - Gap in Norwegian GLM evaluation
2. Related Work - Language models for low-resource languages, multi-task benchmarks
3. Norwegian Generative Language Model Suite (NorGLM) - Architecture, training data, model variants
4. Norwegian Benchmark Dataset (NLEBench) - Tasks, dataset categories, evaluation settings
5. Experiments and Results - Performance comparisons across models
6. Conclusion

## Methods Summary

NorGLM models (NorGPT-369M, NorGPT-3B, NorGPT-23B, NorLlama-3B) are trained from scratch using multi-source Norwegian data. The benchmark NLEBench includes: existing Norwegian datasets, machine-translated datasets (via Google Translation API, validated by native speakers), and manually annotated datasets. Tasks span instruction following with Norwegian cultural content, document-grounded multi-task evaluation (question answering, summarization), and Chain-of-Thought reasoning. GPT-3.5-Turbo serves as a commercial baseline. Pre-training data is carefully curated to avoid overlap with benchmark data.

## Results Summary

Key findings include: (1) GPT-3.5 shows limited capability in understanding Norwegian context despite being the dominant English LLM; (2) increasing model parameter scales has limited impact on downstream task performance when pre-training data is size-constrained; (3) smaller models can demonstrate Chain-of-Thought reasoning capability; (4) multi-task datasets with synergy tasks effectively verify LLM generalizability on natural language understanding. NB-GPT-J-6B, continued-trained from English GPT-J-6B on a dataset 20x larger than NorGLM's training data, provides an informative comparison between training-from-scratch and continued-pretraining approaches.

## Conclusions

NLEBench fills a critical evaluation gap for Norwegian generative language models by providing culturally-specific and multi-task benchmarks. The work demonstrates that dedicated language-specific benchmarks are essential for understanding LLM capabilities in low-resource languages, as English-dominated models show significant limitations in Norwegian contexts. The resources are released under CC BY-NC 4.0 license for reproducibility.

## Artifact Contributions

- **NLEBench benchmark**: First comprehensive Norwegian GLM evaluation suite with culture-specific tasks
- **NorGLM models**: Four Norwegian generative language models (369M-23B parameters)
- **Norwegian instruction dataset**: Human-written instructions specific to Norwegian culture and expressions
- **Document-grounded multi-task dataset**: Human-annotated QA pairs and summaries
- **Code and data**: https://github.com/Smartmedia-AI/NorGLM

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Norwegian benchmark explicitly including toxicity and bias evaluation dimensions alongside cultural content.

## Tags

