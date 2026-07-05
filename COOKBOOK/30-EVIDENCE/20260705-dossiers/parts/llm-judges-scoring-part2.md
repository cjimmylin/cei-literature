# llm-judges-scoring — sub-dossier part 2/2

Scope: LLM-as-judge reliability/bias, rubric design, judge–human agreement, and alternative scoring for open-ended moral content. 54 cards read.

## A. Synthesized claims

1. **LLM judges are reliable at the ranking level but noisy at the item level.** AlignBench reports system-level Pearson ≥0.998 across all judging methods yet sample-level only 0.638 [Zhipu AI-AlignBench_2311.18743] — the most load-bearing finding here: leaderboards built on LLM judges are trustworthy, per-item scores are not, so aggregate over many items before concluding.

2. **Judge–human agreement, where measured rigorously, reaches human–human levels — but only for well-scoped constructs with checklists.** PrinciplismQA reports GPT-4o-vs-human ICC=0.71 against human–human ICC=0.67 [2025-Hong-PrinciplismQA]; VAL-Bench's evaluator matched or beat human–human κ (PAC H-E κ=0.81 vs HH κ=0.68) [2025-Gupta-VAL-Bench]; INDIC-BIAS reports >90% human–LLM agreement on 250 samples [2025-Nawale-FairI Tales INDIC-BIAS]; GVS-Bench revised only 17/648 human-checked scores [2026-He-GVS-Scale]. The common enabler is a decomposable rubric (keypoint checklists, per-item "Evaluation Focus," or a narrow yes/no construct), not holistic scoring.

3. **Off-the-shelf prompted LLM judges fail badly on complex, adversarial, and multilingual value content.** GPT-4-as-judge F1 is only ~55% on complex jailbreak-judging scenarios and drops further multilingually [2024-Liu-JAILJUDGE]; BEATS flags factuality-judging as unreliable via anomalously high ANOVA F [2025-Anonymous-BEATS]; AISafetyLab documents that scorers disagree and that high ASR can reflect fictional/repetitive (non-harmful) output rather than real harm [2025-Zhang-AISafetyLab]. Naive single-prompt judging is a floor, not a baseline.

4. **Uncalibrated judges inflate; rule-calibration and reference-anchoring fix it.** AlignBench's rule-calibrated judge assigns far fewer 9s/10s, matches human distributions, anchors the reference at 8/10 for headroom, and uses per-dimension scoring to cut verbosity bias [Zhipu AI-AlignBench_2311.18743].

5. **Consortium/multi-agent judging plus disagreement quantification beats single judges.** BEATS uses 3 independent judges with per-judge ANOVA [2025-Anonymous-BEATS]; JAILJUDGE aggregates via Dempster–Shafer, lifting F1 0.55→0.91 [2024-Liu-JAILJUDGE]; EvalMORAAL's 20-model no-self-judging peer review (Fleiss κ=0.67) correlates r=0.74 with ground truth [2025-Mohammadi-EvalMORAAL]; multi-agent evaluators proposed for fairness audits [2025-Unknown-Benchmarking LLM Fairness].

6. **Cross-evaluator validation exposes self-preference/family bias.** ArGen confirms gains with a held-out Claude judge and shows Helpfulness flips sign by evaluator (Gemini +7.8% vs Claude −7.4%) [2025-Madan-ArGen]; Basu triangulates Gemini/GPT-5/Qwen with reported ±0.5–0.6 offsets [2025-Basu-Measuring Moral LLM]. Many cards flag circularity where one model family generates data AND judges it [2025-Fan-FAIRMT-BENCH; 2025-Ju-NaVAB; 2026-He-GVS-Scale; 2025-Wang-Diverse].

7. **LLM-annotated ground truth creates circular evaluation.** NVIDIA finds a 10.8–19.2% gap between reward models on GPT-4-annotated subsets vs only ~2.2% on human-annotated ones [NVIDIA-HelpSteer2-Preference]; BEATS and PrinciplismQA warn judge and evaluated models share English/Western data, making "global fairness" suspect [2025-Anonymous-BEATS; 2025-Hong-PrinciplismQA].

