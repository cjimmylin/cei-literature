---
stem: "2022-Yilmaz-Large-Scale Hate Speech Detection with Cross-Domain"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics, contamination-robustness]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 200000
dataset_construction: "scraped"
languages: ["en", "tr"]
models_tested: ["BERT", "BERTweet", "ConvBERT", "Megatron", "RoBERTa", "BERTurk", "ConvBERTurk", "mBERT", "XLM-R", "CNN", "LSTM", "BOW"]
headline_numbers:
  - "200,000 human-labeled tweets: 100k English + 100k Turkish, 5 hate domains each (p.1)"
  - "Krippendorff's alpha: 0.395 EN, 0.417 TR (p.3)"
  - "Best EN model (Megatron) F1: 0.830; best TR (ConvBERTurk) F1: 0.782 (p.4)"
  - "Transformers outperform conventional models by ≥5% EN, ≥10% TR (p.4)"
  - "98% of full-data performance recovered using only 20% training data in EN (p.7)"
  - "Average cross-domain recovery: 96% EN, 92% TR (p.5)"
---
## 1. Gist
This paper constructs and releases two large-scale, human-labeled hate speech detection datasets — 100,000 English and 100,000 Turkish tweets — each balanced across five hate domains (religion, gender, racism, politics, sports) with 20,000 tweets per domain. The study addresses the gap in large-scale, domain-structured hate speech resources, especially for low-resource languages. Beyond establishing performance baselines with a comprehensive model comparison (BOW, CNN, LSTM, multiple transformer variants), the paper makes two primary contributions: (1) a scalability analysis showing that BERT-class models achieve near-full performance with only 20% of training data, and (2) a systematic cross-domain transfer analysis showing that models trained on one hate domain largely generalize to others, with gender and religion as the most transferable domains and sports as the least.

