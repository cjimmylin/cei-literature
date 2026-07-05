---
stem: "2025-Piot-Bridging Gaps in Hate Speech Detection Meta-Collections and"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, best-practices]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 82233
dataset_construction: "mixed"
languages: [es, pt, gl, en]
models_tested: ["Llama 3.1 8B", "Mistral Nemo", "bert-base-multilingual-cased"]
headline_numbers: ["MetaHateES meta-collection: 82,233 samples, 24.85% hate (p.12)", "Best fine-tuned Spanish F1-micro 0.8535 (Nemo) (p.22)", "English fine-tuned F1-macro 0.9048 (BERT) (p.23)", "10 European Spanish datasets from 21 fitting; 0 accessible for PT/GL (p.9)"]
---
## 1. Gist
This paper builds MetaHateES, a standardized meta-collection of 10 European-Spanish hate-speech datasets (82,233 posts), then projects it via translation into European Portuguese and two Galician variants (Spanish-convergent vs Portuguese-convergent) to create aligned multilingual corpora. It establishes new hate-speech-detection benchmarks for low-resource Iberian languages and evaluates LLMs (Llama 3.1, Nemo) and mBERT under zero-shot, few-shot, and fine-tuning. It matters for values-alignment work as a template for building variety-aware, culturally grounded safety benchmarks in underrepresented languages, and for its explicit treatment of intra-language dialectal variation — a factor usually collapsed.

## 2. Benchmark/eval design features
Construct: binary hate speech (0/1) under a unified definition ("offensive, derogatory, humiliating or insulting discourse that promotes violence, discrimination, or hostility... based on attributes such as race, religion, ethnicity, or gender", p.8, aligned with the UN definition). Sub-construct tags (content_type): offensive, hate speech, sexism, stereotype, aggressive, toxicity, misogyny. Metadata: source platform (Twitter, YouTube, News, Instagram, Gab). Answer space is a binary label produced either by encoder classifier (BERT) or by LLM free-text generation parsed to a label. Additional dimension: Galician internal variation (ES-like vs PT-like) as a robustness axis.

## 3. Task format & example item
Binary classification: model given task description + input social-media text, outputs hate / not-hate. Translation prompt for corpus creation: "Translate Spanish to Portuguese (pt PT): %%SENTENCE%%" (p.14). No verbatim classification prompt or labeled example item is reproduced in the extract (only lexical examples like top terms "mujer", "puta", "inmigrante", p.17). Example item text: n/a.

## 4. Scoring / grading methodology
Micro- and macro-averaged F1 for binary classification. LLMs generate with temperature=0, top_p=0.1, top_k=5, max_new_tokens=256 (zero/few-shot); fine-tuned 3 epochs, lr 2e-5, batch 16, AdamW. BERT fine-tuned 3 epochs, lr 5e-5, batch 32, weight decay 0.18. 80/20 train/test split. Cross-lingual matrix: train on Li, test on Lj (p.21-22).

## 5. Dataset construction & provenance
Systematic review (ACL Anthology 666, ACM 308, Scopus 272 docs; two dataset repositories) run Dec 2024. Inclusion criteria: new dataset, social-media text, human-annotated, matches hate definition, targets European variants (p.8). 21 fitting Spanish datasets → only 10 accessible; 3 Portuguese and 1 Galician fitting but 0 accessible (p.9). Labels harmonized (No/False→0; True/Offensive/Sexist/Aggressive→1; majority vote when no gold label). MetaHatePT translated with EuroLLM-9B-Instruct; MetaHateGL_es via Google Translate from Spanish; MetaHateGL_pt via Google Translate from Portuguese. 82,233 total, 24.85% hate. Twitter largest (43,254, 29.7% hate); Gab highest hate rate (54.08%). Released on HuggingFace (irlab-udc/MetaHateES) and GitHub; component datasets have individual licenses.

## 6. Validity evidence
Component datasets all human-annotated (inclusion criterion). Cross-lingual psycholinguistic validity checks: negative emotions (fear, disgust, anger, sadness) more frequent in hate posts across all four languages (NRC lexicon, Plutchik); present-tense and 2nd-person/3rd-plural pronouns ("othering") more common in hate — patterns preserved across translations, supporting synthetic-data fidelity (RQ2, p.19-20). No inter-annotator agreement recomputed (inherited from sources).

