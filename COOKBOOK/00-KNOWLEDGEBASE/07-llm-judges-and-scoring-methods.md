# 07 — LLM Judges and Scoring Methods

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-llm-judges-scoring-dossier.md` (~106 cards). `[stem]` = evidence card.
> **Scope:** how to score open-ended values content so the score means something — judge selection,
> rubric engineering, validation, calibration, aggregation, and the failure modes that invalidate
> published results.

---

## 1. The reliability regime map (when judges can be trusted)

- **System/ranking level: yes.** Judge Pearson ≥0.998 at system level even when item level is 0.638
  [Zhipu AI-AlignBench]. Leaderboards are trustworthy; per-item scores are not — aggregate over many
  items before concluding anything [2025-Anonymous-BEATS].
- **Narrow checklist-backed constructs: yes, at human level.** Judge–human ICC 0.71 vs human–human 0.67
  [2025-Hong-PrinciplismQA]; κ 0.81 vs HH 0.68 [2025-Gupta-VAL-Bench].
- **Open, adversarial, factuality-laden, or multilingual content: no.** GPT-4-judge F1 ~55% on complex
  jailbreaks, worse multilingually [2024-Liu-JAILJUDGE]; distilled judges collapse OOD (0.889→0.278
  [2025-Machlovi-GuardEval]); LLM judges *underperform BERT* in 6/7 low-resource languages [2025-Jigsaw].
- **The variable that decides:** construct scope. If you cannot decompose the construct into checkable
  keypoints, you cannot yet judge it reliably (open problem — no metric predicts decomposability;
  dossier §5.4).

## 2. The highest-ROI decision: rubric decomposition

Per-category/per-item rubric decomposition is a step-change, not a marginal gain: **κ 0.69 → 0.86**
from category-specific judge prompts alone [2024-Zeng-AIR-Bench]. Convergent across MedEthicsQA/MedES
keypoint checklists, PrinciplismQA (ICC 0.71), AlignBench per-dimension scoring, GVS per-item
"Evaluation Focus" [2025-Wei; 2026-Jin-MedES; 2026-He-GVS-Scale]. **Never a single global "is this
good?" prompt.** Score keypoints binary/half/zero (1 / 0.5 / 0).

For **no-ground-truth moral items**, grade the reasoning *process* against signed weighted atomic
criteria ({−3..+3}; MoReBench's 23,018 expert criteria, inter-expert κ=0.75) with two meta-evals a
values benchmark must copy: (a) **neutrality** — equally-good opposite-conclusion traces must score
equally (t=−0.59, p=0.56); (b) **judge selection by worst-case per-category F1**, not average
[2025-Chiu-MoReBench].

## 3. Judge implementation menu

| Option | Evidence | When |
|---|---|---|
| Frontier prompted judge | floor on hard content (F1 ~55% [2024-Liu-JAILJUDGE]) | prototyping; narrow constructs with strong rubrics |
| **Fine-tuned small scorer on your own human labels** | beats frontier judges on-distribution at fraction of cost: 79.5% vs 61.3% [2023-Huang-Flames]; MAE −34.8% [Zhipu AI-AlignMMBench]; F1>0.96 [2026-Jin-MedES]; 80× cheaper at comparable F1 [2025-Chiu-MoReBench] | production scoring; any benchmark with ≥number of labels to train on |
| Distilled open judge | matches API judges in-domain, collapses multilingual OOD (0.4505) [2024-Liu-JAILJUDGE] | cost-constrained monolingual |
| Classical classifier / deployed API (Perspective, Llama Guard) | inherits artifacts: German scored ~3× more toxic than its English translation [2024-Nogara]; version drift [2025-Shen-HateBench] | never as sole ground truth |
| Human panel | the calibration reference — always needed for validation, never scalable as primary | validation sets; contested items |

## 4. The validation stack (non-negotiable)

1. **Human-validate the judge with an imbalance-robust coefficient** (κw/ICC/AUPRC/PABAK) against a
   human panel, and report the human–human ceiling next to it. Raw percent agreement crowns lazy
   majority-class judges [2024-Wynter-RTP-LX]. A judge without a human-agreement number is unvalidated.
2. **≥2 judges from different model families + published disagreement** (per-judge ANOVA, offsets,
   Dempster–Shafer fusion — DS lifts F1 0.55→0.91 [2024-Liu-JAILJUDGE]; peer-review-no-self-judging
   panels reach Fleiss κ=0.67, r=0.74 vs WVS [2025-Mohammadi-EvalMORAAL]).
3. **Kill circularity**: never let one family generate items AND judge them (helpfulness flips sign by
   evaluator: Gemini +7.8% vs Claude −7.4% [2025-Madan-ArGen]); **never use LLM-annotated gold** —
   same-source reward models gain 10.8–19.2% on GPT-4-annotated subsets vs ~2.2% on human ones
   [NVIDIA-HelpSteer2-Preference]. Cross-generator QC (Claude checks GPT items) is the cheap fix
   [2026-Shen-PsychEthicsBench].
4. **Calibrate and anchor**: rule-calibrated intervals, reference answer anchored at 8/10 (leaves
   headroom), per-dimension scoring, length correction (verbosity is a proven confound — GPT-4o advice
   beat a professional ethicist 74% via moral-language density, not substance [2025-Dillion]; ~5% of
   RLHF "advantage" vanishes after length control [OpenAI-learning-to-summarize-rlhf]).
5. **Adversarially test the rubric itself** — professional red-teamers beat the *rubric* (benign
   paraphrase, padding), not the classifier [Anthropic-Constitutional_Classifiers]. Include
   refusal-as-evasion probes: consistency metrics correlate ρ=0.91 with refusal rates — "a consistently
   evil agent would also score highly" [2025-Gupta-VAL-Bench].
6. **Check judge willingness-to-grade** — judges differ in refusing to grade harmful content (GPT-4o 0%
   vs Claude 3.5 27.2% refusal to judge [2024-Kaiyom-HELM Safety]); a refusing judge silently biases
   your sample.

## 5. Metric hygiene

- **Never bare accuracy under class imbalance** (dummy classifier beats GPT-3.5 [2025-Ishmam-BanTH]);
  macro-F1/AUPRC/AP for rare-class constructs (hate prevalence 0.7% → average precision
  [2024-Tonneau-HateDay]).
- **Ordinal harm → deployment-matched metrics** (CEM/RBP/MAE, recall-weighted composites)
  [2021-Taulé-DETOXIS].
- **Reference-based n-gram metrics (ROUGE/BLEU) are invalid for moral content** — ROUGE-2 of 3.68 on
  answers humans rated comparable to experts [2023-Bang-AISOCRATES]; ROUGE-scored "moral alignment" is
  an anti-pattern [2024-Dognin]. BERTScore tracks human judgment best among cheap metrics.
- **State the refusal policy** — four incompatible policies coexist in the literature (pass / penalize /
  exclude / co-report); adopt doc 01 Adjudication 3 (four-way taxonomy + over-refusal co-report) and
  say so explicitly.
- **CoT is not validity evidence** (Law 5) — score it only as an auxiliary construct with faithfulness
  reported separately [Anthropic-Language_Models_Dont_Always_Say; 2025-Samway-MORALLENS].

## 6. Interpretable & steerable aggregation (the frontier)

Expose the aggregation so communities can re-weight it: SafetyAnalyst's 28 human-readable harm/benefit
weights fittable to a community's labels (F1 0.81 vs <0.72 prior) [2025-Li-SafetyAnalyst]; policy-configurable
category re-weighting (M-ALERT: removing two categories shifts "safety" ~2% [2024-Friedrich]); KorNAT's
three scoring variants exposing opinionated-vs-neutral dispositions [2024-Lee-KorNAT]. For genuinely
contested aggregation, report per-framing leaderboards [2024-Defrance-ABCFair] — no consensus aggregator
for moral pluralism exists (dossier §5.1; doc 12).

## 7. Scoring-spec checklist

- [ ] Scoring target chosen by construct scope (verdict / process / behavior / consistency)
- [ ] Per-item keypoint rubric (1/0.5/0); signed weighted criteria for open items; neutrality meta-eval
- [ ] Judge implementation: fine-tuned scorer preferred; OOD generalization reported per language
- [ ] ≥2 cross-family judges; disagreement published; DS or equivalent fusion for hard content
- [ ] Judge validated vs human panel (κw/ICC) with human–human ceiling; imbalance-robust metric
- [ ] No LLM-annotated gold; no generator=judge family overlap; cross-generator QC
- [ ] Calibration: interval rules, 8/10 anchor, length correction, verbosity control
- [ ] Rubric red-teamed (paraphrase/padding/refusal-evasion); judge willingness-to-grade audited
- [ ] Refusal policy stated; over-refusal co-reported
- [ ] Aggregation exposed and re-weightable; per-framing reporting where contested

**Drill-down:** `20260705-llm-judges-scoring-dossier.md` §2 (the 9-layer decision stack), §3 (CoT-trust
and refusal-policy disputes), §4 (AIR-Bench, MoReBench, PrinciplismQA, VAL-Bench, JAILJUDGE, RTP-LX
exemplars; ELAB maximal-circularity anti-pattern).
