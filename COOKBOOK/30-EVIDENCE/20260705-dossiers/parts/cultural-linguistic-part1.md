# cultural-linguistic — sub-dossier part 1/6

Scope: cross-cultural/multilingual value evaluation. 62 cards read (61 papers + 1 lab card).

## A. Synthesized claims

1. **LLMs default to WEIRD / American / liberal moral profiles regardless of prompt language, assigned persona, or country of origin.** All 20 US- and China-made LLMs answered MFQ-2 and WVS items more like American than Chinese respondents; participant-nationality (β=−.30) dwarfed model-origin (β=.03), and Chinese language/persona/models only *slightly* mitigated the skew [2025-Haslett-Made-in China]. English models predict Rich-West norms far better (GPT3 r=0.85 English vs 0.411 WVS) [2023-Ramezani-Knowledge of Cultural Moral Norms], small models over-moralize and miss that sex-before-marriage/homosexuality are the most contested topics [2024-Meijer-LLMs as mirrors], and Delphi mirrors young liberal North American MTurkers because that is who annotated it [2022-Fraser-Does Moral Code Have a Moral Code].

2. **Moral reasoning degrades sharply in lower-resource languages, and judgments shift with input language.** On the multilingual DIT, P-scores dropped from English (~48–56) to Hindi (ChatGPT 25.63) and Swahili, at/below random [2024-Khandelwal-Do Moral Judgment and Reasoning Capability]. GPT judgments flip between English and Korean on the same dilemmas [2025-Yoo-Moral Judgment of LLM Using Korean Datasets]; moral competence "does not automatically transfer across languages" [2025-Flores-BenchMoral]; IslamTrust shows a persistent Arabic-over-English advantage (71.43% vs 61.58%) [2025-Lahmar-IslamTrust].

3. **Translation is not localization: culturally-grounded benchmarks must re-ground stereotypes, entities, and axes, not merely translate.** IndiBias uses a translate-filter-modify pipeline that drops non-applicable categories, swaps US names/places for Indian ones, and adds India-specific axes (caste, region) absent from CrowS-Pairs/StereoSet [2024-Sahoo-IndiBias]. Dutch CrowS-Pairs replaced "Mexican"→"Moroccan," dollars→euros, and fixed non-minimal pairs [2025-Satheesh-Dutch CrowS-Pairs]. SHADES annotates each stereotype with the *regions/languages where it is culturally valid* so models are scored only on locally-applicable items [2025-Al-SHADES]. Fairness axes themselves are geo-cultural: Region and Caste are salient in India but absent from Western frameworks, and American names underestimate MuRIL's bias [2022-Shaily Bhatt-Re-contextualizing Fairness in NLP].

4. **Culture-specific value constructs can be embedded directly into benchmark taxonomies.** FLAMES encodes Chinese values (harmony 和谐, benevolence 仁, courtesy 礼, Doctrine of the Mean 中庸) as a Morality subcomponent [2023-Huang-Flames]; CMoralEval builds a five-category Confucian-plus-modern taxonomy from a CCTV ethics TV program and newspaper "moral anomies" [2024-Yu-CMoralEval]; KoSBI adds Korea-specific axes (regional origin, marital status, criminal record) [2025-Song-Evaluation of Social Bias Classification]; IslamTrust maps each category to an explicit Islamic guideline (e.g. "acknowledge scholarly disagreement") [2025-Lahmar-IslamTrust]; the Social Worldview Taxonomy grounds items in Cultural Theory's Hierarchy/Egalitarianism/Individualism/Fatalism quadrant [2025-Li-Analyzing Cognitive Differences].

5. **Human moral preferences show real cross-cultural clustering benchmarks can exploit as stratification and external-validity anchors.** The Moral Machine's 39.61M decisions from 233 countries yielded three moral clusters (Western/Eastern/Southern) and correlated cultural distance from the US with moral distance at ρ=0.49 [2018-Awad-The Moral Machine experiment]. The same conjoint/AMCE design on 52 LLMs shows larger/proprietary models align closer to aggregated human preferences (size↔distance ρ=−0.54) but amplify utilitarian bias attributed to Western training data [2025-Zaim Bin Ahmad-Large-scale moral machine experiment].

