# design-space — sub-dossier part 4/4

Scope: 60 cards — multilingual hate/offense corpora, bias metrics, moral-dilemma generators,
cultural-persona frameworks, and normative-theory papers — read for the *menu of choices* in
format, scoring, and dataset construction.

## A. Synthesized claims

1. **MCQ/forced-choice systematically under-measures value conflict relative to open-ended
   interaction.** ConflictScope shows models rank protective values avg. 1.7 in MCQ but 4.5 in
   open-ended evaluation of the same scenarios, so MCQ is an unreliable predictor of real behavior
   [2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities]. BBQ-V finds blind
   text-only scores exceed vision scores for all four tested models (Phi-4-MM 89.44% blind vs
   74.30% vision) and that closed-form MCQ "can overestimate performance by masking reasoning
   failures" [2025-Narnaware-SB-Bench]. Rao likewise runs 6 option-order permutations to strip
   positional artifacts from a 3-option forced choice [2023-Rao-Ethical Reasoning over Moral
   Alignment].

2. **Threshold-free and confidence-aware scoring outperforms accuracy/F1 for fairness constructs.**
   Borkan's five AUC-based metrics (Subgroup, BPSN, BNSP AUC; positive/negative AEG) capture
   false-positive vs false-negative inflation per group without setting a threshold
   [2019-Borkan-Nuanced Metrics]. UCerF's confidently-wrong < uncertain < confidently-right scale
   exposes that Mistral-7B ranks 5th on Equalized Odds but 8th on UCerF [2025-Wang-Is Your Model
   Fairly Certain Uncertainty-Aware]. Laszkiewicz wraps each fairness *definition* in a divergence
   with a provable zero-point, reporting a hypothesis-test accept/reject not a rank
   [2024-Laszkiewicz-Benchmarking Fairness in Image Upsampling].

3. **Static item pools saturate or leak; generative/adaptive construction is the emerging answer.**
   GETA frames "evaluation chronoeffect," fuses CAT+IRT with LLM item generation, keeps only
   high-discrimination items, and reaches concurrent validity 0.8897 (vs 0.4309 without variational
   IRT) using ~150 adaptive items [2025-Jiang-Raising the Bar]. OffTheRails generates 400
   factorially-balanced items from causal graphs [2024-Franken-OffTheRails]; ConflictScope from
   value pairs [2025-Liu-ConflictScope]; PluriHarms curates 150 from 62,612 candidates via a genetic
   algorithm [2026-Li-PluriHarms].

4. **Cross-condition transfer is the sharpest discrimination knob for cultural/linguistic
   validity.** ADHAR's train-on-one-dialect / test-on-another drops accuracy from 0.84 to 0.64
   [2024-Aly-Hate speech detection with ADHAR]; KOLD's multilingual MUDES scores F1 12.8 on Korean
   spans vs 40.6 native [2022-Jeong-KOLD]; Rao's models hit 100% on Western dilemmas but GPT-4
   falls to 73.15% on the one Indian scenario [2023-Rao-Ethical Reasoning over Moral Alignment];
   SweEval's harmful-rate rises to 0.92 for transliterated Indic vs much lower English
   [2025-Kumar-SweEval]. CroissantLLM isolates knowledge from fluency by asking France-culture
   questions *in English* [2024-Faysse-CroissantLLM].

5. **Balanced construction beats large-but-skewed collection.** ADHAR enforces ~100 hate + ~100
   non-hate per dialect×category cell [2024-Aly-Hate speech detection with ADHAR]; HateBR removes
   surplus non-offensive comments to hold 50/50 [2022-Vargas-HateBR]; UnfairFace holds FairFace's
   source constant and skews only group balance (>80% White) to attribute unfairness to data vs
   architecture [2024-Laszkiewicz]. Conversely keyword/seed-list collection oversamples explicit
   slurs and distorts distributions [2022-Jeong-KOLD; 2024-Aly; 2023-Haq-NLPashto].

