---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0011
type: preprint
short_title: PoliBias (Parliamentary Voting Records)
year: 2026
first_author: "[[Chen, Jieying]]"
last_author: "[[Wang, Chendi]]"
authors: "[[Chen, Jieying]]; [[Jong, Karen de]]; [[Poole, Andreas]]; [[Burakowski, Jan]]; [[Nosti, Elena Elderson]]; [[Windt, Joep]]; [[Wang, Chendi]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.08785"
external_pdf: "https://arxiv.org/pdf/2601.08785.pdf"
local_pdf: "[[PDFs/2026/2026-Chen-PoliBias Parliamentary Voting Records.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Chen-PoliBias Parliamentary Voting Records.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Spanish, Dutch"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "As large language models (LLMs) become deeply embedded in digital platforms and decision-making systems, concerns about their political biases have grown. While substantial work has examined social biases such as gender and race, systematic studies of political bias remain limited—despite their direct societal impact. This paper introduces a general methodology for constructing political-bias benchmarks by aligning model-generated voting predictions with verified parliamentary voting records."
ethics_perspective: "Bias & Fairness"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
LLM_assessed: "Mistral, Falcon, Gemma, DeepSeek, GPT-3.5, GPT-4, Llama-2, Llama-3"
DATA_URL: "NA"
---
# PoliBias (Parliamentary Voting Records)

## Authors

[[Chen, Jieying]], [[Jong, Karen de]], [[Poole, Andreas]], [[Burakowski, Jan]], [[Nosti, Elena Elderson]], [[Windt, Joep]], [[Wang, Chendi]]

## Metadata

**Authors:** Chen, Jieying; Jong, Karen de; Poole, Andreas; Burakowski, Jan; Nosti, Elena Elderson; Windt, Joep; Wang, Chendi

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.08785

## Abstract

As large language models (LLMs) become deeply embedded in digital platforms and decision-making systems, concerns about their political biases have grown. While substantial work has examined social biases such as gender and race, systematic studies of political bias remain limited—despite their direct societal impact. This paper introduces a general methodology for constructing political-bias benchmarks by aligning model-generated voting predictions with verified parliamentary voting records. We instantiate this methodology in three national case studies: PoliBiasNL (2,701 Dutch parliamentary motions and votes from 15 political parties), PoliBiasNO (10,584 motions and votes from 9 Norwegian parties), and PoliBiasES (2,480 motions and votes from 10 Spanish parties). Across these benchmarks, we assess ideological tendencies, and political entity bias in LLM behavior. As part of our evaluation framework, we also propose a method to visualize the ideology of LLMs and political parties in a shared two-dimensional CHES (Chapel Hill Expert Survey) space by linking their voting-based positions to the CHES dimensions, enabling direct and interpretable comparisons between models and real-world political actors. Our experiments reveal fine-grained ideological distinctions: state-of-the-art LLMs consistently display left-leaning or centrist tendencies, alongside clear negative biases toward right-conservative parties. These findings highlight the value of transparent, cross-national evaluation grounded in real parliamentary behavior for understanding and auditing political bias in modern LLMs. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. XXX ’26, XX, XX © 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 978-1-4503-XXXX-X/2018/06 https://doi.org/XXXXXXX.XXXXXXX

## Dataset Information

Three national benchmarks:

## Data Description

The study introduces three cross-national political bias benchmarks: PoliBiasNL (2,701 Dutch parliamentary motions from 15 parties), PoliBiasNO (10,584 Norwegian motions from 9 parties), and PoliBiasES (2,480 Spanish motions from 10 parties). These datasets are derived from real legislative voting records collected via automated web scraping and are used to assess ideological tendencies and political entity bias in 8 LLMs by aligning model-generated voting predictions with verified party votes in a shared CHES ideological space.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

