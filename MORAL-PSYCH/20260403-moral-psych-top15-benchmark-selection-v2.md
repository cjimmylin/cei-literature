# Moral Psychology Benchmarks: Revised Top-15 Selection (v2)

**Date:** 2026-04-03
**Version:** v2 (expanded keyword scorer + hidden gem assessment)
**Weighting:** PD=0.50, PE=0.30, CI=0.20

## Changes from v1

### Added
- **Differences in Moral Foundations of LLMs** (2024) — composite 63.74
- **EMNLP (Educator-role Moral and Normative LLMs Profiling)** (2025) — composite 46.6
- **Model Editing as a Double-Edged Sword** (2025) — composite 50.75
- **TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs** (2025) — composite 52.2
- **ValueCompass: A Framework for Measuring Contextual Value Alignment** (2025) — composite 55.0
- **Knowing But Not Doing: Convergent Morality and Divergent Action in LLMs (ValAct-15k)** (2026) — composite 58.8

### Removed
- **Assessing LLMs for Moral Value Pluralism** (2023) — composite 55.63
- **How Can a Deontological Decision Lead to Moral** (2016) — composite 55.17
- **Moral Foundations Vignettes** (2015) — composite 64.47
- **Probing the Moral Development of Large Language** (2023) — composite 63.23
- **Concerns and Values in Human-Robot Interactions** (2025) — composite 36.12
- **Do Moral Judgment and Reasoning Capability of** (2024) — composite 66.03

## Revised Top-15

| # | Benchmark | Year | Theory | Format | Size | Composite | PD | PE | CI |
|---|-----------|------|--------|--------|------|-----------|----|----|-----|
| 1 | The Moral Machine experiment | 2018 | trolley | Forced-choice | 40000000 | 78.45 | 75.5 | 74.0 | 92.5 |
| 2 | The moral machine experiment on large language | 2024 | trolley | Forced-choice | 50000 | 69.9 | 72.5 | 69.5 | 64.0 |
| 3 | Crowdsourcing moral machines | 2020 | trolley | Forced-choice | 40000000 | 69.87 | 72.5 | 67.4 | 67.0 |
| 4 | Moral Foundations Twitter Corpus | 2020 | mft | Multi-label classification | 35108 | 68.1 | 68.0 | 66.0 | 71.5 |
| 5 | Does Moral Code Have a Moral Code? | 2022 | mft, schwartz | Binary + MCQ | 100 | 66.29 | 72.0 | 59.3 | 62.5 |
| 6 | Moral Foundations of Large Language Models | 2024 | mft | Likert | 30 | 63.84 | 85.0 | 62.8 | 12.5 |
| 7 | Differences in Moral Foundations of LLMs | 2024 | mft | Likert | 116 | 63.74 | 80.0 | 65.8 | 20.0 |
| 8 | Value Kaleidoscope | 2024 | schwartz | Free-text generation + MCQ | 218000 | 61.6 | 55.5 | 69.5 | 65.0 |
| 9 | Multilingual Defining Issues Test | 2024 | kohlberg | Scenario rating + ranking | 9 | 61.23 | 80.0 | 54.1 | 25.0 |
| 10 | Knowing But Not Doing: Convergent Morality and Div | 2026 | schwartz | MCQ | 15000 | 58.8 | 75.5 | 61.8 | 12.5 |
| 11 | ValueCompass: A Framework for Measuring Contextual | 2025 | schwartz, dyadic | Likert | 6272 | 55.0 | 72.5 | 54.2 | 12.5 |
| 12 | CVC | 2025 |  | MCQ + scenario generation | 250000 | 52.81 | 51.0 | 73.7 | 26.0 |
| 13 | TrolleyBench -- Evaluating Emergent Moral Reasonin | 2025 | kohlberg, trolley | Binary | 50 | 52.2 | 56.0 | 59.0 | 32.5 |
| 14 | Model Editing as a Double-Edged Sword | 2025 | kohlberg, mft | Mixed | 5000 | 50.75 | 63.0 | 55.8 | 12.5 |
| 15 | EMNLP (Educator-role Moral and Normative LLMs Prof | 2025 | kohlberg | Mixed | 88 | 46.6 | 61.0 | 45.5 | 12.5 |

## Theory Coverage

- **mft**: 5 papers
- **trolley**: 4 papers
- **schwartz**: 4 papers
- **kohlberg**: 4 papers
- **dyadic**: 1 papers

## Full Matrix

Total entries in expanded matrix: 54
Entries passing hard gates (PD≥40 + data): 34
