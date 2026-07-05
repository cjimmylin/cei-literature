# validity-psychometrics — sub-dossier part 5/6

Scope: 58 cards (53 papers, 5 AI-lab), skewed toward multilingual harm/hate-speech datasets and moral-values benchmarks. It is rich on inter-rater reliability (IRR), annotator-expertise effects, and construct-validity critiques; a small cluster (Jiang, Chen-MoVa, Mahajan, Anthropic-CoT, NVIDIA-HelpSteer) supplies the heavier psychometric machinery (IRT, factor structure, faithfulness).

## A. Synthesized claims

1. **Inter-rater reliability on "is-this-harmful/biased" labels is chronically low-to-moderate, and it degrades exactly where the construct is hardest.** Reported agreement spans a wide band: KoSBI context-safety Krippendorff α=0.459 and sentence-level α=0.256 [2023-Lee-KoSBI]; German IWG Hatespeech α=38.29% up to Covid2021 α=91.50% within a single language survey [2024-Bertram-Comparative Survey of German Hate Speech Datasets Background]; German TikTok Fleiss κ=0.40 [2025-Fillies-A novel German TikTok hate speech dataset]; ETHOS Fleiss κ=0.814 overall but 0.977 for the crisp "Disability" category [2020-Mollas-ETHOS an Online Hate Speech Detection Dataset]. The pattern: concrete, lexically-anchored categories agree; contextual/pragmatic judgments (context safety, counter-speech, moral sentiment) collapse.

2. **Annotator expertise materially changes both labels and downstream model scores — laypeople systematically under-count harm.** Expert re-annotation of the Polish cyberbullying corpus raised IRR from layperson κ≈0.325–0.378 (fair) to expert κ=0.451–0.517 (moderate) and *nearly doubled* the count of harmful labels [2024-Ptaszynski-Expert-Annotated Dataset to Study Cyberbullying in Polish Language]. This is corroborated by the ETHICS relabeling audit, where expert labels disagreed with crowdworkers on 19% of utilitarianism pairs [2024-Hancox-Li-Is ETHICS about ethics]. Expert-annotated resources (HateBR 2.0 Cohen κ=0.75 / Fleiss κ=0.74) reach usable agreement [2025-Vargas-Context-Aware and Expert Data Resources for Brazilian Portuguese Hate].

3. **Human-baseline gaps are the most reused validity signal, and often large.** Scruples RoBERTa F1=0.305 on ANECDOTES vs human 0.490 [2021-Lourie-Scruples]; TrolleyBench top model ECI 0.708 ≈ human 0.711 [2025-Zhu-TrolleyBench]; SpeciesismBench models 1.8–3.3 vs human ~3.6 (N=1,122) [2025-Jotautaite-SpeciesismBench]. Where models already match humans, the discriminating signal must come from consistency/perturbation, not accuracy.

4. **Item-response theory can convert a static, saturating pool into an adaptive, contamination-resistant instrument — the strongest psychometric exemplar in this set.** GETA fits IRT-2PL for per-item difficulty and discrimination, keeps only high-discrimination items, and generates new items at the model's ability frontier, reaching concurrent validity Va-L 0.8897 (vs 0.4309 without its variational item response module) while administering only ~150 adaptive items instead of the 15k seed pool [2025-Jiang-Raising the Bar]. This is a template for a non-saturating values benchmark.

5. **Predictive/concurrent validity against an existing instrument is achievable and should be reported.** Pikuliak's stereotype rate gs correlates with WinoBias at Pearson ρ=0.95 (p=1.06e−5), an explicit cross-benchmark convergent-validity check [2024-Pikuliak-Women Are Beautiful Men Are Leaders]. Cross-lingual FSB scorer reports MSE 0.057, Pearson r=0.85 against human scores [2026-Reaj-Cross-Lingual Probing]. GETA's concurrent-validity number (claim 4) is the same move at instrument level.

6. **Factor structure of borrowed survey instruments is frequently dirty — items load on multiple constructs.** MoVa's LLM audit of the PVQ found 17 of 40 questionnaire items multi-loaded on 2–3 dimensions [2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values]; ValueCompass operationalizes 56 Schwartz values across 10 motivational types but reports max alignment F1 only 0.529 [2025-Shen-ValueCompass]. NVIDIA showed 4 of 5 helpfulness attributes account for 73.0% of variance (correctness R=0.85, but verbosity R=0.26), i.e. nominally separate attributes are partly redundant [NVIDIA-HelpSteer].

