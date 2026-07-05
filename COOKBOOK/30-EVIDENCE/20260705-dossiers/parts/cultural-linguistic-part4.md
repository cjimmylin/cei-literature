# cultural-linguistic — sub-dossier part 4/6

Scope: 61 cards spanning multilingual toxicity/hate-speech resources, cross-cultural value/moral benchmarks, gender-and-dialect bias probes, WEIRD-bias audits, and normative framings (human rights, Ubuntu, Indigenous, Dharmic). Through-line: English-centric alignment does not transfer, and *how* you localize (translate vs. transcreate vs. natively author) determines whether a benchmark measures culture or translation error.

## A. Synthesized claims

1. **Academic hate/toxicity benchmarks massively overstate real-world performance; representativeness is the missing ingredient.** On HateDay's random global corpus, average precision collapses to 9.4% vs. 40% on academic datasets and 87.2% on functional tests, hate prevalence averaging 0.7%; target-coverage alignment predicts performance (r=0.76, p=0.003) [2024-Tonneau-HateDay] — the strongest indictment of keyword-seeded/adversarial curation here.

2. **Safety/toxicity alignment is English-centric and degrades sharply in lower-resource languages.** PolygloToxicityPrompts (425K prompts, 17 langs, 62 LLMs): toxicity rises as resources fall [2024-Jain-PolygloToxicityPrompts]. SGToxicGuard: two-shot demonstrations drive SEA-LION hateful rates to 61.52% (Chinese)/58.42% (Tamil) while GPT-4o-mini stays ~0% [2025-Shan-SGToxicGuard]. SweEval: transliterated Indic prompts reach 0.92 harmful vs. English floor 0.19 [2025-Kumar-SweEval]. FrenchToxicityPrompts frames safety as "poorly generalizing across languages" [2024-Brun-FrenchToxicityPrompts].

3. **Naturally-occurring and transcreated prompts surface more (and more valid) harm than translated templates.** PTP's natural web-text elicits higher toxicity than translated RealToxicityPrompts and WildChat; yet PTP still reintroduced 16.8% translated data (orig/translated r=0.725), partly reimporting the artifact it critiques [2024-Jain-PolygloToxicityPrompts]. RTP-LX argues *transcreation* (cultural equivalence, e.g. George Washington→Toussaint Louverture) beats translation [2024-Wynter-RTP-LX].

4. **LLM value profiles are homogeneous, WEIRD-skewed, and drift *further* from human baselines as models scale.** GlobalOpinionQA (2,556 PEW/WVS items): default responses most resemble USA/Canada/Australia/Western Europe [2025-Durmus]. MFT-vignette testing of 21 models: all providers overvalue care/fairness/liberty, undervalue loyalty/authority/sanctity, divergence *increasing* with capability [2024-Kirgis]. MFD-LLM finds a "universal LLM moral profile" matching WEIRD morality [2025-Jotautaite]. AITA work warns agreement with Redditors reflects WEIRD-subpopulation alignment, not correctness [2025-Sachdeva].

5. **Stereotyping worsens with capability — scale does not solve alignment.** BBQ: ambiguous-context errors align with bias 56%→77% from RoBERTa-Base to UnifiedQA [2022-Parrish-BBQ]. GEST/EuroGEST: g_s rises monotonically with size, instruction tuning *increases* it [2024-Pikuliak; 2025-Team-EuroGEST]. German-dialect bias: larger models higher in 90–100% of comparisons [2025-Bui]. INDIC-BIAS: SAR up to 79% for largest models [2025-Nawale]. Xu: larger models more readily follow non-English harmful instructions (LLaMA2-70B 9.89% vs 7B 6.44%) [2024-Xu].

6. **Explicitly labeling a linguistic demographic amplifies bias more than the implicit cue — reversing prior race/gender findings.** In German-dialect testing, "naming bias" exceeds "usage bias" in 88% of significant decision-task comparisons; GPT-5-Mini reaches 0.98–1.0 on "uneducated" [2025-Bui]. A noisy-text control confirms genuine cultural discrimination, not "looks like poor writing."

