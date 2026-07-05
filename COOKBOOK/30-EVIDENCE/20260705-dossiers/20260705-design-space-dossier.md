# design-space — theme dossier (CEI COOKBOOK evidence layer, 2026-07-05)

Scope: the full menu of task formats, scoring approaches, and dataset-construction choices for
values benchmarks — with pros/cons and when each is appropriate. Merged and deduplicated from four
sub-dossiers spanning ~230 cards: moral-psychology stimulus sets, hate-speech/bias corpora,
cultural-value benchmarks, fairness meta-benchmarks, deliberation/agentic harnesses, machine-ethics
theory, and frontier-lab specs.

## 1. Synthesized findings

1. **Task format is a first-order experimental variable that materially changes measured "alignment,"
   not a presentation detail.** MCQ/forced-choice systematically under-measures value conflict:
   ConflictScope models rank protective values avg. 1.7 in MCQ vs 4.5 open-ended on the *same*
   scenarios [2025-Liu-ConflictScope]; BBQ-V finds blind text-only scores exceed vision scores for
   all four models (Phi-4-MM 89.44% blind vs 74.30% vision) and closed-form MCQ "can overestimate
   performance by masking reasoning failures" [2025-Narnaware-SB-Bench]; MIST shows VLMs answer ~40%
   of items with no image and Llama-3.2-90B-V collapses 96.6%→13.6% text-only→multimodal
   [2025-Gao-MIST]. Deliberation format is itself the variable: GPT-4.1 change-of-verdict was 0.6%
   synchronous vs high conformity round-robin; inertia odds ratios GPT 8.27 / Claude 4.49 / Gemini
   2.83 [2025-Sachdeva-Deliberative Dynamics]. KorNAT and Su warn MCQ "reveals understanding of
   values rather than actual orientation" [2024-Lee-KorNAT; 2025-Su]. 96% of 69 surveyed studies use
   static datasets, only 3% interactive [2025-Snoswell]. Treat format as a factor and vary it.

2. **Minimal-pair / counterfactual substitution is the dominant, most-reusable item-construction
   primitive for isolating one value/identity variable.** Swap one token, hold the rest fixed, attribute
   any output delta causally: Winogender pronoun swaps at 94.9% human agreement [2018-Rudinger];
   De-Arteaga gender-indicator flip (4.6–12.2%) [2019-De-Arteaga]; identity-slotting templates (77k,
   Dixon; 720 = 60 occ × 2 templates × 2 participants × 3 pronouns, Zhao) [2018-Dixon; 2018-Zhao];
   the 8,640-sentence Equity Evaluation Corpus where bias hit 75–86% of 219 systems but mean deltas
   were <0.03 (3% of range, max 0.34) — visible only under paired t-tests [2018-Kiritchenko]; SHADES
   grammatical-agreement slot tags (`<GENDER:MASC>`) for valid multilingual generation [2025-Al-SHADES];
   EuroGEST log-likelihood on 71k gendered pairs over 30 languages [2025-Team-EuroGEST]; leading vs
   non-leading prompt pairs [2025-Muñoz-García]; GG-BBQ group-term vs proper-name subsets
   [2025-Satheesh-GG-BBQ]. Payoff: causal attribution and a clean null point; cost: ecological
   artificiality.

3. **Scoring against a distribution, not a single modal/gold answer, is the emerging best practice
   for pluralistic value items** — and the sharpest published idea in the corpus. Field baseline is bad:
   97.1% of 105 cultural-alignment datasets score a single majority answer, only 2.9% diversity-aware
   [2025-team]. Exemplars: KorNAT scores by survey probability mass on the chosen option (SVA),
   empirical ceiling 0.450 not 1.0, plus an All-Neutral baseline [2024-Lee-KorNAT]; GlobalOpinionQA
   uses 1−Jensen-Shannon distance to country-level human distributions over 2,556 MCQs
   [2025-Durmus-GlobalOpinionQA]; Scruples targets the full 5-label distribution (626,714 judgments
   over 32,766 anecdotes) with cross-entropy, a BEST oracle ceiling, and a Dirichlet-multinomial layer
   separating model uncertainty from controversiality [2021-Lourie-Scruples]; DEF induces diversity
   (89.8% vs 0% single-shot) so one model simulates a population, scored by KL-divergence
   [2025-Liu-Realistic]; CLCA reuses WVS/KL-D with 1,000 personas per culture [2025-Liu-Cultural];
   Tagarelli sweeps 93,312 persona configs scored by EMD to survey references [2026-Tagarelli]; Morlat
   clusters ternary Blame/Neutral/Support distributions by KL threshold [2025-Morlat]. Preserve
   contested/ambiguous items rather than discarding them (entropy flags, explicit "ambiguous" band
   50%±10%) [2025-Machlovi; 2023-Nie].

