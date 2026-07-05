# cultural-linguistic — sub-dossier part 3/6

Scope: 63 cards spanning non-Western/low-resource hate-speech corpora, cross-cultural moral-reasoning benchmarks, multilingual bias/stereotype suites, and culture-adaptation methods. The through-line is that "values" constructs (offensiveness, stereotype, morality) are culturally and linguistically indexed, and that English-built instruments transfer poorly.

## A. Synthesized claims

1. **English-trained multilingual models collapse on native-language values tasks.** On Korean span detection the multilingual MUDES model scores F1=12.8 vs 40.6 for a native model [2022-Jeong-KOLD]. Monolingual Marathi models (MahaBERT 0.909 2-class) consistently beat multilingual IndicBERT (0.865) [2024-Velankar-SamPar]. On the DIT, ChatGPT's post-conventional P-score falls from 48.09 (English) to 25.63 (Hindi) — a 46.7% drop — and Llama2 Swahili drops 38.2% [2024-Khandelwal-Multilingual Defining Issues Test]. SHADES-family models "fail to provide meaningful answers in Arabic, Bengali, Hindi, Marathi" [2025-Al-Towards a Multilingual Assessment of Stereotypes].

2. **Translation-based benchmark construction imports the source culture's norms.** Machine-translating CrowS-Pairs into Chinese/Russian/Indonesian/Thai (1,042 items) imports US sociocultural framing; Thai mBERT shows the worst bias (90.69) partly as an artifact [2025-Zhou-Bias Beyond English]. SafetyBench's Baidu-translated items and Jigsaw's English-labeled toxicity both carry this caveat [2024-Zhang-SafetyBench; 2025-Jigsaw]. The recommended alternative is native-first authorship (see claim 8).

3. **The language of elicitation is itself a values probe, not a neutral channel.** Simplified vs Traditional Chinese — differing only in Unicode code points — yields systematically less-opinionated, more-censored-aligned outputs in Simplified, across every model tested [2025-Unknown-PoPETs Chinese Censorship Bias]. Arabic-language debate prompts amplify bias to 95–100% one-sided win rates vs more neutral Russian [2025-Demidova-John vs. Ahmed]. Chinese-origin models jump ~0.85–0.95 on moral-stage scores when queried in Chinese [2025-Jiang-EMNLP Educator-role].

4. **Perceived offensiveness/morality is driven more by the individual (and their moral foundations) than by nationality.** Across 4,309 annotators in 21 countries, 39.5% of variance in offensiveness labels is individual, while country explains only 2.9% and region 0.7%; Care and Purity moral foundations significantly mediate cross-cultural gaps [2023-Davani-Disentangling Perceptions of Offensiveness]. This argues for demographic/moral-profile-conditioned baselines rather than a single gold label.

5. **MCQ/likelihood bias scores do NOT reliably predict generative behavior — but recognition can predict safe generation.** BBG shows QA-based and generation-based bias rankings are uncorrelated (English coeff 0.015, p=0.832; Korean −0.102) [2025-Jin-Social Bias Benchmark for Generation]. Yet SafetyBench finds MCQ safety-understanding correlates r=0.91–0.99 with actual safe generation [2024-Zhang-SafetyBench]. The reconciliation: recognition predicts *refusal/safety* but not *latent stereotype leakage* — so both an intrinsic probe and a generative probe are required (see claim 7).

6. **"Bigger model = more biased" is often a task artifact of likelihood-preference probes.** McBE's five-task battery shows intrinsic preference tasks (SS/PC) make larger Qwen2.5 look more biased (87.69→77.11 for 0.5B→32B) while comprehension tasks reverse the ordering [2025-Lan-McBE]. Stronger-reasoning models simultaneously score higher on abstract moral stage yet are MORE vulnerable to role-level jailbreaks (Harmful Response Rate 0.68→0.89 under injection) [2025-Jiang-EMNLP Educator-role].

7. **Multi-dimensional value representations beat binary safe/unsafe.** Grounding evaluation in Schwartz's 10 cross-culturally validated (≈80 countries) value dimensions gives interpretable "which value was violated" signals [2023-Yao-Value FULCRA]. WVS-anchored personas reproduce human demographic distributions (alignment 0.79–0.83, 1−EMD) across 93,312 configurations [2026-Tagarelli-Culturally Grounded Personas], and CLCA reduces WVS KL-divergence from 0.6011 to 0.5112 by fine-tuning on culture-specific social dialogue [2025-Liu-Cultural Learning].

