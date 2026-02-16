---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: GHNYTYDF
type: document
year: 2025
short_title: "HELM Safety"
first_author: "[[Farzaan Kaiyom]]"
last_author: "[[Percy Liang]]"
authors: "Farzaan Kaiyom; Ahmed Ahmed; Yifan Mai; Kevin Klyman; Rishi Bommasani; Percy Liang"
external_pdf: "file:///Users/jimmylin/Zotero/storage/5RFJXS3S/Kaiyom and others - HELM Safety Towards Standardized Safety Evaluations of Language Models.pdf"
pdf_extract: "PDF Extracts/2024/2024-Kaiyom-HELM Safety.md"
local_pdf: "[[PDFs/2024/2024-Kaiyom-HELM Safety.pdf]]"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Part of the Holistic Evaluation of Language Models (HELM), defining and implementing standardized safety evaluations across multiple models."
significance: "Moves safety evaluation from ad-hoc tests to a standardized, rigorous leaderboard entry, forcing all new models to report comparable safety metrics."
tags: 
abstract: "HELM Safety v1.0 is a broad, transparent, and standardized safety evaluation for language models. The evaluation covers a comprehensive taxonomy of risks based on developers' acceptable use policies, spanning violence, fraud, discrimination, sexual content, harassment, and deception. HELM Safety features evaluations including BBQ (social discrimination), SimpleSafetyTest, HarmBench (jailbreaking), XSTest (edge cases), and AnthropicRedTeam."
DATE_ADDED: 20260129
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Claude, Llama-3, Mistral, Mixtral, Qwen, DeepSeek"
DATA_URL: "https://github.com/stanford-crfm/helm"
---
# HELM Safety: Towards Standardized Safety Evaluations of Language Models

## Metadata

**Authors:** Kaiyom, Farzaan; Ahmed, Ahmed; Mai, Yifan; Klyman, Kevin; Bommasani, Rishi; Liang, Percy

**Type:** document

## Links

- **Stanford:** https://crfm.stanford.edu/2024/11/08/helm-safety.html
- **Github:** https://github.com/stanford-crfm/helm

## Abstract

HELM Safety v1.0 is a broad, transparent, and standardized safety evaluation for language models. The evaluation covers a comprehensive taxonomy of risks based on developers' acceptable use policies, spanning violence, fraud, discrimination, sexual content, harassment, and deception. HELM Safety features evaluations including BBQ (social discrimination), SimpleSafetyTest, HarmBench (jailbreaking), XSTest (edge cases), and AnthropicRedTeam.

## Authors

[[Farzaan Kaiyom]], [[Ahmed Ahmed]], [[Yifan Mai]], [[Kevin Klyman]], [[Rishi Bommasani]], [[Percy Liang]]

## Detailed Summary

HELM Safety v1.0 is a standardized safety evaluation framework for language models developed by Stanford CRFM as part of the broader Holistic Evaluation of Language Models (HELM) project. The framework provides broad, transparent, and comparable safety assessments based on a comprehensive taxonomy of risks derived from LLM developers' acceptable use policies. The evaluation covers critical risk categories including violence, fraud, discrimination, sexual content, harassment, and deception.

The framework aggregates and standardizes multiple existing safety benchmarks into a unified evaluation suite. It includes BBQ for social discrimination measurement, SimpleSafetyTest for basic safety compliance, HarmBench for jailbreaking resistance, XSTest for edge case handling, and AnthropicRedTeam for adversarial robustness. This integration enables fair cross-model comparison using consistent methodology.

The significance of HELM Safety lies in moving LLM safety evaluation from ad-hoc testing to rigorous, standardized benchmarking. By requiring all evaluated models to report comparable safety metrics, the framework creates accountability and enables progress tracking. The public leaderboard makes safety performance transparent to researchers, developers, and the broader public.

## Paper Outline

1. Introduction - Need for standardized safety evaluation
2. Background - Existing safety benchmarks and their limitations
3. Risk Taxonomy - Categories based on acceptable use policies
4. Benchmark Selection - BBQ, SimpleSafetyTest, HarmBench, XSTest, AnthropicRedTeam
5. Evaluation Methodology - Standardized testing protocols
6. Results - Cross-model safety comparison
7. Analysis - Performance patterns and vulnerabilities
8. Discussion - Implications for model development
9. Future Directions - Expanding the evaluation suite

## Methods Summary

The methodology encompasses: (1) Development of risk taxonomy from analyzing LLM developers' acceptable use policies across major providers. (2) Selection and integration of five established safety benchmarks covering distinct risk dimensions. (3) BBQ evaluates social discrimination through question-answering. (4) SimpleSafetyTest assesses basic safety guardrails. (5) HarmBench measures resistance to jailbreaking attacks. (6) XSTest examines handling of edge cases and ambiguous requests. (7) AnthropicRedTeam provides adversarial robustness evaluation. (8) Standardized scoring and aggregation across benchmarks for cross-model comparison.

## Results Summary

Key findings from model evaluations: (1) Safety performance varies significantly across models and benchmark categories. (2) Models often show inconsistent safety profiles - strong in some areas, weak in others. (3) Jailbreaking resistance (HarmBench) remains a significant challenge for most models. (4) Social discrimination (BBQ) performance differs substantially between base and instruction-tuned models. (5) Edge case handling (XSTest) reveals overrefusal patterns in some safety-tuned models. (6) No single model achieves top performance across all safety dimensions. (7) Regular benchmark updates capture evolving model capabilities and vulnerabilities.

## Conclusions

The authors conclude that HELM Safety provides essential infrastructure for rigorous, comparable safety evaluation. The framework reveals that current models have heterogeneous safety profiles with significant room for improvement across all categories. Limitations include the evolving nature of both threats and models requiring continuous benchmark updates, and potential gaps in the risk taxonomy. Future work will expand coverage to additional risk categories, develop more sophisticated jailbreak evaluations, and incorporate user-reported safety issues.

## Artifact Contributions

- HELM Safety v1.0: Standardized safety evaluation framework
- Integrated benchmark suite: BBQ, SimpleSafetyTest, HarmBench, XSTest, AnthropicRedTeam
- Public leaderboard: https://crfm.stanford.edu/helm/safety/latest/
- Open-source code: https://github.com/stanford-crfm/helm

## Data Description

HELM Safety v1.0 is a standardized safety evaluation framework comprising five safety benchmarks (BBQ, SimpleSafetyTest, HarmBench, AnthropicRedTeam, XSTest) spanning six risk categories: violence, fraud, discrimination, sexual content, harassment, and deception. The evaluation covers 24 prominent language models using exact-match accuracy for BBQ and model-judge harmfulness scores (assessed by GPT-4o and Llama 3.1 405B) for all other benchmarks, with results normalized to a 0-1 scale where higher scores indicate less safety risk.


## Notes

