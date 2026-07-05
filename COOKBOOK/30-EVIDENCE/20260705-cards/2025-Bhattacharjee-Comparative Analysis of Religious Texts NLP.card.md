---
stem: "2025-Bhattacharjee-Comparative Analysis of Religious Texts NLP"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, normative-ethics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Bible vs Quran pair had the highest cosine similarity (0.8980) vs Bible vs Gita (0.7278) and Gita vs Quran (0.7757) (p.7)"
  - "Bible vs Quran FID distance was lowest at 0.1664, indicating closest distribution (p.7)"
  - "The Gita has a higher percentage of positively classified verses under VADER; Bible and Quran have higher neutral percentages (p.7)"
  - "KMeans centroid cosine similarity: Bible vs Quran 0.7035, Gita vs Quran 0.6226, Bible vs Gita 0.5423 (p.8)"
---
## 1. Gist
This 10-page conference paper (COLING 2025 workshop on Computational Linguistics for Religious Texts) applies NLP techniques — LDA topic modelling, GloVe and Sentence Transformer embeddings, VADER sentiment analysis, and corpus distance metrics (FID, cosine similarity, KMeans centroid distance) — to compare the Bible, Quran, and Bhagavad Gita in English translation. For values-alignment benchmarking, the paper is relevant as a methodological demonstration of how to computationally characterise the thematic and emotional content of religious texts, which are primary sources for religious-values benchmarks. It reveals that the Quran and Bible cluster more closely together (both Abrahamic) than either does with the Gita, suggesting that NLP-derived religious-text representations track broad theological family structure.

## 2. Benchmark/eval design features
This is an applied NLP analysis paper, not a benchmark. Core methods:
- **Word frequency analysis:** Top-20 most frequent content words per text after stopword removal, visualised as bar plots.
- **LDA topic modelling:** 10 topics extracted per text, each represented by 10 keywords.
- **Cross-text topic comparison:** Topic embeddings constructed by concatenating LDA keyword lists, then encoded with GloVe (100-d) and SentenceTransformer (paraphrase-MiniLM-L6-v2). Pairwise cosine similarity between all topic pairs shown in heatmaps.
- **VADER sentiment analysis:** Verse-level sentiment scores (positive/negative/neutral) aggregated per text.
- **Corpus distance:** (a) FID via IBM CompCor using STTokenizerEmbedder; (b) average cosine similarity of corpus-level embeddings; (c) KMeans (k=5) on embeddings with centroid-pair cosine similarity and Euclidean distance.

Key findings: Bible and Quran share strongest thematic and distributional overlap; Bhagavad Gita is more distinct. The Gita is more positively-valenced lexically (VADER), while the Bible and Quran have more neutral verses. Topic keywords suggest distinct cultural focuses: the Gita emphasises philosophical dialogue (duty, soul, Krishna, Arjuna); the Bible emphasises covenant/narrative; the Quran emphasises faith/eschatology.

## 3. Task format & example item
n/a — no benchmark items. The closest to a task is the pairwise topic similarity heatmaps showing which LDA topics across texts are semantically closest, e.g., "Gita Topic 6 and Bible Topic 6: life, wisdom, brother — emphasising spirituality and love" (p.6-7).

## 4. Scoring / grading methodology
n/a — descriptive analysis. Metrics used are: cosine similarity (0 to 1), FID distance (lower = more similar), Euclidean distance (lower = more similar). No ground-truth labels; no classifier trained.

## 5. Dataset construction & provenance
- Texts: English translations of the Bible, Quran, and Bhagavad Gita (specific translation versions not stated in extract).
- Preprocessing: lowercase, punctuation removal, stopword filtering, tokenisation.
- No size figures given for the corpora themselves; the Bhagavad Gita is much shorter (~700 verses) than the Bible or Quran.
- Licensing: no mention; all texts are in public domain in English translation.
- The paper does not report which specific translations were used, a notable limitation for reproducibility.

## 6. Validity evidence
The paper does not formally validate its methods against expert theological judgements or inter-rater reliability. The NLP findings broadly align with prior scholarship: Abrahamic texts (Bible, Quran) clustering together is theologically intuitive. One explicit validity caveat is noted: "the sentiment scores do not represent the moral positive or negative sentiment, but rather the use of positive or negative words, regardless of the context they are used in" (p.7).