4. **LLM-generation of items scales coverage and defeats saturation/contamination, but inherits the
   generator's culture and needs a human-validated filter.** ToxiGen generated 274,186 statements
   (98.2% implicit) via adversarial ALICE decoding, gated by 90.5% human-indistinguishability
   [2022-Hartvigsen]; Rao distilled 1.2M defeasible-morality entries filtered by a critic trained on
   20K human labels [2023-Rao]; GETA fuses CAT+IRT with LLM item generation, keeps only
   high-discrimination items, and reaches concurrent validity 0.8897 vs 0.4309 with ~150 adaptive items
   [2025-Jiang]; OffTheRails builds 400 factorially-balanced items from causal graphs [2024-Franken];
   PluriHarms curates 150 from 62,612 candidates by genetic algorithm [2026-Li-PluriHarms]; Davies
   generates fresh personas each run for leakage-proof-by-construction evaluation [2026-Davies].
   Counter-evidence: Vasilev shows LLM auto-captions err on culturally specific content
   [2024-Vasilev-CRAFT]; Chared and PluriHarms concede generator bias/circularity [2025-Chared;
   2026-Li]. Multiple teams warn the generator's Western-centric bias propagates.

5. **Grade the reasoning, not only the verdict** — a right answer with a wrong rationale is a failure
   benchmarks must catch. Matched correct-vs-plausible-but-wrong reasoning chains [2025-Galatolo;
   Task-1 static accuracy <35% for all models]; LLM-judge rationale classification into
   consequentialist/deontological labels, with reasoning-order manipulation exposing post-hoc
   rationalization [2025-Samway]; an `ideal_response_profile` of required principles [2025-Herrador];
   justifications/steerability/moral-sensitivity as first-class behaviors the field omits — only 19%
   evaluate steerability, 4% "value of information" [2025-Snoswell]; scoring reasoning + stakeholder
   coverage per item [2025-Kasu; 2023-Maile; 2023-Bang]; agent/process-level reasoning-chain evaluation
   over output-level [2020-Akrout]; internal coherence (contradictory rulings on similar cases)
   [2025-Muntean].

6. **External-reference anchoring is the strongest single validity move**, inheriting a pre-validated
   construct and enabling correlation metrics. Bias to BLS employment stats (r=0.87 to text stats, 0.55
   to BLS) [2018-Zhao]; Schwartz values validated across ~80 countries [2023-Yao]; WVS as ground truth
   (fine-tune for $6) [2024-Xie]; Moral Machine intervention rates as per-nationality baselines
   [2025-Hatemo; 2025-Zaim Bin Ahmad]; court rulings as items [2024-Bignotti]; NYT-Ethicist answers as
   gold [2023-Bang]; developmental instruments Kohlberg/Rest [2025-Kumar]; UDHR + national human-rights
   commissions for demographic axes [2023-Lee; 2022-Jiang]; MedES derives 1,278 atomic rules from
   authoritative docs, used to both generate items AND score compliance [2026-Jin-MedES]; COMPL-AI maps
   EU AI Act top-down and flags un-benchmarkable requirements rather than dropping them
   [2024-Guldimann].

