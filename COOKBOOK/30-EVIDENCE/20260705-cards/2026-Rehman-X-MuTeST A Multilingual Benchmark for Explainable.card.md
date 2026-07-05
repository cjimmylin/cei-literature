---
stem: "2026-Rehman-X-MuTeST A Multilingual Benchmark for Explainable"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, llm-judges-scoring, validity-psychometrics, best-practices]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 16830
dataset_construction: "crowdsourced"
languages: [hi, te, en]
models_tested: [GPT-4o, LLaMa-3.1, Mistral-24.07, MuRIL, XLM-R, BERT-HateXplain]
headline_numbers: ["Token-level rationale annotations for 6,004 Hindi, 4,492 Telugu, 6,334 English samples (p.2)", "Fleiss overall kappa: Telugu 81.00, Hindi 83.15, English 85.10 (p.3)", "X-MuTeST-with-LLM Telugu accuracy 0.8881, token-F1 0.6231 (p.6)", "English sufficiency 0.0507, comprehensiveness 0.8433 (p.7)"]
---
## 1. Gist
X-MuTeST is a multilingual explainable hate-speech-detection benchmark and training framework covering Hindi, Telugu, and English. Its benchmark contribution is human-annotated *token-level rationales* (which words justify the hate/not-hate label) for three languages — the first such rationale resource for under-resourced Indic languages Hindi and Telugu, extending the English-only HateXplain paradigm. The methodological contribution is a two-stage training framework that guides transformer attention with human rationales (Stage 1) then with an n-gram-based explainability signal (Stage 2), and fuses model rationales with LLaMA-3.1-generated rationales via set union. For values-alignment benchmarking it matters because it operationalizes *culturally grounded* explanation: the authors show LLMs miss Hindi terms like "to bark"/"to feel offended" that are highly offensive in-culture but not flagged by models trained on English norms — a concrete demonstration that alignment/rationale quality is language- and culture-dependent, and that human rationales are needed to bridge the gap.

## 2. Benchmark/eval design features
- Constructs: (a) binary hate classification, (b) token-level rationale plausibility, (c) rationale faithfulness.
- Item = social-media post with a HATE/NOT-HATE label plus per-token binary rationale mask (1=hate-indicating, 0=not) (p.3).
- Sizes: Telugu 4,492 / Hindi 6,004 / English 6,334 records; avg rationale length 3.10/3.26/3.78 tokens (Table 1, p.4).
- Explainability evaluated with plausibility (Token-F1, IOU-F1 with 0.5 overlap threshold) and faithfulness (Comprehensiveness, Sufficiency) — ERASER/HateXplain metrics (p.6).

## 3. Task format & example item
Binary classification + token rationale. Example (paraphrased from Figure 1, p.2): a Hindi hateful sentence where human annotators mark rationale terms translating to "to feel offended" and "to bark" (offensive in Hindi) plus "dog"; LLMs identify only "dog." No fully verbatim item string is printed in the extract (Figure 1 is an image). Rationale format: annotators mark hate-indicating tokens =1, others =0; non-hate posts have all tokens =0 (p.3).

## 4. Scoring / grading methodology
Classification scored with accuracy, F1, macro-F1. Explanation plausibility scored via Token-F1 and IOU-F1 (overlap>0.5 counts as match) against human rationales (p.6). Faithfulness via Comprehensiveness = P(x)c − P(x\r)c (confidence drop when rationale masked) and Sufficiency = P(x)c − P(r)c (lower is better; rationale alone) (Eq. 12-13, p.6). Top-5 tokens used as predicted rationale; masked with <MASK>. LLMs (GPT-4o, LLaMa-3.1, Mistral) scored zero-shot on Token-F1/IOU-F1 only (no probabilities → no faithfulness).

## 5. Dataset construction & provenance
Sources: Hindi & English from HASOC 2020+2021 (Twitter); Telugu from HOLD-Telugu / DravidianLangTech 2024 (YouTube, transliterated Latin→Telugu via IndicXlit) (p.3). Binary HATE/NOT-HATE labels retained. English/Hindi test split = 15%; Telugu split provided by source. Rationale annotation by 5 hired annotators (3 per language, native experts, age 18+, diverse regions to reduce demographic bias), structured training, iterative re-annotation with consensus resolution (p.3). Data + code public at github.com/ziarehman30/X-MuTeST.

## 6. Validity evidence
Inter-annotator agreement reported: pairwise Cohen's Kappa and Fleiss overall — Telugu 81.00, Hindi 83.15, English 85.10 (Table 2, p.3); initial rounds "moderate to substantial (61-80%)" improved via iterative annotation. Generalizability tested on external HateXplain (IOU-F1 0.314, Token-F1 0.587) and HateBRXplain (Portuguese) with reported gains (p.8). Faithfulness metrics (comp/suff) provide criterion-style evidence that rationales drive predictions.

