---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BGYYMBHZ
type: document
short_title: DecodingTrust
year: 2023
first_author: "[[Boxin Wang]]"
last_author: "[[Bo Li]]"
authors: "Boxin Wang; Weixin Chen; Hengzhi Pei; Chulin Xie; Mintong Kang; Chenhui Zhang; Chejian Xu; Zidi Xiong; Ritik Dutta; Rylan Schaeffer; Sang T. Truong; Simran Arora; Mantas Mazeika; Dan Hendrycks; Zinan Lin; Yu Cheng; Sanmi Koyejo; Dawn Song; Bo Li"
url: "https://arxiv.org/abs/2306.11698"
external_pdf: "https://arxiv.org/pdf/2306.11698.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
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
newtags: "AI Safety & Alignment"
key_contribution: "Released DecodingTrust, a comprehensive benchmark suite for GPT models covering 8 trustworthiness perspectives including toxicity, bias, robustness, and privacy."
significance: "A substantial evaluation of GPT-4 vs GPT-3.5, finding that while GPT-4 is more capable, it is also more vulnerable to certain jailbreaks (e.g., misleading instructions) due to stronger instruction-following."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2023/2023-Wang-DecodingTrust.md"
abstract: "Generative Pre-trained Transformer (GPT) models have exhibited exciting progress in their capabilities, capturing the interest of practitioners and the public alike. Yet, while the literature on the trustworthiness of GPT models remains limited, practitioners have proposed employing capable GPT models for sensitive applications such as healthcare and finance – where mistakes can be costly. To this end, this work proposes a comprehensive trustworthiness evaluation for large language models with..."
paper_summary: "Abstract: Generative Pre-trained Transformer (GPT) models have exhibited exciting progress in their capabilities, capturing the interest of practitioners and the public alike. Yet, while the literature on the t | Overview: DECODINGTRUST: A Comprehensive Assessment of Trustworthiness in GPT Models Boxin Wang1∗, Weixin Chen1∗, Hengzhi Pei1∗, Chulin Xie1∗, Mintong Kang1∗, Chenhui Zhang1∗, Chejian Xu1, Zidi Xiong1, Ritik Du | Methodology: GPT-3.5 GPT-4 Base 88.65 94.38 Word-level Augment 87.39 93.81 Shake-W 83.26 92.66 Sentence-level Tweet (p = 0) 82.00 90.37 Tweet (p = 0.6) 80.96 90.60 | Key Findings: to recent open LLMs, including llama [166], Llama 2 [168], Alpaca [161], Red Pajama [41] and more, in Appendix I. We showcase unreliable responses fro"
local_pdf: "[[Lit-WS-PDFs/2023/2023-Wang-DecodingTrust.pdf]]"
CONF-CC: "NeurIPS 2023"
DATE_ADDED: 20260208
LLM_assessed: "Alpaca, GPT-3.5, GPT-4, LLaMA, Llama-2, Vicuna"
DATA_URL: "https://huggingface.co/datasets/AI-Secure/DecodingTrust"
CONFERENCE: Preprint
helm: incorporated
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset for toxicity detection"
data_metrics: "Not specified"
---
# DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models

## Metadata

**Authors:** Wang, Boxin; Chen, Weixin; Pei, Hengzhi; Xie, Chulin; Kang, Mintong; Zhang, Chenhui; Xu, Chejian; Xiong, Zidi; Dutta, Ritik; Schaeffer, Rylan; Truong, Sang T.; Arora, Simran; Mazeika, Mantas; Hendrycks, Dan; Lin, Zinan; Cheng, Yu; Koyejo, Sanmi; Song, Dawn; Li, Bo

**Year:** 2023

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-PDFs/2023/2023-Wang-DecodingTrust.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2306.11698

## Abstract

Generative Pre-trained Transformer (GPT) models have exhibited exciting progress in their capabilities, capturing the interest of practitioners and the public alike. Yet, while the literature on the trustworthiness of GPT models remains limited, practitioners have proposed employing capable GPT models for sensitive applications such as healthcare and finance -- where mistakes can be costly. To this end, this work proposes a comprehensive trustworthiness evaluation for large language models with a focus on GPT-4 and GPT-3.5, considering diverse perspectives -- including toxicity, stereotype bias, adversarial robustness, out-of-distribution robustness, robustness on adversarial demonstrations, privacy, machine ethics, and fairness. Based on our evaluations, we discover previously unpublished vulnerabilities to trustworthiness threats. For instance, we find that GPT models can be easily misled to generate toxic and biased outputs and leak private information in both training data and conversation history. We also find that although GPT-4 is usually more trustworthy than GPT-3.5 on standard benchmarks, GPT-4 is more vulnerable given jailbreaking system or user prompts, potentially because GPT-4 follows (misleading) instructions more precisely. Our work illustrates a comprehensive trustworthiness evaluation of GPT models and sheds light on the trustworthiness gaps. Our benchmark is publicly available at https://decodingtrust.github.io/ ; our dataset can be previewed at https://huggingface.co/datasets/AI-Secure/DecodingTrust ; a concise version of this work is at https://openreview.net/pdf?id=kaHpo8OZw2 .

## Authors

[[Boxin Wang]], [[Weixin Chen]], [[Hengzhi Pei]], [[Chulin Xie]], [[Mintong Kang]], [[Chenhui Zhang]], [[Chejian Xu]], [[Zidi Xiong]], [[Ritik Dutta]], [[Rylan Schaeffer]], [[Sang T. Truong]], [[Simran Arora]], [[Mantas Mazeika]], [[Dan Hendrycks]], [[Zinan Lin]], [[Yu Cheng]], [[Sanmi Koyejo]], [[Dawn Song]], [[Bo Li]]

## Data Description

Comprehensive trustworthiness benchmark for LLMs covering 8 perspectives: toxicity, stereotype bias, adversarial robustness, OOD robustness, adversarial demonstrations, privacy, machine ethics, and fairness, with custom datasets and evaluation scenarios.


## Notes