7. **Report an empirical ceiling and a naive baseline, or scores are uninterpretable.** KorNAT's 0.45
   SVA ceiling makes a 0.33 legible [2024-Lee-KorNAT]; HOMO-LAT reports MPA 0.939 vs best system 0.53
   [2025-Enguix]; Scruples' BEST oracle sets the achievable cross-entropy floor [2021-Lourie]. Yet
   Rismani finds only 26.9% of 791 RAI measures ship any interpretation criterion — 73% lack one
   [2025-Rismani]. A high raw score without a ceiling audit is a saturation/leakage red flag: Khanduja's
   98.2% Telugu accuracy [2024-Khanduja], Kajiwara-Multimodal's 97–99% undefined "ratios"
   [2024-Kajiwara-Multimodal], and Ibrohim's binary 98.7% (dropping to 66% multi-label) [2023-Ibrohim]
   all illustrate the trap. Add a dictionary/lexicon upper-bound to detect keyword-dependence
   [2024-Kajiwara-Catalogue].

8. **Inter-annotator agreement is the load-bearing, frequently-weak foundation; low agreement forces
   construct-narrowing.** DKHate reports Jaccard 39–43% then narrows "offensive" to "contains profanity"
   to raise it — trading validity for reliability, but documenting the trade [2020-Sigurbergsson];
   HOMO-LAT κ 0.124–0.158 with Mexican annotators defaulted for 15 of 19 countries [2025-Enguix];
   AustroTox α=0.49 [2024-Goldzycher]; OffendES κ=0.36 [2021-Plaza-del-Arco]; CharMoral κ=0.55
   [2025-Bae]; Fortuna's binary tier at Fleiss κ 0.17 vs expert hierarchical 0.72 [2019-Fortuna].
   Iterative rounds and expertise lift it: ETHOS κ≥0.814 via active-learning sampling [2020-Mollas];
   pilot→full→conflict pipelines raise κ ~0.50→0.87–0.90 [2022-Jafri; 2024-Jafri]; paired-annotator
   peer discussion 68.75%→93% [2022-Nkemelu]; Turkish superset α=0.84, ADHAR κ=0.95 via expert+diverse
   pools [2024-Tonneau-Turkish; 2024-Aly]. Experts find ~2× the harm laypeople do [2024-Ptaszynski;
   2025-Hong]. Distributional/soft labels preserve the signal that hard majority labels discard
   [2021-Lourie; 2021-Plaza-del-Arco].

9. **Balanced construction — cell-balance at construction so a competent-but-unbiased system lands on
   the null point — beats large-but-skewed collection.** Zhao is gender-balanced by design so a
   100%-accurate system trivially scores zero bias [2018-Zhao]; CrowS ideal score = 50% [2020-Nangia];
   ADHAR enforces ~100 hate + ~100 non-hate per dialect×category cell [2024-Aly]; HateBR removes
   surplus to hold 50/50 [2022-Vargas]; UnfairFace holds the source constant and skews only group
   balance (>80% White) to attribute unfairness to data vs architecture [2024-Laszkiewicz];
   Velankar's balanced 6,250-per-class design is a deliberate exception in hate-speech [2024-Velankar].
   Minority: on imbalanced classification tasks most treat imbalance as the thing to preserve/measure
   and use macro-F1, not balancing [2019-Basile; 2022-Trager].

10. **Cross-condition transfer is the sharpest discrimination/validity knob for cultural-linguistic
    generalization.** ADHAR train-on-one-dialect/test-on-another drops 0.84→0.64 [2024-Aly]; KOLD's
    multilingual MUDES scores Korean-span F1 12.8 vs 40.6 native [2022-Jeong-KOLD]; Rao's models hit
    100% on Western dilemmas but GPT-4 falls to 73.15% on one Indian scenario [2023-Rao]; SweEval
    harmful-rate rises to 0.92 for transliterated Indic vs much lower English [2025-Kumar-SweEval];
    out-of-domain Polish F1 collapses 0.846→0.50 [2025-Leonardelli]; out-of-domain F1 is the real
    validity signal (WildGuard 0.889 in-distribution → 0.278 on GuardEval) [2025-Machlovi]. Corollary:
    monolingual/language-specific resources beat multilingual transfer on culturally-specific tasks
    (Greek 0.89 vs mBERT 0.73) [2020-Pitenis; 2022-Jahan; 2025-Al-SHADES], so build native seed lists,
    character n-grams, syntax-preserving transliteration — not translated English artifacts. Minority
    caution: Corazza finds cross-platform pooling helps everywhere except Twitter, where in-domain wins
    [2019-Corazza].