7. **Scores are fragile to superficial, validity-irrelevant perturbations.** Surface edits flip moral judgments in 7.5% of cases, POV shifts in 24.3%; protocol choice alone yields only 67.6% agreement [2026-vanNuenen-Fragility of Moral Judgment]. Cheung shows amplified human cognitive-bias structure: 45% commission–omission gap vs 5% for humans, yes–no framing swinging preference 51%→89% [2025-Cheung-LLMs Amplified Cognitive Biases Moral]. Khamassi documents non-repeatability: Gemini gave 3 different response types to the same prompt [2024-Khamassi-Strong and weak alignment].

8. **Recognition ≠ endorsement: accuracy-only scoring can miss the values construct.** SpeciesismBench models classify 86% of statements as speciesist but judge only 34% morally wrong — a 52-point gap invisible to single-label designs [2025-Jotautaite-SpeciesismBench]. Bai's dual metric shows implicit word-association bias (t(33,599)=76.39, P<0.001) predicts explicit decision bias (b=0.986) in models passing explicit-bias checks [2025-Bai-Explicitly unbiased LLMs still form biased].

9. **LLM-as-judge validity must be measured, and Percentage Agreement inflates it.** RTP-LX human IRR was weighted κ=0.62±0.2; best model (GPT-4 Turbo) landed 0.22 below humans, and Llama Guard topped raw PA but near-last on κw — a lazy learner exposed only because κw penalizes majority-class guessing [2024-Wynter-RTP-LX]. DeepSeek reports judge-human consistency >95% on a different (safety-refusal) task [DeepSeek-DeepSeek-R1].

10. **Stated reasoning is often post-hoc, so CoT/rationale scoring is not automatically valid.** Anthropic's AOC shows 44% answer change on CoT truncation (AQuA) vs 2% (ARC-Easy), with faithfulness *lower* for 175B than 13B (inverse scaling, 7/8 tasks); filler tokens give no gain [Anthropic-Measuring_Faithfulness_in_CoT]. MFTCXplain finds moral-rationale F1 <0.35 while hate-speech F1 reaches 0.836 [2025-Trager-MFTCXplain].