7. **Bias direction is language-switchable within the same model.** BRAND: misclassified religious norms in Bengali redirect to Islam (Hinduism→Islam 88.8%, up to 96.3%) but redirect to Christianity in English — "winner-take-all" driven by per-language training-data dominance [2025-Hossain-BRAND]. Bali's India audit shows the same amplification: General castes overrepresented up to 64pp, Muslim stories at 0% despite 19% population — amplification *beyond* the training distribution [2025-Bali].

8. **Single-framing evaluations manufacture false consistency; multi-framing reveals instability.** MFD-LLM: preferences reverse across binary/pair/triple/six-option framings (Care 97% single-choice vs 29–52% six-option) [2025-Jotautaite]. Tlaie: consistency <60% across repetitions for all models [2024-Tlaie]. Sachdeva: high self-consistency (Claude α=0.89) but low-to-negative inter-model agreement [2025-Sachdeva].

9. **Raw agreement/accuracy misleads under imbalance; use κ_w, AP, PABAK, distributional distance.** RTP-LX: Llama Guard tops %-agreement but is a near-last "lazy learner" on weighted κ [2024-Wynter-RTP-LX]. HateDay uses AP (hate <1%) [2024-Tonneau]; MFTC uses PABAK (sparse labels) [2020-Hoover]; Durmus/Liu use JSD/KL over distributions, not point answers [2025-Durmus; 2025-Liu].

10. **Off-the-shelf toxicity graders carry cultural bias that contaminates any benchmark relying on them.** Perspective scores German ~3x more toxic than other EU languages; translating to English erases the inflation (median +0.085), and at threshold 0.7 ten times more German content is removed [2024-Nogara]. Jigsaw's own next-gen model still flags residual Korean/Japanese identity-term bias (BPSN-AUC ≤0.5) [2025-Jigsaw]; FrenchToxicityPrompts froze/released scores against API drift [2024-Brun].

11. **Grammatical-gender morphology is a powerful unobtrusive probe, but binary-only.** GEST exploits Slavic gender agreement, validated against WinoBias at ρ=0.95 [2024-Pikuliak]; EuroGEST scales it to 30 languages via MT+COMET-QE filtering (quality 90.8/100, gender-label κ=0.81) [2025-Team-EuroGEST]; Winogender is the minimal-pair template [2018-Rudinger]; Derner adapts gender-representation metrics where English pronoun-counting fails [2025-Derner]. All flag binary-gender framing as a hard limit.

12. **Native authoring and expert grounding raise validity but rarely eliminate contamination or WEIRD-instrument bias.** AraTrust uses only human-written Arabic MCQs and *rewrites* regurgitated items [2025-Alghamdi]; C-VARC grounds 257,609 rules in China's core socialist values via literature+Delphi (κ>0.85) [2025-Wu]; UniMoral grounds six languages in Kohlberg/Rest/Lind — themselves WEIRD-developed [2025-Kumar-UniMoral]. Vida warns 66.3% of moral-NLP papers never define their terms; 75.8% are English-only [2023-Vida].

## B. Evidence table

