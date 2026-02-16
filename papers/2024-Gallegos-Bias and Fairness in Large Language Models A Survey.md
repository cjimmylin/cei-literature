---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0459
type: preprint
short_title: "Bias and Fairness in Large Language Models: A Survey"
year: 2025
first_author: "[[Gallegos, Isabel O.]]"
last_author: "[[Ahmed, Nesreen K]]"
authors: "[[Gallegos, Isabel O.]]; [[Rossi, Ryan A.]]; [[Barrow, Joe]]; [[Tanjim, Md Mehrab]]; [[Kim, Sungchul]]; [[Dernoncourt, Franck]]; [[Yu, Tong]]; [[Zhang, Ruiyi]]; [[Ahmed, Nesreen K.]]"
authors_incomplete: false
url: "https://aclanthology.org/2024.cl-3.8/"
external_pdf: "https://arxiv.org/pdf/2309.00770.pdf"
publication: "arXiv / ACL Anthology"
pdf_extract: "PDF Extracts/2024/2024-Gallegos-Bias and Fairness in Large Language Models A Survey.md"
local_pdf: "[[PDFs/2024/2024-Gallegos-Bias and Fairness in Large Language Models A Survey.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
cultures_nationalities_list: "N/A"
languages_list: "Multiple including French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "BART, BERT, Bartl, GPT-4"
DATA_URL: "https://github.com/i-gallegos/Fair-LLM-Benchmark"
tags: 
abstract: "Comprehensive survey organizing LLM bias and fairness work into three categories: metrics, datasets, and techniques. Covers embedding-based, probability-based, and generated text-based bias evaluation approaches. Published in Computational Linguistics 2024."
ethics_perspective: "Bias & Fairness"
---
# Bias and Fairness in Large Language Models: A Survey

## Authors

[[Gallegos, Isabel O]], [[Rossi, Ryan A]], [[Barrow, Joe]], [[Tanjim, Md Mehrab]], [[Kim, Sungchul]], [[Dernoncourt, Franck]], [[Yongqi Tong|Yu, Tong]], [[Zhang, Ruiyi]], [[Ahmed, Nesreen K]]

## Metadata

**Authors:** Gallegos, Isabel O.; Rossi, Ryan A.; Barrow, Joe; Tanjim, Md Mehrab; Kim, Sungchul; Dernoncourt, Franck; Yu, Tong; Zhang, Ruiyi; Ahmed, Nesreen K.

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** Multiple including French

## Links

- **arXiv:** https://arxiv.org/abs/2309.00770
- **URL:** https://aclanthology.org/2024.cl-3.8/

## Abstract

Comprehensive survey organizing LLM bias and fairness work into three categories: metrics, datasets, and techniques. Covers embedding-based, probability-based, and generated text-based bias evaluation approaches. Published in Computational Linguistics 2024.

## Summary

This comprehensive survey published in Computational Linguistics 2024 systematically organizes research on bias and fairness in large language models into three main categories: metrics, datasets, and mitigation techniques. The authors review bias evaluation approaches including embedding-based methods, probability-based methods, and generated text-based methods, providing a taxonomy of bias types (gender, race, religion, etc.) and mitigation strategies across the entire LLM lifecycle from data collection to deployment. The survey covers multilingual bias evaluation methodologies including French-language approaches, offering a framework for understanding bias evaluation methods applicable across different languages and model architectures. This work serves as a foundational reference for researchers and practitioners working on fairness issues in LLMs.

## Data Description

Comprehensive survey of bias and fairness research in LLMs. Reviews existing benchmarks and methods but does not test specific models. Provides taxonomy of bias types and mitigation strategies across the LLM lifecycle.


## Detailed Summary

This comprehensive survey, published in Computational Linguistics (Volume 50, Number 3, 2024), systematically organizes research on bias and fairness in large language models into three main areas: metrics for bias evaluation, datasets for bias evaluation, and techniques for bias mitigation. The authors consolidate, formalize, and expand definitions of social bias and fairness for NLP, distinguishing between representational harms (derogatory language, disparate system performance, erasure, exclusionary norms, misrepresentation, stereotyping, toxicity) and allocational harms (direct and indirect discrimination), presented in a taxonomy of social biases. The survey proposes three intuitive taxonomies: (1) metrics organized by the underlying data structure they operate on -- embedding-based (word and sentence embedding metrics like WEAT, SEAT), probability-based (masked token and pseudo-log-likelihood metrics like CrowS-Pairs, BOLD), and generated text-based (distribution, classifier, and lexicon metrics); (2) datasets organized by structure as counterfactual inputs (masked tokens, unmasked sentences) or prompts (sentence completions, question-answering), with identification of targeted harms and social groups; and (3) mitigation techniques organized by intervention stage -- pre-processing (data augmentation, filtering, generation, instruction tuning, projection-based), in-training (architecture modification, loss function modification, selective parameter updating, filtering), intra-processing (decoding strategy modification, weight redistribution, modular debiasing), and post-processing (rewriting). The survey introduces several fairness desiderata for LLMs including fairness through unawareness, invariance, equal social group associations, equal neutral associations, and replicated distributions.