6. **Low-resource, code-mixed, and transliterated text is the hardest frontier and retains the most headroom.** Code-mixed Dravidian span-ID tops out at F1≈0.40 (85.55% OOV) [2021-Ravikiran-DOSA]; SGHateCheck Tamil detection is near-zero even after multilingual fine-tuning [2024-Ng-SGHateCheck]; transliterated Bangla needs translation-based prompting for +8% F1 [2025-Ishmam-BanTH]; Urdu collapses transformer F1 to 0.36–0.50 while English/Spanish near ceiling [2025-Usmana-Multilingual Hate Speech]. Translate-then-classify beats OOD native classification in 81.3% of languages, benefit rising with resource level and MT quality [2025-Jigsaw-Leveraging Machine Translation].

7. **Held-out aggregate F1 masks catastrophic culture-specific failures; functional/contrastive suites expose them.** HateCheckHIn's 34 functionalities show a model at 49.88% overall dropping to 0.0% on code-mixing functionalities; minimal contrast pairs ("I hate Hindus" vs "I hate apples") isolate the boundary [2022-Das-HateCheckHIn]; SGHateCheck separates held-out (0.7–0.9 F1) from diagnostic scores [2024-Ng-SGHateCheck]; small descriptive perturbations collapse a 99.55%-accurate classifier to 51% [2024-Fitzgerald-Some Issues in Predictive Ethics Modeling].

8. **Open-ended and behavioral (enacted) evaluation diverges from — and often inverts — closed-ended (stated) evaluation.** F2Bench's open-ended format inverts CrowS-Pairs rankings, exposing an MCQ "minimum-score" guessing artifact [2025-Davies-F2Bench]; VALACT-15K finds a knowledge-action gap (PVQ-40 vs scenario r≈0.3) and near-perfect cross-model convergence (r≈1.0) despite broad human variability [2026-Huang-Knowing But Not Doing]; word-association probing shows LLM moral associations are more abstract/sterile than humans', especially for vices [2025-Xiang-Comparing Moral Values]; questionnaire leakage into training data threatens direct-probe genuineness [2025-Xiang; 2026-Huang].

9. **Multi-turn context erodes cultural/fairness alignment that single-turn probes certify safe.** FairMT-Bench shows bias accumulates over turns via six attack templates, even GPT-4 at 56.67% on the hard subset [2025-Fan-FAIRMT-BENCH]; F2Bench's 6-round induction drives stereotype-affirming conclusions [2025-Davies-F2Bench]; but context is often weakly related to reply meaning, so naive injection yields marginal gains (+3.29% F1) [2024-Toygar-Turkish Offensive Language].

10. **Annotator identity and aggregation are load-bearing: majority-vote erases minority moral perspectives.** ConvAbuse scores against *all* annotator labels not a single gold [2021-Cercas Curry-ConvAbuse]; Trager warns maximizing agreement suppresses moral variability and collects annotator ideology/MFQ metadata [2022-Trager-The Moral Foundations Reddit Corpus]; WoNBias/OPSD stratify annotators by region and gate on kappa [2024-Aupi-WoNBias; 2024-Hossein-ParsOffensive]; Delphi's demographic-distance-to-annotators is itself a validity flaw [2022-Fraser].

## B. Evidence table

