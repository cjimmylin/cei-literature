---
stem: "2025-Kumar-Are Rules Meant to be Broken"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, cultural-linguistic, normative-ethics, pluralism-aggregation]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 5256
dataset_construction: "mixed"
languages: [ar, zh, en, hi, ru, es]
models_tested: ["Phi-3.5-mini Instruct", "Llama-3.1-8B Instruct", "DeepSeek-R1-Distill-Llama-8B"]
headline_numbers: ["5256 instances across 6 languages (p.5)", "582 extensive + 882 compact annotations per language (p.5)", "Action prediction not significantly above chance for most cues (p.8)", "Models best in English/Spanish/Russian, worst in Arabic/Hindi (p.7)"]
---
## 1. Gist
UNIMORAL is a unified multilingual dataset that models moral reasoning as a full computational *pipeline* — scenario perception → action options → action choice → ethical-principle judgment → contributing-factor attribution → consequence — rather than as isolated tasks. It spans six languages (Arabic, Chinese, English, Hindi, Russian, Spanish) and pairs psychologically grounded dilemmas (from MJI, DIT, MCT) with real Reddit dilemmas, each annotated by crowd workers who also complete MFQ2 (moral foundations) and Hofstede VSM (cultural) questionnaires so every annotation carries an individual moral+cultural *persona*. It matters for values-alignment benchmarking because it (a) operationalizes personalization/pluralism — there is no single "moral" answer; ground truth is the annotator's own choice conditioned on their values — and (b) tests whether LLMs can *replicate a specific person's* moral decisions given their value profile, a direct steerability/persona-alignment probe across cultures.

## 2. Benchmark/eval design features
Four benchmark tasks on the pipeline: [I] Action Prediction (AP) — pick which of 2 mutually exclusive actions the annotator chose; [II] Moral Typology Classification (MTC) — predict the highest-rated ethical principle among deontology/utilitarianism/rights-based/virtue; [III] Factor Attribution Analysis (FAA) — predict the top contributing factor among 8 (emotions, moral, culture, role/responsibilities, relationships, laws, politeness, sacred values); [IV] Consequence Generation (CG) — generate the consequence of a scenario-action pair (p.6-7). Contextual-cue conditioning: models are given the annotator's moral values (m), cultural values (c), persona/self-description (p), or few-shot past decisions (fs) (p.6). Answer spaces: binary action choice, 4-way principle, 8-way factor, free-text generation.

## 3. Task format & example item
Mixed (forced-choice + classification + generation). Canonical wallet dilemma (Figure 1, p.1): a person finds a wallet; actions include "Return wallet to owner" vs "Donate money to charity" vs "keeping the wallet." Ethical frameworks illustrated (p.4): "following rules (e.g. handover the wallet to police), doing good for the majority (e.g. donate money to charity), respecting people's rights (e.g. return wallet to owner), and acting with good character (e.g. return the wallet and check for other missing items)." Full verbatim scenario text not in extract (in Appendix tables).

## 4. Scoring / grading methodology
Weighted F1-score is the primary metric for AP, MTC, and FAA (chosen for class imbalance / multi-class variability) (p.6-7). For CG, multilingual BERTScore against the set of annotator-provided consequences, scored by max similarity to any ground-truth consequence (p.7). A random-performance dotted line is shown for each task (Figure 3, p.7). Statistical-significance-vs-chance testing is applied (e.g., only few-shot in MTC beats chance significantly) (p.8).

## 5. Dataset construction & provenance
Seed scenarios: 16 unique psychological dilemmas from MJI (7), DIT (7), MCT (4) minus 2 duplicates (p.3). Llama-3.1-70B expands seeds × 9 contributing factors → 144 synthetic scenarios, each with 2 LLM-generated mutually exclusive actions (p.3-4). Reddit: ~400k dilemmas scraped from r/AmItheAsshole and similar, rephrased by Llama-3.3-70B; LDA topic modeling + k-means (200 clusters) → 200 representative dilemmas (p.4). Multilingual: MFQ2 + VSM translations select 5 languages; Hindi added via manual back-translation; scenarios/actions machine-translated with SeamlessM4T-v2, manually verified (p.4). Crowd-sourced on Prolific via Potato; 3 annotators per scenario; extensive (8 questions) vs compact (action only) studies. Total: 582 extensive + 882 compact per language → 5256 instances (p.5). HuggingFace release (p.1-2).

