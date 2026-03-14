---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0550
type: preprint
short_title: "The AI Language Proficiency Monitor -- Tracking the Progress of LLMs on Multilingual Benchmarks"
year: 2025
first_author: "[[David Pomerenke]]"
last_author: "[[Simon Ostermann]]"
authors: David Pomerenke; Jonas Nothnagel; Simon Ostermann
url: "https://arxiv.org/abs/2507.08538"
external_pdf: "https://arxiv.org/pdf/2507.08538.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs.md"
local_pdf: "[[PDFs/2025/2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
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
LLM_assessed: "Gemma, Llama-3"
DATA_URL: "https://github.com/datenlabor-bmz/evals-for-every-language"
tags: 
abstract: "To ensure equitable access to the benefits of large language models (LLMs), it is essential to evaluate their capabilities across the world’s languages. We introduce the AI Language Proficiency Monitor, a comprehensive multilingual benchmark that systematically assesses LLM performance across up to 200 languages, with a particular focus on low-resource languages. Our benchmark aggregates diverse tasks including translation, question answering, math, and reasoning, using datasets such as..."
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Translation"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark"
data_metrics: "200 languages"
---
# The AI Language Proficiency Monitor -- Tracking the Progress of LLMs on Multilingual Benchmarks

## Authors

[[David Pomerenke]], [[Jonas Nothnagel]], [[Simon Ostermann]]

## Metadata

**Authors:** David Pomerenke, Jonas Nothnagel, Simon Ostermann

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Up to 200 languages including Greek, Georgian, Armenian, Albanian, Maltese

**Benchmark:** AI Language Proficiency Monitor

## Links

- **arXiv:** https://arxiv.org/abs/2507.08538

## Abstract

Comprehensive multilingual benchmark systematically assessing LLM performance across up to 200 languages with focus on low-resource languages. Aggregates tasks including translation, QA, math, and reasoning using FLORES+, MMLU, GSM8K, TruthfulQA, and ARC. Provides auto-updating leaderboard and dashboard.

## Summary

This paper presents the AI Language Proficiency Monitor, a comprehensive multilingual benchmark systematically assessing LLM performance across up to 200 languages including Greek, Georgian, Armenian, Albanian, and Maltese, with particular focus on low-resource languages. The benchmark aggregates diverse tasks including translation (FLORES+), question answering (MMLU, ARC), math (GSM8K), and reasoning (TruthfulQA), providing an open-source auto-updating leaderboard and dashboard with descriptive analyses including global proficiency maps and temporal trends. The system aims to support researchers, developers, and policymakers in identifying strengths and gaps in model performance, fostering transparency and inclusivity in multilingual AI.

## Data Description

The AI Language Proficiency Monitor is an auto-updating leaderboard and dashboard that aggregates existing multilingual benchmark datasets (FLORES+, MMLU, GSM8K, TruthfulQA, ARC) to evaluate LLMs across up to 200 languages. No new dataset is created; the contribution is the evaluation pipeline and interactive platform hosted at https://huggingface.co/spaces/fair-forward/evals-for-every-language.


## Detailed Summary

This paper presents the AI Language Proficiency Monitor, a comprehensive multilingual benchmark that systematically assesses LLM performance across up to 200 languages, with particular focus on low-resource languages. The benchmark aggregates diverse tasks including translation (FLORES+), multi-domain question answering (MMLU), advanced question answering (ARC), math problems (GSM8K), and factuality assessment (TruthfulQA), covering 80-95% of the world's speakers depending on the task. Depending on the task, 100-200 languages are evaluated, including many low-resource languages such as Greek, Georgian, Armenian, Albanian, and Maltese.

The system provides an open-source, auto-updating leaderboard and dashboard that evaluates state-of-the-art models from commercial AI providers and relevant open-weights models, auto-evaluating daily to include the latest models. Beyond model ranking, the platform offers descriptive analyses including a global map of country-level AI language proficiency scores, progress trends over time for high-resource versus low-resource languages, and analysis of how factors like number of speakers, GDP, and data availability impact AI language proficiency. The system is designed to serve three primary user groups: researchers and model developers for benchmarking, practitioners for identifying suitable models for specific languages, and policymakers and donor agencies for identifying languages where capacity-building is most urgent.

## Paper Outline

1. Introduction - Motivation and primary use cases
2. Background and Related Work - Existing multilingual evaluation benchmarks
3. Benchmark Design - Task selection, language coverage, evaluation methodology
4. Dashboard and Leaderboard - Interface design and descriptive analyses
5. Results and Analysis - Current state of multilingual AI proficiency
6. Conclusion

## Methods Summary

The benchmark relies on multilingual versions of established evaluation datasets: FLORES+ for translation and classification (200 languages), MMLU for multi-domain question answering, ARC for advanced reasoning, GSM8K for math problems, and TruthfulQA for factuality. Machine translation is used to achieve comprehensive language coverage. The system auto-evaluates daily through an automated pipeline, always including the latest relevant models. An "AI Language Proficiency Score" serves as a multi-task multilingual performance metric for overall model comparison. The dashboard includes language-specific leaderboards, a global proficiency map with country-level scores, and temporal trend analysis.

## Results Summary

The analysis reveals significant disparities in LLM performance across languages, with high-resource languages consistently outperforming low-resource ones. The global proficiency map shows strong correlation between AI language proficiency and factors such as data availability and economic resources. Progress over time shows that while performance improves for both high- and low-resource languages, the gap persists. The system covers more than twice the number of languages compared to similar benchmarks like MEGAVERSE, while providing user-friendly visualizations and language-specific leaderboards accessible to non-technical practitioners.

## Conclusions

The AI Language Proficiency Monitor aims to foster transparency, inclusivity, and progress in multilingual AI by providing a continuously updated assessment framework. Limitations include reliance on machine-translated benchmarks for many languages (which may introduce artifacts), incomplete coverage of the most resource-lean languages, and the focus on text-based tasks only. Future work includes integrating additional tasks and languages, partnering with regional AI developers to include locally fine-tuned models, and expanding the system to address multimodal capabilities.

## Artifact Contributions

- **AI Language Proficiency Monitor**: Open-source auto-updating dashboard and leaderboard (https://huggingface.co/spaces/fair-forward/evals-for-every-language)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Covers all five target languages within a 200-language evaluation framework. Includes safety-relevant TruthfulQA. Auto-updating dashboard for tracking progress across low-resource languages.

## Tags