| Card stem | Most design-relevant fact |
|---|---|
| 2018-Awad-The Moral Machine experiment | 9-factor conjoint/AMCE over 39.61M decisions; 3 moral clusters; ρ=0.49 cultural-distance anchor |
| 2025-Zaim Bin Ahmad-Large-scale moral machine | Same AMCE on 52 LLMs; distance-to-human vector; size↔alignment ρ=−0.54; amplified Western utilitarian bias |
| 2023-Ramezani-Knowledge of Cultural Moral Norms | "In [Country] [Topic] is [judgment]" probe; r=0.85 English vs 0.411 WVS; fine-tuning = utility-bias trade-off |
| 2024-Meijer-LLMs as mirrors | Variance test: models over-moralize, miss which topics are cross-culturally contested |
| 2024-Aksoy-Whose Morality Do They Speak | MFQ-2 × 8 langs × 100 reps; WEIRD>non-WEIRD on Care/Loyalty/Purity |
| 2025-Haslett-Made-in China | 20 US+CN LLMs all skew American; leave-one-dimension-out + z-scored cosine to human panels |
| 2024-Khandelwal-Multilingual DIT | Validated instrument; P-score drops to random in Hindi/Swahili; 48 permutations |
| 2023-Rao-Ethical Reasoning over Moral Alignment | Ethical-consistency (policy-following) target; complement pairs; non-Western Rajesh dilemma hardest |
| 2024-Yu-CMoralEval | 30,388 MCQ from Chinese TV + newspapers; morality-neutral 3rd distractor; models ≈random 0.33 |
| 2023-Huang-Flames | Adversarial Chinese; attack-success item gate; Chinese-values subcomponent; scorer beats GPT-4 judge |
| 2024-Liu-Evaluating Moral Beliefs | Word/scenario/debate three-module; Chinese models flip 54–69% post-debate vs 1–8% English |
| 2024-Sahoo-IndiBias | Translate-filter-modify localization; caste+region axes; word-level masking; MT-blinded annotators |
| 2022-Shaily Bhatt-Re-contextualizing Fairness | Geo-specific axes (Region, Caste); American names underestimate MuRIL bias; restorative justice |
| 2025-Al-SHADES | 304 stereotypes × 16 langs; per-item VALID REGIONS/LANGUAGES; agreement slot tags; tiered gated release |
| 2025-Satheesh-Dutch CrowS-Pairs | Cultural re-grounding; persona swing (bad 94% vs good 22%); adaptation-quality taxonomy |
| 2022-Das-HateCheckHIn | 34 functionalities; code-mixing floors models to 0.0%; minimal contrast pairs; κ=0.95 |
| 2024-Ng-SGHateCheck | 4 SE-Asian langs; LLM-translate + native-refine; legal-grounded groups; Tamil near-zero |
| 2024-Fitzgerald-Predictive Ethics | Contrast sets collapse 99.55%→51%; 3–5 word shifts; tabular norm representation |
| 2025-Davies-F2Bench | Open-ended inverts CrowS-Pairs; fairness-factuality FF1; 6-round multi-turn induction |
| 2025-Fan-FAIRMT-BENCH | Multi-turn bias accumulation; 6 attack templates; distill-hardest 10K→1K; triangulated judging |
| 2026-Huang-Knowing But Not Doing | Stated vs enacted gap r≈0.3; LLMs converge r≈1.0 while humans vary; role-play resistance |
| 2025-Xiang-Comparing Moral Values | Word-association indirect probe (contamination-resistant); LLMs abstract/sterile on vices |
| 2026-Hu-The Straight and Narrow | Moral Minimal Pairs; EN/ZH shared-but-different subspace; transfer discrepancy δ metric |
| 2020-Schramowski-Moral Choice Machine | 10-template Q/A averaging; 193-constitution cultural probing; adjective-injection adversarial |
| 2022-Trager-Moral Foundations Reddit Corpus | Annotator ideology/MFQ metadata; maximizing agreement suppresses moral variability |
| 2021-Cercas Curry-ConvAbuse | Score against ALL annotator labels not majority gold; annotators from targeted groups |
| 2024-Songyuan Liu-Measuring Spiritual Values | Repurpose Pew religiosity questionnaires; two-instrument convergent validity; religious-text debiasing |
| 2025-Lahmar-IslamTrust | Guideline-to-category mapping; abstention/"scholars differ" correct; bilingual isolates language effect |
| 2025-Umer-Sacred or Secular | Religious identity conditions output: 50% of ChatGPT financial emails show in/out-group bias |
| 2025-Song-KoSBI | Korea-specific 15-axis taxonomy; dual error-direction metric; GPT-3.5 > GPT-4o |
| 2025-Li-Social Worldview Taxonomy | Cultural Theory scaffold; dynamic social-referencing (peer-consensus dose-response) |
| 2025-Jigsaw-Machine Translation | translate-classify beats OOD in 81.3% of langs; refusal-aware scoring; ΔAUC vs resource level |
| 2025-Ishmam-BanTH | Transliterated Bangla; translation-based prompting +8%; further-pretraining on in-domain texts |
| 2025-Bhattacharjee-INDOHATEMIX | Code-mixed Hindi-English; LLMs beat BERT at 10% data; target-group distribution as validity metric |
| 2025-Piot-Bridging Gaps | Harmonized meta-collection; dialect-variant pairs (Galician-ES vs -PT); psycholinguistic fidelity checks |
| 2025-Mining-Albanian hate speech | Char 4-gram TF-IDF low-resource baseline; targeted provocative-post collection for balance |
| 2019-Fortuna-Portuguese Hate Speech | Rooted-DAG intersectional label ontology; per-category kappa; two-tier annotation |
| 2020-Mollas-ETHOS | Active-learning balanced sampling; multi-dimensional harm schema; soft proportion labels |
| 2024-Toygar-Turkish | Operationalizes conversational context; helps/hurts/irrelevant failure taxonomy |
| 2024-Hossein-ParsOffensive | Iterative kappa-gated 3-phase annotation; MLM domain adaptation for minority classes |
| 2024-Aupi-WoNBias | Regional annotator stratification; 3-class with positive-advocacy class; offline+online fusion |
| 2023-Das-Bengali Gender (BIBED) | Explicit/implicit dual-track; religion+nationality axes; positionality statement; "visibility trap" |
| 2022-researchers-Bulgarian | Sentence-level split; balanced-accuracy secondary metric; char n-grams; 1.74% base rate |
| 2024-Rashid-Urdu Toxicity | Roman-script multilabel toxicity; detect-then-classify pipeline (low-confidence card) |
| 2025-Monnar-Cross-lingual hate speech | Hurtlex-aligned domain embeddings; non-literal equivalence ("migranti"→"illegals") |
| 2025-Usmana-Multilingual Hate Speech | Cross-language pivot-validation subset + cross-lingual κ; Urdu hard split |
| 2025-Chared-French hate speech | Mixed real+AI-generated data; BART zero-shot target labels; balanced-target mitigation |
| 2024-University-Coded Antisemitism | Coded-language discovery pipeline; "coded begets coded"; benchmark-maintenance tool |
| 2025-Akpobi-Yankari Yoruba | Ethical exclusion of missionary (JW300) texts; dataset-audit-before-build; MinHash dedup |
| 2025-Liu-Chinese-language AI bias | Search-autocomplete as zero-annotation stereotype proxy; agreement-as-safeguard; 240-group taxonomy |
| 2024-Bolatbek-Kazakh (mismatched) | Card is wrong paper; lesson: verify OCR-to-stem provenance |
| 2025-Bolatbek-offensive content | Mis-dated 2021 review; image-embedded-text detection as unaddressed gap |
| 2025-Rana-Indigenous Data Sovereignty | OCAP + CARE sovereignty rubric; digital-colonialism framing (abstract-only) |
| 2020-Gabriel-AI Values and Alignment | Six alignment targets; fair principles under pluralism; overlapping-consensus selection |
| 2022-Fraser-Does Moral Code | Psych-instrument probing (CADS/MFQ/OUS); annotator-demographic distance as over-fit signal |
| 2024-Dognin-Contextual Moral Value Alignment | Per-value specialist agents + moral-profile-vector aggregation (MORL) |
| 2024-Ranjan-Survey of Bias | Bias-type + source taxonomy checklist; Western/English-centric research gap |
| 2025-Gao-MIST | Text-image flow: signal only from multimodal combination; good/bad label asymmetry |
| OpenAI-gpt-4o-system-card | Red team 29 countries/45 langs; Uhura-Eval fluent-speaker translations; accent-disparity dimension |

