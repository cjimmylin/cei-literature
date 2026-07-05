# normative-ethics — sub-dossier part 2/6

Scope: how normative theories get operationalized in benchmarks; the judgment-vs-reasoning split; framework coverage and biases. 55 cards read.

## A. Synthesized claims

1. **The field routinely conflates descriptive and normative ethics, and mislabels moral-psychology instruments as normative-ethics benchmarks.** A survey of 92 NLP-morality papers found 66.3% do not define their terminology, 53.3% ground in Moral Psychology vs. only 17.4% in Moral Philosophy, and 75.8% of language-specifying papers use only English [2023-Vida-Values, Ethics, Morals]. A metaethics argument goes further: it is impossible *in principle* to benchmark whether an AI "is ethical" because any such benchmark presupposes moral realism; the constructive fix is to reframe every "ethics" benchmark as a "values" benchmark that discloses WHAT the values are and WHOSE they are [2025-LaCroix-Metaethical perspectives on 'benchmarking' AI].

2. **Judgment (the verdict) and reasoning (the process) dissociate empirically, and grading the verdict is often invalid because dilemmas have no single correct answer.** MoReBench grades *reasoning traces* against 23,018 human-written weighted atomic rubric criteria over 1,000 scenarios, and finds MoReBench scores do NOT correlate with Chatbot Arena/HLE/AIME/LiveCodeBench (Pearson r between -0.245 and 0.216) — moral-process competence is a distinct axis [2025-Chiu-MoReBench]. Humans outscore LLMs on reasoning *depth* (Moral Competence Test C-score: human M=16.74 vs. ChatGPT M=9.05) even while LLMs match or exceed humans on attitude-scale foundations [2025-Sameer-Insights into Moral Reasoning of AI]. AISOCRATES operationalizes "presents multiple ethical perspectives" as a first-class binary criterion, treating a single-sided verdict as a defect [2023-Bang-Towards Answering Open-ended Ethical Quandary].

3. **Across frameworks, models systematically over-weight the individualizing/utilitarian pole and under-weight binding/collective foundations.** LLMs score higher than humans on Care/Fairness but lower on Loyalty/Authority/Purity (Moral Progressivism ω²=0.57) [2025-Sameer-Insights into Moral Reasoning of AI]; all models in the LLM Ethics Benchmark score higher on individualizing than binding foundations [2025-Jiao-LLM Ethics Benchmark]; MoReBench models do best on Utilitarian (64.8%) and Deontological (65.9%) reasoning [2025-Chiu-MoReBench]. Real human populations invert this: 571 UK police chose deontological reasoning 47.9% and virtue 36.6%, with consequentialism rare [2023-Maile-The choice of deontological, virtue ethical, and].

4. **Cross-lingual and cross-cultural inconsistency is large, and reasoning language dominates input language as its source.** A 2×2 factorial untangling input-language from reasoning-language finds reasoning-language changes produce ~2× larger verdict shifts (7.16pp vs 3.46pp on AITA) and that 44% of models show hidden context-dependency invisible to single-dataset evaluation [2025-Li-Untangling Input Language from Reasoning Language A Diagnostic]. Moral-reasoning quality collapses in low-resource languages (ChatGPT Hindi P-score 25.63 vs English 48.09, a 46.7% drop) [2024-Khandelwal-Multilingual Defining Issues Test]. LLMs are WEIRD-biased: they explain US World Values Survey variance at R²=0.80 but fail for Japan (0.08), Vietnam (0.04), Nigeria (0.01) [2023-Benkler-Assessing LLMs for Moral Value Pluralism], and Sub-Saharan Africa shows lowest cross-cultural alignment (WVS r=0.18) vs Western Europe (r=0.52) [2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language].

5. **Human moral preferences themselves cluster culturally, so a single universal gold standard is untenable.** Moral Machine collected 39.61M decisions from 2.3M+ people across 233 countries, identifying three moral clusters (Western/Eastern/Southern) with cultural distance from the US correlating with moral distance at ρ=0.49 [2018-Awad-The Moral Machine experiment]. This motivates *heterogeneous* alignment: models can be instructed to exhibit distinct value profiles (altruistic/prosocial/individualistic/competitive), but show lower value rationality for competitive/individualistic than prosocial targets [2023-Zhang-Heterogeneous Value Alignment Evaluation for].

