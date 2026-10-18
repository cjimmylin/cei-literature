---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ARXIV_2507_20796
type: preprint
short_title: "Aligning LLM Agents with Rational and Kantian Preferences"
year: 2025
first_author: "[[Wei Lu]]"
last_author: "[[Christian B. Hansen]]"
authors: "Wei Lu; Daniel L. Chen; Christian B. Hansen"
doi: 10.48550/arXiv.2507.20796
tags: "Computer Science - Machine Learning"
url: "https://arxiv.org/abs/2507.20796"
pdf_extract: "PDF Extracts/2025/2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.pdf]]"
external_pdf: "https://arxiv.org/pdf/2507.20796.pdf"
publication: arXiv
CONF-CC: Preprint
ethics_perspective: "Kantian Ethics"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: Christianity
rv_islam: 0
rv_christianity: 50
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
religious_values_list: Christianity
mp_mft: 0
mp_schwartz: 0
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "Kantian Ethics, Deontology, AI Alignment, LLM Fine-tuning"
key_contribution: "Proposes supervised fine-tuning pipeline aligning LLM agents with homo economicus and homo moralis (Kantian universalizability) preferences"
significance: "Empirically tests Kantian moral concern parameter in GPT-4o; applies fine-tuned agents to autonomous vehicles and algorithmic pricing"
abstract: "Understanding how large language model (LLM) agents behave in strategic interactions is essential as these systems increasingly participate autonomously in economically and morally consequential decisions. We evaluate LLM preferences using canonical economic games, finding substantial deviations from human behavior. Models like GPT-4o show excessive cooperation and limited incentive sensitivity, while reasoning models, such as o3-mini, align more consistently with payoff-maximizing strategies."
DATE_ADDED: 20260208
LLM_assessed: "GPT-4o, o3"
DATA_URL: NA
normative_ethics_benchmark: Borderline
CONFERENCE: Preprint
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 65
utilitarian_ethics: 80
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: FR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Aligning Large Language Model Agents with Rational and Moral Preferences: A Supervised Fine-Tuning Approach

## Authors

[[Lu]], [[Wei]], [[Chen]], [[Daniel L]], [[Hansen]], [[Christian B]]

## Links

- **arXiv:** https://arxiv.org/abs/2507.20796
- **PDF:** https://arxiv.org/pdf/2507.20796.pdf
- **NBER:** https://users.nber.org/~dlchen/papers/LLMs_as_Machini_Moralis.pdf
- **SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5458954

## Abstract

Understanding how large language model (LLM) agents behave in strategic interactions is essential as these systems increasingly participate autonomously in economically and morally consequential decisions. The authors evaluate LLM preferences using canonical economic games, finding substantial deviations from human behavior. Models like GPT-4o show excessive cooperation and limited incentive sensitivity, while reasoning models, such as o3-mini, align more consistently with payoff-maximizing strategies. They propose a supervised fine-tuning pipeline that uses synthetic datasets derived from economic reasoning to align LLM agents with economic preferences, focusing on two stylized preference structures: utility depending only on individual payoffs (homo economicus) and including Kantian universalizability (homo moralis). The fine-tuned agents are assessed in moral dilemmas involving autonomous vehicles and algorithmic pricing in competitive markets.

## Data Description

This paper evaluates LLM agent behavior using canonical economic games (Sequential Prisoner's Dilemma, Trust Game, Ultimatum Game) and proposes a supervised fine-tuning pipeline to align GPT-4o agents with homo economicus and homo moralis preference structures. The study uses 50 independent sessions with 18 scenarios each, generating synthetic payoff-based training data. Fine-tuned agents are further evaluated on Moral Machine dilemmas and repeated-pricing duopoly scenarios, with o3-mini referenced for baseline comparison.


## Notes

Key finding: GPT-4o's Kantian moral concern parameter κ = 0.05 (weak but statistically significant).

## Tags

#KantianEthics #DeontologicalEthics #AIAlignment #LLMFineTuning #EconomicGames

## Citation Info

arXiv:2507.20796 [cs.LG], July 2025
