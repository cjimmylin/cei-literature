# validity-psychometrics — sub-dossier part 6/6

Scope note: this part is dominated by (a) hate-speech / social-bias corpora whose validity case rests on inter-annotator reliability, and (b) moral-psychology and values papers that transplant validated human instruments (DIT, MFQ, Schwartz PVQ, WVS) into LLM evaluation. The first shows how reliability is established (or faked) at the label level; the second shows how construct validity, human baselines, and factor structure are borrowed from psychology — and where that borrowing breaks.

## A. Synthesized claims

1. **Inter-annotator agreement (IRR) is the single most reported validity statistic, and it varies enormously by construct granularity.** Reported agreement runs from near-perfect — HateCheck Fleiss' κ=0.93 [2021-Röttger-HateCheck], ADHAR Cohen's κ=0.9489 [2024-Aly-Hate speech detection with ADHAR], religious-bias completion κ=0.9644 [2025-Ajwad Abrar-Religious Bias Landscape] — through "moderate" (ViHSD κ=0.52 [2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social], KoSBI α=0.459/0.256 [2023-Lee-KoSBi], MFRC low raw κ PABAK-adjusted [2022-Trager-The Moral Foundations Reddit Corpus]) — to alarming (DKHate Jaccard 39–43% [2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate]; MuLTa Polish α=0.41 [2025-Leonardelli-MuLTa-Telegram]).

2. **Agreement is a function of how narrowly the construct is cut; coarser binary distinctions are far more reliable than fine-grained ones.** BEEP! reports gender-binary bias α=0.767 vs ternary bias α=0.492 and hate α=0.496 on the same items [2020-Moon-BEEP!]; OPSD rose from Phase-I κ=0.711 to Phase-II κ=0.8934 only after tightening guidelines [2024-Hossein-ParsOffensive]; Song shows both GPT models get sub-label full-match rates <0.20 while binary detection exceeds 0.60 on identical KoSBI data [2025-Song-Evaluation of Social Bias Classification]. This is a direct measurement-precision-vs-construct-richness tradeoff.

3. **Raising agreement often means narrowing the construct until the label tracks a surface feature, silently degrading validity.** DKHate reached consistency only by mandating "any profanity ⇒ offensive; never infer context," after which errors confirmed the classifier had become a profanity detector spuriously flagging "she" and "svensken" [2020-Sigurbergsson]. MFRC warns that "maximizing annotator agreement risks artificially inflating agreement at the cost of suppressing the natural variability of moral sentiment" [2022-Trager].

4. **Human moral judgment is not a single ground truth — offensiveness and moral response are demonstrably shaped by geo-culture and individual moral foundations.** In a 4,309-participant, 21-country study, 25/28 regional pairs differed significantly, yet 39.5% of variance was individual vs only 2.9% country and 0.7% region; Care and Purity foundations significantly mediated cross-cultural differences (Care ACME=−0.034, p<.001) [2023-Davani-Disentangling Perceptions of Offensiveness]. This undermines any benchmark that assumes one gold "offensiveness" label.

5. **Transplanting validated psychometric instruments gives LLM benchmarks free human norms, staging, and comparative literature.** The DIT (P-score) places GPT-4 at ~55.68 — graduate-student range — vs GPT-3 at ~29.84 ≈ random baseline 30.56, against known human norms (HS ~20–30, adults ~40–46, grad ~53–63) [2023-Deng-Probing the Moral Development]; the multilingual DIT extends this and finds Hindi/Swahili P-scores collapse to near random [2024-Khandelwal-Multilingual Defining Issues Test]. MFQ/WVS/dilemma composites and Schwartz PVQ are similarly repurposed [2025-Jiao-LLM Ethics Benchmark; 2026-Yun-VAPT].

6. **Positional/order effects threaten MCQ and ranking validity and are controlled by permutation averaging.** Both DIT adaptations run 48 permutations/dilemma at temperature 0 [2023-Deng; 2024-Khandelwal]; SpeciesismBench averages 3 samples/item (50× for human-instrument items) [2025-Jotautaitė-Speciesism in AI]; the pluralism study runs 30 iterations/model [2025-SOCIETY-How Much of a Pluralist is].

7. **High held-out accuracy is not construct validity: adversarial contrast sets collapse "saturated" moral classifiers to near-chance.** A RoBERTa Moral-Stories classifier at 99.55% accuracy fell to 51.58% under descriptive shifts and 26.09% under single-object edits ("nail"→"rusty nail" flips the label) [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]. Representative sampling shows the same illusion: hate-detection AP drops from 87.2% on functional tests and 40% on academic sets to 9.4% on a random Twitter-day sample [2024-Tonneau-HateDay].

