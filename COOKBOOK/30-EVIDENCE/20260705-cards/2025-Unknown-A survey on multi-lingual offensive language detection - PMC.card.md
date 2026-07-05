---
stem: "2025-Unknown-A survey on multi-lingual offensive language detection - PMC"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, best-practices, saturation-discrimination]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [en, hi, ar, es, it, de, pt, fr, fa, bn, ta, ml, kn, tr, da, el]
models_tested: []
headline_numbers: ["Survey of multilingual offensive-language detection, publications 2019-July 2023 (p.8)", "Eight approach categories (LR, DNN, TL, MT, EL, Meta-L, Multitask-L, UL) (p.8)", "hatespeechdata.com indexes 63 datasets in multiple languages (p.5)", "Prior survey covered 18 languages of datasets (p.5)", "Published PeerJ Comput. Sci. 2024, DOI 10.7717/peerj-cs.1934 (p.1)"]
---
## 1. Gist
This is a narrative literature survey (PeerJ Computer Science, 2024, Mnassri et al.) of multilingual and cross-lingual offensive-language and hate-speech detection. It is not a benchmark: it synthesizes prior surveys, taxonomizes detection approaches into eight method families, catalogs multilingual datasets, and lists community resources (shared tasks, source code, APIs), then discusses technical/cultural/linguistic challenges and future directions. Its relevance for values-alignment benchmarking is as a landscape map of how "offensive"/"hate" content — an inherently value-laden, culturally contingent construct — is operationalized, annotated, and measured across languages, and it foregrounds the definitional and annotation-subjectivity problems that also plague values benchmarks.

## 2. Benchmark/eval design features
Not a benchmark. Core content: (a) taxonomy distinguishing offensive content, hate speech, and aggressive content as overlapping categories (Fig 1, p.3); (b) distinction between multilingual NLP (one model, many languages) and cross-lingual NLP (transfer resource-rich to resource-poor) (p.3-4); (c) eight approach families — Logistic Regression, Deep Neural Networks, Transfer Learning, Machine Translation, Ensemble Learning, Meta-Learning, Multitask Learning, Unsupervised Learning — each with representative studies, focused languages, and feature-extraction methods (Table 2, p.9-10); (d) comparison table of prior surveys and how this one differs (Table 1, p.6). Central claim: no widely agreed definition of hate/offensive speech, which increases annotation subjectivity and yields biased models (p.2).

## 3. Task format & example item
n/a — survey paper, no items.

## 4. Scoring / grading methodology
n/a. Notes that reviewed studies predominantly report F1 and that translated-vs-non-translated pipelines trade off cost against performance (p.12). No scoring performed by the survey itself.

## 5. Dataset construction & provenance
The survey reviews (does not construct) multilingual corpora. Methodology: keyword search of IEEE Xplore, ACM DL, Google Scholar for "multilingual/cross-lingual offensive/hate/abusive language detection", publications 2019-July 2023 (p.8). Languages coded with ISO 639-2 (p.8). References external dataset hubs — hatespeechdata.com (63 datasets) and prior survey covering 18 languages (p.5). Categorized as a narrative (qualitative) review vs systematic review (p.6).

## 6. Validity evidence
n/a for psychometrics. The survey itself emphasizes a validity threat in the field: absence of a unified hate-speech definition inflates annotation subjectivity and propagates bias into models (p.2). It contrasts narrative vs systematic review rigor (p.6).

## 7. Saturation / discrimination
n/a. Observes field evolution: early word-embedding/traditional-ML approaches (~2020) gave way to transfer-learning with mBERT/XLM-R dominating, and notes meta-learning (Proto-MAML, HateMAML) outperforming transfer-learning baselines in low-resource few-shot settings (p.13-14).

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- Publications surveyed: 2019 to July 2023 (p.8)
- Eight approach categories (p.8)
- hatespeechdata.com: 63 datasets, multiple languages (p.5)
- Prior survey (Pamungkas et al.) covered datasets in 18 languages (p.5)
- Vidgen & Derczynski reviewed 63 abusive-language datasets (Table 1, p.6)
- Published PeerJ Comput. Sci. 10:e1934, 2024, CC-BY 4.0 (p.1)
- 48-page article (p.1)

## 10. Pitfalls & limitations
As a narrative review it is subjective/qualitative by design and non-exhaustive (p.6). Coverage ends July 2023, so pre-dates most instruction-tuned LLM evaluation work (only mentions ChatGPT via Das et al. 2023 for 11 languages, p.16). Excludes monolingual approaches except in passing (p.8). No quantitative meta-analysis of reported scores — cannot compare methods on a common footing. The field-level flaw it documents (no unified definition of hate/offensive speech) means the reviewed benchmarks are not mutually commensurable, limiting any cross-study conclusions.

## 11. Novel ideas worth stealing
- **Overlapping-category taxonomy** (offensive ⊇ hate speech + aggressive content, distinguished by intent/target/impact) — a template for decomposing fuzzy value-laden constructs into a Venn structure rather than a flat label (Fig 1, p.3).
- **Multilingual vs cross-lingual distinction** as a design axis: build one model for many languages vs transfer from high- to low-resource — directly applicable to how a values benchmark plans language coverage (p.3-4).
- **Method-family × languages × feature-extraction comparison table** (Table 2) as a reusable structured-review format for surveying benchmark approaches (p.9-10).
- **Explicit prior-survey differentiation table** (Table 1) documenting each predecessor's focus and its gap — a rigorous way to justify a new benchmark's contribution (p.6).
- **Flagging definitional non-consensus as the root cause of annotation subjectivity and model bias** — a warning to standardize construct definitions before building value-alignment items (p.2).
- **Meta-learning (Proto-MAML / HateMAML) for low-resource few-shot transfer** as a technique for extending a benchmark's annotations to under-resourced languages (p.13-14).
- **ISO 639 language coding and open dataset hubs (hatespeechdata.com)** as infrastructure conventions for reproducible multilingual coverage (p.5, p.8).

## 12. Notable quotes
"up to date there is no widely acknowledged unique deﬁnition of offensive and hate speech. This is primarily due to the ambiguous, subjective, and personal interpretations" (p.2)
"Unspeciﬁed deﬁnitions can result in increased subjectivity in annotations which then facilitates generating a biased model" (p.2)
"By exploring multilingual offensive content, we can broaden our understanding and effectively combat the widespread global impact of offensive language." (p.1)
"a simple model relying on automatic machine translation and an English BERT pre-trained model achieved competitive results" (p.12)

## 13. UNKNOWN / not in extract
Full contents beyond page ~16 (Datasets, Resources, Challenges/limitations, future-directions sections read only partially). Exact total count of datasets/approaches tabulated by the survey. Complete list of languages in the surveyed corpora. Any quantitative comparison figures. Author affiliations beyond Telecom SudParis. The stem lists author as "Unknown" but the paper is by Mnassri, Farahbakhsh, Chalehchaleh, Rajapaksha, Jafari, Li, Crespi (p.1).
