---
stem: "2024-Tonneau-From Languages to Geographies Towards Evaluating Cultural Bias in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 75
dataset_construction: "scraped"
languages: ["ar", "en", "fr", "de", "id", "pt", "es", "tr"]
models_tested: []
headline_numbers:
  - "75 hate speech datasets identified across 8 languages from 143 candidates (p.3)"
  - "English represents 39% of all available HS corpora and 41% of annotated datapoints (p.4)"
  - "English dominance in share of HS datasets declined from 100% in 2016 to 39% in 2023 (p.4)"
  - "US and UK together represent the majority of English HS dataset authors (p.6)"
  - "None of surveyed English HS datasets provide both data origin and annotator origin (p.8)"
  - "66% of Spanish and 63% of Arabic datasets have partial or full data-annotator origin alignment (p.8)"
  - "Google Geocoding API precision is 92-96% across languages (p.5)"
  - "50% of identified Indonesian and 38% of identified Portuguese datasets could not be retrieved (p.4)"
---
## 1. Gist
This paper is the first systematic investigation of cultural bias in hate speech (HS) detection datasets, moving beyond language-level analysis to examine geo-cultural representation. Tonneau et al. survey 75 HS datasets across eight languages and show that English dominates but is declining in share. For three geographically widespread languages — English, Arabic, Spanish — they geocode tweet authors using Twitter metadata and find severe geo-cultural bias: English datasets are overwhelmingly US/UK-authored, Arabic datasets skew toward Jordan, and Spanish datasets toward Chile and Spain. These over-represented countries are also more economically developed, while less-developed countries with large speaker populations (India, Nigeria, Egypt, Colombia) are systematically underrepresented. The paper matters for values-alignment benchmarking because (1) hate speech perception is culturally contingent and benchmarks built on biased corpora will misrepresent non-WEIRD perspectives, and (2) the methodology for diagnosing geo-cultural representativeness is directly transferable to any NLP annotation dataset including moral judgment, values, and ethics datasets.

## 2. Benchmark/eval design features
Not a benchmark. This is a systematic empirical survey and bias audit. Core contributions:

1. **Language-level survey**: Systematic identification of 75 HS datasets across Arabic, English, French, German, Indonesian, Portuguese, Spanish, and Turkish using three source lists (Hate Speech Data Catalogue, Poletto et al. 2021 survey, Google search). Criteria: documented, publicly available or author-retrievable, focused on hate speech per UN 2019 definition.

2. **Geo-cultural bias quantification**: For English, Arabic, and Spanish (the three most Twitter-dominant languages), tweet IDs were retrieved from existing datasets and re-hydrated via Twitter API to obtain geocoordinates and self-reported user locations. These were geocoded using Google Geocoding API to infer country of origin.

3. **Representativeness benchmarking**: Country representation in HS datasets compared to three reference populations: (a) Twitter user population from Twitter Day dataset (116M English, 27M Spanish, 19M Arabic tweets on Sept 21 2022); (b) broader social media population via Facebook Ads audience measurement tool; (c) general speaker population from official statistics.

4. **Data-annotator alignment analysis**: For English, Arabic, and Spanish, the geographic origin of both the HS data and the annotators is compared using dataset documentation, revealing systematic information gaps.

## 3. Task format & example item
n/a — This is a survey/audit paper, not a benchmark with items.

## 4. Scoring / grading methodology
n/a — No model scoring. Representativeness is measured as the ratio of country share in HS datasets to country share in reference populations. The Pearson correlation between HS dataset country representation and Twitter population representation is computed per language (English: r=0.99, Spanish: r=0.43, Arabic: r=0.21, p.7). Geocoding precision is estimated through manual annotation of 50 geocoded and 50 non-geocoded samples per language (p.5).

## 5. Dataset construction & provenance
The core dataset is a survey of 75 existing HS datasets (not a new annotation effort). Of 143 candidates:
- 75 met all three criteria (documented, available, HS-focused)
- English: 29 datasets; Arabic: 12; Spanish: 7; German: 7; Turkish: 6; French: 6; Portuguese: 5; Indonesian: 3 (Table 1, p.3)

For geo-cultural analysis:
- English: tweet IDs retrieved from 9/15 Twitter datasets; 155,974 unique tweets; 50,116 with inferred country location (Table 2, p.5)
- Arabic: 6/11 datasets; 456,892 unique tweets; 247,408 with inferred location
- Spanish: 4/6 datasets; 24,752 unique tweets; 13,273 with inferred location

Code and preprocessed corpora released at https://github.com/manueltonneau/hs-survey-cultural-bias (p.2).

## 6. Validity evidence
- Geocoding evaluated by manual annotation of 50-sample random subsets per language, achieving 92-96% precision (p.5)
- Representativeness claims are triangulated against three independent reference populations (Twitter Day, Facebook Ads, official speaker statistics), with results qualitatively consistent across all three
- English-Arabic-Spanish comparison allows cross-linguistic validity check; patterns are robust across different data densities and source characteristics
- High Pearson correlation (0.99) between English HS dataset and English Twitter country representation validates that Twitter's own bias is a major driver of HS dataset bias