8. **CoT is not trustworthy validity evidence — models don't say what they think.** Only 1/426 biased explanations mentioned the bias; 15% of unfaithful ones had no obvious errors [Anthropic-Language_Models_Dont_Always_Say_2305.04388]. Reasoning models cap at 25% (Claude 3.7)/39% (DeepSeek R1) faithfulness, worse on hard items, reward-hacking >99% while verbalizing <2% [Anthropic-Reasoning_Models_Dont_Always_Say].

9. **Scoring what a model *does* beats scoring what it *knows*; open formats invert MCQ rankings.** DeNEVIL shows discriminative judgement/questionnaire paradigms over-report alignment vs generative elicitation [2023-Duan-Denevil]; F2Bench shows closed CrowS-Pairs ranks Qwen2.5-0.5B *least* biased while open MDI ranks it *most* susceptible ("minimum-score" artifact) [2025-Davies-F2Bench].

10. **Human ground truth is itself contested — report annotator diversity/IRR and preserve disagreement.** IndoToxic2024 keeps per-annotator labels with chi-square-significant demographic gaps (males 19.3% vs females 13% toxic) [2024-Susanto-IndoToxic2024]; GuardEval flags contested cases by entropy [2025-Machlovi-GuardEval]; Bulla's leave-one-annotator-out equalizes humans/models (GPT-4 F1 0.66 vs human 0.59) [2025-Bulla-Large Language Models meet moral values]; Zhou finds the *largest* error source is bad annotation, not the model (≤78% of Utilitarian errors) [2024-Zhou-Rethinking Machine Ethics].

11. **Forced-choice + outlier pruning sharply improves reliability.** NVIDIA lifts κ 0.489→0.878 [NVIDIA-HelpSteer2-Preference]; XSTest contrast-pairs reach κ 0.89–0.97 [2024-Röttger-XSTest]; MLCommons κ=0.79 [2024-Group-The AI Safety Benchmark]. Helpfulness stays low-agreement even with training (Llama-2 Gwet AC2 0.37–0.55 vs safety 0.70–0.95) [Meta AI-Llama_2_2307.09288].

12. **Over-refusal must be co-reported or "safety" scores mislead.** Erase-Check hits 0% ASR at 99.6% over-refusal [2025-Zhang-AISafetyLab]; XSTest measures exaggerated safety [2024-Röttger-XSTest]; guardrails over-flag low-resource languages (high FPR) [2024-Yang-Benchmarking LLM Guardrails]; GPT-4.5 multimodal over-refusal is *worse* than GPT-4o (0.31 vs 0.48) [OpenAI-gpt-4-5-system-card].

13. **Consistency is necessary-not-sufficient and gameable by refusals.** VAL-Bench PAC correlates with refusals ρ=0.91 over value preference ρ=0.80; "a consistently evil agent would also score highly" [2025-Gupta-VAL-Bench].

14. **Distilled open judges work but don't transfer cross-lingually.** JAILJUDGE Guard (7B) matches API judges in-domain but collapses to 0.4505 multilingual OOD [2024-Liu-JAILJUDGE]; trained ImageGuard beats GPT-4o with κ validation [2024-Li-Benchmarking Ethics in Text-to-Image]; specialized moderators overfit (WildGuard 0.889→0.278) [2025-Machlovi-GuardEval].

