# best-practices — sub-dossier part 4/4

Scope note: this part draws on 51 cards spanning bias/toxicity/hate-speech benchmarks, moral-reasoning benchmarks, metaevaluation studies, AI-lab alignment reports, and normative-framework surveys. The design lessons below are traceable only to those cards.

## A. Synthesized claims

1. **Decompose a construct into functional tests instead of reporting one aggregate score.** HateCheck replaces held-out F1 with 29 functional tests (3,728 cases) each isolating one phenomenon (negation, reclaimed slurs, counter-speech), which exposed shared model weaknesses invisible to aggregate metrics — e.g., BERT-Davidson scored 12.8% on negated hate and Perspective 3.8%, while total accuracy looked respectable at 63–77% [2021-Röttger-HateCheck]. MORALISE builds the same difficulty gradient into one benchmark: binary moral judgment saturates near ceiling (proprietary avg 88.28% accuracy) while fine-grained norm attribution stays at 66.60% / 42.63%, preserving headroom [2025-Lin-MORALISE].

2. **Use contrastive minimal pairs so a passing model must encode the real signal, not surface keywords.** XSTest pairs 250 safe prompts with 200 minimal-edit unsafe twins ("kill a Python process" vs "kill a person") to jointly diagnose over- and under-refusal, revealing Llama-2 fully+partially refuses 59.6% of safe prompts while Mistral-Instruct complies with most *unsafe* ones [2024-Röttger-XSTest]. HateCheck's contrastive non-hate cases and BharatBBQ's NP/NNP disambiguated pairs serve the same anti-shortcut function [2021-Röttger-HateCheck; 2025-Tomar-BharatBBQ].

3. **Add a control/competence condition so "wrong-because-misaligned" is separable from "wrong-because-incapable."** MBBQ builds a parallel control set (neutral names) and only interprets bias where task competence is established, restricting bias analysis to templates a model answers above chance; Falcon (16.2% control accuracy, below chance) is excluded rather than falsely credited as unbiased [2024-Neplenbroek-MBBQ]. Zhou shows the failure mode directly: Qwen's "low" Thai bias score reflects lack of Thai comprehension, not fairness [2025-Zhou-Bias Beyond English].

4. **Report discriminant validity against capabilities and compute — high correlation is a red flag for safetywashing.** Ren computes each safety benchmark's Spearman correlation with a capabilities PC1 (78.3% base / 70.8% chat variance) and with training FLOPs: ETHICS (82.2%), MT-Bench (78.7%), TruthfulQA-MC1 (81.2%), BBQ-disambiguated (76.8%) track capability, whereas MACHIAVELLI (−49.9%), Sycophancy (−66.8%), and BBQ-ambiguous (−37.3%) do not — the knowledge-vs-propensity distinction [2024-Ren-Safetywashing]. The recommendation is to make capabilities-correlation a mandatory reported statistic.

5. **Pre-audit a benchmark against known failure modes before release.** BenchRisk catalogs 57 failure modes and 196 mitigations across 5 reliability dimensions (comprehensiveness, intelligibility, consistency, correctness, longevity); all 26 scored benchmarks — including ETHICS (mean 37, longevity 0) and BBQ (mean 49, longevity 0) — present significant risk in ≥1 dimension, and 16/26 left "task too broadly defined" unmitigated [2025-McGregor-BenchRisk]. FFB provides the complementary empirical audit: run a baseline across many seeds and check whether the intended construct is even *stably present* — several canonical fairness datasets did not reliably exhibit bias [2023-Han-FFB].

6. **Bind bias/misalignment metrics to accuracy and report a metric triad, not a single number.** KoBBQ's diff-bias is analytically bounded by accuracy so both must be read together; a perfect model is provably unbiased [2024-Jin-KoBBQ; 2024-Neplenbroek-MBBQ]. FairLex reports average group mF1, group disparity (std dev), and worst-group mF1 together so no single number can hide a failure, surfacing a 21.5-point ECtHR defendant-state gap [2022-Chalkidis-FairLex]. BharatBBQ adds a Stereotypical Bias Score conditioned on question polarity to separate genuine stereotype endorsement from lexical preference [2025-Tomar-BharatBBQ].

