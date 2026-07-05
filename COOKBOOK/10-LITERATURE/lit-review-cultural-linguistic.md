# Cultural and Linguistic Values Evaluation — A Literature Review

> **CEI COOKBOOK · 10-LITERATURE.** A narrative synthesis of the cross-cultural and
> multilingual values-evaluation literature, prepared for a model tasked with designing
> new cultural/linguistic benchmarks. This document is descriptive: it traces where the
> field's constructs came from, what it has measured, and where it is stuck. The
> prescriptive "what to do" lives in `00-KNOWLEDGEBASE/11-cultural-linguistic-methods.md`
> and is not repeated here. Primary evidence:
> `30-EVIDENCE/20260705-dossiers/20260705-cultural-linguistic-dossier.md` (~366 cards) and
> `30-EVIDENCE/20260705-digests/20260705-cultural-digest.md` (the 218-benchmark
> meta-evaluation). `[stem]` = an evidence card in `30-EVIDENCE/20260705-cards/`.
>
> **Provenance caveat, load-bearing throughout:** the Cultural-Global meta-evaluation's
> *cross-model* trial numbers (Study 3) are **descriptive only** — its 10 nominal models
> collapse to an effective sample size N_eff ≈ 3.4 (range 3.1–4.8) once correlated and
> non-authentic outputs are discounted (design-effect DEFF = 1+(m−1)ρ; minimum detectable
> effect Cohen's d ≈ 2.5). Its *landscape* findings (the 218-benchmark census) stand as
> descriptive facts about the published corpus. Where a statistic comes from the trials,
> this review flags it.

---

## 1. Where the constructs came from: cross-cultural psychology as the anchor layer

Almost every quantitative cultural-values benchmark in NLP borrows its ground truth from
a small set of pre-existing cross-cultural psychology instruments, and inherits their
assumptions wholesale. Four anchor families dominate.

**Survey batteries (WVS, PEW, GlobalOpinionQA).** The World Values Survey and Pew Global
Attitudes surveys are the field's default "human distribution." A model's cultural
alignment is typically operationalized as the correlation between its answers to survey
items and a nation's aggregate responses. This is the frame behind GlobalOpinionQA
[2023-Durmus; 2025-Durmus], the WVS-correlation studies [2023-Ramezani; 2025-Sukiennik;
2025-Mohammadi-Exploring Cultural Variations], and EvalMORAAL [2025-Mohammadi-EvalMORAAL].
The dependence is total: when the anchor survey covers rich Western nations densely and
the Global South sparsely, the benchmark inherits that sampling geometry as a ceiling.

**Moral Foundations Theory (MFT).** Haidt's five/six-foundation taxonomy (care, fairness,
loyalty, authority, sanctity, plus liberty) supplies the item bank for a large family of
probes: MFQ/MFQ-2 questionnaire administration [2025-Haslett], MFT-vignette testing across
21 models [2024-Kirgis], the Moral Foundations Dictionary applied to LLM output
[2025-Jotautaite], and the Moral Foundations Twitter Corpus [2020-Hoover]. MFT's structure
is itself a WEIRD artifact — the individualizing/binding split was validated primarily on
American samples — which is why LLMs score so cleanly on it and so uniformly toward the
"individualizing" pole.

**The Moral Machine cluster geography.** The Moral Machine experiment collected ~40M
trolley-style decisions across 233 countries and induced three cultural clusters (Western,
Eastern, Southern) [2018-Awad; 2020-Awad-Universals]. This became a values anchor for LLMs
via replication studies [2024-Takemoto; 2025-Zaim Bin Ahmad], which report a wide AMCE
spread across models and (for Ahmad) a *negative* size↔human-alignment correlation ρ=−0.54.
The construct also imports the Moral Machine's known limitations: forced binary choice,
sacrificial-dilemma framing, and a preference geometry that may not generalize past
autonomous-vehicle scenarios.

**Hofstede / relational-mobility dimensions.** Hofstede's individualism–collectivism (IDV)
and related national-culture indices are used to score model "personality": GPT-4 scored
individualist (Hofstede IDV +1.21) and ERNIE collectivist (−0.89), each matching its origin
culture, p<0.001 [2025-Fenech-Borg]. Relational-mobility and tightness–looseness constructs
appear as secondary theory in relational-context benchmarks. These dimensional scores are
attractive because they are single numbers, but they compress within-nation variance that
later turns out to be the dominant signal (see §2).

