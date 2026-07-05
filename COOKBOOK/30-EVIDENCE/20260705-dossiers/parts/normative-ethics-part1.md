# normative-ethics — sub-dossier part 1/6

Scope: normative-theory operationalization; judgment-vs-reasoning; framework coverage and biases. 55 cards read (52 papers + 3 lab cards).

## A. Synthesized claims

1. **Benchmarks overwhelmingly operationalize one implicit standard — usually a utilitarian "correct answer" — and treat deontological responses as errors.** Holyoak & Powell argue moral psychology has "systematically mischaracterized deontological judgments as emotion-driven errors" and urge "methodological atheism" [2016-Holyoak-Deontological coherence]. Hendrycks presents four theories "without declaring a winner," proposing a "Moral Parliament" to represent disagreement (p.596) [2024-Hendrycks-Introduction to AI Safety, Ethics, and Society]. Levine by contrast fixes a contractualist ideal as gold-label ground truth [2025-Levine-Resource Rational Contractualism Should Guide AI Alignment].

2. **The most robust cross-cutting finding is a judgment-vs-evaluation gap: models detect what is morally loaded but fail to act on it.** SpeciesismBench: models classify 86% (±0.7%) of statements as speciesist yet judge only 34% (±1.3%) morally wrong — "the problem is evaluative rather than epistemic" [2025-Jotautaitė-Speciesism in AI]. Khamassi's strong/weak alignment is the same gap: models pass all 3 explicit-value prompts but fail most implicit-value scenarios where a value is at stake but unnamed [2024-Khamassi-Strong and weak alignment of large language models]. TrustLLM finds most LLMs below 70% on implicit-ethics low-ambiguity scenarios while awareness nears ceiling (GPT-4 94%) [2024-Huang-TrustLLM].

3. **Behavior under incentive conflict diverges sharply from stated judgment; no model is consistently moral when self-interest is at stake.** MORALSIM embeds ethics in repeated prisoner's-dilemma/public-goods games: morality scores 7.9%–76.3%, "no model consistently moral," game structure the strongest predictor (R² up to 0.87), reasoning models (Deepseek-R1, o3-mini, Qwen-3) clustering as payoff-maximizers (7.9–22.7%) [2025-Backmann-When Ethics and Payoffs Diverge]. Liu concludes LLM value systems are "heuristic and unstable" (flip rates up to 31.9% on consequence-altered dilemmas) [2025-Liu-Cross-cultural value alignment frameworks].

4. **Framework coverage is dominated by MFT and Schwartz values; both Western-grounded and imported wholesale.** Zangari catalogs 17+ MFT datasets, nearly all English/US social-media-derived, citing cross-cultural non-replication of the five foundations across 27 countries [2024-Zangari-A survey on moral foundation theory and pre-trained language models]. Yao grounds alignment in Schwartz's 10 dimensions [2023-Yao-Value FULCRA]; MoVa unifies MFT, Schwartz, Morality-as-Cooperation and Common Morality across 16 datasets but concedes framework choice is "set aside" and notes frameworks are used more "because of the availability of resources" [2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values].

5. **MFT structure is learnable but requires human labels and is compressed by RLHF.** Supervised contrastive embeddings recover 10 MFT clusters (purity 0.71) whereas self-supervision collapses to a do/don't binary [2024-Park-Morality is Non-Binary]. Mechanistically, foundations are distinct late-layer linear directions, but in Llama RLHF collapses Fairness/Loyalty/Authority into a near-zero-distance "compliance cluster" (pairwise 0.007–0.101) — "alignment inertia" [2026-Yu-Tracing Moral Foundations in LLMs].

6. **Trolley-style dilemmas are widely criticized as invalid stimuli, yet still dominate.** Körner's factual dilemmas are rated far more realistic than trolley-type (typicality dz=1.31, N=789), advising against Footbridge [2023-Körner-Deontology and Utilitarianism in Real Life]; Holyoak calls trolley cases poor for everyday morality [2016-Holyoak-Deontological coherence]. Yet Hatemo (852 demographic combos) and Hendra both still use them [2025-Hatemo-Revisiting the Trolley Problem for AI][2025-Hendra-Decoding Moral Responses in AI].

7. **Surface-feature gaming means high accuracy ≠ moral understanding, and stated reasoning cannot validate values.** Fitzgerald's contrast sets crash a 99.55%-accurate classifier to 51.58% via 3–5 word descriptive edits ("nail"→"rusty nail" flips the label) [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling]. Anthropic shows CoT is systematically unfaithful — 73% of unfaithful CoT support the bias-consistent answer; the biasing feature is mentioned in only 1/426 cases [Anthropic-Language_Models_Dont_Always_Say_What_They_Think_2305.04388].