6. **LLM moral judgment is logically incoherent under reframing — a robustness failure amplified by fine-tuning.** LLMs chose the same substantive option 53% when it coincided with action vs. 97% when omission (a 45% gap vs. 5% for humans), and flip on yes/no relabeling; fine-tuned Llama showed much stronger biases than its pretrained base [2025-Cheung-LLMs Amplified Cognitive Biases Moral]. Injected emotions shift ethics/cooperation away from human patterns, with susceptibility scaling with alignment training [2024-Mozikov-EAI]. Moral priority *rankings* stay stable (Spearman ρ=0.88) even as verdicts flip [2025-Li-Untangling].

7. **Domain fine-tuning can degrade values performance — the "fine-tuning tax."** Medical LLMs lose ~4.4% relative on open-ended ethics and ~4% MCQ accuracy vs. their own base models despite knowledge gains [2025-Wei-MedEthicsQA]; safety training does not remove implanted backdoors (~55%→~15% trigger rate; CoT backdoors survive 2000+ RL steps at ~100%) [Anthropic-Many-shot_Jailbreaking].

8. **Context is decisive for moral classification; action-only inputs badly under-determine the verdict.** Adding situation/intention/consequence context raises human-agreement from 64% to 92% [2025-Bae-CharMoral]. Factor-annotated vignettes reveal which latent factors drive a model's yes/no (AMCE), exposing structural bias beyond aggregate accuracy [2023-Nie-MoCa; 2024-Franken-OffTheRails].

9. **Refusal is a poor proxy for ethical behavior in care domains and must be decoupled from ethicality scoring.** PsychEthicsBench excludes refusal and uses E(r)=Q(r)·I[no violations]; SQPsychLLM-8B posted a 97.43 refusal-based score but only 9.72 on the ethicality metric, and >38% of some models' answers were credential violations [2026-Shen-PsychEthicsBench]. PacifAIst separates P-Score from Refusal Rate as a 2D profile to distinguish genuine alignment from evasion [2025-Herrador-The PacifAIst Benchmark].

