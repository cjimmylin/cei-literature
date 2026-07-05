---
stem: "2024-Park-Morality is Non-Binary"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [moral-psychology, pluralism-aggregation, validity-psychometrics, normative-ethics]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 35108
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["SimCSE (supervised)", "SimCSE (unsupervised)", "SimCSE (off-the-shelf)"]
headline_numbers:
  - "Supervised SimCSE achieves clustering purity of 0.71 on MFD2.0 words (p.7)"
  - "Off-the-shelf SimCSE peaks at K=2 clusters (do's vs don'ts); supervised peaks at K=9, near MFT's 10 elements (p.7)"
  - "MFTC contains 35,108 tweets across seven domains, annotated with 10 MFT moral elements (p.2)"
  - "Training set: ~31,572 tweets (90%); test set: ~3,590 tweets (10%) (p.4)"
---
## 1. Gist
This NLP research paper from Delft University of Technology (Park, Liscio, and Murukannaiah, 2024, arXiv) builds a pluralist moral sentence embedding space using Moral Foundations Theory (MFT) and SimCSE contrastive learning. The central argument is that existing NLP approaches to morality are impoverished because they treat moral judgment as a single binary dimension (right vs. wrong), whereas pluralist moral philosophy (and MFT specifically) holds that morality comprises multiple independent foundations (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Purity/Degradation). The paper shows that (a) supervised contrastive learning can produce an embedding space where the 10 MFT elements form geometrically meaningful clusters, but (b) self-supervised approaches (and off-the-shelf pre-trained embeddings) fail to disentangle the moral foundations, collapsing to a coarse do/don't axis. The paper's practical contribution for values-alignment benchmarking is a reusable embedding space and, more importantly, a demonstration that pluralist moral structure is learnable but requires human annotation — self-supervision is insufficient.

## 2. Benchmark/eval design features
Not a benchmark paper in the primary sense; it is a representation-learning paper whose evaluation infrastructure is highly relevant. Core constructs and claims:

**Moral Foundations Theory (MFT)**: Five foundations, each with a virtue and a vice pole, yielding 10 moral elements (Table 1, p.2): Care, Harm, Fairness, Cheating, Loyalty, Betrayal, Authority, Subversion, Purity, Degradation. A text can be labeled with one or more elements, or as non-moral.

**SimCSE**: A contrastive learning framework for sentence embeddings (Gao et al., 2021). Supervised SimCSE minimizes distance between sentences with the same MFT label(s) and maximizes distance between sentences with different labels. Two negative-instance selection policies are proposed:
- *Opposite*: negative is a data point annotated with the opposite virtue/vice of the reference.
- *Outside*: negative is annotated with elements from a different MFT foundation entirely.

**Evaluation protocol**:
- *Intrinsic*: UMAP visualization and moral similarity table (mean cosine similarity between all pairs of MFT element pairs) on training set.
- *Extrinsic*: (1) Generalizability on MFTC test set; (2) consistency with Moral Foundations Dictionary 2.0 (MFD2.0) via K-means clustering (purity + silhouette) and moral similarity of dictionary words.

**Key finding**: Supervised SimCSE achieves MFD2.0 clustering purity=0.71 (K=9), compared to 0.30 (K=2) for off-the-shelf and 0.51 (K=15) for unsupervised. Virtue-virtue and vice-vice similarities are higher than virtue-vice (cross-polarity) similarities, validating the MFT structure.

## 3. Task format & example item
Not a human-facing task format. The training data consists of tweets from the MFTC with MFT labels. Example from Table 1 (p.2):

MFT Foundation definitions (verbatim):
- Care/Harm: "Support for care for others / Refrain from harming others"
- Fairness/Cheating: "Support for fairness and equality / Refrain from cheating or exploiting others"

No individual tweet examples are quoted in the extract.

