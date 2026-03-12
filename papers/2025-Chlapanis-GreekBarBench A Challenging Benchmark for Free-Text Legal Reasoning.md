---

























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0531
type: preprint
short_title: "GreekBarBench: A Challenging Benchmark for Free-Text Legal Reasoning and Citations"
year: 2025
first_author: "[[Odysseas S. Chlapanis]]"
last_author: "[[Ion Androutsopoulos]]"
authors: Odysseas S. Chlapanis; Dimitrios Galanis; Nikolaos Aletras; Ion Androutsopoulos
url: "https://arxiv.org/abs/2505.17267"
external_pdf: "https://arxiv.org/pdf/2505.17267.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2025/2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning.md"
local_pdf: "[[PDFs/2025/2025-Chlapanis-GreekBarBench A Challenging Benchmark for Free-Text Legal Reasoning.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Greek"
languages_list: Greek
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-4o, GPT-4o-mini, GPT-4-Turbo, Claude-3.5-Sonnet, Claude-3-Opus, Gemini-1.5-Pro, Llama-3.1-405B, Llama-3.1-70B, Llama-3.1-8B, Mistral-Large, Qwen2.5-72B, DeepSeek-V3, Command-R-Plus"
DATA_URL: "https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench"
tags: 
abstract: "We introduce GREEKBARBENCH, a benchmark that evaluates LLMs on legal questions across five different legal areas from the Greek Bar exams, requiring citations to statutory articles and case facts. To tackle the challenges of free-text evaluation, we propose a threedimensional scoring system combined with an LLM-as-a-judge approach. We also develop a meta-evaluation benchmark to assess the correlation between LLM-judges and human expert evaluations, revealing that simple, span-based rubrics..."
ethics_perspective: "AI Safety & Alignment"
CONFERENCE: "Preprint"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
---
# GreekBarBench: A Challenging Benchmark for Free-Text Legal Reasoning and Citations

## Authors

[[Odysseas S. Chlapanis]], [[Dimitrios Galanis]], [[Nikolaos Aletras]], [[Ion Androutsopoulos]]

## Metadata

**Authors:** Odysseas S. Chlapanis, Dimitrios Galanis, Nikolaos Aletras, Ion Androutsopoulos

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Greek

**Benchmark:** GreekBarBench

## Links

- **arXiv:** https://arxiv.org/abs/2505.17267
- **Code/Data:** https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench

## Abstract

A benchmark evaluating LLMs on legal questions from Greek Bar exams (2015-2024) across five legal areas, requiring citations to statutory articles and case facts. Uses a three-dimensional scoring system with LLM-as-a-judge approach. Evaluation of 13 proprietary and open-weight LLMs shows best models outperform average expert scores but fall short of 95th percentile.

## Summary

This paper introduces GreekBarBench, a benchmark derived from Greek Bar exam questions (2015-2024) covering five legal areas requiring free-text answers with citations to statutory articles and case facts. The authors develop a three-dimensional scoring system (Facts, Cited Articles, Analysis) and an LLM-as-a-judge framework using span-based rubrics. Evaluation of 13 models including GPT-4o, Claude-3.5-Sonnet, and Llama-3.1 reveals that top-performing models exceed average expert scores but remain susceptible to critical errors, particularly in identifying correct statutory articles.

## Data Description

GreekBarBench is a benchmark evaluating LLMs on legal questions from Greek Bar exams (2015-2024) across five legal areas, requiring citations to statutory articles and case facts. Uses a three-dimensional scoring system (Facts, Cited Articles, Analysis) with LLM-as-a-judge approach. Best models outperform average expert scores but fall short of 95th percentile.


## Detailed Summary

