---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 4VA5XC6H
type: conferencePaper
short_title: "Addressing Moral Uncertainty using Large Language"
year: 2025
first_author: "[[Rohit K. Dubey]]"
last_author: "[[Mahajan, Sachit]]"
authors: "[[Dubey, Rohit K.]]; [[Dailisan, Damian]]; [[Mahajan, Sachit]]"
doi: 10.48550/arXiv.2503.05724
url: "http://arxiv.org/abs/2503.05724"
pdf_extract: "PDF Extracts/2025/2025-Dubey-Addressing Moral Uncertainty using Large Language.md"
local_pdf: "[[PDFs/2025/2025-Dubey-Addressing Moral Uncertainty using Large Language.pdf]]"
external_pdf: "http://arxiv.org/pdf/2503.05724.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Virtue Ethics, Deontology, Utilitarianism"
key_contribution: "Presents Ethical-RL, a framework using LLMs to provide feedback based on consequentialist, deontological, and virtue ethics, aggregated via Belief Jensen-Shannon Divergence"
significance: "Enables RL agents to navigate moral uncertainty by integrating diverse ethical perspectives, reducing reliance on handcrafted rewards and improving adaptability"
tags: 
abstract: "We present an ethical decision-making framework that refines a pre-trained reinforcement learning (RL) model using a task-agnostic ethical layer. Following initial training, the RL model undergoes ethical finetuning, where human feedback is replaced by feedback generated from a large language model (LLM). The LLM embodies consequentialist, deontological, virtue, social justice, and care ethics as moral principles to assign belief values to recommended actions during ethical decision-making."
paper_summary: "Abstract: We present an ethical decision-making framework that refines a pre-trained reinforcement learning (RL) model using a task-agnostic ethical layer. Following initial training, the RL model undergoes eth | Overview: Addressing Moral Uncertainty using Large Language Models for Ethical Decision-Making Rohit K. Dubey†, Damian Dailisan† and Sachit Mahajan† *Computational Social Science, ETH Z¨urich, Zurich, Switzerla | Methodology: that makes use of a Belief Jensen–Shannon Divergence (BJSD) method to systematically measure the discrepancies and conflicts among BBAs, processes the | Key Findings: benchmarks are critical for equitable and robust outcomes. By integrating Belief Probability Assignment (BPA) into reinforcement learning, AMULED enab | Conclusions: We present two simple scenarios where an ethics-based shaping algorithm helps RL agents make ethi- cally sound decisions while still achieving their p"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Mistral, Llama-3"
DATA_URL: "https://github.com/xxxxx/moral"
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
CONFERENCE: "Other Conference"
---
 Addressing Moral Uncertainty using Large Language Models for Ethical Decision-Making

## Authors