11. **Implicit/ambiguous items discriminate; explicit ones saturate — and adversarial/pressure
    conditions expose fragility invisible under benign prompting.** Bai's IAT-style probes reveal
    pervasive bias in models that pass BBQ/BOLD/DecodingTrust (t(33,599)=76.39, p<0.001) [2025-Bai];
    Khamassi shows LLMs pass explicit-dignity prompts but fail implicit [2024-Khamassi]; BBQ-V and
    PluriHarms sample the ambiguous middle where "cannot be determined" is aligned [2025-Narnaware;
    2026-Li]. Pressure: Ebara's GPT-4 ethics scores 91–98 collapse (CM 79.86) when told to prioritize
    the doctor [2025-Ebara]; SweEval's correct answer is refusing a benign-framed swear-insert
    [2025-Kumar]; persona-prompting swings Mistral-7B Dutch CrowS bias 22.21%→94.46% [2025-Satheesh];
    adjective injection corrupts moral scores [2020-Schramowski]; the moral-sycophancy two-turn pushback
    protocol uses right→wrong vs wrong→right transition asymmetry as the diagnostic [2026-MoralSycophancy].

12. **Threshold-free, confidence-aware, and multidimensional scoring outperforms single-scalar
    accuracy/F1 for fairness and pluralism constructs.** Borkan's five AUC metrics decompose per-group
    false-positive (BPSN) vs false-negative (BNSP) inflation without a threshold [2019-Borkan]; UCerF's
    confidently-wrong<uncertain<confidently-right exposes Mistral-7B ranking 5th on Equalized Odds but
    8th on UCerF [2025-Wang]; Laszkiewicz wraps each fairness definition in a divergence with a provable
    zero-point and reports accept/reject not a rank [2024-Laszkiewicz]; VisAlign imports Cronbach's α +
    Hellinger distance + a three-tier Must-Act/Must-Abstain/Uncertain ground truth [2023-Lee-VisAlign].
    Single-scalar targets invite Goodharting [2016-Amodei]; inverse-average weighting stops easy domains
    dominating [Zhipu AI-AgentBench]; multi-objective (collective/Gini/min) scoring resists reward-hacking
    [2025-Tennant]; DeepSeek-R1 argues rule-based rewards resist hacking while model-assigned rewards get
    gamed [DeepSeek-R1].

13. **Two-stage psychometric validation is the stimulus-construction gold standard, almost never done
    for LLM benchmarks.** MFV pruned items >20% cross-classification, then ran EFA/CFA (RMSEA .047) and
    MFQ criterion regression (β .24–.47) [2015-Clifford]; the Dutch adaptation replicated 97% correct
    classification [2023-Hopp]; SMID rates every item on all 8 dimensions with a political-balance rater
    requirement [2018-Crone]. Test-retest reliability is a mandatory but rare validity check
    [2024-Boerstler; 2024-Keswani], and non-repeatability of responses should itself be reported as a
    reliability dimension [2024-Khamassi].

14. **LLM-as-judge is now standard but must be human-validated and family-separated.** MedES keeps
    evaluator+annotator in the Qwen family while base model is DeepSeek to reduce self-preference, with
    guardian test F1 >0.96 [2026-Jin]; BBQ-V reports judge-human κ=0.81 and cross-checks a second open
    judge [2025-Narnaware]; ConflictScope validates GPT-4.1 vs crowdworkers at κ=0.62 [2025-Liu]; Samway's
    Gemini judge is human-validated (P=0.845, F1=0.820) [2025-Samway]; Biedma reports QWK 0.8 human-GPT-4
    [2024-Biedma]; BEATS uses a 3-LLM-judge consortium with per-judge ANOVA to quantify disagreement as a
    result, and flags its own factuality-judge unreliability [2025-Anonymous-BEATS]; AISafetyLab warns its
    7 scorers "lead to inconsistencies" [2025-Zhang-AISafetyLab]. Counter-position: Urchs deliberately
    excludes LLMs to avoid circular bias [2025-Urchs]; the split turns on whether the judged construct
    overlaps the judge's own biases.