## 4. Scoring / grading methodology
- **Intrinsic**: Mean cosine similarity between moral embedding representations of MFTC data points, reported as 11×11 similarity matrix (Table 3, training set; Table 4, test set).
- **Extrinsic - clustering**: K-means on MFD2.0 words; silhouette coefficient (range -1 to 1) and purity score for K=optimal and K=10.
- **Extrinsic - moral similarity on MFD2.0**: Mean cosine similarity of MFD2.0 words per MFT element pair (Table 6).

## 5. Dataset construction & provenance
- **MFTC** (Hoover et al., 2020): 35,108 tweets from seven US-centric political/social discourse domains (All Lives Matter, Baltimore Protest, Black Lives Matter, hate speech/offensive language, 2016 election, MeToo, Hurricane Sandy). Each tweet annotated by 3–8 annotators; majority vote determines final label(s); non-moral assigned when no majority.
- **Train/test split**: 90%/10% stratified by domain. Training set: ~31,572 tweets (Table 2 shows totals: 14,428 non-moral + various moral labels); test set: ~3,590 tweets.
- **MFD2.0** (Frimer, 2019): Independently created MFT dictionary used only as external validation, not training data.
- **Data and code**: Available on GitHub (https://github.com/jeongwoopark0514/morality-is-non-binary) and 4TU.ResearchData.

## 6. Validity evidence
- **UMAP visualization**: Supervised SimCSE shows clearly separable clusters for each of the 10 MFT elements (Figure 2c, p.5); unsupervised and off-the-shelf show no meaningful structure.
- **Virtue/vice separation**: The embedding space learns a clear virtue/vice axis: virtues cluster in one region, vices in another (p.5).
- **Correspondence with MFD2.0**: The supervised embedding space produces purity=0.71 on an independently created MFT lexicon — external construct validity.
- **Emergent similarities**: The model learns unexpected but theoretically meaningful cross-foundation similarities (e.g., care-purity correlation driven by religious language in Sandy hurricane tweets; betrayal-subversion correlation driven by political protest tweets), suggesting the embedding space captures contextually grounded moral associations (p.6).
- **Low inter-rater reliability on MFTC**: The paper acknowledges that annotator agreement on morality tasks is inherently low (p.8), which is an inherent limitation of the training data.

## 7. Saturation / discrimination
- The off-the-shelf and unsupervised models saturate at a do/don't binary — no discrimination among the 10 MFT elements.
- Supervised SimCSE achieves purity=0.71 (K=9) on MFD2.0 but this still leaves 29% of words misclustered, indicating substantial remaining headroom.
- The diagonal of Table 3 shows virtue-element self-similarities in the 57–81 range, vice-element self-similarities in the 47–59 range — vices are less consistently clustered than virtues (p.6).
- Non-moral tweets show modest similarities (~28–32) to all moral elements and do not cluster (p.6), as expected.

## 8. Multiturn / agentic aspects
n/a — single-sentence embedding task, no multi-turn interaction.

## 9. Key numbers
- MFTC: 35,108 tweets, 7 domains, 10 MFT elements + non-moral (p.2)
- Training set: 31,572 tweets (90% stratified); test set: 3,590 (10%) (p.4)
- MFD2.0 clustering purity: Supervised SimCSE = 0.71 (K=9), off-the-shelf = 0.30 (K=2), unsupervised = 0.51 (K=15) (p.7, Table 5)
- Supervised SimCSE silhouette (K=9): 0.15; off-the-shelf (K=2): 0.07; unsupervised (K=15): 0.04 (Table 5)
- Highest virtue-element self-similarity: Care = 81.2 (training), Purity = 79.3 (training) (Table 3, p.6)
- Lowest vice-element self-similarity: Degradation = 46.5 (Table 3)
- Non-moral self-similarity: 30.8 (Table 3)

## 10. Pitfalls & limitations
- **WEIRD bias**: MFTC is composed of English tweets about US-centric political topics; the authors explicitly flag this (p.8). The MFD2.0 validation dictionary is also WEIRD-biased.
- **Low annotator agreement**: MFTC majority voting suppresses minority moral views; the perspectivist limitation is acknowledged but not addressed in this paper (p.8).
- **Single theory, single dataset**: All experiments use MFT and MFTC; generalizability to other moral value taxonomies (Schwartz, etc.) or other corpora is not demonstrated.
- **UMAP as visualization**: The authors note that UMAP is used for visualization only; detailed geometric analysis of the full 1024-dimensional space is deferred as future work (p.8).
- **Self-supervision insufficiency**: The central finding (self-supervision fails, human labels required) is a practical barrier for extending this approach to languages and cultures without existing annotated moral datasets.
- **Dual-use risk**: The paper notes that the moral embedding space could be misused to identify and discriminate against people based on their political moral foundations (p.8).

## 11. Novel ideas worth stealing
1. **Multi-dimensional moral embedding as alternative to binary scoring**: Instead of a single right/wrong score, embed moral content into a 10-dimensional MFT space. For benchmark design, this enables detection of *which* moral foundation a scenario activates, not just whether a response is morally acceptable — a far richer signal for alignment evaluation.

2. **Virtue/vice axis as an emergent check**: The unsupervised collapse to a do/don't binary (aligning with Schramowski et al. 2022) is a useful sanity check for any moral embedding space. Benchmarks can test whether models that score well on binary moral judgment have actually learned the multi-foundation structure.

3. **Opposite vs. outside negative instance policies**: The distinction between within-foundation negatives (opposite polarity: care vs. harm) and cross-foundation negatives (outside: care vs. cheating) is a design move applicable to any contrastive moral training setup. It encodes theoretical structure into the learning objective.

4. **Moral similarity table as diagnostic tool**: The 11×11 cosine similarity matrix between MFT elements is a compact diagnostic for any trained moral embedding model. Expected pattern: high diagonal, moderate virtue-virtue and vice-vice off-diagonal, low virtue-vice, moderate non-moral. Deviations signal miscalibration.

5. **MFD2.0 as an external validation lexicon**: Using an independently constructed moral dictionary (not from the training corpus) as a consistency check is a rigorous external validity design. Benchmark designers should identify analogous external moral lexica for their target culture/language.

6. **Perspectivist future direction**: The paper flags using all individual annotator labels (rather than majority vote) as an avenue to better capture the subjective nature of moral judgment. This is a valuable direction for alignment benchmarks: model disagreement across annotators explicitly rather than collapsing to a single ground truth.

## 12. Notable quotes
- "Pluralist moral philosophers argue that human morality can be deconstructed into a finite number of elements, respecting individual differences in moral judgment." (p.1)
- "Our experiments show that a pluralist approach to morality can be captured in a sentence embedding space, but also that human labels are necessary to successfully train the embeddings. Our work represents the starting point for incorporating a pluralist approach to morality in language models, with a warning that self-supervision alone is not sufficient to capture the complexity of human morality." (p.2)
- "We notice that the supervised approach (Figure 2c) shows distinguishable clusters for each vice and virtue element, exhibiting a visible improvement when compared to the off-the-shelf model (Figure 2a). However, the unsupervised approach (Figure 2b) displays no discernible clusters." (p.5)
- "The MFTC is composed of English tweets about US-centric topics, thus perpetuating Western biases." (p.8)

## 13. UNKNOWN / not in extract
- The full appendices (Appendix A on SimCSE loss formulations, Appendix B on off-the-shelf and unsupervised similarity tables) are referenced but the extract ends at the references section — detailed numerical results for off-the-shelf and unsupervised moral similarity tables are not available.
- Exact number of MFD2.0 words used in clustering experiments.
- Computational resources and training time.
- Whether the released model weights on 4TU.ResearchData include the MFTC-trained supervised SimCSE or only code.
- Performance of the moral embedding space on downstream classification tasks (mentioned as future work in conclusions).
