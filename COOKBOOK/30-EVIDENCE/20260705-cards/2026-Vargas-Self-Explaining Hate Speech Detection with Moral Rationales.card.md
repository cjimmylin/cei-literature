---
stem: "2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, validity-psychometrics, pluralism-aggregation]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 7000
dataset_construction: "crowdsourced"
languages: [pt, en]
models_tested: [BERTimbau, mBERT, GPT-4o-mini, Llama3.1-70B, BiRNN, CNN, BoW]
headline_numbers: ["SMRA improves IoU F1 +7.4pp and Token F1 +5.0pp on hate classification (p.1)", "Multi-label moral Token F1 0.966 vs 0.725 baseline (p.6)", "LLMs peak at F1 0.38 on moral sentiment categories (p.1)", "HateBRMoralXplain = 7,000 Brazilian Portuguese Instagram comments, 3,500 offensive / 3,500 non-offensive (p.4)"]
---
## 1. Gist
This paper introduces (a) SMRA (Supervised Moral Rationale Attention), a self-explaining hate-speech-detection framework that aligns transformer token attention with expert-annotated *moral* rationales grounded in Moral Foundations Theory (MFT), and (b) HateBRMoralXplain, a Brazilian Portuguese benchmark of 7,000 Instagram comments annotated with hate labels, MFT moral categories, token-level moral rationales, and socio-political metadata. Its thesis — highly relevant to values-alignment benchmarking — is that lexical/surface cues for hate speech are language- and culture-specific and spurious, whereas moral categories encode more *stable, transferable normative structures*. By supervising attention with moral rationales, the model grounds predictions in morally salient evidence rather than surface lexemes, improving faithfulness and cross-cultural robustness without sacrificing fairness. The paper also empirically shows that current LLMs are weak at moral-sentiment classification (F1 ≤ 0.38) even when they classify hate reasonably, and that adding moral framing to prompts improves hate detection.

## 2. Benchmark/eval design features
- Two tasks: binary hate classification, and multi-label moral sentiment classification over 6 MFT labels {NN Non-Morality, HN Harm/Care, FN Fairness/Cheating, PN Purity/Degradation, AN Authority/Subversion, LN Loyalty/Betrayal} (p.3-4).
- Each comment gets 1-3 moral labels + rationales, ordered by annotator-perceived salience (primary/secondary/tertiary) (p.4).
- Token-level binary rationale masks derived from character-span annotations (p.4).
- Rich socio-political metadata (party, gender of politician authoring the parent post) enabling fairness/subgroup analyses (p.4).
- Evaluation axes: classification (Macro F1, AUROC), plausibility (IoU F1, Token F1), faithfulness (Comprehensiveness, Sufficiency), fairness (GMB-Sub, GMB-BPSN, GMB-BNSP).

## 3. Task format & example item
Mixed: binary + multi-label classification with token-rationale output. Verbatim example items (Table 5, p.8): "(3) O povo não é mais burro. Você não está ouvindo seus eleitores." (The people aren't stupid anymore. You're not listening to your voters.) → Non-Hate; "(4) Chic esses filhos do mito." (Chic, these kids of the 'Myth') → Non-Hate — "myth" refers to former president Bolsonaro, requiring political/cultural context. "(1) Se jogar um carteira de trabalho não sobra um" → Hate. These illustrate sarcasm/irony and culturally-context-dependent labels.

## 4. Scoring / grading methodology
Classification: Macro F1 (adapted multi-label correctness: correct if predicted category ∈ human label set) (p.6). Plausibility: IoU F1 (match if overlap>0.5, Eq. 1) and Token F1 (Eq. 2) comparing model rationales to human moral rationales (p.6). Faithfulness: Comprehensiveness = prob drop when rationale removed (Eq. 3); Sufficiency = prob using rationale only, lower is better (Eq. 4) (p.6). Fairness: GMB subgroup AUC metrics (Borkan/Dixon) — Sub, BPSN, BNSP (p.6). SMRA training = cross-entropy + α·MSE attention-alignment loss applied only to morally-labeled instances with rationales (p.4).

## 5. Dataset construction & provenance
Third version of HateBR: 7,000 Brazilian Portuguese Instagram comments from public political accounts (3,500 offensive / 3,500 non-offensive), 9 hate-speech targets, annotated by experts (p.4). Two/three expert annotators with diverse Brazilian backgrounds; annotators completed a pre-annotation survey (demographics, political ideology, moral values, personality, cultural orientation) (p.4). Span-based moral rationale protocol from MFTCXplain. Ground-truth rationale = first annotator's annotation (p.5). Released CC BY-NC 4.0 with per-annotator labels and disagreements public (p.9).

## 6. Validity evidence
Inter-annotator agreement via Cohen's weighted Kappa (quadratic weights) per moral category: Class A κ=0.811 (substantial-almost perfect), Class B κ=0.671, Class C κ=0.612 (moderate-substantial, higher subjectivity in secondary/tertiary) (p.5). Grounded in established MFT (Graham et al. 2013) and cross-cultural morality work (Atari et al. 2023). SMRA compared against SRA baseline (Eilertsen 2025) with reported ± std (Table 2, p.7). Fairness stability shown across GMB metrics. Release of annotator-level disagreements supports pluralism analysis.

