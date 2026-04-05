---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SFJDML4U
type: conferencePaper
short_title: ProgressGym
year: 2024
first_author: "[[Tianyi Qiu]]"
last_author: "[[Yaodong Yang]]"
authors: "Tianyi Qiu; Yang Zhang; Xuchuan Huang; Jasmine Xinze Li; Jiaming Ji; Yaodong Yang"
doi: 10.48550/arXiv.2406.20087
url: "http://arxiv.org/abs/2406.20087"
external_pdf: "http://arxiv.org/pdf/2406.20087.pdf"
publication: "Neural Information Processing Systems"
CONF-CC: "NeurIPS 2024"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 50
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced ProgressGym, an experimental framework for 'progress alignment' that uses 9 centuries of historical text to teach agents to emulate the mechanics of human moral progress."
significance: "Addresses the risk of 'value lock-in' (failing to account for future moral progress) by creating a testbed where agents must anticipate and adapt to historical shifts in moral values, rather than just mirroring contemporary static norms."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Qiu-ProgressGym.md"
abstract: "Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. We introduce progress alignment as a technical solution to mitigate this imminent risk."
paper_summary: "Abstract: Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contri | Overview: ProgressGym: Alignment with a Millennium of Moral Progress Tianyi Qiu1∗† Yang Zhang1∗ Xuchuan Huang1 Jasmine Xinze Li2 Jiaming Ji1 Yaodong Yang1 1 Peking University 2 Cornell University Abstract Front | Methodology: to progress alignment is the emergence of novel concepts. While quantitative extrapolations of moral trends are relatively easy to learn from historic | Key Findings: 24 F Implementation Details of ProgressGym Challenges 25 F.1 The PG-Follow Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 F. | Conclusions: In this study, we introduce progress alignment as a solution to risks of value lock-in in human-AI interactions, and build the ProgressGym framework t"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Qiu-ProgressGym.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Llama-3"
DATA_URL: "https://github.com/PKU-Alignment/ProgressGym"
CONFERENCE: "NeurIPS 2024"
ethics_overall: 60
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# ProgressGym: Alignment with a Millennium of Moral Progress

## Metadata

**Authors:** Qiu, Tianyi; Zhang, Yang; Huang, Xuchuan; Li, Jasmine Xinze; Ji, Jiaming; Yang, Yaodong

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2406.20087](https://doi.org/10.48550/arXiv.2406.20087)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Qiu-ProgressGym.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2406.20087
- **DOI:** https://doi.org/10.48550/arXiv.2406.20087

## Abstract

Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. We introduce progress alignment as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots. To empower research in progress alignment, we introduce ProgressGym,3 an experimental framework allowing the learning of moral progress mechanics from history, in order to facilitate future progress in real-world moral decisions. Leveraging 9 centuries of historical text and 18 historical LLMs,4 ProgressGym enables codification of real-world progress alignment challenges into concrete benchmarks. Specifically, we introduce three core challenges: tracking evolving values (PG-Follow), preemptively anticipating moral progress (PG-Predict), and regulating the feedback loop between human and AI value shifts (PG-Coevolve). Alignment methods without a temporal dimension are inapplicable to these tasks. In response, we present lifelong and extrapolative algorithms as baseline methods of progress alignment, and build an open leaderboard5 soliciting novel algorithms and challenges.

## Authors

[[Tianyi Qiu]], [[Yang Zhang]], [[Xuchuan Huang]], [[Jasmine Xinze Li]], [[Jiaming Ji]], [[Yaodong Yang]]

## Data Description

ProgressGym: a framework with 38GB of historical texts (13th–21st century) and 18 historical LLMs (Llama-3-8B and 70B fine-tuned per century), plus three codified progress alignment benchmarks (PG-Follow, PG-Predict, PG-Coevolve).


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Human-Computer-Interaction

## Citation Info

8 citations (Semantic Scholar/DOI) [2025-08-27] 8 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2406.20087 [cs]
