---
stem: "2025-search-DweshVaani An LLM for Detecting Religious"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, contamination-robustness, llm-judges-scoring]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 11549
dataset_construction: "scraped"
languages: [hi, en, hi-en]
models_tested: [Llama-3.1-8B, GPT-4o-Mini, Gemma-2-9B, Sarvam-1, Nemotron-4-Hindi, Indic-Gemma-7B, Airavata, Project-Indus, MuRIL]
headline_numbers: ["DweshVaani (fine-tuned Gemma-2) reaches 76.19 micro-F1 / 64.27 macro-F1 (p.7)", "MuRIL full-data baseline 73.33 micro-F1 (p.6-7)", "Best LLM few-shot (GPT-4o 8-shot RAG) 63.03 micro-F1, ~10pp below MuRIL (p.5-6)", "THAR dataset: 11,549 comments across 4 classes (p.4)"]
---
## 1. Gist
DweshVaani is a fine-tuned Gemma-2 LLM (plus a comprehensive empirical study) for detecting religious hate speech and identifying the *targeted* religion in code-mixed Hindi-English YouTube comments. It is primarily a hate-speech-detection modeling paper, not a values-alignment benchmark, but it is relevant to the COOKBOOK for religious-values and cultural-linguistic robustness: it evaluates many LLMs (Meta, Google, OpenAI, Nvidia, plus Indic-LLMs) on a sensitive, culturally-loaded classification task in a low-resource code-mixed setting, and applies HateCheckHIn black-box functionality testing to expose weaknesses that aggregate F1 hides. Key findings: Indic-tuned LLMs underperform, RAG-based semantically-similar few-shot beats random few-shot, and direct QLoRA fine-tuning beats knowledge-distillation (rationale-augmented) fine-tuning.

## 2. Benchmark/eval design features
Task = 4-way classification of a comment's targeted religion: Christianity, Hinduism, Islam, None (Subtask 2 of the THAR dataset), which subsumes binary anti-religion detection plus target identification (p.3-4). Four experimental arms: (1) MuRIL masked-LM fine-tuned on full data; (2) in-context learning (zero-shot, random 1/2-shot, RAG-based similar 1/4/8-shot) across 8 LLMs; (3) QLoRA fine-tuning of Gemma-2 (→ DweshVaani); (4) knowledge-distillation fine-tuning with GPT-4o-Mini-generated rationales (→ DweshVaani-X). Class criteria hand-defined (e.g., hostility toward beliefs/sacred elements/spiritual leaders).

## 3. Task format & example item
MCQ / classification. Verbatim prompt template (Appendix B.1, p.12): "You are an expert assistant which can analyze hate speech texts from Youtube comments and identify the religion they are targeting. Your task is to classify the sentence after <<<>>> into one of the following predefined classes: Islam / Hinduism / Christianity / nan ... You will only respond with the name of the class." Example item (p.3): Comment "Yeh hain peace wala religion musalman" → label Islam (mockery of a religious group).

## 4. Scoring / grading methodology
Automatic classification metrics: micro-F1 (µ-F1) and macro-F1 (m-F1) against gold THAR labels (p.5, Table 2/3). No LLM-judge for the main scoring; GPT-4o-Mini is used only to *generate rationales* for the distillation arm, not to grade. Additional black-box functionality testing (HateCheckHIn) reports per-functionality accuracy on templated test cases (Tables 6-7, p.14-15).

## 5. Dataset construction & provenance
THAR (Targeted Hate Speech Against Religion; Sharma et al. 2024) — YouTube comments scraped from videos on controversial religious/political topics. 11,549 total (train 10,394 / test 1,155): Christianity 391, Hinduism 1,349, Islam 3,714, None 6,095 (Table 1, p.4) — heavily imbalanced toward None and Islam. Code-mixed Hindi-English in both Devanagari and Roman script with real-world noise (emojis, slang, typos). MuRIL sentence-transformer fine-tuned for RAG retrieval (cosine similarity, K=1/4/8). QLoRA: 4-bit, rank-64 adapters, 216M trainable params, 3 epochs (p.6).

## 6. Validity evidence
Robustness validated via HateCheckHIn functional tests (6 multilingual + 29 monolingual functionalities), showing DweshVaani is more stable than MuRIL baseline on non-hateful/neutral/positive-identity cases (F18 95.24 vs 33.33; F19 83.33 vs 20.00; F20 denouncement 50.00 vs 6.67, p.14-15). Error analysis reveals many misclassifications trace to *dataset labeling errors* (all Christianity comments predicted None often due to mislabels), suggesting the model is sometimes more correct than gold (p.8). No human inter-annotator reliability reported for THAR here.

