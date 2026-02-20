---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UWAKB79Z
type: conferencePaper
short_title: SafeInfer
year: 2025
first_author: "[[Somnath Banerjee]]"
last_author: "[[Rima Hazra]]"
authors: "Somnath Banerjee; Sayan Layek; Soham Tripathy; Shanu Kumar; Animesh Mukherjee; Rima Hazra"
url: "https://ojs.aaai.org/index.php/AAAI/article/view/34927"
external_pdf: "file:///Users/jimmylin/Zotero/storage/KV9GGDEF/Jain and others - 2025 - SafeInfer Context Adaptive Decoding Time Safety Alignment for Large Language Models.pdf"
pdf_extract: "PDF Extracts/2025/2025-Banerjee-SafeInfer.md"
local_pdf: "[[PDFs/2025/2025-Banerjee-SafeInfer.pdf]]"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Proposed 'SafeInfer' for inference-time safety alignment (decoding adaptation)."
significance: "Suggests shifting safety from training (fine-tuning) to inference (decoding), allowing for flexible, context-adaptive safety rails without retraining."
tags: 
abstract: "Language models aligned for safety often exhibit fragile and imbalanced mechanisms, increasing the chances of producing unsafe content. In addition, editing techniques to incorporate new knowledge can further compromise safety. To tackle these issues, we propose SAFEINFER, a context-adaptive, decodingtime safety alignment strategy for generating safe responses to user queries. SAFEINFER involves two phases: the ‘safety amplification’ phase, which uses safe demonstration examples to adjust the..."
DATE_ADDED: 20260129
LLM_assessed: "Llama-2, Mistral, Vicuna, Falcon"
DATA_URL: "https://github.com/NeuralSentinel/SafeInfer"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
CONFERENCE: "AAAI 2025"
---
# SafeInfer: Context Adaptive Decoding Time Safety Alignment for Large Language Models

## Metadata

**Authors:** Banerjee, Somnath; Layek, Sayan; Tripathy, Soham; Kumar, Shanu; Mukherjee, Animesh; Hazra, Rima

**Year:** 2025

**Publication:** AAAI 2025

**Type:** conferencePaper

## Links

- **URL:** https://ojs.aaai.org/index.php/AAAI/article/view/34927

## Abstract

Safety-aligned language models often exhibit fragile and imbalanced safety mechanisms, increasing the likelihood of generating unsafe content. This work proposes SafeInfer, a context-adaptive decoding time safety alignment strategy. SafeInfer operates in two stages: first employing safe demonstration examples to adjust the model's hidden states and increase the likelihood of safer outputs, then applying safety-optimized distributions to guide token selection during generation. We also introduce HarmEval, a novel benchmark for extensive safety evaluations designed to address potential misuse scenarios in accordance with the policies of leading AI tech giants.

## Authors

[[Somnath Banerjee]], [[Sayan Layek]], [[Soham Tripathy]], [[Shanu Kumar]], [[Animesh Mukherjee]], [[Rima Hazra]]

## Detailed Summary

SafeInfer introduces a novel context-adaptive, decoding-time safety alignment strategy for generating safe responses from large language models without requiring retraining or fine-tuning. The approach addresses the observation that even safety-aligned LLMs often exhibit fragile and imbalanced safety mechanisms that can be circumvented through jailbreaking attacks, and that knowledge editing techniques can further compromise safety. Unlike traditional fine-tuning approaches, SafeInfer operates at inference time, allowing dynamic, real-time moderation of outputs.

The method comprises two complementary phases. The Safety Amplification (SA) phase uses safe demonstration examples to compute a safety amplification vector (SV) from attention head activations, which is then integrated into the model's hidden states during forward passes to increase the likelihood of safe outputs. The Safety-Guided Decoding Strategy (sGDS) phase further modifies token selection by combining output distributions to remove harmful tendencies while preserving the model's general capabilities. This is achieved by training an auxiliary "unsafe" model on harmful question-answer pairs and using controlled text generation techniques to debias the output distribution.