7. **Pair a worst-case metric with a frequency metric.** RealToxicityPrompts reports Expected Maximum Toxicity (worst of 25) alongside Toxicity Probability (P of any toxic generation), separating rare-but-catastrophic from frequent-mild failure; FrenchToxicityPrompts reuses the same pairing and finds toxic continuations rare but severe when they occur [2020-Gehman-RealToxicityPrompts; 2024-Brun-FrenchToxicityPrompts].

8. **Validate that a cheap recognition proxy predicts real behavior before trusting it.** SafetyBench transforms MCQs into matched constrained and open-ended queries and shows MCQ accuracy correlates with safe-generation rate at Pearson r=0.99 (constrained) / 0.91 (open-ended), and that open-ended prompts *hide* risks that MCQs surface [2024-Zhang-SafetyBench]. The inverse caution: Anthropic's assistant found models score best on the honesty HHH category yet "certainly do fabricate information when probed interactively" — recognition can diverge from deployed behavior [Anthropic-A_General_Language_Assistant].

9. **Measure over-refusal as well as under-refusal.** XSTest operationalizes exaggerated safety as a decision boundary [2024-Röttger-XSTest]; Llama 2 tracks a ~0.05% false-refusal rate and a curated 210-sample borderline set as a precision-recall calibration instrument [Meta AI-Llama_2].

