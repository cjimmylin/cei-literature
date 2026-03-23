# EleutherAI lm-evaluation-harness Integration Report

**Date:** 2026-03-12
**Session:** EleutherAI Integration
**Vault count:** 2,040 papers (was 2,034; +6 new)

---

## Summary

The [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) implements 200+ evaluation benchmarks for LLMs. We identified **22 values/ethics-related benchmarks** whose underlying papers belong in this vault. Of these, **16 already existed** and **6 were missing**.

**Actions taken:**
- Tagged all 22 papers with `eleutherai: incorporated` in YAML frontmatter
- Created 6 new paper entries with full pipeline (metadata, PDF, extract, classification)
- YAML validation: **2,040/2,040 valid, 0 errors**

---

## Table 1 — Existing Papers (16)

| # | Paper | Benchmark | EleutherAI Task |
|---|-------|-----------|-----------------|
| 1 | 2021-Hendrycks-Aligning AI with Shared Human Values | ETHICS | `hendrycks_ethics` |
| 2 | 2021-Emelin-Moral Stories | Moral Stories | `moral_stories` |
| 3 | 2025-Leteno-Histoires Morales | Histoires Morales | `histoires_morales` |
| 4 | 2022-Parrish-BBQ Bias Benchmark for Question Answering | BBQ | `bbq` |
| 5 | 2025-Ruiz-Fernández-EsBBQ and CaBBQ | EsBBQ / CaBBQ | `esbbq`, `cabbq` |
| 6 | 2020-Nangia-CrowS-Pairs | CrowS-Pairs | `crows_pairs` |
| 7 | 2022-Hartvigsen-ToxiGen | ToxiGen | `toxigen` |
| 8 | 2020-Gehman-RealToxicityPrompts | RealToxicityPrompts | `realtoxicityprompts` |
| 9 | 2022-Lin-TruthfulQA | TruthfulQA | `truthfulqa` |
| 10 | 2024-Sharma-Towards Understanding Sycophancy in Language Models | Sycophancy | `sycophancy` |
| 11 | 2025-Cheng-ELEPHANT Social Sycophancy | ELEPHANT | `elephant` |
| 12 | 2025-Paech-EQ-Bench An Emotional Intelligence Benchmark for Large Language Models | EQ-Bench | `eq_bench` |
| 13 | 2024-Li-The WMDP Benchmark | WMDP | `wmdp` |
| 14 | 2025-Sadallah-Commonsense Reasoning in Arab Culture | Arab Culture Commonsense | `arab_culture_commonsense` |
| 15 | 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs | AraDiCE | `aradice` |
| 16 | 2024-Hooker-Global MMLU Understanding and Addressing Cultural | Global MMLU | `global_mmlu` |

All 16 were already classified and had existing Lit-WS-PDFs/extracts. Only the `eleutherai: incorporated` tag was added.

---

## Table 2 — New Papers (6)

| # | Paper | Key | arXiv | PDF | Extract | Ethics | Classification |
|---|-------|-----|-------|-----|---------|--------|---------------|
| 1 | 2023-Tamkin-Evaluating and Mitigating Discrimination in Language Model Decisions | ELEUTHERAI_01 | 2312.03689 | 3.2 MB, 28pp | 1,696 lines | Yes | Bias & Fairness; eval=Y, dataset=Y |
| 2 | 2018-Rudinger-Gender Bias in Coreference Resolution | ELEUTHERAI_02 | 1804.09301 | 345 KB, 7pp | 717 lines | Yes | Bias & Fairness; eval=Y |
| 3 | 2020-Brown-Language Models are Few-Shot Learners | ELEUTHERAI_03 | 2005.14165 | 6.5 MB, 75pp | 5,470 lines | No | NLP & Representation Learning; benchmark=Y, eval=Y, dataset=Y |
| 4 | 2019-Sap-Social IQa Commonsense Reasoning about Social Interactions | ELEUTHERAI_04 | 1904.09728 | 583 KB, 11pp | 1,219 lines | No | Machine Learning; benchmark=Y |
| 5 | 2022-Perez-Discovering Language Model Behaviors with Model-Written Evaluations | ELEUTHERAI_05 | 2212.09251 | 3.4 MB, 47pp | 5,495 lines | No | Social & Cultural Analysis*; eval=Y, dataset=Y |
| 6 | 2023-McKenzie-Inverse Scaling Can Become U-Shaped | ELEUTHERAI_06 | 2211.02011 | 1.3 MB, 15pp | 1,200 lines | No | Other; eval=Y |

*Perez 2022 `research_topic: "Social & Cultural Analysis"` may warrant manual review — paper focuses on automated LM evaluation methodology, not social/cultural analysis per se.

---

## New Author Profiles Created

| Author | Paper |
|--------|-------|
| Jason Naradowsky | Rudinger 2018 |
| Brian Leonard | Rudinger 2018 |
| Benjamin Van Durme | Rudinger 2018 |
| Tom B. Brown | Brown 2020 (GPT-3) |
| Jason Wei | McKenzie 2023 |
| Najoung Kim | McKenzie 2023 |
| Yi Tay | McKenzie 2023 |
| Quoc V. Le | McKenzie 2023 |

---

## Issues & Notes

1. **McKenzie arXiv ID correction:** The plan specified arXiv 2306.09479, which is the companion paper "Inverse Scaling: When Bigger Isn't Better" by McKenzie et al. The correct ID for "Inverse Scaling Can Become U-Shaped" is **2211.02011** by Jason Wei et al. (published at EMNLP 2023). The filename retains "McKenzie" per the original plan, but YAML metadata correctly attributes authorship to Wei et al.

2. **Classification scripts batch mode:** The `classify_ethics.py` and related scripts do not support `--file` single-file mode — they process the entire vault on each run. Multiple agents ran the full pipeline, which is redundant but not harmful (idempotent classification).

3. **Perez 2022 research_topic:** Classified as "Social & Cultural Analysis" by keyword heuristics. May warrant manual review — the paper is more accurately about AI safety evaluation methodology.

4. **Sap 2019 author profile:** Maarten Sap already had a rich author profile; the new paper was added to his papers list.

---

## Validation

| Check | Result |
|-------|--------|
| Papers with `eleutherai: incorporated` | 22/22 |
| YAML validation | 2,040/2,040 valid, 0 errors |
| New PDFs with `%PDF-` magic bytes | 6/6 |
| New PDF extracts | 6/6 |
| New author profiles | 8 created |
