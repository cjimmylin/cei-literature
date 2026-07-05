---
stem: "2025-Urchs-taz2024full Analysing German Newspapers for Gender Bias and"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "n/a"
scoring_type: "mixed"
dataset_size: 1834026
dataset_construction: "scraped"
languages: ["de"]
models_tested: []
headline_numbers:
  - "Corpus contains 1,834,370 publicly available taz articles from 1980 to 2024 (p.3)"
  - "83% of all articles mention specific individuals, enabling actor-level gender analysis (p.4)"
  - "Men actors appear more frequently and are mentioned more often than women across all four decades (p.7)"
  - "Sentiment towards women actors is consistently slightly more negative than towards men across the entire 44-year period (p.7)"
  - "In 2023 analysis: 9,088 he/him vs. 8,073 she/her actors in 26,357 texts (p.11)"
---
## 1. Gist
This paper introduces taz2024full, a corpus of over 1.8 million German newspaper articles from the left-leaning Berlin daily "taz" spanning 1980–2024, making it the largest publicly available German newspaper corpus. As a proof-of-concept, the authors apply an actor-level gender bias detection pipeline to analyze 44 years of gender representation in reporting. They find persistent overrepresentation of men as subjects and slightly more negative sentiment toward women throughout the period, with gradual progress toward balance since the 2010s. For values-alignment benchmarking, this paper is relevant as an infrastructure and methodology paper demonstrating how large longitudinal corpora enable bias measurement at scale, including the design of actor-level discrimination markers applicable to evaluating model outputs.

## 2. Benchmark/eval design features
This is a dataset paper with an illustrative bias analysis, not a benchmark itself. Core contributions:
1. **Corpus**: 1,834,026 taz articles (1980–2024) with metadata (date, author, keywords, token count) in JSON, publicly available on Zenodo. No predefined train/test split — users define splits for their needs.
2. **Bias detection pipeline** (adapted from Urchs et al. 2024): NER with spaCy for person entity extraction; coreference resolution via coreferee; pronoun-based gender inference (>70% threshold for she/her or he/him); sentiment analysis with oliverguhr/german-sentiment-bert; PMI analysis of top 10 adjectives per actor; detection of generic masculine and gender-neutral language markers; feminine-coded and masculine-coded word counts per Gaucher et al. (2011).
3. **Output**: aggregated discrimination report per time period (actors by gender, mentions, sentiment scores, PMI adjectives).

## 3. Task format & example item
The corpus enables downstream NLP tasks. Sample discrimination report for 2023 (Appendix A, p.11):
```
Total Texts: 26357
Pronoun Distribution: {'he_him': 9088, 'she_her': 8073}
Total Mentions: 109634
Mentions by Pronoun: {'he_him': 60008, 'she_her': 49626}
average_sentiment_all: -0.03
sentiment_by_pronoun_she_her: -0.03
sentiment_by_pronoun_he_him: -0.02
```
No specific "items" in the benchmark sense — the corpus is a resource for research.

## 4. Scoring / grading methodology
The bias pipeline outputs quantitative discrimination markers:
- Actor counts per gender category (she/her, he/him)
- Mention counts per actor/gender
- Sentiment scores (range -1 to +1 from german-sentiment-bert)
- PMI-weighted adjective associations per gender
- Binary flags for generic masculine usage and gender-neutral language
No normative threshold for what constitutes "discriminatory" is imposed; the paper explicitly leaves interpretation to users to avoid imposing a single value system. Yearly aggregation allows diachronic comparison.

## 5. Dataset construction & provenance
- Source: "taz" (die Tageszeitung) website, crawled August–November 2024 for all publicly available articles. Permission granted for academic research; commercial use prohibited.
- Filtering: articles with more than 3 tokens retained (SoMaJo tokenizer).
- Coverage: 1980–2024; peak of 73,002 articles in 2004; declining numbers post-2007 due to paywalled content.
- Vocabulary: 6,944,197 unique tokens.
- Format: JSON with metadata and article text (title, teaser, body).
- Available at Zenodo (DOI: 10.5281/zenodo.15480855).
- Single-source limitation: taz is progressive/left-leaning; findings cannot generalize to German media broadly.