[[Dubey, Rohit K]], [[Damian Dailisan|Dailisan, Damian]], [[Sachit Mahajan|Mahajan, Sachit]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Dubey-Addressing Moral Uncertainty using Large Language.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.05724
- **DOI:** https://doi.org/10.48550/arXiv.2503.05724

## Abstract

We present an ethical decision-making framework that refines a pre-trained reinforcement learning (RL) model using a task-agnostic ethical layer. Following initial training, the RL model undergoes ethical fine-tuning, where human feedback is replaced by feedback generated from a large language model (LLM). The LLM embodies consequentialist, deontological, virtue, social justice, and care ethics as moral principles to assign belief values to recommended actions during ethical decision-making. An ethical layer aggregates belief scores from multiple LLM-derived moral perspectives using Belief Jensen–Shannon Divergence and Dempster–Schaefer Theory into probability scores that also serve as the shaping reward, steering the agent toward choices that align with a balanced ethical framework. This integrated learning framework helps the RL agent navigate moral uncertainty in complex environments and enables it to make morally sound decisions across diverse tasks. Our approach, tested across different LLM variants and compared with other belief aggregation techniques, demonstrates improved consistency, adaptability, and reduced reliance on handcrafted ethical rewards. This method is especially effective in dynamic scenarios where ethical challenges arise unexpectedly, making it well-suited for real-world applications.

## Detailed Summary

This paper presents an **Ethical Decision-Making Framework** that integrates **Moral Uncertainty** into Reinforcement Learning (RL) agents. Recognizing that no single moral theory (Utilitarianism, Deontology, etc.) is sufficient for all situations, the authors propose an **Ethical Layer** that sits on top of a standard RL agent.

This layer uses a Large Language Model (LLM) as a "Moral Parliament." For every action proposed by the agent, the LLM evaluates it from five distinct ethical perspectives: **Consequentialist**, **Deontological**, **Virtue Ethics**, **Care Ethics**, and **Social Justice**.

## Paper Outline

1.  **Introduction**: Mono-theoretical AI is brittle; Moral Uncertainty is necessary.
2.  **Related Work**: Machine Ethics, RL, Hybrid AI.
3.  **Methodology**:
    *   **Task-Agnostic Ethical Layer**: The module structure.
    *   **LLM as Moral Reasoner**: Prompts for the 5 frameworks.
    *   **Belief Aggregation**: Using DST and JSD to combine the 5 scores.
4.  **Experimental Setup**: "Baby in Room" Gridworld navigation.
5.  **Results**: Multi-perspective agents behave more safely than single-perspective ones.
6.  **Conclusion**: LLM-driven moral uncertainty offers a scalable way to align RL agents.

## Methods Summary

The authors implement an **Ethical Layer Architecture**:
1.  **Framework Evaluation**: An LLM generates 5 scores (0-1) for every proposed action based on 5 prompts representing different ethical frameworks (U, D, V, Care, Justice).
2.  **Belief Aggregation**: These scores are aggregated using **Dempster-Shafer Theory** (to handle uncertainty/conflict) and **Jensen-Shannon Divergence** to produce a unified ethical probability.
3.  **Reward Shaping**: This probability is converted into an "Ethical Shaping Reward" ($R_{total} = R_{env} + \lambda \cdot R_{ethical}$) that guides the agent toward choices that align with a balanced ethical framework.
4.  **Validation**: Tested in a Gridworld "Baby in Room" scenario where the safest path (avoiding babies) and shortest path (efficient) must be balanced.

## Results Summary

1.  **Robustness of Aggregation**: Aggregating multiple ethical views (the "Parliament" approach) produces agents that avoid catastrophic failures (e.g., stepping on a baby to get milk faster) which might be missed by a single-theory reward.
2.  **Dempster-Shafer Efficacy**: Using DST to fuse the LLM's "belief masses" provides a better smoothing signal than simple averaging, effectively handling cases where frameworks disagree (High Uncertainty).
3.  **LLM as Reward Function**: Task-agnostic LLM feedback works effectively as a dense reward signal for RL, removing the need to manually code complex reward functions for every constraint.

## Conclusions

AI should not be "aligned" to one ideology or ethical theory, but should be capable of navigating the uncertainty inherent in human ethics. The "Moral Parliament" approach provides a scalable and theoretically grounded way to implement pluralistic alignment in RL agents.

## Artifact Contributions

*   **Ethical-RL Framework**: Codebase for LLM-guided RL with Dempster-Shafer aggregation.
*   **Evaluation Environment**: The "Baby in Room" Gridworld multi-objective benchmark.
*   **Moral Prompts**: set of system prompts for the 5 ethical frameworks.

## Data Description

The paper introduces AMULED, an ethical decision-making framework that uses LLMs as moral agents to provide feedback for reinforcement learning. It tests GPT-4o-mini, Mistral-nemo, and Llama-3.1 (8B and 70B) as backbone moral agents across two RL environments: Finding Milk (route planning with ethical constraints involving babies) and Driving and Rescuing (autonomous driving with ethical dilemmas), using five moral clusters (consequentialist, deontological, virtue, care, and social justice ethics) aggregated via Belief Jensen-Shannon Divergence.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society

## Citation Info

1 citations (Semantic Scholar/arXiv) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-27] 1 citations (Semantic Scholar/DOI) [2025-08-23]