6. **Implicit/ambiguous items discriminate; explicit ones saturate.** Bai's IAT-style probes reveal
   pervasive stereotype bias in models that pass BBQ/BOLD/DecodingTrust (bias t(33,599)=76.39,
   p<0.001) [2025-Bai-Explicitly unbiased]. Khamassi shows LLMs pass 3 explicit-dignity prompts but
   fail when the value is implicit [2024-Khamassi]. BBQ-V and PluriHarms sample the ambiguous middle
   where "cannot be determined" or a borderline rating is aligned [2025-Narnaware-SB-Bench;
   2026-Li-PluriHarms]; Wang defines difficulty by human-judged ambiguity so items stay hard
   [2025-Wang-Is Your Model Fairly Certain].

7. **Adversarial/pressure conditions expose fragility invisible under benign prompting.** Ebara's
   trees show GPT-4 ethics scores 91-98 collapse (CM 79.86) when told to prioritize the doctor
   [2025-Ebara]; SweEval's correct answer is refusing a benign-framed swear-insert instruction
   [2025-Kumar-SweEval]; persona-prompting swings Mistral-7B Dutch CrowS bias 22.21%→94.46%
   [2025-Satheesh-Dutch CrowS-Pairs]; Schramowski's adjective injection corrupts moral scores
   [2020-Schramowski].

8. **Multiturn/tree-structured formats capture coherence single-turn MCQ cannot.** Ebara scores
   full trajectories through branching decision trees (avg 8.1 nodes) [2025-Ebara]; Tennant's
   iterated social-dilemma games score G_collective/G_Gini/G_min over T rounds [2025-Tennant].

9. **LLM-as-judge is scalable but must be validated against humans.** BBQ-V reports judge-human
   κ=0.81 and cross-checks a second open judge [2025-Narnaware-SB-Bench]; ConflictScope validates
   GPT-4.1 vs crowdworkers at κ=0.62 [2025-Liu]; AISafetyLab flags its 7 scorers "lead to
   inconsistencies and potentially unfair comparisons" [2025-Zhang-AISafetyLab].

10. **Annotator design is load-bearing.** Per-worker caps (KOLD 1%), entrance tests, and gold
    questions raise quality [2022-Jeong-KOLD; 2025-Wang]; expert + diverse pools raise agreement
    (HateBR κ=0.75, ADHAR κ=0.95) [2022-Vargas-HateBR; 2024-Aly]; author-only pools risk shared
    bias [2024-Toygar-Turkish Offensive Language; 2019-Jigsaw]. PluriHarms uses 100 profiled
    annotators × 150 prompts = 15,000 ratings, treating disagreement as structured signal
    [2026-Li-PluriHarms].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Ljubesic-Datasets of Slovene and Croatian | Thread-level (not comment-level) train/test split prevents conversational leakage; encrypted release enables research on toxic text without propagating it. |
