# Paper Statistics 6: Benchmarks, Datasets, and Evaluations
**Generated**: 2026-01-24
**Total Verified Items**: 46

## Executive Summary
This report contains a manually verified list of key contributions to AI Alignment in the form of **Benchmarks**, **Datasets**, and **Evaluation Frameworks**. These papers were identified through a semantic analysis of 300+ candidates and selected for their direct contribution of quantitative tools for measuring values, safety, and ethics.

## Summary Statistics
- **Benchmarks**: 16
- **Datasets**: 26
- **Evaluation Frameworks**: 4

## Benchmarks (16)

| Year | Implementation Name | Values Measured | Usage |
|------|-------------------|-----------------|-------|
| 2024 | **FFB (Fair Fairness Benchmark)** | Fairness | Assessment |
| 2024 | **AlignBench** | General Alignment (Chinese) | Assessment |
| 2023 | **Safety Gymnasium** | Safety (RL Constraints) | Training/Assessment |
| 2023 | **MACHIAVELLI** | Ethics (Power-seeking, Deception) | Assessment |
| 2023 | **HaluEval** | Truthfulness (Hallucination) | Assessment |
| 2023 | **FACET** | Fairness (Computer Vision) | Assessment |
| 2023 | **CValues** | Safety, Responsibility (Chinese) | Assessment |
| 2023 | **BIRD** | Grounding/Reasoning (Text-to-SQL) | Assessment |
| 2023 | **AgentBench** | Agent Capabilities/Safety | Assessment |
| 2022 | **TruthfulQA** | Truthfulness | Assessment |
| 2022 | **Jiminy Cricket** | Morality | Assessment |
| 2022 | **FairLex** | Fairness (Legal) | Assessment |
| 2022 | **BBQ (Bias Benchmark for QA)** | Bias (Protected Groups) | Assessment |
| 2021 | **HateCheck** | Safety (Hate Speech) | Assessment |
| 2021 | **ETHICS** | Morality (Justice, Virtue, Deontology, Utilitarianism) | Assessment |
| 2018 | **WinoBias (Zhao et al.)** | Bias (Gender/Coreference) | Assessment |

### Detailed Benchmark Descriptions
#### FFB (Fair Fairness Benchmark) (2024)
- **Paper**: [[2023-Han-FFB]]
- **Author**: Han
- **Items/Size**: 45k experiments
- **Usage**: Assessment
- **Target Values**: Fairness

#### AlignBench (2024)
- **Paper**: [[2023-Liu-AlignBench]]
- **Author**: Liu
- **Items/Size**: 683 queries
- **Usage**: Assessment
- **Target Values**: General Alignment (Chinese)

#### Safety Gymnasium (2023)
- **Paper**: [[2023-Ji-Safety Gymnasium]]
- **Author**: Ji
- **Items/Size**: RL Environments
- **Usage**: Training/Assessment
- **Target Values**: Safety (RL Constraints)

#### MACHIAVELLI (2023)
- **Paper**: [[2023-Jiang-MACHIAVELLI]]
- **Author**: Jiang
- **Items/Size**: 134 games / 500k scenarios
- **Usage**: Assessment
- **Target Values**: Ethics (Power-seeking, Deception)

#### HaluEval (2023)
- **Paper**: [[2023-Li-HaluEval]]
- **Author**: Li
- **Items/Size**: Large-scale
- **Usage**: Assessment
- **Target Values**: Truthfulness (Hallucination)

#### FACET (2023)
- **Paper**: [[2023-Gustafson-FACET]]
- **Author**: Gustafson
- **Items/Size**: 32k images
- **Usage**: Assessment
- **Target Values**: Fairness (Computer Vision)

#### CValues (2023)
- **Paper**: [[2023-Xu-CValues]]
- **Author**: Xu
- **Items/Size**: Safety/Responsibility prompts
- **Usage**: Assessment
- **Target Values**: Safety, Responsibility (Chinese)

#### BIRD (2023)
- **Paper**: [[2023-Li-BIRD]]
- **Author**: Li
- **Items/Size**: 12,751 pairs
- **Usage**: Assessment
- **Target Values**: Grounding/Reasoning (Text-to-SQL)

#### AgentBench (2023)
- **Paper**: [[2023-Liu-AgentBench]]
- **Author**: Liu
- **Items/Size**: 8 environments
- **Usage**: Assessment
- **Target Values**: Agent Capabilities/Safety

