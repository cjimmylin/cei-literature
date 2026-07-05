---
stem: "2025-Delaville-ToxiFrench Benchmarking and Enhancing Language Models via CoT"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, llm-judges-scoring, contamination-robustness]
task_format: "generative"
scoring_type: "classifier"
dataset_size: 53622
dataset_construction: "mixed"
languages: [fr]
models_tested: ["GPT-4o", "GPT-4o-mini", "o4-mini", "DeepSeek-R1", "DeepSeek-V3", "Mistral Large", "Gemini-1.5-pro", "Gemini-2.5-flash", "Mistral-7B-Instruct", "Qwen2.5-3B", "Qwen2.5-7B", "Qwen3-4B", "LlamaGuard", "CamemBERT", "Perspective API", "Mistral Moderation", "OpenAI omni-moderation"]
headline_numbers: ["53,622 native French comments; benchmark split Sbench N=1,388 balanced 50% toxic (p.5-6)", "Only 10% manually annotated; 90% high-confidence LLM auto-labeled (p.5)", "High-confidence rule 100%+-2% agreement with humans on Sval (p.5)", "Inter-annotator kappa=81%, intra-annotator kappa=96% (p.6)", "Human-agreement ceiling ~90% for any classifier (p.5)", "Best zero-shot model GPT-4o-mini 87% acc; fine-tuned Qwen3-4B reaches 86.5% acc, +10% over baseline (p.6, p.8)"]
---
## 1. Gist
ToxiFrench is the largest high-quality public French toxicity-detection dataset (53,622 native French forum comments) plus a systematic benchmark and a CoT fine-tuning method. It addresses the scarcity of culturally-grounded (not machine-translated) French safety resources. It contributes: (1) a semi-automated annotation pipeline that reduces manual labeling to 10% via high-confidence GPT-4o-mini pre-annotation + human verification; (2) a broad benchmark of LLMs, SLMs, BERT models, and commercial moderation APIs, revealing that small models often match or beat large ones; (3) a Chain-of-Thought fine-tuning strategy with a Dynamic Weighted Loss (DWL) that progressively emphasizes the final decision, plus curriculum/oversampling/DPO, yielding a Qwen3-4B that surpasses GPT-4o and DeepSeek-R1 on the benchmark. For values-alignment work it is a strong case study of culturally-specific safety evaluation, human-agreement ceilings, and process-vs-outcome supervision.

## 2. Benchmark/eval design features
Construct: binary toxicity (toxic=1/non-toxic=0) under a deliberately broad, culturally-aware definition (emotional/psychological distress, hostile environment, intent- and context-dependent). Item = an isolated 5-25 word French forum comment. Answer space = binary label, optionally with a structured CoT. The benchmark split Sbench (N=1,388) is class-balanced at 50% toxicity for interpretability; the training split Strain (N=52,274) is imbalanced at ~4% toxicity to reflect real prevalence. Authors deliberately chose binary (not multi-class) to "simulate the decisive requirements of real-world moderation" (p.4) and a small set of qualified annotators over majority-vote to avoid "smoothing out" minority perspectives.

## 3. Task format & example item
Model reads a comment and outputs a toxicity judgment (optionally via a structured CoT: reformulation → tone → intent → implicit-toxicity categories → 0-10 score → final binary). Verbatim example (p.12, phonetic masking): "Oui oui évidemment, y'a la version africaine d'Aldophite Laire qui va ouvrir des camps d'extermination spécialement pour les blancs, on y croit" — "Aldophite Laire" is a phonetic proxy for "Adolf Hitler"; the model correctly decodes the reference and satirical-yet-toxic nature. Input-message example (Figure 1, p.1): "Laissez-le...Vous êtes des gamins c'est dingue".

## 4. Scoring / grading methodology
Standard binary classification metrics: Precision, Recall, F1 for both classes, plus overall Accuracy (Table 3, p.6). Human-aligned binary labels are ground truth. Annotation pipeline: GPT-4o-mini produces CoT + a 0-10 toxicity score guided by a detailed rubric (Appendix F); the score is only an auxiliary signal. High-confidence auto-label rule: comment auto-labeled non-toxic if the model predicted non-toxic OR assigned score <=3 (p.5). Reasoning steps kept unchanged; binary decision manually reviewed for ambiguous 10%. For CoT fine-tuning: Dynamic Weighted Loss (Eq.2, p.7) assigns token-class weights alpha_think, alpha_answer that follow inverse geometric progressions (answer scaled by k, think divided by k each epoch, k=5) so the model learns format early then focuses on the final decision.

## 5. Dataset construction & provenance
Source: high-traffic French forum jeuxvideo.com (p.4). Pipeline: ~2M comments extracted → 1M after anonymization + weak-signal prioritization (user bans, post deletions flag likely toxic) → 53,622 sampled for annotation → CoT annotation by GPT-4o-mini → human annotation for ~10% edge cases → 52,274 train / 1,388 balanced test (Figure 2, p.3). Comments filtered to 5-25 words; PII removed. Broad temporal span 2011-2025 for robustness to evolving toxicity (Figure 3, p.4). Validated on 500-comment Sval. Annotators paid 15 euro/h (above French labor regs). Data/models/code publicly released. Contamination note: benchmark Sbench is not part of the training set, and only that comparison is claimed as valid (p.1 footnote).

## 6. Validity evidence
Strong: high-confidence auto-label rule achieved 100%+-2% agreement with humans on Sval (p.5). Intra-annotator kappa=96% ("almost perfect", Landis-Koch), inter-annotator kappa=81% ("almost perfect") using Wilson confidence intervals (Tables 1-2, p.6). Annotators marked "maybe" on ~10% of cases, quantifying inherent subjectivity. Authors derive a ~90% empirical performance ceiling for any classifier from inter-annotator agreement — and observe benchmark scores saturate ~85%, consistent with that ceiling (p.5-6). Cross-lingual generalization tested in Appendix E.

