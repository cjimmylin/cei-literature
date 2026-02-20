---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 5ZMPHLEK
type: journalArticle
short_title: ValueNet
year: 2022
first_author: "[[Liang Qiu]]"
last_author: "[[Song-Chun Zhu]]"
authors: "Liang Qiu; Yizhou Zhao; Jinchao Li; Pan Lu; Baolin Peng; Jianfeng Gao; Song-Chun Zhu"
doi: 10.1609/aaai.v36i10.21368
url: "http://arxiv.org/abs/2112.06346"
external_pdf: "http://arxiv.org/pdf/2112.06346.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Presented ValueNet, a dataset of 21k text scenarios annotated with Schwartz values, and a value regression model"
significance: "First large-scale dataset for teaching agents diverse human values (Schwartz dimensions) rather than just social norms, enabling value-driven dialogue systems"
tags: 
pdf_extract: "PDF Extracts/2022/2022-Qiu-ValueNet.md"
abstract: "Building a socially intelligent agent involves many challenges, one of which is to teach the agent to speak guided by its value like a human. However, value-driven chatbots are still understudied in the area of dialogue systems. Most existing datasets focus on commonsense reasoning or social norm modeling. In this work, we present a new large-scale human value dataset called VALUENET, which contains human attitudes on 21,374 text scenarios."
paper_summary: "Abstract: Building a socially intelligent agent involves many chal- lenges, one of which is to teach the agent to speak guided by its value like a human. However, value-driven chatbots are still understudied in | Overview: VALUENET: A New Dataset for Human Value Driven Dialogue System Liang Qiu1, Yizhou Zhao1, Jinchao Li2, Pan Lu1, Baolin Peng2, Jianfeng Gao2, Song-Chun Zhu1 1UCLA Center for Vision, Cognition, Learning, | Methodology: obtains a relative improvement of 5.2% on DistilBERT and | Key Findings: We compare the performance between our imple- mentation and the baseline that directly applies the BERT model for emotion classiﬁcation. As shown in T | Conclusions: We introduce a new dataset for human value modeling, VAL- UENET, which contains 21,374 scenarios in ten distinct hu- man values. We also apply the lea"
local_pdf: "[[PDFs/2022/2022-Qiu-ValueNet.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "BERT, RoBERTa, BART"
DATA_URL: "https://liang-qiu.github.io/ValueNet/"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus for conversational ai"
data_metrics: "Not specified"
CONFERENCE: "Journal"
---
# ValueNet: A New Dataset for Human Value Driven Dialogue System

## Metadata

**Authors:** Qiu, Liang; Zhao, Yizhou; Li, Jinchao; Lu, Pan; Peng, Baolin; Gao, Jianfeng; Zhu, Song-Chun

**Year:** 2022

**Publication:** Proceedings of the AAAI Conference on Artificial Intelligence

**Type:** journalArticle

**DOI:** [10.1609/aaai.v36i10.21368](https://doi.org/10.1609/aaai.v36i10.21368)

**Pages:** 11183-11191

**Volume/Issue:** Vol. 36, Issue 10

## Links

- **Local PDF:** [[PDFs/2022/2022-Qiu-ValueNet.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2112.06346
- **DOI:** https://doi.org/10.1609/aaai.v36i10.21368

## Abstract

Building a socially intelligent agent involves many challenges, one of which is to teach the agent to speak guided by its value like a human. However, value-driven chatbots are still understudied in the area of dialogue systems. Most existing datasets focus on commonsense reasoning or social norm modeling. In this work, we present a new large-scale human value dataset called VALUENET, which contains human attitudes on 21,374 text scenarios. The dataset is organized in ten dimensions that conform to the basic human value theory in intercultural research. We further develop a Transformerbased value regression model on VALUENET to learn the utility distribution. Comprehensive empirical results show that the learned value model could beneﬁt a wide range of dialogue tasks. For example, by teaching a generative agent with reinforcement learning and the rewards from the value model, our method attains state-of-the-art performance on the personalized dialog generation dataset: PERSONA-CHAT. With values as additional features, existing emotion recognition models enable capturing rich human emotions in the context, which further improves the empathetic response generation performance in the EMPATHETICDIALOGUES dataset. To the best of our knowledge, VALUENET is the ﬁrst largescale text dataset for human value modeling, and we are the ﬁrst one trying to incorporate a value model into emotionally intelligent dialogue systems. The dataset is available at https://liang-qiu.github.io/ValueNet/.

## Authors

[[Liang Qiu]], [[Yizhou Zhao]], [[Jinchao Li]], [[Pan Lu]], [[Baolin Peng]], [[Jianfeng Gao]], [[Song-Chun Zhu]]

## Data Description

VALUENET is a large-scale dataset containing human attitudes on 21,374 text scenarios organized across ten Schwartz basic human value dimensions (e.g., security, power, achievement, benevolence). Scenarios were curated from SOCIAL-CHEM-101 using value-related keywords and annotated by 443 qualified Amazon Mechanical Turk workers for positive, negative, or neutral attitudes. The dataset was used to train Transformer-based value regression models (BERT, RoBERTa, DistilBERT, BART) and applied to personalized dialogue generation and empathetic response generation tasks.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

38 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/arXiv) [2025-08-27] 38 citations (Semantic Scholar/arXiv) [2025-08-23] 7 citations (Crossref/DOI) [2025-08-23]