**How NLP inherited the baggage.** The literature imported not just the instruments but
their epistemology: (i) a single "gold" national answer per item, so 97.1% of 105
cultural-alignment datasets are "majority-focused," collapsing a distribution to one label
[2025-team-Diverse Perspectives]; (ii) etic (outside-imposed) dimensions treated as
universal axes; and (iii) English-first item authoring. The **WEIRD critique** (Henrich et
al.) — that behavioral-science findings drawn from Western, Educated, Industrialized, Rich,
Democratic samples do not generalize — was the intellectual warning that NLP largely
ignored at construction time and then rediscovered empirically in its own systems. The
Cultural-Global corpus quantifies the inheritance: 55.5% of benchmark creators are in North
America + Western Europe, and the scholarship corpus has mean WEIRD score 64.5/100 with
59.7% High-WEIRD papers [cultural-digest §3].

---

## 2. The WEIRD-default findings: the most-replicated result in the field

The single most-replicated empirical finding across every probe type is that **LLMs default
to a WEIRD / American / liberal-individualist moral profile regardless of prompt language,
persona, or model origin.** Five load-bearing results anchor it.

**Origin does not rescue you (Haslett).** All 20 US- and China-made LLMs answered MFQ-2/WVS
items more like Americans than like Chinese respondents; participant-nationality dominated
(β=−.30) while model-origin was negligible (β=.03) [2025-Haslett]. A Chinese training
provenance does not produce Chinese-aligned values.

**Language is not culture (Durmus).** Prompting GlobalOpinionQA in Russian, Chinese, or
Turkish does **not** shift a model's answers toward those language communities; defaults
resemble the USA/Canada/Australia/Western Europe [2023-Durmus; 2025-Durmus]. This directly
falsifies the convenient assumption — built into CultureLLM, UniVaR, and Fenech-Borg
[2024-Xie; 2024-Cahyawijaya; 2025-Fenech-Borg] — that language can proxy for culture. The
corpus is genuinely split on this (see §6), but Durmus's null is the cleanest single test.

**Data volume, not scale, drives alignment (Sukiennik).** Web-content-percentage-per-country
correlates with cultural alignment at **r=0.94**, GDP at r=0.81, but log model size at only
**r=0.13**; GLM-4 (9B) aligns best despite near-lowest size [2025-Sukiennik]. Alignment is
a data-availability phenomenon, which means scaling the model will not close the gap —
only changing the training distribution will.

**Variance compression (Benkler).** text-davinci-003 explains US WVS variance at R²=0.80 but
Japan at 0.08 and Nigeria at 0.01 [2023-Benkler]. The model has effectively learned one
population's value structure and applies it everywhere; non-Western populations are near
noise. Relatedly the best frontier models correlate WVS r≈0.50 / PEW r≈0.62 overall, but
Western-Europe alignment (WVS r=0.52) is roughly **threefold** Sub-Saharan Africa (r=0.18)
[2025-Mohammadi-Exploring Cultural Variations]; EvalMORAAL shows Western r=0.82 vs
non-Western r=0.61 [2025-Mohammadi-EvalMORAAL].

**Capability and RLHF widen the gap.** Divergence from human MFT baselines *increases* with
model capability [2024-Kirgis], and RLHF moved models *farther* from human distributions,
not closer [2024-Abdulhai]. This is the most important trend for a benchmark designer: the
default post-training pipeline is actively anti-pluralist, so the phenomenon a new benchmark
must detect is getting stronger over time, not weaker. Models also carry a measurable
"cultural gene" from origin (the Fenech-Borg IDV result), but it is a weak perturbation on
a dominant American baseline.

Corroborating the trials layer (descriptive only, N_eff≈3.4): Claude Opus 4.6 clustered
closest to Germany (0.538) and farthest from Saudi Arabia (1.974), a 3.7-fold spread, with
an MFQ individualizing:binding ratio of 3.75 — 2.7× more extreme than the most liberal
documented human population (I:B ≈ 1.4) and 4.4× the non-WEIRD baseline (0.86)
[cultural-digest §3, Study 3]. Western-liberal resolution occurred in 100% (40/40) of
value-conflict scenarios. These numbers illustrate the phenomenon vividly but cannot support
between-model inference.

---

## 3. Localization methodology: the evolution from translation to survey-grounding