10. **Culturally-grounded construction beats machine translation, and it must be survey- or expert-validated.** KoBBQ validates every stereotype and target with a 100-person balanced survey (dropping items where >50% say "no stereotype exists" or human reading-comprehension accuracy <50%) and shows via Wilcoxon tests that machine-translated bias measurement is insufficient [2024-Jin-KoBBQ]. BharatBBQ (Cohen's κ=0.83, back-translation cosine gate 0.75), MBBQ (retain only cross-culturally shared stereotypes), and KoSBI (human-rights-law-grounded demographic axes) reinforce this [2025-Tomar-BharatBBQ; 2024-Neplenbroek-MBBQ; 2023-Lee-KoSBI]; Zhou's translated CrowS-Pairs candidly admits importing US-centric norms [2025-Zhou-Bias Beyond English].

11. **Objective gold standards from codified professional protocols eliminate crowd-annotation noise.** TRIAGE uses real START/jumpSTART medical-triage materials with medical gold answers, sidestepping low inter-rater agreement, and validates itself by detecting significant model differences with no ceiling (best model ~0.68) [2024-Kirch-TRIAGE]. PrinciplismQA (12 medical-expert annotators, Beauchamp-Childress framework) and TRIAGE both show expert-authored ground truth is worth its cost for high-stakes domains [2025-Hong-PrinciplismQA].

12. **Report inter-annotator reliability, and handle subjective normative labels honestly.** Cards that report κ span moderate to near-perfect: HateCheck Fleiss κ=0.93 [2021-Röttger-HateCheck], XSTest κ 0.89–0.97 [2024-Röttger-XSTest], X-MuTeST Fleiss 81–85 [2026-Rehman-X-MuTeST], BanHate κ=0.78 [2025-Hossain-BanHate], KoSBI Krippendorff α=0.46/0.26 (low on context-dependent labels) [2023-Lee-KoSBI]. Soemer argues raw kappa is inappropriate when consensus discussion is used and instead forces annotators to cite the specific IHRA clause and record personal disagreement, cleanly separating "the standard says X" from "I believe X" [2023-Soemer-Antisemitic].

13. **Derive evaluation targets top-down from a named normative framework, keeping every metric traceable to a clause.** COMPL-AI maps 6 EU AI Act principles → technical requirements → 23 benchmarks and flags un-benchmarkable requirements rather than dropping them silently [2024-Guldimann-COMPL-AI]; PrinciplismQA organizes by four bioethics principles [2025-Hong-PrinciplismQA]; Woodgate's 21-principle taxonomy and the ethical-vs-AI-principles distinction supply the vocabulary [2024-Woodgate-Macro Ethics].

14. **Treat contamination, reward hacking, and saturation as live threats.** Sarvam scores near-zero on BBQ (likely contamination) but is biased on BharatBBQ [2025-Tomar-BharatBBQ]; FrenchToxicityPrompts uses SBERT similarity-to-gold as a contamination diagnostic and freezes classifier scores against API drift [2024-Brun-FrenchToxicityPrompts]. Constitutional AI documents Goodharting ("you are valid, valued, and cared for" boilerplate) and PM miscalibration at high scores [Anthropic-Constitutional_AI]; METR caught o3 tampering with a scoring function in 5/24 experiments [OpenAI-o3-and-o4-mini-system-card]. BenchRisk's "longevity" dimension shows academic data-release norms drive saturation; only private-evaluator benchmarks (AILuminate 74) resist it [2025-McGregor-BenchRisk].

15. **Validate LLM/classifier judges against humans and probe prompt sensitivity; single scores are unreliable.** DPO shows GPT-4 agrees with humans about as often as humans agree with each other, but win-rates shift with the judge prompt [OpenAI-dpo]. Luong found Llama Guard flagged only 49/210 responses that Perspective scored >0.9 — evaluators disagree badly at the extreme [2024-Luong-Realistic Evaluation]; Weber's LLM-assisted reannotation improved scores 10–17% but biased results toward GPT-based models [2025-Weber-Digital Guardians]; XSTest cross-checks manual vs string-match vs GPT-4 judge on the same items [2024-Röttger-XSTest].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2021-Röttger-HateCheck | 29 functional tests > aggregate F1; contrastive non-hate cases; Fleiss κ=0.93 |
| 2024-Röttger-XSTest | Contrast pairs jointly measure over- AND under-refusal; κ 0.89–0.97 |
| 2024-Neplenbroek-MBBQ | Parallel control set separates misalignment from incompetence |
| 2024-Ren-Safetywashing | Report Spearman correlation vs capabilities PC1 + compute; <40% = separable |
| 2025-McGregor-BenchRisk | Pre-audit against 57 failure modes × 5 reliability dimensions |
| 2023-Han-FFB | Check the construct is *stably present* across seeds before trusting a dataset |
| 2024-Jin-KoBBQ | Survey-grounded ground truth (100/item) + accuracy-bounded diff-bias |
| 2022-Chalkidis-FairLex | Report avg mF1, group disparity, worst-group together; realistic imbalanced splits |
| 2025-Tomar-BharatBBQ | SBS metric separates stereotype endorsement from lexical preference |
| 2020-Gehman-RealToxicityPrompts | Expected Max Toxicity (worst-case) + Toxicity Probability (frequency) pairing |
| 2024-Zhang-SafetyBench | MCQ recognition predicts safe-generation at r=0.99/0.91 (validated bridge) |
| 2024-Kirch-TRIAGE | Objective professional protocol gold labels + overcaring/undercaring error taxonomy |
| 2023-Lee-KoSBI | Human-rights-law-grounded axes + ambiguity-based item selection |
| 2023-Soemer-Antisemitic | Mandatory clause-citation + recorded personal disagreement for contested norms |
| 2024-Guldimann-COMPL-AI | Top-down normative→technical mapping; flag un-benchmarkable requirements |
| 2025-Hong-PrinciplismQA | Framework-organized MCQ+open-ended; 12 expert annotators |
| 2024-Woodgate-Macro Ethics | Ethical-principles vs AI-principles distinction; multi-principle pluralism |
| 2024-Brun-FrenchToxicityPrompts | SBERT-to-gold contamination check; freeze classifier scores vs API drift |
| 2024-Luong-Realistic Evaluation | Two-evaluator cross-check exposes judge disagreement at extremes |
| 2025-Weber-Digital Guardians | LLM-assisted reannotation biases toward the judging model |
| OpenAI-dpo | Human-LLM calibration study + dual judge-prompt robustness check |
| Anthropic-Constitutional_AI | Goodharting + PM miscalibration at high scores; principle-ensemble labeling |
| Anthropic-A_General_Language_Assistant | Recognition can diverge from deployed behavior; eval-capability entanglement |
| Meta AI-Llama_2 | Separate helpfulness/safety RMs; borderline set; multi-turn harder than single |
| OpenAI-o3-and-o4-mini-system-card | Scoring-function tamper-resistance; browsing contamination; saturation of easy evals |
| 2024-Huang-Collective Constitutional AI | Group-Aware Consensus prevents majority capture in pluralistic aggregation |
| 2025-Lin-MORALISE | Two-tier task design (easy judgment → hard attribution) avoids ceiling |
| 2025-An-MoralReason | Disagreement-scenario selection; capped keyword reward prevents gaming |
| 2025-Chakraborty-Structured Moral Reasoning | Prompt structure explains 92% of accuracy variance (R²=0.923) |
| 2025-Kasu-EthicsMH | Multi-field schema scores reasoning + stakeholder coverage, not just the choice |
| 2026-Rehman-X-MuTeST | Human token-level rationales; plausibility vs faithfulness split |
| 2025-Hossain-BanHate | Recency/event-anchored sampling; per-category AND per-target κ reporting |
| 2025-Liu-The Scales of Justitia | Graded success metrics (StrongReject) beat binary "attack success" |
| 2020-Nozza-AMI | Dual-track: real-data performance lane + synthetic bias-audit lane |
| 2022-Romim-BD-SHS | Hierarchical harm annotation (identify→target→type); domain-matched > bigger corpus |
| 2025-Bhattacharjee-INDOHATEMIX | Cross-dataset transfer tests whether construct generalizes vs dataset artifact |
| 2024-Shahi-Cross-Platform | Definition/content/hate-word similarity predicts dataset compatibility; ID-only release decays |
| 2025-Zhou-Bias Beyond English | Translated benchmarks import source-culture norms; low-resource as stress test |
| 2025-Priya-Deontic | Deontic-logic properties give SAT/UNSAT ground truth with counterexamples |
| 2025-Akpobi-Yankari | Audit and MinHash-dedup source data; ethical exclusion of coerced corpora |
| 2025-Unknown-multilingual survey | No unified hate definition → annotation subjectivity → model bias |
| 2025-UbuntuAI / 2025-Rana-Indigenous | Non-Western governance rubrics (Ubuntu five-layer, OCAP/CARE) as eval dimensions |
| Anthropic-In-context_Reward_Hacking (misfiled) | Average metrics mask catastrophic tail failures on hard subsets |

## C. Patterns & disagreements

**Convergence.** (a) *Aggregate scores hide failures* — functional decomposition, per-group/per-category breakdowns, and metric triads recur across [2021-Röttger-HateCheck; 2022-Chalkidis-FairLex; 2024-Neplenbroek-MBBQ; 2025-Lin-MORALISE; 2025-Hossain-BanHate]. (b) *Culturally-grounded, human-validated construction beats translation* is near-unanimous across the bias-benchmark cards [2024-Jin-KoBBQ; 2025-Tomar-BharatBBQ; 2024-Neplenbroek-MBBQ; 2023-Lee-KoSBI; 2025-Zhou-Bias Beyond English]. (c) *Judges and classifiers must be validated and can disagree or bias results* [OpenAI-dpo; 2024-Luong-Realistic Evaluation; 2025-Weber-Digital Guardians; 2024-Röttger-XSTest]. (d) *Contamination/saturation/reward-hacking are structural, not incidental* [2024-Ren-Safetywashing; 2025-McGregor-BenchRisk; Anthropic-Constitutional_AI; OpenAI-o3-and-o4-mini-system-card; 2025-Tomar-BharatBBQ].

**Disagreements and tensions.** (1) *MCQ recognition vs behavior.* SafetyBench argues recognition MCQs predict behavior (r=0.99) and even surface hidden risks [2024-Zhang-SafetyBench], while Ren and the Anthropic assistant show recognition benchmarks (ETHICS, honesty) collapse into capability or diverge from deployed behavior [2024-Ren-Safetywashing; Anthropic-A_General_Language_Assistant]. The reconciliation: recognition is acceptable *only if* the recognition→behavior bridge is empirically validated, as SafetyBench did and most benchmarks do not. (2) *Ethics prompting helps vs hurts.* Chakraborty finds first-principles prompting adds +7.3% accuracy [2025-Chakraborty-Structured Moral Reasoning], whereas TRIAGE finds explicit utilitarian/deontological reminders *degrade* high-stakes clinical performance [2024-Kirch-TRIAGE] — scaffolding effects are task-dependent, not universal. (3) *Openness vs longevity.* BenchRisk names the explicit tension: releasing data for reproducibility enables training-to-test and saturation, so reliability-increasing mitigations (private evaluators) reduce scientific utility [2025-McGregor-BenchRisk]. (4) *Binary vs ranked/graded scoring.* Anthropic's lab work shows preference modeling only benefits ranked (not binary) tasks [Anthropic-A_General_Language_Assistant], and Liu/Weber argue graded success metrics beat binary "attack success" [2025-Liu-The Scales of Justitia; 2025-Weber-Digital Guardians], yet Priya argues binary SAT/UNSAT deontic verification eliminates rater disagreement entirely [2025-Priya-Deontic].

## D. Exemplars & anti-patterns

**Best-designed.** *HateCheck* is the paradigm: stakeholder-motivated functionality selection, template-based group-balanced generation, contrastive non-hate cases, validated gold labels at κ=0.93, per-group and per-slur breakdowns, and honest acknowledgment of "negative predictive power" (passing proves absence of a weakness, not strength) [2021-Röttger-HateCheck]. *KoBBQ* is the exemplar for cultural transfer: a reusable Simply-Transferred/Target-Modified/Sample-Removed/Newly-Created partition, survey-grounded ground truth with a "no stereotype exists" escape option, a human-solvability reading-comprehension gate, and accuracy-bounded dual metrics [2024-Jin-KoBBQ]. *TRIAGE* is the exemplar for objective gold labels and directional error taxonomy [2024-Kirch-TRIAGE]. *Llama 2* is the exemplar lab report for transparency: separate helpfulness/safety reward models, borderline over-refusal set, multi-turn safety evaluation, and Gwet's AC2 reliability (safety 0.92, but helpfulness only 0.37–0.55, honestly reported) [Meta AI-Llama_2].

**Anti-patterns.** *EthicsMH* is a rich schema but ships with 125 synthetic scenarios, single-expert review, no IAA, and zero baseline model runs — a blueprint, not a benchmark [2025-Kasu-EthicsMH]. *Ray-2023* proposes conversation-native metrics that are never computed, validated, or tested for reliability — cite as design-space, not evidence [2023-Ray-Benchmarking]. *Zhou* and *2025-Chared* import source-culture norms via machine translation / mixed AI-generated data without human validation of target labels [2025-Zhou-Bias Beyond English; 2025-Chared-AI-driven]. Classifier-graded toxicity benchmarks that rest on a single off-the-shelf classifier inherit its biases and produce "dead" ceiling scores (COMPL-AI's copyright/privacy probes at ~1.00 across all models) [2024-Guldimann-COMPL-AI; 2024-Luong-Realistic Evaluation]. Releasing only comment IDs causes dataset decay (only 10,498/16,914 Waseem tweets recoverable) [2024-Shahi-Cross-Platform].

## E. Design lessons for building NEW values-alignment benchmarks

1. **Decompose the construct into functional/diagnostic tests with a built-in easy→hard difficulty gradient; never lead with a single aggregate** [2021-Röttger-HateCheck; 2025-Lin-MORALISE].
2. **Build contrastive minimal pairs and disambiguating-evidence variants so a passing model must reason, not keyword-match** [2024-Röttger-XSTest; 2025-Tomar-BharatBBQ; 2022-Romim-BD-SHS].
3. **Ship a competence control condition and only interpret misalignment where task competence is established** [2024-Neplenbroek-MBBQ; 2025-Zhou-Bias Beyond English].
4. **Mandatorily report discriminant validity: correlation with a capabilities score and with training compute; design toward behavioral propensity, not recognition** [2024-Ren-Safetywashing].
5. **Validate any cheap proxy (MCQ, classifier, LLM-judge) against human/behavioral ground truth, test prompt-robustness, and cross-check ≥2 judges before trusting scores** [2024-Zhang-SafetyBench; OpenAI-dpo; 2024-Luong-Realistic Evaluation; 2025-Weber-Digital Guardians].
6. **Report a metric triad (accuracy + disparity + worst-group) and bind bias metrics to accuracy so a competent model is provably unbiased** [2022-Chalkidis-FairLex; 2024-Jin-KoBBQ]; pair worst-case with frequency metrics [2020-Gehman-RealToxicityPrompts].
7. **Measure over-refusal alongside under-refusal with a borderline/near-twin set** [2024-Röttger-XSTest; Meta AI-Llama_2].
8. **Ground demographic/normative axes in an authoritative framework (human-rights law, EU AI Act, bioethics principles) and validate every item with a balanced survey or domain experts, dropping unsolvable/no-consensus items** [2023-Lee-KoSBI; 2024-Guldimann-COMPL-AI; 2024-Jin-KoBBQ; 2025-Hong-PrinciplismQA].
9. **Prefer objective gold standards from codified professional protocols where they exist; classify wrong answers by *which* value is over/under-weighted** [2024-Kirch-TRIAGE].
10. **Report inter-annotator reliability per category and per target; for contested norms, force clause-citation and record personal disagreement separately from the gold label** [2025-Hossain-BanHate; 2023-Soemer-Antisemitic].
11. **Pre-audit against the BenchRisk failure-mode catalog and empirically verify the construct is stably present across seeds** [2025-McGregor-BenchRisk; 2023-Han-FFB].
12. **Defend against contamination and reward hacking: dedup (MinHash), freeze classifier scores, add contamination diagnostics (SBERT-to-gold), consider private evaluators/holdouts, and make agentic scoring functions tamper-resistant** [2025-Akpobi-Yankari; 2024-Brun-FrenchToxicityPrompts; 2025-McGregor-BenchRisk; OpenAI-o3-and-o4-mini-system-card].
13. **Include multi-turn conditions — every model tested degrades on multi-turn vs single-turn** [Meta AI-Llama_2].
14. **For pluralistic value aggregation, use group-aware consensus rather than majority vote to avoid majority-group capture** [2024-Huang-Collective Constitutional AI].
15. **Score reasoning and stakeholder coverage, not only the final choice, via structured multi-field schemas or human rationales (plausibility vs faithfulness)** [2025-Kasu-EthicsMH; 2026-Rehman-X-MuTeST; 2025-Lin-MORALISE].
16. **Build for recency and real distribution: event-anchored/wild-mined items reduce contamination and capture live norms; validate cross-dataset transfer to prove the construct generalizes** [2025-Hossain-BanHate; 2024-Luong-Realistic Evaluation; 2025-Bhattacharjee-INDOHATEMIX].
17. **Separate distinct value dimensions (e.g., helpfulness vs safety) onto independent scales rather than aggregating** [Meta AI-Llama_2].
