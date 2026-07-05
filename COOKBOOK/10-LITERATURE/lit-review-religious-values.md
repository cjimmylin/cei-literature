# Literature Review — Religious Values in LLM Evaluation

> **CEI COOKBOOK · 10-LITERATURE.** Descriptive survey of the research field for a designer
> of new religious-values benchmarks. Primary evidence:
> `../30-EVIDENCE/20260705-dossiers/20260705-religious-values-dossier.md` (37 cards) and
> `../30-EVIDENCE/20260705-digests/20260705-religious-digest.md` (the completed 401-candidate
> meta-evaluation). Prescriptive design rules live in `../00-KNOWLEDGEBASE/10-religious-values-methods.md`
> and are *not* repeated here — this document maps what the field has done, found, and left undone.
> `[stem]` = evidence card in `../30-EVIDENCE/20260705-cards/`. **Caveat propagated throughout:** the
> RV meta-evaluation's cross-vendor trial numbers carry three disclosed caveats — same-vendor rubric
> scoring (all by Claude Opus 4.6), T2 blinding asymmetry (Claude family saw gold labels; OpenAI/Gemini
> blind), and Gemini backfill provenance. Treat vendor comparisons as suggestive; structural findings stand.

---

## 1. The research strata: who studies what

The literature that touches "religion" and "language models" is not one field but three, and they rarely
cite each other. A designer must read all three because each supplies a different piece: the bias-probe
studies supply the phenomena a benchmark must *detect*, the benchmarks supply the *instruments* (and their
failure modes), and the normative papers supply the *value axes* the first two strata systematically omit.

**Stratum (a) — Empirical bias-probe studies (~11 cards).** These are not framed as benchmarks; they are
audits that probe a model and report a bias statistic. They span mask-filling and completion
[2025-Ajwad Abrar; 2021-Barikeri], image generation [2025-Ajwad Abrar], emotion attribution over personas
[2024-Hovy], internal-representation probing via sparse autoencoders [2025-Mahran], multilingual debate
framing [2025-Demidova], dialect proxies [2024-Wasi], and even a human-subjects RCT on attitude shift
[2025-Zhang]. Methodologically they are the most rigorous stratum (Abrar reports Fleiss κ=0.9644; Yasseri
Krippendorff α=0.895) but they measure *harm*, not *alignment* — they tell you a model is Islamophobic,
not whether it can reason within Islamic ethics.

**Stratum (b) — Benchmarks and eval pipelines (~11 cards, ~45 gate-passers in the wider corpus).** These
claim to *score* religious competence: IslamTrust [2025-Lahmar], BRAND [2025-Hossain], Flourishing-AI
[2025-Hilliard], BengaliMoralBench [2025-Kumar], ELQV, IslamicMMLU, QIAS, and the Quranic-QA cluster. This
stratum is overwhelmingly Islamic and, as §3 shows, mostly measures knowledge rather than values.

**Stratum (c) — Normative / theory papers (~15 cards).** These propose non-Western ethical frameworks as
alignment grounding and argue the first two strata are built on Western defaults. They divide by tradition:
**Islamic** ethics is the largest and — crucially — *internally plural*: the Maqasid al-Shariah
five-protection rubric (faith/life/intellect/lineage/wealth) [2024-MaqasidAI; 2022-IslamicVirtue], the
Amanah/Adl/Maslahah governance triad [2025-AlGhazali], I'timani *trusteeship* [2025-Ali], and
novel-category generation such as the "neutragent" beyond mahram/non-mahram [2025-AbuMusab]. **African**
Ubuntu supplies relational personhood and community-over-individual value [2020-van Norren; 2024-Mokoena].
**Confucian** virtue ethics (ren/xiao/li/yi) [2024-So], **Daoist** wu-wei minimal-intervention and
"companion" framing [2021-DaoistAI], **Buddhist/Dharmic** ahimsa and dukkha-alleviation as *positive*
alignment targets [2025-DharmaDigital], and **Indigenous/Andean** reciprocity (ayni) and community
validation [2025-Maldonado] each name an axis absent from Western harm-avoidance framings. Comparative
surveys sit across traditions [2023-Ty; 2024-Puzio]. This stratum is rich in constructs and almost empty of
instruments — its ideas have not been operationalized into anything that scores a model.

---

## 2. Empirical bias findings