The field's methodological history is a ladder from cheap, invalid translation toward
expensive, valid native construction. Understanding the ladder is essential because most
published benchmarks sit on its lower rungs, and a new benchmark's credibility is largely
determined by which rung it targets.

**Raw machine translation (invalid for value items).** MT imports the *source* culture's
norms into the target-language benchmark. Machine-translated CrowS-Pairs carries US framing
into Thai (mBERT's worst-bias 90.69 is partly a translation artifact) [2025-Zhou]; naive
NLLB translation destroyed BBQ's gender-neutrality, requiring 15 hours of manual repair and
expanding 50→167 templates [2025-Satheesh-GG-BBQ]; a single translation error recast China's
"leading center" as "domination" [2025-ÓhÉigeartaigh]; Bengali translation retained only
24–31% of the original bias signal [2026-Reaj]. Translation error is not noise — it
systematically voids the construct, especially in gendered and morphologically rich
languages.

**Transcreation.** RTP-LX argues that culturally-grounded evaluation requires *transcreation*
— re-grounding referents, not translating words (George Washington → Toussaint Louverture)
[2024-Wynter]. Demonstration-based translation that preserves cultural function was preferred
by 80% of annotators in Histoires Morales [2025-Leteno].

**Translate-filter-modify.** IndiBias operationalizes a middle path: translate, then drop
non-applicable categories, swap US→Indian names, and *add* locally-salient axes (caste,
region) [2024-Sahoo]. Dutch CrowS-Pairs similarly swapped "Mexican"→"Moroccan" and
dollars→euros [2025-Satheesh]. The key move is additive — importing the source benchmark's
structure but grafting on axes the source culture lacks.

**Native authoring.** SHADES is the reference template: 304 stereotypes across 37 regions and
16 languages, authored by 43 native speakers, each item tagged with per-region cultural
validity so models are scored only on locally-valid items, with morphology-aware slot
templates [2025-Al-SHADES]. BengaliMoralBench hand-authored 3,000 scenarios, using
hand-authoring simultaneously as contamination control [2025-Kumar]. Native authoring solves
the norm-import problem but is labor-intensive and still lacks a distributional ground truth.

**Survey-grounded native (current gold standard).** KoBBQ validated every stereotype and
target with a 100-person Korean survey, included a "no stereotype exists" opt-out and a human
solvability gate, and demonstrated that machine-translated mtBBQ gives *statistically
different* bias readings from the survey-grounded version [2024-Jin-KoBBQ]. KorNAT built its
ground truth from a national survey, reporting an empirical survey-vote-agreement ceiling of
only 0.450 (best model 0.331) that reflects genuine within-population disagreement
[2024-Lee], and passed a government data-quality audit. This rung couples native authoring
with a *population distribution* as the target, and reports the ceiling honestly.

**The cross-script / code-mixed / transliteration frontier.** Orthogonal to the localization
ladder is a fragility that no amount of native authoring fixes: performance collapses on
non-canonical script. Zero-shot Bengali → Romanized-Bengali detection drops Macro-F1
0.80→0.39 (~50% relative) despite identical semantics [2022-Das]; code-mixed Dravidian
span-ID tops out at F1≈0.40 with 85.55% OOV [2021-Ravikiran; 2021-Saha]; transliterated
Bangla needs translation-based prompting for a mere +8% F1 [2025-Ishmam]; SweEval's
transliterated Indic prompts reach 0.92 harmful-compliance vs 0.19 in English
[2025-Kumar-SweEval]; Urdu collapses transformer F1 to 0.36–0.50 [2025-Usmana]; and tokenizer
coverage is load-bearing (poor WordPiece drops Assamese 16pp below Bodo [2024-with.pdf-NEIHS]).
This is the highest-headroom, most-underserved surface in the entire field, and it interacts
with safety: transliteration is a live jailbreak vector.

---

## 4. State of the art: the 218-benchmark landscape

The Cultural-Global meta-evaluation is the most systematic census of the field to date: 218
benchmarks scored against a 96-feature taxonomy across 13 dimensions, ranked by TOPSIS with
ELECTRE III veto thresholds and hierarchically clustered [cultural-digest §1–2]. Its
findings define the current frontier and, more importantly, the shape of the unclaimed
design space. All numbers below are descriptive facts about the published corpus.

**Zero measurement invariance.** Of 218 benchmarks, **precisely 0** report measurement
invariance testing — the psychometric prerequisite for any valid cross-cultural score
comparison [cultural-digest §3 finding 1]. Without configural/metric/scalar invariance, a
"fairness = 3" response means different things to Western, Confucian, and Ubuntu respondents,
and every cross-cultural leaderboard in the field is, strictly, semantically incoherent.
This is the single most consequential gap and the largest single differentiation opportunity:
the first benchmark to ship a proper MGCFA invariance pipeline has no precedent to beat.

**6.8% concept coverage.** Of 44 moral concepts mapped across 7 non-Western traditions, only
**3/44 (6.8%)** have any operational benchmark measure: *ren* (仁), *li* (禮), and *ubuntu*.
Five traditions have **zero** measured concepts — Islamic (0/7), Dharmic (0/6), Buddhist
(0/6), Indigenous/Relational (0/6), Buen Vivir (0/5) — with Confucian at 2/9 and Ubuntu at
1/5 [cultural-digest §3 finding 2–3]. The evaluation infrastructure is blind to the vast
majority of the world's named moral vocabulary.

**Two-cluster bifurcation and the <7% intersection.** Hierarchical clustering (Gower
distance, Ward linkage, silhouette 0.221 — "moderate" separation) splits the field into
Cluster 1 "Non-Western Focused" (n=47, 21.9%; mean NW-framework count 0.915, indigenous
inclusion 0.277, but low LLM administrability) and Cluster 2 "LLM-Ready" (n=168, 78.1%;
administrability 0.952, data availability 2.095, but NW-framework 0.012 and zero indigenous
content) [cultural-digest §3 finding 4]. The intersection of culturally-substantive **and**
LLM-administrable is **≈15 benchmarks (<7%)**. This intersection is the entire design target
for a new benchmark: depth-without-administrability cannot evaluate a model, and
administrability-without-content is culturally monochrome.

**TOPSIS top tier and the Pareto frontier.** The top-ranked instrument, Ray's Indigenous
Knowledge Systems benchmark (Māori & Navajo governance), scores TOPSIS 0.6374 with perfect
rank stability [1,1,1,1,1] — yet has **zero LLM administrability and zero data availability**
[cultural-digest §5]. It is the most culturally substantive instrument in the field and
cannot currently evaluate a language model. The rest of the top 15 (CVC #2 0.5968, CMoralEval
#3 0.5691, EMoTES-3K #4 0.5685, Islamic RAG #5, CCD-Bench #6, IslamTrust #7/#8, NormAd
#9/#10) are the field's best-balanced instruments, but a 7-benchmark Pareto frontier (NormAd,
CCD-Bench, EMoTES-3K, MITRA-zh-eval, Neira-Davila, HBC, Ray) confirms **no single benchmark
dominates all four axes** (scope, psychometrics, data availability, NW-framework count):
cultural depth and practical usability are negatively correlated. The TOPSIS ranking is
robust — Kendall's W = 0.9242 across six weight schemes — so the trade-off is not a weighting
artifact.

**Geographic concentration and participatory-design void.** Creator geography: North America
39.4%, East Asia 19.3%, Western Europe 16.1% — NA+WEU together **55.5%**; Sub-Saharan Africa
0.9% (2 benchmarks), Latin America 1.4% (3). Strikingly, **52.3% of benchmarks focused on
non-Western values are created by Western institutions** (90 of 172). Only **15/218 (6.9%)**
show any community participatory design; 93.1% were built without systematic consultation
with the cultures being measured; **0** Indigenous benchmarks are CARE-compliant; ecological
scope appears in 2 papers (0.9%) and intergenerational scope in 0 papers (0.0%)
[cultural-digest §3 findings 7–9].

**Scaling without diversifying.** Benchmark production rose tenfold in two years (12 in 2023
→ 129 in 2025), but cross-cultural instruments' proportional share *declined* from 25% to
17.8% [cultural-digest §3 finding 6], and reliability reporting is *inversely* related to
cultural ambition (bicultural 39.3% vs multicultural 18.7%) [finding 5]. The field is
getting bigger and more monocultural at once.

---

## 5. Non-Western frameworks in the literature

A parallel literature names the value dimensions the mainstream benchmarks miss. It is rich
in rubrics and poor in scored items.

**The named dimensions.** Ubuntu relational personhood, "I am because we are"
[2020-van Norren; 2024-Mokoena]; Confucian *ren* / *xiao* / *li* / *yi* role-ethics
[2024-So]; Afro-relational bidirectional trust [2025-Amugongo]; Andean *ayni* reciprocity
[2025-Maldonado]; Māori Kaitiakitanga and Navajo Hózhó [2025-Ray]; Daoist *wu-wei*
[2021-DaoistAI]; Dharmic *sādharaṇa*-vs-*viśeṣa* (general vs role-specific) harm
[2024-Varshney]. A pointed methodological observation from this literature: standard
worst-case red-teaming itself *violates* Hózhó, which centers restoration of harmony rather
than adversarial extremes [2025-Ray] — the evaluation paradigm is not culturally neutral.

**Operationalization attempts.** A handful of benchmarks encode culture-native constructs as
first-class dimensions rather than translating them away: FLAMES encodes Chinese
harmony/benevolence/courtesy/Doctrine-of-the-Mean [2023-Huang]; CMoralEval builds a
Confucian-plus-modern taxonomy [2024-Yu]; C-VARC grounds 257,609 rules in China's core
socialist values [2025-Wu]; IslamTrust maps each category to an Islamic guideline and
evaluates alignment across the five *maqāṣid* as a structured jurisprudential framework
[2025-Lahmar]; UbuntuGuard operationalizes Ubuntu as a policy-evaluation framework
[2026-Eickhoff]. MedES shows structured atomic-rule grounding can beat scale (an aligned 7B
composite 0.9356 vs deepseek-r1-671B 0.8103, grounded in 1,278 atomic rules [2026-Jin-MedES]).

**The knowledge-about vs reasoning-within gap.** The trials layer's sharpest result (again
descriptive, N_eff≈3.4): on 37 of 40 items (**92.5%**), the model described a tradition
accurately while being unable to reason *within* it [cultural-digest §3 finding 12]. The
top-ranked knowledge benchmarks share this ceiling by construction — CVC tests whether a
model *knows* Confucian concepts, not whether it reasons within Confucian relational ontology;
IslamTrust assesses *conformity* to Islamic positions, not the capacity to reason within
*uṣūl al-fiqh* that generate them [cultural-digest §5]. This is the reasoning-within frontier:
the construct that matters is almost entirely unmeasured.

