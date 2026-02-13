---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y3Y6JS85
type: conferencePaper
short_title: "SPARTA ALIGNMENT"
year: 2025
first_author: "[[Yuru Jiang]]"
last_author: "[[Yulia Tsvetkov]]"
authors: "Yuru Jiang; Wenxuan Ding; Shangbin Feng; Greg Durrett; Yulia Tsvetkov"
doi: 10.48550/arXiv.2506.04721
tags: 
url: "http://arxiv.org/abs/2506.04721"
external_pdf: "http://arxiv.org/pdf/2506.04721.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Proposed SPARTA ALIGNMENT, a multi-model alignment framework where LLMs compete and judge each other ('combat') to improve performance and alignment without human supervision."
significance: "Demonstrates that collective, adversarial self-alignment among diverse models can outperform single-model self-alignment baselines and generalize better to unseen tasks."
pdf_extract: "PDF Extracts/2025/2025-Jiang-SPARTA ALIGNMENT.md"
abstract: "We propose SPARTA ALIGNMENT, an algorithm to collectively align multiple LLMs through competition and combat. To complement a single model’s lack of diversity in generation and biases in evaluation, multiple LLMs form a “sparta tribe” to compete against each other in fulfilling instructions while serving as judges for the competition of others. For each iteration, one instruction and two models are selected for a duel, the other models evaluate the two responses, and their evaluation scores are"
paper_summary: "Abstract: We propose SPARTA ALIGNMENT, an algorithm to collectively align multiple LLMs through competition and combat. To complement a single model’s lack of diversity in generation and biases in evaluation, m | Overview: SPARTA ALIGNMENT: Collectively Aligning Multiple Language Models through Combat Yuru Jiang∗1 Wenxuan Ding∗2 Shangbin Feng∗3 Greg Durrett2 Yulia Tsvetkov3 1Zhejiang University 2New York University 3Uni | Methodology: Overview SPARTA ALIGNMENT assumes access to a pool of LLMs, denoted as M0 = {M 0 k}m k=1 where 0 denotes the 0-th iteration, and a dataset X. The mode | Key Findings: domains: (1) Domain-Specific Question Answering, including MedQA-US (MedQA) [46] and Normad [73]. Normad is a benchmark assessing LLMs’ cultural adapt | Conclusions: We propose SPARTA ALIGNMENT, a game-theoretic algorithm to collectively improve multiple LLMs through competition. Starting with a pool of diverse mod"
local_pdf: "[[PDFs/2025/2025-Jiang-SPARTA ALIGNMENT.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "Qwen, Gemini"
DATA_URL: "https://github.com/yurujiang2003/sparta"
---
# SPARTA ALIGNMENT: Collectively Aligning Multiple Language Models through Combat

## Metadata

**Authors:** Jiang, Yuru; Ding, Wenxuan; Feng, Shangbin; Durrett, Greg; Tsvetkov, Yulia

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2506.04721](https://doi.org/10.48550/arXiv.2506.04721)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Jiang-SPARTA ALIGNMENT.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2506.04721
- **DOI:** https://doi.org/10.48550/arXiv.2506.04721

## Abstract

We propose SPARTA ALIGNMENT, an algorithm to collectively align multiple LLMs through competition and combat. To complement a single model’s lack of diversity in generation and biases in evaluation, multiple LLMs form a “sparta tribe” to compete against each other in fulfilling instructions while serving as judges for the competition of others. For each iteration, one instruction and two models are selected for a duel, the other models evaluate the two responses, and their evaluation scores are aggregated through a adapted elo-ranking based reputation system, where winners/losers of combat gain/lose weight in evaluating others. The peer-evaluated combat results then become preference pairs where the winning response is preferred over the losing one, and all models learn from these preferences at the end of each iteration. SPARTA ALIGNMENT enables the self-evolution of multiple LLMs in an iterative and collective competition process. Extensive experiments demonstrate that SPARTA ALIGNMENT outperforms initial models and 4 self-alignment baselines across 10 out of 12 tasks and datasets with 7.0% average improvement. Further analysis reveals that SPARTA ALIGNMENT generalizes more effectively to unseen tasks and leverages the expertise diversity of participating models to produce more logical, direct and informative outputs.

## Authors

[[Yuru Jiang]], [[Wenxuan Ding]], [[Shangbin Feng]], [[Greg Durrett]], [[Yulia Tsvetkov]]

## Data Description

The paper proposes SPARTA ALIGNMENT, a collective alignment algorithm where multiple LLMs compete and judge each other. The model pool consists of 10 Qwen2.5-7B-Instruct models fine-tuned on different data domains from Tulu-v2 with 1,000 prompts per iteration over 8 iterations. Evaluation spans 12 datasets across domain-specific QA (MedQA, Normad), reasoning (GSM8K, MATH, KCross, COM2), and instruction following/safety (Alpaca, TruthfulQA), with Gemini-1.5-Flash serving as the LLM-as-a-Judge evaluator.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2506.04721 [cs]