#### TruthfulQA (2022)
- **Paper**: [[2022-Lin-TruthfulQA]]
- **Author**: Lin
- **Items/Size**: 817 questions
- **Usage**: Assessment
- **Target Values**: Truthfulness

#### Jiminy Cricket (2022)
- **Paper**: [[2022-Hendrycks-What Would Jiminy Cricket Do]]
- **Author**: Hendrycks
- **Items/Size**: 25 text adventure games
- **Usage**: Assessment
- **Target Values**: Morality

#### FairLex (2022)
- **Paper**: [[2022-Chalkidis-FairLex]]
- **Author**: Chalkidis
- **Items/Size**: 4 datasets
- **Usage**: Assessment
- **Target Values**: Fairness (Legal)

#### BBQ (Bias Benchmark for QA) (2022)
- **Paper**: [[2022-Parrish-BBQ]]
- **Author**: Parrish
- **Items/Size**: Question sets
- **Usage**: Assessment
- **Target Values**: Bias (Protected Groups)

#### HateCheck (2021)
- **Paper**: [[2021-Röttger-HateCheck]]
- **Author**: Röttger
- **Items/Size**: Functional tests
- **Usage**: Assessment
- **Target Values**: Safety (Hate Speech)

#### ETHICS (2021)
- **Paper**: [[2021-Hendrycks-Aligning AI with Shared Human Values]]
- **Author**: Hendrycks
- **Items/Size**: N/A
- **Usage**: Assessment
- **Target Values**: Morality (Justice, Virtue, Deontology, Utilitarianism)

#### WinoBias (Zhao et al.) (2018)
- **Paper**: [[2018-Zhao-Gender Bias in Coreference Resolution]]
- **Author**: Zhao
- **Items/Size**: 3,160 sentences
- **Usage**: Assessment
- **Target Values**: Bias (Gender/Coreference)

---

## Datasets (26)

| Year | Implementation Name | Values Measured | Usage |
|------|-------------------|-----------------|-------|
| 2023 | **Value FULCRA** | Human Values (Schwartz Theory) | Assessment/Alignment |
| 2023 | **ToxicChat** | Safety (Toxicity) | Assessment/Training |
| 2023 | **OpinionsQA** | Bias (Political/Demographic) | Assessment |
| 2023 | **Moral Beliefs Survey** | Morality | Assessment |
| 2023 | **HelpSteer** | Helpfulness (Correctness, Coherence) | Training (SteerLM) |
| 2023 | **FairPrism** | Fairness (Stereotyping) | Assessment |
| 2022 | **ValueNet** | Human Values (Schwartz Theory) | Training/Assessment |
| 2022 | **ToxiGen** | Safety (Implicit Hate Speech) | Training/Assessment |
| 2022 | **SODA** | Social Commonsense | Training |
| 2022 | **ProsocialDialog** | Safety/Prosocial norms | Training |
| 2022 | **MIC (Moral Integrity Corpus)** | Morality | Assessment |
| 2022 | **Anthropic Red Teaming Dataset** | Safety (Harms) | Assessment/Training |
| 2021 | **StereoSet** | Bias (Stereotypes) | Assessment |
| 2021 | **Scruples** | Ethics (Descriptive) | Assessment/Training |
| 2021 | **RAL-E / HateBERT** | Safety (Abusive Language) | Training |
| 2021 | **Moral Stories** | Morality (Social Norms) | Training/Assessment |
| 2021 | **BOLD** | Bias (Open-ended generation) | Assessment |
| 2020 | **Social Chemistry 101** | Morality (Social Norms) | Training/Assessment |
| 2020 | **Social Bias Frames (SBIC)** | Bias (Power implications) | Assessment/Training |
| 2020 | **RealToxicityPrompts** | Safety (Toxicity) | Assessment |
| 2020 | **MFTC (Moral Foundations Twitter Corpus)** | Morality (MFT) | Assessment |
| 2020 | **HateXplain** | Safety (Hate Speech) | Assessment (Explainability) |
| 2020 | **CrowS-Pairs** | Bias (Social) | Assessment |
| 2019 | **Bias in Bios** | Bias (Gender/Occupation) | Assessment |
| 2018 | **Unintended Bias in Text Classification** | Bias (Identity Terms) | Assessment |
| 2018 | **EEC (Equity Evaluation Corpus)** | Bias (Gender/Race) | Assessment |