**Liberal-compatibility filtering.** The mechanism behind the 100%-Western-default resolution
rate is selective: models score 3–4/5 on non-Western positions that happen to *converge* with
liberalism (Ubuntu care → welfare, *zakat* → redistribution, *ahimsa* → harm-reduction) and
0–1 on positions that *diverge* (Confucian filial loyalty overriding impartial justice,
Dharmic *svadharma* role-duties, complementarian inheritance) [cultural-digest §5]. A model
that appears "culturally competent" may simply be passing through a liberal-compatible subset
and silently reformatting the rest. Detecting this requires deliberately including divergent
items and penalizing silent Western-default resolution — recognition is not endorsement, and
the two must be probed separately (SpeciesismBench: models detect 86% of speciesist statements
but call only 34% wrong — "the problem is evaluative not epistemic" [2025-Jotautaite-Speciesism]).

**Caveat on the frameworks themselves.** Not all named dimensions are benchmark-ready. Ubuntu
is criticized as "too vague to operationalize," and only 1 of 5 African AI strategies even
references it [2025-Yilma]. A separate failure mode — the "NLP-on-texts false positive" — is
the largest single source of measurement error in tradition detection: a Chinese NLP benchmark
run *on* classical Chinese texts triggers the same keywords as a paper arguing *for* Confucian
role ethics, which is why keyword precision collapses to 0.167 for Buen Vivir and 0.333 for
Buddhist while Islamic-jurisprudence terms (*maqasid*/*fiqh*/*ijtihad*) reach precision 1.000
[cultural-digest §4]. Studying a tradition's corpus is not engaging its ethics.

