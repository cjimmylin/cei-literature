---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 2Y8UILKM
type: conferencePaper
short_title: TrustLLM
year: 2024
first_author: "[[Yue Huang]]"
last_author: "[[Zhao, Yue]]"
authors: "Huang, Yue; Sun, Lichao; Wang, Haoran; Wu, Siyuan; Zhang, Qihui; Li, Yuan; Gao, Chujie; Huang, Yixin; Lyu, Wenhan; Zhang, Yixuan; Li, Xiner; Liu, Zhengliang; Liu, Yixin; Wang, Yijue; Zhang, Zhikun; Vidgen, Bertie; Kailkhura, Bhavya; Xiong, Caiming; Xiao, Chaowei; Li, Chunyuan; Xing, Eric; Huang, Furong; Liu, Hao; Ji, Heng; Wang, Hongyi; Zhang, Huan; Yao, Huaxiu; Kellis, Manolis; Zitnik, Marinka; Jiang, Meng; Bansal, Mohit; Zou, James; Pei, Jian; Liu, Jian; Gao, Jianfeng; Han, Jiawei; Zhao, Jieyu; Tang, Jiliang; Wang, Jindong; Vanschoren, Joaquin; Mitchell, John; Shu, Kai; Xu, Kaidi; Chang, Kai-Wei; He, Lifang; Huang, Lifu; Backes, Michael; Gong, Neil Zhenqiang; Philip S. Yu; Chen, Pin-Yu; Gu, Quanquan; Xu, Ran; Ying, Rex; Ji, Shuiwang; Jana, Suman; Chen, Tianlong; Liu, Tianming; Zhou, Tianyi; Wang, William; Li, Xiang; Zhang, Xiangliang; Wang, Xiao; Xie, Xing; Chen, Xun; Wang, Xuyu; Liu, Yan; Ye, Yanfang; Cao, Yinzhi; Chen, Yong; Zhao, Yue"
doi: 10.48550/arXiv.2401.05561
tags: 
url: "http://arxiv.org/abs/2401.05561"
pdf_extract: "PDF Extracts/2024/2024-Huang-TrustLLM.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Huang-TrustLLM.pdf]]"
external_pdf: "http://arxiv.org/pdf/2401.05561.pdf"
publication: arXiv.org
CONF-CC: Preprint
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
newtags: "Deontology, Utilitarianism"
key_contribution: "Establishes a comprehensive benchmark (TRUSTLLM) across 8 dimensions including machine ethics, evaluating 16 mainstream LLMs"
significance: "Finds that while LLMs have basic moral understanding, they fall short in complex scenarios and proprietary models outperform open-source ones"
abstract: "Large language models (LLMs), exemplified by ChatGPT, have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges, particularly in the realm of trustworthiness. Therefore, ensuring the trustworthiness of LLMs emerges as an important topic. This paper introduces TRUSTLLM, a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark,..."
paper_summary: "Abstract: Large language models (LLMs), exemplified by ChatGPT, have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges,  | Overview: TRUSTLLM: TRUSTWORTHINESS IN LARGE LANGUAGE MODELS – A PRINCIPLE AND BENCHMARK Yue Huang1,2∗† ‡ Lichao Sun1∗† Haoran Wang3∗Siyuan Wu4∗‡ Qihui Zhang4∗‡ Yuan Li5 ‡ Chujie Gao4∗‡ Yixin Huang6∗Wenhan Lyu7 | Key Findings: provides a significant reference value for relevant open-weight developers. Both the model itself and trustworthiness-related technology should be tra | Conclusions: 79 17 Acknowledgement 79 4 --- Page 5 --- TRUSTLLM 1 Introduction The advent of large language models (LLMs) marks a significant milestone in natural"
nw_confucian: 30
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: GE
author_region: "Eastern Europe & Central Asia"
author_global_north_south: Ambiguous
weird_score: 38
DATE_ADDED: 20260208
LLM_assessed: "Baichuan, ChatGLM2, ERNIE, GPT-3.5, GPT-4, Koala, Llama-2, Mistral, Oasst, PaLM-2, Vicuna, WizardLM"
DATA_URL: "https://github.com/HowieHwong/TrustLLM"
CONFERENCE: "Other Conference"
ethics_overall: 75
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety dataset"
data_metrics: "30 datasets"
ethics_perspective: "AI Safety & Alignment"
---
 TrustLLM: Trustworthiness in Large Language Models