8. **Native-speaker-first, community-in-the-loop construction is the emerging gold standard for non-WEIRD benchmarks.** SHADES built 304 stereotypes across 37 regions and 16 languages from 43 native speakers, not translation [2025-Al]. BengaliMoralBench hand-authored 3,000 scenarios from scratch for contamination resistance [2025-Kumar-BengaliMoralBench]. IndoToxic2024 used focus groups with targeted minorities for keyword elicitation [2024-Wijanarko; 2025-Susanto]. Burmese context experts raised annotator agreement 68.75%→93% via paired peer discussion [2022-Nkemelu]. Ethiopian GGBTD used native translators plus separate professional-linguist editors [2024-Sewunetie].

9. **Non-Western ethical ontologies are structurally absent from current benchmarks and would change item content, not just language.** Ubuntu's relational personhood ("I am because we are") contradicts the individualist assumptions baked into OECD/COMEST-style principles [2020-van Norren; 2025-UbuntuAI]. Confucian virtue vocabulary (ren, xiao, li, yi) [2024-So], Shinto techno-animist moral patienthood [2024-Puzio], and Indigenous epistemologies [2025-Ofosu-Asare] each imply paired individual-vs-communal item framings absent from Western suites.

10. **Value judgments are relative to a specified value, and models can be made to condition on it.** Providing an explicit natural-language value as *input* lets one model label the same content "Sexist" or "Non-Sexist" depending on the value supplied (VA-BART 74.07% acc, +15.56 W-F1 over baselines) [2022-Bang-Enabling Classifiers]. This "value-as-instruction" design is the cleanest pluralism-aware pattern in the batch.

