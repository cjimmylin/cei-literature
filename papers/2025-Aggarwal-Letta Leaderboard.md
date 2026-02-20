---









Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 4Q6V7F2E
type: document
short_title: "Letta Leaderboard"
year: 2025
first_author: "[[Charles Packer]]"
last_author: "[[Letta Team]]"
authors: "[[Charles Packer]]; [[Sarah Wooders]]; Letta Team"
url: "https://www.letta.com/blog/letta-leaderboard"
external_pdf: "file:///Users/jimmylin/Zotero/storage/ASQRZ4EW/Aggarwal and others - 2025 - Letta Leaderboard Benchmarking Agentic Memory in LLMs.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "The Letta Leaderboard is a comprehensive benchmark suite that evaluates how effectively LLMs manage agentic memory. It measures two foundational aspects of context management: core memory (in-context memory) and archival memory (external memory). The benchmark evaluates stateful agents' fundamental capabilities on reading, writing, and updating memories using fictional question-answering datasets with supporting facts to minimize prior knowledge from LLM training."
DATE_ADDED: 20260208
LLM_assessed: "Claude, GPT-4"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2025/2025-Aggarwal-Letta Leaderboard.md"
local_pdf: "[[PDFs/2025/2025-Aggarwal-Letta Leaderboard.pdf]]"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
CONFERENCE: "Unknown"
---
# Letta Leaderboard: Benchmarking Agentic Memory in LLMs

## Metadata

**Authors:** Packer, Charles; Wooders, Sarah (Letta Team)

**Year:** 2025

**Type:** document

## Links

- **URL:** https://www.letta.com/blog/letta-leaderboard

## Abstract

The Letta Leaderboard is a comprehensive benchmark suite that evaluates how effectively LLMs manage agentic memory. It measures two foundational aspects of context management: core memory (in-context memory) and archival memory (external memory). The benchmark evaluates stateful agents' fundamental capabilities on reading, writing, and updating memories using fictional question-answering datasets with supporting facts to minimize prior knowledge from LLM training.

## Authors

[[Charles Packer]], [[Sarah Wooders]], [[Letta Team]]

## Detailed Summary

The Letta Leaderboard is a comprehensive benchmark suite evaluating how effectively LLMs manage agentic memory - a critical capability for AI agents that must maintain context and learn from interactions over extended periods. The benchmark measures two foundational aspects of context management: core memory (in-context memory within the model's attention window) and archival memory (external memory systems for storing and retrieving information beyond context limits).

The benchmark addresses the growing importance of stateful AI agents that maintain persistent memory across conversations and tasks. Unlike traditional one-shot evaluations, the Letta Leaderboard tests agents' fundamental capabilities for reading, writing, and updating memories over time. The evaluation uses fictional question-answering datasets with supporting facts specifically designed to minimize contamination from LLM pre-training knowledge.

The significance of this work lies in establishing rigorous evaluation standards for a capability that is increasingly central to practical AI applications. As LLM agents are deployed in scenarios requiring long-term memory (personal assistants, research tools, enterprise applications), the ability to reliably store, retrieve, and update information becomes critical. The Letta Leaderboard provides the first systematic framework for comparing this capability across models.

## Paper Outline

1. Introduction - Memory management in LLM agents
2. Background - Core vs. archival memory architectures
3. Benchmark Design - Task structure and evaluation criteria
4. Dataset Construction - Fictional QA with supporting facts
5. Evaluation Tasks - Reading, writing, updating memory
6. Model Evaluation - Testing across LLM families
7. Results Analysis - Performance patterns and limitations
8. Discussion - Implications for agent development
9. Conclusion and Future Directions

## Methods Summary

The methodology involves: (1) Definition of two memory types: core memory (in-context) and archival memory (external storage). (2) Design of evaluation tasks testing fundamental memory operations: reading stored information, writing new facts, and updating existing memories. (3) Construction of fictional QA datasets that cannot be answered from pre-training knowledge, requiring actual memory use. (4) Evaluation protocols measuring accuracy, latency, and reliability of memory operations. (5) Testing across multiple LLM families and agent architectures. (6) Analysis of failure modes and performance degradation patterns.

## Results Summary

Key findings: (1) Significant variation exists in memory management capabilities across models. (2) Core memory (in-context) operations are generally more reliable than archival memory. (3) Memory update operations prove more challenging than reading or initial writing. (4) Larger models do not uniformly outperform smaller ones on memory tasks. (5) Agent architectures matter - the same base model shows different performance depending on memory system implementation. (6) Long-range dependencies in archival memory retrieval remain challenging for all tested systems.

## Conclusions

The authors conclude that agentic memory remains an underdeveloped capability requiring dedicated evaluation and optimization. The Letta Leaderboard provides essential infrastructure for measuring and comparing memory performance. Limitations include focus on English text and relatively simple memory operations. Future work should extend to multi-modal memory, more complex reasoning over stored information, and evaluation of memory in realistic long-running agent scenarios.

## Artifact Contributions

- Letta Leaderboard: Benchmark suite for agentic memory evaluation
- Fictional QA datasets: Evaluation data minimizing pre-training contamination
- Evaluation framework: Protocols for testing memory read/write/update operations
- Public leaderboard: https://www.letta.com/blog/letta-leaderboard

## Data Description

The Letta Leaderboard benchmarks LLMs on agentic memory management across three capabilities: reading, writing, and updating memory. It uses synthetic facts and questions for evaluation, with a prompted GPT-4.1 grading agent responses following the SimpleQA methodology. Top models tested include Claude 4 Sonnet, GPT-4.1, GPT-4o, GPT-4o-mini, and Gemini 2.5 Flash.


## Notes

