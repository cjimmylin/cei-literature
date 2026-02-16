---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 79LASFK4
type: journalArticle
short_title: BIRD
year: 2023
first_author: "[[Jinyang Li]]"
last_author: "[[Yongbin Li]]"
authors: "Jinyang Li; Binyuan Hui; Ge Qu; Jiaxi Yang; Binhua Li; Bowen Li; Bailin Wang; Bowen Qin; Ruiying Geng; Nan Huo; Xuanhe Zhou; Chenhao Ma; Guoliang Li; Kevin Chen-Chuan Chang; Fei Huang; Reynold Cheng; Yongbin Li"
url: "https://bird-bench.github.io/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/TFIDUKB8/Li and others - 2023 - BIRD BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
research_topic: Other
abstract: "Text-to-SQL parsing, which aims at converting natural language questions into executable SQLs, has gained increasing attention in recent years. In particular, GPT-4 and Claude-2 have shown impressive results in this task. However, most of the prevalent benchmarks, i.e., Spider, and WikiSQL, focus on database schema with few rows of database values leaving the gap between academic study and real-world applications."
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, ChatGPT, Claude, T5"
DATA_URL: "https://bird-bench.github.io/"
pdf_extract: "PDF Extracts/2023/2023-Li-BIRD.md"
local_pdf: "[[PDFs/2023/2023-Li-BIRD.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "General Ethics"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "33.4 gb"
---
# BIRD: BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation

## Metadata

**Authors:** Li, Jinyang; Hui, Binyuan; Qu, Ge; Yang, Jiaxi; Li, Binhua; Li, Bowen; Wang, Bailin; Qin, Bowen; Geng, Ruiying; Huo, Nan; Zhou, Xuanhe; Ma, Chenhao; Li, Guoliang; Chang, Kevin Chen-Chuan; Huang, Fei; Cheng, Reynold; Li, Yongbin

**Year:** 2023

**Publication:** NeurIPS 2023 Track on Datasets and Benchmarks

**Type:** journalArticle

## Links

- **URL:** https://bird-bench.github.io/

## Abstract

Text-to-SQL parsing, which aims at converting natural language instructions into executable SQLs, has gained increasing attention in recent years. In particular, Codex and ChatGPT have shown impressive results in this task. However, most of the prevalent benchmarks, i.e., Spider, and WikiSQL, focus on database schema with few rows of database contents leaving the gap between academic study and real-world applications. To mitigate this gap, we present BIRD, a BIg benchmark for laRge-scale Database grounded in text-to-SQL tasks, containing 12,751 pairs of text-to-SQL data and 95 databases with a total size of 33.4 GB, spanning 37 professional domains. The emphasis on database values highlights new challenges including dirty database contents, external knowledge between NL questions and database contents, and SQL efficiency.

## Authors

[[Jinyang Li]], [[Binyuan Hui]], [[Ge Qu]], [[Jiaxi Yang]], [[Binhua Li]], [[Bowen Li]], [[Bailin Wang]], [[Bowen Qin]], [[Ruiying Geng]], [[Nan Huo]], [[Xuanhe Zhou]], [[Chenhao Ma]], [[Guoliang Li]], [[Kevin Chen-Chuan Chang]], [[Fei Huang]], [[Reynold Cheng]], [[Yongbin Li]]

## Detailed Summary

BIRD (BIg Bench for LaRge-scale Database Grounded Text-to-SQL) addresses the critical gap between academic text-to-SQL benchmarks and real-world database applications. While existing benchmarks like Spider and WikiSQL have driven impressive improvements in neural text-to-SQL models, they focus on database schemas with few rows of actual data. BIRD provides a more realistic benchmark with 12,751 text-to-SQL pairs across 95 databases totaling 33.4 GB, spanning 37 professional domains from healthcare to blockchain.

The benchmark introduces three key challenges absent from prior work: (1) dirty and noisy database values requiring data type processing and special character handling; (2) external knowledge reasoning where natural language questions require domain knowledge to map to database values; and (3) SQL execution efficiency, which is critical for industrial applications with large databases. For example, one challenge involves calculating average salary from strings like "US$57,500.00" that require parsing and type conversion.