## 7. Saturation / discrimination
The analysis reveals the Gita as distinctly more positive in VADER sentiment and more distant from the Abrahamic pair on all corpus-distance metrics. However, all pairwise cosine similarities are relatively high (0.73–0.90), suggesting that high-level embedding models may not discriminate well between very different religious traditions at the corpus level.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Top word in Bhagavad Gita: "arjuna" (119 occurrences) (p.4)
- Top word in Bible: "give" (8,847 occurrences); "lord" (7,887) (p.4)
- Top word in Quran: "allah" (2,833 occurrences) (p.4)
- Cosine similarity (averaged embeddings): Bible vs Quran 0.8980; Bible vs Gita 0.7278; Gita vs Quran 0.7757 (p.7-8)
- FID distance: Bible vs Quran 0.1664 (closest); Bible vs Gita 0.3868; Gita vs Quran 0.3801 (p.7)
- KMeans centroid cosine: Bible vs Quran 0.7035; Gita vs Quran 0.6226; Bible vs Gita 0.5423 (p.8)
- KMeans centroid Euclidean: Bible vs Quran 0.4170 (closest); Gita vs Quran 0.4911; Bible vs Gita 0.5284 (p.8)
- LDA extracted 10 topics per text, each represented by 10 keywords (p.3)
- Initial literature search: not stated; 40 studies mentioned in Bolatbek (wrong paper)

## 10. Pitfalls & limitations
- VADER was designed for social media microtext; applying it to ancient religious scripture introduces systematic bias — the paper explicitly acknowledges sentiment scores reflect word polarity rather than moral valence (p.7)
- English translations introduce translator bias; different translations of the same text would produce different NLP results; translation versions are not specified
- LDA topic coherence is not formally evaluated (no coherence scores reported)
- k=5 for KMeans is arbitrary; no cluster validity analysis
- Only three religious traditions represented; inter-faith variation is vast (Islam, Christianity, Hinduism together cover ~5 billion people but many internal traditions)
- The paper conflates "scripture" with its English translation, which is culturally and linguistically a distinct artefact

## 11. Novel ideas worth stealing
1. **Corpus-level embedding distance as a proxy for theological distance:** The FID and centroid-cosine metrics could be applied to any set of value-laden texts (e.g., AI ethics frameworks, national constitutions, religious legal codes) to map their pairwise semantic proximity — useful for identifying gaps in coverage when building a values benchmark.

2. **VADER as a fast screen for emotional valence in religious/normative text:** Despite its limitations, VADER provides a quick distributional look at positive/negative/neutral word use across corpora. Benchmark designers could use this as a preliminary filter to assess whether training data or test items are emotionally lopsided.

3. **LDA topic keyword sets as seed vocabulary for item generation:** The 10-keyword LDA topics extracted from each tradition (duty, soul, wisdom, battle, divine for Gita; covenant, kingdom, prophets, faith, law for Bible; mercy, believers, guidance, prophet, judgment for Quran) could serve as culturally grounded seed vocabularies for generating benchmark items targeting specific theological concepts.

4. **Cross-tradition topic alignment heatmaps:** The GloVe/SentenceTransformer similarity heatmaps showing which topics across traditions are closest could be used to identify *shared moral concepts* (e.g., righteousness, duty, divine judgment appear across all three) versus *tradition-specific* concepts — structuring a benchmark around the shared vs. unique distinction.

## 12. Notable quotes
- "Analyzing these texts with advanced methods can help improve our understanding of their significance and the similarities or differences between them." (p.1)
- "The findings reveal unique and shared themes and sentiment patterns across the Bible, the Quran, and the Bhagavad Gita, offering new perspectives in computational religious studies." (p.1)
- "The sentiment values obtained using VADER are also not representative of the moral sentiment of the verses in the text, but only based on the polarity of the words in them." (p.8)
- "The strongest overlap is between Gita Topic 6 and Bible Topic 6, which emphasize spirituality and love through terms such as 'life,' 'wisdom,' and 'brother.'" (p.6-7)

## 13. UNKNOWN / not in extract
- Specific English translation versions used for each of the three texts
- Total verse/sentence counts for each corpus
- LDA hyperparameters (number of passes, alpha, beta)
- Whether results are reproducible (code/data not mentioned as released)
- Any statistical significance testing for the similarity/distance scores
- Whether any non-English translations were considered (the paper uses only English)
