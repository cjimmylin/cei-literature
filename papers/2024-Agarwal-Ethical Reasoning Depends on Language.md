---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AGARWAL2024
type: conferencePaper
short_title: "Ethical Reasoning Depends on Language"
year: 2025
first_author: "[[Utkarsh Agarwal]]"
last_author: "[[Choudhury, Monojit]]"
authors: "[[Agarwal, Utkarsh]]; [[Tanmay, Kumar]]; [[Khandelwal, Aditi]]; [[Choudhury, Monojit]]"
doi: 10.48550/arXiv.2404.18460
url: "https://arxiv.org/abs/2404.18460"
external_pdf: "https://arxiv.org/pdf/2404.18460.pdf"
publication: "LREC-COLING 2024"
national_ethnic_cultural: "Chinese, Indian, African/Ubuntu, Spanish, Russian"
cultures_nationalities_list: "Chinese, Indian, African, Spanish, Russian"
languages_list: "Arabic, Chinese, English, Hindi, Russian, Spanish, Swahili"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Multilingual, Cross-Cultural, Deontology, Virtue-Ethics, Consequentialism, LLM-Evaluation"
key_contribution: "Shows LLM ethical reasoning varies by prompt language; GPT-4 most consistent across 6 languages"
significance: "Demonstrates cultural/linguistic bias in AI moral reasoning, crucial for global AI deployment"
tags: 
abstract: "Ethical reasoning is a crucial skill for Large Language Models (LLMs). However, moral values are not universal, but rather influenced by language and culture. This paper explores how three prominent LLMs – GPT-4, ChatGPT, and Llama2-70B-Chat – perform ethical reasoning in different languages and if their moral judgement depend on the language in which they are prompted. We extend the study of ethical reasoning of LLMs by Rao et al."
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
research_topic: "LLM Moral Reasoning"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, ChatGPT, Llama-2"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2024/2024-Agarwal-Ethical Reasoning Depends on Language.md"
local_pdf: "[[PDFs/2024/2024-Agarwal-Ethical Reasoning Depends on Language.pdf]]"
normative_ethics_benchmark: Yes
DATE_ADDED: 20260207
---
# Ethical Reasoning and Moral Value Alignment of LLMs Depend on the Language We Prompt Them In

## Authors

[[Utkarsh Agarwal|Agarwal, Utkarsh]], [[Kumar Tanmay|Tanmay, Kumar]], [[Aditi Khandelwal|Khandelwal, Aditi]], [[Monojit Choudhury|Choudhury, Monojit]]

## Metadata

**Authors:** Agarwal, Utkarsh; Tanmay, Kumar; Khandelwal, Aditi; Choudhury, Monojit

**Year:** 2024

**Publication:** LREC-COLING 2024

**Type:** conferencePaper