8. **Confidence/uncertainty is a distinct fairness axis accuracy-only metrics miss.** UCerF scores correctness×confidence ("confidently-wrong < uncertain < confidently-right"); Mistral-7B ranks 5th on Equalized Odds but 8th on UCerF because it is confidently biased [2025-Wang-Is Your Model Fairly Certain]. HateCheck and Winogender both frame diagnostic power as high positive / low negative predictive value — presence, not absence, of bias [2021-Röttger; 2018-Zhao(Rudinger)].

9. **Criterion validity can be anchored to external ground truth.** Winogender correlates system bias with BLS statistics (r=0.87 to text stats) [2018-Zhao]; JudiFair validates sentencing biases against real judicial outcomes, finding accuracy and bias rise together [2025-Hu-LLMs on Trial]; HateDay shows academic-vs-real target-coverage alignment predicts detection performance at r=0.76, p=0.003 [2024-Tonneau].

10. **Factor structure and internal consistency increasingly serve as construct-validity evidence.** The pluralism instrument reports Cronbach α=0.96/0.89 and a two-factor solution separating rights- from preference-issues [2025-SOCIETY]; VAPT reports Spearman ρ≈.58 to Schwartz PVQ and per-value QWK (best Humility .48, worst Face .07) [2026-Yun-VAPT]; LLM Ethics Benchmark uses an inter-foundation correlation matrix (Care–Fairness 0.78) to argue the model mirrors MFT structure [2025-Jiao].