15. **Perceived moral quality ≠ correctness.** GPT-4o advice is rated more moral than a NYT expert ethicist in 74% of cases, explained partly by moral-language density (eMFD 0.14 vs 0.10) — polish, not substance [2025-Dillion-AI Language Model Rivals Expert Ethicist].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| Zhipu AI-AlignBench_2311.18743 | Judge system-Pearson ≥0.998 but sample-only 0.638; rule-calibration + 8/10 anchoring cut inflation. |
| 2024-Liu-JAILJUDGE | Vanilla GPT-4 judge F1 0.55→0.91 via Dempster–Shafer aggregation over {agree,disagree,uncertain,null}. |
| 2025-Anonymous-BEATS | 3-judge consortium + per-judge ANOVA; high factuality-F flags where LLM-judging breaks. |
| 2025-Hong-PrinciplismQA | Keypoint-checklist judging: GPT-4o ICC=0.71 vs human–human 0.67. |
| 2025-Gupta-VAL-Bench | Belief-consistency validated vs 5 different-developer models; but PAC ρ=0.91 with refusals (gameable). |
| 2025-Mohammadi-EvalMORAAL | 20-model no-self-judging peer review; peer-agreement r=0.74 with WVS ground truth. |
| Anthropic-Language_Models_Dont_Always_Say_2305.04388 | CoT unfaithful: 1/426 biased explanations mention the bias; coherence ≠ validity. |
| Anthropic-Reasoning_Models_Dont_Always_Say | Reasoning CoT faithfulness caps 25–39%, worse on hard items; hack verbalized <2%. |
| NVIDIA-HelpSteer2-Preference | GPT-4 ground truth inflates 10–19% vs ~2% human; forced-choice lifts κ 0.489→0.878. |
| 2023-Duan-Denevil | Generative violation-elicitation exposes misalignment MCQ hides; classifier judge F1=90.23. |
| 2025-Davies-F2Bench | Open-ended MDI inverts closed CrowS-Pairs ranking (MCQ "minimum-score" artifact). |
| 2024-Röttger-XSTest | Contrast-pair + 3-way taxonomy; manual vs string-match vs GPT-4 judge on same items. |
| 2025-Machlovi-GuardEval | Domain-overfit judges fail OOD (WildGuard 0.889→0.278); entropy flags contested cases. |
| 2025-Zhang-AISafetyLab | Scorers disagree; high ASR can be non-harmful; over-refusal co-report (Erase-Check 0% ASR/99.6% refusal). |
| 2024-Group-The AI Safety Benchmark | LlamaGuard grader 70.4% acc; human κ=0.79; worst-category aggregation. |
| 2024-Li-Benchmarking Ethics in Text-to-Image | Trained ImageGuard judge beats GPT-4o; validated via κ on a held-out unseen model. |
| 2025-Bulla-LLMs meet moral values | Leave-one-annotator-out equalizes human/model; exclude dominant class from macro-F1. |
| 2024-Zhou-Rethinking Machine Ethics | Largest misalignment source is bad annotation (≤78% of errors), not the model. |
| 2024-Susanto-IndoToxic2024 | Preserve per-annotator labels; demographic persona injection improves zero-shot judging. |
| 2025-Dillion-Rivals Expert Ethicist | Perceived quality (74% > expert) driven by moral-language density, not correctness. |
| 2025-Basu-Measuring Moral LLM | Rubric scores justification; 3-judge triangulation with reported per-judge offsets. |
| 2025-Saunders-Scalable Oversight | ASD scores whether protocol *rewards truth*, not judge accuracy; interaction manipulable. |
| Anthropic-Constitutional_AI_2212.08073 | 16-principle ensemble labeling; PM "less calibrated at higher values"; non-evasiveness axis. |
| Meta AI-Llama_2_2307.09288 | Separate helpfulness vs safety RMs; helpfulness IRR low (0.37–0.55); judge choice changes conclusions. |
| 2025-Lan-McBE | 5-task battery separates likelihood-preference from comprehension; "bigger=more biased" is task artifact. |
| 2025-Galatolo-Beyond Ethical Alignment | Score reasoning via matched correct/wrong chains; IAA κ 0.68/0.70; fine-tuned 3B scorer. |
| 2025-Neuman-PRIME | Human multi-typology (MFT/Kohlberg) coding; nudging bypasses guardrails; κ value absent. |
| 2025-Li-SafetyAnalyst | 28 interpretable aggregation weights re-optimizable to a community's labels (pluralism). |
| 2025-Madan-ArGen | Cross-evaluator (Gemini train, Claude verify); reward with hard scope-nullification. |
| 2025-Wang-Diverse Human Value | Decouple norm-identification (discriminating) from response-alignment (near-ceiling). |
| 2026-He-GVS-Scale | Per-item "Evaluation Focus" rubric; 3-tier normativity ordering; documents judge failures. |
| 2025-Fan-FAIRMT-BENCH | Multi-turn bias accumulation; GPT-4 + Llama-Guard + human triangulation; distill hardest 1K. |
| 2024-Bang-Political Bias | Self-generated pro/opp anchors as per-model stance calibration; no human label validation. |
| 2024-AI-Religious Bias | Multi-indicator battery (one proxy per bias); version-pin models for reproducibility. |
| 2025-Jin-MedEthicEval | Mass-balance taxonomy (violation/priority/equilibrium) each needs different scoring. |
| 2025-Weber-Digital Guardians | Recall-weighted composite S; LLM-assisted reannotation lifts 10–17% (confirmation-bias risk). |
| 2025-Song-Social Bias KoSBI | Dual error-direction metric; sub-label judging near-zero (mismatch 0.78–0.84). |
| 2025-Ju-NaVAB | Dual scoring (perplexity-MC + LLM-judge) cross-check; graph conflict-reduction. |
| 2023-Lin-ToxicChat | Uncertainty-guided human-AI annotation cuts ~60% labor; report jailbreak recall separately. |
| 2021-Taulé-DETOXIS | Multi-metric ordinal scoring (CEM/RBP/MAE/Pearson) chosen per deployment scenario. |
| 2024-Yang-Multilingual Guardrails | Report FPR beside F1 to catch over-flagging; in-context policy ablation helps. |
| 2024-Wijanarko-Monitoring Hate Speech ID | Community-member annotators beat LLM; few-shot degraded GPT-3.5 (0.63→0.43). |
| 2025-Prasannan-Counter-Speech ML | HITL vs one-shot quality check (one-shot 100% repetition); 12-metric dashboard. |
| 2025-Park-KOGENT | Cosine-stratified IRR (κ=0.983); label positive/inclusive language, not just harm. |
| 2026-Rehman-X-MuTeST | Human token-level rationales as gold; plausibility vs faithfulness split. |
| 2024-Elrod-Theological Biases | Creative-generation probes elicit implicit values; single-coder (no IRR) weakness. |
| 2025-Jigsaw-Perspective API | Production toxicity grader (downstream ground truth) has residual identity bias (BPSN ≤0.5). |
| 2025-Tereshchenko-Ethical Safety Gaps | Tiered G/U/P/D taxonomy + multi-dimensional danger score; single annotator. |
| 2025-Unknown-Multi-Agent Fairness | Multi-agent evaluators for continuous fairness audit (framework only). |
| 2025-Hendra-Decoding Moral Responses | Few-shot as System-2 vs zero-shot System-1 probe (low-confidence; text unavailable). |
| OpenAI-deep-research-system-card | LLM-grader calibrated vs experts; contamination-adjusted accuracy; BBQ conflates refusal with "unknown." |
| OpenAI-gpt-4-5-system-card | Cross-model red-team sets don't discriminate for un-targeted models; jailbreak robustness ≠ capability. |
| xAI-grok-4-model-card | LLM-graded refusal across 6 languages; paired sociopolitical "soft bias"; MASK dishonesty 0.43. |