## 6. Validity evidence
Grounded in established moral-psychology instruments (MFQ2, Hofstede VSM, MJI/DIT/MCT), lending construct validity to the value profiles (p.3-4). Aggregate analyses show culturally coherent patterns (e.g., Arabic speakers score higher on 'purity'; English/Russian higher individualism correlating with deontology; TSNE clusters English/Spanish/Chinese apart from Arabic/Hindi) (p.5-6), acting as convergent-validity signals. Three annotators per item, but no explicit inter-annotator agreement number reported. Pilot of 100 scenarios (English, Chinese) led to merging 'legal'+'rule' into 'laws' (p.5).

## 7. Saturation / discrimination
Far from saturated — headroom is large. AP is "not significantly different from chance" for most cues (p.8); FAA "performs worse than AP and MTC" though above chance; only few-shot in MTC is statistically above chance (p.8). Strong language discrimination: high in English/Spanish/Russian, low in Arabic/Chinese/Hindi (p.7). Models do consistently better on psychologically grounded than Reddit scenarios, most pronounced in MTC/FAA (p.8).

## 8. Multiturn / agentic aspects
n/a for the LLM evaluation (single-shot prediction/generation). Conceptually framed around agent-based modeling / synthetic-persona simulation (p.6) but no interactive/tool-use protocol.

## 9. Key numbers
- 5256 total instances; 582 extensive + 882 compact per language × 6 (p.5).
- 16 seed dilemmas; 144 synthetic scenarios (16 × 9 factors) (p.3).
- ~400k Reddit dilemmas mined; 200 selected via clustering (p.4).
- 3 annotators/scenario; extensive study = 7 scenarios/annotator, compact = 30 (p.5).
- 9 contributing factors reduced to 8 (legal+rule merged) after pilot (p.5).
- Action distribution ~55/45 split across languages (Figure 2a, p.5).
- 3 LLMs tested: Phi-3.5-mini, Llama-3.1-8B, DeepSeek-R1-Distill-Llama-8B (p.6).

## 10. Pitfalls & limitations
Author-admitted (p.8-9): only four exploratory tasks, no fine-tuning; limited to 6 languages by MFQ2/VSM availability and team proficiency; Prolific sample may not represent global moral reasoning. Reviewer-observed: scenarios and actions are LLM-generated (Llama-70B) and machine-translated, risking artifacts and contamination overlap with tested Llama models; near-chance AP performance makes the benchmark's discriminative power for that task questionable; ground truth for MTC/FAA is a single annotator's highest-rated Likert principle (ties allowed), a noisy target; no reported IAA; BERTScore for CG rewards surface semantic overlap, not moral correctness.

## 11. Novel ideas worth stealing
- **Person-conditioned moral prediction**: ground truth = *this annotator's* choice given their MFQ2/VSM/persona profile — turns moral benchmarking into a steerability/persona-alignment test rather than a single-key-answer task (p.6). Directly reusable for pluralism-aware value alignment evals.
- **Pipeline decomposition**: score perception → action → principle → factor → consequence as separate stages, exposing *where* in the reasoning chain a model fails (p.3, Figure 1).
- **Multi-cue ablation harness** (morals m / culture c / persona p / few-shot fs) to measure which representation of a person's values most improves alignment — persona and explicit morals help most (p.8).
- **Paired psychological + social-media sources** with a controlled-vs-noisy contrast that itself becomes a robustness diagnostic (p.8).
- **Bundling validated instruments (MFQ2, Hofstede VSM) into the annotation** so each item carries a portable, cross-culturally comparable value vector.
- **Factor attribution** (8-way "why did they decide this") as an interpretability target beyond the binary choice.

## 12. Notable quotes
- "many existing studies overlook the critical aspect of moral evaluation: assuming only one action is moral and ignoring the decision-maker's context." (p.3)
- "while the self-descriptions provided by annotators make effective proxies for moral reasoning, LLMs still struggle to internalize ethical principles, often relying on surface-level patterns rather than genuine moral understanding." (p.8)
- "models exhibit significant performance disparities across languages... tasks like moral typology classification and factor attribution remain challenging, exposing gaps in models' ability to reason about the broader effects of moral actions." (p.8-9)

## 13. UNKNOWN / not in extract
Exact inter-annotator agreement, numeric per-model/per-task scores (only bar-chart figures described), full prompt templates, demographic composition of annotators, licensing terms, and verbatim full scenario text.