| 2019-Borkan-Nuanced Metrics | Five threshold-agnostic AUC metrics decompose per-group false-positive (BPSN) vs false-negative (BNSP) inflation; robust to class imbalance. |
| 2019-Jigsaw-Unintended Bias | Free-text "bias implication" annotation + counter-narrative augmentation fixes identity-term lexical overfitting. |
| 2020-Schramowski-Moral Choice Machine | Averaging 10 QA templates cuts phrasing artifacts; positive-adjective injection is an adversarial robustness probe. |
| 2021-Mohit Chandra-Antisemitism | 4-subtype hate taxonomy whose predictable confusion structure (Political×Racial) validates construct validity. |
| 2021-Ravikiran-DOSA | Span-level (character-offset exact-match) annotation gives moderator-actionable attribution vs document labels. |
| 2022-Jeong-KOLD | Culture-tailored 21-group taxonomy from a 1,000-item pilot; title-context input adds +13.1 F1 to group ID. |
| 2022-Vargas-HateBR | Three-layer hierarchy (binary → ordinal severity → 9 hate groups) + enforced 50/50 balance + PhD-diverse annotators. |
| 2023-Catapang-EMoTES-3K | Mixed-intent scenarios (good act/bad intent) stress-test intent-vs-surface reasoning; bilingual parallel corpus. |
| 2023-Haq-NLPashto | Iterative bootstrap annotation (seed model pre-labels, human corrects, retrain) cheapens low-resource dataset build. |
| 2023-Lee-VisAlign | Three-tier ground truth (Must-Act/Must-Abstain/Uncertain) with soft human distribution + Hellinger distance scoring. |
| 2023-Rao-Ethical Reasoning | Test policy-following not value-endorsement; complement policy pairs (π, ¬π) double data and measure value entrenchment. |
| 2024-Aly-ADHAR | Dialect×category×class cell-balance (~100 each) + cross-dialect transfer as a hardness measure. |
| 2024-Franken-OffTheRails | Causal-graph scaffolding: LLM fills typed slots, conditions stitched into factorially-balanced controlled items. |
| 2024-Guldimann-COMPL-AI | Top-down normative→technical mapping from EU AI Act; flags un-benchmarkable requirements rather than dropping them. |
| 2024-Laszkiewicz-Fairness Upsampling | Definition→metric with provable zero-point; report a hypothesis test (fair? accept/reject), not a rank. |
| 2024-Sharma-TABHATE | Target-level classes (individual/community/none); reports pre- and post-SMOTE to show imbalance penalty. |
| 2024-Toygar-Turkish Offensive | Parallel with/without-context design shows contextual prior turn adds only +3.29 F1; "ambiguous" option removed. |
| 2024-with.pdf-Bodo/Assamese NEIHS | Annotation guidelines grounded in platform community standards; cross-script transfer heuristic for model choice. |
| 2025-An-MoralReason | OOD alignment score (softmax over disjoint held-out); disagreement scenarios force prior-shift not recall. |
| 2025-Bai-Explicitly unbiased | Behavior-only, embedding-free IAT + relative (two-candidate) decisions expose bias absolute framing hides. |
| 2025-Ebara-Medical Ethics | Tree-structured multiturn scenarios scored over full trajectory; misaligned-instruction prompting as validity check. |
| 2025-Galea-Measurement to Mitigation | Multi-metric triangulation (CrowS+SEAT+templates+t-SNE) with explicit documentation of when metrics disagree. |
| 2025-Jiang-Raising the Bar (GETA) | Adaptive item generation at target difficulty defeats saturation/leakage; report concurrent validity vs 3 references. |
| 2025-Kumar-SweEval | Instruction-to-violate framing; compound harmful = task-completed AND term-present prevents crediting empty refusals. |
| 2025-Liu-ConflictScope | Expressed (MCQ) vs revealed (open-ended) preference divergence; Bradley-Terry ranking + 6-dimension filter. |
| 2025-Narnaware-SB-Bench (BBQ-V) | Ambiguity-as-probe ("cannot be determined"); blind-vs-vision ablation as validity check; multi-dim ordinal judge rubric. |
| 2025-Satheesh-Dutch CrowS-Pairs | Persona manipulation (good/bad) yields huge bias dynamic range; adaptation quality taxonomy for translated benchmarks. |
| 2025-Shen-ValueCompass | Same Schwartz-value instrument to humans and LLMs; scenario×country factorial; 8-prompt robustness averaging. |
| 2025-Wang-Is Your Model Fairly Certain | Correctness×confidence joint scoring + minimal-pair disparity; difficulty by human-ambiguity to resist saturation. |
| 2025-Zaim Bin Ahmad-Moral Machine | Conjoint/AMCE reduces values to low-dim preference vector; distance-to-human as scalar; version-snapshot sweep. |
| 2026-Li-PluriHarms | Two-axis (harm × agreement) design treating disagreement as measured signal; personalized k-shot beats value-profile. |
| 2024-Faysse-CroissantLLM | Cultural-knowledge probe phrased in a neutral language; seeded canaries for contamination auditing. |
| 2025-Firmino-Cross-Lingual | Transfer degradation (source→target language drop) as a quantitative cultural-specificity metric. |
| 2025-Unknown-Multi-Agent Evaluators | Multi-agent redundant/adversarial LLM judges reduce single-judge bias; continuous vs static evaluation. |
| 2016-Holyoak-Deontological coherence | Methodological atheism: don't treat utilitarian answers as ground truth; measure soft-constraint weighting + coherence shift. |
| 2018-Crone-SMID | Rate every item on all 8 dimensions (not one category); political-balance rater requirement; uniqueness scores. |
| 2020-Akrout-Virtuous Machine | Agent/process-level (reasoning-chain) evaluation vs output-level; audit-first design. |
| 2021-Prabhumoye-Case Study | Universalizability + informed-consent audits; contrastive pairs where model should flag vs proceed. |
| 2023-Astobiza-MoralNet | Recurring adversarial competition governance; multi-framework scoring of a single item. |
| 2023-Ji-AI Alignment | RICE axes as benchmark taxonomy; dynamic DAG generation to prevent contamination; moral-consistency (same case, diff parties). |
| 2023-Mougan-Kantian Deontology | Disparate-treatment (behavior) = deontological metric, computable without post-deployment outcome data. |
| 2024-Hendrycks-Intro to AI Safety | Moral-parliament vector scoring across lenses; revealed/stated/idealised preference taxonomy; fairness-impossibility reporting. |
| 2024-Khamassi-Strong/weak alignment | Implicit-vs-explicit value scenarios; non-repeatability of responses as a reliability dimension to report. |
| 2024-Sun-Towards Friendly AI | Four challenge axes (no unified definition, subjectivity, cross-cultural variation, no metrics) as a coverage checklist. |
| 2024-Vasilev-CRAFT | 17-category cultural taxonomy + entity-level granularity; LLM auto-captions fail on culturally specific content. |
| 2025-Chared-French hate speech | Mixed real+AI-generated data for balance; BART zero-shot adds target labels for bias analysis. |
| 2025-Fillies-German TikTok | Classifier-ensemble-guided sampling raises hate prevalence ~1%→14%; three-axis type/origin/target taxonomy + intensity. |
| 2025-Kasirzadeh-Characterizing AI Agents | 8-category risk taxonomy as scaffolding; only 4.2% of safety papers address "undesirable behavior". |
| 2025-Mahajan-Mapping Moral Reasoning | 11-dim hybrid (semantic+lexicon) alignment vector + dictionary-ablation to validate the instrument. |
| 2025-Pipitone-Practical wisdom | Second-order metric: did interacting with the model improve the *human's* ethical decisions? Dual behavioral+self-report. |
| 2025-Tennant-Hybrid Approaches | Moral frameworks formalized as reward functions; multi-objective (collective/Gini/min) scoring resists reward-hacking. |
| 2025-Zhang-AISafetyLab | Attack×defense matrix; over-refusal as mandatory co-metric; unified score(query,response)→judgment interface. |
| 2026-Tagarelli-Culturally Grounded Personas | 10 WVS variables → 93,312-config cartesian sweep; EMD distributional alignment vs human survey references. |
| DeepSeek-DeepSeek-R1 | Rule-based rewards resist reward-hacking, model-assigned rewards get gamed; LLM-judge safety hits >95% human consistency. |
| 2019-Aliman-Requisite Variety | A benchmark must have at least as many moral dimensions as failure types it detects; ethical adversarial examples. |
| 2024-Chhabra-SPECTRA | Hold scenario/goal constant, vary the ethical paradigm; framework-level harness hosting multiple paradigms. |
| 2025-Ravindran-Moral Anchor | Value state as multidim vector (utility/empathy/rule); predictive vs reactive drift monitoring. |
| 2025-Sun-Axiology MCDA | Intrinsic vs instrumental value taxonomy; MCDA for auditable trade-off scoring vs opaque composites. |
| 2026-Hendricks-Extremist Attitudes | Second-order harm metric: does model moral framing increase sacralization/extremism in downstream human raters? |

