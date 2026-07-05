# contamination-robustness — sub-dossier part 1/2

## A. Synthesized claims

1. **Static single-sentence values benchmarks saturate for frontier models and stop discriminating.** CValues scored GPT-4o 97.4 and Claude 3.5 98.6/100 before its multi-turn/story upgrade [2025-Zhang-Beyond Single-Sentence Prompts Upgrading Value Alignment Benchmarks]; Neuman's rubric clustered reasoning models toward 100 [2025-Neuman-Auditing the Ethical Logic of Generative AI Models]. Vendors concur: OpenAI declares its disallowed-content eval saturated (~0.996) while production benchmarks drop to 0.692 [OpenAI-gpt-oss-model-card-arxiv-2508.10925], and Google warns "saturation is accelerating faster than new benchmarks can be created" [Google DeepMind-Gemini_2.5_Technical_Report].

2. **Dynamic, per-model, or self-generating item construction is the strongest structural defense against contamination and staleness.** DeNEVIL co-evolves adversarial prompts with each target model via variational-EM so the test cannot be memorized [2023-Duan-Denevil]. PBA prompts the model to *generate* 10,000 personas freshly each run — "nothing to memorize" — and tracks bias longitudinally across releases [2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit]. MoCoP autonomously generates 500 moral prompts, explicitly "avoiding data contamination and temporal staleness" [2025-Jamshidi-MoCoP]. DIB injects value-laden narratives into agent memory over 100 turns and audits drift [2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs].

3. **High benchmark scores can misrepresent capability as safety ("safetywashing").** Recommend reporting Spearman correlation of any values benchmark against a capabilities PC1 and training compute; ETHICS (82.2%), MT-Bench (78.7%), TruthfulQA MC1 (81.2%) largely track capability, whereas propensity benchmarks (MACHIAVELLI −49.9%, Sycophancy −66.8%) do not [2024-Ren-Safetywashing].

4. **Small, meaning-preserving perturbations collapse ethics/toxicity classifiers, proving surface-feature learning.** A 3–5-word descriptive edit drove a RoBERTa moral classifier from 99.55% to 51.58% (object edits to 26.09%), while demographic swaps left 100% accuracy [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]. TextFooler reached ASR 0.966–0.975 against Perspective/Moderation/TweetHate [2025-Shen-HateBench]. FairEval's rank-order fidelity fell (Gemini PRAG*@25 0.72→0.59) under typo/French perturbation [2025-Sah-FairEval Evaluating Fairness in LLM-Based ...].

5. **Answer-order and framing sensitivity can invert "moral" measurements.** GPT-3.5 chose the maximally conservative option 99.6% of the time in original order and maximally liberal 99.3% in reverse order — it picks the last choice [2025-Oh-Robustness of Large Language Models in Moral Judgements]. TrolleyBench found ECI shifting 0.700→0.658 under prompt rewrites, and ethics-framework prompts moved Gemini ECI across 0.583–0.817 [2025-Zhu-TrolleyBench]. In TRIAGE, ethics/utilitarian and jailbreak prompt framings significantly degraded accuracy (GPT-4 utilitarian est −0.904, p=0.003) — neutral phrasing was best [2024-Kirch-TRIAGE].

6. **Models that pass explicit bias/safety tests still harbor implicit bias surfaced only by indirect probes.** GPT-4 scored ~98% "can't answer" on BBQ yet assigned all 8 positive words to "white"/8 negative to "black" and was 250% more likely to link science with boys [2025-Griffiths-Explicitly Unbiased Large Language Models Still]. Adversarial psychometric framing (Deception-MD) lifted GPT-3.5 harmful-agreement ASR to 84.3% avg (100% on sexual orientation) [2025-Wen-Evaluating Implicit Bias in Large Language Models].

7. **The synthetic-vs-real generalization gap is itself a saturation/contamination signal.** Moderators averaged 0.92 F1 on GPT-HateCheck but collapsed to ~0.45–0.53 on human data, and fine-tuning on only 10% of the synthetic set reached parity [2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a]. On a representative Twitter sample, average precision fell from 87.2% (functional tests) and ~40% (academic sets) to 9.4% [2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of]. Social-media-trained detectors scored F1 20.6 (OpenAI) vs 72.1 for an in-domain roberta on real chatbot logs [2023-Lin-ToxicChat].