This paper introduces GreekBarBench (GBB), a benchmark that evaluates LLMs on legal questions from the Greek Bar exams (2015-2024) across five legal areas: Civil Law, Criminal Law, Commercial Law, Public Law, and Lawyers' Code. Unlike most existing legal benchmarks that rely on closed-form questions (e.g., multiple choice), GBB requires free-text answers with citations to statutory articles and case facts, capturing the true complexity of legal reasoning in practice. The benchmark addresses a critical gap as the only Greek dataset for legal reasoning.

To tackle the challenges of evaluating free-text legal responses, the authors propose a three-dimensional scoring system covering Facts (identifying relevant case facts), Cited Articles (referencing correct statutory articles), and Analysis (legal reasoning quality). They develop an LLM-as-a-judge framework using span-based rubrics per dimension, which aligns well with human expert evaluation. An accompanying meta-evaluation benchmark (GBB-JME) with human-evaluated answers from five LLMs is introduced to assess judge quality. Evaluation of 13 proprietary and open-weight LLMs, including GPT-4o, Claude-3.5-Sonnet, Llama-3.1, and DeepSeek-V3, reveals that top models exhibit impressive performance exceeding average expert scores but remain susceptible to critical errors, most notably failing to identify correct statutory articles.

## Paper Outline

1. Introduction - Need for realistic legal LLM benchmarks
2. GreekBarBench (GBB) - Greek Bar Exam structure and benchmark design
3. GBB-JME - Meta-evaluation benchmark for LLM judges
4. LLM-as-a-Judge Framework - Three-dimensional scoring with span-based rubrics
5. Experimental Setup - Models evaluated and evaluation methodology
6. Results - Model performance and error analysis
7. Related Work - Comparison with existing legal benchmarks
8. Conclusion

## Methods Summary

The benchmark draws questions from Greek Bar exams requiring free-text answers with citations. The evaluation employs a three-dimensional scoring system (Facts, Cited Articles, Analysis) combined with an LLM-as-a-judge approach using span-based rubrics. The meta-evaluation benchmark GBB-JME contains human expert evaluations against five LLM-generated answers to calibrate judge quality. Thirteen models are evaluated: proprietary (GPT-4o, GPT-4o-mini, GPT-4-Turbo, Claude-3.5-Sonnet, Claude-3-Opus, Gemini-1.5-Pro) and open-weight (Llama-3.1-405B/70B/8B, Mistral-Large, Qwen2.5-72B, DeepSeek-V3, Command-R-Plus). Manual error analysis identifies weaknesses in model responses.

## Results Summary

Top-performing models outperform average expert scores on the benchmark but fall short of the 95th percentile of expert performance. GPT-4o and Claude-3.5-Sonnet lead among proprietary models, while DeepSeek-V3 and Qwen2.5-72B perform well among open-weight models. The most critical weakness across all models is failure to identify correct statutory articles, highlighting a fundamental gap in legal knowledge retrieval. The span-based rubric approach for LLM judges shows strong correlation with human expert evaluations, demonstrating that simple, structured rubrics improve judge alignment. Error analysis reveals that models sometimes fabricate non-existent legal articles and fail at multi-hop reasoning required for complex legal scenarios.

## Conclusions

The study demonstrates that while current LLMs show impressive legal reasoning capabilities in Greek, they remain unreliable for practical legal applications due to critical errors in statutory article identification. Limitations include the focus on Greek law only and the reliance on LLM-as-a-judge evaluation. Future work includes expanding to other jurisdictions, developing retrieval-augmented approaches for legal article identification, and improving evaluation methodology for free-text legal responses.

## Artifact Contributions

- **GreekBarBench**: Greek Bar exam legal reasoning benchmark (https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench)
- **GBB-JME**: Meta-evaluation benchmark for LLM judges with human expert evaluations
- **Code and Prompts**: Evaluation code and prompts (https://github.com/nlpaueb/greek-bar-bench)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Greek legal reasoning benchmark with cultural and jurisdictional specificity. Evaluates ethical and legal reasoning capabilities in Greek. Relevant to fairness and justice-related evaluation.

## Tags

