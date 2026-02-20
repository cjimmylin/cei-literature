---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SD7W6PHQ
type: conferencePaper
short_title: DailyDilemmas
year: 2024
first_author: "[[Yu Ying Chiu]]"
last_author: "[[Yejin Choi]]"
authors: "Yu Ying Chiu; Liwei Jiang; Yejin Choi"
doi: 10.48550/arXiv.2410.02683
url: "http://arxiv.org/abs/2410.02683"
external_pdf: "http://arxiv.org/pdf/2410.02683.pdf"
publication: "International Conference on Learning Representations"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Moral Foundations Theory"
newtags: "Moral Foundations Theory, Moral Reasoning & Psychology"
key_contribution: "Presented DailyDilemmas, a dataset of 1,360 everyday moral dilemmas, using it to analyze LLM value preferences through five frameworks (e.g., Moral Foundations, Maslow)."
significance: "Reveals that current LLMs exhibit distinct value biases (e.g., favoring self-expression over survival) and that system prompts are often ineffective at steering these ingrained value prioritizations."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Chiu-DailyDilemmas.md"
abstract: "As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DAILYDILEMMAS, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action."
paper_summary: "Abstract: As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of peop | Overview: Published as a conference paper at ICLR 2025 DAILYDILEMMAS: REVEALING VALUE PREFERENCES OF LLMS WITH QUANDARIES OF DAILY LIFE Yu Ying Chiu♡, Liwei Jiang♡, Yejin Choi♡ ♡University of Washington kellycy | Methodology: (Park et al., 2023; Shao et al., 2023) and our study lies in applying such a methodology to moral value judgments. Human Verification. We used the Ope | Key Findings: Have ≥1 similar dilemma 1st: similar 2nd: no 3rd: no Result: Have ≥1 similar dilemma Table 5: Annotated examples on our reddit validation dataset. 1st | Conclusions: We introduce DAILYDILEMMAS, a dataset for evaluating how LLMs navigate value conflicts in daily life. Grounded in theories from psychology, philosophy"
local_pdf: "[[PDFs/2024/2024-Chiu-DailyDilemmas.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Llama-3, Mixtral, Claude"
DATA_URL: "https://hf.co/datasets/kellycyy/daily_dilemmas, https://github.com/kellycyy/daily_dilemmas"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
CONFERENCE: "ICLR 2024"
---
# DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life

## Metadata

**Authors:** Chiu, Yu Ying; Jiang, Liwei; Choi, Yejin

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.02683](https://doi.org/10.48550/arXiv.2410.02683)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Chiu-DailyDilemmas.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.02683
- **DOI:** https://doi.org/10.48550/arXiv.2410.02683

## Abstract

As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DAILYDILEMMAS, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action. Based on these dilemmas, we gather a repository of human values covering diverse everyday topics, such as interpersonal relationships, workplace, and environmental issues. With DAILYDILEMMAS, we evaluate LLMs on these dilemmas to determine what action they will choose and the values represented by these action choices. Then, we analyze values through the lens of five theoretical frameworks inspired by sociology, psychology, and philosophy, including the World Values Survey, Moral Foundations Theory, Maslow’s Hierarchy of Needs, Aristotle’s Virtues, and Plutchik’s Wheel of Emotions. For instance, we find LLMs are most aligned with self-expression over survival in World Values Survey and care over loyalty in Moral Foundations Theory. Interestingly, we find substantial preference differences in models for some core values. For example, for truthfulness, Mixtral-8x7B neglects it by 9.7% while GPT-4-turbo selects it by 9.4%. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their designated principles reflect their models’ actual value prioritization when facing nuanced moral reasoning in daily-life settings. Finally, we find that end users cannot effectively steer such prioritization using system prompts.

## Authors

[[Yu Ying Chiu]], [[Liwei Jiang]], [[Yejin Choi]]

## Data Description

DAILYDILEMMAS is a dataset of 1,360 moral dilemmas encountered in everyday life, generated with GPT-4 and covering 17 topics from interpersonal relationships to environmental issues. Each dilemma presents two possible actions with associated stakeholders and 301 human values mapped to five theoretical frameworks (World Values Survey, Moral Foundations Theory, Maslow's Hierarchy of Needs, Aristotle's Virtues, Plutchik's Wheel of Emotions). Six LLMs are evaluated on their value preferences through binary-choice action selections.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

12 citations (Semantic Scholar/arXiv) [2025-08-27] 12 citations (Semantic Scholar/DOI) [2025-08-23]