---

## 6. Open problems

Six problems are genuinely unsolved and define the research frontier.

**The invariance pipeline.** Nobody has shipped configural → metric → scalar invariance
testing for a cross-cultural values benchmark (0/218). Until an item is shown to load on the
same latent construct across cultures, cross-cultural score comparison is uninterpretable.
This is a solved problem in psychometrics (MGCFA via `lavaan`/Mplus) that the NLP field has
simply not imported.

**Language–culture disentanglement.** The corpus is split on whether language proxies culture
at all — Durmus's null [2023-Durmus] and Tonneau's "English-from-Nigeria ≠ English-from-US"
[2024-Tonneau-Geographies] against CultureLLM/UniVaR/Fenech-Borg operationalizing culture *via*
language. There is no clean factorial design isolating language, script, nationality, and
religion as independent variables; the only partial attempts are Simplified/Traditional Chinese
pairs and paired XX-EN designs. The reasoning-language confound compounds this: reasoning-language
changes drive ~2× the cross-lingual instability of input-language changes (7.16pp vs 3.46pp YTA
shift on AITA), and 44% of models hide context-dependency invisible to single-dataset evaluation
[2025-Li-Untangling]. Cross-language *consistency* is a separate catastrophe from per-language
score: a model can be ~97% aligned per language yet only 44.74% consistent in which items it
passes [2024-Friedrich-M-ALERT].