## 7. Saturation / discrimination
Hate classification near ceiling for BERTimbau (Macro F1 ~0.90-0.91), but multi-label moral sentiment far from saturated (BERTimbau Macro F1 0.757→0.772; mBERT collapses to ~0.17-0.20) (Table 1, p.7). LLMs show a stark floor on moral categories (F1 ≤ 0.38 GPT-4o-mini, ≤0.383 Llama70B) — large headroom (Table 4, p.8). Plausibility IoU F1 varies 0.716-0.836; Token F1 up to 0.966, discriminating SMRA from baselines. Classic models (BoW/CNN/BiRNN) reveal task trade-offs (Table 3, p.7).

## 8. Multiturn / agentic aspects
n/a — single-turn classification. No dialogue, tools, or environment. LLM evaluation is one-shot prompting across configurations (hate, hate w def., hate moral, w context, etc.).

## 9. Key numbers
- Dataset: 7,000 comments, 3,500/3,500 split, 9 targets, C=6 moral labels (p.4).
- Binary hate BERTimbau-SMRA vs base: Acc 0.9114 vs 0.9029; Macro F1 0.9114 vs 0.9028; IoU F1 0.8355 vs 0.7612; Token F1 0.8958 vs 0.8455; Suff 0.0426 vs 0.0657 (Table 1, p.7).
- Moral BERTimbau-SMRA: Macro F1 0.772 vs 0.757; Token F1 0.966 vs 0.725 (Table 1, p.7).
- SMRA vs SRA: IoU F1 0.7612 vs 0.716; Token F1 0.8455 vs 0.745 (Table 2, p.7).
- Fairness GMB-Sub 0.9139→0.9212 (p.1, Table 1).
- LLM moral sentiment F1 peak ~0.38 (Table 4, p.8); Llama70B hate w def. F1 0.901 pt (p.8).
- English translation degrades performance across both tasks/models (Table 4, p.8).
- Kappa: A 0.811, B 0.671, C 0.612 (p.5).
- Ablation: removing MFT guidance drops moral F1 by 34% (GPT-4o-mini) / 36% (Llama70B) (p.8).

## 10. Pitfalls & limitations
- Author-admitted: relies on costly expert moral-rationale annotation, limiting scalability; evaluated only on Brazilian Portuguese social media; moral reasoning doesn't eliminate all training biases (p.9).
- Ground-truth rationale = single (first) annotator, discarding disagreement despite the paper's own thesis that disagreement is morally meaningful — a tension.
- mBERT performs near-randomly on this Portuguese data, so multilingual transfer of the method is unproven.
- Multi-label moral IoU F1 is low/flat (0.235) even for best model — rationale localization for morality remains weak.
- Small classification gains (+0.9 F1) may be within noise; main value is explainability.

## 11. Novel ideas worth stealing
- **Moral rationales as attention supervision**: aligning model attention to MFT-grounded moral spans instead of lexical spans — a template for building values benchmarks where the *moral basis* of a judgment, not the surface trigger, is the gold signal; more culturally transferable.
- **Multi-label salience-ordered moral annotation** (primary/secondary/tertiary moral foundations per item) — captures moral pluralism within a single instance.
- **Releasing per-annotator labels + disagreements** grounded in a pre-annotation survey of annotators' ideology/moral values/personality — directly supports pluralistic aggregation and studying whose values a benchmark encodes.
- **Cross-cultural stability argument**: use morality as a latent transferable representation across languages — reusable rationale for multilingual values benchmarks.
- **Prompt-ablation of moral framing**: measuring how much moral-foundation guidance helps LLM judgments (huge drop when removed for moral classification) — a diagnostic for whether models have intrinsic moral competence.
- **English-translation degradation test** as evidence that moral labels don't transfer cleanly across cultures — a validity check for translated benchmarks.
- **Socio-political metadata linkage** (party/gender of target) enabling subgroup fairness (GMB-BPSN/BNSP) analysis.

## 12. Notable quotes
- "moral values constitute a transferable latent representation for hate speech across languages and cultures... hate speech targets a recurring set of moral violations and rarely occurs in the absence of moral sentiments" (p.2)
- "disagreements in hate speech annotation are shaped by annotators' moral values rather than annotation noise... standard label aggregation and opaque modeling approaches risk encoding dominant moral norms while obscuring minority perspectives." (p.2)
- "While lexical markers of hate speech are highly language- and culture-dependent, moral categories and their rationales encode more stable normative structures" (p.2)
- "LLMs perform poorly on moral sentiment categories (at most F1 of 0.38), even though incorporating moral rationales leads to significant improvements in hate speech classification" (p.2)

## 13. UNKNOWN / not in extract
- Exact value of α / attention weight beyond mention of 0.001 (p.5, ambiguous).
- Full MSE attention-alignment loss equation (rendered incompletely in extract).
- Complete per-category and per-annotator agreement tables (Appendix A.1 not in extract).
- Number of annotators (text says "three different experts" p.4 but "two expert annotators" p.4 — inconsistent).
- Statistical significance test details for LLM improvements.
- Full LLM prompt texts (Appendix C).