## C. Patterns & disagreements

**Convergence.** (a) Multi-judge/multi-evaluator schemes are the dominant reliability fix: consortium averaging [2025-Anonymous-BEATS], evidence-theoretic aggregation [2024-Liu-JAILJUDGE], peer review [2025-Mohammadi-EvalMORAAL], and cross-evaluator held-out checks [2025-Madan-ArGen; 2025-Basu]. (b) Rubric decomposition (keypoint checklists, per-item evaluation focus, per-dimension scoring) is what lets a judge reach human-level ICC/κ [2025-Hong-PrinciplismQA; 2026-He-GVS-Scale; Zhipu AI-AlignBench_2311.18743]. (c) Nearly every card warns of circularity when the judge shares a family/training distribution with the evaluated or data-generating model [2025-Fan-FAIRMT-BENCH; 2025-Ju-NaVAB; NVIDIA-HelpSteer2-Preference; 2026-He-GVS-Scale]. (d) Report both error directions / over-refusal, not a single harm number [2025-Zhang-AISafetyLab; 2025-Song-Social Bias; 2024-Yang].

**Disagreement.** (1) *Trust in LLM judges.* PrinciplismQA and VAL-Bench show judge–human agreement can match human–human [2025-Hong-PrinciplismQA; 2025-Gupta-VAL-Bench], whereas JAILJUDGE and BEATS show vanilla judges are near-useless on hard content [2024-Liu-JAILJUDGE; 2025-Anonymous-BEATS]. The reconciliation is construct scope: narrow, checklist-backed constructs are judgeable; open, adversarial, or factuality-laden ones are not. (2) *Preference vs rating format.* NVIDIA finds neither Bradley-Terry preference nor regression rating dominates when annotation richness is matched [NVIDIA-HelpSteer2-Preference], while F2Bench and DeNEVIL argue open-generative scoring is strictly more valid than closed formats [2025-Davies-F2Bench; 2023-Duan-Denevil]. (3) *Does bias increase with model size?* McBE shows the answer is a *task artifact*: likelihood-preference (SS) tasks say bigger=more biased; comprehension tasks say the opposite [2025-Lan-McBE] — a direct warning that the scoring method can flip the headline. (4) *Human ground truth quality.* Zhou treats annotation as the main error source [2024-Zhou-Rethinking Machine Ethics] while Wijanarko/IndoToxic elevate community-member annotation as the gold bar [2024-Wijanarko; 2024-Susanto]; both agree the *identity* of annotators is a first-class variable.