## C. Patterns & disagreements

**Convergence.** (a) Many teams reject single-scalar accuracy for vectors/hypothesis tests: Borkan
(suite), Laszkiewicz (accept/reject), Wang (confidence-weighted), Sun (MCDA), Hendrycks
(moral-parliament vector), Tennant (multi-objective) [2019-Borkan; 2024-Laszkiewicz; 2025-Wang;
2025-Sun-Axiology; 2024-Hendrycks; 2025-Tennant].
(b) Everyone building non-English resources reports that off-the-shelf multilingual transfer fails
and culture-tailored taxonomies are required [2022-Jeong-KOLD; 2024-Aly; 2023-Catapang; 2024-with.pdf;
2024-Vasilev-CRAFT]. (c) Generative/adaptive construction is repeatedly proposed as the fix for
saturation and contamination [2025-Jiang; 2024-Franken; 2025-Liu; 2026-Li; 2023-Ji-AI Alignment].
(d) Format matters as much as content: MCQ inflates and hides bias in three separate studies
[2025-Liu; 2025-Narnaware; 2024-Faysse (letter vs continuation)].

**Disagreements.** (1) *Prescriptive vs anti-prescriptive scoring.* Rao scores policy-*following*
and Holyoak preaches "methodological atheism," refusing a "correct" moral answer [2023-Rao;
2016-Holyoak]; in tension, MoralReason, EMoTES-3K, and the medical/hate corpora assume author- or
framework-defined gold labels [2025-An-MoralReason; 2023-Catapang; 2025-Ebara; 2022-Vargas].
(2) *Synthetic data: enabler or contaminant.* OffTheRails, ConflictScope, PluriHarms, GETA, and
Wang embrace LLM generation [2024-Franken; 2025-Liu; 2026-Li; 2025-Jiang; 2025-Wang]; Vasilev shows
LLM auto-captions err on cultural content, and Chared/PluriHarms concede generator bias/circularity
[2024-Vasilev; 2025-Chared; 2026-Li]. (3) *Reward source.* DeepSeek-R1 argues rule-based rewards
resist hacking while model-assigned rewards get exploited — a caution against the LLM-judge scoring
that Narnaware/Liu/multi-agent rely on [DeepSeek; 2025-Narnaware; 2025-Liu; 2025-Unknown]. (4) Most
hate corpora treat harmlessness as target, but Hendricks shows rights/fairness framings *fuel*
extremism, contradicting "positive values = safe outputs" [2026-Hendricks].