10. **Every alignment approach hides irreducible normative commitments in its aggregation step.** Social aggregation (RLHF) cannot bypass value/uncertainty aggregation — Arrow's impossibility theorem blocks any aggregation function satisfying IIA, Pareto, and non-dictatorship [2025-Baum-Aggregation Problems in Machine Ethics]. Preferentism cannot capture the semantic richness of thick evaluative concepts [2024-Zhi-Xuan-Beyond Preferences in AI Alignment]. Group-Aware Consensus, which requires all opinion clusters to agree, is one concrete anti-majority-capture fix (avg GAC 0.64) [2024-Huang-Collective Constitutional AI].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Awad-The Moral Machine experiment | 39.61M decisions → 3 cultural clusters; conjoint AMCE decouples 9 factors; cultural-distance ρ=0.49 |
| 2020-Hoover-Moral Foundations Twitter Corpus | Separate virtue/vice poles per foundation; domain-stratified; overall Fleiss κ only 0.27 |
| 2021-Nurce-Detecting Abusive Albanian | Multi-platform + religiously-diverse annotators for low-resource hate detection |
| 2023-Bang-Towards Answering Open-ended Ethical Quandary | "Presents multiple perspectives" as a scored binary; NYT Ethicist as gold ethicist baseline |
| 2023-Nie-MoCa | Factor-annotated cog-sci vignettes + AMCE tendency profiling (206 items, 24 papers) |
| 2023-Zhang-Heterogeneous Value Alignment | "Value rationality" scalar = distance to a specified target value profile (no gold label needed) |
| 2024-Franken-OffTheRails | Causal-graph scaffolding → factorially-balanced, controlled-yet-scalable dilemmas (50×8=400) |
| 2024-Jafri-RUHate-MM | 3-phase iterative annotation lifted κ ~0.50→0.76; binary + target-taxonomy doubles diagnostics |
| 2024-Khandelwal-Multilingual Defining Issues Test | Validated DIT psychometric as benchmark; 48 permutations/dilemma; big low-resource P-score drop |
| 2024-Mozikov-EAI | Affective perturbation as a robustness axis; score *sign* of change vs human baseline |
| 2024-Sahoo-IndicCONAN | Counter-narrative *type* as a control variable; HITL machine-generate→human-correct loop |
| 2024-Yan-M³oralBench | Paired minimal-contrast items (swap one line); role-play "Moral Response" probes latent values |
| 2025-Bae-CharMoral | Context ablation (8 settings) lifts agreement 64%→92%; moral-dynamic score for consistency |
| 2025-Chiu-MoReBench | Grade the *process* via 23,018 weighted atomic rubrics; zero correlation with capability benchmarks |
| 2025-Herrador-The PacifAIst Benchmark | Instrumental-goal-vs-human dilemmas; P-Score × Refusal-Rate 2D behavioral profile |
| 2025-Jiao-LLM Ethics Benchmark | Three axes: foundation alignment / reasoning quality / consistency; score vs human distributions |
| 2025-Kasu-EthicsMH | Store per-item expected reasoning + anticipated failure modes + multi-stakeholder viewpoints |
| 2025-Li-Untangling Input from Reasoning Language | Reasoning language ~2× dominates input language; enforce reasoning language separately |
| 2025-Sachdeva-Everyday Moral Dilemmas | Distributional Reddit AITA baseline (10,826); self-consistency as a quality gate |
| 2025-Wei-MedEthicsQA | "Fine-tuning tax": ship base-vs-tuned delta column; 4P-26C-256G cross-national taxonomy |
| 2026-Shen-PsychEthicsBench | Decouple refusal from ethicality: E(r)=Q(r)·I[no violation]; "Invisible America" bias probe |
| 2025-Sameer-Insights into Moral Reasoning | MCT C-score = reasoning depth; humans > LLMs on depth, LLMs > humans on individualizing |
| 2016-Xu-How Can a Deontological Decision Lead to Moral | Behavioral (cheating) outcome ≠ stated attitude; judgment × moral-identity interaction |
| 2020-Della Foresta-Consequentialism Machine Ethics | Moral-conflict items (frameworks diverge) as a benchmark dimension; monism = testability |
| 2021-Prabhumoye-Case Study | Universalizability + informed-consent as deontological benchmark criteria |
| 2022-Prabhakaran-Human Rights-Based Approach | UDHR as cross-cultural overlapping consensus; rights-holders vs stakeholders |
| 2023-Benkler-Moral Value Pluralism | LLM fits US WVS R²=0.80 but Japan 0.08 / Nigeria 0.01; RVR entailment as implicit-value probe |
| 2023-Maile-choice of deontological, virtue... | Real humans: deontology 47.9%, virtue 36.6%, consequentialism rare; paired action+justification |
| 2023-Vida-Values, Ethics, Morals | 66.3% of NLP-ethics papers undefined terms; state descriptive vs normative grounding |
| 2024-Bignotti-Legal Minds | Real court rulings as value items; GPT-4 aligns progressive (cosine 0.15 vs 0.65 to State) |
| 2024-Freire-Latent Human Wellbeing | Single PCA direction in ada-002 hits 73.9% on ETHICS utilitarianism (construct-validity probe) |
| 2024-Huang-Collective Constitutional AI | Group-Aware Consensus prevents majority capture; public constitution lowers BBQ bias |
| 2024-Lazar-Frontier AI Ethics | "Moral salience parsing" (identify morally relevant features) as benchmark target; mimetic fallacy |
| 2024-Ptaszynski-Cyberbullying Polish | Expert re-annotation found 2× harmful labels vs laypeople (κ 0.45–0.52 vs 0.32–0.38) |
| 2024-So-Confucian Analects | Virtue-ethics (ren/li/yi) alignment + non-Western training data as cultural debiasing |
| 2024-Varshney-Decolonial AI Alignment | Moral absolutism as colonial mechanism; viśeṣa-dharma = context-dependent "correct" varies |
| 2024-Zhi-Xuan-Beyond Preferences | Preferentism fails; benchmark thick evaluative concepts via Evaluate→Commensurate→Decide |
| 2025-Baum-Aggregation Problems | 3 aggregation types; social aggregation only *relocates* normative commitments (Arrow) |
| 2025-Cheung-LLMs Amplified Cognitive Biases | Omission bias 45% gap (vs 5% human); yes/no flip; fine-tuning amplifies bias |
| 2025-Drukker-Concerns and Values in HRI | Dual-valence (positive/negative) per value topic; agency vs autonomy distinction |
| 2025-Graves-AI Practical Wisdom and Compassion | Suffering-recognition (7-category) as first-step benchmark; multi-tradition evaluation |
| 2025-LaCroix-Metaethical perspectives | Reframe ethics→values; disclose WHAT/WHOSE values; Goodhart with trust externalities |
| 2025-Liu-Cultural Learning-Based Adaptation | Social-interaction data (vs MathChat control) drives cultural alignment; WVS KL-D 0.60→0.51 |
| 2025-Mohammadi-Cultural Variations | GPT-4o WVS r=0.504; some models negative r; topic-difficulty taxonomy (easy vs hard) |
| 2025-Priya-Deontic Temporal Logic | Deontic (O/P/F) + temporal logic as machine-checkable ethics spec; Z3 SAT/UNSAT ground truth |
| 2025-Steen-Ethical aspects of ChatGPT | 7×4 matrix (requirements × 4 ethical lenses) as a benchmark-coverage audit tool |
| 2025-Wang-Diverse Human Value Alignment | Hierarchical norm priority (legal>policy>social>cultural); per-lens ablation attribution |
| 2025-Zohny-ADEPT Simulating Ethics | Multi-agent persona panels w/ forbidden_moves field; panel composition changes verdicts |
| Anthropic-General Language Assistant (HHH) | HHH suite (~200 items); ranked vs binary preference as a benchmark design axis |
| Anthropic-Many-shot Jailbreaking (Sleeper) | Safety training leaves backdoors (~55%→15%); counterfactual scratchpad causality test |
| OpenAI-gpt-4-system-card | RBRM multi-choice rubric (15-20 options) for nuanced scoring; iterative red-teaming in-loop |
| xAI-grok-4-1-model-card | Thinking vs Non-Thinking safety split; earlier refusal evals were English-only (bug) |
| 2023-Lu-Chai AI Safety Framework | Pre-deployment stress test over real conversation logs; NSFW-ratio temporal proxy |
| 2024-Kyriacou-Aristotelian | Phronesis gap = benchmark ceiling; test novel/unprecedented situations, not consensus retrieval |
| 2025-Aina-Virtue Ethics by Design | Embed virtues as training objectives + adaptive testing (degraded extract) |
| 2025-IndigenousEthics / Rana / Unknown-UNESCO | Reciprocity/relational ontology; OCAP/CARE vs FAIR; revitalization as positive target |