11. **Effect-size + significance reporting (WEAT d, t-tests, CIs), including nulls, is the norm for the strongest cards.** Origin bias German d=1.134, French d=1.29 (p<0.001), with math/science *non-significant* (p=0.65/0.83) [2020-Kurpicz-Briki]; Mahajan reports ARI 0.475 [CI 0.346,0.645] and Kruskal–Wallis H tests [2025-Mahajan]. A formal validity catalog now exists: BenchRisk lists 57 failure modes / 196 mitigations across 26 benchmarks, all carrying significant risk in ≥1 of 5 dimensions [2025-McGregor-BenchRisk].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Rudinger-Gender Bias in Coreference Resolution | Minimal-pair "gotcha" design + 94.9% worker agreement with intended answers validates the item template (p.2-3) |
| 2019-Ibrohim-Multi-label Hate Speech and Abusive Language | 30 demographically-diverse annotators; 68.44% of items reached 100% first-pass agreement (p.5) |
| 2020-Mollas-ETHOS | Fleiss κ ranges 0.814 (hate) to 0.977 (disability) — crisper categories agree far better (p.7) |
| 2020-Shekhar-Automating News Comment Moderation | On real ~5-6% base-rate data, F1 collapses to 0.38 — balanced-test metrics overstate validity (p.4,13) |
| 2021-Lourie-Scruples | 626,714 judgments give distributional "soft" labels; RoBERTa 0.305 vs human 0.490 F1 gap (p.3,6) |
| 2021-Ravikiran-DOSA | Span-level offensive annotation at Cohen κ=0.6 with 85.55% OOV — code-mix stresses agreement (p.3-4) |
| 2022-Hartvigsen-ToxiGen | 90.5% of machine-generated items judged human-written; implicit-toxicity validity check (p.8) |
| 2022-Röttger-Multilingual HateCheck | 34 functional tests × 11 classes give diagnostic construct coverage per language (p.3) |
| 2023-Das-Bengali Gender | 121k+ sentence pairs across gender/religion/nationality — scale via templated minimal pairs (p.5) |
| 2023-Lee-KoSBI | Context-safety α=0.459, sentence-level α=0.256 — contextual constructs annotate poorly (p.4-5) |
| 2023-Plaza-del-Arco-MarIA and BETO | 96 paired templates (192 sentences) → 19/20 models body-adjective biased toward female (p.7,19) |
| 2023-Zhang-Heterogeneous Value Alignment | Value rationality as distance in a value space (SVO Slider game) — no gold labels needed (p.6) |
| 2024-Defrance-ABCFair | 7 fairness notions × 3 sensitive-feature formats — validity depends on which notion you pick (p.1) |
| 2024-Grigoreva-RuBia | Highest SuperGLUE model (ruRoBERTa) is also most biased — capability ≠ alignment (p.7-8) |
| 2024-Khandelwal-Indian-BhED | India-centric bias 69.5% vs US-centric 52.8% — construct coverage is geography-dependent (p.8) |
| 2024-Lin-AI-Face | 10/12 detectors AUC>98% (saturated) yet intersectional FEO up to 67.5% — fairness hidden by utility (p.6) |
| 2024-Pikuliak-Women Are Beautiful | Convergent validity: gs vs WinoBias Pearson ρ=0.95 (p=1.06e-5) (p.12) |
| 2024-Shahi-Cross-Platform Hate Speech | Cohen κ=0.86 on YouTube; base rates differ 37.4% (EN) vs 4.6% (DE) — transfer stress test (p.4) |
| 2024-Team-FABLE | Formal Sfact–SE trade-off (when Sfact=1, SE=0) makes a validity tension explicit (p.5) |
| 2024-Wynter-RTP-LX | κw over Percentage Agreement exposes Llama Guard as a lazy learner on imbalanced data (p.5) |
| 2025-Ahmed-Chinese Censorship Bias | CensorshipDetector 91% validated accuracy before use as a scoring instrument (p.5) |
| 2025-Bai-Explicitly unbiased LLMs | Implicit word-association bias predicts explicit decision bias b=0.986, P<0.001 (p.6) |
| 2025-Chen-MoVa | PVQ audit: 17/40 items multi-load on 2-3 dimensions — borrowed instruments have dirty factor structure (p.9) |
| 2025-Gamboa-Filipino Benchmarks | CrowS/WinoQueer challenge-pair paradigm ported to Filipino; mean bias 59.44 (p.7) |
| 2025-Hossain-BanHate | Binary-hate Cohen κ avg 0.78 via careful guidelines on fresh (2024-25) data (p.3) |
| 2025-Jiang-Raising the Bar | IRT-2PL adaptive testing: concurrent validity 0.8897 vs 0.4309, ~150 items (p.7) |
| 2025-Jotautaite-SpeciesismBench | 86% recognition vs 34% endorsement — accuracy-only scoring misses the values construct (p.5) |
| 2025-Lan-McBE | Rouge-L overlap <0.2 across items evidences item diversity / anti-redundancy (p.5) |
| 2025-McGregor-BenchRisk | 57 failure modes / 196 mitigations; pre-release validity checklist (p.1,3) |
| 2025-Park-KOGENT | Krippendorff α=0.983 achieved via 0.9 cosine-similarity annotation threshold (p.6) |
| 2025-Shen-ValueCompass | 56 Schwartz values × 28 scenarios × 7 countries; 8 prompt variants for robustness averaging (p.2) |
| 2025-Trager-MFTCXplain | Rationale-token IRR 0.631; moral F1<0.35 while hate F1=0.836 — rationale is the hard construct (p.5,9) |
| 2025-Zhu-TrolleyBench | ECI 0.708 ≈ human 0.711; system prompt swings ECI 0.583→0.817 (p.4) |
| 2022-Unknown-HOTTEST | Tamil MCQ hate-ID; low-confidence card, no reported IRR/headline numbers |
| 2024-Velankar-SamPar | Monolingual Marathi models beat multilingual — measurement validity is language-specific (p.8) |
| 2025-Kumar-UniMoral | 6-language moral dataset (ACL Best Resource); low-detail card |
| 2026-vanNuenen-Fragility of Moral Judgment | POV shifts flip 24.3%; protocol agreement only 67.6% — perturbation as validity test (abstract) |
| 2020-Kurpicz-Briki-Cultural Bias Origin | WEAT with effect sizes AND reported nulls (math/science p=0.65/0.83) (p.9) |
| 2022-Sahoo-Detecting Unintended Social Bias | Cohen κ=64.3; 87% of Muslim-mentioning comments biased — target-group skew audit (p.4,9) |
| 2023-Sukhamsri-Toxicity Thai | Ensemble F1 0.82 > BERT 0.66 — baseline choice governs apparent validity (p.6) |
| 2024-Bertram-German Hate Speech Survey | Cross-dataset α range 38.29%–91.50% — IRR is dataset-, not language-, determined (p.4) |
| 2024-Hancox-Li-Is ETHICS about ethics | 19% expert/crowd disagreement; 18% deontology items solvable by physics alone (construct-invalid) (p.2) |
| 2024-Khamassi-Strong and weak alignment | Same prompt, 3 different Gemini response types — non-repeatability documented (p.10) |
| 2024-Ptaszynski-Polish Cyberbullying | Expert re-annotation doubles harmful labels; κ 0.33→0.51 (p.12,20) |
| 2024-Ungless-ETHICS WHITEPAPER | 6-stage lifecycle checklist including an Evaluation-stage validity gate (p.2) |
| 2025-Cheung-Amplified Cognitive Biases | 45% commission-omission gap (vs 5% human); yes-no framing swings 51%→89% (p.3-4) |
| 2025-Fillies-German TikTok | Fleiss κ=0.40; two-tier "hateful" vs "problematic" label counts differ 13.76% vs 26.04% (p.13) |
| 2025-Mahajan-Mapping Moral Reasoning | Dictionary-ablation ARI 0.475 [CI 0.346,0.645] validates the measurement instrument (p.9) |
| 2025-Priya-Deontic Temporal Logic | Formal SMT (Z3) verification of 5 ethical properties — validity as logical proof (p.8-9) |
| 2025-Vargas-Brazilian Portuguese Hate | Expert annotation Cohen κ=0.75 / Fleiss κ=0.74 (p.10) |
| 2026-Yu-Tracing Moral Foundations | Per-foundation separability SW1 (Care 1.71, Authority near-flat 0.041) — differential construct salience (p.7) |
| Anthropic-Claude_4_System_Card | BBQ ambiguous bias 0.21% at 99.8% accuracy — paired bias+accuracy reporting (p.13) |
| Anthropic-Measuring_Faithfulness_in_CoT | AOC metric: 44% answer change on truncation; inverse scaling of faithfulness (p.5,7) |
| DeepSeek-DeepSeek-R1 | LLM-as-judge safety consistency >95% with humans (p.50) |
| NVIDIA-HelpSteer | 5 anchored Likert attributes; 4 explain 73.0% of helpfulness variance (p.4) |
| OpenAI-gpt-5.2-system-card | Refusal-as-pass scoring convention makes a validity decision explicit (bio 83.33%) (p.14) |
| 2023-Roger-Towards ethical multimodal systems | Classifier 52-55% vs crowd votes — near-chance shows weak construct capture (p.5) |
| 2026-Reaj-Cross-Lingual Probing | FSB scorer Pearson r=0.85; ~30% community data culturally misaligned (p.4-5) |

