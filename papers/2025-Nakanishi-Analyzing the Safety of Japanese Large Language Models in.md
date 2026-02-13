---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0024
type: preprint
short_title: Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts
year: 2025
first_author: "[[A. Nakanishi]]"
last_author: "[[F]]"
authors: "Nakanishi, A., Sano, Y., Liu, G., & Pierri, F"
url: "https://arxiv.org/abs/2503.01947"
external_pdf: "https://arxiv.org/pdf/2503.01947.pdf"
local_pdf: "[[PDFs/2025/2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Chinese, Japanese"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "In recent years, Large Language Models (LLMs) have attracted growing interest for their significant potential, though concerns have rapidly emerged regarding unsafe behaviors stemming from inherent stereotypes and biases. Most research on stereotypes in LLMs has primarily relied on indirect evaluation setups, in which models are prompted to select between pairs of sentences associated with particular social groups."
ethics_perspective: "Bias & Fairness"
data_description: "Evaluation methodology"
data_metrics: "3,612 prompts"
LLM_assessed: "Gemma, Qwen"
DATA_URL: "https://github.com/momijiro/stereotype_japanese_llm"
---
# Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts

## Authors

[[Nakanishi]], [[A.]], [[Sano]], [[Y.]], [[Liu]], [[G.]], [[& Pierri]], [[F]]

## Metadata

**Authors:** Nakanishi, A., Sano, Y., Liu, G., & Pierri, F

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2503.01947

## Abstract

In recent years, Large Language Models (LLMs) have attracted growing interest for their significant potential, though concerns have rapidly emerged regarding unsafe behaviors stemming from inherent stereotypes and biases. Most research on stereotypes in LLMs has primarily relied on indirect evaluation setups, in which models are prompted to select between pairs of sentences associated with particular social groups. Recently, direct evaluation methods have emerged, examining open-ended model responses to overcome limitations of previous approaches, such as annotator biases. Most existing studies have focused on English-centric LLMs, whereas research on nonEnglish models—particularly Japanese—remains sparse, despite the growing development and adoption of these models. This study examines the safety of Japanese LLMs when responding to stereotype-triggering prompts in direct setups. We constructed 3,612 prompts by combining 301 social group terms–categorized by age, gender, and other attributes–with 12 stereotype-inducing templates in Japanese. Responses were analyzed from three foundational models trained respectively on Japanese, English, and Chinese language. Our findings reveal that LLM-jp, a Japanese native model, exhibits the lowest refusal rate and is more likely to generate toxic and negative responses compared to other models. Additionally, prompt format significantly influence the output of all models, and the generated responses include exaggerated reactions toward specific social groups, varying across models. These findings underscore the insufficient ethical safety mechanisms in Japanese LLMs and demonstrate that even highaccuracy models can produce biased outputs when processing Japanese-language prompts. We advocate for improving safety mechanisms and bias mitigation strategies in Japanese LLMs, contributing to ongoing discussions on AI ethics beyond linguistic boundaries. Impact Statement—Large language models (LLMs) are increasingly used in sectors such as medicine, education, and finance, offering unprecedented performance. As their use expands, particularly in chatbots, ensuring the ethical safety of LLMs—especially concerning stereotypes and social biases—is critical, as biased models can negatively influence human decision-making and shape societal norms. Despite extensive research on English-language models, bias in non-English LLMs, particularly Japanese, remains underexplored, raising concerns given their growing societal impact. This study assesses the safety of Japanese LLMs using stereotype-triggering prompts, comparing biases across Japanese, English, and Chinese models. Our experiments show that while English and Chinese LLMs refused biased responses at rates of 12.2% and 29.3%, This paper has been submitted to IEEE Transactions on Artificial Intelligence for possible publication. Akito Nakanishi. Author is with Graduate School of Science and Technology, University of Tsukuba, Ibaraki, 3058577 JP, (e-mail: nakanishi.aki...

## Dataset Information

Size: 3,612 prompts (301 social group terms x 12 stereotype-inducing templates)

## Data Description

This study constructs 3,612 stereotype-triggering prompts by combining 301 Japanese social group terms across 9 categories (age, gender, nationality, religion, etc.) with 12 templates (statements, questions, and opinion formats). Three foundation models (Gemma-2-27b-it, Qwen2.5-14B-Instruct, and LLM-jp-3-13b-instruct) representing English, Chinese, and Japanese training bases were evaluated for refusal rate, toxicity, and sentiment in their open-ended responses.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** HIGH

## Tags

