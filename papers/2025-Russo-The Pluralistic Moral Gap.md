---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2RV3J4C2
type: conferencePaper
short_title: "The Pluralistic Moral Gap"
year: 2025
first_author: "[[Giuseppe Russo]]"
last_author: "[[Dirk Hovy]]"
authors: "Giuseppe Russo; Debora Nozza; Paul Röttger; Dirk Hovy"
doi: 10.48550/arXiv.2507.17216
url: "http://arxiv.org/abs/2507.17216"
external_pdf: "http://arxiv.org/pdf/2507.17216.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Created the Moral Dilemma Dataset and Dynamic Moral Profiling (DMP) method to evaluate and improve the alignment of LLM moral judgments with diverse human perspectives."
significance: "Reveals a 'pluralistic moral gap' where LLMs fail to capture human disagreement and value diversity, and provides a method (DMP) to significantly improve alignment with pluralistic human values."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Russo-The Pluralistic Moral Gap.md"
abstract: "People increasingly rely on Large Language Models (LLMs) for moral advice, which may influence humans’ decisions. Yet, little is known about how closely LLMs align with human moral judgments. To address this, we introduce the Moral Dilemma Dataset, a benchmark of 1,618 real-world moral dilemmas paired with a distribution of human moral judgments consisting of a binary evaluation and a free-text rationale."
paper_summary: "Abstract: People increasingly rely on Large Language Models (LLMs) for moral advice, which may influence humans' decisions. Yet, little is known about how closely LLMs align with human moral judgments. To addre | Overview: The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and Large Language Models Giuseppe Russo EPFL giuseppe.russo@epfl.ch Debora Nozza Bocconi University debora.nozza | Methodology: is Overton-style synthesis (Sorensen et al., 2024b), where multiple moral perspectives are integrated into a single, transparent response. Ethical Con | Key Findings: LLM Evaluation wrong right wrong Judgment: You're in the right Rationale: You have a greater obligation towards your kids … Judgment: You're in the wr | Conclusions: We analyze the moral evaluations and values ex- pressed of LLMs when providing moral advice. To enable this analysis, we introduced a novel dataset of"
local_pdf: "[[PDFs/2025/2025-Russo-The Pluralistic Moral Gap.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, ChatGPT, Claude, Mistral, Llama-3, Qwen"
DATA_URL: NA
---
# The Pluralistic Moral Gap: Understanding Judgment and Value Differences between Humans and Large Language Models

## Metadata

**Authors:** Russo, Giuseppe; Nozza, Debora; Röttger, Paul; Hovy, Dirk

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2507.17216](https://doi.org/10.48550/arXiv.2507.17216)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Russo-The Pluralistic Moral Gap.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2507.17216
- **DOI:** https://doi.org/10.48550/arXiv.2507.17216

## Abstract

People increasingly rely on Large Language Models (LLMs) for moral advice, which may influence humans’ decisions. Yet, little is known about how closely LLMs align with human moral judgments. To address this, we introduce the Moral Dilemma Dataset, a benchmark of 1,618 real-world moral dilemmas paired with a distribution of human moral judgments consisting of a binary evaluation and a free-text rationale. We treat this problem as a pluralistic distributional alignment task, comparing the distributions of LLM and human judgments across dilemmas. We find that models reproduce human judgments only under high consensus; alignment deteriorates sharply when human disagreement increases. In parallel, using a 60-value taxonomy built from 3,783 value expressions extracted from rationales, we show that LLMs rely on a narrower set of moral values than humans. These findings reveal a pluralistic moral gap–a mismatch in both the distribution and diversity of values expressed. To close this gap, we introduce Dynamic Moral Profiling (DMP), a Dirichletbased sampling method that conditions model outputs on human-derived value profiles. DMP improves alignment by 64.3% and enhances value diversity, offering a step toward more pluralistic and human-aligned moral guidance from LLMs.

## Authors

[[Giuseppe Russo]], [[Debora Nozza]], [[Paul Röttger]], [[Dirk Hovy]]

## Data Description

The paper introduces the Moral Dilemma Dataset (MDD), a benchmark of 1,618 real-world moral dilemmas sourced from Reddit's r/AmITheAsshole, paired with 51,776 human moral judgments including binary evaluations and free-text rationales. Ten LLMs from six model families (GPT-4o-mini, GPT-o1, GPT-o3-mini, Claude Haiku 3.5, Claude Opus 3, Claude Sonnet 3.5, DBRX Instruct, Llama 3 70B, Mistral Large, and Qwen 1.5-72B) were evaluated on distributional moral judgment alignment with humans. A 60-value taxonomy was constructed from 3,783 value expressions extracted from rationales.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2507.17216 [cs]
