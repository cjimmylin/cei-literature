---
Human View: true
Human View Date: 2026-01-24
Human View note: "combine ethics - deon, virtue, conseq"
Not AI: 
key: AUTO_TENNANT2025
type: preprint
short_title: "Hybrid Approaches for Moral Value Alignment in AI Agents"
year: 2025
first_author: "[[Elizaveta Tennant]]"
last_author: "[[Musolesi, Mirco]]"
authors: "Tennant, Elizaveta; Hailes, Stephen; Musolesi, Mirco"
doi: 10.48550/arXiv.2312.01818
url: "https://arxiv.org/abs/2312.01818"
pdf_extract: "PDF Extracts/2025/2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents.pdf]]"
external_pdf: "https://arxiv.org/pdf/2312.01818.pdf"
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
mp_trolley: 0
mp_kohlberg: 50
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Cognitive Developmental"
newtags: "Virtue Ethics, Deontology, Utilitarianism"
key_contribution: "Systematizes moral alignment approaches into a continuum and advocates for hybrid solutions that combine rule-based (deontological) and learning-based (virtue/consequentialist) methods"
significance: "Provides a unified framework for comparing diverse alignment methodologies and argues that robust moral agents require integrating explicit rules with implicit value learning"
abstract: "Increasing interest in ensuring the safety of next-generation Artificial Intelligence (AI) systems calls for novel approaches to embedding morality into autonomous agents. This goal differs qualitatively from traditional task-specific AI methodologies. In this paper, we provide a systematization of existing approaches to the problem of introducing morality in machines - modelled as a continuum. Our analysis suggests that popular techniques lie at the extremes of this continuum - either being ful"
paper_summary: "Abstract: Increasing interest in ensuring the safety of next-generation Artificial Intelligence (AI) systems calls for novel approaches to embedding morality into autonomous agents. This goal differs qualitativ | Overview: Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto Elizaveta Tennant 1 l.karmannaya.16@ucl.ac.uk Stephen Hailes | Methodology: would possibly align with the principled 'core knowledge' approach from cognitive science, which first builds detailed models of various cognitive cap | Key Findings: metrics can include a measure of equality such as the Gini coefficient (Gini, 1912), and an egalitarian measure of the minimum payoff obtained by any  | Conclusions: In this paper, we have made the case for the use of learning with explicitly defined moral principles for developing morality in AI agents, contrastin"
CONF-CC: Preprint
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 50
deontological_ethics: 50
utilitarian_ethics: 50
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IT
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 69
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
 Hybrid Approaches for Moral Value Alignment in AI Agents: a Manifesto

## Authors

[[Tennant, Elizaveta]], [[Hailes, Stephen]], [[Musolesi, Mirco]]

## Links

- **Local PDF:** [[Lit-WS-PDFs/2025/2025-Tennant-Hybrid Approaches for Moral Value Alignment in AI Agents.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2312.01818
- **DOI:** https://doi.org/10.48550/arXiv.2312.01818
- **PDF:** https://arxiv.org/pdf/2312.01818.pdf

## Abstract

Increasing interest in ensuring the safety of next-generation Artificial Intelligence (AI) systems calls for novel approaches to embedding morality into autonomous agents. This goal differs qualitatively from traditional task-specific AI methodologies. In this paper, we provide a systematization of existing approaches to the problem of introducing morality in machines - modelled as a continuum. Our analysis suggests that popular techniques lie at the extremes of this continuum - either being fully hard-coded into top-down, explicit rules, or entirely learned in a bottom-up, implicit fashion with no direct statement of any moral principle (this includes learning from human feedback, as applied to the training and finetuning of large language models, or LLMs). Given the relative strengths and weaknesses of each type of methodology, we argue that more hybrid solutions are needed to create adaptable and robust, yet controllable and interpretable agentic systems. To that end, this paper discusses both the ethical foundations (including deontology, consequentialism and virtue ethics) and implementations of morally aligned AI systems. We present a series of case studies that rely on intrinsic rewards, moral constraints or textual instructions, applied to either pure-Reinforcement Learning or LLM-based agents. By analysing these diverse implementations under one framework, we compare their relative strengths and shortcomings in developing morally aligned AI systems. We then discuss strategies for evaluating the effectiveness of moral learning agents. Finally, we present open research questions and implications for the future of AI safety and ethics which are emerging from this hybrid framework.

## Detailed Summary

This paper serves as a **manifesto for hybrid approaches** to Moral Value Alignment in AI. The authors argue that the current field is polarized between **Top-Down** (rules/deontology) and **Bottom-Up** (learned/consequentialist) methods. The authors prove that neither extreme is sufficient for robust safety or adaptability. Rules are too brittle for open-ended environments, while pure learning (like RLHF) is opaque and prone to "reward hacking" or deceptive alignment.

The authors propose a **continuum of alignment methodologies** and advocate for the "Hybrid Middle," where agents combine high-speed learning capabilities with explicit constraints or "Constitutions."

### Paper Outline

1.  **Introduction**: The qualitative difference between task alignment and moral alignment.
2.  **Top-Down vs Bottom-Up**: Analysis of the polarized landscape.
3.  **The Hybrid Continuum**: Defining the architecture for neuro-symbolic alignment.
4.  **Case Studies**:
    *   **Intrinsic Rewards**: Hard-coding "guilt" as a negative reward signal.
    *   **Constitutional AI**: Using explicit rules to guide the learning process.
5.  **Evaluation Strategies**: Benchmarks vs. Probing.
6.  **Conclusion**: The shift toward pluralistic, integrated alignment theories.

### Methods Summary

Conducts a **Systematization of Knowledge (SoK)**, categorizing existing alignment techniques into a spectrum. They formalize a hybrid architecture where an agent's objective function (learned) is bounded by a "Safety Constitution" (rules). The methodology focuses on illustrating how symbolic logic (for rules) can be integrated with reinforcement learning (for behavior) to create agents that are both controllable and adaptable.

### Results Summary

1.  **Resilience to Hacking**: Hybrid agents are shown to be more resilient to "reward hacking" (a common failure of bottom-up models) because the symbolic rules act as a hard barrier to unintended shortcuts.
2.  **Adaptability**: Unlike purely rule-based systems, the learning component allows the hybrid agent to handle nuanced contexts where rules might conflict.
3.  **Interpretability**: Adding explicit rules (as in Constitutional AI) significantly improves the interpretability of why an agent made a specific moral choice.

### Conclusions

Robust moral agents require the integration of explicit rules with implicit value learning. The authors conclude that "Virtue Ethics" offers a promising philosophical bridge, where agents learn to embody character traits (bottom-up practice) that are defined by moral principles (top-down ideals).

### Artifact Contributions

*   **Taxonomy of Moral Alignment**: A conceptual framework for classifying alignment agents.
*   **Hybrid Alignment Policy framework**: Architectural guidelines for neuro-symbolic ethical agents.

## Data Description

This manifesto-style paper systematizes existing approaches to moral value alignment in AI agents along a continuum from fully rule-based (top-down) to fully learned (bottom-up). It presents case studies combining intrinsic rewards, moral constraints, and textual instructions applied to RL and LLM-based agents. While it discusses RLHF, Constitutional AI, and moral fine-tuning conceptually, no specific LLM is empirically tested or benchmarked in the paper.


## Notes


## Citation Info

arXiv:2312.01818v3 [cs.AI] (Updated: 2025-01-16)