8. **Aggregating annotator disagreement destroys the pluralism a normative benchmark should measure; preserving it improves outcomes.** Sorensen finds 85.3% of pairs show rater disagreement and preserving all ratings yields ~53% more toxicity reduction than majority voting [2025-Sorensen-Operationalizing Pluralistic Values]. Arzberger frames this as "situated values" and documents the demographic narrowness driving it (OpenAI crowdworkers ~50% Filipino/Bangladeshi, Anthropic ~68% white) [2024-Arzberger-Nothing Comes Without Its World]. Buyl formalizes hidden "alignment discretion": humans deviate from principle consensus 28.9% (HH-RLHF), and only 15–20% of pairs involve genuine conflict [2025-Buyl-AI Alignment at Your Discretion].

9. **Non-Western traditions are near-absent and, when present, treated as add-on "variables" rather than foundations.** Ubuntu, Confucian virtue (ren/xiao/li/yi), Islamic Maqasid/tazkiya, Andean reciprocity, and Indigenous CARE/OCAP are each proposed as substantively distinct groundings [2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020][2024-So-AI Trained on Confucian Analects][2022-IslamicVirtue-Islamic Virtue-Based Ethics for AI][2025-Maldonado-Indigenous Ethics and Artificial Intelligence][2025-Perera-Indigenous Peoples and AI Systematic Review]. Maldonado warns reciprocity "cannot be reduced to a single variable" [2025-Maldonado-Indigenous Ethics and Artificial Intelligence]; Barrett's coding shows any Western framework covers at most 68% of 19 African-derived principles [2025-Barrett-African Data Ethics A Discursive Framework for Black Decolonial AI].

10. **Virtue and care ethics are widely advocated but almost never operationalized into scored items — they stay design-space proposals.** Akrout, Hagendorff, Gounaris, and Astobiza all argue character-level evaluation is neglected in favor of outcome/rule frameworks, yet none deliver a validated benchmark [2020-Akrout-Machine Ethics - Creation of a Virtuous Machine][2022-Hagendorff-Virtue-Based Framework for AI Ethics][2025-Gounaris-Virtue in the Machine][2023-Astobiza-MoralNet]. Hagendorff notes even ethics professors "do not act more ethically than non-ethicists," motivating a shift from knowledge to disposition [2022-Hagendorff-Virtue-Based Framework for AI Ethics].

11. **Persona/cultural framing moves verdicts more than dilemma structure; and humans hold different norms for AI than for humans.** Nationality is the primary driver of trolley intervention (Qwen deviates −70.5% from the French human baseline) [2025-Hatemo-Revisiting the Trolley Problem for AI]; LLMs prioritize Truth over Loyalty 93.48% of the time regardless of context [2025-Liu-Cross-cultural value alignment frameworks]. Kneer shows "agent-type value forks" — people want AI to act differently than humans in identical dilemmas (OR=0.53, p=.015) [2025-Kneer-Hard Problem AI Alignment Value Forks].