## 7. Saturation / discrimination
Clear discrimination across settings: English fine-tuned highest (BERT F1-macro 0.9048), Spanish next (~0.75-0.80), Portuguese/Galician lower especially zero/few-shot — substantial headroom for low-resource varieties. Zero-shot ~0.65-0.68 macro-F1 vs fine-tuned 0.72-0.80, so task-adaptation gap is large. Galician (ES) vs (PT) differ despite identical source content, showing the benchmark discriminates dialectal alignment (e.g., Llama macro 0.6148 vs 0.5995).

## 8. Multiturn / agentic aspects
n/a — single-turn classification.

## 9. Key numbers
- Meta-collection: 82,233 samples, 24.85% hate / 75.15% non-hate (p.12)
- Content types by hate rate: sexism 42.31%, misogyny 38.11%, toxicity 31.83%, hate speech 30.68%, stereotype 26.30%, offensive 15.91%, aggressive 9.26% (p.13)
- Fine-tuned Spanish: Nemo F1-micro 0.8535 / macro 0.7981; Llama 0.8309/0.7575; BERT 0.8211/0.7583 (p.22)
- Fine-tuned English: BERT F1-micro 0.9229 / macro 0.9048 (p.23)
- Galician (PT) fine-tuned: Llama F1-micro 0.7803 / macro 0.5926; BERT 0.8047/0.7331 (p.22-23)
- Cross-lingual: Spanish-trained BERT on English drops to macro 0.4962 (p.23)
- 6 major topics per language via BERTopic; Spanish topics concentrated on sexism/misogyny (p.16-17)

## 10. Pitfalls & limitations
Author-admitted: no accessible European Portuguese or Galician gold datasets, so PT/GL corpora are entirely machine-translated (translation artifacts, Brazilian-Portuguese bias in tools and NRC lexicon); topic diversity reduced in Galician (PT); spaCy lacks a Galician model (Portuguese model substituted, p.20); content skewed toward gender/sexism, under-representing xenophobia, LGBTQ+phobia, political hate. Seen flaws: binary label loses multi-class nuance; label harmonization via majority vote across heterogeneous schemes may distort constructs; no human validation of synthetic translations' label preservation; benchmark inherits source-dataset biases and sampling (keyword/lexicon-driven negativity).

## 11. Novel ideas worth stealing
- **Meta-collection with harmonized labels + provenance metadata** (content_type sub-construct + source platform): a reusable pattern for merging fragmented values datasets into one standardized benchmark while retaining granularity.
- **Deliberate dialect-variant pairs from a single source** (Galician-ES vs Galician-PT translated from different pivots) to isolate the effect of linguistic convergence — a clean controlled probe of variety sensitivity transferable to any values eval across dialects/registers.
- **Translation-direction as an experimental variable** in cross-lingual transfer matrices.
- **Psycholinguistic fidelity checks** (emotion lexicon, pronoun/tense profiles) to validate that synthetic/translated data preserves the target construct — cheap validity evidence for generated benchmark items.
- **Avoiding contamination** by choosing non-default translation tooling (EuroLLM for genuine European Portuguese) rather than commercial Brazilian-default translators.
- Using an **independent same-construct English set** as an external cross-lingual anchor/control.

## 12. Notable quotes
- "many of these languages have multiple linguistic varieties, a factor often overlooked in current approaches." (p.1)
- "no datasets for European Portuguese or Galician were accessible." (p.8)
- "Fine-tuning consistently outperforms zero and few-shot approaches, reinforcing the importance of targeted dataset development." (p.3)
- "even small shifts between Spanish-like and Portuguese-like features can impact classification accuracy." (p.25)

## 13. UNKNOWN / not in extract
Exact classification prompt text; a verbatim labeled example item; per-content-type model F1; inter-annotator agreement of source datasets; number/size of few-shot examples beyond "8"; whether translated corpora underwent any human label re-verification; total sample counts of MetaHatePT/GL; licensing terms per component dataset; figures 1-5 numeric detail beyond cited cells.
