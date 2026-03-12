---

























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0436
type: preprint
short_title: "LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models"
year: 2025
first_author: "[[Ning, Zhiyuan]]"
last_author: "[[Wang, Yingchun]]"
authors: "Ning, Zhiyuan; Gu, Tianle; Song, Jiaxin; Hong, Shixin; Li, Lingyu; Liu, Huacan; Li, Jie; Wang, Yixu; Lingyu, Meng; Teng, Yan; Wang, Yingchun"
authors_incomplete: false
url: "https://arxiv.org/abs/2508.12733"
external_pdf: "https://arxiv.org/pdf/2508.12733.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Ning-LinguaSafe A Comprehensive Multilingual Safety Benchmark for Large.md"
local_pdf: "[[PDFs/2025/2025-Ning-LinguaSafe A Comprehensive Multilingual Safety Benchmark for Large.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: "12 languages including French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Claude-3.5-Sonnet, GPT-4o, Gemini-Pro, Llama-3, Qwen, DeepSeek"
DATA_URL: "https://huggingface.co/datasets/telegraphpolehead/linguasafe"
tags: 
abstract: "The widespread adoption and increasing prominence of large language models (LLMs) in global technologies necessitate a rigorous focus on ensuring their safety across a diverse range of linguistic and cultural contexts. The lack of a comprehensive evaluation and diverse data in existing multilingual safety evaluations for LLMs limits their effectiveness, hindering the development of robust multilingual safety alignment."
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Multilingual benchmark for ai safety"
data_metrics: "12 languages"
---
# LinguaSafe: A Comprehensive Multilingual Safety Benchmark for Large Language Models

## Authors

[[Ning, Zhiyuan]], [[Gu, Tianle]], [[Song, Jiaxin]], [[Hong, Shixin]], [[Li, Lingyu]], [[Liu, Huacan]], [[Li, Jie]], [[Yixu Wang|Wang, Yixu]], [[Lingyu, Meng]], [[Yan Teng|Teng, Yan]], [[Yingchun Wang|Wang, Yingchun]]

## Metadata

**Authors:** Ning, Zhiyuan; Gu, Tianle; Song, Jiaxin; Hong, Shixin; Li, Lingyu; Liu, Huacan; Li, Jie; Wang, Yixu; Lingyu, Meng; Teng, Yan; Wang, Yingchun

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** 12 languages including French

**Benchmark:** LinguaSafe

## Links

- **arXiv:** https://arxiv.org/abs/2508.12733

## Abstract

Comprehensive multilingual safety benchmark with 45K entries in 12 languages curated using translated, transcreated, and natively-sourced data. Introduces TATER (Task-Aware Translate, Estimate, and Refine) framework. Finds safety performance varies dramatically across languages with English typically surpassing others.

## Summary

This paper introduces LinguaSafe, a comprehensive multilingual safety benchmark containing 45,000 entries across 12 languages including French, Hungarian, and Malay, curated using translated, transcreated, and natively-sourced data. The authors develop the TATER (Task-Aware Translate, Estimate, and Refine) framework to improve multilingual data quality and introduce a multidimensional evaluation framework with direct and indirect safety assessments including oversensitivity evaluation. Evaluation of models including Claude-3.5-Sonnet, GPT-4o, and Llama-3 reveals that safety performance varies dramatically across languages with English typically surpassing others, and Claude-3.5-Sonnet achieves the lowest vulnerability.

## Data Description

LinguaSafe is a comprehensive multilingual safety benchmark with 45,000 entries in 12 languages (including French) curated using translated, transcreated, and natively-sourced data. Introduces TATER (Task-Aware Translate, Estimate, and Refine) framework for safety evaluation. Finds safety performance varies dramatically across languages with English typically surpassing others. Claude-3.5-Sonnet achieves lowest vulnerability.


## Detailed Summary

This paper introduces LinguaSafe, a comprehensive multilingual safety benchmark containing 45,000 entries across 12 languages ranging from high-resource (e.g., French) to low-resource (e.g., Hungarian, Malay, Bengali). The dataset addresses limitations of existing multilingual safety evaluations, which suffer from overdependence on translated data, limited language coverage, and narrow evaluation frameworks. LinguaSafe is curated using three data sourcing strategies: translation, transcreation (cultural adaptation), and native data collection, ensuring linguistic authenticity and diversity.

The authors develop the TATER (Task-Aware Translate, Estimate and Refine) framework, an adaptation of TEaR that improves the quality of LLM transcreation and the efficiency of human refinement for multilingual data. The dataset is organized into a hierarchical safety taxonomy with 5 safety domains and 23 subtypes, annotated with 4 levels of severity through collective human and AI judgment. The evaluation framework includes both direct and indirect safety assessments, with the indirect evaluation incorporating oversensitivity evaluation to assess the robustness of multilingual safety alignment. Evaluation of models including Claude-3.5-Sonnet, GPT-4o, Gemini-Pro, Llama-3, Qwen, and DeepSeek reveals that safety performance varies dramatically across languages, even among languages with similar resource levels, with English typically surpassing others. Claude-3.5-Sonnet achieves the lowest vulnerability across the benchmark.

## Paper Outline

1. Introduction - Multilingual safety challenges and motivation
2. Related Work - Existing multilingual safety benchmarks and their limitations
3. LinguaSafe Dataset - Data sourcing, TATER framework, taxonomy, and annotation
4. Evaluation Framework - Direct and indirect safety evaluations, oversensitivity assessment
5. Experiments - Model evaluation setup and metrics
6. Results - Cross-language and cross-domain safety analysis
7. Conclusion

## Methods Summary

Data is sourced through three strategies: translation from English safety datasets, transcreation using the TATER (Task-Aware Translate, Estimate and Refine) framework for cultural adaptation, and collection of native multilingual data. The dataset covers 12 languages across high-, medium-, and low-resource categories. Entries are organized into 5 safety domains and 23 subtypes with 4 severity levels annotated by human-AI collaboration. The evaluation framework includes direct evaluation (measuring model safety responses to harmful prompts with weighted severity scores) and indirect evaluation (assessing model behavior on benign prompts to detect oversensitivity). Metrics include weighted confusion matrices for nuanced assessment across safety domains and languages.

## Results Summary

Safety performance varies dramatically across languages and domains, with English typically outperforming other languages. Even languages with similar resource levels show significant performance differences, suggesting that resource level alone does not predict safety alignment quality. Claude-3.5-Sonnet achieves the lowest vulnerability across the benchmark, demonstrating the most robust multilingual safety alignment. The study reveals both undersensitivity (failing to detect harmful content in non-English languages) and oversensitivity (incorrectly flagging benign content) as significant issues. Native multilingual data elicits significantly more toxicity than translated data, confirming the importance of culturally grounded safety evaluation.

## Conclusions

The benchmark demonstrates that multilingual safety alignment remains a critical challenge, with significant disparities across languages. Limitations include coverage of only 12 languages (out of thousands worldwide) and potential biases in the TATER transcreation framework. Future work includes expanding language coverage, developing language-specific safety alignment techniques, and investigating the relationship between cultural context and safety perception across different linguistic communities.

## Artifact Contributions

- **LinguaSafe Dataset**: 45,000 multilingual safety entries across 12 languages (https://huggingface.co/datasets/telegraphpolehead/linguasafe)
- **LinguaSafe Code**: Evaluation framework and code (https://github.com/telegraph-pole-head/LinguaSafe)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Evaluates multilingual safety with French. TATER framework addresses limitations of direct translation for safety evaluation. Shows Claude-3.5-Sonnet achieves lowest vulnerability.

## Tags