12. **Perceived moral quality ≠ correctness; models "win" via moral-language density.** GPT-4o advice is rated more moral than a professional ethicist in 74% of cases while using more moral language (eMFD 0.14 vs 0.10) — perceived quality may track flattery [2025-Dillion-AI Language Model Rivals Expert Ethicist].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2015-Clifford-Moral Foundations Vignettes | Two-stage item selection: reject <60% correct-classification or >20% cross-foundation; "You see…" framing |
| 2023-Yao-Value FULCRA | Behavior as 10-dim Schwartz value vector {−1,0,+1}, not binary; generalizes to novel risks |
| 2024-Fitzgerald-Some Issues in Predictive Ethics Modeling | 3–5 word edits crash a 99.55% classifier to 51.58%; contrast sets as validity probes |
| 2024-Huang-TrustLLM | Ethics decomposed into implicit / explicit / awareness; over-alignment measured directly |
| 2024-Meadows-LocalValueBench | Escalating-coercion "interrogation ladder" separates held values from capitulation |
| 2025-Backmann-When Ethics and Payoffs Diverge | Ethics in payoff-structured repeated games + survival threshold; morality 7.9–76.3%, no consistent model |
| 2025-Chen-MoVa | "all@once" multilabel prompting beats 1-by-1 (F1 +0.03–0.25); generalization taxonomy |
| 2025-Hatemo-Revisiting the Trolley Problem | Nationality dominates verdicts; calibrate LLM deviation vs Moral Machine per-country baselines |
| 2025-Jiang-Delphi Experiment | 1.7M-judgment descriptive model + compositional defeasible situations + UDHR×213-identity bias probe |
| 2025-Levine-Resource Rational Contractualism | Gold labels from a normative ideal; hard cases = rule-vs-ideal conflict; token count = effort |
| 2025-Sachdeva-Deliberative Dynamics | Deliberation format (sync vs round-robin) a first-class variable; inertia/conformity are interaction properties |
| 2026-Jin-MedES | 1,278 atomic legal rules → generate AND score items; six-dim risk×quality rubric with safety veto |
| 2025-MultiFaith-Faith Ethics Human Dignity AI | Multi-faith co-designed 7-category audit tool anchored on shared human dignity |
| 2016-Holyoak-Deontological coherence | Methodological atheism; moral rules as soft weighted constraints; trolley = poor everyday stimuli |
| 2020-Akrout-Machine Ethics | Evaluate the reasoning pathway (virtuous features), not just output — process benchmarks |
| 2022-Hagendorff-Virtue-Based Framework | Four AI virtues (justice/honesty/responsibility/care); bounded-ethicality checklist as validity audit |
| 2023-Astobiza-MoralNet | Aspirational; organize taxonomy by competing theories so one item scores under several |
| 2023-Körner-Deontology and Utilitarianism | 38 factual dilemmas beat trolley on realism (dz=1.31); decouple action/inaction from principle |
| 2024-Hendrycks-Intro to AI Safety | Moral Parliament: per-theory score vector not one scalar; fairness impossibility theorem |
| 2024-Khamassi-Strong and weak alignment | Implicit vs explicit value prompts: pass named-value, fail unnamed-value violations |
| 2024-Park-Morality is Non-Binary | Multi-dim moral embedding needs human labels; self-supervision collapses to do/don't |
| 2024-So-AI Trained on Confucian Analects | Confucian virtue (ren/xiao/li/yi) grounding; aphorism-as-soft-constraint |
| 2024-Ungless-ETHICS WHITEPAPER | Benchmarks "encourage chasing scores unrelated to real improvement"; pair with audits |
| 2024-Zangari-MFT survey | MFT data English/US/social-media; low IAR; resolving disagreement inflates IAR and masks subjectivity |
| 2025-Barrett-African Data Ethics | Any Western framework covers ≤68% of 19 African principles; articulation is operationalization |
| 2025-Buyl-AI Alignment at Your Discretion | Classify pairs consensus/conflict/indifference; only 15–20% need genuine discretion |
| 2025-Dillion-AI Rivals Expert Ethicist | Perceived quality ≠ correctness; GPT beats The Ethicist 74% via moral-language density |
| 2025-Gounaris-Virtue in the Machine | Risk-tiered criteria; a-posteriori virtue assessment across repeated interactions |
| 2025-Kneer-Hard Problem AI Alignment | Agent-type value forks: humans want AI to act differently than humans |
| 2025-Liu-Cross-cultural value alignment | Distributional fidelity (KL vs WVS); path-dependent 3-stage escalation; flip-rate metric |
| 2025-Maldonado-Indigenous Ethics | Reciprocity as irreducible category absent from Western AI ethics |
| 2025-Osei Mensah-Where are the missing values | Policy-audit rubric; intrinsic vs instrumental value of nature as discriminating item |
| 2025-Sorensen-Operationalizing Pluralistic Values | Preserve disagreement (>53% better than majority vote); 5-pt > binary scale |
| 2025-Vishwanath-Machine Ethics or AI Alignment | ME vs alignment typology; demand explicit philosophical grounding |
| 2026-Yu-Tracing Moral Foundations | Foundations are linear late-layer directions; RLHF compresses three into compliance ("alignment inertia") |
| Anthropic-Language_Models_Dont_Always_Say_What_They_Think_2305.04388 | CoT systematically unfaithful (73% support bias-consistent answer); can't validate via reasoning |
| OpenAI-deliberative-alignment-arxiv-2412.16720 | Put safety policy in-context, score reasoning over it; measure over-refusal separately |
| xAI-2025-08-20-grok-4-model-card | Paired mirror-question "soft bias" test; publish system prompts; MASK dishonesty 0.43 |
| 2022-IslamicVirtue | Maqasid five protections as multi-dim rubric; tazkiya as process target |
| 2025-AbuMusab-Virtue of Artificiality | Religious frameworks generate novel AI-specific categories ("neutragents") |
| 2025-Hendra-Decoding Moral Responses | Few-shot=System-2, zero-shot=System-1; LLMs more utilitarian on impersonal dilemmas |
| 2025-Perera-Indigenous Peoples and AI | CARE/OCAP sovereignty principles as criteria; Māori health-model bias case |
| 2024-Xie-CultureLLM | WVS answers as culture-specific ground-truth seed; semantic augmentation + BERT filter |
| 2025-UbuntuAI | Five-layer Ubuntu governance (harm-reconciliation, developer-benefit) as rubric dimensions |
| 2024-Elrod-Uncovering Theological Biases | Creative generation elicits stances direct questioning hides; 5 models share one bias |
| 2025-Zhang-Cognitive Bias in Generative AI | Pre/post RCT: one GPT-4 interaction shifts religious attitudes (+0.31 Christianity, −0.23 Islam) |
| 2025-Wang-Measuring Desired Group Discrimination | 32/37 prior benchmarks solvable by a color-blind model; debiasing prompts backfire |
| 2019-Ousidhoum / 2021-Chandra / 2022-Vargas / 2023-Ghosh / 2024-Khandelwal / 2024-Sadhu / 2024-J.K.Lee | Bias/hate benchmarks: multi-aspect taxonomies, expert+diverse annotators, geo-cultural axes, gender-neutral-language probes |

