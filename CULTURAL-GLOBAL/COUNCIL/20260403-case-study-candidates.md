# Case Study Candidates for Deliberation #2

Per Council Recommendation R11 from Deliberation 01.

3 candidates per slot for council selection.

Data: 20260403-nw-scores.json, 20260403-author-geography.json, paper YAML files.


## Slot 1: Japanese Syncretic

**Criterion:** Highest nw_confucian score among papers with author_country = JP.

**Purpose:** Illustrate how keyword scoring handles hybrid Shinto-Buddhist-Confucian traditions.


| # | Paper | nw_confucian | Other NW Scores | Rationale |
|---|-------|-------------|-----------------|-----------|
| 1 | AI-based medical ethics education | 50 | all 0 | Highest Confucian score from JP |
| 2 | JCommonsenseMorality: Japanese Dataset for Evaluating Commonsense Mora | 0 | all 0 | #2 Confucian score from JP |
| 3 | Does Cross-Cultural Alignment Change the Commonsense Morality of Langu | 0 | all 0 | #3 Confucian score from JP |

## Slot 2: Southeast Asian

**Criterion:** Highest max across all 7 nw_* scores among papers with author_region = Southeast Asia.

**Purpose:** Illustrate what keywords capture/miss in this culturally diverse, underrepresented region.


| # | Paper | Max NW Score | Leading Framework | All NW Scores | Rationale |
|---|-------|-------------|-------------------|---------------|-----------|
| 1 | Fine-tuning Large Language Model (BERT) for | 100 | Islamic | Isl=100 | Top SE Asian paper |
| 2 | Divine LLaMAs Bias Stereotypes Stigmatization and | 65 | Buddhist | Conf=5, Bud=65, Dha=25 | Top SE Asian paper |
| 3 | A New Age Indigenous Instrument: Artificial Intelligence & Its Potenti | 55 | Indigenous | Ind=55 | Top SE Asian paper |

## Slot 3: Sanctions-Affected Country

**Criterion:** Paper with author_country in {IR, SY, CU, KP, VE}.

**Purpose:** Illustrate structural exclusion from the corpus due to geopolitical sanctions.


| # | Paper | Country | Max NW Score | All NW Scores | Rationale |
|---|-------|---------|-------------|---------------|-----------|
| 1 | EPT Benchmark: Evaluation of Persian Trustworthiness in Large Language | IR | 50 | Isl=50 | Sanctions-affected country |
| 2 | FarsTail: A Persian Natural Language Inference Dataset | IR | 0 | all 0 | Sanctions-affected country |
| 3 | IslamicPCQA | IR | 0 | all 0 | Sanctions-affected country |

## Slot 4: Latin American — Low Buen Vivir Despite Relevant Content

**Criterion:** Paper with author_region = Latin America & Caribbean, lowest nw_buen_vivir score
despite title/abstract mentioning Latin America, decolonial, indigenous, or related terms.

**Purpose:** Illustrate the language/indexing gap — Latin American papers engaging relevant
concepts in Western-legible vocabulary score low on buen_vivir keywords.


| # | Paper | nw_buen_vivir | Other NW Scores | Short Title | Rationale |
|---|-------|--------------|-----------------|-------------|-----------|
| 1 | 2021-Carroll-Operationalizing the CARE and FAIR Principles f | 0 | Ind=65 | Operationalizing the CARE and FAIR Principles for Indigenous Data Futures | Low BV despite LatAm content |
| 2 | 2023-Mager-Neural Machine Translation for the Indigenous Lan | 0 | Ind=5 | Neural Machine Translation for the Indigenous Languages of the Americas: An Intr | Low BV despite LatAm content |
| 3 | 2024-Lewis-Abundant Intelligences Placing AI within Indigeno | 0 | Ind=50 | Abundant Intelligences: Placing AI within Indigenous Knowledge Frameworks | Low BV despite LatAm content |

## Slot 5: rv_islam vs nw_islamic Divergence

**Criterion:** Paper with maximum |rv_islam - nw_islamic_jurisprudence| score divergence.

**Purpose:** Illustrate the descriptive-vs-normative distinction between religious values
detection (rv_islam: Islamic content broadly) and normative framework detection
(nw_islamic_ethics: engagement with Islamic ethical reasoning).


| # | Paper | rv_islam | nw_islamic | Divergence | Short Title | Rationale |
|---|-------|----------|-----------|------------|-------------|-----------|
| 1 | 2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classifi | 100 | 0 | 100 | Jigsaw Unintended Bias in Toxicity Classification | High rv, low nw: descriptive not normative |
| 2 | 2020-Yasseri-Detecting Weak and Strong Islamophobic Hat | 100 | 0 | 100 | Detecting Weak and Strong Islamophobic Hate | High rv, low nw: descriptive not normative |
| 3 | 2021-Barikeri-REDDITBIAS.md | 100 | 0 | 100 | REDDITBIAS | High rv, low nw: descriptive not normative |