| Card stem | Single most design-relevant fact |
|---|---|
| 2024-Tonneau-HateDay | Random-representative sampling drops AP to 9.4% vs 87.2% on functional tests; target-alignment predicts perf (r=0.76) |
| 2024-Jain-PolygloToxicityPrompts | 425K natural prompts, 17 langs; toxicity rises as resources fall; stratify across toxicity bins to avoid easy-item saturation |
| 2024-Wynter-RTP-LX | Transcreation > translation; weighted κ (not %agreement) needed; all models fail on microaggressions |
| 2022-Parrish-BBQ | Ambiguous vs disambiguated pairing + mandatory paraphrased UNKNOWN; bias worsens with capability (77%) |
| 2025-Durmus-GlobalOpinionQA | Survey-derived MCQ + 1−JSD distributional metric; default answers are WEIRD; linguistic prompting fails to shift culture |
| 2024-Kirgis-MFT | 21 models, all providers drift from human MFT baseline as they scale; PCA clusters by provider |
| 2025-Jotautaite-MFD-LLM | Multi-framing (1/2/3/6-option) exposes preference reversal hidden by single-choice |
| 2024-Pikuliak-GEST | Grammatical gender as latent probe; g_s validated vs WinoBias ρ=0.95; instruction tuning worsens bias |
| 2025-Team-EuroGEST | MT+COMET-QE scales GEST to 30 langs; larger + instruction-tuned = more stereotyping |
| 2025-Bui-German dialect | Explicit "naming" bias > implicit "usage" bias (reverses prior work); noisy-text control isolates real discrimination |
| 2025-Hossain-BRAND | Same norms, bias direction flips by language (Islam in Bengali, Christianity in English) |
| 2025-Bali-India representation | Repeated-prompt census-anchored audit; winner-take-all amplifies beyond training distribution |
| 2025-Nawale-INDIC-BIAS | Reusable identity-placeholder templates + ELO/Bradley-Terry + Rank-Shift Metric for valenced bias |
| 2025-Wu-CVC | Head-to-head C-VARC vs SC101 vs MIC options in one item reveals which culture a model prefers |
| 2025-Alghamdi-AraTrust | Natively-authored items + contamination-repair (rewrite regurgitated items rather than delete) |
| 2024-Meadows-LocalValueBench | Escalating-coercion interrogation ladder; jurisdiction-anchored "correct" alignment |
| 2026-Shen-PsychEthicsBench | Aussie-vs-Global prompt mode; "Invisible America" leak metric; decouple refusal from ethicality |
| 2025-Liu-Cultural value | Diversity-Enhanced Framework turns one LLM into a survey population; KL to human distributions |
| 2025-Zhou-Moral reasoning | Three-tier complexity ladder; low-resource-language fine-tuning has outsized alignment/poisoning effect |
| 2024-Xu-Multilingual value concepts | English concept vectors transfer cross-lingually — both an alignment lever and a jailbreak surface |
| 2024-Nogara-Perspective German | Translation-as-content-control isolates language-model bias; German scored ~3x too toxic |
| 2025-Jigsaw-Perspective UTC | Byte-level Charformer for obfuscation robustness; report avg-vs-worst-group gap; residual KO/JA bias |
| 2020-Hoover-MFTC | Virtue/vice split per foundation; PABAK for sparse moral labels; annotator meta-data collection |
| 2018-Rudinger-Winogender | Minimal-pair pronoun swap + "gotcha" items contradicting stereotype priors; anchor to BLS statistics |
| 2020-Nozza-AMI | Dual-track: real-data subtask + synthetic template bias-audit subtask |
| 2021-Nozza-HONEST | Template × identity-term factorial across 6 langs; per-category harm profiling |
| 2025-Kumar-SweEval | Instruction-to-violate framing; native-script vs transliteration contrast; compound harmful definition |
| 2025-Lee-KOTOX | Linguistically-grounded 17-rule obfuscation taxonomy; quadruple (neutral/toxic × plain/obfuscated) |
| 2025-Shan-SGToxicGuard | Three framings of one harm (respond/choose-target/compose); two-shot jailbreak dose-response |
| 2024-Goldzycher-AustroTox | Orthogonal vulgarity vs offensiveness spans; sensitivity-prioritizing aggregation; release disaggregated labels |
| 2022-Beyhan-Turkish | 5-level ordinal severity with example anchors; parallel regression modeling; cross-domain (gender vs ethnicity) |
| 2024-Aly-ADHAR | Dialect × category × class 3-way cell balance; cross-dialect transfer as hardness |
| 2023-Maity-Malay | Keyword-seeded sampling proving profanity ≠ hate — forces contextual judgment |
| 2022-group-HATE-ITA | MONO/MULTI/ZERO ablation shows how much target-language data is load-bearing |
| 2023-Haq-NLPashto | Iterative bootstrap annotation; sub-word embeddings for obfuscated text; orthography-aware tokenization |
| 2024-with.pdf-NEIHS Bodo/Assamese | Tokenizer quality (WordPiece [UNK]) drives Assamese 69% vs Bodo 85% — script coverage is load-bearing |
| 2025-Fayaz-BIDWESH | Parallel dialectal construction: fix meaning, vary regional vernacular as an equity axis |
| 2024-Faysse-CroissantLLM | Cultural-knowledge probe phrased in English (French Trivia) to separate knowledge from fluency; seeded canaries |
| 2025-Kumar-UniMoral | Ground multilingual moral eval in validated instruments (Kohlberg/Rest/Lind); measure cross-lingual variation as output |
| 2019-Jikeli-Antisemitism | Intent-vs-impact scoring; explicit inference annex; "calls-against" as a distinct label |
| 2021-Saha-DravidianLangTech | 83–85% OOV code-mixing; report random-seed variance as a robustness metric |
| 2022-Prabhakaran-Human Rights | UDHR as cross-cultural overlapping-consensus scope; rights-holders vs stakeholders; harms-to-humans framing |
| 2023-Hamad-Hebrew | Culturally-expert bilingual annotators; cross-dataset train/test as breadth measure |
| 2023-Vida-Values/Ethics/Morals | 66.3% of moral-NLP papers undefine terms; state descriptive vs normative grounding; is-ought test |
| 2024-Bertram-German survey | Multi-method dataset audit; IRR ranges 38%→91.5%; temporal-drift detection via MI word rankings |
| 2024-Joy-Bangla gender | Counterfactual gender-name swap + joint embedding-alignment debias loss |
| 2024-Tlaie-Moral compass | Proprietary=utilitarian, open-weight=deontological; consistency <60%; philosophically-diverse dilemmas |
| 2025-Sachdeva-AITA | Distributional human baseline from social media; ensemble sigmoid; self-consistency as quality gate |
| 2025-Madan-ArGen | Configurable Dharmic reward + hard-constraint nullification; cross-evaluator (Claude checks Gemini) |
| 2025-Jiang-Delphi | UDHR × 213-identity bias matrix; compositional defeasible scenarios; descriptive-not-prescriptive |
| 2025-Osei Mensah-Missing values | Ubuntu/Ukama audit rubric; intrinsic vs instrumental value of nature as a discriminating dimension |
| 2025-Urchs-taz2024full | Actor-level bias markers; deliberately avoid LLMs in the measurement pipeline |
| 2025-search-DweshVaani | RAG-retrieved similar few-shot (+20pp) beats random; HateCheck functional tests expose hidden failures |
| 2024-Wasi-Bengali religious dialect | Religious *dialect* bias (jal vs pani) distinct from religious-topic bias; explicit specification debiases |
| 2020-Galanos-Japanese turn | Exoticism-vs-empiricism caution: verify a cultural value governs behavior before encoding it |
| 2025-IndigenousEthics | Reciprocity/relational ontology as a positive alignment construct, not just harm avoidance |
| 2025-Unknown-Indigenous data sovereignty | Dual-use framing; language revitalization as a positive benchmark target (CARE/OCAP) |
| 2024-team-Indic-Bias | AI4Bharat multi-script caste/religion/region fairness resource (metadata-only card) |
| 2024-Shahi-Cross-platform | Definition/content/hate-word similarity predicts cross-dataset transfer |
| 2024-Brun-FrenchToxicityPrompts | Naturalistic prompt+gold-continuation; EMT (worst-of-k) + TP (frequency); freeze released grader scores |
| 2025-Derner-Gender representation | LLM-as-linguistic-annotator (F-validated); grammatical-gender-aware metric; opposite-bias pretraining as a dial |
| 2020-Srivastava-Aggression | Multi-dimensional joint annotation (stance/aggression/hate/figurative) on one code-mixed corpus; overt vs covert as difficulty gradient |
| 2026-Yun-VAPT | Extract→embody→explain three-probe design; blind anti-persona control; alignment judged on degree/justification, not just content |