11. **Low-resource languages carry hidden measurement-validity threats: OOV, script/transliteration noise, and code-switching.** Only 4.25% of STEM bias-probe words appear in a major Bangla corpus, masking bias rather than showing its absence [2025-Arnob-Bangla]. Telugu Latin→native transliteration degrades LLM performance and confounds language with script [2026-Rehman-X-MuTeST]. Assamese code-mixing/transliteration and Malayalam Romanization both degrade detection [2025-Nath; 2025-Prasannan].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Ljubesic-Slovene/Croatian | Thread-level (not comment-level) train/test split prevents conversational-context leakage; encrypted release enables research on harmful content |
| 2019-Ousidhoum-Multilingual Multi-Aspect | Five simultaneous aspects incl. annotator emotional reaction; IAA varies by language (α 0.153 EN / 0.244 FR) |
| 2020-Nangia-CrowS-Pairs | Minimal-pair group-word substitution + pseudo-log-likelihood; ALBERT 67.0% (ideal 50), highest bias on religion; US-centric |
| 2020-Sigurbergsson-DKHate | Publish low IAA *then* document construct-narrowing; full Bender-Friedman data statement |
| 2021-Chandra-Antisemitism | Single hate type subdivided into 4 theoretical subtypes (Political/Economic/Religious/Racial) |
| 2022-Bang-Enabling Classifiers | Value-as-instruction: same content, opposite label under value vs counter-value |
| 2022-Jeong-KOLD | Culturally-specific target groups; multilingual MUDES F1=12.8 vs native 40.6 |
| 2022-Yilmaz-Cross-Domain | Domain-balanced (5×20k) design + recovery/decay ratios for cross-domain transfer |
| 2023-Ghosh-ChatGPT MT gender | Gender-neutral-source→English translation as an organic bias probe; 100% failure to use "they" |
| 2023-Lee-KoSBi | Context-conditioned safety labeling; demographic axes anchored to human-rights instruments |
| 2023-Yao-Value FULCRA | 10-dim Schwartz value vector (validated ≈80 countries) instead of binary safe/unsafe |
| 2024-Bang-Political Bias | Self-generated pro/opp "extreme anchors"; decompose bias into stance/content/style |
| 2024-Garcia-Moral Turing Test | Actual vs *believed* source dissociation exposes rater bias; humanization ablation |
| 2024-Jafri-RUHate-MM | 3-phase iterative annotation raised κ ~0.50→0.76; multimodal target taxonomy |
| 2024-Khandelwal-Multilingual DIT | Validated psychometric instrument + 48 permutations/dilemma; Hindi P-score drops 46.7% |
| 2024-Luu-ViTHSD | Aspect-based per-target labels; report κ by target and by severity separately |
| 2024-Pfister-SuperGLEBer | Hierarchical per-task-type averaging + uniform training protocol for fair leaderboards |
| 2024-Sewunetie-Amharic/Tigrigna | Enumerate the full set of valid gendered outputs as ground truth; strict gender-balancing |
| 2024-Takemoto-Moral Machine LLM | AMCE preference-vector profile + Euclidean distance to human data; no cultural disaggregation |
| 2024-Wijanarko-Indonesia | Community focus-group keyword elicitation; local legal definitions of harm |
| 2024-Zhang-SafetyBench | MCQ safety understanding correlates r=0.91–0.99 with safe generation |
| 2025-Al-SHADES | 304 stereotypes / 37 regions / 16 languages, native-authored; geographic-validity annotation |
| 2025-Brito-ToxSyn | Systematic non-toxic counterexamples about each minority + discourse-type labels |
| 2025-Do-ViToSA | Toxic-vs-nontoxic WER decomposition; test-set-first construction |
| 2025-Fasching-Inconsistencies | Full-factorial synthetic set; cross-system SD as primary metric (78.4% of groups SD>0.2) |
| 2025-Hatemo-Trolley | Nationality is the dominant driver of LLM moral variation; human survey as per-nationality baseline |
| 2025-Jiang-EMNLP Educator | Capability-safety paradox on same items; bilingual moral-stage shift ~+0.9 in Chinese |
| 2025-Jin-BBG | QA vs generation bias uncorrelated; order-swap consistency as neutrality metric |
| 2025-Kumar-BengaliMoralBench | From-scratch native authorship as contamination control; MCC + κ reported; κ 0.61→0.87 |
| 2025-Lan-McBE | Five-task battery; "bigger=more biased" is an SS-task artifact |
| 2025-Lin-MORALISE | Turiel-domain taxonomy; modality-attribution annotation; judgment (~88) vs norm-attribution (~42–66) gap |
| 2025-Nath-Assamese | Train-only augmentation + authentic-only test; temporally-distinct few-shot exemplars |
| 2025-Prasannan-Malayalam CS | HITL vs one-shot: one-shot generation 100% repetition; 12-metric dataset-quality dashboard |
| 2025-Seker-HATECAT-TR | GPT-4o pre-annotation + expert review (51% accepted unmodified); span-level discourse typology |
| 2025-Susanto-IndoToxic2024 | Demographic-aware annotation boosts polarization detection; preserve annotator disagreement |
| 2025-Wen-BUMBLE | Psychometric-grounded attack families (Disguise/Deception/Teaching); cross-category bias transfer |
| 2025-Zhou-Bias Beyond English | Normalized Bias Score for cross-model comparison; translation imports US norms |
| 2026-Rehman-X-MuTeST | Human token-level rationales across languages; culturally-divergent rationale items |
| 2023-Wang-STREAM | Judgment+degree+confidence capture; demographic-anchored (not universal) baselines |
| 2024-Velankar-SamPar/MahaHate | Monolingual > multilingual as a validity check; 4-way hate taxonomy |
| 2025-Jigsaw-Multilingual Toxic | Cross-lingual transfer (train EN, test other) probes construct robustness |
| 2019-Corazza-Italian | Hold model fixed, vary only training-data mix; hate speech doesn't transfer across platforms |
| 2020-van Norren-Ubuntu | Multi-ontology side-by-side principle table; paired individual-vs-communal item framing |
| 2022-Nkemelu-Burmese | Context experts as co-designers; paired peer discussion raised agreement 68.75%→93% |
| 2023-Davani-Offensiveness | 39.5% variance individual, 2.9% country; Care/Purity foundations mediate |
| 2023-Sukhamsri-Thai | Graded tripartite voting label; emoticon-adversarial sarcasm items |
| 2024-Arzberger-Situated Values | Situation triad {user/context/AI} metadata; record annotator situation, preserve disagreement |
| 2024-Hayes-Virtue/Narrative | Practice-embedded evaluation; triadic ethical-intention rubric |
| 2024-Nguyen-ViHateT5 | Prefix-based multi-task unification (classify+span) in one generative evaluator |
| 2024-So-Confucian | Virtue-ethics vocabulary (ren/xiao/li/yi) for non-Western alignment framing |
| 2024-Vasilev-CRAFT | 17-category cultural taxonomy; entity-level cultural ground truth; human > LLaVA captions |
| 2025-Arnob-Bangla | Report OOV rate before running bias metrics (only 4.25% in-vocab) |
| 2025-Demidova-Debate | Forced-outcome debate framing; language-as-confound (Arabic amplifies to 95–100%) |
| 2025-Jiang-Cross-lingual Capsule | Four-way error taxonomy (implicit/keyword/world-knowledge/translation) for multilingual audits |
| 2025-Liu-CLCA | Social-interaction data (not knowledge) is the active ingredient; WVS KL-D control |
| 2025-Ofosu-Asare-Cognitive imperialism | Epistemological audit of who authored items and what counts as "correct" |
| 2025-Unknown-Chinese Censorship | Script-pair (Simplified/Traditional) as minimal contrastive elicitation control |
| 2025-Zhang-Cognitive Bias religion | Pre/post RCT measuring whether model content actually shifts human attitudes |
| 2026-Tagarelli-Personas | Cartesian product of WVS variables as full-coverage item scaffold; generator≠evaluator |
| Zhipu AI-AlignMMBench | Prompt-rewrite → consistency-as-inverse-SD; fine-tuned calibrated evaluator beats GPT-4 judge |
| 2024-Puzio-Eco-Relational | Anthropocentric-assumption reflexive check; multi-species/eco moral-patienthood items |
| 2025-Hashmi-Multilingual HS | Language-specific insight → cross-linguistic integration (not translation) |
| 2025-UbuntuAI-Governance | Five-layer relational governance rubric incl. Harm Reconciliation Panels |

