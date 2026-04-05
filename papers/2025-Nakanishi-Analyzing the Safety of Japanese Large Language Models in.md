---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0024
type: preprint
short_title: "Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts"
year: 2025
first_author: "[[A. Nakanishi]]"
last_author: "[[F & Pierri]]"
authors: "A. Nakanishi; Y. Sano; Geng Liu; F & Pierri"
url: "https://arxiv.org/abs/2503.01947"
external_pdf: "https://arxiv.org/pdf/2503.01947.pdf"
pdf_extract: "PDF Extracts/2025/2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Nakanishi-Analyzing the Safety of Japanese Large Language Models in.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Japanese"
cultures_nationalities_list: "Japanese"
languages_list: "Japanese"
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
tags: 
abstract: "In recent years, Large Language Models (LLMs) have attracted growing interest for their significant potential, though concerns have rapidly emerged regarding unsafe behaviors stemming from inherent stereotypes and biases. Most research on stereotypes in LLMs has primarily relied on indirect evaluation setups, in which models are prompted to select between pairs of sentences associated with particular social groups."
LLM_assessed: "Gemma-2, Qwen"
DATA_URL: "https://github.com/momijiro/stereotype_japanese_llm"
CONFERENCE: "Preprint"
ethics_overall: 100
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
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 80
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation methodology"
data_metrics: "3,612 prompts"
---
# Analyzing the Safety of Japanese Large Language Models in Stereotype-Triggering Prompts

## Authors

[[A. Nakanishi]], [[Y. Sano]], [[Geng Liu]], [[F & Pierri]]

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

Constructs a dataset of 3,612 Japanese stereotype-triggering prompts combining 301 social group terms (age, gender, and other attributes) with 12 stereotype-inducing sentence templates, used for direct evaluation of safety in Japanese LLMs.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** HIGH

## Tags

