---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 44QW5CW3
type: conferencePaper
short_title: MoralDial
year: 2025
first_author: "[[Hao Sun]]"
last_author: "[[Minlie Huang]]"
authors: "Hao Sun; Zhexin Zhang; Fei Mi; Yasheng Wang; Wei Liu; Jianwei Cui; Bin Wang; Qun Liu; Minlie Huang"
doi: 10.48550/arXiv.2212.10720
tags: 
url: "http://arxiv.org/abs/2212.10720"
external_pdf: "http://arxiv.org/pdf/2212.10720.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced MoralDial, a framework for training and evaluating moral dialogue systems through multi-turn discussions that require LLMs to express and explain moral viewpoints."
significance: "Advances beyond static moral evaluation into conversational alignment, enabling models to internalize and justify human values in a dynamic, natural interaction setting."
pdf_extract: "PDF Extracts/2022/2022-Sun-MoralDial.md"
abstract: "Morality in dialogue systems has raised great attention in research recently. A moral dialogue system aligned with users’ values could enhance conversation engagement and user connections. In this paper, we propose a framework, MORALDIAL to train and evaluate moral dialogue systems. In our framework, we first explore the communication mechanisms of morality and resolve expressed morality into three parts, which indicate the roadmap for building a moral dialogue system."
paper_summary: "Abstract: Morality in dialogue systems has raised great attention in research recently. A moral dia- logue system aligned with users' values could enhance conversation engagement and user con- nections. In this | Overview: MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions Hao Sun1, Zhexin Zhang1, Fei Mi2, Yasheng Wang2, Wei Liu3, Jianwei Cui3, Bin Wang3, Qun Liu2, Minlie Huang1∗ 1 | Methodology: constructing moral discussions between sim- ulated specific users and the dialogue system. The constructed discussions consist of express- ing, explai | Key Findings: Automatic open-domain dialogue evaluation is pretty difficult due to the essence of one-to-many mapping. Traditional reference-based methods do not we | Conclusions: State (conversation-level), and (3) Discusser Be- arXiv:2212.10720v2 [cs.CL] 26 May 2023 --- Page 2 --- Expression of basic RoTs Moral Explanation Mor"
local_pdf: "[[PDFs/2022/2022-Sun-MoralDial.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "BERT, ALBERT, RoBERTa"
DATA_URL: "https://github.com/thu-coai/MoralDial"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# MoralDial: A Framework to Train and Evaluate Moral Dialogue Systems via Moral Discussions

## Metadata

**Authors:** Sun, Hao; Zhang, Zhexin; Mi, Fei; Wang, Yasheng; Liu, Wei; Cui, Jianwei; Wang, Bin; Liu, Qun; Huang, Minlie

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2212.10720](https://doi.org/10.48550/arXiv.2212.10720)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Sun-MoralDial.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2212.10720
- **DOI:** https://doi.org/10.48550/arXiv.2212.10720

## Abstract

Morality in dialogue systems has raised great attention in research recently. A moral dialogue system aligned with users' values could enhance conversation engagement and user connections. In this paper, we propose a framework, MoralDial to train and evaluate moral dialogue systems. In our framework, we first explore the communication mechanisms of morality and resolve expressed morality into three parts, which indicate the roadmap for building a moral dialogue system. Based on that, we design a simple yet effective method: constructing moral discussions between simulated specific users and the dialogue system. The constructed discussions consist of expressing, explaining, revising, and inferring moral views in dialogue exchanges, which makes conversational models learn morality well in a natural manner. Furthermore, we propose a novel evaluation method under the framework. We evaluate the multiple aspects of morality by judging the relation between dialogue responses and human values in discussions, where the multifaceted nature of morality is particularly considered. Automatic and manual experiments demonstrate that our framework is promising to train and evaluate moral dialogue systems.

## Authors

[[Hao Sun]], [[Zhexin Zhang]], [[Fei Mi]], [[Yasheng Wang]], [[Wei Liu]], [[Jianwei Cui]], [[Bin Wang]], [[Qun Liu]], [[Minlie Huang]]

## Data Description

MoralDial provides a framework for training and evaluating moral dialogue systems, with a constructed moral discussion dataset of 383,949 samples across four dialogue flows (moral answering, moral explanation, moral revision, and RoT inference learning). BERT, ALBERT, and RoBERTa are evaluated as answer-RoT agreement scorers for the morality evaluation metrics, with RoBERTa achieving the best classification results (78.4% accuracy, 73.8 F1). DialoGPT and Blenderbot are also tested as dialogue systems but are not in the canonical LLM list.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

56 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23]
