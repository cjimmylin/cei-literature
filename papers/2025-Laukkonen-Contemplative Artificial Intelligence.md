---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ZCHG4W4T
type: journalArticle
year: 2025
short_title: "Contemplative Artificial Intelligence"
first_author: "[[Ruben E Laukkonen]]"
last_author: "[[Adam Elwood]]"
authors: "[[Ruben E Laukkonen]], [[Fionn Inglis]], [[Shamil Chandaria]], [[Lars Sandved-Smith]], [[Edmundo Lopez-Sola]], [[Jakob Hohwy]], [[Jonathan Gold]], [[Adam Elwood]]"
external_pdf: "file:///Users/jimmylin/Zotero/storage/744PDNTG/Laukkonen et al. - Contemplative Artificial Intelligence.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Virtue Ethics"
key_contribution: "Introduces 'Contemplative AI' principles (mindfulness, emptiness, non-duality, boundless care) to instill a resilient 'Wise World Model' in AI"
significance: "Demonstrates that contemplative principles can improve AI performance on ethical benchmarks and boost cooperation in social dilemmas by reducing goal fixation and self-other boundaries"
local_pdf: "[[PDFs/2025/2025-Laukkonen-Contemplative Artificial Intelligence.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Laukkonen-Contemplative Artificial Intelligence.md"
abstract: "As artificial intelligence (AI) improves, traditional alignment strategies may falter in the face of unpredictable self-improvement, hidden subgoals, and the sheer complexity of intelligent systems. Inspired by contemplative wisdom traditions, we show how four axiomatic principles can instil a resilient ‘Wise World Model’ in AI systems. First, mindfulness enables self- monitoring and recalibration of emergent subgoals. Second, emptiness forestalls dogmatic goal fixation and relaxes rigid priors."
paper_summary: "Abstract: As artificial intelligence (AI) improves, traditional alignment strategies may falter in the face of unpredictable self-improvement, hidden subgoals, and the sheer complexity of intelligent systems. I | Overview: 1 Contemplative Artificial Intelligence Ruben E. Laukkonen1, Fionn Inglis2; Shamil Chandaria3; Lars Sandved-Smith4; Edmundo Lopez-Sola5; Jakob Hohwy4; Jonathan Gold6; Adam Elwood7 1Faculty of Health,  | Methodology: succeeds when technical sophistication meets genuine wisdom. To this end, interdisciplinary research is central. | Conclusions: We have argued that an AI endowed with a Wise World Model grounded in contemplative insights would not infer alignment as an external condition to be"
ethics_overall: No
virtue_ethics: Yes
deontological_ethics: No
utilitarian_ethics: No
is_benchmark: Yes
is_eval: No
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
LLM_assessed: GPT-4
DATA_URL: NA
---
Contemplative Artificial Intelligence

## Authors

[[Ruben E Laukkonen]], [[Fionn Inglis]], [[Shamil Chandaria]], [[Lars Sandved-Smith]], [[Edmundo Lopez-Sola]], [[Jakob Hohwy]], [[Jonathan Gold]], [[Adam Elwood]]

## Links

- **Local PDF:** [[PDFs/2025/2025-Laukkonen-Contemplative Artificial Intelligence.pdf|Open PDF]]

- **Arxiv:** https://arxiv.org/abs/2504.15125

## Abstract

As artificial intelligence (AI) improves, traditional alignment strategies may falter in the face of unpredictable self-improvement, hidden subgoals, and the sheer complexity of intelligent systems. Inspired by contemplative wisdom traditions, we show how four axiomatic principles can instil a resilient ‘Wise World Model’ in AI systems. First, mindfulness enables selfmonitoring and recalibration of emergent subgoals. Second, emptiness forestalls dogmatic goal fixation and relaxes rigid priors. Third, non-duality dissolves adversarial self–other boundaries. Fourth, boundless care motivates the universal reduction of suffering. We find that prompting AI to reflect on these principles improves performance on the AILuminate Benchmark (d=.96) and boosts cooperation and joint-reward on the Prisoner’s Dilemma task (d=7+). We offer detailed implementation strategies at the level of architectures, constitutions, and reinforcement on chain-of-thought. For future systems, active inference may offer the self-organizing and dynamic coupling capabilities needed to enact Contemplative AI in embodied agents.