## 2. Benchmark/eval design features
Each dataset contains 100,000 top-level tweets (not retweets/replies) with three-class labels: hate, offensive, and normal. Five hate domains with balanced 20,000 tweets each. Five annotators per tweet sampled from a pool of 20 (75% graduate, 25% undergraduate students; 65% female, 35% male, ages 20–26). Labels determined by majority vote; curator resolves 8% of ties. Cross-domain transfer evaluated via recovery ratio (how much target-domain performance a source-domain model recovers) and decay ratio (how much a source-domain model's performance decays on other targets). 10-fold cross-validation used throughout.

## 3. Task format & example item
Three-class tweet classification (hate / offensive / normal). Example items from Table 2 (p.3):
- Gender/Hate: "I can't live in a world where gay marriage is legal." Okay, so die.
- Race/Hate: "Türklere iyi geceler, amerikalılar gebersin" (Good night to the Turks, death to the Americans)
- Religion/Offensive: "Self proclaim atheist doesn't make you cool kid bitch"
- Politics/Offensive: "Biden your a lier and a cheat and a old idiot"

## 4. Scoring / grading methodology
Weighted precision, recall, and F1 via 10-fold cross-validation. Statistical significance tested with two-sided Mann-Whitney U test at 95% confidence with Bonferroni correction. Cross-domain experiments use "recovery ratio" M(S,T)/M(T,T) and "decay ratio" [M(S,T)-M(S,S)]/M(S,S). Scalability measured across five training data utilization ratios (20%–100%) with five repetitions each.

## 5. Dataset construction & provenance
Tweets retrieved from Twitter Full-Archive Search Premium API filtered by language, year (2020–2021), and top-level tweet type. Domain-specific keyword lists (Table 1, p.3) used for filtering; each domain balanced to exactly 20,000 tweets. Cleaning removes near-duplicate tweets (>80% cosine-TF-IDF similarity), limits per-user tweet count to ≤1% of corpus, and removes tweets shorter than 5 non-hashtag/URL/emoji words. Dataset published as tweet IDs on GitHub. Annotations collected February 15 – May 10, 2021 (84 days).

## 6. Validity evidence
Krippendorff's alpha: 0.395 EN, 0.417 TR (p.3) — higher than comparable hate speech datasets (cited: 0.38 binary, 0.153 multiclass). Curator resolves only 8% of ties (38% achieve 5-annotator consensus, 26% with 4, 28% with 3). Ablation study removing URLs, hashtags, and emojis shows essentially no effect on performance, validating content-focused modeling. Zero-shot evaluation of HateXplain and HateBERT shows poor generalization to this dataset, supporting that the corpus captures distinct signal.

## 7. Saturation / discrimination
Top transformer models reach 0.83 F1 (EN) and 0.78 F1 (TR). Normal class saturates early with training data; hate class continues improving with more data (Figure 1b, p.7). Greater class imbalance in English (7,325 hate vs. 27,593 in Turkish) explains lower hate-class performance in English. Sports domain shows highest within-domain performance but worst cross-domain generalization (avg decay >10%). Gender domain achieves near-zero decay in English — effectively transfers to all other domains.

## 8. Multiturn / agentic aspects
n/a — static single-tweet classification task.

## 9. Key numbers
- 100,000 EN tweets: 7,325 hate, 27,140 offensive, 65,535 normal (p.4)
- 100,000 TR tweets: 27,593 hate, 30,747 offensive, 41,660 normal (p.4)
- Krippendorff's alpha: 0.395 EN, 0.417 TR (p.3)
- Megatron (EN) weighted F1: 0.830; ConvBERTurk (TR) weighted F1: 0.782 (p.4)
- BOW baseline EN F1: 0.779; TR F1: 0.706 (p.4)
- 98% of full performance with 20% training data (EN); 97% (TR) (p.7)
- Average cross-domain recovery: 96% EN, 92% TR (p.5)
- Gender cross-domain recovery EN: 91% avg; decay avg: 0% (p.5–6)
- Sports cross-domain decay avg EN: -11%; TR: -15% (p.6)
- HateBERT zero-shot binary F1: 0.485 (vs. fine-tuned 0.865) (p.7)

## 10. Pitfalls & limitations
- Keyword-based tweet sampling ensures domain membership but introduces lexical biases — tweets may be classified by surface keywords rather than hate content, artificially inflating performance (acknowledged in discussion of BOW competitiveness).
- Annotators are young (ages 20–26), mostly graduate students — not diverse in age or cultural background; cultural nuance in Turkish hate speech may be underrepresented.
- Curator override system (8% of tweets) is a single person, introducing potential individual bias.
- Only two languages; Turkish hate patterns may differ from other non-Western low-resource languages.
- Scalability results show performance plateaus early, potentially indicating the task is too easy at current difficulty levels for some domains.
- No analysis of false positive rates across demographic groups.

## 11. Novel ideas worth stealing
- **Domain-balanced dataset design**: constructing exactly equal numbers of items per hate domain (5 × 20k) and per language enables systematic cross-domain transfer experiments — a model for values-alignment benchmarks covering multiple ethical domains.
- **Recovery/decay ratio framework**: the quantitative cross-domain transfer metrics (recovery and decay ratios) provide a rigorous way to measure generalization across thematic subsets of a values benchmark, useful for detecting which value dimensions are most portable.
- **Scalability curves**: systematic evaluation of model performance as a function of training data size (20%–100%) reveals diminishing returns early, informing decisions about how large a values-alignment training set needs to be.
- **Multilingual parallel construction**: building the same domain-structured dataset for two typologically different languages (English and Turkish) with parallel annotation protocols enables direct cross-lingual comparisons.
- **Near-duplicate filtering**: the 80% cosine-TF-IDF similarity threshold for deduplication and per-user tweet limits are practical contamination controls worth adopting in any web-scraped values benchmark.

## 12. Notable quotes
- "Transformer-based language models outperform conventional bag-of-words and neural models by at least 5% in English and 10% in Turkish for large-scale hate speech detection." (p.1)
- "98% of performance in English, and 97% in Turkish, are recovered when 20% of training instances are used." (p.1)
- "Gender and religion are more successful to generalize to other domains, while sports fail most." (p.1)
- "Existing models have limited generalization capability to new data. A possible reason for existing models failing to generalize can be that our dataset consists of tweets from various topics." (p.7)

## 13. UNKNOWN / not in extract
- Whether the dataset includes demographic annotation of tweet authors
- Full keyword lists in Turkish (only partial shown in Table 1)
- Error analysis broken down by hate domain
- Whether the model achieves different performance on implicit vs. explicit hate content
- Licensing terms for the released dataset