15. **Frontier lab practice lags the academic design frontier.** Qwen3 has no safety/values eval section
    and no model spec; "alignment tasks" mean instruction-following [Alibaba (Qwen)-Qwen3]. Gemini 2.5 Pro
    is richer — CCL + early-warning alert thresholds, held-out assurance evals, decoupled over-refusal
    (+14.8% IF vs −0.9% violations) — but all safety evals are text-only [Google DeepMind-Gemini_2.5_Pro].
    Where labs lead is governance coupling: Capability-Threshold→Required-Safeguards pairing with
    elicitation-first testing on safeguards-removed models [Anthropic-Model_Spec; Anthropic-Responsible_Scaling_Policy_1.0].

## 2. Design-space structure (decision table)

**Axis A — Task format (choose to the construct; know its blind spot):**

| Format | Buys | Costs / blind spot | Use when | Stems |
|---|---|---|---|---|
| MCQ / forced-choice | cheap exact-match, high reliability | measures understanding not disposition; overestimates; gameable | large-scale screening WITH ambiguity trap | 2018-Rudinger; 2024-Sorin; 2025-Su; 2025-Liu-ConflictScope |
| Minimal-pair / factorial template | causal attribution, clean null point | ecological artificiality | isolating one identity/value variable | 2018-Kiritchenko; 2018-Dixon; 2025-Al-SHADES; 2025-Fasching |
| Generative / free-text | ecological disposition + reasoning | needs a validated downstream scorer | disposition/reasoning is the target | 2025-Su; 2023-Bang; 2024-Biedma; 2026-He |
| Distribution-elicitation | pluralism honored | needs survey ground truth + persona induction | contested values with real pluralism | 2024-Lee-KorNAT; 2025-Durmus; 2025-Liu-Realistic |
| Multi-step / tree / multiturn | path-dependence, coherence | scoring full trajectories | consistency under escalation | 2025-Wu-Staircase; 2025-Ebara; 2025-Bae |
| Agentic / game-theoretic | real incentive conflict | complex harness | when trade-off/oversight is the point | 2025-Backmann; 2025-Saunders; Zhipu AI-AgentBench |
| Multimodal / embodied | expanded harm surface | signal distribution + degraded scoring | vision/time-pressure matters | 2025-Gao-MIST; 2022-Jafri; 2018-Behzadan |

**Axis B — Scoring approach:** exact-match/macro-F1 (imbalanced → never bare accuracy, adjust with PABAK)
[2019-Basile; 2022-Trager]; distributional cross-entropy / JSD / KL / EMD / Hellinger with an oracle ceiling
[2021-Lourie; 2025-Durmus; 2023-Lee-VisAlign]; threshold-free AUC suites and confidence-weighted scales
[2019-Borkan; 2025-Wang]; hypothesis-test accept/reject with a provable zero-point [2024-Laszkiewicz];
multidimensional/vector/multi-objective to resist Goodharting [2024-Hendrycks; 2025-Tennant; 2016-Amodei];
"acceptable range"/moral-threshold floor and per-framing leaderboards for pluralism [2025-Snoswell;
2025-Yaacov; 2024-Defrance]; reasoning/rationale scoring on top of the verdict [2025-Galatolo; 2025-Samway].
Always attach an empirical ceiling, a naive baseline, and an interpretation threshold [2024-Lee-KorNAT;
2025-Rismani].

**Axis C — Dataset construction:** minimal-pair/factorial templates [2018-Kiritchenko; 2025-Fasching];
external-reference anchoring [2018-Zhao; 2023-Yao; 2026-Jin]; incident/inductive taxonomies via grounded
theory + saturation [2026-He; 2024-Biedma; 2025-Wu]; adversarial/dynamic DADC rounds [2024-Goldzycher];
generative/adaptive (CAT+IRT, causal graphs, GA curation, fresh-per-run) [2025-Jiang; 2024-Franken;
2026-Li; 2026-Davies]; iterative agreement-tracked annotation with engineered pools (caps, entrance tests,
gold questions, expert/diverse, documented provenance) [2022-Jafri; 2022-Jeong; 2024-Tonneau-Languages];
balanced or deliberately-skewed-twin cells [2024-Aly; 2024-Laszkiewicz]; leakage prevention (thread-level
split, seeded canaries, dynamic DAG) [2018-Ljubesic; 2024-Faysse; 2023-Ji].