## Paper Outline

1. Introduction - LLM capabilities and social bias concerns, survey scope and contributions
2. Formalizing Bias and Fairness for LLMs - Definitions (social group, protected attribute, group/individual fairness, social bias), bias in NLP tasks, bias in development lifecycle, fairness desiderata, taxonomy overview
3. Taxonomy of Metrics for Bias Evaluation - Embedding-based (WEAT, SEAT), probability-based (masked token, pseudo-log-likelihood), generated text-based (distribution, classifier, lexicon)
4. Taxonomy of Datasets for Bias Evaluation - Counterfactual inputs (WinoBias, CrowS-Pairs, StereoSet), prompts (BOLD, RealToxicityPrompts, BBQ)
5. Taxonomy of Techniques for Bias Mitigation - Pre-processing, in-training, intra-processing, post-processing methods
6. Open Problems and Challenges - Power imbalances, fairness conceptualization, evaluation principles, mitigation expansion, theoretical limits

## Methods Summary

The survey employs a systematic literature review approach, focusing solely on bias in LLMs for English (with additional languages for machine translation and multilingual models). The authors restrict their search to works proposing novel closed-form metrics, datasets, or mitigation techniques, requiring each work to specify applicability to social bias or fairness. Metrics are formalized mathematically with unified notation to improve cross-metric comparability. The relationship between evaluation metrics and datasets is explicitly disambiguated, as these are often conflated in the literature. Each taxonomy provides structured categorization enabling researchers to identify appropriate tools for their use case and understand tradeoffs between techniques. The survey covers both autoregressive models (GPT family), autoencoding models (BERT, RoBERTa, XLM-R), and encoder-decoder models (BART, T5).

## Results Summary

The survey synthesizes findings across the literature rather than presenting original experimental results. Key patterns identified include: embedding-based metrics capture static associations but may not reflect downstream biases; probability-based metrics are sensitive to template design and may conflate frequency with bias; generated text-based metrics better capture real-world harm but are harder to formalize. For datasets, the survey identifies consistency, reliability, and validity challenges -- many datasets contain errors, use binary gender assumptions, focus on US-centric social groups, and lack representation of intersectional identities. For mitigation, pre-processing techniques (especially data augmentation) are most common but may not address deeper model biases, while in-training methods show promise but require retraining. The survey finds that bias evaluation and mitigation efforts overwhelmingly focus on gender and race, with limited attention to disability, age, religion, and other dimensions, and that multilingual bias evaluation remains substantially underexplored.

## Conclusions

The survey identifies five key open problems: (1) power imbalances in LLM development, where stakeholders most affected by bias often have least influence; (2) the need for more robust fairness conceptualization beyond binary group comparisons; (3) improving bias evaluation principles including consistency, reliability, and validity of benchmarks; (4) expanding mitigation efforts to address the full range of bias types and social groups; and (5) exploring theoretical limits and impossibility results for fairness guarantees in NLP. Key limitations of the survey include its focus primarily on English, its restriction to papers proposing novel techniques (excluding application papers), and the rapidly evolving nature of the field. The authors emphasize that technical solutions alone are insufficient -- bias mitigation requires engagement with the social, historical, and institutional forces that produce inequity.

## Artifact Contributions

- **Consolidated Dataset Repository**: Compilation of publicly-available bias evaluation datasets (https://github.com/i-gallegos/Fair-LLM-Benchmark)
- **Three Taxonomies**: Comprehensive classification frameworks for metrics, datasets, and mitigation techniques with unified mathematical notation
- **Fairness Desiderata**: Five formal definitions operationalizing fairness notions for LLMs
- **Taxonomy of Social Biases**: Seven-category classification of representational and allocational harms in NLP

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Comprehensive survey covering French-language bias evaluation methodologies. Framework for understanding bias evaluation approaches applicable to French LLMs.

## Tags