### Detailed Dataset Descriptions
#### Value FULCRA (2023)
- **Paper**: [[2023-Yao-Value FULCRA]]
- **Author**: Yao
- **Items/Size**: 5k pairs
- **Usage**: Assessment/Alignment
- **Target Values**: Human Values (Schwartz Theory)

#### ToxicChat (2023)
- **Paper**: [[2023-Lin-ToxicChat]]
- **Author**: Lin
- **Items/Size**: User-AI conversations
- **Usage**: Assessment/Training
- **Target Values**: Safety (Toxicity)

#### OpinionsQA (2023)
- **Paper**: [[2023-Santurkar-Whose Opinions Do Language Models Reflect]]
- **Author**: Santurkar
- **Items/Size**: Poll questions
- **Usage**: Assessment
- **Target Values**: Bias (Political/Demographic)

#### Moral Beliefs Survey (2023)
- **Paper**: [[2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs]]
- **Author**: Scherrer
- **Items/Size**: 680 ambiguous scenarios
- **Usage**: Assessment
- **Target Values**: Morality

#### HelpSteer (2023)
- **Paper**: [[2023-TheDevastator-HelpSteer A-i Alignment Dataset]]
- **Author**: TheDevastator
- **Items/Size**: 37k samples
- **Usage**: Training (SteerLM)
- **Target Values**: Helpfulness (Correctness, Coherence)

#### FairPrism (2023)
- **Paper**: [[2023-Fleisig-FairPrism]]
- **Author**: Fleisig
- **Items/Size**: 5,000 examples
- **Usage**: Assessment
- **Target Values**: Fairness (Stereotyping)

#### ValueNet (2022)
- **Paper**: [[2022-Qiu-ValueNet]]
- **Author**: Qiu
- **Items/Size**: 21,374 scenarios
- **Usage**: Training/Assessment
- **Target Values**: Human Values (Schwartz Theory)

#### ToxiGen (2022)
- **Paper**: [[2022-Hartvigsen-ToxiGen]]
- **Author**: Hartvigsen
- **Items/Size**: 274k statements
- **Usage**: Training/Assessment
- **Target Values**: Safety (Implicit Hate Speech)

#### SODA (2022)
- **Paper**: [[2022-Kim-SODA]]
- **Author**: Kim
- **Items/Size**: Million-scale
- **Usage**: Training
- **Target Values**: Social Commonsense

#### ProsocialDialog (2022)
- **Paper**: [[2022-Kim-ProsocialDialog]]
- **Author**: Kim
- **Items/Size**: 58K dialogues
- **Usage**: Training
- **Target Values**: Safety/Prosocial norms

#### MIC (Moral Integrity Corpus) (2022)
- **Paper**: [[2022-Ziems-The Moral Integrity Corpus]]
- **Author**: Ziems
- **Items/Size**: 38k pairs / 99k RoTs
- **Usage**: Assessment
- **Target Values**: Morality

#### Anthropic Red Teaming Dataset (2022)
- **Paper**: [[2022-Ganguli-Red Teaming Language Models to Reduce Harms]]
- **Author**: Ganguli
- **Items/Size**: 38,961 attacks
- **Usage**: Assessment/Training
- **Target Values**: Safety (Harms)

#### StereoSet (2021)
- **Paper**: [[2021-Nadeem-StereoSet]]
- **Author**: Nadeem
- **Items/Size**: Large-scale
- **Usage**: Assessment
- **Target Values**: Bias (Stereotypes)

#### Scruples (2021)
- **Paper**: [[2021-Lourie-Scruples]]
- **Author**: Lourie
- **Items/Size**: 32,000 anecdotes
- **Usage**: Assessment/Training
- **Target Values**: Ethics (Descriptive)

#### RAL-E / HateBERT (2021)
- **Paper**: [[2021-Caselli-HateBERT]]
- **Author**: Caselli
- **Items/Size**: Reddit comments
- **Usage**: Training
- **Target Values**: Safety (Abusive Language)

#### Moral Stories (2021)
- **Paper**: [[2021-Emelin-Moral Stories]]
- **Author**: Emelin
- **Items/Size**: Situated narratives
- **Usage**: Training/Assessment
- **Target Values**: Morality (Social Norms)

