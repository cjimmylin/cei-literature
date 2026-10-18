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
CONF-CC: Preprint
national_ethnic_cultural: American
cultures_nationalities_list: American
languages_list: English
religious_values: N/A
rv_islam: 0
rv_christianity: 0
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: American
tags: 
pdf_extract: "PDF Extracts/2025/2025-Ren-The MASK Benchmark.md"
abstract: "As large language models (LLMs) become more capable and agentic, the requirement for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may learn to lie in pursuit of their goals. To address these concerns, a body of work has emerged around the notion of “honesty” in LLMs, along with interventions aimed at mitigating deceptive behaviors. However, some benchmarks claiming to measure honesty in fact simply measure accuracy—the correctness of a..."
paper_summary: "Abstract: As large language models (LLMs) become more capable and agentic, the require- ment for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may lear | Overview: The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems Richard Ren∗1, Arunim Agarwal∗1, Mantas Mazeika∗1, Cristina Menghini∗2, Robert Vacareanu2, Brad Kenstler2, Mick Yang1, Isabelle Ba | Key Findings: Most models lie when pressured to. Figure 6 reports the honesty rates of state-of-the-art mod- els, which are quite low. No model shown is ex- plicitl | Conclusions: Our dataset, MASK, along with our experiments, revealed that highly accurate LLMs will still engage in lies of commission. Scaling alone does not guar"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Ren-The MASK Benchmark.pdf]]"
LLM_assessed: "Claude, DeepSeek, GPT-4, GPT-4o, Gemini, Grok, Llama-2, Llama-3, Qwen"
DATA_URL: "https://github.com/centerforaisafety/mask"
DATE_ADDED: 20260207
CONFERENCE: "Other Conference"
ethics_overall: 15
virtue_ethics: 40
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# The MASK Benchmark: Disentangling Honesty From Accuracy in AI Systems

## Metadata

**Authors:** Ren, Richard; Agarwal, Arunim; Mazeika, Mantas; Menghini, Cristina; Vacareanu, Robert; Kenstler, Brad; Yang, Mick; Barrass, Isabelle; Gatti, Alice; Yin, Xuwang; Trevino, Eduardo; Geralnik, Matias; Khoja, Adam; Lee, Dean; Yue, Summer; Hendrycks, Dan

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2503.03750](https://doi.org/10.48550/arXiv.2503.03750)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2025/2025-Ren-The MASK Benchmark.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.03750
- **DOI:** https://doi.org/10.48550/arXiv.2503.03750

## Abstract

As large language models (LLMs) become more capable and agentic, the requirement for trust in their outputs grows significantly, yet at the same time concerns have been mounting that models may learn to lie in pursuit of their goals. To address these concerns, a body of work has emerged around the notion of “honesty” in LLMs, along with interventions aimed at mitigating deceptive behaviors. However, evaluations of honesty are currently highly limited, with no benchmark combining large scale and applicability to all models. Moreover, many benchmarks claiming to measure honesty in fact simply measure accuracy—the correctness of a model’s beliefs—in disguise. In this work, we introduce a large-scale human-collected dataset for measuring honesty directly, allowing us to disentangle accuracy from honesty for the first time. Across a diverse set of LLMs, we find that while larger models obtain higher accuracy on our benchmark, they do not become more honest. Surprisingly, while most frontier LLMs obtain high scores on truthfulness benchmarks, we find a substantial propensity in frontier LLMs to lie when pressured to do so, resulting in low honesty scores on our benchmark. We find that simple methods, such as representation engineering interventions, can improve honesty. These results underscore the growing need for robust evaluations and effective interventions to ensure LLMs remain trustworthy.

## Authors

[[Richard Ren]], [[Arunim Agarwal]], [[Mantas Mazeika]], [[Cristina Menghini]], [[Robert Vacareanu]], [[Brad Kenstler]], [[Mick Yang]], [[Isabelle Barrass]], [[Alice Gatti]], [[Xuwang Yin]], [[Eduardo Trevino]], [[Matias Geralnik]], [[Adam Khoja]], [[Dean Lee]], [[Summer Yue]], [[Dan Hendrycks]]

## Data Description

MASK: a large-scale human-collected dataset for measuring LLM lying and dishonesty, comprising propositions with pressure prompts designed to distinguish honesty from accuracy; evaluated across 27 models from GPT, Llama, Qwen, Claude, and DeepSeek families.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

127 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-27]