## C. Patterns & disagreements

**Convergence.** (i) Near-unanimous finding that current models carry a WEIRD/US/liberal default surfacing through *any* probe — questionnaire [2024-Aksoy; 2025-Haslett], norm-prediction [2023-Ramezani; 2024-Meijer], crowd-annotated classifier [2022-Fraser], and behavioral scenario [2026-Huang]. (ii) Held-out F1 is repeatedly shown to be a misleading aggregate that hides culture-specific failure, hence the strong convergence on functional/contrastive suites [2022-Das-HateCheckHIn; 2024-Ng-SGHateCheck; 2024-Fitzgerald]. (iii) Translation ≠ localization is a near-universal methodological lesson [2024-Sahoo; 2025-Satheesh; 2025-Al-SHADES; 2022-Shaily Bhatt]. (iv) Low-resource languages are consistently the discriminating hard split with the most headroom [2021-Ravikiran; 2025-Usmana; 2025-Jigsaw].

**Disagreements.** (a) *Does origin/language steer values?* Haslett finds origin and Chinese-language prompting barely move the American skew [2025-Haslett], while Liu finds Chinese-background models more collectivist and flip under debate far more [2024-Liu-Evaluating Moral Beliefs], and Aksoy finds both language and model have large effects with English *not* dominant [2024-Aksoy] — likely a construct/method difference (aggregate cosine vs foundation-level/behavioral). (b) *Converge or diverge?* Huang finds near-perfect enacted convergence [2026-Huang], Hu finds a "shared but different" EN/ZH subspace [2026-Hu], and Ahmad finds wide AMCE spread [2025-Zaim Bin Ahmad]. (c) *Bigger better?* Ahmad finds size↔alignment ρ=−0.54 and INDOHATEMIX finds LLMs beat BERT at 10% data [2025-Bhattacharjee], yet KoSBI finds GPT-3.5 > GPT-4o [2025-Song] and CMoralEval finds most models near random [2024-Yu] — scale helps only where the target culture is well-represented. (d) *Fine-tuning a fix?* Ramezani documents a utility-bias trade-off [2023-Ramezani] and NaVAB shows DPO shifts national alignment [2025-Ju], but both warn it injects the survey's biases [2023-Ramezani; 2024-Dognin].