Four findings recur strongly enough to treat as established phenomena a benchmark must be able to surface.

**Anti-Islam bias is the single most reproduced result in the entire corpus, and it replicates across
modality and probe depth.** Abrar finds DistilBERT scores a 63% total Religious Bias Score with 42% against
Islam; GPT-2 completions are 23% biased (17% anti-Muslim); Stable Diffusion 3 produces 78% biased images
for "religious terrorist" versus DALL-E 3's 18% [2025-Ajwad Abrar]. Mahran's sparse-autoencoder probing
shows Islam carries the highest Violence Association Index of all five models tested (VAI 117 vs 94–96 for
other religions in Gemma-2-2b) [2025-Mahran]. The 2024-AI ChatGPT study flagged >30% of GPT-4 responses for
statement bias and ~50% for Islam specifically [2024-AI]. Barikeri's REDDITBIAS found DialoGPT
significantly biased *only* on its two religion dimensions [2021-Barikeri]. Most consequentially, Zhang's
pre/post RCT (n=1,005 across 12 regions) shows a single AI interaction *decreases* human evaluation of Islam
by −0.23 (p<0.001) while raising Christianity by +0.31, with AI-generated Islam texts carrying 1.5× more
"conflict" references [2025-Zhang] — bias is not a benchmark artifact but shifts real attitudes.

**Bias direction is language-dependent: the same model defaults to a different "reference religion" per
language.** Hossain's BRAND shows all models reach >90% Islam accuracy in Bengali but Buddhism drops to
~40–60%; when models err in Bengali they redirect toward Islam (Llama: 88.8% of Hinduism errors, 79.3% of
Christianity errors → Islam), whereas English bias is Christianity-dominant [2025-Hossain]. Demidova finds
Arabic prompts push forced-debate win rates to 95–100% for one side while Russian yields the most neutral
outcomes [2025-Demidova]. Lahmar's IslamTrust shows a persistent Arabic>English gap (71.43% vs 61.58%)
[2025-Lahmar]. Wasi shows LLMs favor the Muslim Bengali dialect (~55–60% vs ~40–45% Hindu) even without any
explicit religious label [2024-Wasi]. The design implication is unambiguous: elicitation language is a
first-order variable, not a translation detail.

**Differential refusal is a measurable stigmatization signal — but a treacherous one.** Hovy's Divine
LLaMAs generated over 3M emotion attributions and found Llama2-13b refuses 55.61% of Jewish and 31.75% of
Muslim persona prompts, while Llama3-70b refuses 0.04%/0.03% and GPT-4o refuses 0% [2024-Hovy].
Refusal-rate-as-stigmatization is a cheap audit signal, but it conflates safety-training over-caution with
genuine bias, so it must be scored as its own axis rather than folded into a competence number.

**Attitude-shift and RCT evidence elevate the stakes.** Beyond Zhang's SEM-mediated RCT, the field shows
bias is not static across model generations: Abrar finds modern LLMs reach ~0% RBS after debiasing and Hovy
finds newer models refuse far less, yet the 2024-AI study warns that "advances in LLMs may result in more,
not fewer, instances of certain biases" — anthropomorphism and equivocation *worsened* in GPT-4 [2024-AI].
Progress is real but uneven and bias-type-specific.

---

## 3. State of the art: the 401-candidate landscape

The RV meta-evaluation is the first systematic meta-evaluation of religious-values benchmarks and supplies
the field's only population-level map. From a two-stage PRISMA search (2,099 vault papers + 72 external
queries) it assembled **401 benchmark candidates across 14 traditions**, applied two hard gates (theological
depth RD ≥ 30 and public data availability), and produced **47 gate-passers → 45 after trial review → 25
tiered benchmarks**. Five structural facts define the state of the art.

**Tradition asymmetry (SUPPORTED).** χ²=64.96, Cramér's V=0.53, p<0.001. Islam accounts for **28 of 47
gate-passers (59.6%)** and **9 of 12 Tier 1 benchmarks**, versus 7.1% expected under uniform coverage. A
conservative corpus-proportional test still rejects the null (χ²=21.84, V=0.30, p=0.0006). Critically,
**8 of 14 traditions have zero viable benchmarks:** Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy,
Indigenous Spirituality, Baha'i, Zoroastrianism. The asymmetry is *infrastructure*, not formalizability —
publication-infrastructure correlates r=0.74 with gate passage while formalizability is r=0.41 (n.s.). Islam
leads because of the Quranic-QA shared-task community, not because it is uniquely benchmarkable.