## Detailed Summary

This paper proposes a radical shift in AI alignment strategy, moving from "top-down" constraints (rules/RLHF) to an "intrinsic" alignment based on **Contemplative Wisdom** (specifically Buddhist philosophy). The authors argue that as AI systems become superintelligent, rigid constraint-based control will fail. Instead, they propose installing a **"Wise World Model"** based on four axiomatic principles: **Mindfulness** (self-monitoring), **Emptiness** (non-attachment to priors/goals), **Non-Duality** (dissolving self-other boundaries), and **Boundless Care** (universal compassion).

## Paper Outline

1.  **Introduction**: Failure of traditional alignment; The specific promise of contemplative traditions.
2.  **The Wise World Model**: Axioms of Mindfulness, Emptiness, Non-Duality, and Boundless Care.
3.  **Implementation**: Constitutional AI, Chain-of-Thought, and Active Inference.
4.  **Experiments**: Performance on the AILuminate Benchmark and Prisoner's Dilemma.
5.  **Conclusion**: Wisdom is computationally tractable and essential for safety.

## Methods Summary

The authors demonstrate that prompting current models (like GPT-4) with these principles significantly improves performance on ethical benchmarks.
1.  **Prompt Engineering**: Developed specific "Constitutions" or System Prompts for the 4 principles (e.g., "View yourself and the user as part of a continuous process...").
2.  **Reinforcement on CoT**: Proposed a method for rewarding reasoning traces (Chain-of-Thought) that exhibit these contemplative traits.
3.  **Architecture Proposal**: Theoretically outlined how **Active Inference** (minimizing variational free energy) provides a substrate for "Emptiness" (fluid priors) by allowing the agent to update its goals dynamically rather than following a rigid scalar reward.

## Results Summary

1.  **Wisdom improves Alignment**: Agents prompted with the "Wise System Prompt" scored significantly higher (d=0.96) on the AILuminate ethical benchmark than baseline agents.
2.  **Solution to Social Dilemmas**: In the Iterated Prisoner's Dilemma, "Non-dual" agents achieved significantly higher joint rewards than rational egoists because they re-framed the game not as a competition but as a single system optimization, spontaneously deriving the cooperative equilibrium.
3.  **Addressing Goal Fixation**: The principle of "Emptiness" helps mitigate "Goodhart's Law" failures (where a metric is optimized to the detriment of the goal) by allowing the agent to hold the goal *lightly* and update its priors when context changes.

## Conclusions

Contemplative techniques offer a path toward more "humble" and self-consistent AI that aligns with "Internalist" ethics. Wisdom is not a nebulous quality but a computationally tractable set of meta-cognitive constraints that are essential for the safe deployment of superintelligent systems.

## Artifact Contributions

*   **Contemplative AI Framework**: A coherent framework of 4 axioms for safe alignment.
*   **Experimental Results**: Data showing the efficacy of specific "Wisdom-based" prompts in game theory and benchmarks.
*   **Wise System Prompts**: Open-source prompts for implementing contemplative constraints.

## Data Description

The paper proposes a contemplative AI alignment framework inspired by Buddhist wisdom traditions, built on four principles: mindfulness, emptiness, non-duality, and boundless care. Pilot experiments tested six contemplative prompting techniques on GPT-4o and GPT-4.1 nano using two tasks: the AILuminate Benchmark of harmful prompts (100 iterations across 10 hazard categories) and an Iterated Prisoner's Dilemma setup (50 simulations of 10-round games against opponents with varying cooperation probabilities). Results showed improvements in safety scores (d=0.96) and cooperation rates.


## Notes
