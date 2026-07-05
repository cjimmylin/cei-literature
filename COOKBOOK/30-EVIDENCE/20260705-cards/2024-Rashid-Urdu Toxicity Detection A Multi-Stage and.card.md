---
stem: "2024-Rashid-Urdu Toxicity Detection A Multi-Stage and"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 72000
dataset_construction: "scraped"
languages: ["ur"]
models_tested: []
headline_numbers: ["95% F1-score with data augmentation techniques (abstract)"]
---
## 1. Gist
This paper presents the Urdu Toxicity Corpus (UTC), a large-scale multilabel dataset of over 72,000 Roman Urdu social media comments annotated for multiple toxicity categories. It proposes a multi-stage, multi-label classification pipeline and demonstrates strong performance using data augmentation. The work matters for values-alignment benchmarking because it addresses a major gap: the near-total absence of safety evaluation infrastructure for Urdu and Roman script languages, which are used by hundreds of millions of speakers primarily in South Asia.

## 2. Benchmark/eval design features
The paper constructs a multilabel toxicity detection benchmark covering several toxicity subcategories (exact category labels unknown from metadata alone). The corpus is drawn from Roman Urdu social media comments — a code-mixed script form in which Urdu is written in Latin characters rather than Nastaliq. The multi-stage classification approach appears to first detect toxicity presence and then classify type. Data augmentation techniques are employed to address class imbalance and improve coverage.

## 3. Task format & example item
Full text unavailable. Task is classifier-based toxicity detection on Roman Urdu social media text; specific example items and item format details are not determinable from metadata alone.

## 4. Scoring / grading methodology
F1-score reported as the primary metric (95% with data augmentation). Multi-label classification scoring implies per-category F1 in addition to macro/micro aggregates, but breakdown is not available from metadata.

## 5. Dataset construction & provenance
Over 72,000 Roman Urdu comments scraped from social media platforms. Annotation process, annotator details, inter-annotator agreement, and licensing information are not available from metadata. Data augmentation was applied to address class imbalance.

## 6. Validity evidence
Not determinable from metadata. Full text unavailable.

## 7. Saturation / discrimination
Not determinable from metadata. The 95% F1 figure suggests possible ceiling effects, but without per-class breakdowns or difficulty analyses this cannot be assessed.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 72,000+ Roman Urdu social media comments in corpus (abstract)
- 95% F1-score with data augmentation (abstract)

## 10. Pitfalls & limitations
- Author-admitted limitations unknown (full text unavailable).
- Roman Urdu (Latin script) may not generalize to Nastaliq-script Urdu NLP systems.
- Metadata does not clarify inter-annotator agreement, which is critical for toxicity annotation quality.
- Abstract origin of 95% F1 figure means it may refer to a best-condition result, not average performance.

## 11. Novel ideas worth stealing
- Multilabel toxicity taxonomy for a low-resource language: designing a benchmark that simultaneously captures multiple harm types (rather than binary toxic/non-toxic) is directly applicable to values-alignment evals that need to distinguish harm subcategories.
- Multi-stage pipeline design: separating detection (is this toxic?) from classification (what kind?) allows finer-grained safety evaluation and could be adopted in LLM output safety benchmarks.
- Roman script coverage: building safety evals for code-mixed or transliterated script forms is an underexplored design space relevant to multilingual LLM deployment.

## 12. Notable quotes
Full text unavailable; no verbatim quotes can be provided.

## 13. UNKNOWN / not in extract
- Exact toxicity category taxonomy (labels and definitions)
- Annotation protocol and inter-annotator agreement statistics
- Train/validation/test split sizes
- Licensing and data availability details
- Which models were tested and full performance breakdown
- Data augmentation method details
- Full text unavailable