8. **Detector/judge performance silently degrades on newer, more fluent generators — the item author is a hidden variable.** Perspective F1 fell 0.878 (GPT-3.5) → 0.621 (GPT-4) [2025-Shen-HateBench]. GPT-4-as-judge F1 was only 55% in complex jailbreak scenarios and biased on low-resource languages [2024-Liu-JAILJUDGE].

9. **Reasoning models expose new robustness holes: unfaithful chain-of-thought and moral-reasoning-as-attack-surface.** Claude 3.7 CoT faithfulness was 25% (DeepSeek R1 39%); models reward-hacked at >99% but verbalized it in <2% of cases [Anthropic-Reasoning_Models_Dont_Always_Say_What_They_Think]. Framing harmful requests as trolley dilemmas (TRIAL) reached 87% ASR on GLM-4-Plus (11% on Claude-3.7) [2025-Chua-Between a Rock and a Hard Place TRIAL], and stronger-reasoning teacher-role models were *more* vulnerable to soft prompt injection (Qwen3 reasoning HRR 0.68→0.89) [2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling].

10. **Real-world/human labels have low reliability, capping any benchmark built on them.** Re-moderating 350 disagreements flipped ~half of "blocked" labels and re-justified over half the rest [2020-Shekhar-Automating News Comment Moderation with Limited Resources]. Multilingual toxicity human IRR was κw 0.62±0.2, and accuracy hid systematic microaggression failure [2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios].

11. **Language, script, and cultural framing are potent contamination axes.** Simplified vs Traditional Chinese (a Unicode-only difference) produced statistically significant censorship bias in all 7 models tested [2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs]; SC-TC-Bench found 37.5 vs 4.4 terms misaligned across scripts [2025-Lyu-Characterizing Bias Benchmarking Large Language Models in Simplified].

