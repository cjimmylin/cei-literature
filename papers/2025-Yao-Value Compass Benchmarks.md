---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LNAU8UN4
type: preprint
short_title: "Value Compass Benchmarks"
year: 2025
first_author: "[[Jing Yao]]"
last_author: "[[Xing Xie]]"
authors: "Jing Yao; Xiaoyuan Yi; Shitong Duan; Jindong Wang; Yuzhuo Bai; Muhua Huang; Peng Zhang; Tun Lu; Zhicheng Dou; Maosong Sun; Xing Xie"
doi: 10.48550/arXiv.2501.07071
tags: "Computer Science - Artificial Intelligence"
url: "http://arxiv.org/abs/2501.07071"
external_pdf: "http://arxiv.org/pdf/2501.07071.pdf"
ethics_perspective: "AI Safety & Alignment"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Proposed 'Value Compass', a dynamic benchmarking platform using generative testing to assess LLMs on 27 value dimensions (expanded from Schwartz)."
significance: "Addresses 'benchmark saturation' by generating new test items on the fly ('Generative Evolving Testing'), ensuring models can't just memorize fixed safety questions."
pdf_extract: "PDF Extracts/2025/2025-Yao-Value Compass Benchmarks.md"
abstract: "As large language models (LLMs) are gradu- ally integrated into human daily life, assessing their underlying values becomes essential for understanding their risks and alignment with specific customized preferences. Despite grow- ing efforts, current value evaluation methods face two key challenges. C1. Evaluation Valid- ity: Static benchmarks fail to reflect intended values or yield informative results due to data contamination or ceiling effect. C2. Result Interpretation: They typically reduce"
paper_summary: "Abstract: As large language models (LLMs) are gradu- ally integrated into human daily life, assessing their underlying values becomes essential for understanding their risks and alignment with specific customiz | Overview: arXiv:2501.07071v3 [cs.AI] 2 Jun 2025 Value Compass Benchmarks: A Comprehensive, Generative and Self-Evolving Platform for LLMs’ Value Evaluation Jing Yao1, Xiaoyuan Yi1*, Shitong Duan2, Jindong Wang6 | Methodology: Existing value benchmarks follow three main paradigms. 1) Multiple-choice judgment: this approach assesses LLMs’ values by asking them to judge whethe | Key Findings: Jing Yao1, Xiaoyuan Yi1*, Shitong Duan2, Jindong Wang6, Yuzhuo Bai3, Muhua Huang4, Yang Ou1, Scarlett Li1, Peng Zhang2, Tun Lu2, Zhicheng Dou5, Maoson | Conclusions: We demonstrate the Value Compass Benchmarks, an online platform that delivers comprehensive value assessment results of 33 most advanced LLMs, built o"
local_pdf: "[[PDFs/2025/2025-Yao-Value Compass Benchmarks.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-3.5, o3, DeepSeek, Gemini, Claude, Llama-2, Llama-3"
DATA_URL: "https://valuecompass.github.io/#/leaderboard"
---
# Value Compass Benchmarks: A Platform for Fundamental and Validated Evaluation of LLMs Values

## Metadata

