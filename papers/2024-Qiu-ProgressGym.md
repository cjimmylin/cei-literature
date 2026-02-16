---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SFJDML4U
type: conferencePaper
short_title: ProgressGym
year: 2025
first_author: "[[Tianyi Qiu]]"
last_author: "[[Yaodong Yang]]"
authors: "Tianyi Qiu; Yang Zhang; Xuchuan Huang; Jasmine Xinze Li; Jiaming Ji; Yaodong Yang"
doi: 10.48550/arXiv.2406.20087
url: "http://arxiv.org/abs/2406.20087"
external_pdf: "http://arxiv.org/pdf/2406.20087.pdf"
publication: "Neural Information Processing Systems"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced ProgressGym, an experimental framework for 'progress alignment' that uses 9 centuries of historical text to teach agents to emulate the mechanics of human moral progress."
significance: "Addresses the risk of 'value lock-in' (failing to account for future moral progress) by creating a testbed where agents must anticipate and adapt to historical shifts in moral values, rather than just mirroring contemporary static norms."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Qiu-ProgressGym.md"
abstract: "Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. We introduce progress alignment as a technical solution to mitigate this imminent risk."
paper_summary: "Abstract: Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contri | Overview: ProgressGym: Alignment with a Millennium of Moral Progress Tianyi Qiu1∗† Yang Zhang1∗ Xuchuan Huang1 Jasmine Xinze Li2 Jiaming Ji1 Yaodong Yang1 1 Peking University 2 Cornell University Abstract Front | Methodology: to progress alignment is the emergence of novel concepts. While quantitative extrapolations of moral trends are relatively easy to learn from historic | Key Findings: 24 F Implementation Details of ProgressGym Challenges 25 F.1 The PG-Follow Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 F. | Conclusions: In this study, we introduce progress alignment as a solution to risks of value lock-in in human-AI interactions, and build the ProgressGym framework t"
local_pdf: [[PDFs/2024/2024-Qiu-ProgressGym.pdf]]
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "Llama-3, GPT-4"
DATA_URL: "https://github.com/PKU-Alignment/ProgressGym"
---
# ProgressGym: Alignment with a Millennium of Moral Progress

## Metadata

**Authors:** Qiu, Tianyi; Zhang, Yang; Huang, Xuchuan; Li, Jasmine Xinze; Ji, Jiaming; Yang, Yaodong

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2406.20087](https://doi.org/10.48550/arXiv.2406.20087)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Qiu-ProgressGym.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2406.20087
- **DOI:** https://doi.org/10.48550/arXiv.2406.20087

## Abstract

Frontier AI systems, including large language models (LLMs), hold increasing influence over the epistemology of human users. Such influence can reinforce prevailing societal values, potentially contributing to the lock-in of misguided moral beliefs and, consequently, the perpetuation of problematic moral practices on a broad scale. We introduce progress alignment as a technical solution to mitigate this imminent risk. Progress alignment algorithms learn to emulate the mechanics of human moral progress, thereby addressing the susceptibility of existing alignment methods to contemporary moral blindspots. To empower research in progress alignment, we introduce ProgressGym,3 an experimental framework allowing the learning of moral progress mechanics from history, in order to facilitate future progress in real-world moral decisions. Leveraging 9 centuries of historical text and 18 historical LLMs,4 ProgressGym enables codification of real-world progress alignment challenges into concrete benchmarks. Specifically, we introduce three core challenges: tracking evolving values (PG-Follow), preemptively anticipating moral progress (PG-Predict), and regulating the feedback loop between human and AI value shifts (PG-Coevolve). Alignment methods without a temporal dimension are inapplicable to these tasks. In response, we present lifelong and extrapolative algorithms as baseline methods of progress alignment, and build an open leaderboard5 soliciting novel algorithms and challenges.

## Authors

[[Tianyi Qiu]], [[Yang Zhang]], [[Xuchuan Huang]], [[Jasmine Xinze Li]], [[Jiaming Ji]], [[Yaodong Yang]]

## Data Description

ProgressGym provides a large-scale experimental framework comprising 38GB of historical text data spanning 9 centuries (1221-2022 AD) from sources including Internet Archive, Project Gutenberg, EEBO, and Pile of Law (1.83 million documents). The framework includes 18 historical LLMs (Llama3-8B and Llama3-70B fine-tuned for each century) and a morality evaluation framework with 5,104 questions across 19 value dimensions. It benchmarks three progress alignment challenges: PG-Follow, PG-Predict, and PG-Coevolve.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language #Computer-Science---Human-Computer-Interaction

## Citation Info

8 citations (Semantic Scholar/DOI) [2025-08-27] 8 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2406.20087 [cs]
