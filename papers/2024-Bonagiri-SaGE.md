---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7IGEURG5
type: conferencePaper
short_title: SaGE
year: 2024
first_author: "[[Vamshi Krishna Bonagiri]]"
last_author: "[[Manas Gaur]]"
authors: "Vamshi Krishna Bonagiri; Sreeram Vennam; Priyanshul Govil; Ponnurangam Kumaraguru; Manas Gaur"
doi: 10.48550/arXiv.2402.13709
url: "http://arxiv.org/abs/2402.13709"
external_pdf: "http://arxiv.org/pdf/2402.13709.pdf"
publication: "International Conference on Language Resources and Evaluation"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Proposed Semantic Graph Entropy (SaGE), a metric based on abstract 'Rules-of-Thumb' (RoTs), to evaluate the moral consistency of LLM generations."
significance: "Argues that consistency is as crucial as accuracy in moral scenarios (which often lack single right answers), showing that state-of-the-art models are often morally inconsistent despite high task accuracy."
tags: 
pdf_extract: "PDF Extracts/0000/2024-Bonagiri-SaGE.md"
abstract: "Despite recent advancements showcasing the impressive capabilities of Large Language Models (LLMs) in conversational systems, we show that even state-of-the-art LLMs are morally inconsistent in their generations, questioning their reliability (and trustworthiness in general). Prior works in LLM evaluation focus on developing ground-truth data to measure accuracy on specific tasks. However, for moral scenarios that often lack universally agreed-upon answers, consistency in model responses becomes"
paper_summary: "Abstract: Despite recent advancements showcasing the impressive capabilities of Large Language Models (LLMs) in conversational systems, we show that even state-of-the-art LLMs are morally inconsistent in their  | Overview: SaGE: Evaluating Moral Consistency in Large Language Models Vamshi Krishna Bonagiri1,2, Sreeram Vennam1, Priyanshul Govil1,2 Ponnurangam Kumaraguru1, Manas Gaur2 1International Institute of Informatio | Methodology: to sampling-based generation. It is used to alter the probability distribution of a model's output, with temperature as a parameter (Holtzman et al.,  | Key Findings: practices for generated text. Journal of Artificial Intelligence Research, 77:103–166. --- Page 11 --- Anmol Goel, Charu Sharma, and Ponnurangam Kumar | Conclusions: In this work, we introduce a novel framework to evaluate the moral consistency of LLMs. We in- troduce SaGE, a new information-theoretic metric, groun"
local_pdf: "[[PDFs/2024/2024-Bonagiri-SaGE.pdf]]"
LLM_assessed: "GPT-4, GPT-3.5, OPT, Llama-2, Falcon, Mistral"
DATA_URL: "https://github.com/vnnm404/SaGE"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach text corpus for question answering"
data_metrics: "Not specified"
---
# SaGE: Evaluating Moral Consistency in Large Language Models

## Metadata

**Authors:** Bonagiri, Vamshi Krishna; Vennam, Sreeram; Govil, Priyanshul; Kumaraguru, Ponnurangam; Gaur, Manas

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2402.13709](https://doi.org/10.48550/arXiv.2402.13709)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Bonagiri-SaGE.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2402.13709
- **DOI:** https://doi.org/10.48550/arXiv.2402.13709

## Abstract

Despite recent advancements showcasing the impressive capabilities of Large Language Models (LLMs) in conversational systems, we show that even state-of-the-art LLMs are morally inconsistent in their generations, questioning their reliability (and trustworthiness in general). Prior works in LLM evaluation focus on developing ground-truth data to measure accuracy on specific tasks. However, for moral scenarios that often lack universally agreed-upon answers, consistency in model responses becomes crucial for their reliability. To address this issue, we propose an information-theoretic measure called Semantic Graph Entropy (SaGE), grounded in the concept of "Rules of Thumb" (RoTs) to measure a model's moral consistency. RoTs are abstract principles learned by a model and can help explain their decision-making strategies effectively. To this extent, we construct the Moral Consistency Corpus (MCC), containing 50K moral questions, responses to them by LLMs, and the RoTs that these models followed. Furthermore, to illustrate the generalizability of SaGE, we use it to investigate LLM consistency on two popular datasets -- TruthfulQA and HellaSwag. Our results reveal that task-accuracy and consistency are independent problems, and there is a dire need to investigate these issues further.

## Authors

[[Vamshi Krishna Bonagiri]], [[Sreeram Vennam]], [[Priyanshul Govil]], [[Ponnurangam Kumaraguru]], [[Manas Gaur]]

## Data Description

The paper introduces the Moral Consistency Corpus (MCC), containing 50K moral questions depicting 10K unique moral scenarios, with 550K answers generated by 11 LLMs (OPT 125m/1.3b/2.7b/6.7b/13b, Llama-2 7b-chat/13b-chat, Falcon-7b-instruct, Mistral-7b-instruct, GPT-3.5 Turbo, GPT-4) along with extracted Rules of Thumb (RoTs). MCC is constructed by paraphrasing questions from the Moral Integrity Corpus using Vicuna-13b, and the Semantic Graph Entropy (SaGE) metric evaluates moral consistency across semantically equivalent scenarios.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