## 6. Validity evidence
- High reproducibility via public corpus and open-source pipeline (GitHub: Ognatai/corpus_pipeline).
- Limitation acknowledged: no gold standard for German gender bias detection; no comparable benchmark exists to evaluate pipeline performance.
- Co-reference resolution for German has lower accuracy than English — acknowledged as a precision risk.
- Deliberately avoided LLMs in the analysis pipeline to avoid introducing unknown model biases.
- 83% of articles contain named persons enabling actor-level analysis.
- Five articles or fewer per year before 1986 — insufficient for interpretation.

## 7. Saturation / discrimination
The 44-year span enables longitudinal discrimination analysis. Key finding: despite gradual improvement since 2010s, by 2023 he/him actors still outnumber she/her (9,088 vs. 8,073) and receive more mentions (60,008 vs. 49,626). Sentiment differences are small but persistent (she/her: -0.03, he/him: -0.02 in 2023). These near-parity numbers suggest ceiling effects may be approaching for actor count but not for mention frequency. The corpus provides strong discrimination over time periods, enabling trend detection.

## 8. Multiturn / agentic aspects
n/a — this is a static corpus and offline analysis pipeline with no interactive or agentic elements.

## 9. Key numbers
- 1,834,026 total articles (p.3)
- 1980–2024 temporal span (p.3)
- 6,944,197 unique tokens (p.4)
- 73,002 articles peak in 2004 (p.3)
- 83% of articles mention named individuals (p.4)
- Mean article length: 396.89 tokens, median 276 (p.4)
- 2023 report: 26,357 texts, 17,161 actors, 109,634 total mentions (p.11)
- 2023 gender: 9,088 he/him vs. 8,073 she/her actors (p.11)
- 2023 mentions: 60,008 he/him vs. 49,626 she/her (p.11)
- taz has 13,800 subscribers + 39,000 digital subscribers (p.3)

## 10. Pitfalls & limitations
- Single-source corpus from a progressive newspaper; not representative of German media landscape.
- Binary gender framework (she/her and he/him only); non-binary pronouns found in only 5 texts in the entire corpus — effectively excluded.
- German coreference resolution is less accurate than English, affecting gender attribution precision.
- No ground truth or evaluation metric for the bias pipeline itself; no comparable benchmark to validate against.
- Bias and discrimination are inherently subjective — pipeline outputs discrimination markers, not definitive bias labels.
- Declining article numbers post-2007 due to paywalled content reduces representativeness of recent period.
- Pipeline could be misused to curate discriminatory training datasets — authors acknowledge and warn against this.

## 11. Novel ideas worth stealing
- **Actor-level discrimination markers over entity-level**: Tracking individual named persons (nomination + predication) rather than aggregate word frequency enables more precise bias characterization — useful for benchmarking how LLMs represent specific groups.
- **PMI-based adjective attribution**: Using Pointwise Mutual Information to identify the most semantically distinctive adjectives associated with actors of each gender is a scalable, interpretable method that doesn't require labeled data.
- **Longitudinal corpus as calibration baseline**: A 44-year newspaper corpus provides a historical baseline against which model outputs could be calibrated — e.g., "does GPT-4o reflect 1990s or 2020s gender norms in its characterizations?"
- **Avoiding LLMs in bias measurement**: The explicit decision not to use LLMs in the analysis pipeline (to avoid circular bias) is a methodological principle worth building into values-alignment benchmark evaluation designs.
- **Generic masculine as a discrete marker**: The binary detection of generic masculine forms vs. gender-neutral language provides a simple, reproducible cultural/linguistic bias proxy.

## 12. Notable quotes
- "Bias and discrimination detection within corpora is inherently subjective, as no universally accepted gold standard exists." (p.8)
- "We deliberately chose not to use large language models (LLMs) for the analysis, despite known challenges with pronoun detection and co-referencing. While LLMs could potentially enhance performance, we opted against them due to concerns about the biases they may introduce and the lack of transparency in their outputs." (p.7)
- "Even in recent years, where gender representation appears almost balanced in terms of actor inclusion, men continue to receive more textual space, indicating a continued dominance in media visibility." (p.7)
- "We intentionally leave the final interpretation to human users. This allows them to apply their understanding of what constitutes discrimination in their specific use cases." (p.9)

## 13. UNKNOWN / not in extract
- Whether the corpus includes articles behind paywall or only free content post-2007
- Inter-annotator reliability for gender disambiguation in edge cases
- Exact pipeline accuracy metrics on held-out articles
- Whether the pipeline has been validated against human-coded examples
- Performance of oliverguhr/german-sentiment-bert on taz-style text specifically
- Lexicon sources for feminine-coded and masculine-coded words (only partial attribution given)
