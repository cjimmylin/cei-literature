---
stem: "2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, best-practices]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 177749
dataset_construction: "scraped"
languages: [it, en, ar, fr]
models_tested: ["XLM-RoBERTa base", "XLM-RoBERTa large", mBERT, "XLM-Twitter", "ITA-Base-XXL", "ITA-Base", DeHateBert]
headline_numbers: ["Best multi-lingual XLM-Large macro-F1 81.23 vs best mono-lingual mBERT 66.93 (p.3)", "XLM-Twitter beats DeHateBert by 39 and 19 F1 points on AMI18/AMI20 (p.4)", "XLM-Large macro-F1 77.26 on Italian Multilingual HateCheck vs Röttger baseline 69.60 (p.4)", "Combined English training set 177,749 instances across 5 target categories (p.3)"]
---
## 1. Gist
HATE-ITA is a set of multilingual hate-speech detection models (and an open-source Python library) for Italian, built by fine-tuning multilingual transformers on a large English hate-speech collection combined with a small amount of Italian data. Its central finding for values-alignment work: joint multilingual fine-tuning substantially outperforms monolingual Italian models even when little Italian data is available, demonstrating cross-lingual transfer of a normative/safety construct (hate speech) into a mid-resource language. It matters as a template for extending value-laden benchmarks and safety classifiers beyond English, and it foregrounds the difficulty of language-specific slurs and taboo expressions that shift meaning by context (e.g., "finocchi" = fennels or a homophobic slur).

## 2. Benchmark/eval design features
Construct: binary hate/non-hate classification, controlled by six target attributes (origin, gender identity, sexual orientation, religious affiliation, disability) selected as a superset covering most dataset-specific labels; "other"/"none" discarded (p.2). Three training regimes are the design axis: MONO (Italian only), MULTI (Italian+English), ZERO (English only, zero-shot cross-lingual), all tested on Italian test sets (p.3). External validation via Multilingual HateCheck (MHC) functional test suite (counterspeech, spelling variation, slurs) — Italian subset only (p.4). Qualitative SHAP token-attribution evaluation on hard ambiguous Italian examples (p.4).

## 3. Task format & example item
Binary classification of a social-media message. Verbatim example with model output (p.4): "sono arrivati i finocchi" → P(hate)=0.960/True 1 (slur sense "here come the f*ggots"); "è arrivata l'insalata di finocchi" → P(hate)=0.080/True 0 (food sense, "fennel salad"). These minimal pairs test contextual disambiguation of a polysemous slur.

## 4. Scoring / grading methodology
Macro-F1 as the primary metric; a most-frequent-class baseline scores macro-F1 36.85 (p.3). Per-dataset F1 reported on AMI18, AMI20, Sanguinetti2018, HaSpeeDe18, HaSpeeDe20 (p.4). On MHC, F1 reported separately for hateful (F1-h), non-hateful (F1-nh), and macro-F1 (p.4). Models trained 5 epochs with step-wise evaluation, best checkpoint by validation loss; each experiment run 5 times and averaged (p.8).

## 5. Dataset construction & provenance
Italian training data: two EVALITA shared-task corpora — AMI18 (misogyny) and HaSpeeDe18 (anti-immigrant), each 2,500 train / 500 val / 1,000 test (p.2). English training data aggregated from public corpora on hatespeechdata.com: MlMa (Ousidhoum, Ar/En/Fr), ETHOS (Reddit), Kennedy 2020c (YouTube/Twitter/Reddit continuous scores thresholded), HateXplain (Twitter/Gab, majority vote), Gab Hate Corpus (27k posts), and Dynabench adversarially-generated data (p.2-3). Various label schemes binarized and target-mapped into the 6 categories. Combined English set: 177,749 instances (Disability 4,526; Gender 46,829; Origin 75,327; Religion 27,864; Sex.Orientation 22,313) (p.3). Official shared-task splits reused for comparability.