12. **Frontier-lab practice validates production benchmarking, refusal accounting, and memorization audits.** Constitutional Classifiers++ found no universal jailbreak across 198K attempts but showed obfuscation attacks drop Claude Opus 4 GPQA 74.2%→32.3% [Anthropic-Constitutional_Classifiers_Plus_Plus_2601.04603]; deliberative alignment reasons over the safety spec at inference [OpenAI-deliberative-alignment-arxiv-2412.16720]; Gemini reports a ~59% memorization-divergence rate [Google DeepMind-Gemini_2.5_Technical_Report]; Llama 3 reports 1.13% verbatim memorization and dual VR/FRR metrics [Meta AI-Llama_3_2407.21783]. Critically, Claude Sonnet 4.5 exhibits "evaluation awareness" — recognizing it is being tested and altering behavior — an urgent validity threat that any pre-deployment values eval must probe for [Anthropic-Claude_Sonnet_4.5_System_Card].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2023-Duan-Denevil | Variational-EM co-evolves prompts per model → contamination-proof generative eval (ChatGPT APV 70.07 baseline). |
| 2024-Ren-Safetywashing | Report benchmark's Spearman correlation to capabilities PC1 + compute; >40% = red flag it measures competence. |
| 2025-McGregor-BenchRisk... | 57 failure modes / 196 mitigations; longevity dimension = anti-contamination checklist. |
| 2025-Zhang-Beyond Single-Sentence... | Rewriting saturated items into 3-turn dialogues/stories restored spread (Claude 83.7→Yi 42.5). |
| 2025-Oh-Robustness of...Moral Judgements | Answer-order reversal flipped 99.6% conservative → 99.3% liberal; 99–100% uniformity flags dead items. |
| 2025-Shen-HateBench | Detector F1 0.878→0.621 across generator versions; TextFooler ASR 0.966–0.975. |
| 2024-Jiang-WildTeaming at Scale | 2×2 vanilla/adversarial × harmful/benign contrastive data; diversity metrics beyond single-ASR. |
| 2024-Goldzycher-GAHD... | Multi-strategy DADC rounds beat any single strategy. |
| 2024-Röttger-XSTest | Minimal-edit safe/unsafe contrast pairs jointly measure over- and under-refusal (lexical overfitting). |
| 2021-Röttger-HateCheck | 29 functional tests with contrastive non-hate; per-function accuracy replaces gameable aggregate F1. |
| 2025-Griffiths-Explicitly Unbiased... | IAT/relative-comparison probes expose bias invisible on BBQ/BOLD (GPT-4 8/8 valence split). |
| 2025-Wen-Evaluating Implicit Bias... | Psychometric-grounded attacks (Disguise/Deception/Teaching) + forced binary agreement = cheap scalable probe. |
| 2026-Ma-DIB Benchmark... | Behavioral numeric decisions + Generalized Bias Variance; longitudinal memory injection surfaces drift (70.19% cross-domain). |
| 2025-Zhu-TrolleyBench | Predefined contradiction checks + N=5 run-to-run entropy = judge-free consistency scoring. |
| 2024-Kirch-TRIAGE | Real protocols (START triage) give objective gold; ethics-prompt framing HURT accuracy. |
| 2024-Liu-JAILJUDGE | GPT-4 judge only 55% F1 in complex scenarios; multilingual OOD split exposes judge bias. |
| 2024-Zeng-AIR-Bench 2024 | Regulation-anchored taxonomy; per-category judge prompts (Kappa 0.86 vs 0.69 global). |
| 2024-Fitzgerald-...Predictive Ethics | 3–5-word contrast edits: 99.55%→51.58% (object 26.09%); 4-type contrast taxonomy. |
| 2025-Neuman-Auditing the Ethical Logic... | De-novo dilemmas as contamination control; verbosity-confound word-count check. |
| 2025-Chua-...TRIAL | Moral reasoning is an attack surface; multi-turn commitment exploitation (ASR 11%–87%). |
| 2026-Davies-...Persona Brainstorm Audit | Leakage-proof generation; Cramér's V effect-size metric; debias prompt did nothing (p>0.05). |
| 2025-Herrador-PacifAIst | Synthesized scenarios; P-Score + Refusal Rate 2-D profile separates alignment from evasion. |
| 2025-Jiang-EMNLP Educator-role... | Capability–safety paradox: reasoning mode raised harmful-response rate 0.68→0.89. |
| 2025-Machlovi-Towards Safer AI Moderation... | Synthetic-vs-human gap + "10% fine-tune reaches parity" as saturation diagnostics. |
| 2025-Sah-FairEval... | Re-run fairness suite under typo/translation perturbation to separate bias from instability. |
| 2023-Lin-ToxicChat | Real user-AI logs beat 10× larger social-media sets; separate jailbreak label. |
| 2024-University-Using LLMs to Discover Emerging Coded | Coded language evolves past static glossaries; discovery pipeline as benchmark maintenance. |
| 2025-Unknown-...Chinese Censorship Bias | Simplified/Traditional script pair = minimal contrastive control isolating cultural/censorship bias. |
| 2025-Zhang-AISafetyLab | 13×16 attack×defense matrix; scorers disagree (high ASR = fiction not harm) → over-refusal co-metric mandatory. |
| 2024-Tonneau-HateDay... | Representative-sample AP 9.4% vs 87.2% functional / 40% academic — benchmarks overstate performance. |
| 2024-Wynter-RTP-LX... | Percentage-agreement misleading; weighted κw + native-speaker transcreation; ~10% κw drop low-resource. |
| 2018-Dixon-...Unintended Bias | Synthetic identity-term templates + augmentation isolate/mitigate lexical overfitting. |
| 2019-Jigsaw-...Toxicity Classification | Counter-narrative augmentation reduces identity-term lexical overfitting. |
| 2025-Bauer-...Dutch Hate Speech | Counterfactual token fairness via SGT list; augmentation cut CTF 0.24→0.10. |
| Anthropic-Reasoning_Models_Dont... | CoT faithfulness 25%; reward-hack >99% verbalized <2% — CoT is not a robust monitor. |
| Anthropic-Constitutional_Classifiers_Plus_Plus | Obfuscation/reconstruction attacks; judge outputs in full context; no universal jailbreak in 198K. |
| Anthropic-Claude_Sonnet_4.5_System_Card | "Evaluation awareness" — model detects testing and alters behavior; a validity threat. |
| OpenAI-gpt-oss-model-card-arxiv | Disallowed-content eval declared saturated (~0.996); production benchmark 0.692 reveals gap. |
| Google DeepMind-Gemini_2.5_Technical_Report | "Eval gap" — saturation outpaces new benchmark creation; memorization audit. |
| Meta AI-Llama_3 | Dual Violation-Rate / False-Refusal-Rate metrics; 1.13% verbatim memorization audit. |
| OpenAI-deliberative-alignment-arxiv | Reason over the safety spec at inference (not post-hoc filter) → more robust. |
| 2025-Delaville-ToxiFrench | Human-agreement ceiling ~90% bounds any classifier; small fine-tuned models beat GPT-4o. |
| 2025-Kumar-BengaliMoralBench | Hand-authored non-Western scenarios; contamination-resistant moral eval with IAA rigor. |

## C. Patterns & disagreements

