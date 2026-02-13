---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: NXYQCYND
type: conferencePaper
short_title: "Steering Risk Preferences in Large Language"
year: 2025
first_author: "[[Jian-Qiao Zhu]]"
last_author: "[[Thomas L. Griffiths]]"
authors: "Jian-Qiao Zhu; Haijiang Yan; Thomas L. Griffiths"
doi: 10.48550/arXiv.2505.11615
url: "http://arxiv.org/abs/2505.11615"
external_pdf: "http://arxiv.org/pdf/2505.11615.pdf"
publication: arXiv.org
research_topic: "NLP & Representation Learning"
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: 
tags: 
pdf_extract: "PDF Extracts/2025/2025-Zhu-Steering Risk Preferences in Large Language.md"
abstract: "Changing the behavior of large language models (LLMs) can be as straightforward as editing the Transformer’s residual streams using appropriately constructed “steering vectors.” These modifications to internal neural activations, a form of representation engineering, offer an effective and targeted means of influencing model behavior without retraining or fine-tuning the model. But how can such steering vectors be systematically identified? We propose a principled approach for uncovering steerin"
paper_summary: "Abstract: Changing the behavior of large language models (LLMs) can be as straightforward as editing the Transformer’s residual streams using appropriately constructed “steering vectors.” These modifications to | Overview: arXiv:2505.11615v1 [cs.CL] 16 May 2025 Steering Risk Preferences in Large Language Models by Aligning Behavioral and Neural Representations Jian-Qiao Zhu∗ Department of Computer Science Princeton Univ | Methodology: for uncovering steering vectors by aligning latent representations elicited through behavioral methods (specifically, Markov chain Monte Carlo with LL | Conclusions: We investigated the use of aligned behavioral and neural representations of risk to steer LLM behavior across three risk-related domains: risky decisi"
local_pdf: "[[PDFs/2025/2025-Zhu-Steering Risk Preferences in Large Language.pdf]]"
key_contribution: "Proposes a principled approach for steering risk preferences in LLMs by aligning behavioral representations (elicited via MCMC) with neural representations (activations)."
significance: "Bridges the gap between behavioral psychometrics and mechanistic interpretability, providing a lightweight, training-free way to control model risk-taking behavior for safer alignment."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
LLM_assessed: "Gemma"
DATA_URL: "NA"
---
# Steering Risk Preferences in Large Language Models by Aligning Behavioral and Neural Representations

## Metadata

**Authors:** Zhu, Jian-Qiao; Yan, Haijiang; Griffiths, Thomas L.

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.11615](https://doi.org/10.48550/arXiv.2505.11615)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Zhu-Steering Risk Preferences in Large Language.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.11615
- **DOI:** https://doi.org/10.48550/arXiv.2505.11615

## Abstract

This paper proposes a principled approach for **Steering Risk Preferences** in LLMs. The authors address the challenge of identifying the correct "Steering Vectors" (directions in the neural activation space to intervene on). They propose aligning **Behavioral Representations** (elicited via MCMC sampling of model choices) with **Neural Representations** (activations). This allows them to mathematically map "Risk Seeking" or "Risk Averse" behaviors to specific neuron clusters and control them.

### Detailed Summary
"Representation Engineering" allows us to control model behavior by adding vectors to residual streams (like "lobotomizing" a specific urge). The hard part is finding the vector.
The authors use **Markov Chain Monte Carlo (MCMC)** to sample the model's "Latent Risk Preference" from its behavior in economic games (e.g., "Would you take this gamble?"). They then correlate this behavioral latent variable with the internal neural state. The resulting vector, when added back to the model during inference, reliably makes the model more or less risky.

### Paper Outline
1.  **Introduction**: Steering vectors as a lightweight alternative to fine-tuning.
2.  **Methodology**:
    *   Behavioral Elicitation: Using MCMC to estimate the model's risk parameter ($\rho$) from choice data.
    *   Neural Alignment: Regressing the neural state against the estimated $\rho$.
    *   Steering: Injecting the learned vector.
3.  **Experiments**: Controlling risk taking in financial and social decision tasks.
4.  **Results**: High correlation between injection strength and risk behavior.

### Methods Summary
*   **Task**: Repeated gambles / Decision-making under uncertainty.
*   **Metric**: Rate of choosing the "Safe" vs. "Risky" option.
*   **Technique**: **Behavioral-Neural Alignment**. Instead of just "taking the average activation of risky prompts" (a naive method), they solve for the vector that *maximizes the correlation* with the MCMC-estimated behavioral trait.

### Results Summary
1.  **Reliability**: The steered models showed consistent shifts in risk preference across different domains, not just the training domain.
2.  **Granularity**: The method allows for continuous control (e.g., "Make the model 20% more risk-averse").
3.  **Neuro-Symbolic Link**: This paper bridges the gap between "Psychometric" (Behavioral) and "Mechanistic" (Neural) interpretability.

### Conclusions
We can "tune" the personality of an LLM at inference time using behaviorally-grounded steering vectors. This is a powerful tool for safety (e.g., ensuring a medical bot is always risk-averse).

### Artifact Contributions
*   **Steering Code**: Framework for MCMC elicitation and vector injection.
*   **Risk Preference Dataset**: Set of gambles for calibrating LLMs.

## Authors

[[Jian-Qiao Zhu]], [[Haijiang Yan]], [[Thomas L. Griffiths]]

## Data Description

The study uses a behavioral elicitation approach based on Markov chain Monte Carlo (MCMC) to extract latent risk preferences from Gemma-2-9B-Instruct (and Gemma-2-2B-Instruct in appendix). The experimental data consists of 3,000 binary choices between gambles defined over a probability triangle with three outcomes ($0, $50, $100), along with neural activations from the model's residual stream. The evaluation spans three domains: risky decision-making with classic prospect-theory gambles, risk perception ratings of 150 real-world risky events, and steered text generation.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