## 6. Validity evidence
Criterion validity via external MHC functional test suite where HATE-ITA (XLM-Large 77.26, XLM-Twitter 72.96) beats the Röttger et al. baseline (69.60) (p.4). Consistent performance across multiple held-out Italian datasets (Table 3) supports generalization. Qualitative SHAP explanations show the model correctly attributes hate to slur usage while not over-triggering on the food sense or the taboo-but-non-misogynistic expression "porca puttana" (p.4).

## 7. Saturation / discrimination
Wide score spread differentiates approaches: monolingual ITA-Base as low as 40.45 macro-F1 vs XLM-Twitter MULTI 83.34 (p.3). Substantial headroom remains, especially non-hateful F1 on MHC (best 65.88) lags hateful F1 (88.63) (p.4). ZERO cross-lingual is much worse than MONO, showing the Italian data is load-bearing (p.3). Authors explicitly decline to claim a solved/final model (p.5).

## 8. Multiturn / agentic aspects
n/a — single-message classification, no interaction or agentic component.

## 9. Key numbers
- Combined English set: 177,749 instances; hate 97,014 / non-hate 80,729 (p.3).
- Italian corpora: 2,500/500/1,000 splits each (p.2).
- MONO best mBERT 66.93; MULTI best XLM-Twitter 83.34; ZERO best XLM-Base 54.47 (p.3).
- Most-frequent-class baseline macro-F1 36.85 (p.3).
- XLM-Twitter vs DeHateBert: +39 (AMI18), +19 (AMI20) F1 (p.4).
- MHC Italian: XLM-Large F1-h 88.63, F1-nh 65.88, macro 77.26; baseline 69.60 (p.4).
- Training: batch 64, LR 1e-3, max length 100, AdamW, 5 runs averaged (p.8).

## 10. Pitfalls & limitations
Author-admitted: uncertain whether the model maintains stable, fair precision across targets/categories; not a definitive assessment; may overlook sensitive details (p.5). Binary hate/non-hate collapses severity and type. Heavy reliance on aggregating heterogeneous English corpora with inconsistent label schemes and ad-hoc thresholds (e.g., <-1→0, >0.5→1) risks label noise. Target coverage limited to five categories; DeHateBert comparison confounded by train/test overlap on some Italian sets (p.4). My addition: aggregating many scraped corpora raises contamination and annotation-drift concerns, and the SHAP qualitative section is cherry-picked correct predictions.

## 11. Novel ideas worth stealing
- Cross-lingual transfer of a normative construct: train mostly on a high-resource language plus a small target-language slice — directly reusable for porting values benchmarks to low-resource languages/cultures.
- Target-attribute harmonization: map heterogeneous dataset labels onto a fixed superset of protected categories to enable per-target coverage analysis (identifying which value dimensions remain untested).
- Minimal-pair contrastive items around polysemous slurs (slur sense vs benign sense) as a discrimination/robustness probe.
- Use of an external independent functional test suite (HateCheck/MHC) as a held-out validity check rather than trusting in-distribution test F1.
- MONO/MULTI/ZERO ablation design to isolate how much target-language data is actually load-bearing.

## 12. Notable quotes
"multi-lingual models can effectively be used to cover missing ground in some mid-to-low resource languages" (p.1)
"training only on the small set of Italian data is not enough even when using a language-specific model: joint fine-tuning with larger datasets is an effective way of obtaining more accurate hate speech classifiers." (p.3)
"When used separately (porca e puttana...), they should be considered literally; when used together, the two words form taboo expressions that do not have a misogynistic connotation." (p.4)
"We are unsure if our model can maintain a stable and fair precision across the different targets and categories." (p.5)

## 13. UNKNOWN / not in extract
- Per-target F1 breakdown (fairness across categories) — not reported.
- Exact licensing of the aggregated English corpora.
- Whether the released library models are the XLM-Large or XLM-Twitter checkpoints.
- Inter-annotator agreement figures for the source corpora.