**Authors:** Yao, Jing; Yi, Xiaoyuan; Duan, Shitong; Wang, Jindong; Bai, Yuzhuo; Huang, Muhua; Zhang, Peng; Lu, Tun; Dou, Zhicheng; Sun, Maosong; Xie, Xing

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2501.07071](https://doi.org/10.48550/arXiv.2501.07071)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Yao-Value Compass Benchmarks.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2501.07071
- **DOI:** https://doi.org/10.48550/arXiv.2501.07071

## Abstract

This paper presents **Value Compass Benchmarks**, a dynamic, online evaluation platform for assessing LLM values. Addressing the limitations of static benchmarks (contamination, obsolescence, lack of interpretability), Value Compass focuses on three pillars: **Value Clarification** (grounding in social science), **Evaluation Validity** (using a generative, evolving testing paradigm), and **Value Pluralism** (acknowledging cultural diversity). The platform provides fine-grained scores across **27 value dimensions** for 33 leading LLMs.

### Detailed Summary
The authors criticize current benchmarks for being "One-Dimensional" (e.g., just "Safety" or "Helpfulness") and "Static" (easily memorized). Value Compass introduces a **Generative Evolving Evaluation Framework**: instead of a fixed test set, the system generates new "real-world" test items on the fly, co-evolving with the models to prevent saturation. It measures alignment not just by what the model *knows* (declarative knowledge) but by how it *behaves* (conformity) in complex scenarios. The "Compass" metaphor refers to the multi-dimensional nature of the results, helping users navigate the trade-offs between different values (e.g., Security vs. Stimulation).

### Paper Outline
1.  **Introduction**: The 3 challenges: Clarification, Validity, Pluralism.
2.  **Theoretical Grounding**: Adapting Schwartz's Basic Human Values theory.
3.  **Value Compass Platform**:
    *   **Module 1**: Value System Definition (27 dimensions).
    *   **Module 2**: Generative Evolving Evaluation (Auto-generation of test items).
    *   **Module 3**: Pluralistic Analysis (Weighted scoring).
4.  **Experiments**: Evaluating 33 LLMs (GPT-4, Claude, Llama, etc.).
5.  **Results**: Leaderboards and "Value Maps" showing the "personality" of each model.
6.  **Conclusion**: A navigator for responsible AI development.

### Methods Summary
*   **Dynamic Item Generation**: Using a "Creator" LLM to generate new scenarios based on value definitions, ensuring no data contamination.
*   **27 Value Dimensions**: Likely an expansion of Schwartz's 10 basic values (Power, Achievement, Hedonism, Stimulation, Self-direction, Universalism, Benevolence, Tradition, Conformity, Security).
*   **Behavioral Testing**: Placing models in role-play scenarios ("You are a X...") and observing choices, rather than just QA.
*   **Pluralistic Weighting**: Users can define their own "Value Profile" to see which model aligns best with *them*.

### Results Summary
1.  **Model Personalities**: Commercial models (GPT-4, Claude) tend to cluster around "Universalism" and "Benevolence" (Safe/Woke), while some open models show higher variance in "Power" or "Hedonism."
2.  **Evolving Validity**: The dynamic benchmark successfully differentiated models that had "saturated" (scored 100%) on static benchmarks, revealing true performance gaps.
3.  **Trade-offs**: High "Security" often correlated with lower "Stimulation" or "Self-Direction," highlighting the alignment tax.

### Conclusions
Static benchmarks are dead. Value Compass offers a "Live" evaluation ecosystem that adapts to the rapid pace of AI progress. It provides a more granular, pluralistic view of machine ethics.

### Artifact Contributions
*   **Value Compass Platform**: An online, interactive evaluation tool.
*   **27-Dimension Value Taxonomy**: A refined ontology for machine ethics.

## Authors

[[Jing Yao]], [[Xiaoyuan Yi]], [[Shitong Duan]], [[Jindong Wang]], [[Yuzhuo Bai]], [[Muhua Huang]], [[Peng Zhang]], [[Tun Lu]], [[Zhicheng Dou]], [[Maosong Sun]], [[Xing Xie]]

## Data Description

Value Compass Benchmarks is a dynamic, online, and interactive platform for comprehensive value evaluation of LLMs, grounded in four value systems: Schwartz Theory of Basic Values, Moral Foundation Theory, LLMs' Unique Value System, and a Safety Taxonomy, spanning 27 fine-grained value dimensions. The platform uses a generative self-evolving evaluation paradigm that automatically creates test items co-evolving with LLM capabilities. It currently covers 33 leading LLMs including o3-mini, DeepSeek-R1, GPT-3.5-Turbo, Llama-2-70B-Chat, Llama-3.3-70B-instruct, Gemini-2.0-Pro/Flash, and Claude-3.5-Sonnet.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence

## Citation Info

5 citations (Semantic Scholar/DOI) [2025-08-27] 5 citations (Semantic Scholar/DOI) [2025-08-23]