## C. Patterns & disagreements

**Convergence.** (a) Nearly every dataset card reports a kappa/alpha as validity's entry ticket — but with no shared threshold. (b) Independent cards converge that *concrete lexical categories agree and pragmatic/contextual ones do not* [2020-Mollas-ETHOS; 2023-Lee-KoSBI; 2025-Trager-MFTCXplain; 2025-Fillies-German TikTok]. (c) Capability ≠ alignment: the highest-scoring backbone is most biased [2024-Grigoreva-RuBia], saturated detectors still fail fairness [2024-Lin-AI-Face]. (d) Expert > layperson labeling is a consistent, sizeable effect [2024-Ptaszynski; 2024-Hancox-Li; 2025-Vargas].

**Disagreements / tensions.** (1) *Balanced vs base-rate testing.* Most cards report balanced-set F1, but Shekhar shows F1 crashing to 0.38 on realistic 5-6% base rates [2020-Shekhar] and Wynter shows Percentage Agreement concealing lazy learners [2024-Wynter] — the default metric choice is itself a validity threat. (2) *Human baseline as ceiling.* Zhu finds top models at the human ECI [2025-Zhu-TrolleyBench] while Lourie/Jotautaite find large gaps [2021-Lourie; 2025-Jotautaite] — "gap to human" discriminates only on hard constructs; on saturated ones, pivot to consistency/perturbation. (3) *Borrowed instrument fidelity.* MoVa/Hancox-Li argue for importing survey/theory instruments [2025-Chen-MoVa; 2024-Hancox-Li], yet MoVa's imported PVQ has 17/40 cross-loaded items and Schwartz-based ValueCompass tops out at F1 0.529 [2025-Shen] — importing is necessary but not sufficient without re-audit. (4) *LLM-as-judge trust.* DeepSeek reports >95% judge-human consistency [DeepSeek-R1] while Wynter shows best-model κw 0.22 below humans and universal microaggression blindness [2024-Wynter] — judge validity is task- and imbalance-dependent.

## D. Exemplars & anti-patterns