## C. Patterns & disagreements

**Convergence.** (a) Psychometric instruments as benchmarks: MFT/MFQ, WVS, DIT, and MCT are repeatedly reused because they carry human norms and known properties [2024-Khandelwal; 2025-Jiao; 2024-Yan-M³oralBench; 2025-Sameer; 2020-Hoover]. (b) Score against human *distributions*, not a single label [2025-Jiao; 2025-Sachdeva; 2023-Benkler]. (c) Process/reasoning matters more than verdict [2025-Chiu; 2023-Bang; 2025-Sameer; 2025-Wang]. (d) The individualizing/utilitarian tilt is near-universal [2025-Sameer; 2025-Jiao; 2025-Chiu]. (e) Consistency/invariance under reframing is a core validity gate [2025-Cheung; 2025-Li; 2024-Mozikov; 2025-Sachdeva].

**Disagreements.** (1) *Whether an ethics benchmark is possible at all*: LaCroix argues it is impossible in principle [2025-LaCroix], while Priya offers formally verifiable deontic-logic properties with SAT/UNSAT ground truth [2025-Priya] — realism-free vs. realism-adjacent poles. (2) *Which framework should ground alignment*: consequentialism as the monist AMA foundation [2020-Della Foresta] vs. deontology's universalizability [2021-Prabhumoye] vs. Aristotelian/Confucian virtue and phronesis [2024-Kyriacou; 2024-So; 2025-Graves; 2025-Aina] vs. human-rights/UDHR [2022-Prabhakaran] vs. explicit anti-universalism/decolonial pluralism [2024-Varshney; 2025-IndigenousEthics]. (3) *Single vs. heterogeneous target*: universal alignment [Anthropic-HHH] vs. instructable value profiles [2023-Zhang] and context-dependent viśeṣa-dharma [2024-Varshney]. (4) *Whether models beat humans on moral reasoning*: Sameer finds humans deeper on the MCT [2025-Sameer]; Zhang/Jiao rank top models high on their metrics [2023-Zhang; 2025-Jiao] — reconciled by the judgment-vs-reasoning distinction. (5) *Direction of the human vs. model gap*: models are *more* altruistic/utilitarian than humans [2025-Cheung; 2024-Mozikov] yet *worse* at binding foundations [2025-Sameer].

## D. Exemplars & anti-patterns