**Communal and relational units of assessment.** Every mainstream benchmark asks "what should
the model do?", which imports an individualist unit of moral agency. Among deep-scored papers the
unit was "model" 50% / "LLM" 12.5% / "community" exactly **one** paper [cultural-digest §3 finding
9]. No instrument supports communal/deliberative units (Ubuntu *indaba* consensus, where the
deliberation *is* the moral act) or role-situated/relational-state evaluation (Confucian *wu lun*,
Dharmic *svadharma*, non-universalizable by design). Forced-choice formats strip exactly the
deliberative quality these traditions evaluate. Building process-scored, relationally-situated
evaluation is open territory.

**Ecological and intergenerational scope.** These moral dimensions are essentially absent (0.9%
and 0.0% of instruments), which blinds the infrastructure to Buen Vivir (*sumak kawsay*),
Indigenous land-based ethics, and Buddhist interdependence. The taxonomy already flags both as
scorable features; nobody scores them.

**Ground truth for genuinely contested values.** Distribution-matching (KorNAT, MULTITP,
Sorensen), single-expert/state answers (VC-LLM, LocalValueBench), and pluralistic multi-tradition
endorsement all have advocates, with no principled criterion for when each applies — and several
warn that equating population-or-state agreement with ethical truth commits the is-ought fallacy
[2022-Prabhakaran; 2023-Vida; 2025-Jiang]. Refusal semantics are a live sub-case: four incompatible
scoring stances exist (score 0/failure [2024-Meadows]; ideal [2025-Nawale]; excluded because a cold
refusal is itself harmful [2026-Shen]; first-class [2024-Lee]) with no selection rule. A benchmark
must *declare* whose values are the target and its descriptive-vs-normative grounding rather than
smuggle a contested stance (the HKGAI-V1 / VC-LLM "safe = law-compliant / same-ideology-judge"
anti-patterns show how easily this happens [2025-Han; 2026-Gao]).

**Durable vs patched cultural competence.** Fine-tuning shifts national alignment (NaVAB DPO; CLCA
KL 0.6011→0.5112) but injects the survey's own biases, and no card measures durable, un-gamed
cultural competence versus item-level patching [2025-Ju; 2025-Liu-CLCA]. Combined with thin
behavioral/enacted coverage (the stated-vs-enacted gap is documented mainly in English/Chinese) and
low-resource generative-quality confounds (models often "fail to provide meaningful answers" in
Arabic/Bengali/Hindi/Marathi, so compliance/refusal rates must be reported before any values claim
[2025-Al]), the field lacks any established way to show that a "culturally aligned" model is
anything more than a test-set-fitted one.

---

## 7. Annotated bibliography

Twenty-four keystone papers, grouped by the role they play for a benchmark designer.

**The WEIRD-default replication set**

1. **[2025-Haslett]** *Made-in-China Thinking in America.* 20 US/China LLMs answer MFQ-2/WVS more
   like Americans than Chinese; nationality β=−.30 dwarfs origin β=.03. The origin-does-not-help
   result.
2. **[2023-Durmus] / [2025-Durmus]** *GlobalOpinionQA.* Defaults resemble US/Canada/Australia/W-Europe;
   linguistic prompting does not shift toward the language's speakers. The language≠culture null.
3. **[2025-Sukiennik]** *Cultural Value Alignment in LLMs.* Web-content-per-country r=0.94, GDP r=0.81,
   log size r=0.13. Alignment is data-bound, not scale-bound.
4. **[2023-Benkler]** *LLMs for Moral Value Pluralism.* US WVS R²=0.80, Japan 0.08, Nigeria 0.01. The
   variance-compression result.