**Best-designed.** *2025-Jiang-Raising the Bar (GETA)*: IRT-2PL calibration, discrimination-based filtering, adaptive item generation, and an explicit concurrent-validity number (0.8897) — addressing saturation, contamination, and validity at once. *2024-Ptaszynski*: two-round layperson→expert design published as v1/v2 with a custom ordered-multiclass weighted kappa, quantifying the expertise effect. *NVIDIA-HelpSteer*: 5 named attributes with per-point behavioral anchors and a variance decomposition (73.0%). *2025-McGregor-BenchRisk*: a reusable 57-failure-mode audit checklist, itself scored at κ=0.53.

**Anti-patterns.** *2023-Roger* reports classifiers at 52-55% vs crowd votes — near chance, the construct barely captured, yet presented as a benchmark. Single balanced-set F1 with no base-rate or κw check risks Shekhar/Wynter inflation [2020-Shekhar; 2024-Wynter]. *2022-Unknown-HOTTEST* is a documentation anti-pattern: low confidence, no IRR or headline numbers — validity unassessable. Single-label recognition designs erase the 52-point recognition/endorsement gap [2025-Jotautaite]. Borrowing a survey instrument without re-auditing factor structure (ValueCompass 0.529 ceiling; MoVa 17/40 cross-loaded PVQ items) is the psychometric anti-pattern [2025-Shen; 2025-Chen-MoVa].

## E. Design lessons

1. **Report IRR with a metric that survives class imbalance.** Use weighted Cohen κ / Krippendorff α, not raw Percentage Agreement, and expect it to reveal lazy learners and skew [2024-Wynter; 2024-Bertram]. Report per-category IRR: aggregate kappa hides that pragmatic categories collapse [2020-Mollas; 2023-Lee-KoSBI].

2. **Run an expert re-annotation pass on a sample and publish both versions.** Laypeople under-count harm by ~2× and disagree with experts on ~19% of moral items; quantifying this is cheap, high-signal QA [2024-Ptaszynski; 2024-Hancox-Li; 2025-Vargas].

3. **Collect a human baseline on the same items, and pre-plan a fallback discriminator for when models saturate it** (consistency, perturbation-flip rate, endorsement-vs-recognition) [2021-Lourie; 2025-Zhu-TrolleyBench; 2025-Jotautaite].

4. **Adopt IRT for item calibration.** Fit 2PL, keep high-discrimination items, and (ideally) generate items adaptively to resist saturation and contamination while cutting item count ~100× [2025-Jiang]. Report a concurrent-validity coefficient against a reference instrument.

5. **Report convergent/predictive validity against an existing benchmark or human instrument** (Pearson/MSE), not just internal accuracy [2024-Pikuliak ρ=0.95; 2026-Reaj r=0.85].

6. **Separate recognition from endorsement, and implicit from explicit, with dual metrics** so a model cannot pass by labeling correctly while behaving badly [2025-Jotautaite; 2025-Bai].

7. **Test perturbation/protocol robustness as a first-class validity check.** Vary surface wording, POV, prompt framing, and option ordering; report flip rates — expect double-digit instability [2026-vanNuenen; 2025-Cheung; 2024-Khamassi].

8. **Validate any borrowed survey/theory instrument in-context before trusting it** — audit for multi-loaded items and reword to isolate constructs; operationalize theories structurally (test rule-*selection*, not rule-obeying) [2025-Chen-MoVa; 2024-Hancox-Li].

9. **When scoring with an LLM judge or CoT rationale, measure the judge's validity** (κw vs human, faithfulness via truncation/counterfactual AOC) before relying on it [2024-Wynter; Anthropic-Measuring_Faithfulness_in_CoT; 2025-Trager].

10. **Anchor every rating-scale point with behavioral descriptors** and decompose holistic judgments into named sub-attributes to raise IRR and expose trade-offs [NVIDIA-HelpSteer].

11. **Evaluate at realistic base rates, not just balanced sets** — F1 can fall by half on production distributions [2020-Shekhar].

12. **Report effect sizes, significance, and nulls** (WEAT d, t-tests, CIs, non-significant results) rather than bare point estimates [2020-Kurpicz-Briki; 2025-Bai; 2025-Mahajan].

13. **Pre-audit against a failure-mode catalog before release** (task-too-broad, contamination, LLM-authored-item privilege); record mitigations applied [2025-McGregor; 2024-Ungless].

14. **For multilingual items, transcreate rather than translate and have native speakers author hard cases** — validity is culture-specific; ~30% of naively-collected community data is culturally misaligned and monolingual models beat multilingual ones [2024-Wynter; 2026-Reaj; 2024-Velankar].
