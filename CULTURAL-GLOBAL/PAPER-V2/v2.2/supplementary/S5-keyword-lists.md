# Supplementary: Complete Keyword Taxonomy Statistics

## S5.1 Keyword Counts by Framework

| Framework | Strong Keywords | Medium Keywords | FP Patterns | Total Terms |
|-----------|----------------|-----------------|-------------|-------------|
| Confucian | 10 | 10 | 6 | 26 |
| Ubuntu | 6 | 10 | 4 | 20 |
| Islamic | 7 | 9 | 0 | 16 |
| Buddhist | 6 | 7 | 6 | 19 |
| Dharmic | 6 | 7 | 4 | 17 |
| Indigenous | 6 | 6 | 4 | 16 |
| Buen Vivir | 3 | 5 | 1 | 9 |
| **Total** | **44** | **54** | **25** | **123** |

## S5.2 Scoring Statistics

### Detection Rates by Framework
| Framework | Papers ≥ 50 | % of Corpus | Mean Score (all) | Mean Score (≥50 only) | Precision | Adj. Count |
|-----------|-------------|-------------|------------------|----------------------|-----------|------------|
| Indigenous | 49 | 2.1% | 1.8 | 62.4 | 0.675 | ~33 |
| Confucian | 38 | 1.6% | 1.6 | 58.7 | 0.364 | ~14 |
| Islamic | 23 | 1.0% | 0.8 | 61.2 | 1.000 | ~23 |
| Ubuntu | 23 | 1.0% | 0.9 | 59.8 | 0.579 | ~13 |
| Buddhist | 22 | 0.9% | 0.9 | 57.3 | 0.333 | ~7 |
| Dharmic | 18 | 0.8% | 0.7 | 56.1 | 0.250 | ~4 |
| Buen Vivir | 8 | 0.3% | 0.2 | 53.5 | 0.167 | ~1 |

### Corpus-Wide Score Distribution
| Score Range | Papers | % |
|-------------|--------|---|
| 0 | 1,891 | 81.2% |
| 1--24 | 148 | 6.4% |
| 25--49 | 129 | 5.5% |
| 50--74 | 107 | 4.6% |
| 75--100 | 54 | 2.3% |

## S5.3 False Positive Pattern Taxonomy

The "NLP-on-texts" false positive pattern is the dominant source of scoring error across all frameworks except Islamic ethics. The pattern occurs when a paper applies computational or NLP methods to texts from a cultural tradition without engaging that tradition's ethical framework as an analytical tool. Subcategories:

1. **Corpus linguistics** — Papers building or analyzing digital corpora of tradition-associated texts (Buddhist parallel corpus, Classical Chinese digital archives, Sanskrit text digitization)
2. **NLP benchmarks** — Papers creating language model evaluation datasets using tradition-associated texts (Chinese moral evaluation, Buddhist text comprehension)
3. **Sentiment analysis** — Papers applying sentiment analysis to tradition-associated texts (Hindu text sentiment, Quranic text analysis)
4. **Machine translation** — Papers on translating tradition-associated texts (Pali-English MT, Classical Chinese-Modern Chinese)
5. **Named entity recognition** — Papers identifying entities in tradition-associated texts (Buddhist figure extraction, Islamic legal term identification)
6. **Passing mentions** — Papers that reference a tradition in a comparative list or single sentence without substantive engagement

The distinction between *studying a tradition's texts* and *thinking with a tradition's ethics* is the key methodological insight. Islamic keywords achieve perfect precision because terms like *maqāṣid*, *fiqh*, and *ijtihād* are specific to ethical and legal reasoning, with no NLP-on-texts equivalent.

## S5.4 Full Keyword Lists

Complete keyword lists for all 7 frameworks, including exact string patterns and regex patterns used in the scoring pipeline, are provided in Supplementary Methods (S1.1).
