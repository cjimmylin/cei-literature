---
stem: "2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: null
dataset_construction: "scraped"
languages: ["de", "fr", "en"]
models_tested: ["fastText (German)", "fastText (French)", "GloVe (English)", "word2vec (English)"]
headline_numbers:
  - "Origin bias detected in German (d=1.134, p<0.001) and French (d=1.29, p<0.001) word embeddings (p.9)"
  - "Career/family gender bias detected in German names (WEAT6-ger1: d=1.62, p<0.001; WEAT6-ger2: d=1.44, p=0.003) (p.9)"
  - "Historical 18th-century gender stereotypes still detectable in German word embeddings (GER-2: d=1.43, p=0.002) (p.9)"
  - "Math/Science gender bias not significant in German or French word embeddings (WEAT7-ger: p=0.65; WEAT8-ger: p=0.83) (p.9)"
---
## 1. Gist
Kurpicz-Briki (2020) extends the Word Embedding Association Test (WEAT) methodology from English to German and French pre-trained word embeddings. The paper tests whether known English gender and origin biases replicate cross-linguistically, and finds that while some biases do transfer (career/family gender bias, origin-based pleasant/unpleasant associations), others do not (math/science gender bias fails to reach significance for German and French). Crucially, the paper identifies culturally specific biases in German that have no English equivalent: gender bias in Swiss/German university subject choices, and rationality/emotionality stereotypes traceable to 18th-century gender roles. This demonstrates that bias in word embeddings is culturally inflected — a finding with direct implications for cross-lingual values-alignment benchmarks.

## 2. Benchmark/eval design features
The paper uses the WEAT (Word Embedding Association Test) as its primary measurement tool. WEAT operationalizes implicit association by measuring cosine similarity between sets of target words (e.g., male/female names, math/arts terms) and sets of attribute words (e.g., career/family terms), using a permutation test to assess statistical significance. The effect size is Cohen's d. The paper runs: (a) validation experiments on English (GloVe, word2vec) replicating Caliskan et al. 2017; (b) translated/adapted WEAT 5-8 for German (fastText) and French (fastText); and (c) two novel German-specific experiments (GER-1: university subject gender-skew, GER-2: 18th-century character attributes). Nine separate experiments for German and French are reported.

## 3. Task format & example item
Not a human-facing task; purely a computational measurement procedure applied to word embeddings. WEAT takes word vectors and computes differential associations. Example: WEAT6 tests whether male names (Peter, Daniel, Hans...) are more associated with career words (Führungskraft, Gehalt...) than female names (Maria, Anna, Ursula...), which are more associated with family words (Zuhause, Familie...). Effect size d=1.62 for German Swiss names (p.9).

## 4. Scoring / grading methodology
WEAT test statistic s(X,Y,A,B) = sum of individual word-attribute associations for target set X minus Y. Significance tested via randomization test with 100,000 iterations. Effect size: Cohen's d = (mean_X - mean_Y) / pooled_SD. Bias "detected" if p < 0.05 (following Caliskan et al. 2017 and Chaloner & Maldonado 2019). This is an automated, fully deterministic scoring procedure with no human annotation in the loop.

## 5. Dataset construction & provenance
Pre-trained word embeddings used:
- German and French: fastText embeddings (300 dimensions) trained on CommonCrawl + Wikipedia by Grave et al. 2018, available for 157 languages
- English validation: GloVe Common Crawl 840B tokens (300 dim) and Google News word2vec (300 dim)

Word lists (targets and attributes) were manually translated and adapted from the original English WEAT stimuli. German novel experiments (GER-1, GER-2) used word lists derived from Swiss federal statistics (university enrollment by gender) and Hausen (1981)'s historical dictionary analysis of 18th-century German gender roles.

## 6. Validity evidence
- English results replicate Caliskan et al. 2017 for WEAT 5-8 on both GloVe and word2vec, confirming the validity of the implementation (p.9)
- German career/family bias (WEAT6-ger1: d=1.62) replicates English career/family bias (WEAT6-ori: d=1.8/1.88 in GloVe/word2vec) with similar effect size
- The failure to detect math/science gender bias in German (WEAT7-ger: p=0.65, d=0.23; WEAT8-ger: p=0.83, d=0.11) is interpreted as culturally meaningful rather than methodological failure — these concepts may be less gender-associated in German-speaking contexts
- WEAT can only detect presence of bias, not its absence; null results must be interpreted cautiously (p.9)

