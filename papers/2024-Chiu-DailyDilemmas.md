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
CONF-CC: "ICLR 2024"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
mp_mft: 100
mp_schwartz: 0
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory, Trolley / Dilemmas (Psych)"
newtags: "Moral Foundations Theory, Moral Reasoning & Psychology"
key_contribution: "Presented DailyDilemmas, a dataset of 1,360 everyday moral dilemmas, using it to analyze LLM value preferences through five frameworks (e.g., Moral Foundations, Maslow)."
significance: "Reveals that current LLMs exhibit distinct value biases (e.g., favoring self-expression over survival) and that system prompts are often ineffective at steering these ingrained value prioritizations."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Chiu-DailyDilemmas.md"
abstract: "As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DAILYDILEMMAS, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action."
paper_summary: "Abstract: As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of peop | Overview: Published as a conference paper at ICLR 2025 DAILYDILEMMAS: REVEALING VALUE PREFERENCES OF LLMS WITH QUANDARIES OF DAILY LIFE Yu Ying Chiu♡, Liwei Jiang♡, Yejin Choi♡ ♡University of Washington kellycy | Methodology: (Park et al., 2023; Shao et al., 2023) and our study lies in applying such a methodology to moral value judgments. Human Verification. We used the Ope | Key Findings: Have ≥1 similar dilemma 1st: similar 2nd: no 3rd: no Result: Have ≥1 similar dilemma Table 5: Annotated examples on our reddit validation dataset. 1st | Conclusions: We introduce DAILYDILEMMAS, a dataset for evaluating how LLMs navigate value conflicts in daily life. Grounded in theories from psychology, philosophy"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2024/2024-Chiu-DailyDilemmas.pdf]]
DATE_ADDED: 20260208
LLM_assessed: "Claude-3 Haiku, GPT-3.5, GPT-4, Llama-2, Llama-3, Mixtral"
DATA_URL: "https://hf.co/datasets/kellycyy/daily_dilemmas, https://github.com/kellycyy/daily_dilemmas"
CONFERENCE: "ICLR 2024"
ethics_overall: 90
virtue_ethics: 10
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
normative_ethics_benchmark: Yes
ethics_perspective: "Moral Reasoning & Psychology"
nw_confucian: 10
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
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
---
# DailyDilemmas: Revealing Value Preferences of LLMs with Quandaries of Daily Life

## Metadata

**Authors:** Chiu, Yu Ying; Jiang, Liwei; Choi, Yejin

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2410.02683](https://doi.org/10.48550/arXiv.2410.02683)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Chiu-DailyDilemmas.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2410.02683
- **DOI:** https://doi.org/10.48550/arXiv.2410.02683

## Abstract

As users increasingly seek guidance from LLMs for decision-making in daily life, many of these decisions are not clear-cut and depend significantly on the personal values and ethical standards of people. We present DAILYDILEMMAS, a dataset of 1,360 moral dilemmas encountered in everyday life. Each dilemma presents two possible actions, along with affected parties and relevant human values for each action. Based on these dilemmas, we gather a repository of human values covering diverse everyday topics, such as interpersonal relationships, workplace, and environmental issues. With DAILYDILEMMAS, we evaluate LLMs on these dilemmas to determine what action they will choose and the values represented by these action choices. Then, we analyze values through the lens of five theoretical frameworks inspired by sociology, psychology, and philosophy, including the World Values Survey, Moral Foundations Theory, Maslow’s Hierarchy of Needs, Aristotle’s Virtues, and Plutchik’s Wheel of Emotions. For instance, we find LLMs are most aligned with self-expression over survival in World Values Survey and care over loyalty in Moral Foundations Theory. Interestingly, we find substantial preference differences in models for some core values. For example, for truthfulness, Mixtral-8x7B neglects it by 9.7% while GPT-4-turbo selects it by 9.4%. We also study the recent guidance released by OpenAI (ModelSpec), and Anthropic (Constitutional AI) to understand how their designated principles reflect their models’ actual value prioritization when facing nuanced moral reasoning in daily-life settings. Finally, we find that end users cannot effectively steer such prioritization using system prompts.

## Authors

[[Yu Ying Chiu]], [[Liwei Jiang]], [[Yejin Choi]]

## Data Description

DailyDilemmas: a dataset of 1,360 moral dilemmas encountered in everyday life, each with two possible actions, affected parties, and relevant human values, analyzed through five theoretical frameworks (World Values Survey, Moral Foundations Theory, Maslow's Hierarchy, Aristotle's Virtues, Plutchik's Emotions).


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

12 citations (Semantic Scholar/arXiv) [2025-08-27] 12 citations (Semantic Scholar/DOI) [2025-08-23]
