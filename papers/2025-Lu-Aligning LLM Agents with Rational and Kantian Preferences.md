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
authors: "[[Lu, Wei]], [[Chen, Daniel L.]], [[Hansen, Christian B.]]"
doi: 10.48550/arXiv.2507.20796
tags: "Computer Science - Machine Learning"
url: "https://arxiv.org/abs/2507.20796"
pdf_extract: "PDF Extracts/2025/2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.md"
local_pdf: "[[PDFs/2025/2025-Lu-Aligning LLM Agents with Rational and Kantian Preferences.pdf]]"
external_pdf: "https://arxiv.org/pdf/2507.20796.pdf"
publication: arXiv
ethics_perspective: "Kantian Ethics"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Kantian Ethics, Deontology, AI Alignment, LLM Fine-tuning"
key_contribution: "Proposes supervised fine-tuning pipeline aligning LLM agents with homo economicus and homo moralis (Kantian universalizability) preferences"
significance: "Empirically tests Kantian moral concern parameter in GPT-4o; applies fine-tuned agents to autonomous vehicles and algorithmic pricing"
abstract: "Understanding how large language model (LLM) agents behave in strategic interactions is essential as these systems increasingly participate autonomously in economically and morally consequential decisions. The authors evaluate LLM preferences using canonical economic games, finding substantial deviations from human behavior. Models like GPT-4o show excessive cooperation and limited incentive sensitivity, while reasoning models, such as o3-mini, align more consistently with payoff-maximizing strategies. They propose a supervised fine-tuning pipeline that uses synthetic datasets derived from economic reasoning to align LLM agents with economic preferences, focusing on two stylized preference structures: utility depending only on individual payoffs (homo economicus) and including Kantian universalizability (homo moralis). The fine-tuned agents are assessed in moral dilemmas involving autonomous vehicles and algorithmic pricing in competitive markets."
ethics_overall: No
virtue_ethics: No
deontological_ethics: Yes
utilitarian_ethics: Yes
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Synthetic datasets from economic games"
data_metrics: "Kantian moral concern parameter κ, cooperation rates"
LLM_assessed: "GPT-4"
DATA_URL: NA
normative_ethics_benchmark: Borderline
---
# Aligning Large Language Model Agents with Rational and Moral Preferences: A Supervised Fine-Tuning Approach

## Authors

[[Wei Lu]], [[Daniel L Chen|Daniel L. Chen]], [[Christian B. Hansen]]

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