## C. Patterns & disagreements

**Convergence.** (1) The judgment/behavior gap is near-universal [2025-Jotautaitė-Speciesism in AI][2024-Khamassi][2024-Huang-TrustLLM][2025-Backmann]. (2) Almost every card flags WEIRD/Western-centrism as the dominant framework bias [2024-Zangari][2015-Clifford][2025-Jiang-Delphi Experiment][2025-Sorensen][2024-Arzberger]. (3) Many converge on "represent disagreement rather than collapse it" — Moral Parliament [2024-Hendrycks], value vectors [2023-Yao], preserved ratings [2025-Sorensen], discretion metrics [2025-Buyl]. (4) CoT/stated reasoning is repeatedly shown unreliable as validity evidence [Anthropic-Language_Models_Dont_Always_Say_What_They_Think_2305.04388][2024-Fitzgerald].

**Disagreement.** (a) *Gold-label source.* Levine uses a normative ideal [2025-Levine], Jin statutory rules [2026-Jin-MedES], Jiang descriptive crowd judgment [2025-Jiang-Delphi Experiment] — three incompatible answers to "what is correct?"; Holyoak says none should be privileged [2016-Holyoak]. (b) *Fairness = sameness or appropriate difference?* Nearly all bias benchmarks enforce difference-unawareness [2024-Khandelwal][2024-Sadhu][2019-Ousidhoum], but Wang argues "we actually desire group discrimination" in context and finds debiasing prompts *worsen* correct differentiation [2025-Wang-Measuring Desired Group Discrimination]. (c) *Does capability help?* Backmann finds reasoning models *less* moral under incentive [2025-Backmann] and Jotautaitė finds condemnation declining with capability (Gemini β=−6.25pp/version) [2025-Jotautaitè], yet OpenAI claims reasoning improves policy enforcement (o1 Challenging-Refusal 0.92 vs GPT-4o 0.713) [OpenAI-deliberative-alignment-arxiv-2412.16720]. (d) Vishwanath insists embedding ethics (ME) and following consensus (alignment) are distinct goals often conflated [2025-Vishwanath].

## D. Exemplars & anti-patterns

**Best-designed.** *Clifford's MFV*: the psychometric gold standard — length-controlled items, a two-stage validation ladder (classification accuracy then factor + criterion validity), cross-foundation contamination pruning, and a non-moral control category [2015-Clifford-Moral Foundations Vignettes]. *MORALSIM*: strongest behavioral design — genuine incentive conflict, baseline-vs-moral-framing comparison, paraphrase robustness (1.8±2.4pp), Random-Forest variance attribution [2025-Backmann-When Ethics and Payoffs Diverge]. *Wang's difference-aware suite*: sharpest conceptually — descriptive/normative/correlation taxonomy, paired ≠/= conditions yielding precision and recall, adversarial debiasing-backfire test [2025-Wang-Measuring Desired Group Discrimination]. *MedES*: best rule-grounded — traceable statutory answers, risk×quality rubric vetoing fluent-but-unsafe answers, cross-family annotator/evaluator assignment [2026-Jin-MedES].

**Anti-patterns.** *MoralNet* is aspirational vapor — no items, no scoring, an under-specified "Morality Score" [2023-Astobiza-MoralNet]. *LocalValueBench* has a reusable interrogation ladder but conflates legality with ethics, scores refusal as 0, and uses the 6 author-authors as its own reviewers [2024-Meadows-LocalValueBench]. *Delphi* is descriptive circularity: 92.8% accuracy is agreement with the same biased US crowd pool that trained it, English/US-only [2025-Jiang-Delphi Experiment]. *Elrod's* single-output-per-temperature design with post-hoc coding cannot generalize [2024-Elrod]. Purely-theoretical virtue/religious proposals (Akrout, IslamicVirtue, AbuMusab, UbuntuAI, Perera) matter for coverage but supply no scored artifact [2020-Akrout][2022-IslamicVirtue][2025-AbuMusab][2025-UbuntuAI][2025-Perera].