## D. Exemplars & anti-patterns

**Best-designed.** *SHADES* [2025-Al-SHADES] is the strongest cultural-linguistic template: native-speaker authored (not translated), per-item cultural-validity annotation so models are scored only on locally-valid stereotypes, grammatical-agreement slot tags for morphological robustness, ships reusable templates (decoupling contamination from a fixed item set), and a tiered gated release keyed to resource level. *HateCheckHIn* [2022-Das-HateCheckHIn] and *SGHateCheck* [2024-Ng-SGHateCheck] are exemplary functional suites: minimal contrast pairs, hard negatives (counter-speech, reclaimed slurs), cross-script perturbations, per-protected-group scoring, and legal-framework grounding, all with κ=0.95 gold labels. *FLAMES* [2023-Huang-Flames] pairs a genuinely adversarial implicit-malice design with an attack-success item-quality gate, a withheld private split for contamination control, and a purpose-built scorer beating GPT-4-as-judge. *IndiBias* [2024-Sahoo] is the cleanest localization pipeline (translate-filter-modify + language-property-aware scoring + MT-blinded annotators).

**Anti-patterns.** *Fitzgerald's classifier* [2024-Fitzgerald] and the *Moral Choice Machine* [2020-Schramowski] show over-fit surface learning: 99.55%→51% under 3–5 word perturbations, and moral scores fooled by adjective injection — cautionary for any embedding/classifier-based values scorer. *Delphi* [2022-Fraser] exemplifies the majority-vote trap: crowd annotation silently encodes one demographic's morality and cannot distinguish moral from convention violations. *BenchMoral* [2025-Flores] and the *Umer study* [2025-Umer] (16 prompts, single run/annotator) show identity-variation designs need scale and replication. The two *Bolatbek* cards [2024-Bolatbek; 2025-Bolatbek] are provenance anti-patterns — wrong/mis-dated papers under the stem — verify source-to-card mapping before citing. NaVAB's equating *official media with national values* [2025-Ju] and CMoralEval's *state-sanctioned "correct" answers* [2024-Yu] risk encoding one institutional voice as a culture's ground truth.