## 7. Saturation / discrimination
The method is highly sensitive (all four English validation experiments significant, effect sizes 0.72–1.88). Cultural variation is substantial: German shows significant origin and career/family bias but not math/science bias; French shows origin bias but inconsistent career/family bias across name sets; novel German experiments show strong effects (d=1.43–1.74). The approach discriminates between cultures and between types of bias, though it is limited to word-level associations and cannot capture sentence-level or contextual bias.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- WEAT5-ger (origin bias, German): p<0.001, d=1.134 (p.9)
- WEAT5-fr (origin bias, French): p<0.001, d=1.29 (p.9)
- WEAT6-ger1 (career/family, Swiss German names): p<0.001, d=1.62 (p.9)
- WEAT6-ger2 (career/family, German names): p=0.003, d=1.44 (p.9)
- WEAT7-ger (math/arts, German): p=0.65, d=0.23 (not significant) (p.9)
- WEAT8-ger (science/arts, German): p=0.83, d=0.11 (not significant) (p.9)
- GER-1 (university subject gender-skew, German): p<0.001, d=1.74 (p.9)
- GER-2 (18th-century rationality/emotionality stereotypes, German): p=0.002, d=1.43 (p.9)
- WEAT6-fr1 (career/family, Swiss French names): p=0.14, d=0.75 (not significant) (p.9)
- WEAT6-fr2 (career/family, French names): p=0.03, d=1.03 (p.9)
- 100,000 randomization iterations per experiment (p.4)

## 10. Pitfalls & limitations
- Word-level WEAT cannot capture bias in contextual representations (BERT, GPT, etc.); findings apply only to static word embeddings
- Word list translation is imperfect: German and French pronoun ambiguity required dropping pronoun items (sie/sein conflict in German) that were present in English, reducing comparability
- Small word sets (8 names per group, 8 attribute words) make results sensitive to individual word choices
- Origin bias experiments use name-based proxies for ethnicity, which conflate origin with name frequency and cultural familiarity
- The paper does not study whether identified biases propagate into downstream task predictions (only embedding-level associations measured)
- Self-acknowledged limitation: WEAT detects presence but not absence of bias (p.9)

## 11. Novel ideas worth stealing
- **Culturally adapted word lists rather than direct translation**: GER-1 and GER-2 demonstrate the value of creating culture-specific evaluation items grounded in local statistical realities (Swiss university enrollment data, 18th-century German gender role vocabulary). Values benchmarks for non-English cultures should follow this pattern — adapting stimuli to local cultural norms rather than translating English items
- **Cross-language comparison as validity check**: Running the same measurement protocol in multiple languages and comparing effect sizes tests whether a bias is universal (cross-linguistic replication) or culturally specific (null result in one language). This design should be adopted for any cross-cultural values benchmark
- **Historical bias as a testable dimension**: GER-2 shows that 18th-century gender stereotypes are empirically measurable in contemporary word embeddings. Benchmarks for historical bias or anachronistic stereotypes (e.g., "does the model still associate women with irrationality?") could be constructed similarly
- **Name-based origin bias testing**: Using nationally/regionally common names from different ethnic backgrounds as WEAT targets is a practical way to test implicit origin discrimination in LM representations, applicable to any language with documented name-ethnicity associations

## 12. Notable quotes
- "Real-world bias and stereotypes from the 18th century are still included in today's word embeddings." (p.1)
- "Gender bias in German has a different form from English and there is indication that bias has cultural differences that need to be considered when analyzing texts and word embeddings in different languages." (p.1)
- "Whenever we build a system that is capable of understanding or producing natural languages (e.g. text generation, machine translation), it risks to learn the stereotypes and prejudices included in the language as well." (p.9)
- "Cultural stereotypes have already propagated to state-of-the-art artificial intelligence applications." (p.3)

## 13. UNKNOWN / not in extract
- Whether the paper was peer-reviewed or is a workshop paper (extract indicates a workshop copyright notice)
- Specific corpus size for German and French fastText embeddings
- Whether debiasing techniques were tested on German/French embeddings
- Power analysis: whether 8-item word sets are sufficient for reliable WEAT results
- The exact source and licensing of the Hausen (1981) word list used in GER-2
