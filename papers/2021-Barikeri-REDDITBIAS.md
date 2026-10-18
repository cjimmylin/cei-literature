---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: JKQ75SNA
type: document
short_title: REDDITBIAS
year: 2021
first_author: "[[Soumya Barikeri]]"
last_author: "[[Glavaš, Goran]]"
authors: "Barikeri, Soumya; Lauscher, Anne; Vulić, Ivan; Glavaš, Goran"
url: "https://aclanthology.org/2021.acl-long.151/"
external_pdf: "https://aclanthology.org/2021.acl-long.151.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: "Multiple Religions"
rv_islam: 100
rv_christianity: 100
rv_buddhism: 0
rv_judaism: 60
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
religious_values_list: "Islam, Christianity, Judaism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Created REDDITBIAS, the first conversational dataset from Reddit to measure bias (gender, race, religion, queerness) and tested debiasing methods on DialoGPT."
significance: "Addresses the lack of realistic conversational resources for bias, showing that debiasing can reduce religious bias without hurting chat performance."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Barikeri-REDDITBIAS.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2021/2021-Barikeri-REDDITBIAS.pdf]]"
abstract: "Text representation models are prone to exhibit a range of societal biases, reﬂecting the noncontrolled and biased nature of the underlying pretraining data, which consequently leads to severe ethical issues and even bias ampliﬁcation. Recent work has predominantly focused on measuring and mitigating bias in pretrained language models. Surprisingly, the landscape of bias measurements and mitigation resources and methods for conversational language models is still very scarce: it is limited to..."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: GPT-2
DATA_URL: "https://github.com/umanlp/RedditBias"
CONFERENCE: "ACL 2021"
ethics_overall: 80
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# REDDITBIAS: A Real-World Resource for Bias Evaluation and Debiasing in Conversational Language Models

## Authors

[[Soumya Barikeri|Barikeri, Soumya]], [[Anne Lauscher|Lauscher, Anne]], [[Ivan Vulić|Vulić, Ivan]], [[Goran Glavaš|Glavaš, Goran]]

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2021/2021-Barikeri-REDDITBIAS.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.acl-long.151/

## Abstract

Text representation models are prone to exhibit a range of societal biases, reflecting the non-controlled and biased nature of the underlying pretraining data, which consequently leads to severe ethical issues and even bias amplification. Recent work has predominantly focused on measuring and mitigating bias in pretrained language models. Surprisingly, the landscape of bias measurements and mitigation resources and methods for conversational language models is still very scarce: it is limited to only a few types of bias, artificially constructed resources, and completely ignores the impact that debiasing methods may have on the final perfor mance in dialog tasks, e.g., conversational response generation. In this work, we present REDDITBIAS, the first conversational data set grounded in the actual human conversations from Reddit, allowing for bias measurement and mitigation across four important bias dimensions: gender,race,religion, and queerness. Further, we develop an evaluation framework which simultaneously 1)measures bias on the developed REDDITBIAS resource, and 2)evaluates model capability in dialog tasks after model debiasing. We use the evaluation framework to benchmark the widely used conversational DialoGPT model along with the adaptations of four debiasing methods. Our results indicate that DialoGPT is biased with respect to religious groups and that some debiasing techniques can remove this bias while preserving downstream task performance.

## Data Description

RedditBias benchmark dataset for measuring and mitigating social biases in conversational language models across four dimensions (gender, race, religion, queerness).


## Notes