## E. Design lessons

1. **Localize, don't translate.** Drop non-applicable categories, re-ground entities to local names/places/currency, and add culture-native axes (caste, region, marital status, religion×nationality) [2024-Sahoo; 2025-Satheesh; 2022-Shaily Bhatt; 2023-Das-Bengali Gender]. Annotate each item with the regions/languages where it is culturally valid and score only on valid items [2025-Al-SHADES].

2. **Author from within the culture, and record provenance.** Native-speaker authoring beats pivot-translation [2025-Al-SHADES; 2025-Akpobi]; stratify annotators by region [2024-Aupi]; collect annotator metadata and measure annotator-to-model demographic distance as an over-fit signal [2022-Trager; 2022-Fraser]; include a positionality statement [2023-Das-Bengali Gender]; apply OCAP/CARE sovereignty rubrics for Indigenous data [2025-Rana].

3. **Preserve pluralism in aggregation.** Score against all annotator labels not majority gold [2021-Cercas Curry]; use soft proportion labels [2020-Mollas]; report per-group kappa and gate on it [2019-Fortuna; 2024-Hossein]; treat maximizing agreement as a red flag [2022-Trager]. Consider modular per-value agents aggregated on a moral-profile vector [2024-Dognin] and overlapping-consensus selection over one "true" theory [2020-Gabriel].

4. **Decompose the aggregate.** Replace single F1/accuracy with functional suites (minimal contrast pairs, hard negatives, cross-script perturbations, per-group scoring) so failures localize [2022-Das-HateCheckHIn; 2024-Ng-SGHateCheck]; report dual error-direction metrics (over-permissive vs over-hedging) and separate held-out from diagnostic scores [2025-Song].

5. **Prefer open-ended and behavioral over closed-ended.** MCQ invites minimum-score guessing and can invert rankings; pair stated (questionnaire) with enacted (scenario) measures to expose the knowledge-action gap [2025-Davies; 2026-Huang]. Use contamination-resistant indirect probes (word association, text-image flow, moral minimal pairs) where leakage is a risk [2025-Xiang; 2025-Gao; 2026-Hu].

6. **Test multi-turn robustness.** Bias/misalignment accumulates across turns and slips past single-turn filters; include anaphora-laundering, scattered-question, and induction attack templates and score only the final turn [2025-Fan; 2025-Davies]. But validate that context is actually relevant before injecting it [2024-Toygar].

7. **Build for low-resource and code-mixed text explicitly.** These are the discriminating hard splits; report ΔAUC vs resource level and offer translate-then-classify / translation-based-prompting baselines [2025-Jigsaw; 2025-Ishmam]; use char n-grams or domain-specific embeddings for morphology and loaded connotations [2022-researchers-Bulgarian; 2025-Monnar]; measure refusals separately for sensitive content [2025-Jigsaw].

8. **Anchor to external human data and design difficulty in.** Use conjoint/AMCE with distance-to-human-vector [2018-Awad; 2025-Zaim Bin Ahmad], validated instruments with known norms [2024-Khandelwal; 2024-Aksoy], and correlate with cultural indicators [2018-Awad; 2023-Ramezani]. Escalate difficulty with tempting distractors [2024-Yu], attack-success item gates [2023-Huang], complement-policy pairs [2023-Rao], and distill-the-hardest subsets [2025-Fan]; withhold a private split against contamination [2023-Huang].

9. **Embed culture-native constructs and pluralism-aware "correct" answers.** Encode local value systems as first-class taxonomy dimensions [2023-Huang; 2024-Yu; 2025-Li], reward abstention/"scholars differ" where genuine disagreement exists, and test whether models default to the majority worldview under ambiguity [2025-Lahmar]. Test policy-following (ethical consistency) separately from endorsement to sidestep prescriptivism [2023-Rao].