11. **Terminology and philosophical grounding are frequently unspecified — an upstream validity failure.** A survey of 92 moral-NLP papers found 66.3% define no key terms and many make normative claims from descriptive data (the is–ought problem) [2023-Vida-Values, Ethics, Morals]; a 791-measure scoping review found only 26.9% of RAI measures ship with interpretation criteria and zero traced a measure to downstream harm [2025-Rismani-Measuring What Matters].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Zhao (Rudinger Winogender) | 720 human-validated minimal pairs; bias correlated to BLS stats; explicit PPV-high/NPV-low framing |
| 2019-Jigsaw (ToxicBias) | κ=64.3; AUC subgroup metrics validate that counter-narrative augmentation fixes identity-term overfitting |
| 2020-Moon-BEEP! | Binary-gender α=0.767 vs ternary 0.492 exposes which distinctions are reliable |
| 2020-Sigurbergsson-DKHate | Jaccard 39–43%; construct narrowed to "profanity⇒offensive" to raise agreement; full data statement |
| 2021-Luu-ViHSD | κ=0.52 "moderate"; escalating 2→3→4 annotator consensus pipeline |
| 2021-Röttger-HateCheck | 29 functional tests, κ=0.93; diagnostic decomposition instead of aggregate F1 |
| 2022-Jafri-Multimodal | Pilot κ 0.50–0.63 → final 0.87–0.90 via 3-phase iterative annotation |
| 2022-Trager-MFRC | Raw Fleiss κ low, PABAK medium-high; warns agreement-maximization suppresses moral variance |
| 2023-Deng-DIT | GPT-4 P-score 55.68 (grad range) vs GPT-3 29.84≈random 30.56; 48 permutations/dilemma |
| 2023-Lee-KoSBi | α 0.459/0.256; cross-corpus classifiers ≈random on KoSBI → captures distinct construct |
| 2023-Rao-δ-ROT | Critic model (DeBERTa on 20k human labels) as scalable human-proxy; 85.9% human validity |
| 2024-Aly-ADHAR | κ=0.9489; dialect×category×class 3-way balance; cross-dialect transfer as hardness measure |
| 2024-Fitzgerald | 99.55%→51.58%→26.09% under contrast sets; saturation is an artifact |
| 2024-Hossein-OPSD | κ-gated phases (advance only when κ>0.75): 0.711→0.8934 |
| 2024-Khandelwal-mDIT | Hindi/Swahili P-scores fall to near-random; judgment vs reasoning dissociation |
| 2024-Tonneau-HateDay | Representative sampling: AP 9.4% vs 40%/87.2%; target-alignment predicts perf r=0.76 |
| 2024-Xie-CultureLLM | WVS as seed ground truth; human semantic-equivalence rating 4.60/5 validates augmentation |
| 2025-Ajwad-Religious Bias | Fleiss κ=0.9644; before/after-debiasing RBS table; cross-task convergent validity |
| 2025-Bauer-Dutch | Grammar-aware SGT list; CTF/DPD/EOD; counterfactual template eval separates identity from content |
| 2025-Durmus-GlobalOpinionQA | 1−JSD distributional similarity to PEW/WVS country distributions; WEIRD skew |
| 2025-Gao-MIST | Text-image-flow so no single modality is diagnostic; good/bad label asymmetry as diagnostic |
| 2025-Hu-JudiFair | Counterfactual-per-query design; Bernoulli test for multi-label FDR; accuracy↑⇒bias↑ |
| 2025-Jiao-LLM Ethics | MFA/RQI/ECM three-axis decomposition; scores vs human population distributions (MAE/RMSE) |
| 2025-Jotautaitė-Speciesism | Two scored axes (recognition 86% vs moral-wrong 34%); orthogonal capacity manipulation |
| 2025-Leonardelli-MuLTa | Polish α=0.41 flags cross-language annotation inconsistency; target-mention auxiliary task |
| 2025-Mekky-HALF | Harm-weighted (3:2:1) composite; performance–fairness dissociation as validity evidence |
| 2025-SOCIETY-Pluralism | Cronbach α 0.96/0.89; two-factor structure; ANOVA discriminates models |
| 2025-Song-KoSBI eval | Single-positive-class stress test; dual error-direction (safety vs undecided bias) |
| 2025-Wang-UCerF | Confidence×correctness fairness; difficulty redefined by human-judged ambiguity vs syntax |
| 2026-Davies-Persona Audit | Leakage-proof generative audit; normalized Cramér's V; debiasing prompt = no significant effect |
| 2022-Bulgarian | κ not reported (single annotator); balanced-accuracy vs macro-F1 divergence exposed |
| 2024-Indic-Bias | Metadata-only card; caste/religion/region axes absent from Western benchmarks |
| 2025-Muñoz-García | Leading vs non-leading prompt pairs isolate prompt-induced from intrinsic bias |
| 2016-Holyoak | "Methodological atheism": don't treat utilitarian answers as gold; coherence-shift signal |
| 2021-Wang-MedAI | Toxic-span F1 ~70% ceiling likely bounded by annotator disagreement on span boundaries |
| 2023-Davani | 39.5% individual vs 2.9% country variance; MFQ-2 as moderator of annotation |
| 2023-Vida | 66.3% of moral-NLP papers define no terms; is–ought grounding failure |
| 2024-Bignotti-Legal | Real court rulings as natural benchmark; contrastive embedding; FATTO/FATTO-CLEAN leakage check |
| 2024-Joy-Bangla | Counterfactual gender-swap pairs; bias varies 0.46%–7.48% by task |
| 2024-Li-Toxicity | Bilingual retrieval accuracy predicts cross-lingual safety transfer r=0.73 |
| 2024-Ranjan-Survey | Bias taxonomy as coverage checklist; intersectional metrics gap |
| 2024-Xu-Multilingual Value | Concept-vector recognition (τ=65%) as pre-behavioral probe; cross-lingual inconsistency metric |
| 2025-Davies-Recommendation | Counterfactual demographic prompt; fairness-to-utility ratio; extreme model divergence |
| 2025-Kajiwara-MetaHate | ELECTRA F1 0.898 near ceiling; label noise bounds validity; linguistic error taxonomy |
| 2025-Mahran-SAE | Intra-group coherence baseline before inter-group bias; VAI normalization; multi-model convergence |
| 2025-Rismani | 791 measures; 26.9% have criteria; 0 traced to downstream harm |
| 2025-Xiang-Moral Values | Word-association (contamination-resistant) indirect probing; emotionality/concreteness diagnostics |
| Anthropic-Opus 4.5 card | Single-turn evals "nearing saturation"; evaluation-awareness as validity threat; τ²-bench letter-vs-spirit |
| Anthropic-Reasoning CoT | CoT faithfulness 25–39%; verbosity ≠ faithfulness; reward hacks verbalized <2% |
| Google-Gemini 2.5 Pro | Held-out assurance prompts; CTFs saturated; over-refusal tracked separately from violations |
| NVIDIA-SteerLM | Attribute-prediction model denoises labels (+4.6%); GPT-4 judge favors length; κ=0.46 volunteers |
| OpenAI-InstructGPT | "Who are we aligning to?"; held-out labeler RM generalization (69.6%); RLHF doesn't fix bias |
| Anthropic-In-context RH (misfiled) | Perplexity as surrogate for capability collapse; avg metrics mask tail failures |