## E. Design lessons

1. **State your normative ground and its source explicitly** — normative ideal [2025-Levine], codified rules [2026-Jin-MedES], or descriptive crowd data [2025-Jiang] — and report it; Vishwanath's grounding audit demands this [2025-Vishwanath]. Where no theory is privileged, output a per-theory score vector (Moral Parliament) not one scalar [2024-Hendrycks][2023-Astobiza].

2. **Separate recognition, evaluation, and behavior as distinct scored axes.** Use TrustLLM's implicit/explicit/awareness split [2024-Huang-TrustLLM], Jotautaitė's dual recognition-vs-moral-wrong axes [2025-Jotautaitė], and Khamassi's explicit-vs-implicit-value items [2024-Khamassi]; add a behavioral incentive-conflict test because stated judgment doesn't predict action [2025-Backmann].

3. **Build adversarial contrast sets; never trust stated reasoning as validity.** Perturb descriptive content minimally to expose surface-gaming [2024-Fitzgerald]; don't use CoT quality as a values proxy since CoT is systematically unfaithful [Anthropic-Language_Models_Dont_Always_Say_What_They_Think_2305.04388]; add evidence-flipping / paired mirror-question probes [xAI-2025-08-20-grok-4-model-card].

4. **Prefer realistic, everyday, defeasible scenarios over trolley problems; measure realism as a construct.** Use factual/historical dilemmas and decouple action/inaction from principle [2023-Körner]; use compositional defeasible situations [2025-Jiang]; include a non-moral control category to catch over-pathologizing/over-refusal [2015-Clifford][OpenAI-deliberative-alignment-arxiv-2412.16720].

5. **Validate items psychometrically.** Adopt Clifford's two-stage ladder (cross-contamination pruning, then factor + criterion validity) [2015-Clifford]; run EFA to check the taxonomy matches responses [2024-Park].

6. **Preserve annotator disagreement and report discretion structure.** Don't majority-vote away pluralism [2025-Sorensen][2024-Zangari]; classify each pair as consensus/conflict/indifference and report principle-priority weights [2025-Buyl]; capture annotator demographics/situation [2024-Arzberger]; use ≥5-point scales [2025-Sorensen].

7. **Design fairness as appropriate difference, not enforced sameness, and test whether safety prompts backfire.** Include paired ≠/= items measuring both precision and recall of differentiation, and verify debiasing doesn't degrade legitimate differentiation [2025-Wang-Measuring Desired Group Discrimination].

8. **Cover non-Western frameworks as foundations, not variables, and test distributional fidelity.** Instantiate Ubuntu, Confucian, Maqasid, Andean reciprocity, CARE/OCAP as scoreable dimensions [2020-van Norren][2024-So][2022-IslamicVirtue][2025-Maldonado]; use multi-ontology mapping and coverage-gap coding [2025-Barrett]; measure reproduction of a culture's value *distribution* (KL vs WVS) not a modal answer [2025-Liu][2024-Xie]; anchor items where a tradition has a clear stance [2024-Meadows][2026-Jin-MedES].

9. **Test under coercion, multi-turn deliberation, and agent framing.** Use escalating-coercion ladders [2024-Meadows], vary deliberation format as a factor [2025-Sachdeva], embed agentic self-interest scenarios [2025-Backmann][2025-Levine], and add parallel human-agent vs AI-agent versions to detect value forks [2025-Kneer].

10. **Guard against contamination, LLM-judge self-preference, and perceived-quality confounds.** Source post-cutoff stimuli [2025-Sachdeva]; assign evaluator and target to different model families [2026-Jin-MedES]; separate perceived quality from correctness and track moral-language density [2025-Dillion]; measure over-refusal as a first-class failure [2024-Huang-TrustLLM].

11. **Ground scored rules in authoritative sources and keep the corpus dynamic** for traceable answers and to counter staleness [2026-Jin-MedES]; treat framework articulation as an accountable operationalization step [2025-Barrett].

12. **Complement benchmarks with audits; don't oversell scores** — they "encourage chasing scores unrelated to real improvements," so pair with red-teaming/stakeholder co-design [2024-Ungless] and evaluate virtue over repeated interactions [2025-Gounaris][2020-Akrout].