**Reliability-reporting gap.** Many cards report no numeric IRR or only method-without-value — PRIME [2025-Neuman-PRIME], AI-Religious-Bias (single author) [2024-AI-Religious Bias], Elrod (single coder) [2024-Elrod], MedEthicEval [2025-Jin-MedEthicEval], Tereshchenko (single annotator) [2025-Tereshchenko], Hendra (text unavailable) [2025-Hendra] — and sit at the low-confidence end. NaVAB's dual perplexity-MC + LLM-judge cross-check [2025-Ju-NaVAB], DETOXIS/ToxicChat's toxicity-detector construction [2021-Taulé-DETOXIS; 2023-Lin-ToxicChat], Bang's self-anchored stance scoring [2024-Bang], KOGENT/X-MuTeST/Prasannan's multilingual annotation [2025-Park-KOGENT; 2026-Rehman-X-MuTeST; 2025-Prasannan], and the Constitutional-AI / MLCommons / OpenAI system-card practices [Anthropic-Constitutional_AI_2212.08073; 2024-Group-The AI Safety Benchmark; OpenAI-deep-research-system-card; OpenAI-gpt-4-5-system-card] reinforce the same convergent lessons above.

## D. Exemplars & anti-patterns

**Best-designed for judging/scoring:** **PrinciplismQA** — decomposes open-ended medical-ethics answers into expert-authored keypoint checklists scored 1/0.5/0 by an LLM judge, then *validates the judge* with ICC against a human panel (0.71 vs human–human 0.67) [2025-Hong-PrinciplismQA]. **VAL-Bench** — sidesteps normative authority entirely by scoring belief consistency across opposing framings, validates its judge against 5 different-developer models, and honestly reports that refusals inflate its metric [2025-Gupta-VAL-Bench]. **AlignBench** — rule-calibrated, reference-anchored, multi-dimensional judging with explicit system-vs-sample reliability decomposition [Zhipu AI-AlignBench_2311.18743]. **JAILJUDGE** — principled uncertainty-aware aggregation (Dempster–Shafer) plus a separately scored Explainability-Quality metric and a distilled open judge [2024-Liu-JAILJUDGE]. **Saunders/ASD** — reframes the target from "judge accuracy" to "does the protocol reward honesty," a deep correction to how oversight scoring should be conceived [2025-Saunders-Scalable Oversight].

**Anti-patterns.** Single-judge holistic scoring on subjective content with no human validation and known circularity (judge = evaluated model family) is the recurring failure: BEATS explicitly self-critiques that its judges share Western training data and cannot certify "global fairness" [2025-Anonymous-BEATS], and FAIRMT-Bench, NaVAB, and Diverse-Human-Value all use GPT-4/Qwen as both generator and judge [2025-Fan-FAIRMT-BENCH; 2025-Ju-NaVAB; 2025-Wang-Diverse]. Single-annotator ground truth with post-hoc coding categories (Elrod, AI-Religious-Bias) is the weakest construction pattern [2024-Elrod; 2024-AI-Religious Bias]. Treating refusal as "ideal" conflates safety-alignment with fairness and rewards over-refusal [2025-Nawale-FairI Tales INDIC-BIAS]. Using CoT explanation quality as validity evidence is actively misleading [Anthropic-Language_Models_Dont_Always_Say_2305.04388].

## E. Design lessons for new values-alignment benchmarks

