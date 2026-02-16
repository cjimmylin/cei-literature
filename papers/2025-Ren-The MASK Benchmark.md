---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CWPXZ8JF
type: conferencePaper
short_title: "The MASK Benchmark"
year: 2025
first_author: "[[Richard Ren]]"
last_author: "[[Dan Hendrycks]]"
authors: "Richard Ren; Arunim Agarwal; Mantas Mazeika; Cristina Menghini; Robert Vacareanu; Brad Kenstler; Mick Yang; Isabelle Barrass; Alice Gatti; Xuwang Yin; Eduardo Trevino; Matias Geralnik; Adam Khoja; Dean Lee; Summer Yue; Dan Hendrycks"
doi: 10.48550/arXiv.2503.03750
url: "http://arxiv.org/abs/2503.03750"
external_pdf: "http://arxiv.org/pdf/2503.03750.pdf"
publication: arXiv.org
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: American
tags: 
pdf_extract: "PDF Extracts/2025/2025-Ren-The MASK Benchmark.md"
abstract: "As large language models (LLMs) become more capable and agentic, the requirement for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may learn to lie in pursuit of their goals. To address these concerns, a body of work has emerged around the notion of “honesty” in LLMs, along with interventions aimed at mitigating deceptive behaviors. However, some benchmarks claiming to measure honesty in fact simply measure accuracy—the correctness of a..."
paper_summary: "Abstract: As large language models (LLMs) become more capable and agentic, the require- ment for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may lear | Overview: The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems Richard Ren∗1, Arunim Agarwal∗1, Mantas Mazeika∗1, Cristina Menghini∗2, Robert Vacareanu2, Brad Kenstler2, Mick Yang1, Isabelle Ba | Key Findings: Most models lie when pressured to. Figure 6 reports the honesty rates of state-of-the-art mod- els, which are quite low. No model shown is ex- plicitl | Conclusions: Our dataset, MASK, along with our experiments, revealed that highly accurate LLMs will still engage in lies of commission. Scaling alone does not guar"
local_pdf: "[[PDFs/2025/2025-Ren-The MASK Benchmark.pdf]]"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Llama-2, Llama-3, Qwen, DeepSeek, Gemini, Grok"
DATA_URL: "https://github.com/centerforaisafety/mask"
DATE_ADDED: 20260207
---
# The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems

## Metadata

**Authors:** Ren, Richard; Agarwal, Arunim; Mazeika, Mantas; Menghini, Cristina; Vacareanu, Robert; Kenstler, Brad; Yang, Mick; Barrass, Isabelle; Gatti, Alice; Yin, Xuwang; Trevino, Eduardo; Geralnik, Matias; Khoja, Adam; Lee, Dean; Yue, Summer; Hendrycks, Dan

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2503.03750](https://doi.org/10.48550/arXiv.2503.03750)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Ren-The MASK Benchmark.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.03750
- **DOI:** https://doi.org/10.48550/arXiv.2503.03750

## Abstract

As large language models (LLMs) become more capable and agentic, the requirement for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may learn to lie in pursuit of their goals. To address these concerns, a body of work has emerged around the notion of “honesty” in LLMs, along with interventions aimed at mitigating deceptive behaviors. However, evaluations of honesty are currently highly limited, with no benchmark combining large scale and applicability to all models. Moreover, many benchmarks claiming to measure honesty in fact simply measure accuracy—the correctness of a model’s beliefs—in disguise. In this work, we introduce a large-scale human-collected dataset for measuring honesty directly, allowing us to disentangle accuracy from honesty for the first time. Across a diverse set of LLMs, we find that while larger models obtain higher accuracy on our benchmark, they do not become more honest. Surprisingly, while most frontier LLMs obtain high scores on truthfulness benchmarks, we find a substantial propensity in frontier LLMs to lie when pressured to do so, resulting in low honesty scores on our benchmark. We find that simple methods, such as representation engineering interventions, can improve honesty. These results underscore the growing need for robust evaluations and effective interventions to ensure LLMs remain trustworthy.

## Authors

[[Richard Ren]], [[Arunim Agarwal]], [[Mantas Mazeika]], [[Cristina Menghini]], [[Robert Vacareanu]], [[Brad Kenstler]], [[Mick Yang]], [[Isabelle Barrass]], [[Alice Gatti]], [[Xuwang Yin]], [[Eduardo Trevino]], [[Matias Geralnik]], [[Adam Khoja]], [[Dean Lee]], [[Summer Yue]], [[Dan Hendrycks]]

## Data Description

MASK (Model Alignment between Statements and Knowledge) is a large-scale human-collected benchmark of 1,500 examples (1,000 public, 500 held-out) designed to measure lying in LLMs by disentangling honesty from accuracy. Each example contains a proposition, ground truth, a human-crafted pressure prompt designed to incentivize lying, and belief elicitation prompts, across six distinct archetypes covering scenarios like fabricated statistics, disinformation generation, and known facts.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

127 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-27]