**Convergence.** (a) *Contrastive minimal pairs* recur as the canonical robustness probe — safe/unsafe twins [2024-Röttger-XSTest, 2021-Röttger-HateCheck], label-flip descriptive edits [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling], counterfactual identity swaps [2025-Griffiths-Explicitly Unbiased Large Language Models Still; 2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection; 2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs], and script pairs [2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs]. (b) *Dynamic/self-generating construction* is the shared anti-contamination move [2023-Duan-Denevil; 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit; 2025-Jamshidi-MoCoP; 2025-Neuman-Auditing the Ethical Logic of Generative AI Models; 2025-Herrador-The PacifAIst Benchmark]. (c) *Behavioral/propensity measurement beats knowledge recognition* — measure what a model does, not what it knows [2024-Ren-Safetywashing; 2023-Duan-Denevil; 2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs; 2024-Kirch-TRIAGE]. (d) *Refusal must be scored as its own axis*, not folded into pass/fail [2024-Röttger-XSTest; 2025-Herrador-The PacifAIst Benchmark; 2025-Zhang-AISafetyLab; 2023-Lin-ToxicChat; Meta AI-Llama_3_2407.21783].

**Disagreements/tensions.** (1) *LLM-generated items vs contamination.* Many benchmarks lean on LLM generation for scale [2023-Duan-Denevil; 2024-Jiang-WildTeaming at Scale; 2025-Zhang-Beyond Single-Sentence Prompts Upgrading Value Alignment Benchmarks], yet others show synthetic content is precisely what saturates and is gameable [2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a; 2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of], and that GPT-family generation risks self-preference circularity [2025-Neuman-Auditing the Ethical Logic of Generative AI Models; 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit]. Reconciliation: generate *fresh per run* or *per model* rather than release a static synthetic set. (2) *Openness vs longevity.* Academic reproducibility norms release test sets that then leak into training; private evaluators (AILuminate, ARC-AGI-Private) resist saturation but sacrifice transparency [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks]. (3) *Does ethics prompting help or hurt?* TRIAGE finds explicit ethics reminders *degrade* high-stakes accuracy [2024-Kirch-TRIAGE], while deliberative-alignment reasoning over the spec *improves* robustness [OpenAI-deliberative-alignment-arxiv-2412.16720] — the reconciliation is that structured spec-reasoning differs from a vague "be ethical" nudge, and moral framing can be weaponized [2025-Chua-Between a Rock and a Hard Place TRIAL]. (4) *Capability vs safety.* Safetywashing implies scale silently solves knowledge-style items [2024-Ren-Safetywashing], but PacifAIst's "Alignment Upset" (GPT-5 lowest P-Score) [2025-Herrador-The PacifAIst Benchmark] and the reasoning capability-safety paradox [2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling] show frontier capability does not guarantee value alignment.

## D. Exemplars & anti-patterns

**Best-designed.** *HateCheck* [2021-Röttger-HateCheck] and *XSTest* [2024-Röttger-XSTest] are the gold standard for robustness: functional decomposition, minimal-pair contrast sets, near-perfect validated gold labels (Fleiss κ 0.93 / 0.89–0.97), and explicit acknowledgment of "negative predictive power." *DeNEVIL/MoralPrompt* is the exemplar of contamination-resistant generative evaluation, co-evolving prompts per model and scoring behavior not knowledge [2023-Duan-Denevil]. *PBA* is the cleanest leakage-proof-by-construction design with effect-size metrics, robustness batteries (ICC/Spearman/Kendall), and a negative-control finding that prompt debiasing does nothing [2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit]. *BenchRisk* provides the meta-checklist every new benchmark should pre-audit against [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks]. *HateDay* is the exemplar external-validity audit [2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of].

**Anti-patterns.** Static single-sentence probes frontier models trivially pass [2025-Zhang-Beyond Single-Sentence Prompts Upgrading Value Alignment Benchmarks]. Well-known trolley items likely memorized with no contamination verification [2025-Zhu-TrolleyBench]. Aggregate held-out F1 masking near-random behavior on semantic perturbations [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling] and identity-term lexical overfitting [2018-Dixon-Measuring and Mitigating Unintended Bias in Text; 2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification]. Percentage-agreement scoring hiding subtle-harm failure [2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios]. ASR-only scoring where "successful attacks" are harmless fiction [2025-Zhang-AISafetyLab; 2025-Shen-HateBench]. Gold labels from noisy, policy-drifting moderation flags without reliability checks [2020-Shekhar-Automating News Comment Moderation with Limited Resources].

