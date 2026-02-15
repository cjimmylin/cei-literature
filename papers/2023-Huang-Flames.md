---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: I5KYMURQ
type: conferencePaper
short_title: Flames
year: 2025
first_author: "[[Kexin Huang]]"
last_author: "[[Dahua Lin]]"
authors: "Kexin Huang; Xiangyang Liu; Qianyu Guo; Tianxiang Sun; Jiawei Sun; Yaru Wang; Zeyang Zhou; Yixu Wang; Yan Teng; Xipeng Qiu; Yingchun Wang; Dahua Lin"
doi: 10.48550/arXiv.2311.06899
url: "http://arxiv.org/abs/2311.06899"
external_pdf: "http://arxiv.org/pdf/2311.06899.pdf"
publication: "North American Chapter of the Association for Computational Linguistics"
national_ethnic_cultural: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Benchmarked LLM value alignment in Chinese (FLAMES), focusing on 'harmony' and other specific Chinese values, finding most models perform poorly on safety/fairness."
significance: "Demonstrates the gap in safety alignment for non-Western values (like social harmony), showing that Western-aligned models may fail in specific cultural contexts."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Huang-Flames.md"
abstract: "The widespread adoption of large language models (LLMs) across various regions underscores the urgent need to evaluate their alignment with human values. Current benchmarks, however, fall short of effectively uncovering safety vulnerabilities in LLMs. Despite numerous models achieving high scores and ‘topping the chart’ in these evaluations, there is still a significant gap in LLMs’ deeper alignment with human values and achieving genuine harmlessness."
paper_summary: "Abstract: The widespread adoption of large language models (LLMs) across various regions under- scores the urgent need to evaluate their align- ment with human values. Current benchmarks, however, fall short of | Overview: FLAMES: Benchmarking Value Alignment of LLMs in Chinese Warning: this paper contains content that may be offensive or upsetting. Kexin Huang*†1,2 Xiangyang Liu*†1,2 Qianyu Guo*†1,2 Tianxiang Sun†1,2 J | Key Findings: LLM N+1 ? Adversarial methods Complex scenarios Figure 1: Pipeline of the construction of FLAMES Benchmark. tailed and fine-grained evaluation. Notabl | Conclusions: This study proposes FLAMES - the first highly ad- versarial benchmark for evaluating the value align- ment of LLMs in Chinese. FLAMES Benchmark consis"
local_pdf: [[PDFs/2023/2023-Huang-Flames.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "ChatGPT, GPT-4, Claude"
DATA_URL: "https://github.com/AIFlames/Flames"
DATE_ADDED: 20260207
---
# Flames: Benchmarking Value Alignment of LLMs in Chinese

## Metadata

**Authors:** Huang, Kexin; Liu, Xiangyang; Guo, Qianyu; Sun, Tianxiang; Sun, Jiawei; Wang, Yaru; Zhou, Zeyang; Wang, Yixu; Teng, Yan; Qiu, Xipeng; Wang, Yingchun; Lin, Dahua

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2311.06899](https://doi.org/10.48550/arXiv.2311.06899)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Huang-Flames.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2311.06899
- **DOI:** https://doi.org/10.48550/arXiv.2311.06899

## Abstract

The widespread adoption of large language models (LLMs) across various regions underscores the urgent need to evaluate their alignment with human values. Current benchmarks, however, fall short of effectively uncovering safety vulnerabilities in LLMs. Despite numerous models achieving high scores and ‘topping the chart’ in these evaluations, there is still a significant gap in LLMs’ deeper alignment with human values and achieving genuine harmlessness. To this end, this paper proposes a value alignment benchmark named FLAMES, which encompasses both common harmlessness principles and a unique morality dimension that integrates specific Chinese values such as harmony. Accordingly, we carefully design adversarial prompts that incorporate complex scenarios and jailbreaking methods, mostly with implicit malice. By prompting 17 mainstream LLMs, we obtain model responses and rigorously annotate them for detailed evaluation. Our findings indicate that all the evaluated LLMs demonstrate relatively poor performance on FLAMES, particularly in the safety and fairness dimensions. We also develop a lightweight specified scorer capable of scoring LLMs across multiple dimensions to efficiently evaluate new models on the benchmark. The complexity of FLAMES has far exceeded existing benchmarks, setting a new challenge for contemporary LLMs and highlighting the need for further alignment of LLMs. Our benchmark is publicly available at https://github.com/AIFlames/Flames.

## Authors

[[Kexin Huang]], [[Xiangyang Liu]], [[Qianyu Guo]], [[Tianxiang Sun]], [[Jiawei Sun]], [[Yaru Wang]], [[Zeyang Zhou]], [[Yixu Wang]], [[Yan Teng]], [[Xipeng Qiu]], [[Yingchun Wang]], [[Dahua Lin]]

## Data Description

FLAMES is an adversarial benchmark for evaluating value alignment of LLMs in Chinese, comprising 2,251 manually crafted adversarial prompts across five dimensions (Fairness, Legality, Data protection, Morality, Safety). The dataset includes fine-grained human annotations of approximately 22,900 response-label pairs from 17 mainstream LLMs, along with a trained specified scorer achieving 79.5% accuracy.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 20 citations (Semantic Scholar/arXiv) [2025-08-27] 6 citations (Semantic Scholar/DOI) [2025-08-23]