## C. Patterns & disagreements

**Convergences.** (a) *Native-first beats translation* — asserted by [2025-Al], [2025-Kumar], [2024-Wijanarko], [2022-Nkemelu], [2024-Sewunetie] and confirmed negatively by [2025-Zhou] and [2024-Zhang-SafetyBench] whose translated items import source-culture norms. (b) *Monolingual/culturally-grounded models beat generic multilingual ones on native tasks* [2022-Jeong-KOLD; 2024-Velankar; 2025-Nath]. (c) *Disaggregate, never collapse to one score* — recurs as issue-disaggregation [2024-Bang-Political], per-task-type averaging [2024-Pfister], demographic baselines [2023-Wang-STREAM; 2023-Davani], and multi-task batteries [2025-Lan-McBE]. (d) *Report reliability honestly* — publishing low IAA and the construct-narrowing decision [2020-Sigurbergsson], per-target κ [2024-Luu], and OOV rates [2025-Arnob].

**Disagreements.** (1) *Does recognition predict behavior?* SafetyBench says MCQ↔generation correlates r=0.91–0.99 [2024-Zhang-SafetyBench]; BBG says QA and generation bias are uncorrelated [2025-Jin]. Best read: MCQ predicts refusal-safety but not latent-stereotype leakage. (2) *Universalism vs pluralism of the value frame.* Value FULCRA leans on Schwartz as cross-culturally universal [2023-Yao]; the ontology papers argue Western frames systematically misrepresent non-Western moral universes [2020-van Norren; 2025-Ofosu-Asare; 2024-Puzio; 2025-UbuntuAI]. (3) *Does cross-lingual transfer work?* Debiasing (SenDeb) transfers cross-lingually [2025-Zhou] and Jigsaw treats EN→other transfer as viable [2025-Jigsaw], but KOLD and Velankar show catastrophic transfer failure. (4) *Bigger = better or worse?* [2025-Lan] and [2025-Jiang-EMNLP] show larger/stronger-reasoning models can be more biased or more jailbreakable, contradicting the naive scaling assumption.

