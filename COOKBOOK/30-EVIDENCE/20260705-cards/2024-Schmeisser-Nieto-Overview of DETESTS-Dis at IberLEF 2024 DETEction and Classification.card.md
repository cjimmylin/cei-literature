---
stem: "2024-Schmeisser-Nieto-Overview of DETESTS-Dis at IberLEF 2024 DETEction and Classification"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, contamination-robustness]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 12111
dataset_construction: "scraped"
languages: ["es"]
models_tested: []
headline_numbers: []
---
## 1. Gist
DETESTS-Dis is a shared task at IberLEF 2024 focused on detecting and classifying explicit and implicit racial stereotypes in Spanish-language social media and news comments, with a distinctive "learning with disagreement" design. The dataset covers 12,111 sentences from tweets and immigration-related news comments, and the task framework explicitly models annotator disagreement rather than forcing a single ground-truth label. This is highly relevant to values-alignment benchmarking because racial stereotype detection in Spanish is underrepresented, and the disagreement-aware methodology offers a more realistic account of how value judgments vary across human raters.

## 2. Benchmark/eval design features
The benchmark involves detecting whether text contains racial stereotypes (binary or multi-class) and classifying whether they are explicit or implicit. The "learning with disagreement" component is the key design innovation: rather than resolving annotator disagreements to a single label, the task preserves the distribution of annotations. This allows models to be trained and evaluated on soft or distributional labels, better capturing the inherently contested nature of stereotype identification. Dataset covers immigration-related content and racial hoaxes in Spanish social media and news.

## 3. Task format & example item
Full text unavailable. Task involves classifying Spanish-language sentences as containing racial stereotypes (explicit or implicit) or not. Specific example items are not available from metadata.

## 4. Scoring / grading methodology
Shared task scoring; specific metrics not determinable from metadata. Likely includes standard classification metrics (F1, accuracy) adapted for soft-label or distribution-based evaluation given the disagreement focus.

## 5. Dataset construction & provenance
- 12,111 sentences from Spanish Twitter and immigration/racial-hoax news comments.
- Annotated with multiple annotators; disagreement explicitly retained rather than resolved.
- Dataset URL: https://detests-dis.github.io/
- Licensing and exact annotation protocol details not available from metadata alone.

## 6. Validity evidence
Learning-with-disagreement design implicitly acknowledges and preserves inter-annotator disagreement, which is itself a form of validity evidence about the contested nature of stereotype judgments. Quantitative reliability statistics not available from metadata.

## 7. Saturation / discrimination
Not determinable from metadata.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 12,111 sentences in corpus (abstract)
- Dataset covers tweets and news comments related to immigration and racial hoaxes in Spanish (abstract)

## 10. Pitfalls & limitations
- Full text unavailable; specific system results and findings unknown.
- Spanish-only scope limits cross-lingual generalization.
- Implicit stereotype detection is notoriously difficult and subjective; the disagreement design acknowledges this but doesn't resolve it.
- Single author listed in metadata (authors_incomplete: true) — full authorship unknown.

## 11. Novel ideas worth stealing
- Learning with disagreement as a first-class design principle: instead of forcing consensus labels, retain annotator distributions and evaluate model predictions against the full distribution. This is directly reusable in values-alignment benchmarks where moral judgments are legitimately contested.
- Explicit/implicit stereotype distinction: designing separate evaluation tracks for overt vs. subtle expression of harmful values captures a broader range of real-world harm and is a useful template for bias/values benchmarks.
- Shared-task format for cross-system comparison: running multiple participant systems on the same data enables systematic benchmarking of detection approaches, valuable for establishing baselines.

## 12. Notable quotes
Full text unavailable; no verbatim quotes can be provided.

## 13. UNKNOWN / not in extract
- Full author list (metadata incomplete)
- Specific annotation schema and label definitions
- Number of annotators and annotator demographics
- System results from participating teams
- Exact scoring formulas for disagreement-aware evaluation
- Train/test split sizes
- Full text unavailable (extract existed but was 0 pages)
