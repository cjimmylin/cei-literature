---
stem: "2024-University-Using LLMs to Discover Emerging Coded"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, contamination-robustness, design-space]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 659
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["BERT (fine-tuned)"]
headline_numbers:
  - "Best pipeline (tfidf-posttrunc): accuracy 0.80, F-score 0.72 (p.9)"
  - "Standard colloc pipeline: recall 1.0 on 7 truly antisemitic terms; tfidf extracted 94 terms, 29 truly antisemitic (p.8)"
  - "BERT vocabulary extended from 30k to 55k tokens via fine-tuning on 56K additional posts (p.6)"
---
## 1. Gist
This paper presents a pipeline for automatically discovering emerging coded antisemitic terminology in extremist social media posts. Coded language uses terms that carry dual meanings — innocent on the surface, antisemitic in context — and evolves rapidly, quickly outpacing static glossaries. The authors propose and evaluate four pipeline variants combining two trending-term extraction methods (concordance/collocation vs. TF-IDF+frequency) with two embedding strategies (pre-truncate vs. post-truncate BERT embeddings). A gold standard was constructed from existing antisemitic glossaries plus manual internet verification. The best pipeline achieves 80% accuracy and 72% F-score. This work is directly relevant to values-alignment benchmarking: it shows how coded language systematically evades safety evaluations, and proposes methods to surface it automatically — a model for how benchmark contamination can be detected and remedied.

## 2. Benchmark/eval design features
Not a benchmark but an NLP pipeline for coded hate-speech discovery. Core methodological contributions: (1) Phase 1 — extract trending terms using either concordance+collocation (NLTK, 52 terms after filtering) or TF-IDF+frequency (94 terms after filtering); (2) removal strategy — strip redundant bigrams-within-trigrams, remove known seed words, remove terms containing overt Jewish references (jew, jewish, kike, zionist); (3) Phase 2 — compare trending term embeddings to seed term embeddings via cosine similarity using fine-tuned BERT, with majority-vote across 10 window sizes; (4) gold standard: known-term glossary lookup + manual Google verification for new terms. Four pipeline variants: standard/standard, standard/advanced, advanced/standard, advanced/advanced.

## 3. Task format & example item
Not a prompt-based eval. Example post used in sanity check for "Deep State" (Known Term, 4chan platform): "US deep state MIGApede detected. The real deep state is the Jewish lobby." (p.9)

## 4. Scoring / grading methodology
Accuracy, Precision, Recall, F-score against gold standard labels. Gold standard built from three glossaries (ICS Historical Glossary, AJC Translate Hate, R2Pris) plus manual internet search for new terms. Known terms verified by glossary lookup; new terms verified by examining Google search results for antisemitic associations (p.7–8). Threshold for antisemitic label: cosine similarity greater than median across seed terms, for majority of window sizes (m=7 for pre-truncate, m=9 for post-truncate).

## 5. Dataset construction & provenance
659 posts retrieved from Disqus, Telegram, Minds, and GETTR using 16 seed expressions from AJC Glossary and SPLC (subset of 46 AJC expressions available at time of study). Data collection via Pyrra commercial software. 14 seed words retained after filtering (Jew Down and Cosmopolitan Elite dropped for <5 posts). Additional 56K posts scraped for BERT fine-tuning (p.6). No explicit train/test split described; evaluation uses the 659-post corpus.

## 6. Validity evidence
Quantitative evaluation against a carefully constructed gold standard (p.7–8). Qualitative sanity checks: authors inspected posts containing extracted terms to verify antisemitic usage in context (Table III, p.9). "Neutral (in an antisemitic context)" category introduced to handle false positives that appear in antisemitic contexts but are not themselves antisemitic (e.g., "End game," "Big Part"). No human inter-rater reliability statistics reported. The gold standard construction process is systematic but manual.