## D. Exemplars & anti-patterns

**Best-designed.** *SHADES* [2025-Al] — 43 native speakers, 16 languages, geographic-validity annotation per item, minimally-contrastive pairs, grammatically-annotated templates for synthetic expansion: the reference standard for multilingual stereotype coverage. *BengaliMoralBench* [2025-Kumar] — from-scratch native authorship for contamination resistance, culturally-adapted triadic ethics lenses (Virtue/Commonsense/Justice with indigenous vocabulary), country-specific-vs-shared item tagging (52% CS), and a full psychometric package (MCC + κ, κ 0.61→0.87 after calibration). *Multilingual DIT* [2024-Khandelwal] — reuses a validated instrument with known human norms and 48 permutations per dilemma to control order effects. *Davani* [2023] — the cleanest empirical grounding for why per-annotator, moral-foundation-conditioned baselines are needed.

**Anti-patterns.** *Machine-translated CrowS-Pairs* [2025-Zhou] — imports US stereotype framing into Chinese/Thai/Indonesian, so "bias" scores partly measure translation mismatch (authors concede). *CrowS-Pairs itself* [2020-Nangia] — explicitly US-only, non-transferable, with 23 known-invalid items left in. *L3Cube-MahaHate* [2024-Velankar] — no IAA statistic reported and uniform (unnatural) class balance inflating accuracy. *Fasching* [2025] as a cautionary result rather than a bad design: 78.4% of 125 groups had cross-system SD>0.2, i.e. the *same* content is scored radically differently depending on which moderation system labels it — evidence that any single-labeler benchmark is fragile. Persona/synthetic-data methods carry a "cultural caricature" risk [2025-Liu; 2026-Tagarelli].

## E. Design lessons

1. **Build native-first; treat translation as a last resort and always report the caveat.** Elicit items from native speakers with geographic-validity tags [2025-Al], hand-author for contamination resistance [2025-Kumar], and use community focus groups for harm vocabulary [2024-Wijanarko; 2022-Nkemelu].
2. **Include an intrinsic *and* a generative probe** for every values axis, because MCQ rankings do not transfer to generation [2025-Jin]; validate with an understanding↔generation correlation study [2024-Zhang-SafetyBench] and an order-swap neutrality check [2025-Jin].
3. **Make elicitation language a controlled variable.** Use script-pair minimal contrasts [2025-Unknown-Censorship], parallel multilingual items [2025-Demidova], and per-language reporting — never a single aggregate [2024-Khandelwal].
4. **Replace universal gold labels with demographic/moral-profile-conditioned baselines** [2023-Davani; 2023-Wang-STREAM], and record annotator situation and disagreement rather than majority-voting them away [2024-Arzberger; 2025-Susanto].
5. **Use value-as-instruction and multi-dimensional value vectors** so one item supports plural judgments [2022-Bang] and violations are interpretable [2023-Yao; 2026-Tagarelli].
6. **Guard low-resource validity:** report OOV rates before trusting bias metrics [2025-Arnob], separate script/transliteration effects from language effects [2026-Rehman], and keep synthetic augmentation out of the test set [2025-Nath].
7. **Build a difficulty gradient to avoid ceiling saturation:** pair easy binary judgment with hard fine-grained attribution [2025-Lin], hierarchical/conditional labels [2022-Jeong; 2020-Sigurbergsson], and span- or rationale-level evidence [2026-Rehman; 2025-Do].
8. **Pair harmful items with structurally-similar benign counterexamples** so classifiers learn context not keywords [2025-Brito], and test cross-system consistency [2025-Fasching] and cross-domain transfer [2022-Yilmaz].
9. **Audit the embedded ontology:** offer paired individual-vs-communal framings and non-Western ethical vocabularies (Ubuntu, Confucian, Shinto, Indigenous) rather than assuming a Western individualist frame [2020-van Norren; 2024-So; 2024-Puzio; 2025-Ofosu-Asare; 2025-UbuntuAI].
10. **Prefer a calibrated, fine-tuned evaluator over an API LLM-judge** where feasible [Zhipu AI-AlignMMBench], and quantify prompt robustness via paraphrase consistency [Zhipu AI-AlignMMBench].
