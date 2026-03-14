---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EZY3F9KR
type: conferencePaper
short_title: GMAI-MMBench
year: 2024
first_author: "[[Pengcheng Chen]]"
last_author: "[[Yu Qiao]]"
authors: "Pengcheng Chen; Jin Ye; Guoan Wang; Yanjun Li; Zhongying Deng; Wei Li; Tianbin Li; Haodong Duan; Ziyan Huang; Yanzhou Su; Benyou Wang; Shaoting Zhang; Bin Fu; Jianfei Cai; Bohan Zhuang; Eric J Seibel; Junjun He; Yu Qiao"
doi: 10.48550/arXiv.2408.03361
url: "http://arxiv.org/abs/2408.03361"
external_pdf: "http://arxiv.org/pdf/2408.03361.pdf"
publication: "Neural Information Processing Systems"
CONF-CC: "NeurIPS 2024"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2024/2024-Chen-GMAI-MMBench.md"
abstract: "Large Vision-Language Models (LVLMs) are capable of handling diverse data types such as imaging, text, and physiological signals, and can be applied in various fields. In the medical field, LVLMs have a high potential to offer substantial assistance for diagnosis and treatment. Before that, it is crucial to develop benchmarks to evaluate LVLMs’ effectiveness in various medical applications. Current benchmarks are often built upon specific academic literature, mainly focusing on a single domain,..."
paper_summary: "Abstract: Large Vision-Language Models (LVLMs) are capable of handling diverse data types such as imaging, text, and physiological signals, and can be applied in vari- ous fields. In the medical field, LVLMs ha | Overview: GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI Pengcheng Chen1,2∗Jin Ye1,3∗† Guoan Wang1,4∗Yanjun Li1,4 Zhongying Deng5 Wei Li1,6 Tianbin Li1 Haodong Duan1 Zi | Methodology: for the semantic segmentation and quantitative analysis of retinal arteries and veins in infrared reflectance imaging. IEEE Journal of Biomedical and  | Key Findings: across all clinical aspects. A comprehensive benchmark should be easily customized to evaluate any specific abilities of LVLMs for each clinical profe | Conclusions: The development of GMAI-MMBench as a benchmark for evaluating LVLMs' capabilities represents a significant advancement in the pursuit of general medic"
local_pdf: "[[PDFs/2024/2024-Chen-GMAI-MMBench.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Claude-3 Opus, CogVLM, DeepSeek-VL, Gemini, Gemini Pro 1.5, GPT-4V, GPT-4o, InternVL, LLaVA, MiniCPM-V, Qwen-VL"
DATA_URL: "https://huggingface.co/datasets/OpenGVLab/GMAI-MMBench"
CONFERENCE: "NeurIPS 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
research_topic: "Computer Vision & Multimodal"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset for question answering"
data_metrics: "284 datasets"
---
# GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI

## Metadata

**Authors:** Chen, Pengcheng; Ye, Jin; Wang, Guoan; Li, Yanjun; Deng, Zhongying; Li, Wei; Li, Tianbin; Duan, Haodong; Huang, Ziyan; Su, Yanzhou; Wang, Benyou; Zhang, Shaoting; Fu, Bin; Cai, Jianfei; Zhuang, Bohan; Seibel, Eric J.; He, Junjun; Qiao, Yu

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2408.03361](https://doi.org/10.48550/arXiv.2408.03361)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Chen-GMAI-MMBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2408.03361
- **DOI:** https://doi.org/10.48550/arXiv.2408.03361

## Abstract

Large Vision-Language Models (LVLMs) are capable of handling diverse data types such as imaging, text, and physiological signals, and can be applied in various fields. In the medical field, LVLMs have a high potential to offer substantial assistance for diagnosis and treatment. Before that, it is crucial to develop benchmarks to evaluate LVLMs' effectiveness in various medical applications. Current benchmarks are often built upon specific academic literature, mainly focusing on a single domain, and lacking varying perceptual granularities. Thus, they face specific challenges, including limited clinical relevance, incomplete evaluations, and insufficient guidance for interactive LVLMs. To address these limitations, we developed the GMAI-MMBench, the most comprehensive general medical AI benchmark with well-categorized data structure and multi-perceptual granularity to date. It is constructed from 284 datasets across 38 medical image modalities, 18 clinical-related tasks, 18 departments, and 4 perceptual granularities in a Visual Question Answering (VQA) format. Additionally, we implemented a lexical tree structure that allows users to customize evaluation tasks, accommodating various assessment needs and substantially supporting medical AI research and applications. We evaluated 50 LVLMs, and the results show that even the advanced GPT-4o only achieves an accuracy of 53.96%, indicating significant room for improvement. Moreover, we identified five key insufficiencies in current cutting-edge LVLMs that need to be addressed to advance the development of better medical applications. We believe that GMAI-MMBench will stimulate the community to build the next generation of LVLMs toward GMAI.

## Authors

[[Pengcheng Chen]], [[Jin Ye]], [[Guoan Wang]], [[Yanjun Li]], [[Zhongying Deng]], [[Wei Li]], [[Tianbin Li]], [[Haodong Duan]], [[Ziyan Huang]], [[Yanzhou Su]], [[Benyou Wang]], [[Shaoting Zhang]], [[Bin Fu]], [[Jianfei Cai]], [[Bohan Zhuang]], [[Eric J Seibel]], [[Junjun He]], [[Yu Qiao]]

## Data Description

GMAI-MMBench: a comprehensive medical AI multimodal benchmark with ~26K VQA pairs from 284 datasets across 38 imaging modalities, 18 clinical VQA tasks, 18 departments, and 4 perceptual granularities, organized in a lexical tree for customized evaluation.


## Notes


## Tags

#Computer-Science---Computer-Vision-and-Pattern-Recognition #Electrical-Engineering-and-Systems-Science---Image-and-Video-Processing

## Citation Info

0 citations (Semantic Scholar/arXiv) [2025-08-27] 52 citations (Semantic Scholar/DOI) [2025-08-27]