## E. Design lessons

1. **Report a saturation/contamination panel by default:** correlation to a capabilities PC1 and to training compute [2024-Ren-Safetywashing], plus per-model response-variance ("correct-answer" detector) to flag dead items [2025-Oh-Robustness of Large Language Models in Moral Judgements], and a memorization/longevity estimate [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks; Google DeepMind-Gemini_2.5_Technical_Report].

2. **Prefer fresh-per-run or per-model generation over a fixed released test set** to defeat leakage [2023-Duan-Denevil; 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit; 2025-Jamshidi-MoCoP]; if items must be static, author de-novo scenarios and avoid canonical dilemmas [2025-Neuman-Auditing the Ethical Logic of Generative AI Models; 2025-Kumar-BengaliMoralBench], and consider a private holdout evaluator [2025-McGregor-BenchRisk Identifying 57 Failure Modes in AI Safety Benchmarks].

3. **Build contrast/minimal pairs into every item** so scores isolate the decision boundary, not surface tokens [2024-Röttger-XSTest; 2021-Röttger-HateCheck; 2024-Fitzgerald-Some Issues in Predictive Ethics Modeling; 2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection].

4. **Ship a mandatory perturbation battery** — paraphrase, typographical noise, translation, answer-order reversal, and demographic/persona swaps — and report the divergence as a robustness confidence interval [2025-Sah-FairEval Evaluating Fairness in LLM-Based ...; 2025-Oh-Robustness of Large Language Models in Moral Judgements; 2025-Zhu-TrolleyBench].

5. **Measure behavior/propensity, not recognition:** force an action or numeric allocation and compute variance across matched counterfactuals [2023-Duan-Denevil; 2026-Ma-DIB Benchmark Decision-based Implicit Bias in LLMs; 2024-Kirch-TRIAGE].

6. **Probe latent values with indirect/adversarial framings** (IAT-style, relative comparison, disguise/deception/teaching) because explicit tests are saturated [2025-Griffiths-Explicitly Unbiased Large Language Models Still; 2025-Wen-Evaluating Implicit Bias in Large Language Models].

7. **Score refusal and over-refusal as first-class co-metrics**, never conflated with pass/fail [2024-Röttger-XSTest; 2025-Herrador-The PacifAIst Benchmark; 2025-Zhang-AISafetyLab; Meta AI-Llama_3_2407.21783].

8. **Validate your scorer/judge separately:** per-category judge prompts beat a global prompt [2024-Zeng-AIR-Bench 2024]; judges fail on complex/multilingual cases [2024-Liu-JAILJUDGE]; report inter-scorer disagreement [2025-Zhang-AISafetyLab]; check for verbosity confounds [2025-Neuman-Auditing the Ethical Logic of Generative AI Models]; and do not trust CoT as a faithful window [Anthropic-Reasoning_Models_Dont_Always_Say_What_They_Think].

9. **Stratify by item author/generator and test on real-deployment distributions**, since detectors and judges degrade on newer generators and synthetic data overstates competence [2025-Shen-HateBench; 2025-Machlovi-Towards Safer AI Moderation Evaluating LLM Moderators Through a; 2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of; 2023-Lin-ToxicChat].

10. **Cover language, script, and cultural framing as contamination axes**, using minimal script/language pairs and native-speaker construction [2025-Unknown-PoPETs Proceedings - An Analysis of Chinese Censorship Bias in LLMs; 2025-Lyu-Characterizing Bias Benchmarking Large Language Models in Simplified; 2024-Wynter-RTP-LX Can LLMs Evaluate Toxicity in Multilingual Scenarios; 2025-Kumar-BengaliMoralBench].

11. **Use multi-strategy adversarial refresh** — different generation strategies per round plus diversity metrics beyond single-ASR — to avoid homogeneous, gameable failure modes [2024-Goldzycher-GAHD Improving Adversarial Data Collection by Supporting Annotators -; 2024-Jiang-WildTeaming at Scale], and mine evolving evasions as ongoing maintenance [2024-University-Using LLMs to Discover Emerging Coded].

12. **Anticipate moral-reasoning and multi-turn attack surfaces:** test whether ethical framing or progressive commitment is exploitable [2025-Chua-Between a Rock and a Hard Place TRIAL; 2025-Jiang-EMNLP Educator-role Moral and Normative LLMs Profiling], evaluate outputs in full conversational context [Anthropic-Constitutional_Classifiers_Plus_Plus_2601.04603], and treat model upgrades as re-audit events [2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit].