## 7. Saturation / discrimination
Not applicable in the standard sense. For the survey's purpose, the 75 datasets represent the available English-dominant corpus well. Key finding: coverage is sparse for under-resourced languages (Indonesian: 3 datasets; Portuguese: 5) and some datasets cannot be retrieved at all (50% of Indonesian, 38% of Portuguese), indicating significant gaps in the field.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 143 candidate datasets identified; 75 meeting criteria for 8 languages (p.3)
- English: 29 datasets (39% of total), 41% of annotated datapoints (p.4)
- English share of all HS datasets: 100% in 2016, declined to 39% by 2023 (p.4)
- Arabic Twitter-sourced: 92% of Arabic corpora; Spanish: 86%; Turkish: 83% (p.4)
- English tweets with inferred country: 50,116 representing 8% of all surveyed English posts (p.6)
- Arabic tweets with inferred country: 247,408 representing 52% (p.6)
- Spanish tweets with inferred country: 13,273 representing 27% (p.6)
- Geocoding precision: 92-96% across languages (p.5)
- Percentage of geocoded locations that could have been geocoded but were not: 12-16% (p.5)
- Pearson correlation English HS vs. Twitter population by country: r=0.99 (p.7)
- Pearson correlation Arabic HS vs. Twitter population: r=0.21 (p.7)
- 0% of surveyed English HS datasets provide both data origin and annotator origin (p.8)
- 66% of Spanish and 63% of Arabic datasets have partial or full data-annotator alignment (p.8)
- Twitter Day dataset: ~116M English, ~27M Spanish, ~19M Arabic tweets (p.5)
- Facebook Ads reference: 1.66Bn English speakers, 400Mn Spanish, 207.3Mn Arabic (Figure 3, p.6)

## 10. Pitfalls & limitations
- Analysis is restricted to Twitter; Reddit and other platforms share the same non-representativeness bias but are not analyzed
- Geographical metadata is available for only 8-52% of tweets depending on language, likely missing at non-random rates (more privacy-protective users/countries may have lower geocoding rates)
- Language and geography are imperfect proxies for culture: diaspora communities, code-mixing, and multilingual users are not captured
- Code-mixing (e.g., Hinglish in India, Pidgin in Nigeria) is excluded from analysis, potentially underestimating the diversity of English speakers from Majority World countries
- The Twitter Day reference dataset (one 24-hour period) may not be representative of longer-term Twitter demographics
- Dataset creators who did not respond to data requests are excluded, possibly biasing the retrievable sample
- Definition of "hate speech" varies across datasets; the UN 2019 definition used as inclusion criterion is broad

## 11. Novel ideas worth stealing
1. **Geo-cultural representativeness audit as a standard practice**: The paper's methodology — compare dataset author locations to multiple reference populations (platform-level, social media, general speakers) — is directly applicable to any NLP annotation dataset including moral judgment, values surveys, or ethics benchmarks. This could be operationalized as a checklist item in CEI COOKBOOK benchmark design.

2. **Language × Geography pairing**: Treating "English from Nigeria" and "English from the US" as distinct geo-cultural contexts (rather than both just "English") is a crucial reframing for any benchmark claiming cross-cultural coverage. Values-alignment benchmarks should explicitly track both language of stimulus and geographic/cultural origin of annotators.

3. **Data-annotator origin alignment matrix**: Measuring the match between data origin and annotator origin as a four-category variable (both known and aligned, partially aligned, no information) surfaces a frequently hidden source of annotation error. Applied to moral judgment datasets, this would reveal whether US-based crowdworkers are rating moral intuitions drawn from non-US cultural contexts.

4. **Temporal analysis of representation bias**: Tracking the share of datasets by language over time (Figure 2) reveals whether the field is becoming more diverse. This longitudinal lens is reusable for tracking whether values-alignment research is diversifying its geographic coverage.

5. **Seeding bias as a root cause**: The observation that country overrepresentation in Spanish and Arabic HS datasets is often intentional (country-specific keywords/seed terms) provides an actionable diagnostic. Benchmark designers should audit whether their item sourcing methods systematically favor particular geographic or cultural contexts.

6. **Multi-reference triangulation for representativeness claims**: Using three independent reference populations (platform, social media, general speakers) to validate representativeness findings reduces dependence on any single potentially biased baseline — a design principle worth adopting for cultural benchmark coverage analyses.

## 12. Notable quotes
- "Statements may be perceived as hateful in one culture but not in another, even within the same language. For instance, the term 'Paki' is used as a neutral abbreviation for Pakistani in Pakistan whereas it is a racial slur in the UK." (p.1)
- "None of the surveyed English datasets provide both pieces of information [data and annotator origin]. Specifically, the vast majority of English HS datasets report only the data source (e.g., Twitter) but no precise geographical origin." (p.8)
- "Countries with higher economic development are overrepresented in HS datasets compared to both the social media population and the general population of speakers (notably the US, UK, Australia, and Canada for English)." (p.7)
- "We advocate for more inclusive representation of different cultures in resources like HS datasets, while recognizing the limitations of language and geography as cultural proxies." (p.9)

## 13. UNKNOWN / not in extract
- The full list of 75 surveyed datasets (referenced as Appendix §A.2) is not reproduced in the extract
- Detailed geocoding evaluation results for each language (Appendix §B)
- Statistical significance tests for the geo-cultural representativeness differences
- Results for French, German, Indonesian, Portuguese, and Turkish at the geo-cultural level (only English, Arabic, and Spanish are analyzed geo-culturally)
- Whether the analysis has been replicated or updated after the Twitter API changes post-Musk acquisition
- The exact Facebook Ads Audience measurement procedure and whether it is still available
