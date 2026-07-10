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
authors: "Charles Packer; Sarah Wooders; Letta Team"
url: "https://www.letta.com/blog/letta-leaderboard"
external_pdf: "file:///Users/jimmylin/Zotero/storage/ASQRZ4EW/Aggarwal and others - 2025 - Letta Leaderboard Benchmarking Agentic Memory in LLMs.pdf"
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
newtags: 
tags: 
abstract: "The Letta Leaderboard is a comprehensive benchmark suite that evaluates how effectively LLMs manage agentic memory. It measures two foundational aspects of context management: core memory (in-context memory) and archival memory (external memory). The benchmark evaluates stateful agents' fundamental capabilities on reading, writing, and updating memories using fictional question-answering datasets with supporting facts to minimize prior knowledge from LLM training."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "Claude, GPT-4, GPT-4o, GPT-4o mini, Gemini"
DATA_URL: NA
pdf_extract: "PDF Extracts/2025/2025-Aggarwal-Letta Leaderboard.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Aggarwal-Letta Leaderboard.pdf]]"
CONFERENCE: Unknown
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
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

The Letta Leaderboard evaluates LLMs on agentic memory management across core and archival memory tasks (read, write, update) using synthetic fictional question-answering datasets designed to isolate memory operations from prior training knowledge.


## Notes