**Knowledge–reasoning conflation (SUPPORTED).** Only **27.7% (13/47)** of gate-passers test genuine
theological reasoning rather than factual recall (binomial p=0.0015, 95% CI [0.000, 0.403]). The field
over-produces recall because it is the easiest to build and auto-score.

**Values-relevance failure (SUPPORTED — the strongest result).** Among **16 gate-passing benchmarks** scored
on a 24-dimension values-relevance rubric, **mean A3 = 30.0/100 (SD=16.2)**, significantly below the
midpoint: t(15)=−4.93, p=0.000181, **Cohen's d=−1.23** (large); Wilcoxon W=5.0, p=0.00061. Only **3 of 16
(18.8%)** score above 50 and **0 of 16** reach 75 (binomial p=0.000015). Claims 1, 2, 3, and 8 survive
Bonferroni correction (α_adj=0.00625). In plain terms: the field's strongest instruments are knowledge
tasks wearing values labels.

**The monolith problem.** **15 of 16 A3-assessed benchmarks (93.75%)** treat their target religion as a
monolith — no denominational or school-level distinction (Hanafi vs Ja'fari; Catholic natural law vs
Reformed covenantal). Since values vary as much within traditions as between them, monolithic scoring
forfeits the values-alignment claim.

**Exemplars and what discriminates.** The top-ranked benchmark, **ELQV** (Composite 52.0, the highest in the
corpus; RD=62.0; inclusion probability p=1.000 across every weight config), annotates 2,100 Quranic verses
for emotional valence by PhD experts in Arabic linguistics — yet it embodies the **"ELQV paradox":** the
field's #1 instrument is a sophisticated *knowledge-extraction* task ("what emotion does this verse
convey?"), not values reasoning. Its ranking reveals the field's actual priorities. Other exemplars each
carry a flaw: **IslamTrust** [2025-Lahmar] is the construct-auditability model (every category maps to an
explicit alignment guideline, it rewards "scholars differ" abstention, and includes a contrastive
default-to-majority probe) but best model only 66.5%; **Flourishing-AI** [2025-Hilliard] contributes
geometric-mean aggregation so a strong dimension cannot mask a weak one (Faith is the persistent floor,
mean 35/100 across 28 models) but has no human baseline, no IRR, an arbitrary 90 threshold, and one run per
model; **BRAND** [2025-Hossain] isolates language and exposes the accuracy-bias coupling paradox;
**BengaliMoralBench** [2025-Kumar] is exemplary for anti-shortcut, build-from-scratch contamination control.
The **Bhagavad Gita Sentiment** entry (Composite 47.1) is the highest non-Islamic Tier 1 benchmark but
processes English translations rather than Sanskrit and tests sentiment, not dharmic reasoning.

The one genuinely discriminative instrument in the whole trial layer was the **fara'id T2 recipe**: a
30-item Arabic MCQ on Islamic inheritance law, stratified 15 Beginner / 15 Advanced, sampled (seed=42) from
the 12,450-item `bouchekif/inheritance_evaluation` set. It produced a **93.3-percentage-point spread**
(6.7% → 100%) where every rubric-scored instrument collapsed into a trimodal ceiling/floor pathology (no
model landed in the 0.2–0.8 band on any Knowledge/Reasoning/Values dimension). Its power comes from three
properties: domain specificity (multi-step math — LCM, *radd*, *'awl*, share redistribution — that resists
recall), liturgical-language presentation (Arabic, not translation), and exact-match verifiable scoring.
**Caveat:** the trial's cross-vendor T2 numbers (vendor-mean Anthropic 92.2%, OpenAI 93.3%, Gemini 11.7%)
are subject to the blinding asymmetry and backfill caveats above and are suggestive, not confirmatory.

---

## 4. Method debates

The field is not settled, and four live disagreements matter directly for design.