## 7. Saturation / discrimination
Of 94 tfidf-extracted trending terms, only 29 (31%) were truly antisemitic — precision challenge is real. Standard colloc pipeline achieved perfect recall on 7 antisemitic terms but very low precision (0.34). Advanced tfidf+posttrunc pipeline achieved best balance: precision 0.63, recall 0.83, F-score 0.72 (p.8). The approach demonstrates that automated discovery does surface known-but-missed terms as well as genuinely new ones.

## 8. Multiturn / agentic aspects
n/a — the system is a static batch pipeline.

## 9. Key numbers
- 659 posts in corpus; 16 seed expressions; 14 retained (p.3–4)
- 56K additional posts for BERT fine-tuning; vocabulary extended 30k→55k tokens (p.6)
- Standard (colloc) pipeline after filtering: 52 trending terms, 7 truly antisemitic (p.8)
- Advanced (tfidf) pipeline after filtering: 94 trending terms, 29 truly antisemitic (p.8)
- Best pipeline (tfidf-posttrunc): accuracy=0.80, precision=0.63, recall=0.83, F=0.72 (p.9)
- Colloc-pretrunc: accuracy=0.74, recall=1.0, F=0.51 (p.8)
- Optimal majority-vote threshold: m=7 (pre-truncate), m=9 (post-truncate) (p.6–7)

## 10. Pitfalls & limitations
- Small dataset (659 posts) limits generalizability.
- Only 14 seed expressions; many known antisemitic terms not included, possibly missing whole sub-domains.
- Precision remains low even for best pipeline (0.63); human vetting still required.
- Gold standard for new terms relies on Google search — subjective and potentially inconsistent.
- Post-processing step to remove "obviously Jewish" terms (jew, jewish, kike, zionist) may discard useful signal and assumes clear demarcation that may not hold.
- Unigrams were excluded from analysis due to difficulty filtering them — potentially missing important signals.
- No temporal validation — the system was not tested in a truly streaming setting.

## 11. Novel ideas worth stealing
- **Coded-term discovery pipeline as benchmark maintenance tool**: the hypothesis "coded antisemitic terminology begets coded antisemitic terminology" implies a structural principle — if an LLM learns to evade one safety constraint through coded language, it will generate nearby coded terms. The pipeline could be applied to model outputs to discover new evasion strategies.
- **Two-phase extraction + semantic similarity to seed set**: separating trending-term extraction from semantic-antisemitism filtering is a modular design that allows swapping components. Benchmark designers could use the same architecture to continuously update a "coded harmful language" vocabulary.
- **Majority-vote across window sizes**: averaging cosine similarity labels across multiple context window sizes provides a robust signal that is less sensitive to any single context length — a noise-reduction technique applicable to LLM-judge scoring across prompt variants.
- **"Neutral in antisemitic context" category**: formally distinguishing between terms that are incorrect predictions vs. terms that are contextually harmful but not intrinsically hateful is a nuanced validity category useful in harm evaluation rubrics.
- **Gold standard from multiple glossary sources + manual verification**: the tiered gold-standard construction (known glossary entries + manual verification of new terms) is a transferable protocol for building human-validated labels for novel harmful content.

## 12. Notable quotes
- "Coded terminology evolves rapidly online and fixed glossaries such as the AJC glossary become quickly outdated." (p.2)
- "The methodology is based on the hypothesis that coded antisemitic terminology begets coded antisemitic terminology." (p.2)
- "Future work will attempt to improve all these metrics scores, with a focus on precision so as not to unduly label terms as antisemitic when they are, in fact, benign." (p.8)
- "After being vetted by a human team, the emergent coded terminology it discovers could be input to the moderating algorithms used by social media platforms to discover problematic discourse or users currently avoiding discovery." (p.8)

## 13. UNKNOWN / not in extract
- Exact number of unique users in the corpus.
- Whether the 659 posts are balanced across platforms.
- Licensing or ethics approval for use of scraped data.
- Inter-rater reliability statistics for the gold standard construction.
- Performance broken down by seed expression category.
