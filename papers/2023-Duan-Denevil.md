---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: NFX5I9VC
type: conferencePaper
short_title: Denevil
year: 2025
first_author: "[[Shitong Duan]]"
last_author: "[[Ning Gu]]"
authors: "Shitong Duan; Xiaoyuan Yi; Peng Zhang; Tun Lu; Xing Xie; Ning Gu"
doi: 10.48550/arXiv.2310.11053
url: "http://arxiv.org/abs/2310.11053"
external_pdf: "http://arxiv.org/pdf/2310.11053.pdf"
publication: "International Conference on Learning Representations"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced 'Denevil', a prompt generation algorithm to elicit ethical violations, and 'MoralPrompt' (dataset), revealing that most LLMs are misaligned intrinsic values."
significance: "Highlights the 'dark matter' of LLM values which are often hidden by surface-level RLHF, showing that adversarial prompting reveals latent misalignment."
tags: 
pdf_extract: "PDF Extracts/0000/2023-Duan-Denevil.md"
abstract: "Warning: this paper contains model outputs exhibiting unethical information. Large Language Models (LLMs) have made unprecedented breakthroughs, yet their increasing integration into everyday life might raise societal risks due to generated unethical content. Despite extensive study on specific issues like bias, the intrinsic values of LLMs remain largely unexplored from a moral philosophy perspective. This work delves into automatically navigating LLMs' ethical values based on value theories. M"
paper_summary: "Abstract: Warning: this paper contains model outputs exhibiting unethical information. Large Language Models (LLMs) have made unprecedented breakthroughs, yet their increasing integration into everyday life mig | Overview: Published as a conference paper at ICLR 2024 DENEVIL: TOWARDS DECIPHERING AND NAVIGAT- ING THE ETHICAL VALUES OF LARGE LANGUAGE MODELS VIA INSTRUCTION LEARNING Shitong Duan1, Xiaoyuan Yi2∗, Peng Zhang | Methodology: In this section, we first formalize generative evaluation and introduce our dynamic prompt generation framework DeNEVIL in Sec. 3.1, describe the cons | Key Findings: Write a completion for the prompt. Prompt: Tom had struggled with his mental health. One day, he saw a man. Tom heard felt that the man was a threat w"
local_pdf: "[[PDFs/2023/2023-Duan-Denevil.pdf]]"
LLM_assessed: "ChatGPT, Llama"
DATA_URL: "https://valuecompass.github.io"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "2,397 prompts"
---
# Denevil: Towards Deciphering and Navigating the Ethical Values of Large Language Models via Instruction Learning

## Metadata

**Authors:** Duan, Shitong; Yi, Xiaoyuan; Zhang, Peng; Lu, Tun; Xie, Xing; Gu, Ning

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.11053](https://doi.org/10.48550/arXiv.2310.11053)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Duan-Denevil.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2310.11053
- **DOI:** https://doi.org/10.48550/arXiv.2310.11053

## Abstract

Warning: this paper contains model outputs exhibiting unethical information. Large Language Models (LLMs) have made unprecedented breakthroughs, yet their increasing integration into everyday life might raise societal risks due to generated unethical content. Despite extensive study on specific issues like bias, the intrinsic values of LLMs remain largely unexplored from a moral philosophy perspective. This work delves into automatically navigating LLMs’ ethical values based on value theories. Moving beyond static discriminative evaluations with poor reliability, we propose DeNEVIL, a novel prompt generation algorithm tailored to dynamically exploit LLMs’ value vulnerabilities and elicit the violation of ethics in a generative manner, revealing their underlying value inclinations. On such a basis, we construct MoralPrompt, a high-quality dataset comprising 2,397 prompts covering 500+ value principles, and then benchmark the intrinsic values across a spectrum of LLMs. We discovered that most models are essentially misaligned, necessitating further ethical value alignment. In response, we develop VILMO, an in-context alignment method that enhances the value compliance of LLM outputs by learning to generate appropriate value instructions, outperforming existing competitors. Our methods are suitable for black-box and open-source models, serving as an initial step in studying LLMs’ ethical values.

## Authors

[[Shitong Duan]], [[Xiaoyuan Yi]], [[Peng Zhang]], [[Tun Lu]], [[Xing Xie]], [[Ning Gu]]

## Data Description

The paper introduces MoralPrompt, a dataset of 2,397 provocative prompts covering 522 value principles across five moral foundations (care, fairness, loyalty, authority, sanctity) from Moral Foundations Theory. The prompts are dynamically generated using the DeNEVIL framework to exploit value vulnerabilities in LLMs, and 27 LLMs of diverse architectures and scales are benchmarked for ethical value conformity in a generative evaluation setting.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Computation-and-Language

## Citation Info

15 citations (Semantic Scholar/arXiv) [2025-08-27] 15 citations (Semantic Scholar/DOI) [2025-08-23]