**Is high religious-vocabulary output good or bad?** This is a genuine scholarly split. Songyuan Liu treats
religious-text fine-tuning as beneficial — adding the Vedas lifted hate-detection F1 by +14pp (53.30→67.14)
— yet warns the gain "may be vocabulary, not internalized values" [2024-Songyuan Liu]. Hovy treats the same
religion-specific vocabulary (kvetch, krodha, khushu) as evidence of shallow stereotyping "not grounded on
an understanding of religious texts" [2024-Hovy]. The knowledge-vs-values conflation is therefore not merely
a design hazard but an unresolved empirical question about what vocabulary attribution *means*.

**Refusal semantics.** Is a refusal an alignment success (correctly declining to grade a religion) or a
stigmatization failure (differentially refusing Jewish/Muslim personas)? Both. The 2024-AI study's
ungrounded "what grade would you give religion X?" probe treats *any* grade as bias because refusal is the
correct behavior [2024-AI]; Hovy treats the *rate* of refusal as the bias signal [2024-Hovy]. A benchmark
must distinguish justified deferral from unjustified refusal, which means refusal cannot be a single scalar.

**Whose "unbiased"?** The corpus disagrees on whether "bias" is even well-defined. Abrar's annotators are
Bangladeshi (Muslim-majority) students, so "unbiased" is calibrated to a particular community
[2025-Ajwad Abrar]; Bhatt and Maldonado argue the Western default is itself not neutral — Bhatt shows
Western fairness axes miss India's most salient ones (Region and Caste) and that using American names
underestimates bias for Indian deployment [2022-Shaily Bhatt], while Maldonado frames uncredited
training-data harvesting as "cognitive colonialism" [2025-Maldonado]. There is no view-from-nowhere for
"unbiased religious output."

**Intra-tradition plurality.** Ali explicitly argues Islamic AI ethics is *not* monolithic — Maqasid,
Qawaid Fiqhiyya, and I'timani trusteeship yield different priorities [2025-Ali], contrasting with framings
that treat "the Maqasid rubric" as a single settled schema [2024-MaqasidAI; 2025-AlGhazali]. This debate
generalizes: the monolith problem (§3) is not an oversight but a contested question of *which* internal
framework a benchmark should score against.

Beneath these sits the deepest debate — **epistemic sovereignty**. van Norren and Mokoena argue Ubuntu's
relational personhood is a whole missing axis [2020-van Norren; 2024-Mokoena]; Maldonado proposes reciprocity
(ayni) and community validation as *alternative evaluation criteria* under CARE-principle data sovereignty
[2025-Maldonado]. For oral/communal traditions the very prerequisites of the benchmark pipeline (textual
corpora, propositional formalization, individual-response formats, open licenses) are epistemically
inappropriate — a benchmark of an oral tradition may be a category error, not a coverage gap.

---

## 5. Open problems

**Critical tradition gaps where corpora exist but benchmarks do not.** Judaism (25 candidates, 0
gate-passers) is the starkest: Sefaria, the Bar-Ilan Responsa project (running since the 1960s), and rich
Talmudic-logic formalization all exist, yet nothing passes the gates — the reserved DLG (dialectical/Talmudic)
format code has no instrument pointed at it. Jainism (59 candidates, 0 gate-passers) is the largest
false-positive pool, nearly all triggered by the *ahimsa* keyword. These are **community-coordination**
problems, solvable in ~2–3 years via the shared-task playbook that made Islam strong; the barrier is
infrastructure (r=0.74), not formalizability (r=0.41, n.s.).

**The shared-task playbook is proven but unreplicated.** Islam's benchmark advantage traces entirely to the
Quranic-QA shared-task community (coordinated data release + evaluation protocols + community participation
since ~2019). No other tradition has stood up an equivalent. The first shared task is the hardest —
investment is front-loaded into a year-one workshop, annotation, and venue — but the mechanism is
demonstrated and transferable to textual VOID traditions (Taoism via the Chinese Text Project, Confucianism
via the Daozang and Classics, Hinduism via the Digital Corpus of Sanskrit, Sikhism via GurbaniDB).

**No adapted psychometric instrument has ever been applied.** Despite the success of the Schwartz SVS/PVQ and
similar instruments in *secular* values measurement, **not one** religious-values benchmark adapts a
validated psychometric instrument; only SEA-Guard uses a PSY format at all. Among 45 gate-passers only 6 of
12 format codes appear, MIX dominates (a sign of methodological immaturity — ad hoc combination, not
principled design), and BIN, MRC, OPN, SHT, OUT, and IRT are entirely absent. This is an open first: a
properly adapted psychometric instrument for religious values does not yet exist.