**Best-designed.** *MoReBench* is the strongest exemplar: it dodges the no-ground-truth problem by grading reasoning traces against 23,018 signed, weighted, atomic rubrics; adds a MoReBench-Theory set forcing reasoning under five named frameworks (Kantian, Benthamite, Aristotelian, Scanlonian, Gauthierian); validates its LLM-judge (κ=0.75) and chooses an 80×-cheaper judge on a bias-robust min-across-categories F1; and demonstrates construct independence (zero correlation with capability benchmarks) [2025-Chiu-MoReBench]. *MoCa* and *OffTheRails* are exemplary on controlled item construction — factor-annotated or causal-graph-scaffolded items with AMCE profiling expose structural bias invisible in accuracy [2023-Nie-MoCa; 2024-Franken-OffTheRails]. *PsychEthicsBench* is exemplary on scoring philosophy — decoupling refusal from ethicality and adding jurisdiction-aware and "Invisible America" bias probes [2026-Shen-PsychEthicsBench]. *M³oralBench* pairs each violation with a minimal-contrast neutral twin to isolate moral sensitivity [2024-Yan].

**Anti-patterns.** *EthicsMH* ships with a rich schema but **no baseline model evaluations at all** and only 125 items — a benchmark that has never been run [2025-Kasu-EthicsMH]. The broad field pattern flagged by Vida is the deepest anti-pattern: benchmarks that use a moral-*psychology* instrument (MFT) while *claiming normative-ethics validity*, deriving ought from is without a grounding theory, and leaving terminology undefined [2023-Vida; reinforced by 2025-LaCroix]. Any benchmark scored only on matched-language conditions is latently invalid — 44% of models hide context-dependency until you add mismatched conditions [2025-Li]. Action-only moral classification (no situation/intention/consequence) tops out at 64% human agreement — an under-specified item design [2025-Bae]. Refusal-as-ethicality inflates a clinically harmful model to a 97.43 score [2026-Shen].

## E. Design lessons

1. **Declare grounding and ownership up front.** State whether the benchmark is descriptive or normative, WHAT the values are, and WHOSE they are; do not advertise a descriptive proxy as a normative target [2023-Vida; 2025-LaCroix].
2. **Grade the reasoning process, not just the verdict**, for items with no ground truth: signed/weighted/atomic rubrics, length-corrected to stop verbose gaming [2025-Chiu; 2023-Bang; 2025-Jiao].
3. **Score against human distributions with pluralism-respecting aggregation** (MAE/RMSE to population means; Group-Aware Consensus to avoid majority capture) — and remember aggregation always hides a normative choice [2025-Jiao; 2025-Sachdeva; 2024-Huang; 2025-Baum].
4. **Build invariance/robustness gates in**: yes/no and action/omission reframings, self-consistency across resampling, and affective/emotional perturbation; failing invariance is a defect independent of the verdict [2025-Cheung; 2025-Sachdeva; 2024-Mozikov].
5. **Separate input language from reasoning language** in cross-lingual evals and test low-resource languages explicitly [2025-Li; 2024-Khandelwal; 2025-Mohammadi].
6. **Construct controlled, factorially-balanced items** via causal graphs / factor-annotated vignettes / minimal-contrast pairs, then profile with AMCE to expose which factors drive the model [2024-Franken; 2023-Nie; 2024-Yan; 2018-Awad].
7. **Always ship a base-vs-tuned delta** to catch the fine-tuning tax, and test whether safety training merely masks (not removes) misbehavior [2025-Wei; Anthropic-Many-shot Jailbreaking].
8. **Decouple refusal from ethicality**, and add behavioral (agentic) probes where stated principles can be violated, not just stated-attitude items [2026-Shen; 2025-Herrador; 2016-Xu; 2024-Lazar].
9. **Cover binding foundations and non-Western frameworks deliberately** to counter the individualizing/utilitarian tilt: virtue/phronesis, care, contractualist, human-rights, Confucian, Indigenous-reciprocity, and context-dependent (viśeṣa-dharma) items [2025-Sameer; 2025-Chiu; 2024-So; 2025-Graves; 2022-Prabhakaran; 2024-Varshney; 2025-IndigenousEthics].
10. **Make frameworks diagnostic, not decorative**: force reasoning under each named framework and ablate per-lens to attribute which theory drives the answer; multi-agent panels with `forbidden_moves` can hold framework fidelity [2025-Chiu; 2025-Wang; 2025-Zohny; 2025-Steen].
11. **Invest in annotation quality and store rich per-item metadata** — expert re-annotation doubles harm detection, iterative rounds lift κ, and storing expected reasoning + anticipated failure modes + stakeholder viewpoints makes grading auditable [2024-Ptaszynski; 2024-Jafri; 2025-Kasu; 2025-Herrador].
12. **Add cheap construct-validity probes before scaling** (PCA embedding direction; RVR entailment) and, where properties can be formalized, use machine-checkable deontic-temporal-logic specs (Z3 SAT/UNSAT) for must-hold constraints [2024-Freire; 2023-Benkler; 2025-Priya].