## 3. Patterns & disagreements

**Convergences.** (a) *Format is a confound* — MCQ inflates/hides bias in at least four independent studies
[2024-Lee-KorNAT; 2025-Wang-Desired; 2025-Liu-ConflictScope; 2025-Narnaware]; the near-universal fix is a
built-in abstention/ambiguity trap ("no answer" correct) [2025-Satheesh; 2025-Narnaware; 2023-Lee-VisAlign].
(b) *Resist contamination by construction* via fresh generation, shipped templates, adaptive IRT, or thread-
level splits [2022-Hartvigsen; 2026-Davies; 2025-Jiang; 2018-Ljubesic]. (c) *Realism beats trolley-style
artifice* — fact-grounded dilemmas rated far more realistic (dz=1.31) [2023-Körner], with items sourced from
AITA/JAMA/court cases [2023-Feng; 2025-Hong; 2024-Bignotti]. (d) *Reasoning quality is the frontier*, not
verdicts [2025-Galatolo; 2025-Samway; 2025-Snoswell; 2023-Maity]. (e) *Non-English transfer fails*;
culture-tailored taxonomies and native resources are required [2022-Jeong-KOLD; 2024-Aly; 2024-Vasilev].

**Disagreements (preserved minority positions).**
(1) *Majority-label vs distribution as ground truth.* Most binarize to a gold label [2018-Rudinger;
2024-Sorin]; KorNAT/Liu/Lourie reject this as misrepresenting pluralism [2024-Lee-KorNAT; 2025-Liu-Realistic;
2021-Lourie], and Wang argues *against averaging* sub-benchmarks with different normative commitments
[2025-Wang-Desired].
(2) *Ground truth vs acceptable range.* MedES and PacifAIst use exact-match against one "correct" choice
[2026-Jin; 2025-Herrador]; Snoswell and Yaacov argue accuracy-against-ground-truth is wrong for moral items
and propose an acceptable range / moral-threshold floor [2025-Snoswell; 2025-Yaacov].
(3) *Who labels values, is "intuition" valid.* ETHOS/Awad treat crowd preference as truth [2020-Mollas;
2020-Awad]; Ptaszynski/Hong mandate experts [2024-Ptaszynski; 2025-Hong]; Kim attacks the whole enterprise —
intuitions are inconsistent and should be *replaced* by formal universalizability tests, not used as labels
[2018-Kim]; Holyoak preaches "methodological atheism," refusing to treat utilitarian answers as ground truth
[2016-Holyoak].
(4) *Aggregation of pluralism.* Boddington endorses equal-credence MEC aggregation (justified by ~32/31/37%
philosopher endorsement) [2023-Boddington]; Baum and Yaacov argue every aggregation rule relocates the
normative choice and faces Arrow-type impossibility [2025-Baum; 2025-Yaacov]; Defrance says report per-framing
leaderboards, not one number [2024-Defrance].
(5) *Synthetic data: enabler or contaminant.* OffTheRails/ConflictScope/PluriHarms/GETA/Wang embrace LLM
generation [2024-Franken; 2025-Liu; 2026-Li; 2025-Jiang; 2025-Wang]; Vasilev shows LLM captions err on
cultural content and Chared/PluriHarms concede circularity [2024-Vasilev; 2025-Chared].
(6) *Reward source / LLM-in-the-loop: essential or circular.* BEATS/MIST/NaVAB embed judges [2025-Anonymous-BEATS;
2025-Gao; 2025-Ju]; DeepSeek-R1 warns model-assigned rewards get gamed vs rule-based [DeepSeek-R1]; Urchs
excludes LLMs entirely [2025-Urchs].
(7) *Factuality vs neutrality collide.* FABLE proves a formal trade-off (when Sfact=1, SE=0) — rewarding
group-uniform answers can reward fact-distortion, a tension most bias benchmarks ignore [2024-Team-FABLE].
(8) *Positive values = safe outputs?* Most hate corpora treat harmlessness as target, but Hendricks shows
rights/fairness framings can *fuel* extremism [2026-Hendricks].
(9) *Cross-domain pooling.* Usually helps; Corazza finds it hurts on Twitter (in-domain wins) [2019-Corazza].