## C. Patterns & disagreements

**Convergence.** (i) Nearly every dataset paper treats IRR as the load-bearing validity claim, and the best-designed ones report agreement at *multiple granularities* to reveal which distinctions to trust [2020-Moon; 2024-Ranasinghe-SOLD sentence 0.7–0.8 vs token 0.6–0.7]. (ii) Iterative, guideline-gated annotation reliably lifts agreement — pilot→revise→re-annotate raised κ in [2022-Jafri], [2024-Hossein], and [2024-Tonneau] (which required α≥0.7 before main annotation). (iii) Multiple independent lines conclude that aggregate accuracy overstates validity, and adversarial/representative testing is the corrective [2024-Fitzgerald; 2024-Tonneau; 2025-Wang; Anthropic-Opus 4.5]. (iv) The psychometric-transplant papers converge on permutation averaging + published human norms + random-baseline anchoring as the recipe for defensible LLM scoring [2023-Deng; 2024-Khandelwal; 2025-Jiao; 2026-Yun].

**Disagreement / tension.** (a) *Maximize agreement vs preserve disagreement.* DKHate and OPSD deliberately engineer high κ; MFRC and Davani argue that high agreement destroys the very moral/cultural variance the benchmark should measure [2020-Sigurbergsson; 2024-Hossein vs 2022-Trager; 2023-Davani]. These are irreconcilable philosophies of ground truth. (b) *Is human judgment the target or a lower bound?* Winogender treats annotators as a lower bound carrying their own bias [2018-Zhao]; the DIT/Schwartz transplants treat human norms as the criterion [2023-Deng; 2026-Yun]; Holyoak warns against treating any normative standard (esp. utilitarian) as gold at all [2016-Holyoak]. (c) *Does model scale improve bias detection?* Song finds GPT-3.5 > GPT-4o on KoSBI bias classification [2025-Song] and Davies finds smaller ChatGLM3 diverges wildly from Llama2 [2025-Davies-Recommendation], while Ajwad finds newer/larger models near-zero bias [2025-Ajwad]; JudiFair finds accuracy and bias positively correlated [2025-Hu]. Scale is not a monotone validity lever. (d) *LLM-generated data.* KoSBI, SpeciesismBench, MIST, δ-ROT, SynthBias, and the Persona Audit all generate items with an LLM, then variously defend against generator idiosyncrasy by human review [2023-Lee; 2025-Jotautaitė; 2025-Gao; 2023-Rao; 2025-Wang; 2026-Davies] — but Davies' own consolidation step reuses GPT-5, and SpeciesismBench has no negative-control (non-speciesist) class, so false-positive rates are unmeasurable.

## D. Exemplars & anti-patterns

**Best-designed.** *HateCheck* [2021-Röttger] is the paradigm: 29 functional tests decompose "detect hate" into isolated linguistic phenomena (negation, reclaimed slurs, counter-speech), every case contrastively paired, template-balanced across 7 groups, gold labels validated to κ=0.93 rather than assumed, and diagnostic power honestly framed as NPV-limited. *Winogender/Rudinger* [2018-Zhao] pairs 10-way human validation (99.7% majority agreement) with external criterion anchoring to BLS statistics. *JudiFair* [2025-Hu] is the strongest quantitative-validity design: counterfactual-per-query (no in-context anchoring), document fixed-effects regression, Bernoulli tests for multi-comparison FDR, and criterion validation against real sentences. *UCerF/SynthBias* [2025-Wang] redefines difficulty by human-judged ambiguity so the benchmark resists saturation and adds a genuinely new fairness axis (confidence).

**Anti-patterns.** The *anti-Semitic hate* study runs a 3-annotator threshold protocol but reports **no** IRR and no class balance, so accuracy 0.94 is uninterpretable [2024-Liu-Detecting Anti-Semitic]; the *Bulgarian* corpus is single-annotator with no agreement metric on a 1.74%-positive set [2022-Bulgarian]. *Fitzgerald* shows the saturation illusion from the victim's side — 99.55% accuracy masking near-chance robustness [2024-Fitzgerald]. Two cards are *misfiled* (the "Bolatbek Kazakh" extract is a stemming study; the "Anthropic In-context Reward Hacking" extract is the model-editing "Butterfly Effect" paper), a provenance failure that threatens downstream synthesis [2024-Bolatbek; Anthropic-In-context]. SpeciesismBench's lack of a negative-control (non-speciesist) class is a subtler gap in an otherwise careful design [2025-Jotautaitė].