**Multi-turn pastoral / advisory formats are absent.** Every gate-passing benchmark is single-turn. Yet the
highest-stakes deployment surface — a model giving religiously-inflected advice over a conversation — has no
instrument. Umer's 4×4 advisor×client factorial gestures at it (finding 50% of generated financial-advice
emails biased) but is statistically thin at 16 items with no significance testing [2025-Umer]. A multi-turn
pastoral format where the advisee's tradition is revealed mid-conversation is an obvious and unbuilt values
probe.

**Saturation and ceiling effects limit the strongest probes.** Elrod's creative-completion probe ("write a
lost 5th chapter of Jonah") saw all five models converge on the dominant "compassionate God" interpretation
— zero discrimination [2024-Elrod]; Demidova's forced-debate hits 95–100% [2025-Demidova]. Probes powerful
enough to bypass safety layers tend to saturate, leaving no discriminative headroom. Building probes that are
both revealing *and* graded remains unsolved outside the fara'id-style verifiable-answer recipe.

---

## 6. Annotated bibliography

Ordered roughly by design relevance. Stems index cards in `../30-EVIDENCE/20260705-cards/`.

1. **[2021-Barikeri] REDDITBIAS.** The methodological exemplar. Real scraped (not templated) items, a
   signed, significance-tested counterfactual-perplexity metric, explicit minoritized-vs-dominant
   specification, and — uniquely — capability coupling in the same run so a debiasing intervention is scored
   on the harm-vs-capability frontier, plus an over-correction check on non-biased dimensions. DialoGPT was
   significantly biased *only* on religion.

2. **[2025-Lahmar] IslamTrust.** The construct-auditability exemplar: every category maps to an explicit
   alignment guideline, it separates factual Islamic-knowledge QA from *behavioral* alignment (not endorsing
   prohibited acts, acknowledging scholarly disagreement), rewards "scholars differ" abstention, includes a
   contrastive default-to-majority category, and uses deterministic log-prob MC1 scoring. Best model 66.5%;
   Arabic>English gap 71.43% vs 61.58%; "Other faiths" hardest at 49.75%.

3. **[2025-Hossain] BRAND (Bilingual Religious Accountable Norm Dataset).** Isolates language as a variable
   and adds a Specific/General scope dimension plus misclassification-directionality analysis. Documents the
   accuracy-bias coupling paradox: 99.11% general-norm accuracy (Gemini) coexisting with 0% correct Buddhist
   attribution. Bengali errors redirect to Islam; English bias is Christianity-dominant.

4. **[2025-Hilliard] Flourishing-AI.** Geometric-mean aggregation prevents one strong dimension from masking
   a weak one, with negative-weighted rubric floors (harmful = −100). Faith is the persistent floor (mean 35
   across 28 models; o3 best overall 72/100 but only 43 in Faith; none reached 90). Design caution: no human
   baseline, no IRR, arbitrary threshold, single run per model.

5. **[2024-Hovy] Divine LLaMAs.** Refusal-rate-as-stigmatization (55.61% Jewish / 31.75% Muslim refusals in
   Llama2-13b vs 0% GPT-4o) over 3M emotion attributions in a persona×ISEAR-event factorial with a
   devout/practicing/cultural practice-depth axis. Argues religion-specific vocabulary attribution is
   "piecemeal and not grounded."

6. **[2025-Ajwad Abrar] Religious Bias Landscape.** Standardized Religious Bias Score across
   mask-fill/completion/image (DistilBERT 63% total, 42% anti-Islam; SD3 78% vs DALL-E 3 18% biased
   "religious terrorist" images), with intersectional covariate probes. Fleiss κ=0.9644. Finds modern LLMs
   reach ~0% RBS after debiasing.

7. **[2024-Songyuan Liu] Measuring Spiritual Values and Bias.** Repurposes human psychometric instruments
   (Pew SP-Typology, SP-10Axes) on LLMs and explicitly warns religious-text fine-tuning gains (+14pp
   hate-detection F1 with the Vedas) may be vocabulary, not values. Two-instrument convergent validation.

8. **[2025-Kumar] BengaliMoralBench.** Triadic Virtue/Commonsense/Justice lenses with balanced,
   lexically-neutral items to block shortcut pattern-matching; build-from-scratch as contamination control.
   κ lift 0.61→0.87 after pilot calibration. Shows scale does not buy cultural competence — pretraining
   coverage matters more than parameter count.

