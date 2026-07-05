---
stem: "2024-Altinok-Gender Bias in Turkish Word Embeddings"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, normative-ethics, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "scraped"
languages: ["tr"]
models_tested: []
headline_numbers:
  - "87% of vocabulary words in mC4 Turkish embeddings are masculine-associated (p.4)"
  - "Only 13% of vocabulary words are feminine-associated in web crawl corpus (p.4)"
  - "88% of words in Academic Crawl are masculine; 12% feminine (p.6)"
  - "Medical Crawl: 87% masculine, 13% feminine (p.8)"
  - "Only 11 out of 973 pronouns are categorized as feminine in mC4 (p.5)"
  - "mC4 corpus: 172.7GB, 20B words; Academic Crawl: 4.3GB, 480M words (p.3)"
---

## 1. Gist
This paper presents the first comprehensive study of gender bias in Turkish word embeddings, examining syntax, semantics, and morphology across three domains: web crawl (mC4), academic papers, and medical text. Using Floret (subword-enriched fastText) embeddings and an unsupervised gender-bias scoring method based on dot products with gendered seed words, the authors reveal pervasive masculine defaults across all domains and all grammatical categories of Turkish. The morphological dimension is novel and important: Turkish suffixes themselves can shift the gender association of a word form, making bias detection in agglutinative languages substantially more complex than in English. For values-alignment benchmarking this paper matters because it documents how deeply patriarchal social structures become encoded in the very token-level representations that LLMs build on, especially in non-Western, non-English languages.

## 2. Benchmark/eval design features
This is not a benchmark paper; it is an empirical corpus study. Core claims:
- Turkish pretrained embeddings encode strong masculine defaults across web, academic, and medical domains, regardless of the presumably neutral nature of academic/medical text.
- Syntactic categories (nouns, verbs, adjectives, adverbs, pronouns) all skew masculine; feminine words cluster around beauty, domesticity, and caregiving.
- Turkish morphology interacts with gender scoring: inflectional suffixes (especially plural "-lAr"), copular constructions, verbal negation ("-mA"), and derivational processes can flip the gender category of word forms independent of lemma gender.
- K-means clustering identifies 11 masculine topic clusters (science, technology, business, politics, arts) vs. 6 feminine clusters (family, appearance, beauty, lifestyle, domesticity).
- The study connects corpus-level findings to sociological data on Turkish patriarchy (World Economic Forum Gender Gap Report rankings).

## 3. Task format & example item
n/a — no evaluation task or scored items. The methodology is a corpus analysis: compute bias score = dot(word_vector, woman_vector − man_vector) for each vocabulary word; positive = masculine association, negative = feminine.

## 4. Scoring / grading methodology
Unsupervised gender bias scoring: for each word w, compute bias(w) = vec(w) · (vec("kadın") − vec("erkek")) where "kadın" = woman and "erkek" = man in Turkish. Positive values indicate masculine association, negative indicate feminine. No WEAT or supervised classifier used. K-means clustering with Silhouette-method cluster-count selection. spaCy pipeline trained on BOUN treebank used to evaluate embedding quality (POS accuracy, morphological accuracy, lemma accuracy, dependency parsing UAS/LAS).

## 5. Dataset construction & provenance
Three corpora used to train Floret (CBOW, dim=300, subword 2-5grams):
- mC4 (web): 172.7 GB, 20B words, from CulturaX; vocab=250K
- Academic Crawl: 4.3 GB, 480M words, from YÖK Açık Erişim and Dergipark; vocab=250K
- Medical Crawl: 178.6 MB, 20M words, from Dergipark medical journals; vocab=80K
Data cleaning applied (language filtering, PDF-to-text error correction using Qwen2-7B). All datasets publicly available on Huggingface. No license information provided in extract.

## 6. Validity evidence
Embedding quality validated against spaCy's tr_core_news_lg on BOUN treebank (test split): web-trained model achieves POS acc=0.91, morph acc=0.92, lemma acc=0.86, UAS=0.73, LAS=0.65 — matching or exceeding existing spaCy Turkish model (p.4). Academic and medical models perform slightly lower due to smaller, domain-focused vocabularies. The gender bias scoring relies on a single word-pair seed ("kadın"/"erkek"), which is a methodological limitation acknowledged implicitly. No inter-rater reliability for clustering labels; no human baseline for the bias scores.