## 4. Exemplars & anti-patterns

**Best-designed.** *MFV* [2015-Clifford] — the psychometric exemplar: length/reading-controlled items,
cross-loading pruning, EFA/CFA, criterion validity, ideological-balanced recruitment; cross-culturally
replicated [2023-Hopp]. *KorNAT* [2024-Lee-KorNAT] — pluralistic scoring: survey distribution as truth,
demographic re-weighting, reported ceiling, refusal as first-class, human-preference validation (94/100).
*FABLE* [2024-Team-FABLE] — separates objective from subjective over the same statistic, proves the
factuality–diversity bound, computes entropy before averaging, human-validates its grader. *Wang-Desired*
[2025-Wang-Desired] — descriptive/normative/correlation taxonomy + paired ≠/= items yielding precision AND
recall, and an adversarial check that debiasing prompts backfire. *MLCommons AI Safety Benchmark*
[2024-Group] — explicit scope (adult × general assistant × English × Western), persona-conditioned generation,
speech-act template taxonomy, validated grader (κ=0.79), conservative min-across-tests aggregation. *GETA*
[2025-Jiang], *ABCFair* + *FFB* [2024-Defrance; 2023-Han], *Scruples* [2021-Lourie], *MedES* [2026-Jin],
*PluriHarms* [2026-Li], *VisAlign* [2023-Lee-VisAlign], *ADHAR* (κ=0.95, cross-dialect transfer) [2024-Aly],
*ConflictScope* (MCQ+open-ended on same items) [2025-Liu] round out the exemplar set.

**Anti-patterns.** *Khanduja-Telugu* 98.2% accuracy with no ceiling analysis — saturation/leakage red flag
[2024-Khanduja]. *Kajiwara-Multimodal* 97–99% undefined "ratios," no SOTA comparison [2024-Kajiwara-Multimodal].
*Kasu-EthicsMH* — 125 LLM-generated scenarios, no baseline evals, scoring_type "n/a": a schema, not a benchmark
[2025-Kasu]. *SamPar* reports only accuracy on imbalanced hate data [2024-Velankar]. *OffendES/CharMoral* force
hard majority labels onto contested items (κ 0.36/0.55), discarding Scruples-style signal [2021-Plaza-del-Arco;
2025-Bae]. *Rao* — 72 items, 4 dilemmas, 5 homogeneous annotators, culturally-situated gold labeled universal
[2023-Rao]. *Khamassi* — 7 prompts × 3 models, no IRR [2024-Khamassi]. *Mahajan* — 90 responses, ω=0.4 tuned on
the same data it evaluates (circularity) [2025-Mahajan]. *DKHate* is a *productive* anti-pattern: low agreement
forced narrowing "offensive" → "contains profanity," but the trade is documented honestly [2020-Sigurbergsson].
Recurring cheap failure across the hate cluster: author-only annotators + seed-keyword collection biasing toward
explicit slurs [2024-Toygar; 2024-Aly; 2022-Jeong].

## 5. Open questions the corpus does NOT answer

1. **How to aggregate genuine moral pluralism into a score without an impossibility result** — Baum/Yaacov prove
   every rule relocates the normative choice; no card offers a validated resolution, only "report per-framing"
   [2025-Baum; 2025-Yaacov; 2024-Defrance].
2. **When distribution-matching is the right target vs when it merely launders a majority view** — no card
   compares SVA/JSD scoring against a normative floor on the same items.
3. **How to certify LLM-generated items are free of the generator's cultural bias** — the field embraces
   generation while conceding circularity, with no accepted audit [2024-Vasilev; 2026-Li].
4. **Whether reasoning-quality scores predict downstream behavior** — process metrics exist [2025-Galatolo;
   2020-Akrout] but none is validated against real deployment outcomes.
5. **The judgment–behavior gap** — Xu measured covert cheating vs stated judgment [2016-Xu], but no benchmark
   systematically links stated values to behavioral action at scale.
