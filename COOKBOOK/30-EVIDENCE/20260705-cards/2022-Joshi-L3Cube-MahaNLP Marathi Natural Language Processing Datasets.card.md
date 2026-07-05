---
stem: "2022-Joshi-L3Cube-MahaNLP Marathi Natural Language Processing Datasets"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space]
task_format: "classifier"
scoring_type: "exact-match"
dataset_size: 25000
dataset_construction: "crowdsourced"
languages: ["mr"]
models_tested: ["MahaBERT", "MahaRoBERTa", "MahaAlBERT", "multilingual-BERT", "XLM-R", "IndicBERT"]
headline_numbers:
  - "MahaCorpus: 24.8M sentences and 289M tokens; total 752M tokens with other public resources (p.2)"
  - "MahaSent: 12,114 train, 2,250 test, 1,500 validation examples for sentiment analysis (p.3)"
  - "MahaNER: 25,000 manually tagged sentences, 8 entity classes (p.3)"
  - "MahaHate: 25,000+ tweets, 4 classes (hate, offensive, profane, not) (p.4)"
---
## 1. Gist
L3Cube-MahaNLP is a resource paper introducing a suite of NLP datasets and pre-trained models for Marathi, the third most spoken language in India (~83 million speakers) that has historically lacked NLP resources. The paper presents MahaCorpus (large unlabeled corpus), MahaBERT/MahaRoBERTa/MahaAlBERT (monolingual BERT variants), MahaSent (sentiment analysis), MahaNER (named entity recognition), and MahaHate (hate speech detection). For values-alignment benchmarking, this paper is relevant primarily as a demonstration that low-resource non-English languages remain severely underserved in NLP evaluation infrastructure, and that culturally specific hate speech detection for underrepresented languages requires purpose-built datasets. It is not itself a values-alignment benchmark but provides the building blocks (particularly MahaHate) that could support one.

## 2. Benchmark/eval design features
The paper presents several supervised task datasets:
- **MahaSent**: Marathi tweet sentiment analysis with 3 classes (positive, negative, neutral); supports 2-way and 3-way classification.
- **MahaNER**: Gold-standard NER with 8 entity classes (persons, organizations, locations, time, measure, dates, designations, other); IOB and non-IOB notation.
- **MahaHate**: Hate speech detection with 4 classes (hate, offensive, profane, not); supports 2-way (hate/non-hate) and 4-way classification.

All datasets curated from real social media data (Twitter primarily) with manual annotation. The paper positions these as production-quality datasets rather than small academic benchmarks.

## 3. Task format & example item
n/a — no example items are provided in the extract. All tasks are text classification of Marathi social media posts.

## 4. Scoring / grading methodology
Not explicitly described in the extract. Models are released and evaluated on downstream classification tasks using standard precision/recall/F1 metrics based on referenced companion papers (Velankar et al. 2022 for hate speech, Litake et al. 2022 for NER). Models available via HuggingFace with 2-way and 4-way classification variants.

## 5. Dataset construction & provenance
- **MahaCorpus**: Scraped from internet (news and non-news sources); 24.8M sentences, 289M tokens, combined with public resources for 752M total tokens.
- **MahaSent**: Marathi tweets, 12,114 train / 2,250 test / 1,500 validation.
- **MahaNER**: 25,000 manually tagged sentences, 21,500 train / 2,000 test / 1,500 validation.
- **MahaHate**: 25,000+ tweets, 21,500 train / 2,000 test / 1,500 validation; curated from Twitter, manually annotated.
- Annotation details (annotator count, IAA) are not provided in this overview paper; see companion papers.
- All resources publicly released at https://github.com/l3cube-pune/MarathiNLP and HuggingFace model hub.

## 6. Validity evidence
Not reported in this paper; referenced to companion papers (Velankar et al. 2022 for hate speech, Litake et al. 2022 for NER). The paper claims monolingual MahaBERT models outperform multilingual alternatives (multilingual-BERT, XLM-R, IndicBERT) on downstream tasks, but numeric results are not reproduced in this overview paper.

## 7. Saturation / discrimination
Not reported in this overview paper.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- MahaCorpus: 24.8M sentences, 289M tokens from L3Cube; 752M total with public data (p.2)
- MahaSent train/test/val: 12,114 / 2,250 / 1,500 (p.3)
- MahaNER: 25,000 sentences, 8 entity classes; 21,500 / 2,000 / 1,500 split (p.3)
- MahaHate: 25,000+ tweets, 4 classes; 21,500 / 2,000 / 1,500 split (p.4)
- Marathi speakers: ~83 million (p.1)

## 10. Pitfalls & limitations
- **Thin overview paper**: 6 pages total; actual experimental details, annotation procedures, and model performance numbers are deferred entirely to companion papers.
- **No inter-annotator agreement reported** in this paper; annotation quality details unknown without reading companion papers.
- **Twitter-centric**: Both MahaSent and MahaHate are Twitter-derived, potentially limiting generalizability to other Marathi language contexts.
- **No cross-lingual evaluation**: No assessment of whether models trained on Marathi data transfer to related languages (e.g., Hindi, Bengali).
- **Hate speech taxonomy breadth**: 4-class hate speech scheme (hate/offensive/profane/not) is coarser than datasets like KOLD; limited target group identification.
- **Data skew**: Hate speech is rare in natural data; the 21,500 training samples likely have significant class imbalance.

## 11. Novel ideas worth stealing
1. **Parallel release of corpus + BERT variants + task datasets** as a unified NLP ecosystem — a good model for creating language-specific evaluation infrastructure in underrepresented languages, including non-Western languages relevant for values-alignment benchmarking.
2. **Production-quality vs. benchmark-quality distinction**: The paper explicitly aims to move beyond small academic benchmark datasets toward datasets usable in production systems — a useful framing for values-alignment benchmarks that aspire to real-world applicability.
3. **Monolingual models outperform multilingual**: The finding (from companion papers) that language-specific BERT models beat multilingual alternatives on Marathi tasks reinforces the need for language-specific resources in cultural values benchmarking.

## 12. Notable quotes
- "Despite being the third most popular language in India, the Marathi language lacks useful NLP resources." (p.1)
- "Another objective of this work is to move away from small benchmark datasets which may help advance the state of the art but are not normally useful in production." (p.2)
- "The monolingual Marathi models released in this work have been shown to work better than the currently available alternatives." (p.4)

## 13. UNKNOWN / not in extract
- Actual model performance numbers (F1, accuracy) on MahaSent, MahaNER, MahaHate — deferred to companion papers
- Annotation methodology details (annotator count, IAA, guidelines) — not in this overview paper
- Whether MahaHate includes target group identification or only offense-level labels
- License terms for the released datasets and models
- Details of the MahaGPT model evaluation
- Whether the datasets are balanced or class-imbalanced and by how much