#### BOLD (2021)
- **Paper**: [[2021-Dhamala-BOLD]]
- **Author**: Dhamala
- **Items/Size**: 23,679 prompts
- **Usage**: Assessment
- **Target Values**: Bias (Open-ended generation)

#### Social Chemistry 101 (2020)
- **Paper**: [[2020-Forbes-Social Chemistry 101]]
- **Author**: Forbes
- **Items/Size**: 292k rules
- **Usage**: Training/Assessment
- **Target Values**: Morality (Social Norms)

#### Social Bias Frames (SBIC) (2020)
- **Paper**: [[2020-Sap-Social Bias Frames]]
- **Author**: Sap
- **Items/Size**: 44k posts
- **Usage**: Assessment/Training
- **Target Values**: Bias (Power implications)

#### RealToxicityPrompts (2020)
- **Paper**: [[2020-Gehman-RealToxicityPrompts]]
- **Author**: Gehman
- **Items/Size**: 100K prompts
- **Usage**: Assessment
- **Target Values**: Safety (Toxicity)

#### MFTC (Moral Foundations Twitter Corpus) (2020)
- **Paper**: [[2020-Hoover-Moral Foundations Twitter Corpus]]
- **Author**: Hoover
- **Items/Size**: 35,108 tweets
- **Usage**: Assessment
- **Target Values**: Morality (MFT)

#### HateXplain (2020)
- **Paper**: [[2020-Mathew-HateXplain]]
- **Author**: Mathew
- **Items/Size**: Benchmark dataset
- **Usage**: Assessment (Explainability)
- **Target Values**: Safety (Hate Speech)

#### CrowS-Pairs (2020)
- **Paper**: [[2020-Nangia-CrowS-Pairs]]
- **Author**: Nangia
- **Items/Size**: Challenge dataset
- **Usage**: Assessment
- **Target Values**: Bias (Social)

#### Bias in Bios (2019)
- **Paper**: [[2019-De-Arteaga-Bias in Bios]]
- **Author**: De-Arteaga
- **Items/Size**: Large-scale
- **Usage**: Assessment
- **Target Values**: Bias (Gender/Occupation)

#### Unintended Bias in Text Classification (2018)
- **Paper**: [[2018-Dixon-Measuring and Mitigating Unintended Bias in Text]]
- **Author**: Dixon
- **Items/Size**: Wikipedia Talk Labels
- **Usage**: Assessment
- **Target Values**: Bias (Identity Terms)

#### EEC (Equity Evaluation Corpus) (2018)
- **Paper**: [[2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred]]
- **Author**: Kiritchenko
- **Items/Size**: 8,640 sentences
- **Usage**: Assessment
- **Target Values**: Bias (Gender/Race)

---

## Evaluation Frameworks (4)

| Year | Implementation Name | Values Measured | Usage |
|------|-------------------|-----------------|-------|
| 2023 | **NIST AI RMF** | Risk Management | Governance |
| 2023 | **GPTFuzzer** | Safety (Jailbreaking) | Red Teaming |
| 2023 | **DecodingTrust** | Trustworthiness (Toxicity, Bias, Privacy, Robustness) | Assessment |
| 2022 | **HELM** | Holistic (Accuracy, Fairness, Toxicity, etc.) | Assessment |

### Detailed Evaluation Framework Descriptions
#### NIST AI RMF (2023)
- **Paper**: [[2023-Standards-NIST AI Risk Management Framework]]
- **Author**: NIST
- **Items/Size**: N/A
- **Usage**: Governance
- **Target Values**: Risk Management

#### GPTFuzzer (2023)
- **Paper**: [[2023-Yu-GPTFuzzer]]
- **Author**: Yu
- **Items/Size**: Fuzzing framework
- **Usage**: Red Teaming
- **Target Values**: Safety (Jailbreaking)

#### DecodingTrust (2023)
- **Paper**: [[2023-Wang-DecodingTrust]]
- **Author**: Wang
- **Items/Size**: Comprehensive suite
- **Usage**: Assessment
- **Target Values**: Trustworthiness (Toxicity, Bias, Privacy, Robustness)

#### HELM (2022)
- **Paper**: [[2022-Liang-Holistic Evaluation of Language Models]]
- **Author**: Liang
- **Items/Size**: 42 scenarios
- **Usage**: Assessment
- **Target Values**: Holistic (Accuracy, Fairness, Toxicity, etc.)

---