5. **[2025-Mohammadi-Exploring Cultural Variations] / [2025-Mohammadi-EvalMORAAL]** The threefold
   regional gradient (W-Europe r=0.52 vs Sub-Saharan Africa r=0.18; Western r=0.82 vs non-Western r=0.61).
6. **[2024-Kirgis]** *Differences in Moral Foundations of LLMs.* 21 models overvalue
   care/fairness/liberty, undervalue loyalty/authority/sanctity; divergence *grows* with capability.
7. **[2024-Abdulhai]** RLHF moved models *farther* from human moral distributions — the anti-pluralist
   post-training trend.

**Anchor constructs**

8. **[2018-Awad] / [2020-Awad-Universals]** *The Moral Machine experiment.* The three-cluster
   (Western/Eastern/Southern) geography that later LLM studies adopt as an anchor.
9. **[2025-Fenech-Borg]** Models carry a "cultural gene": GPT-4 individualist (Hofstede IDV +1.21),
   ERNIE collectivist (−0.89), p<0.001 — the origin-perturbation on the American baseline.
10. **[2020-Hoover]** *Moral Foundations Twitter Corpus* — the MFT operationalization that seeded a
    family of dictionary-based probes.

**Localization methodology (the ladder)**

11. **[2024-Jin-KoBBQ]** The survey-grounded gold standard: 100-person validation per stereotype,
    "no stereotype exists" opt-out, human solvability gate; mtBBQ gives statistically different readings.
12. **[2024-Lee]** *KorNAT.* National-survey ground truth with an honest SVA ceiling 0.450 (best model
    0.331); passed a government data-quality audit; refusal as first-class.
13. **[2025-Al-SHADES]** The native-authored multilingual template: 304 stereotypes, 37 regions, 16
    languages, 43 native speakers, per-item cultural-validity tags, morphology-aware slots.
14. **[2024-Wynter]** *RTP-LX.* The transcreation argument (George Washington → Toussaint Louverture)
    — re-ground referents, don't translate them.
15. **[2024-Sahoo]** *IndiBias.* The translate-filter-modify recipe; adds caste/region axes absent from
    the source.
16. **[2025-Satheesh-GG-BBQ]** Naive NLLB MT destroyed BBQ's gender-neutrality (15h repair, 50→167
    templates) — the concrete cost of raw MT for value items.
17. **[2022-Das]** Bengali→Romanized Macro-F1 0.80→0.39 — the canonical cross-script fragility datapoint.

**Bias-axis localization and validity design**

18. **[2022-Parrish]** *BBQ.* The psychometric gold standard (ambiguous/disambiguated ×
    negative/non-negative counterbalancing, human ceiling 99.7%, bias metric orthogonal to accuracy).
19. **[2024-Neplenbroek]** *MBBQ.* The cleanest bias-vs-competence separation via a parallel neutral
    control set.
20. **[2022-Shaily Bhatt]** Region and Caste are salient in India and absent from Western frameworks;
    American names *underestimate* real bias — the imported-axis failure.
21. **[2024-Tonneau-HateDay] / [2024-Tonneau-NaijaHate]** Ecological validity: representative sampling
    collapses average precision to 9.4% (vs 87.2% functional / 40% academic). Holdout F1 is a mirage.

**Non-Western operationalization and its limits**

22. **[2025-Ray]** *Indigenous Knowledge Systems (Māori & Navajo).* TOPSIS #1, most culturally
    substantive instrument; zero LLM administrability — and the observation that red-teaming violates Hózhó.
23. **[2025-Lahmar]** *IslamTrust.* Counter-hegemonic *maqāṣid*-structured evaluation; the exemplar of
    conformity-not-reasoning as a remaining flaw.
24. **[2024-Yu]** *CMoralEval.* Confucian-plus-modern taxonomy encoding culture-native constructs as
    first-class dimensions; most models near random 0.33.

**The census**

25. **Cultural-Global meta-evaluation** (`20260705-cultural-digest.md`). The 218-benchmark landscape:
    0/218 measurement invariance, 6.8% concept coverage, <7% substance×usability intersection, 55.5%
    NA+WEU creators, 6.9% participatory design, TOPSIS+ELECTRE ranking (Kendall W=0.9242), and the
    92.5% knowledge-vs-reasoning gap. Cross-model trial numbers are descriptive only (N_eff≈3.4).

---

*See `00-KNOWLEDGEBASE/11-cultural-linguistic-methods.md` for the prescriptive design checklist,
the localization ladder as an actionable recipe, and the design brief for the next benchmark.*