## Authors

[[Yue Huang|Huang, Yue]], [[Lichao Sun|Sun, Lichao]], [[Haoran Wang|Wang, Haoran]], [[Siyuan Wu|Wu, Siyuan]], [[Qihui Zhang|Zhang, Qihui]], [[Yuan Li|Li, Yuan]], [[Chujie Gao|Gao, Chujie]], [[Yixin Huang|Huang, Yixin]], [[Wenhan Lyu|Lyu, Wenhan]], [[Yixuan Zhang|Zhang, Yixuan]], [[Xiner Li|Li, Xiner]], [[Zhengliang Liu|Liu, Zhengliang]], [[Yixin Liu|Liu, Yixin]], [[Yijue Wang|Wang, Yijue]], [[Zhikun Zhang|Zhang, Zhikun]], [[Bertie Vidgen|Vidgen, Bertie]], [[Bhavya Kailkhura|Kailkhura, Bhavya]], [[Caiming Xiong|Xiong, Caiming]], [[Chaowei Xiao|Xiao, Chaowei]], [[Chunyuan Li|Li, Chunyuan]], [[Eric Xing|Xing, Eric]], [[Furong Huang|Huang, Furong]], [[Hao Liu|Liu, Hao]], [[Heng Ji|Ji, Heng]], [[Hongyi Wang|Wang, Hongyi]], [[Huan Zhang|Zhang, Huan]], [[Huaxiu Yao|Yao, Huaxiu]], [[Manolis Kellis|Kellis, Manolis]], [[Marinka Zitnik|Zitnik, Marinka]], [[Meng Jiang|Jiang, Meng]], [[Mohit Bansal|Bansal, Mohit]], [[James Zou|Zou, James]], [[Jian Pei|Pei, Jian]], [[Jian Liu|Liu, Jian]], [[Jianfeng Gao|Gao, Jianfeng]], [[Jiawei Han|Han, Jiawei]], [[Jieyu Zhao|Zhao, Jieyu]], [[Jiliang Tang|Tang, Jiliang]], [[Jindong Wang|Wang, Jindong]], [[Joaquin Vanschoren|Vanschoren, Joaquin]], [[John Mitchell|Mitchell, John]], [[Kai Shu|Shu, Kai]], [[Kaidi Xu|Xu, Kaidi]], [[Kai-Wei Chang|Chang, Kai-Wei]], [[Lifang He|He, Lifang]], [[Lifu Huang|Huang, Lifu]], [[Michael Backes|Backes, Michael]], [[Neil Zhenqiang Gong|Gong, Neil Zhenqiang]], [[Yu, Philip S]], [[Pin-Yu Chen|Chen, Pin-Yu]], [[Quanquan Gu|Gu, Quanquan]], [[Ran Xu|Xu, Ran]], [[Rex Ying|Ying, Rex]], [[Shuiwang Ji|Ji, Shuiwang]], [[Suman Jana|Jana, Suman]], [[Tianlong Chen|Chen, Tianlong]], [[Tianming Liu|Liu, Tianming]], [[Tianyi Zhou|Zhou, Tianyi]], [[William Wang|Wang, William]], [[Xiang Li|Li, Xiang]], [[Xiangliang Zhang|Zhang, Xiangliang]], [[Xiao Wang|Wang, Xiao]], [[Xing Xie|Xie, Xing]], [[Xun Chen|Chen, Xun]], [[Xuyu Wang|Wang, Xuyu]], [[Yan Liu|Liu, Yan]], [[Yanfang Ye|Ye, Yanfang]], [[Yinzhi Cao|Cao, Yinzhi]], [[Yong Chen|Chen, Yong]], [[Yue Zhao|Zhao, Yue]]

## Links

