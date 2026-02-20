---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: MRVW3KBG
type: conferencePaper
short_title: NormBank
year: 2023
first_author: "[[Caleb Ziems]]"
last_author: "[[Diyi Yang]]"
authors: "Caleb Ziems; Jane Dwivedi-Yu; Yi-Chia Wang; Alon Halevy; Diyi Yang"
doi: 10.48550/arXiv.2305.17008
tags: 
url: "http://arxiv.org/abs/2305.17008"
external_pdf: "http://arxiv.org/pdf/2305.17008.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Introduces NormBank, a knowledge bank of 155k situational norms grounded in multivalent sociocultural frames (roles, setting, attributes)"
significance: "Standardizes non-monotonic social reasoning, allowing AI to handle context-dependent norms, essential for nuanced alignment"
pdf_extract: "PDF Extracts/2023/2023-Ziems-NormBank.md"
abstract: "We present NORMBANK, a knowledge bank of 155k situational norms. This resource is designed to ground flexible normative reasoning for interactive, assistive, and collaborative AI systems. Unlike prior commonsense resources, NORMBANK grounds each inference within a multivalent sociocultural frame, which includes the setting (e.g., restaurant), the agents’ contingent roles (waiter, customer), their attributes (age, gender), and other physical, social, and cultural constraints (e.g."
paper_summary: "Abstract: We present NORMBANK, a knowledge bank of 155k situational norms. This resource is designed to ground flexible normative reason- ing for interactive, assistive, and collabora- tive AI systems. Unlike p | Overview: NORMBANK: A Knowledge Bank of Situational Social Norms Caleb Ziems Jane Dwivedi-Yu Yi-Chia Wang Alon Y. Halevy Diyi Yang Stanford University, Meta AI {cziems, diyiy}@stanford.edu, {janeyu, yichiaw, ay | Methodology: achieved high recall, especially for roles, and least so for behaviors, which is unsurprising, given the almost unbounded space of viable human behavi | Key Findings: (LREC 2018), Miyazaki, Japan. European Language Resources Association (ELRA). Denis Emelin, Ronan Le Bras, Jena D Hwang, Maxwell Forbes, and Yejin Cho | Conclusions: Social norms are the foundation of culture and soci- ety (McDonald and Crandall, 2015; Hogg and Reid, 2006), and an understanding of these norms is cr"
local_pdf: "[[PDFs/2023/2023-Ziems-NormBank.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: GPT-3
DATA_URL: "https://github.com/SALT-NLP/normbank"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "ACL 2023"
---
# NormBank: A Knowledge Bank of Situational Social Norms

## Metadata

**Authors:** Ziems, Caleb; Dwivedi-Yu, Jane; Wang, Yi-Chia; Halevy, Alon; Yang, Diyi

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2305.17008](https://doi.org/10.48550/arXiv.2305.17008)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Ziems-NormBank.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2305.17008
- **DOI:** https://doi.org/10.48550/arXiv.2305.17008

## Abstract

We present NormBank, a knowledge bank of 155k situational norms. This resource is designed to ground flexible normative reasoning for interactive, assistive, and collaborative AI systems. Unlike prior commonsense resources, NormBank grounds each inference within a multivalent sociocultural frame, which includes the setting (e.g., restaurant), the agents' contingent roles (waiter, customer), their attributes (age, gender), and other physical, social, and cultural constraints (e.g., the temperature or the country of operation). In total, NormBank contains 63k unique constraints from a taxonomy that we introduce and iteratively refine here. Constraints then apply in different combinations to frame social norms. Under these manipulations, norms are non-monotonic - one can cancel an inference by updating its frame even slightly. Still, we find evidence that neural models can help reliably extend the scope and coverage of NormBank. We further demonstrate the utility of this resource with a series of transfer experiments.

## Authors

[[Caleb Ziems]], [[Jane Dwivedi-Yu]], [[Yi-Chia Wang]], [[Alon Halevy]], [[Diyi Yang]]

## Data Description

NormBank is a knowledge bank of 155k situational social norms grounded within a multivalent sociocultural frame called SCENE, containing 63k unique constraints including settings, roles, attributes, and behaviors. The dataset was built through scalable human annotation on Amazon Mechanical Turk, bootstrapped with GPT-3 (text-davinci-002) for generating roles and behaviors. Neural models were trained and evaluated on knowledge completion and transfer learning tasks using the NormBank data.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

47 citations (Semantic Scholar/arXiv) [2025-08-27] 47 citations (Semantic Scholar/DOI) [2025-08-23]
