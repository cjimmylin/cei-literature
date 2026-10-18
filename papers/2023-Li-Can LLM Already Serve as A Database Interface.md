---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: IKK34ECN
type: conferencePaper
short_title: "Can LLM Already Serve as A Database Interface?"
year: 2023
first_author: "[[Jinyang Li]]"
last_author: "[[Yongbin Li]]"
authors: "Jinyang Li; Binyuan Hui; Ge Qu; Jiaxi Yang; Binhua Li; Bowen Li; Bailin Wang; Bowen Qin; Rongyu Cao; Ruiying Geng; Nan Huo; Xuanhe Zhou; Chenhao Ma; Guoliang Li; Kevin C. C. Chang; Fei Huang; Reynold Cheng; Yongbin Li"
doi: 10.48550/arXiv.2305.03111
tags: 
url: "http://arxiv.org/abs/2305.03111"
external_pdf: "http://arxiv.org/pdf/2305.03111.pdf"
publication: "Neural Information Processing Systems"
CONF-CC: "NeurIPS 2023"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
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
newtags: "Hallucination & Truthfulness"
key_contribution: "Presented BIRD, a large-scale Text-to-SQL benchmark emphasizing 'dirty' database values and external knowledge grounding, pushing models beyond clean schema matching."
significance: "While primarily a technical benchmark, it highlights the 'truthfulness' and 'grounding' aspect of model reliability, showing that even GPT-4 struggles (54% accuracy) when faced with real-world, noisy data constraints."
pdf_extract: "PDF Extracts/2023/2023-Li-Can LLM Already Serve as A Database Interface.md"
abstract: "Text-to-SQL parsing, which aims at converting natural language questions into executable SQLs, has gained increasing attention in recent years. In particular, GPT-4 and Claude-2 have shown impressive results in this task. However, most of the prevalent benchmarks, i.e., Spider, and WikiSQL, focus on database schema with few rows of database values leaving the gap between academic study and real-world applications."
paper_summary: "Abstract: Text-to-SQL parsing, which aims at converting natural language questions into executable SQLs, has gained increasing attention in recent years. In particular, GPT-4 and Claude-2 have shown impressive  | Overview: Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs Jinyang Li1,♣‡, Binyuan Hui2,♣, Ge Qu1,♣, Jiaxi Yang2, Binhua Li2, Bowen Li6, Bailin Wang5, Bo | Key Findings: benchmark towards text-to-SQL robustness. In The Eleventh International Conference on Learning Representations, 2023. [7] Zhiyu Chen, Wenhu Chen, Char | Conclusions: In this paper, we introduce BIRD, a large-scale cross-domain, text-to-SQL benchmark with a particular focus on large database values. BIRD mitigates t"
local_pdf: "[[Lit-WS-PDFs/2023/2023-Li-Can LLM Already Serve as A Database Interface.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, GPT-4, Claude, T5"
DATA_URL: "https://bird-bench.github.io/"
CONFERENCE: "NeurIPS 2023"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Hallucination & Truthfulness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark dataset"
data_metrics: "33.4 gb"
---
# Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs

## Metadata

**Authors:** Li, Jinyang; Hui, Binyuan; Qu, Ge; Yang, Jiaxi; Li, Binhua; Li, Bowen; Wang, Bailin; Qin, Bowen; Cao, Rongyu; Geng, Ruiying; Huo, Nan; Zhou, Xuanhe; Ma, Chenhao; Li, Guoliang; Chang, Kevin C. C.; Huang, Fei; Cheng, Reynold; Li, Yongbin

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2305.03111](https://doi.org/10.48550/arXiv.2305.03111)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-PDFs/2023/2023-Li-Can LLM Already Serve as A Database Interface.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2305.03111
- **DOI:** https://doi.org/10.48550/arXiv.2305.03111

## Abstract

Text-to-SQL parsing, which aims at converting natural language questions into executable SQLs, has gained increasing attention in recent years. In particular, GPT-4 and Claude-2 have shown impressive results in this task. However, most of the prevalent benchmarks, i.e., Spider, and WikiSQL, focus on database schema with few rows of database values leaving the gap between academic study and real-world applications. To mitigate this gap, we present BIRD, a BIg bench for laRge-scale Database grounded in text-to-SQL tasks, containing 12,751 text-toSQL pairs and 95 databases with a total size of 33.4 GB, spanning 37 professional domains. Our emphasis on database values highlights the new challenges of dirty and noisy database values, external knowledge grounding between NL questions and database values, and SQL efficiency, particularly in the context of massive databases. To solve these problems, text-to-SQL models must feature database value comprehension in addition to semantic parsing. The experimental results demonstrate the significance of database values in generating accurate text-to-SQLs for big databases. Furthermore, even the most effective text-to-SQL models, i.e. GPT-4, only achieve 54.89% in execution accuracy, which is still far from the human result of 92.96%, proving that challenges still stand. We also provide an efficiency analysis to offer insights into generating text-to-efficient-SQLs that are beneficial to industries. We believe that BIRD will contribute to advancing real-world applications of text-to-SQL research. The leaderboard and source code are available: https://bird-bench.github.io/.

## Authors

[[Jinyang Li]], [[Binyuan Hui]], [[Ge Qu]], [[Jiaxi Yang]], [[Binhua Li]], [[Bowen Li]], [[Bailin Wang]], [[Bowen Qin]], [[Rongyu Cao]], [[Ruiying Geng]], [[Nan Huo]], [[Xuanhe Zhou]], [[Chenhao Ma]], [[Guoliang Li]], [[Kevin C. C. Chang]], [[Fei Huang]], [[Reynold Cheng]], [[Yongbin Li]]

## Data Description

BIRD: 12,751 text-to-SQL pairs over 95 databases (33.4 GB total) spanning 37 professional domains, with external knowledge annotations and efficiency metrics.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

13 citations (Semantic Scholar/DOI) [2025-08-27] 477 citations (Semantic Scholar/arXiv) [2025-08-27]
