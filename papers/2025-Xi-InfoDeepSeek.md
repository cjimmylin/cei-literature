---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VPXHQ939
type: conferencePaper
short_title: InfoDeepSeek
year: 2025
first_author: "[[Yunjia Xi]]"
authors: "Yunjia Xi; Jianghao Lin; Menghui Zhu; Yongzhao Xiao; Zhuoying Ou; Jiaqi Liu; Tong Wan; Bo Chen; Weiwen Liu; Yasheng Wang; Ruiming Tang; Weinan Zhang; Yong Yu"
doi: 10.48550/arXiv.2505.15872
url: "http://arxiv.org/abs/2505.15872"
external_pdf: "http://arxiv.org/pdf/2505.15872.pdf"
publication: arXiv.org
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: Utilitarianism
key_contribution: "Presents InfoDeepSeek, a benchmark for 'Agentic RAG' evaluating information seeking in dynamic web environments"
significance: "Moves evaluation from static retrieval to dynamic agentic behavior, measuring 'utility' and 'compactness' of information seeking, essential for developing autonomous knowledge agents"
pdf_extract: "PDF Extracts/2025-Xi-InfoDeepSeek.md"
abstract: "Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by grounding responses with retrieved information. As an emerging paradigm, Agentic RAG further enhances this process by introducing autonomous LLM agents into the information seeking process. However, existing benchmarks fall short in evaluating such systems, as they are confined to a static retrieval environment with a fixed, limited corpus and simple queries that fail to elicit agentic behavior. Moreover, their evaluat"
paper_summary: "Abstract: Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by grounding responses with retrieved information. As an emerging paradigm, Agentic RAG further enhances this process by intr | Overview: InfoDeepSeek: Benchmarking Agentic Information Seeking for Retrieval-Augmented Generation Yunjia Xi1, Jianghao Lin1∗, Menghui Zhu2, Yongzhao Xiao1, Zhuoying Ou1, Jiaqi Liu1, Tong Wan1, Bo Chen2, Weiwe | Key Findings: w/ Golden Doc Set Dynamic Evaluation w/o Golden Doc Set 🎯 Answer Accuracy 📦 Info. Quality by NDCG & Recall ✂️ Rubost & Compact 🎯 Answer Accuracy ⏱️ In"
local_pdf: [[PDFs/2025-Xi-InfoDeepSeek.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: Yes
research_topic: "Machine Learning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark text corpus"
data_metrics: "Not specified"
---
# InfoDeepSeek: Benchmarking Agentic Information Seeking for Retrieval-Augmented Generation

## Metadata

**Authors:** Xi, Yunjia; Lin, Jianghao; Zhu, Menghui; Xiao, Yongzhao; Ou, Zhuoying; Liu, Jiaqi; Wan, Tong; Chen, Bo; Liu, Weiwen; Wang, Yasheng; Tang, Ruiming; Zhang, Weinan; Yu, Yong

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.15872](https://doi.org/10.48550/arXiv.2505.15872)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025-Xi-InfoDeepSeek.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.15872
- **DOI:** https://doi.org/10.48550/arXiv.2505.15872

## Abstract

This paper introduces **InfoDeepSeek**, a benchmark designed to evaluate **Agentic Retrieval-Augmented Generation (Agentic RAG)**. Unlike traditional RAG which retrieves from a static corpus, Agentic RAG involves autonomous agents actively seeking information in dynamic web environments. The authors criticize existing benchmarks for being static and relying on "gold sets" that don't reflect the open-ended nature of the web. InfoDeepSeek provides a framework with challenging queries (determinacy, difficulty, diversity) and fine-grained metrics for accuracy, utility, and compactness.

### Detailed Summary
The paper addresses the shift from "passive" retrieval to "active" agentic information seeking. In Agentic RAG, the model doesn't just receive documents; it must decide *what* to search for, *how* to refine its queries, and *when* to stop. InfoDeepSeek creates a realistic testbed for this by simulating dynamic web interactions. The benchmark reveals that many current LLMs struggle with the "utility" of their searches—often retrieving redundant or irrelevant information even if they eventually answer the question. The authors propose a methodical query construction process to ensure high difficulty and determinacy.

### Paper Outline
1.  **Introduction**: the rise of Agentic RAG and the limitations of static benchmarks (e.g., simplistic queries, fixed corpora).
2.  **InfoDeepSeek Benchmark**: Methodology for constructing "D3" queries (Determinacy, Difficulty, Diversity).
3.  **Evaluation Framework**: New metrics beyond simple accuracy: Search Utility and Search Compactness.
4.  **Experiments**: Testing various LLMs and search engines.
5.  **Analysis**: Nuanced behaviors of different agents (e.g., some are "lazy searchers," others are "spam searchers").
6.  **Conclusion**: Future directions for autonomous information seeking agents.

### Methods Summary
*   **Query Construction**: A systematic pipeline ensuring queries require multi-step reasoning and cannot be answered by simple lookup.
*   **Environment**: A dynamic web simulation (or live web wrapper) where agents issue queries and receive search engine results.
*   **Metrics**:
    *   **Accuracy**: Correctness of the final answer.
    *   **Utility**: The ratio of useful information retrieved to total information retrieved.
    *   **Compactness**: The efficiency of the search process (number of steps/tokens).

### Results Summary
1.  **Agent Behavior**: Significant variance in search strategies. Some models (like GPT-4) are highly efficient, while smaller open weights models often get stuck in loops or retrieve vast amounts of irrelevant data.
2.  **Performance Gap**: Existing static benchmarks overestimate the capabilities of these agents. Real-world dynamic seeking is much harder.
3.  **Search Engine Impact**: The quality of the underlying search engine (e.g., Google vs. Bing vs. DuckDuckGo) significantly affects agent performance, but "smarter" agents are more robust to poor search results.

### Conclusions
Agentic RAG is the future of knowledge systems, but we lack the tools to measure it properly. InfoDeepSeek fills this gap, providing a rigorous standard that penalizes inefficient or "hallucinating" search behaviors.

### Artifact Contributions
*   **InfoDeepSeek Benchmark**: A dataset of challenging, open-ended information-seeking queries.
*   **Evaluation Codebase**: Tools for measuring agentic search metrics.

## Authors

[[Yunjia Xi]], [[Jianghao Lin]], [[Menghui Zhu]], [[Yongzhao Xiao]], [[Zhuoying Ou]], [[Jiaqi Liu]], [[Tong Wan]], [[Bo Chen]], [[Weiwen Liu]], [[Yasheng Wang]], [[Ruiming Tang]], [[Weinan Zhang]], [[Yong Yu]]

## Notes


## Tags

#Computer-Science---Computation-and-Language #Computer-Science---Information-Retrieval

## Citation Info

68 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23]