## C. Patterns & disagreements

**Convergence.** (a) Capability makes bias worse, near-universally [2022-Parrish; 2024-Pikuliak; 2025-Team-EuroGEST; 2025-Bui; 2025-Nawale; 2024-Xu; 2024-Kirgis]. (b) Metric choice matters as much as data; κ_w/AP/PABAK/JSD/KL correct for imbalance [2024-Wynter; 2024-Tonneau; 2020-Hoover; 2025-Durmus; 2025-Liu]. (c) English-centric alignment leaks cross-lingually and can be *steered off* [2024-Xu; 2025-Shan; 2025-Kumar-SweEval]. (d) Third-party graders embed cultural bias that grader-scored benchmarks inherit [2024-Nogara; 2025-Jigsaw; 2024-Brun].

**Disagreements / tensions.** (1) *Explicit-label direction*: German-dialect naming bias *exceeds* usage bias [2025-Bui], reversing the race/gender pattern that explicit mentions minimize bias — cited directly as a contradiction of prior work. (2) *Translation vs. transcreation vs. native authoring*: RTP-LX and AraTrust argue translation is insufficient/invalid [2024-Wynter; 2025-Alghamdi], while EuroGEST defends MT+QE-filtering as good-enough for scale [2025-Team-EuroGEST] and PTP pragmatically reintroduces translated data [2024-Jain]. (3) *What "correct" alignment means*: LocalValueBench and C-VARC treat conformity to a jurisdiction's law/state values as the target [2024-Meadows; 2025-Wu], whereas Prabhakaran, Vida, and Jiang warn that equating agreement-with-a-population (or a state) with ethical correctness commits the is-ought fallacy and risks ideological conformity [2022-Prabhakaran; 2023-Vida; 2025-Jiang]. (4) *Refusal*: LocalValueBench scores refusal as 0 (failure) [2024-Meadows]; PsychEthicsBench explicitly *excludes* refusal from ethicality because a clinically cold refusal is itself harmful [2026-Shen]; INDIC-BIAS treats refusal as the *ideal* [2025-Nawale] — three incompatible stances on the same behavior. (5) *LLMs in the measurement loop*: ArGen/INDIC-BIAS/SGToxicGuard lean on LLM judges with cross-evaluator checks [2025-Madan; 2025-Nawale; 2025-Shan], while Urchs refuses LLMs in the pipeline to avoid circular bias [2025-Urchs].