**DOI:** [10.48550/arXiv.2404.18460](https://doi.org/10.48550/arXiv.2404.18460)

**arXiv ID:** 2404.18460

## Links

- **arXiv:** https://arxiv.org/abs/2404.18460
- **PDF:** https://arxiv.org/pdf/2404.18460.pdf
- **DOI:** https://doi.org/10.48550/arXiv.2404.18460
- **ACL Anthology:** https://aclanthology.org/2024.lrec-main.560/

## Abstract

This paper extends the study of ethical reasoning of LLMs to a multilingual setup, probing LLMs with ethical dilemmas and policies from three branches of normative ethics: deontology, virtue, and consequentialism. Testing across six languages (English, Spanish, Russian, Chinese, Hindi, and Swahili), the team found that GPT-4 is the most consistent and unbiased ethical reasoner across languages while the other two models (ChatGPT and Llama2-70B-Chat) demonstrated notable bias shifts in non-English contexts. Their findings suggest that moral value judgments in LLMs are substantially influenced by the prompt language used.

## Detailed Summary

This paper investigates how the ethical reasoning abilities of Large Language Models (LLMs) vary when prompted in different languages, extending the study of LLM ethics to multilingual settings. The research is motivated by the "Foreign Language Effect" observed in human psychology, where people make different moral judgments when facing dilemmas in a foreign language compared to their native language. The authors probe whether LLMs exhibit similar language-dependent moral biases and whether they can function as generic ethical reasoners across linguistic contexts.

The study tests three prominent LLMs (GPT-4, ChatGPT, and Llama2-70B-Chat) across six languages: English, Spanish, Russian, Chinese, Hindi, and Swahili. The experimental framework follows Rao et al. (2023), presenting models with ethical dilemmas and policies derived from three branches of normative ethics: deontology (rules and duties), virtue ethics (character traits), and consequentialism (outcomes). Policies are presented at three levels of abstraction (Level 0, 1, and 2), with Level 2 being most abstract and Level 0 most specific to the dilemma.

Key findings reveal significant cross-linguistic variation in LLM ethical reasoning. GPT-4 demonstrated the most consistent and unbiased ethical reasoning across languages, while ChatGPT and Llama2-70B-Chat showed substantial moral value bias in non-English contexts. Notably, bias was minimal for English (where dilemma resolution depends on ethical policy rather than model bias) but maximal for low-resource languages like Hindi and Swahili. The study also found that English and Spanish exhibit similar bias patterns, as do Hindi and Chinese - suggesting language family or resource level may influence ethical alignment.

## Paper Outline

1. Introduction - LLMs, value pluralism, and the need for multilingual ethical reasoning
2. Background
   - 2.1 Ethics and Moral Philosophy - Normative ethics overview
   - 2.2 Foreign Language Effect on Morality
   - 2.3 Ethics in LLMs - AI alignment and existing frameworks
   - 2.4 Multilingual Performance of LLMs
3. Methodology
   - 3.1 Language-based Ethical Framework
   - 3.2 Ethical Policies (Levels 0, 1, 2)
4. Evaluating Ethical Reasoning Across Languages
   - 4.1 Dataset - Ethical dilemmas and policy pairs
   - Models tested (GPT-4, ChatGPT, Llama2-70B-Chat)
5. Results - Cross-linguistic ethical consistency analysis
6. Discussion and Conclusions

## Methods Summary

The researchers extended Rao et al.'s ethical reasoning framework to multilingual settings. Ethical policies were translated into six languages and presented to LLMs alongside ethical dilemmas reflecting interpersonal, professional, social, and cultural value conflicts. The experimental design tested whether LLMs could resolve dilemmas consistently with provided policies across languages. Key metrics included ethical consistency (whether model output is a valid resolution according to the stated policy) and bias measurement (whether the model applies its own judgment rather than following the policy). Temperature was set to 0 with top probability 0.95 and presence penalty 1 for deterministic outputs.

## Results Summary

GPT-4 showed highest ethical reasoning ability across all languages, while Llama2-70B-Chat performed poorest. Across all models, reasoning was best for English and Russian, poorest for Hindi and Swahili. Key bias patterns: (1) English showed minimal bias - model correctly followed ethical policies; (2) Non-English languages showed increased model-imposed value judgments overriding provided policies; (3) English and Spanish clustered together in bias patterns, as did Hindi and Chinese. The variation was dilemma-specific, indicating LLMs have strong value alignment biases that manifest differently depending on topic and language combination.

## Conclusions

The study demonstrates that LLM moral reasoning is substantially influenced by prompt language, complicating the vision of LLMs as generic ethical reasoners that can handle value pluralism globally. Current models, especially those other than GPT-4, cannot reliably apply specified ethical frameworks when prompted in non-English languages. This poses serious concerns for deploying LLMs in culturally diverse contexts where stakeholders may interact in their native languages. The findings suggest that (1) more multilingual ethical training data is needed, (2) ethical evaluation must extend beyond English, and (3) the Foreign Language Effect may have a computational analog in LLMs.

## Artifact Contributions

- Multilingual ethical dilemma test set across 6 languages
- Framework for evaluating LLM ethical consistency across languages
- First systematic study of LLM ethics in multilingual settings

## Data Description

The study extends Rao et al.'s ethical reasoning framework to a multilingual setup across six languages (English, Spanish, Russian, Chinese, Hindi, Swahili), probing GPT-4, ChatGPT (GPT-3.5-turbo), and Llama2-70B-Chat with ethical dilemmas and policies from three branches of normative ethics (deontology, virtue, consequentialism) at three levels of abstraction. The evaluation measures ethical consistency of model responses across languages and policy types.


## Notes


## Citation Info

