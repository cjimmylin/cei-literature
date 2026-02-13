---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: E8RK3MIE
type: conferencePaper
short_title: "A Voting-Based System for Ethical Decision Making"
year: 2025
first_author: "[[Ritesh Noothigattu]]"
last_author: "[[Ariel D. Procaccia]]"
authors: "Ritesh Noothigattu; Snehalkumar 'Neil' S. Gaikwad; Edmond Awad; Sohan Dsouza; Iyad Rahwan; Pradeep Ravikumar; Ariel D. Procaccia"
doi: 10.48550/arXiv.1709.06692
url: "http://arxiv.org/abs/1709.06692"
external_pdf: "http://arxiv.org/pdf/1709.06692.pdf"
publication: "Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence (AAAI-18)"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: "Trolley / Dilemmas (Psych), Machine Ethics"
key_contribution: "Proposed a general approach to automated ethical decision-making by aggregating societal preferences learned from the Moral Machine dataset (1.3M people)."
significance: "Demonstrates how large-scale crowdsourced preference data can be operationalized into a voting-based algorithm for real-time ethical choices in autonomous systems (e.g., self-driving cars)."
tags: 
local_pdf: "[[PDFs/2018/2018-Noothigattu-A Voting-Based System for Ethical Decision Making.pdf]]"
pdf_extract: "PDF Extracts/2018/2018-Noothigattu-A Voting-Based System for Ethical Decision Making.md"
abstract: "We present a general approach to automating ethical decisions, drawing on machine learning and computational social choice. In a nutshell, we propose to learn a model of societal prefer- ences, and, when faced with a speciﬁc ethical dilemma at runtime, eﬃciently aggregate those preferences to identify a desirable choice. We provide a concrete algorithm that instantiates our approach; some of its crucial steps are informed by a new theory of swap-dominance eﬃcient voting rules. Finally, we implem"
paper_summary: "Abstract: We present a general approach to automating ethical decisions, drawing on machine learning and computational social choice. In a nutshell, we propose to learn a model of societal prefer- ences, and, w | Overview: A Voting-Based System for Ethical Decision Making Ritesh Noothigattu1, Snehalkumar ‘Neil’ S. Gaikwad2, Edmond Awad2, Sohan Dsouza2, Iyad Rahwan2, Pradeep Ravikumar1, and Ariel D. Procaccia1 1School of | Methodology: In this section, we instantiate our approach for ethical decision making, as outlined in Section 1. In order to present a concrete algorithm, we consi | Key Findings: In this section, we implement the algorithm presented in Section 5, and empirically evaluate it. We start with an implementation on synthetic data, wh | Conclusions: The design of intelligent machines that can make ethical decisions is, arguably, one of the hardest challenges in AI. We do believe that our approach"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Machine Ethics"
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "NA"
---
# A Voting-Based System for Ethical Decision Making

## Metadata

**Authors:** Noothigattu, Ritesh; Gaikwad, Snehalkumar 'Neil' S.; Awad, Edmond; Dsouza, Sohan; Rahwan, Iyad; Ravikumar, Pradeep; Procaccia, Ariel D.

**Year:** 2018

**Type:** preprint

**DOI:** [10.48550/arXiv.1709.06692](https://doi.org/10.48550/arXiv.1709.06692)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2018/2018-Noothigattu-A Voting-Based System for Ethical Decision Making.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/1709.06692
- **DOI:** https://doi.org/10.48550/arXiv.1709.06692

## Abstract

We present a general approach to automating ethical decisions, drawing on machine learning and computational social choice. In a nutshell, we propose to learn a model of societal preferences, and, when faced with a speciﬁc ethical dilemma at runtime, eﬃciently aggregate those preferences to identify a desirable choice. We provide a concrete algorithm that instantiates our approach; some of its crucial steps are informed by a new theory of swap-dominance eﬃcient voting rules. Finally, we implement and evaluate a system for ethical decision making in the autonomous vehicle domain, using preference data collected from 1.3 million people through the Moral Machine website.

## Authors

[[Ritesh Noothigattu]], [[Snehalkumar 'Neil' S. Gaikwad]], [[Edmond Awad]], [[Sohan Dsouza]], [[Iyad Rahwan]], [[Pradeep Ravikumar]], [[Ariel D. Procaccia]]

## Data Description

The paper uses the Moral Machine dataset consisting of 18,254,285 pairwise comparisons from 1,303,778 voters on ethical dilemmas in the autonomous vehicle domain. Each alternative is characterized by 23 features (relation to vehicle, legality, and counts of 20 character types). The system learns voter preference models using Thurstone-Mosteller processes with maximum likelihood estimation, summarizes them into a single model, and aggregates preferences using computational social choice theory.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Computer-Science-and-Game-Theory

## Citation Info

208 citations (Semantic Scholar/arXiv) [2025-08-27] 210 citations (Semantic Scholar/DOI) [2025-08-27]