## 7. Saturation / discrimination
The masculine skew is extreme (~87% masculine across all three corpora), leaving little discrimination: virtually the entire vocabulary is masculine by this metric. Feminine words form a small, coherent cluster around stereotypically "women's" domains. Cluster quality assessed by Silhouette score (6 feminine, 11 masculine clusters for mC4). The morphology analysis does show finer discrimination: specific suffix types (plural, copular-nominalization, passive voice) reliably shift gender associations in predictable directions, providing nuanced signal.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- mC4: 87% masculine / 13% feminine vocabulary (p.4)
- Academic Crawl: 88% masculine / 12% feminine (p.6)
- Medical Crawl: 87% masculine / 13% feminine (p.8)
- Only 11 of 973 pronouns feminine in mC4 (p.5)
- 6 feminine vs. 11 masculine semantic clusters in mC4 (p.5)
- mC4: 172.7 GB, 20B words; Academic: 4.3 GB, 480M words; Medical: 178.6 MB, 20M words (p.3)
- Web model: POS acc 0.91, morph acc 0.92, lemma acc 0.86 (p.4)
- Turkey ranked 127th out of 145 in WEF Global Gender Gap Report 2024 (p.5)
- Plural suffix "-lAr" converts ~50% of masculine lemma plurals toward feminine category (p.10, Figure 6)
- Passive voice suffix reliably converts masculine verbs to feminine (p.11)

## 10. Pitfalls & limitations
- Single-axis gender measurement (masculine/feminine binary) does not capture non-binary identities or intersectional identities.
- Gender bias score relies solely on a single seed pair ("kadın"/"erkek"); no WEAT-style robustness check or multiple seed words.
- Unsupervised approach means no ground-truth labels for "correct" gendering; impossible to distinguish true societal bias from legitimate linguistic gender marking.
- Clustering analysis (K-means) is exploratory only; no significance testing for cluster topic labels.
- No comparison to LLM-level bias (only static word vectors); findings may not transfer directly to transformer-based language models.
- Academic and Medical domains use smaller corpora, so the apparent similarity in bias ratios to web may partly reflect domain vocabulary constraints rather than comparable bias intensity.
- No downstream task evaluation demonstrating harm from the measured bias.

## 11. Novel ideas worth stealing
1. **Morphology-aware bias scoring**: For agglutinative languages (Turkish, Finnish, Hungarian, Swahili), suffix-level gender analysis is essential. A values-alignment benchmark should include morphologically complex test items where a word's social valence shifts with inflection.
2. **Domain-stratified embedding training**: Testing bias across web/academic/medical domains reveals that "neutral" domains (academia, medicine) are almost as biased as general web data — a sobering check for benchmarks that assume domain filtering removes bias.
3. **Suffix-type taxonomy of gender shifts**: Cataloguing which suffix categories (plural, passive, copular, derivational) reliably change gender associations provides a principled way to generate hard negatives for a gender-bias test suite in morphologically rich languages.
4. **Cluster-level semantic audit**: Using K-means + Silhouette on gendered word groups and naming the resulting topic clusters is a low-cost, interpretable way to document what domains are masculine/feminine-coded in a target culture — useful for constructing culturally specific stereotype items.
5. **Connecting corpus findings to sociological context**: The paper's grounding in WEF gender gap data and sociology of patriarchy in Turkey models how benchmark papers should anchor empirical NLP findings to real-world validity anchors.

## 12. Notable quotes
- "87% of the vocabulary words in our word vectors are associated with men, while only 13% are associated with women." (p.4)
- "The masculine clusters encompass various 'serious societal matters', such as science and technology, arts and music, business, economy, and politics. In contrast, the feminine clusters associated with family, appearance, beauty, lifestyle, and domesticity reinforce cultural expectations for women to be 'submissive' and 'passive'." (p.5)
- "The passive voice changes masculine verbs into feminine verbs, but not the other way around. We attribute this to the societal perception of females being associated with passive roles." (p.11)
- "These findings raise concerns about the amplification of gender biases in AI and society through social, cultural, and digital mechanisms." (p.12)

## 13. UNKNOWN / not in extract
- Exact Silhouette scores for the K-means clustering are not reported numerically.
- Licensing terms for the released datasets and models are not stated.
- No information about whether the embeddings were tested in any downstream NLP application.
- The 108 hours of Qwen2-7B processing mentioned for Academic Crawl cleaning: unclear what fraction of data was removed.
- No comparison to English or other language gender bias benchmarks (e.g., WEAT scores for Turkish).
