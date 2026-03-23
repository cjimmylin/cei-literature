---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JRW7RCQN
type: journalArticle
short_title: FAIRMT-BENCH
year: 2025
first_author: "[[Zhiting Fan]]"
last_author: "[[Zuozhu Liu]]"
authors: "Zhiting Fan; Ruizhe Chen; Tianxiang Hu; Zuozhu Liu"
external_pdf: "file:///Users/jimmylin/Zotero/storage/PNCXQE8M/Fan et al. - 2025 - FAIRMT-BENCH BENCHMARKING FAIRNESS FOR MULTI-TURN DIALOGUE IN CONVERSATIONAL LLMS.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
rv_islam: 10
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
newtags: "Bias & Fairness"
key_contribution: "Introduced FairMT-Bench for evaluating fairness in *multi-turn* dialogues, finding bias accumulates over turns unlike in single-turn benchmarks."
significance: "Critical for evaluating chat agents, as single-turn benchmarks miss the 'drift' into biased behavior that happens in longer interactions."
tags: 
abstract: "The increasing deployment of large language model (LLM)-based chatbots has raised concerns regarding fairness. Fairness issues in LLMs may result in serious consequences, such as bias amplification, discrimination, and harm to minority groups. Many efforts are dedicated to evaluating and mitigating biases in LLMs. However, existing fairness benchmarks mainly focus on single-turn dialogues, while multi-turn scenarios, which better reflect real-world conversations, pose greater challenges due to..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, GPT-4, Gemma, Gemma-2, Llama-2, Llama-3, Mistral, Mixtral, Qwen"
DATA_URL: "https://github.com/FanZT6/FairMT-bench"
pdf_extract: "PDF Extracts/2025/2025-Fan-FAIRMT-BENCH.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Fan-FAIRMT-BENCH.pdf]]"
CONFERENCE: "Journal"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness text corpus for conversational ai"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# FAIRMT-BENCH: BENCHMARKING FAIRNESS FOR MULTI-TURN DIALOGUE IN CONVERSATIONAL LLMS

## Metadata

**Authors:** Fan, Zhiting; Chen, Ruizhe; Hu, Tianxiang; Liu, Zuozhu

**Year:** 2025

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2410.19317
- **Github:** https://github.com/FanZT6/FairMT-bench

## Abstract

The increasing deployment of large language model (LLM)-based chatbots has raised concerns regarding fairness. Fairness issues in LLMs may result in serious consequences, such as bias amplification, discrimination, and harm to minority groups. Many efforts are dedicated to evaluating and mitigating biases in LLMs. However, existing fairness benchmarks mainly focus on single-turn dialogues, while multi-turn scenarios, which better reflect real-world conversations, pose greater challenges due to conversational complexity and risk for bias accumulation. In this paper, we introduce a comprehensive benchmark for fairness of LLMs in multi-turn scenarios, FairMT-Bench. Specifically, We propose a task taxonomy to evaluate fairness of LLMs across three stages: context understanding, interaction fairness, and fairness trade-offs, each comprising two tasks. To ensure coverage of diverse bias types and attributes, our multi-turn dialogue dataset FairMT-10K is constructed by integrating data from established fairness benchmarks. For evaluation, we employ GPT-4 along with bias classifiers like Llama-Guard-3, and human annotators to ensure robustness. Our experiments and analysis on FairMT-10K reveal that in multi-turn dialogue scenarios, LLMs are more prone to generating biased responses, showing significant variation in performance across different tasks and models. Based on these findings, we develop a more challenging dataset, FairMT-1K, and test 15 current state-of-theart (SOTA) LLMs on this dataset. The results highlight the current state of fairness in LLMs and demonstrate the value of this benchmark for evaluating fairness of LLMs in more realistic multi-turn dialogue contexts. This underscores the need for future works to enhance LLM fairness and incorporate FairMT-1K in such efforts. Our code and dataset are available at FairMT-Bench.

## Authors