## D. Exemplars & anti-patterns

**Best-designed.** *PluriHarms* is strongest: two-axis harm×agreement design, anchor-based
continuous rating, GA curation to a target distribution, deep annotator profiling regressing
disagreement onto interpretable features, prompt-only release [2026-Li-PluriHarms]. *GETA* best
answers saturation/contamination: IRT-2PL discrimination filtering, self-refreshing items, validity
via three concurrent-validity references [2025-Jiang]. *VisAlign* imports real psychometrics
(Cronbach's α, Hellinger distance, three-tier abstain ground truth) [2023-Lee-VisAlign]. *ADHAR*
is the model multilingual corpus: dialect×category×class cell-balance + cross-dialect transfer,
κ=0.95 [2024-Aly]. *ConflictScope* pairs MCQ with open-ended on the same items to expose the
expressed/revealed gap [2025-Liu].

**Anti-patterns.** *Rao's* 72-item, 4-dilemma set with author-defined ground truth and 5
homogeneous annotators has minimal power and a culturally-situated gold standard labeled universal
[2023-Rao]. *Khamassi's* 7 prompts × 3 models, no quantitative scoring or IRR, is exploratory-only
[2024-Khamassi]. *Mahajan's* 90 responses with ω=0.4 tuned on the same data it evaluates carries
circularity risk [2025-Mahajan]. *NLPashto's* "100% theoretical accuracy" POS claim rests on
verifying a single lexicon tag (anchoring bias), no κ [2023-Haq]. *Ravindran's* Moral Anchor
validates only on Q-table noise in a 5×5 maze, FPR 0.55-0.59 [2025-Ravindran]. *MoralNet* and
*Sun-Axiology* propose "Morality Scores"/MCDA with no operational definition [2023-Astobiza;
2025-Sun-Axiology]. Recurring cheap failure across the hate-speech cluster: author-only annotators
and seed-keyword collection biasing toward explicit slurs [2024-Toygar; 2024-Aly; 2022-Jeong].

## E. Design lessons

1. **Pair MCQ with open-ended/interactive on the same items** and report the divergence as a
   validity check; never ship MCQ-only value rankings [2025-Liu; 2025-Narnaware].
2. **Score confidence and abstention, not just correctness.** Use confidently-wrong < uncertain <
   confidently-right, make "cannot be determined" a gold answer, and collect soft human distributions
   for ambiguous items scored by Hellinger/EMD [2025-Wang; 2025-Narnaware; 2023-Lee; 2026-Tagarelli].
3. **Prefer threshold-free metrics with a provable zero-point and a hypothesis test** over
   leaderboard scalars; pair an aggregate with a worst-group score [2019-Borkan; 2024-Laszkiewicz].
4. **Build in a cross-condition transfer test** (dialect→dialect, language→language, culture→culture,
   blind vs context) as your primary hardness/validity knob [2024-Aly; 2022-Jeong; 2025-Narnaware;
   2025-Firmino; 2024-Faysse].
5. **Enforce cell-balance at construction** (condition×class) and, where natural data is skewed, build
   a deliberately-skewed twin to attribute bias to data vs method [2024-Aly; 2022-Vargas; 2024-Laszkiewicz].
6. **Sample the ambiguous middle and treat annotator disagreement as signal**; define difficulty by
   human-judged ambiguity so items resist saturation [2026-Li; 2025-Wang; 2025-An].
7. **Add adversarial/pressure conditions** (misaligned instruction, instruction-to-violate,
   good/bad persona, adjective injection) — benign prompting alone under-detects fragility
   [2025-Ebara; 2025-Kumar; 2025-Satheesh; 2020-Schramowski].
8. **Use generative/adaptive construction with guardrails**: causal-graph or value-pair scaffolds,
   multi-dimension LLM-judge filters, IRT difficulty targeting, GA distribution-matching, and seeded
   canaries for contamination — but human-validate labels because LLM generators err on cultural
   content and can create circularity [2024-Franken; 2025-Liu; 2025-Jiang; 2026-Li; 2024-Faysse;
   2024-Vasilev].
9. **Validate any LLM-judge against humans (report κ) and cross-check with a second judge**; be aware
   model-assigned rewards are more gameable than rule-based ones [2025-Narnaware; 2025-Liu; DeepSeek;
   2025-Zhang; 2025-Unknown].
10. **Engineer the annotator pool**: per-worker caps, qualification/entrance tests, gold questions,
    demographic/expert diversity, documented demographics, staged adjudication, and mental-health
    safeguards [2022-Jeong; 2025-Wang; 2022-Vargas; 2024-Aly; 2025-Fillies; 2018-Crone].
11. **Derive constructs top-down from a named normative source** (legal act, Schwartz, MFT, WVS,
    biomedical principles) for traceability, and flag un-benchmarkable requirements rather than
    dropping them [2024-Guldimann; 2025-Shen; 2026-Tagarelli; 2025-Ebara].
12. **Score multidimensionally/pluralistically**: moral-parliament vectors, RICE axes,
    intrinsic-vs-instrumental split, multi-objective outcomes, and multi-framework scoring of one
    item resist reward-hacking and honor disagreement [2024-Hendrycks; 2023-Ji; 2025-Sun-Axiology;
    2025-Tennant; 2023-Astobiza; 2024-Chhabra].
13. **Prevent leakage/document provenance**: split at the natural unit (thread not comment), seed
    canaries, dynamically generate items, and report contamination controls [2018-Ljubesic;
    2024-Faysse; 2023-Ji].
14. **Consider process- and second-order metrics**: score reasoning chains for virtue/coherence,
    test implicit (unnamed) value detection, measure consistency across identity swaps, and whether
    the model improves the *human's* decisions or amplifies extremism [2020-Akrout; 2024-Khamassi;
    2023-Ji; 2025-Pipitone; 2026-Hendricks].
15. **Report over-refusal alongside safety, and non-repeatability as a reliability dimension** —
    optimizing one in isolation misleads [2025-Zhang; 2024-Khamassi].