6. **Second-order human-impact metrics** — whether the model improves the *human's* decisions or amplifies
   extremism is proposed but essentially unmeasured [2025-Pipitone; 2026-Hendricks].
7. **Multimodal/agentic scoring at scale** — signal-distribution designs exist [2025-Gao; 2025-Ebara] but lack
   validated graders for long trajectories.
8. **How much annotator/geo provenance actually moves benchmark conclusions** — Tonneau shows 0% report both
   data+annotator origin (r=0.99 with Twitter geography) [2024-Tonneau-Languages], but the downstream effect on
   rankings is unquantified.

## 6. TOP IMPLICATIONS FOR NEW BENCHMARK DESIGN

1. **Treat task format as an experimental factor and vary it.** Ship MCQ *and* open-ended on the same items and
   report the divergence as a validity check — never MCQ-only value rankings; expect MCQ to overestimate and hide
   reasoning failures [F1; 2025-Liu-ConflictScope; 2025-Narnaware; 2025-Sachdeva].
2. **Score contested items by distribution-match against a re-weighted survey, with an oracle ceiling, a naive
   baseline, and an explicit interpretation threshold.** The single strongest published idea; do not average a
   pluralistic construct to one gold label [F3, F7; 2024-Lee-KorNAT; 2021-Lourie; 2025-Durmus; 2025-Rismani].
3. **Build minimal-pair/factorial items with grammatical-agreement handling and a counter-stereotype "gotcha"
   subset**, and report paired/distributional deltas — mean effects can be <0.03 while prevalence is 75%+
   [F2; 2018-Kiritchenko; 2025-Al-SHADES; 2018-Rudinger].
4. **Bake an abstention/ambiguity trap into every MCQ** so "cannot be determined" is sometimes the aligned answer,
   defeating always-guess and always-equalize shortcuts, and sample the ambiguous middle so items resist saturation
   [F1, F11; 2025-Satheesh; 2025-Narnaware; 2026-Li].
5. **Anchor the construct to a pre-validated external reference** (WVS/Schwartz, labor stats, Moral Machine, court
   rulings, biomedical principles, legal acts) to inherit validity and enable correlation metrics; flag
   un-benchmarkable requirements rather than dropping them [F6; 2023-Yao; 2026-Jin; 2024-Guldimann].
6. **Grade the reasoning, not only the verdict** — matched correct-vs-plausible-wrong chains, rationale
   classification, ideal-response profiles, and steerability/moral-sensitivity tasks the field currently omits
   [F5; 2025-Galatolo; 2025-Samway; 2025-Snoswell].
7. **Prefer threshold-free, confidence-aware, multidimensional scoring over single-scalar accuracy**; pair an
   aggregate with a worst-group score, adjust for base rate (macro-F1/PABAK), and separate descriptive accuracy
   from normative neutrality — they formally trade off [F12; 2019-Borkan; 2025-Wang; 2024-Team-FABLE; 2016-Amodei].
8. **Use generative/adaptive construction with guardrails to defeat saturation/leakage** — causal-graph or
   value-pair scaffolds, IRT difficulty targeting, GA distribution-matching, fresh-per-run items, seeded canaries,
   thread-level splits — but human-validate labels because generators err on cultural content and risk circularity
   [F4; 2025-Jiang; 2024-Franken; 2026-Davies; 2018-Ljubesic; 2024-Vasilev].
9. **Engineer and document the annotator pipeline**: iterative rounds with tracked κ/α per category and language,
   per-worker caps, entrance/gold questions, expert or lived-experience raters for subtle harms, prefer
   distributional/soft labels, and disclose data+annotator provenance *before* any construct-narrowing
   [F8; 2022-Jafri; 2024-Ptaszynski; 2021-Lourie; 2020-Sigurbergsson; 2024-Tonneau-Languages].
10. **Add adversarial/pressure conditions and cross-condition transfer tests as the primary hardness knobs**, and
    report over-refusal, consistency-across-runs/steps, and non-repeatability as first-class metrics; tie thresholds
    to governance triggers on safeguards-removed models [F10, F11; 2025-Ebara; 2024-Aly; 2024-Huang;
    Anthropic-Responsible_Scaling_Policy_1.0].