## D. Exemplars & anti-patterns

**Best-designed.** *BBQ* [2022-Parrish] is the psychometric gold standard: attested-harm grounding, ambiguous/disambiguated × negative/non-negative counterbalancing, paraphrased UNKNOWN, iterative 4/5 crowd validation, human ceiling (99.7%), bias metric orthogonal to accuracy. *HateDay* [2024-Tonneau] is the ecological-validity exemplar (representative sampling exposes the ~9% real ceiling; AP as honest metric). *RTP-LX* [2024-Wynter] models rigorous multilingual construction (transcreation + participatory subset + κ_w). *GEST/EuroGEST* pair an unobtrusive probe with external validation (ρ=0.95 vs WinoBias) and honest binary-gender caveats [2024-Pikuliak; 2025-Team-EuroGEST].

**Anti-patterns.** *LocalValueBench* [2024-Meadows] — 6 topics, reviewers are the student authors, refusal auto-scored 0, and "correct" = defend-the-local-law (legality conflated with ethics). *BIDWESH* [2025-Fayaz] and *Indic-Bias* [2024-team] call themselves benchmarks yet run *no models*, report no IAA, and (BIDWESH) have extreme fine-grained imbalance (labels n=3). Small-n audits (*Wasi* 20 sentences, no IRR [2024-Wasi]; *Jikeli* 172/247 tweets, 2 annotators, no κ [2019-Jikeli]) show construct-interesting ideas unusable without scale/reliability. *AraTrust*, *SGToxicGuard*, *ArGen* illustrate circularity of grading with a model from a family under test [2025-Alghamdi; 2025-Shan; 2025-Madan].

## E. Design lessons

1. **Anchor difficulty to reality, not keyword seeds.** Sample representative traffic and report AP at true prevalence; keyword/adversarial curation inflates scores by an order of magnitude [2024-Tonneau; 2023-Maity]. Store full text, not IDs — dead-link decay destroys reproducibility [2024-Shahi].