## 7. Saturation / discrimination
Classification accuracies cluster ~0.83-0.89; X-MuTeST-with-LLM leads but by modest margins (e.g., +1.41% acc over Muril-RX on Telugu, p.6). Explainability metrics discriminate strongly: token-F1 ranges 0.28-0.62 across models/languages, leaving substantial headroom (best Telugu 0.6231, best Hindi only 0.4344, p.6). Hindi sufficiency remains high (~0.47-0.73) indicating rationale faithfulness is far from saturated. LLMs underperform fine-tuned encoders on classification (e.g., Llama-3.1 Hindi acc 0.5172, p.6).

## 8. Multiturn / agentic aspects
n/a — single-turn classification; "LLM consultation" is a one-shot prompt to LLaMA-3.1 for rationale terms, fused by union with the model's n-gram rationale. No interaction, tools, or environment.

## 9. Key numbers
- Dataset: Telugu 4,492 (2,131 hate), Hindi 6,004 (2,026 hate), English 6,334 (3,767 hate) (Table 1, p.4).
- Fleiss kappa: Telugu 81.00, Hindi 83.15, English 85.10 (Table 2, p.3).
- Telugu best: X-MuTeST+LLM acc 0.8881, F1 0.8762, macro-F1 0.8849, token-F1 0.6231, IOU-F1 0.3189, suff 0.0448 (Table 3, p.6-7).
- Hindi best: acc 0.8745, token-F1 0.4344, suff 0.4768 (Table 4, p.6).
- English best: acc 0.8604, token-F1 0.5125, comp 0.8433, suff 0.0507 (Table 5, p.7-8).
- LLM zero-shot Telugu: GPT-4o acc 0.6484, Llama-3.1 0.6362, Mistral 0.6402 (Table 3, p.6).
- α balancing: 0.3 Stage-1; Stage-2 0.6 (Hindi/English), 0.7 (Telugu) (p.5).
- External: HateXplain IOU-F1 0.314 / Token-F1 0.587 (p.8).

## 10. Pitfalls & limitations
- Author-admitted: initial annotator agreement only moderate (61-80%), requiring iterative re-annotation — raises questions about rationale subjectivity.
- Telugu transliteration (Latin→Telugu) degrades LLM performance, confounding language effect with script/transliteration noise (p.6).
- Small binary label set (HATE/NOT-HATE) — no severity/target dimensions.
- Union-of-explanations inflates rationale recall but may hurt precision; agreement score between sources reported as formula only.
- Only 3 annotators/language; compensation was GPU hours, not standardized pay.
- Not a values benchmark per se — hate-speech proxy for cultural-normative alignment.

## 11. Novel ideas worth stealing
- **Human token-level rationales as gold explanations** across multiple languages — a template for evaluating whether a model's *reasoning* (not just verdict) matches culturally-grounded human judgment; directly transferable to values-alignment where "why" matters as much as "what."
- **Culturally-divergent rationale examples** (Hindi "to bark" offensive, missed by English-aligned LLMs) — a sharp diagnostic for cultural-alignment blind spots; build items where the *rationale* differs by culture even if the label doesn't.
- **Plausibility vs. faithfulness split** (does the explanation match humans AND does it reflect the model's actual decision) — a two-axis evaluation reusable for any explanation-producing values judge.
- **Comprehensiveness/Sufficiency via masking** as a faithfulness probe for LLM-judge rationales.
- **Iterative annotation with re-annotation rounds** to lift kappa on subjective normative labels — a construction QA practice.
- Using an **LLM as a rationale consultant fused by union** with a cheaper saliency method — hybrid human/model/LLM rationale aggregation.

## 12. Notable quotes
- "societal and cultural aspects of languages are often overlooked by these methods for under-resourced languages. This gap between machine-provided rationales and human rationales can be bridged by providing rationale resources for these languages." (p.2)
- "even though a model may be accurate in classification, its reasoning may not align with human logic or provide meaningful explanations." (p.2)
- "we carefully select annotators above the age of 18 from diverse regions across the country to mitigate potential demographic biases." (p.3)
- "Lower sufficiency indicates that the rationale is informative." (p.6)

## 13. UNKNOWN / not in extract
- Exact Figure 1 verbatim sentence text (image not OCR'd).
- Per-source agreement (EX∩ELLM) numeric values.
- Annotator demographic composition beyond age/region.
- Full external-benchmark absolute tables (only percentage gains given).
- Licensing terms of released dataset.