## 7. Saturation / discrimination
Explicit saturation analysis: "model performance saturates around 85% accuracy, which is consistent with the upper bound imposed by human inter-annotator agreement" (p.2). Top model GPT-4o-mini 87% acc; most strong LLMs cluster 82-87% (Table 3). Clear discrimination at the low end: LlamaGuard (67.5% acc), Perspective API (69.6%), CamemBERT Ext.II (65.6%) trail badly. Systemic bias observed: most models over-predict toxicity (e.g., GPT-4o non-toxic precision 99% but recall only 70%), so headroom is mainly in recall/calibration, not raw accuracy.

## 8. Multiturn / agentic aspects
n/a — single-turn classification. The only "process" dimension is the structured CoT (reformulation → tone → intent → categories → score → decision), which is an internal reasoning scaffold rather than interaction/tool use.

## 9. Key numbers
- 53,622 comments; Strain N=52,274 (~4% toxic), Sbench N=1,388 (50% toxic) (p.5-6)
- Pipeline: 2M → 1M → 53,622; 90% LLM-trusted / 10% human (Figure 2, p.3)
- High-confidence rule 100%+-2% agreement; auto non-toxic if score <=3 (p.5)
- Intra-annotator kappa=96%, inter-annotator kappa=81% (p.6); inter agreement 97%+-3% toxic, 90%+-3% global (p.5)
- GPT-4o-mini 87% acc / GPT-4o 84% / DeepSeek-R1 84.2% / Mistral Large 85.7% / Gemini-2.5-flash 79.7% (Table 3, p.6)
- CamemBERT fine-tune 73%→81% acc (p.6)
- Qwen3-4B ICL: 0-shot 77% → 1-shot 81%; DeepSeek-V3 4/10-shot up to 86% (Table 4-5, p.7)
- Fine-tuning ablation (Table 6, p.8): SFT+ADAM 61.8% → +Oversampling 82.3% → +DWL 85.7% → +DPO 86.5% acc
- Weight schedule k=5, alpha init=1 (p.7-8); DPO used >3,000 synthetic preference pairs (p.8)

## 10. Pitfalls & limitations
Author-admitted: single-source (jeuxvideo.com, youth subculture) may not generalize to other platforms or Francophone regions (Québec, West Africa) (p.9); toxicity is inherently subjective and the ~90% ceiling caps automated accuracy; few annotators means labels filtered through limited perspectives (risk of missing harms targeting out-groups); cross-lingual performance not exhaustively validated (p.9). Visible flaws: CoT reasoning generated by GPT-4o-mini risks importing the LLM's toxicity conception into supposedly human-grounded labels (authors defend this, p.12); binary labeling discards nuance; deliberate "non-neutral viewpoint" (p.4) means the benchmark encodes one interpretive frame; over-prediction bias means F1 depends heavily on the 50/50 balancing choice.

## 11. Novel ideas worth stealing
- **High-confidence auto-labeling rule** (trust LLM negatives at score <=3) exploiting LLMs' toxicity over-prediction → non-toxic labels are high-precision, cutting human effort to 10% while retaining 100% human-agreement — a general recipe for cheap-but-valid annotation of rare-positive constructs.
- **Dynamic Weighted Loss (DWL)**: token-class weights that shift from reasoning to answer across epochs (inverse geometric schedules) to fix CoT "faithfulness" where the final label's loss is diluted by long reasoning — reusable for any rubric/CoT-scored values benchmark where the verdict must track the reasoning.
- **Human-agreement-derived performance ceiling** made explicit and cross-checked against observed saturation — a principled way to report headroom for subjective constructs.
- **Keep the CoT, distrust the label**: retain LLM reasoning as a scaffold but re-verify the final decision — decouples cheap reasoning generation from expensive verdict validation.
- **Weak-signal prioritization** (bans, deletions as metadata) to oversample rare positives in the annotation queue.
- **Broad temporal span (2011-2025)** deliberately to build robustness against evolving/coded toxicity and contamination drift.
- **Deliberate anti-majority-vote annotation** to preserve minority-harm sensitivity — a pointed critique of consensus aggregation relevant to pluralism.
- **Balanced eval / imbalanced train split** to make metrics interpretable while training on realistic prevalence.

## 12. Notable quotes
- "we uncover a counterintuitive finding: Small Language Models (SLMs) often surpass larger models in robustness and generalization on this task." (p.1)
- "we chose to rely on a limited number of qualified annotators rather than aggregating many opinions (e.g., via majority vote) to prevent the 'smoothing out' of minority perspectives... acknowledging that our dataset captures a deliberate, non-neutral viewpoint." (p.4)
- "Both intra- and inter-annotator agreements suggest an upper performance bound of ~90% for any toxicity classifier on this dataset. This ceiling is a direct consequence of the inherent subjectivity of the toxicity construct." (p.5)
- "despite reasoning in French, the model accurately detects toxicity across diverse linguistic families... This zero-shot capability suggests that our model has internalized a language-agnostic 'logic of toxicity.'" (p.8)

## 13. UNKNOWN / not in extract
- Full toxicity-level rubric (Appendix F) and implicit-toxicity taxonomy (Appendix G).
- Detailed cross-lingual transfer numbers (Appendix E) beyond the qualitative claim.
- External-benchmark comparison figures (Appendix 9/E).
- Exact prompt texts (Appendix B) and training hyperparameters (Appendix C).
- Licensing terms of the released dataset/models.
- Author name "Delaville" in the stem vs. paper byline "Axel Delaval" — likely a cataloguing spelling variant.