## 7. Saturation / discrimination
Wide discrimination across methods: zero-shot LLMs 34–50 µ-F1; RAG few-shot lifts to ~55–63; MuRIL 73.33; DweshVaani 76.19 (p.5-7). RAG example count saturates/declines beyond a threshold (GPT-4o plateaus at 8-shot; Airavata drops 60.43→58.96, p.6). Substantial headroom: even best model far from ceiling on this noisy real-world task; low-resource-language slur functionalities (MF2/MF3 30%, F7 25.93%) show sharp failure modes.

## 8. Multiturn / agentic aspects
n/a — single-turn classification. Only "dynamic" element is RAG retrieval of semantically similar in-context examples at inference (Figure 1, p.5), not agentic interaction.

## 9. Key numbers
- THAR: 11,549 comments (train 10,394 / test 1,155); classes Christianity 391 / Hinduism 1,349 / Islam 3,714 / None 6,095 (p.4).
- DweshVaani 76.19 µ-F1 / 64.27 m-F1; DweshVaani-X (distillation) only 60.69 / 41.92; MuRIL 73.33 / 61.31; Sarvam-1 51.86 / 44.98 (p.7).
- Best few-shot LLM: GPT-4o 8-shot RAG 63.03 / 53.14 (p.5-6).
- RAG lift: Airavata 1-shot µ-F1 34.03→55.58 (+20pp) with one similar example (p.5).
- HateCheckHIn: DweshVaani F18 neutral-identity 95.24% vs MuRIL 33.33%; but MF3 Hindi-except-slur 30.0% vs MuRIL 56.67% (p.14).
- Zero-shot DweshVaani misclassification: Christianity 54.84%, Hinduism 55.30%, Islam 20.62%, None 17.38% (p.8).

## 10. Pitfalls & limitations
Author-admitted: counter-intuitive distillation failure needs investigation; dataset needs refinement (labeling errors); should extend to gender/misogyny (p.8, p.8-limitations). Reviewer-visible: severe class imbalance (Christianity only 391) inflates macro-F1 variance and drives the all-Christianity→None error; gold labels demonstrably noisy (author's own error analysis); rationales generated by GPT-4o-Mini import that model's biases into the distillation set; "religion" reduced to only 3 targeted faiths (Christianity/Hinduism/Islam), omitting Sikhism/Buddhism/Judaism etc. despite the Indian context; no human agreement statistics; single-author industry affiliation, no ablation on prompt-order sensitivity for the classifier.

## 11. Novel ideas worth stealing
- **RAG-retrieved similar few-shot examples** dramatically outperform random few-shot on culturally/linguistically hard items (+20pp) — for values benchmarks in low-resource or code-mixed settings, retrieving semantically-nearby in-context exemplars is a cheap, large lever.
- **Functional black-box testing (HateCheck-style) layered on top of aggregate F1** — templated identity-swapped test cases isolate failure modes (neutral-mention vs slur vs reclaimed slur vs denouncement) that a single F1 number hides; a strong template for auditing values classifiers for over-triggering on protected-group mentions.
- **Error analysis that surfaces gold-label errors** — treating disagreements as a diagnostic of dataset quality rather than model failure; useful discipline for any values dataset.
- **Rationale-distillation as a (negative) result**: injecting LLM-generated rationales during fine-tuning *hurt* here — a caution for benchmark builders assuming CoT/rationale augmentation always helps.
- **Script-variation robustness axis** (Devanagari vs Roman Hindi vs mixed) as an explicit generalization test — transferable to any multilingual values eval.

## 12. Notable quotes
- "Indic-LLMs which are instruction tuned on Indian content fall behind on the task." (p.1)
- "even when presented with upto RAG-based 8 similar examples, the best performing model (GPT-4o-Mini), still lags upto 10 percentage points compared to the MuRIL language model, which was fine-tuned on the whole dataset, but is much smaller in size." (p.5-6)
- "these metrics do help to measure the model performance, however they are incapable of identifying the weaknesses that could potentially exist in the model." (p.8)
- "Contrary to our hypothesis, we achieved significantly poor results ... as compared to both in-context learning, as well as Dwesh-Vaani, which was directly fine-tuned without using any additional knowledge." (p.7)

## 13. UNKNOWN / not in extract
THAR inter-annotator agreement / annotation protocol; MuRIL architecture full detail beyond Appendix C summary; exact HateCheckHIn aggregate score; licensing of THAR/DweshVaani beyond the HuggingFace link; whether any human evaluation of model outputs was done; how "None" vs subtle-hate boundary was adjudicated; per-class precision/recall breakdown; compute/runtime totals.