The experimental results are humbling for state-of-the-art models: even GPT-4 achieves only 54.89% execution accuracy on BIRD, compared to 92.96% human performance. This 38% gap demonstrates that current LLMs are far from serving as reliable database interfaces for real-world scenarios. The benchmark thus provides a challenging testbed for advancing text-to-SQL research toward practical deployment.

## Paper Outline

1. Introduction
   - Rise of text-to-SQL parsing with LLMs
   - Gap between academic benchmarks and real-world applications
   - BIRD's key challenges: dirty values, external knowledge, efficiency
2. Task Formulation
   - Text-to-SQL with database values and external knowledge
   - Formal problem definition
3. Dataset Construction
   - Annotation entrance and quality control
   - Database sources (Kaggle, CTU Prague Repository)
   - Question annotation with database description files
   - SQL annotation with double-blind procedure
4. Data Statistics
   - Overall statistics comparison with prior benchmarks
   - Question types: Fundamental and Reasoning
   - SQL complexity analysis
5. Experiments
   - Fine-tuning approaches (T5)
   - In-context learning with LLMs (ChatGPT, Claude-2, GPT-4)
   - Execution accuracy and Valid Efficiency Score (VES)
6. Analysis
   - Error analysis and failure modes
   - Efficiency considerations

## Methods Summary

BIRD was constructed through rigorous crowdsourcing with quality controls. Annotators passed thorough examinations before participation. Databases were sourced from Kaggle (32%), CTU Prague Relational Learning Repository (48%), and synthesized from open tables (20%), covering 37 professional domains including healthcare, blockchain, sports, and finance.

Question annotation utilized Database Description Files providing full schema names and value descriptions to help annotators understand database contents. External knowledge evidence was classified into four categories: (1) Numeric Reasoning (mathematical computations), (2) Domain Knowledge (field-specific concepts), (3) Synonym Knowledge (equivalent expressions), and (4) Value Illustration (mapping descriptions to database values).

SQL annotation followed a double-blind procedure: two independent annotators generated SQLs without discussion, and results were compared by execution. Mismatches were resolved by experts. A new metric, Valid Efficiency Score (VES), was introduced to evaluate not just correctness but also SQL execution efficiency.

## Results Summary

- Dataset Scale: 12,751 text-to-SQL pairs, 95 databases (69 train, 11 dev, 15 test), 33.4 GB total
- Domain Coverage: 37 professional domains (blockchain, healthcare, sports, etc.)
- Database Size: Average 549K rows per database vs. 2K in Spider
- GPT-4 Performance: 54.89% execution accuracy
- Human Performance: 92.96% execution accuracy
- Performance Gap: 38 percentage points between best model and humans
- Question Types: Fundamental (match, ranking, comparison, counting, aggregation) and Reasoning (numeric, domain, synonym, value illustration)
- Efficiency Analysis: Significant variations in SQL execution time between naive and optimized queries

## Conclusions

BIRD demonstrates that current state-of-the-art text-to-SQL models, including GPT-4, are far from ready to serve as reliable database interfaces for real-world applications. The 38% gap between GPT-4 (54.89%) and human performance (92.96%) highlights the challenges posed by realistic database values, external knowledge requirements, and efficiency considerations. The benchmark encourages the NLP and database communities to address these more realistic settings. BIRD's emphasis on execution efficiency through the VES metric promotes research into generating not just correct but also efficient SQL queries, which is essential for industrial deployment.

## Artifact Contributions

- BIRD benchmark: 12,751 text-to-SQL pairs across 95 databases
- Total database size: 33.4 GB spanning 37 professional domains
- Database Description Files with schema and value explanations
- External Knowledge Evidence annotations (4 categories)
- Valid Efficiency Score (VES) metric for SQL efficiency evaluation
- Leaderboard and source code: https://bird-bench.github.io/
- Hidden test set with 15 databases to prevent data leakage

## Data Description

BIRD is a large-scale text-to-SQL benchmark containing 12,751 text-to-SQL pairs across 95 databases with a total size of 33.4 GB spanning 37 professional domains. The benchmark emphasizes challenges of dirty and noisy database values, external knowledge grounding, and SQL execution efficiency. It includes a novel Valid Efficiency Score (VES) metric and databases sourced from Kaggle, CTU Prague Relational Learning Repository, and open tables.


## Notes