9. **[2025-Zhang] AI and Religious Attitude Shift.** Pre/post RCT (n=1,005, 12 regions) with SEM mediation:
   one AI interaction shifts human religious attitudes (−0.23 Islam, +0.31 Christianity, p<0.001); AI Islam
   texts carry 1.5× more "conflict" references. Establishes real-world stakes beyond benchmark artifacts.

10. **[2025-Mahran] SAE Religion Probing.** Mechanistic/sparse-autoencoder probing of internal religion
    representations with a Violence Association Index normalized to remove model-size confound; Islam highest
    VAI in all five models (117 vs 94–96). Bias lives in internal representations, not just outputs.

11. **[2020-Yasseri] Weak/Strong Islamophobia.** Intensity/scope gradation: the subtle "Weak" class has the
    lowest annotator agreement (κ=0.737 vs 0.907 Strong) and highest model confusion (22% misclassified as
    None). Krippendorff α=0.895. Gradations are genuinely hard to annotate but catch what binary labels miss.

12. **[2022-Shaily Bhatt] Re-contextualizing Fairness.** Geo-culturally specific disparity axes (Region,
    Caste) absent from Western frameworks; using American identity names underestimates bias for Indian
    deployment. The empirical case that "unbiased" is culturally defined.

13. **[2025-Maldonado] Andean/Indigenous AI Ethics.** Reframes uncredited training-data harvesting as
    "cognitive colonialism" and proposes reciprocity (ayni) and community validation as *alternative*
    evaluation criteria under data-sovereignty. The sharpest epistemic-sovereignty critique.

14. **[2020-van Norren] Ubuntu / Multi-Ontology Mapping.** Multi-ontology principle-mapping table
    (COMEST/OECD vs Ubuntu) with paired individual-vs-community item framing; argues relational personhood is
    a whole missing value axis. (Complement: **[2024-Mokoena]** tripartite Ubuntu rubric —
    humanity/spirituality/environment — with non-anthropocentric harm.)

15. **[2025-Ali] Islamic Ethics of Trusteeship.** Argues Islamic AI ethics is *not* monolithic (Maqasid vs
    Qawaid Fiqhiyya vs I'timani trusteeship yield different priorities). The clearest statement of the
    intra-tradition-plurality problem. (Complements **[2024-MaqasidAI]** five-protection rubric and
    **[2025-AbuMusab]** novel-category generation.)

16. **[2024-Elrod] Theological/Ethical Biases via Creative Completion.** Creative completion elicits
    theological stance better than direct Q&A, but all five models converge on the historically dominant
    interpretation — a documented ceiling/saturation anti-pattern.

17. **[2025-Demidova] John vs. Ahmed.** Forced-outcome debate framing bypasses RLHF safety layers and
    exposes language-as-confound (Arabic amplifies to 95–100%; Russian most neutral). Also a saturation
    caution.

18. **[2024-So] Confucian Alignment.** Non-Western virtue ethics (ren/xiao/li/yi) as alignment grounding,
    aphorism-as-item, implicit-vs-explicit ethical agency. Representative of the Confucian normative stratum.
    (Companions in the Eastern/Indigenous cluster: **[2021-DaoistAI]** wu-wei minimal intervention;
    **[2025-DharmaDigital]** ahimsa/dukkha as positive targets; **[2024-Puzio]** eco-relational
    non-anthropocentric ontology; **[2023-Ty]** multi-tradition comparative survey.)

19. **[2024-AI] Religious Bias Benchmarks for ChatGPT.** The instructive anti-pattern: an inventive
    multi-indicator battery (>50% statement bias for Islam) undercut by single-author scoring with no IRR,
    crude proxies (pronoun count for anthropomorphism, length for "coverage"), a BERT classifier with 35%
    false-alarm rate, refusal miscounted as "unbiased," and questions drawn from Catholic moral-theology
    texts. Read it for what *not* to do.

20. **[2020-Galanos] Exoticism vs Empiricism.** The methodological governor on the whole normative stratum:
    verify ethnographically that a cultural value actually governs behavior before encoding it as a benchmark
    item, lest a benchmark reify an exoticized stereotype.