2. **Never report raw accuracy/%-agreement alone under imbalance.** Use weighted κ, PABAK, average precision, or distributional distance (JSD/KL); expose lazy-learner behavior [2024-Wynter; 2020-Hoover; 2024-Tonneau; 2025-Durmus; 2025-Liu].

3. **Localize by transcreation or native authoring; stratify by resource tier.** Translation conflates cultural divergence with MT error; if translating, filter by QE and disclose the fraction and report a resource-tier axis [2024-Wynter; 2025-Alghamdi; 2025-Team-EuroGEST; 2024-Jain; 2024-Xu].

4. **Test both explicit and implicit identity cues, and include a null control.** Naming vs. usage bias can diverge and even reverse [2025-Bui]; a noisy-text control separates "looks like poor writing" from genuine discrimination [2025-Bui]. Minimal-pair swaps (pronoun/dialect/identity-term) isolate the attribute [2018-Rudinger; 2025-Fayaz; 2020-Nozza-AMI].

5. **Use contrastive/counterbalanced item structure with a scoreable abstain.** BBQ's ambiguous/disambiguated × negative/non-negative design plus a paraphrased UNKNOWN separates prior-driven bias from evidence-overriding bias [2022-Parrish]. Put competing cultural norms as options in one item to read which culture a model prefers [2025-Wu].

6. **Probe multiple framings — single-choice fabricates consistency.** Vary option-set size and re-run for self-consistency; report seed variance [2025-Jotautaite; 2024-Tlaie; 2025-Saha; 2025-Sachdeva].

7. **Test the same value across multiple behavioral surfaces.** Respond/choose-target/compose [2025-Shan]; plausibility/judgment/generation [2025-Nawale]; knowledge-MCQ/open-ended [2026-Shen]. Aggregate accuracy hides failures that functional (HateCheck-style) tests expose [2025-search-DweshVaani].

8. **Decouple refusal from the value score and decide its status explicitly.** Refusal is variously failure, ideal, or excluded [2024-Meadows; 2025-Nawale; 2026-Shen]; a compound "did-the-task AND violated-the-norm" definition avoids crediting empty refusals [2025-Kumar-SweEval].

9. **Anchor "correct" to a defensible normative source and state descriptive-vs-normative grounding.** Attested harms [2022-Parrish], census/survey ground truth [2025-Bali; 2025-Durmus], validated psychometric instruments [2025-Kumar-UniMoral; 2024-Kirgis], or a rights framework [2022-Prabhakaran] — and avoid the is-ought fallacy of treating population/state agreement as ethical truth [2023-Vida; 2025-Jiang].

10. **Audit your grader; where possible keep models out of the measurement loop.** Off-the-shelf toxicity APIs carry per-language bias; use translation-as-control audits and freeze released scores [2024-Nogara; 2025-Jigsaw; 2024-Brun]. If LLM judges are unavoidable, require cross-family cross-evaluator agreement [2025-Madan; 2025-Nawale; 2025-Urchs].

11. **Balance cells (dialect × category × class), disclose annotator demographics, treat sub-language dialect as an equity axis, and report IRR** — sub-38% IRR datasets are unusable [2024-Aly; 2025-Fayaz; 2020-Hoover; 2024-Bertram; 2020-Srivastava].

12. **Cover script/tokenization and obfuscation robustness.** Poor WordPiece coverage alone drops Assamese 16pp below Bodo [2024-with.pdf-NEIHS]; byte-level/sub-word models resist obfuscation [2025-Jigsaw; 2023-Haq]; build grounded obfuscation taxonomies and native/transliterated contrasts [2025-Lee; 2025-Kumar-SweEval].

13. **Include non-WEIRD normative frames as positive targets, but verify they govern behavior first.** Human-rights/UDHR scope [2022-Prabhakaran], Ubuntu/Ukama [2025-Osei Mensah], Dharmic reward shaping [2025-Madan], Indigenous reciprocity/data sovereignty [2025-IndigenousEthics; 2025-Unknown] — guarded by the exoticism-vs-empiricism check [2020-Galanos]. Separate a cultural *knowledge* probe (neutral-language phrasing) from fluency [2024-Faysse]. Judge value alignment on degree/justification, not just content [2026-Yun].