- **Local PDF:** [[Lit-WS-PDFs/2024/2024-Huang-TrustLLM.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2401.05561
- **DOI:** https://doi.org/10.48550/arXiv.2401.05561

## Detailed Summary

**TrustLLM** is a comprehensive framework and survey designed to benchmark and evaluate the **trustworthiness** of Large Language Models. The authors identify eight critical facets of trustworthiness that an LLM should possess: **Truthfulness, Safety, Fairness, Robustness, Privacy, Machine Ethics, Transparency, and Accountability**. 

The paper evaluates 16 mainstream LLMs (both proprietary like GPT-4 and open-source like Llama2) across these dimensions using 30 diverse datasets. The study highlights a persistent "Trustworthiness Gap" and provides a roadmap for future auditing.

## Paper Outline

1.  **Introduction**: The complexity and risks of generative AI; High user expectations for alignment.
2.  **The TRUSTLLM Framework**:
    *   Identification of 8 facets.
    *   Evaluation of 16 diverse LLMs.
    *   Benchmarking 30 datasets.
3.  **Survey of Trustworthiness**: Reviewing 600 papers to define the state of the art.
4.  **Evaluation Results**: Insights into how current models handle truth, safety, and bias.
5.  **Conclusion**: Future directions for trustworthy AI development.

## Methods Summary

The authors separate **utility** (functional effectiveness) from **trustworthiness**. They identify eight key aspects through an extensive review of over 600 papers across AI, security, and human-computer interaction (HCI). The evaluation involves benchmarking 16 LLMs on 30 datasets using varied metrics ranging from classification accuracy to qualitative generation quality. Specifically, they use "Jailbreaking" attacks to test robustness and "TruthfulQA" style probes for machine ethics.

## Results Summary

1.  **Disparity in Trustworthiness**: Proprietary models generally outperform open-source models in safety and robustness, but even top-tier models like GPT-4 remain vulnerable to sophisticated jailbreaking.
2.  **Truthfulness Challenge**: LLMs still struggle significantly with hallucinations and misinformation, particularly when internal knowledge is contradicted by subtle prompts.
3.  **Bias and Fairness**: Models frequently exhibit cultural and gender biases, reflecting the imbalances present in their massive training datasets.

## Conclusions

To be genuinely trustworthy, an LLM must appropriately reflect all eight identified characteristics. The authors conclude that standardized benchmarks like TRUSTLLM are essential because "utility" does not guarantee "safety." The project establishes a comprehensive evaluation framework for the community to assess future iterations of LLMs.

## Artifact Contributions

*   **TRUSTLLM Benchmark**: 30 datasets and evaluation scripts for auditing LLMs.
*   **Taxonomy of Trustworthiness**: A rigorous 8-facet definition of what makes an AI "trustworthy."


## Abstract

Large language models (LLMs), exemplified by ChatGPT, have gained considerable attention for their excellent natural language processing capabilities. Nonetheless, these LLMs present many challenges, particularly in the realm of trustworthiness. Therefore, ensuring the trustworthiness of LLMs emerges as an important topic. This paper introduces TrustLLM, a comprehensive study of trustworthiness in LLMs, including principles for different dimensions of trustworthiness, established benchmark, evaluation, and analysis of trustworthiness for mainstream LLMs, and discussion of open challenges and future directions. Specifically, we first propose a set of principles for trustworthy LLMs that span eight different dimensions. Based on these principles, we further establish a benchmark across six dimensions including truthfulness, safety, fairness, robustness, privacy, and machine ethics. We then present a study evaluating 16 mainstream LLMs in TrustLLM, consisting of over 30 datasets. Our findings firstly show that in general trustworthiness and utility (i.e., functional effectiveness) are positively related. Secondly, our observations reveal that proprietary LLMs generally outperform most open-source counterparts in terms of trustworthiness, raising concerns about the potential risks of widely accessible open-source LLMs. However, a few open-source LLMs come very close to proprietary ones. Thirdly, it is important to note that some LLMs may be overly calibrated towards exhibiting trustworthiness, to the extent that they compromise their utility by mistakenly treating benign prompts as harmful and consequently not responding. Finally, we emphasize the importance of ensuring transparency not only in the models themselves but also in the technologies that underpin trustworthiness. Knowing the specific trustworthy technologies that have been employed is crucial for analyzing their effectiveness.

## Data Description

TrustLLM benchmark comprising 30+ datasets across six trustworthiness dimensions (truthfulness, safety, fairness, robustness, privacy, machine ethics) for evaluating 16 mainstream LLMs.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

234 citations (Semantic Scholar/DOI) [2025-08-27] 232 citations (Semantic Scholar/DOI) [2025-08-23]