The paper also introduces HarmEval, a new benchmark for comprehensive safety evaluation based on prohibited use cases outlined by OpenAI and Meta. HarmEval covers 11 policy-violating categories with approximately 550 harmful queries. Experiments demonstrate that SafeInfer drastically reduces harmful responses across six benchmark datasets while preserving model utility on five open-ended benchmark tasks. The approach is evaluated across multiple prompting techniques (simple, instruction-centric, chain-of-thought) and on both base models and edited versions of LLMs.

## Paper Outline

1. Introduction - Need for decoding-time safety alignment
2. Related Work
   - Inference time safety alignment
   - Controlled text generation
3. Context Adaptive Decoding Time Alignment (SAFEINFER)
   - Preliminaries and notation
   - Safety Amplification (SA) phase
   - Computing safety amplification vector (SV)
   - Safety-guided decoding strategy (sGDS)
4. Datasets
   - DangerousQA, AdvBench, HEx-PHI
   - TechHazardQA, NicheHazardQA
   - HarmEval (new benchmark)
5. Experiments
   - Language models (base and edited versions)
   - Evaluation metrics
   - Results and comparisons
6. Analysis and Discussion
7. Conclusion

## Methods Summary

SafeInfer methodology comprises two phases: (1) Safety Amplification (SA): Identify top influential attention heads through activation patching; construct prompts from safe demonstration dataset Dsf with unsafe-question/safe-answer pairs; compute mean safety-conditioned activations across prompts; sum across attention heads to create safety amplification vector SV; integrate SV into hidden states during forward pass with coefficient gamma. (2) Safety-Guided Decoding Strategy (sGDS): Fine-tune an auxiliary model Musf on harmful question-answer pairs; use Union operator from controlled text generation to combine distributions of intermediate model M't and Musf; subtract the combined distribution (scaled by lambda) from M't to obtain safe output distribution Msf_t. The approach is evaluated on six safety datasets (DangerousQA, AdvBench, HEx-PHI, TechHazardQA, NicheHazardQA, HarmEval) and five utility benchmarks using models including Llama2-7b-chat, Mistral-7B-Instruct, Vicuna-7b, and Falcon-7b-instruct.

## Results Summary

Key results include: (1) SafeInfer significantly reduces harmful responses across all evaluated models and datasets compared to baselines; (2) The two-phase approach (SA + sGDS) outperforms either phase alone; (3) SafeInfer preserves model utility on open-ended benchmark tasks (TruthfulQA, BoolQ, ARC, HellaSwag, PIQA); (4) The method is effective across three prompting techniques: simple prompts, instruction-centric prompts, and chain-of-thought prompts; (5) SafeInfer works on both base safety-aligned models and edited models where knowledge updates had compromised safety; (6) The approach generalizes across different model architectures (Llama, Mistral, Vicuna, Falcon); (7) HarmEval validation shows GPT-4 classified queries as harmful and Perspective API confirmed toxicity scores above 0.7 threshold.

## Conclusions

The paper concludes that SafeInfer provides a versatile and effective approach to inference-time safety alignment that: (1) Operates without requiring model retraining or architecture changes; (2) Is adaptable across different LLM architectures; (3) Preserves general model capabilities while improving safety; (4) Addresses both inherent safety fragility and safety degradation from knowledge editing; (5) Can be applied flexibly to various prompting scenarios. The combination of safety amplification (working in latent space) with safety-guided decoding (working in output distribution space) proves more effective than either approach alone. The introduction of HarmEval provides a comprehensive benchmark aligned with major AI companies' usage policies for future safety research.

## Artifact Contributions

- SafeInfer methodology for decoding-time safety alignment
- Safety amplification vector computation method
- Safety-guided decoding strategy implementation
- HarmEval benchmark: ~550 harmful queries across 11 policy-violating categories
- Code available at: https://github.com/NeuralSentinel/SafeInfer
- Evaluation results across multiple models and datasets

## Data Description

SafeInfer is evaluated on six safety datasets (DangerousQA, AdvBench, HEx-PHI, TechHazardQA, NicheHazardQA, and the newly proposed HarmEval with ~550 harmful queries). The method is tested on Llama-2-7b-chat, Mistral-7B-Instruct, Vicuna-7b, and Falcon-7b-instruct, assessing decoding-time safety alignment for reducing harmful responses while preserving model utility.


## Notes