[[Zhiting Fan]], [[Ruizhe Chen]], [[Tianxiang Hu]], [[Zuozhu Liu]]

## Detailed Summary

This paper introduces FairMT-Bench, a comprehensive benchmark for evaluating fairness in large language models during multi-turn dialogues. While existing fairness benchmarks focus on single-turn interactions, the authors argue that real-world conversations involve extended exchanges where biases can accumulate and compound over multiple turns. The benchmark addresses this gap by providing systematic evaluation across three stages: context understanding, interaction fairness, and fairness trade-offs.

The research makes two key contributions. First, FairMT-10K, a large-scale dataset constructed by integrating and extending existing fairness benchmarks into multi-turn dialogue formats. Second, FairMT-1K, a curated challenging subset for benchmarking state-of-the-art models. The task taxonomy covers six distinct evaluation scenarios examining how LLMs handle bias in conversational contexts including stereotype recognition, fair response generation, and bias mitigation when context contains prejudicial information.

The significance of this work lies in demonstrating that single-turn fairness evaluations significantly underestimate LLM bias vulnerabilities. Multi-turn settings reveal "fairness drift" where models that appear unbiased in isolated queries generate increasingly problematic responses as conversations develop. This has critical implications for conversational AI deployment in sensitive domains.

## Paper Outline

1. Introduction - Motivation for multi-turn fairness evaluation
2. Related Work - Single-turn fairness benchmarks and their limitations
3. FairMT-Bench Framework - Task taxonomy and evaluation design
4. Dataset Construction - FairMT-10K and FairMT-1K methodology
5. Evaluation Setup - Models, metrics, and annotators
6. Experiments on FairMT-10K - Comprehensive model comparison
7. Experiments on FairMT-1K - State-of-the-art model benchmarking
8. Analysis and Discussion - Key findings on bias accumulation
9. Conclusion

## Methods Summary

The benchmark employs a multi-faceted methodology: (1) Task taxonomy design covering context understanding (identifying bias in conversation history), interaction fairness (generating fair responses during dialogue), and fairness trade-offs (balancing fairness with helpfulness). (2) Dataset construction by converting existing bias datasets (BBQ, StereoSet, etc.) into multi-turn formats and generating additional synthetic dialogues. (3) Evaluation using GPT-4, specialized bias classifiers (Llama-Guard-3), and human annotators for robustness. (4) Testing 15 SOTA LLMs including GPT-4, Claude, Llama variants, and others.

## Results Summary

Key findings: (1) All tested LLMs show degraded fairness performance in multi-turn vs. single-turn settings. (2) Bias accumulation effects are observable - models become less fair as conversations extend. (3) Significant variation exists across task types - models perform worse on implicit bias detection than explicit. (4) Open-source models generally underperform proprietary ones on fairness metrics. (5) Safety-tuned models show improved but still imperfect multi-turn fairness. (6) Trade-offs exist between helpfulness and fairness in adversarial contexts.

## Conclusions

The authors conclude that current LLM fairness evaluations based on single-turn interactions provide incomplete and overly optimistic assessments. They demonstrate the necessity of multi-turn evaluation for realistic fairness measurement. Limitations include the English-language focus and reliance on existing bias taxonomies. Future work should extend to multilingual settings, develop dynamic bias mitigation techniques, and investigate longitudinal fairness effects in deployed systems.

## Artifact Contributions

- FairMT-10K dataset: Large-scale multi-turn fairness benchmark
- FairMT-1K dataset: Curated challenging subset for SOTA evaluation
- Code repository: https://github.com/FanZT6/FairMT-bench
- Benchmark leaderboard and evaluation scripts

## Data Description

FairMT-Bench introduces FairMT-10K (~10K multi-turn dialogue samples covering stereotype and toxicity bias across 6 attributes) and a more challenging FairMT-1K subset, both designed to evaluate LLM fairness in multi-turn dialogue scenarios with a six-task taxonomy.


## Notes