## E. Design lessons

1. **Report IRR at multiple construct granularities and pre-register the level you trust.** Publish binary AND fine-grained agreement so users know which labels are reliable [2020-Moon; 2024-Ranasinghe; 2025-Song]. Gate annotation phases on a κ threshold before scaling [2024-Hossein; 2024-Tonneau].

2. **Decide explicitly whether your ground truth maximizes or preserves disagreement, and disclose the consequence.** If you tighten guidelines to raise κ, document that the construct narrowed [2020-Sigurbergsson]; if the value is pluralistic, retain per-annotator labels [2022-Trager; 2023-Davani].

3. **Anchor to external criteria, not just internal labels.** Correlate model behavior with real-world statistics or outcomes (BLS, court sentences, survey distributions) for criterion validity [2018-Zhao; 2025-Hu; 2025-Durmus; 2024-Tonneau].

4. **Never trust held-out accuracy as validity — ship contrast sets and, where possible, a representative-sample slice.** Minimal-pair perturbations and random real-world sampling both expose the saturation illusion [2024-Fitzgerald; 2024-Tonneau; 2025-Wang]. Anthropic and Google confirm simple safety evals are already saturated on frontier models [Anthropic-Opus 4.5; Google-Gemini 2.5 Pro].

5. **Control positional/order effects and stochasticity with permutation averaging and repeated sampling.** Adopt the 48-permutation DIT protocol or ≥30-iteration sampling at fixed temperature [2023-Deng; 2024-Khandelwal; 2025-SOCIETY; 2025-Jotautaitė].

6. **Transplant validated psychometric instruments to inherit human norms, staging, factor structure — but stratify by language/culture and mark the random baseline.** DIT, MFQ, Schwartz PVQ, WVS all supply human anchors; multilingual replication reveals the low-resource collapse that English-only scores hide [2023-Deng; 2024-Khandelwal; 2025-Jiao; 2026-Yun; 2024-Xie].

7. **Separate the axes: recognition vs endorsement, content vs reasoning vs consistency, accuracy vs confidence, over-refusal vs violation.** Two-axis and three-axis decompositions surface failures single scores hide [2025-Jotautaitė; 2025-Jiao; 2025-Wang; Google-Gemini 2.5 Pro].

8. **Design against contamination and gaming by construction.** Prefer freshly-generated audit content [2026-Davies], indirect probes (word association) [2025-Xiang], multi-modal or multi-turn "flow" where no single fragment is diagnostic [2025-Gao], counterfactual-per-query instead of in-context comparison [2025-Hu], and embed canary strings [Anthropic-Opus 4.5].

9. **Weight items by harm severity and report weighted vs unweighted side by side** — the gap itself shows where a model's weaknesses cluster [2025-Mekky].

10. **When using an LLM as judge or generator, validate it: report judge self-preference and length bias, and add a negative-control class.** GPT-4 judges favor length and attribute-prediction models denoise labels (+4.6%) [NVIDIA-SteerLM]; test judge generalization across labeler groups [OpenAI-InstructGPT]; do not omit a non-target control class [2025-Jotautaitė].

11. **Localize the construct to the culture, not the translation.** Culture-specific axes (Korean military-service, marital status; Dutch "Moroccan"; Indian caste; grammar-aware SGT variants) are invisible to translated Western benchmarks [2020-Moon; 2023-Lee; 2025-Bauer; 2024-Indic-Bias].

12. **State philosophical grounding and interpretation criteria up front.** Declare descriptive vs normative stance to avoid the is–ought error, define every term, and attach an explicit hazard-threshold to each measure [2023-Vida; 2016-Holyoak; 2025-Rismani].

13. **Treat CoT/reasoning as an unreliable validity witness** — faithfulness is only 25–39% and drops on harder items; verbosity is not faithfulness [Anthropic-Reasoning CoT].

14. **Publish full provenance and annotator demographics (a Bender–Friedman data statement).** DKHate's disclosure that a single non-native annotator defined Danish "offensiveness" is exactly the metadata a values benchmark needs [2020-Sigurbergsson]; two misfiled cards in this batch show what happens when provenance is not checked [2024-Bolatbek; Anthropic-In-context].
