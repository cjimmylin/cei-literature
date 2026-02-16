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
authors: "[[Barikeri, Soumya]]; [[Lauscher, Anne]]; [[Vulić, Ivan]]; [[Glavaš, Goran]]"
url: "https://aclanthology.org/2021.acl-long.151/"
external_pdf: "https://aclanthology.org/2021.acl-long.151.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Created REDDITBIAS, the first conversational dataset from Reddit to measure bias (gender, race, religion, queerness) and tested debiasing methods on DialoGPT."
significance: "Addresses the lack of realistic conversational resources for bias, showing that debiasing can reduce religious bias without hurting chat performance."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Barikeri-REDDITBIAS.md"
local_pdf: "[[PDFs/2021/2021-Barikeri-REDDITBIAS.pdf]]"
abstract: "Text representation models are prone to exhibit a range of societal biases, reﬂecting the noncontrolled and biased nature of the underlying pretraining data, which consequently leads to severe ethical issues and even bias ampliﬁcation. Recent work has predominantly focused on measuring and mitigating bias in pretrained language models. Surprisingly, the landscape of bias measurements and mitigation resources and methods for conversational language models is still very scarce: it is limited to..."
DATE_ADDED: 20260208
LLM_assessed: GPT-2
DATA_URL: "https://github.com/umanlp/RedditBias"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# REDDITBIAS: A Real-World Resource for Bias Evaluation and Debiasing in Conversational Language Models

## Authors

[[Soumya Barikeri|Barikeri, Soumya]], [[Anne Lauscher|Lauscher, Anne]], [[Ivan Vulić|Vulić, Ivan]], [[Goran Glavaš|Glavaš, Goran]]

## Links

- **Local PDF:** [[PDFs/2021/2021-Barikeri-REDDITBIAS.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.acl-long.151/

## Abstract

Text representation models are prone to exhibit a range of societal biases, reflecting the non-controlled and biased nature of the underlying pretraining data, which consequently leads to severe ethical issues and even bias amplification. Recent work has predominantly focused on measuring and mitigating bias in pretrained language models. Surprisingly, the landscape of bias measurements and mitigation resources and methods for conversational language models is still very scarce: it is limited to only a few types of bias, artificially constructed resources, and completely ignores the impact that debiasing methods may have on the final perfor mance in dialog tasks, e.g., conversational response generation. In this work, we present REDDITBIAS, the first conversational data set grounded in the actual human conversations from Reddit, allowing for bias measurement and mitigation across four important bias dimensions: gender,race,religion, and queerness. Further, we develop an evaluation framework which simultaneously 1)measures bias on the developed REDDITBIAS resource, and 2)evaluates model capability in dialog tasks after model debiasing. We use the evaluation framework to benchmark the widely used conversational DialoGPT model along with the adaptations of four debiasing methods. Our results indicate that DialoGPT is biased with respect to religious groups and that some debiasing techniques can remove this bias while preserving downstream task performance.

## Data Description

REDDITBIAS is a conversational dataset grounded in real Reddit conversations, designed for bias measurement and mitigation across four dimensions: gender, race, religion (two subtypes), and queerness. The dataset includes approximately 11,873 manually annotated comments and corresponding target phrases, split into training, development, and test sets. The evaluation framework benchmarks DialoGPT (a GPT-2 variant) using perplexity-based bias measures alongside dialog state tracking on MultiWoZ and conversational response generation on DSTC-7.


## Notes