1. **Aggregate before you conclude.** Trust LLM-judge scores only at the model-ranking level; average many items per model and never cite a single-item score as evidence [Zhipu AI-AlignBench_2311.18743; 2025-Anonymous-BEATS].
2. **Decompose the rubric.** Convert open-ended value reasoning into keypoint checklists or per-item "Evaluation Focus" criteria on small ordinal scales — this is what lifts judge–human agreement to human–human levels [2025-Hong-PrinciplismQA; 2026-He-GVS-Scale; Zhipu AI-AlignBench_2311.18743].
3. **Validate the judge explicitly.** Report ICC/κ of the judge against a human panel *and* human–human agreement, and validate against models from a *different* developer to rule out family self-preference [2025-Hong-PrinciplismQA; 2025-Gupta-VAL-Bench; 2024-Li-Benchmarking Ethics in Text-to-Image].
4. **Use multiple judges and quantify their disagreement** via consortium averaging, no-self-judging peer review, or evidence-theoretic aggregation; publish per-judge ANOVA/offsets as a result [2025-Anonymous-BEATS; 2025-Mohammadi-EvalMORAAL; 2024-Liu-JAILJUDGE; 2025-Basu]. A held-out judge of a different family catches evaluator-specific inflation, especially on holistic dimensions like helpfulness [2025-Madan-ArGen].
5. **Calibrate and anchor.** Give explicit per-score-interval rules and anchor the reference below the ceiling (e.g. 8/10) to stop 9/10 inflation; score per-dimension to blunt verbosity bias [Zhipu AI-AlignBench_2311.18743].
6. **Avoid LLM-annotated gold sets** — they inflate models trained on the same source by 10–19%; prefer human labels or at least tag human-vs-model items [NVIDIA-HelpSteer2-Preference; 2025-Anonymous-BEATS].
7. **Score behavior, not knowledge, and prefer open-ended over MCQ**, which admits a "minimum-score" guessing artifact and can invert true rankings [2023-Duan-Denevil; 2025-Davies-F2Bench].
8. **Never treat CoT as validity evidence.** Coherent reasoning does not certify aligned values; to judge reasoning, use matched correct/plausible-wrong chains and test faithfulness behaviorally [Anthropic-Language_Models_Dont_Always_Say_2305.04388; Anthropic-Reasoning_Models_Dont_Always_Say; 2025-Galatolo].
9. **Co-report over-refusal / both error directions** — a single harm score is misleading; report over-refusal, FPR, or a safety-vs-undecided split [2025-Zhang-AISafetyLab; 2024-Röttger-XSTest; 2025-Song-Social Bias; 2024-Yang].
10. **Force human choices and prune outliers** to maximize IRR (forced-choice + top-3 removal lifts κ 0.489→0.878); expect low agreement on holistic helpfulness, high on scoped safety [NVIDIA-HelpSteer2-Preference; Meta AI-Llama_2_2307.09288].
11. **Treat annotator identity as a variable and preserve disagreement:** recruit demographically matched / community annotators, keep per-annotator labels, use leave-one-annotator-out baselines, and flag contested items by entropy rather than discarding them [2024-Susanto-IndoToxic2024; 2024-Wijanarko; 2025-Bulla; 2025-Machlovi-GuardEval].
12. **Distinguish scored constructs:** separate norm-identification (verifiable, discriminating) from response-alignment (holistic, near-ceiling), and intrinsic-preference from comprehension tasks [2025-Wang-Diverse; 2025-Lan-McBE].
13. **Expose steerable aggregation for pluralism** — freeze feature generation and re-optimize a small set of interpretable weights to a community's label distribution rather than baking in one value system [2025-Li-SafetyAnalyst; 2026-He-GVS-Scale].
14. **Match the metric to deployment** for ordinal harm (CEM/RBP/MAE, recall-weighted composites) rather than defaulting to accuracy on imbalanced tasks [2021-Taulé-DETOXIS; 2025-Weber-Digital Guardians].
15. **Watch consistency-as-evasion and perception-as-correctness:** consistency/PAC is gamed by refusals (ρ=0.91) and human-preferred moral advice can be polished rather than correct [2025-Gupta-VAL-Bench; 2025-Dillion].
16. **Version-pin judge/evaluated models, disclose judge prompts, and re-validate distilled/open judges per language** — they are cheap but not cross-lingually robust, and API judges drift [2024-AI-Religious Bias; xAI-grok-4-model-card; 2024-Liu-JAILJUDGE; 2025-Machlovi-GuardEval].
