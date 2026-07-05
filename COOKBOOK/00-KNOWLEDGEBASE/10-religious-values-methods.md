# 10 — Religious Values: Methods for Benchmarking

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-religious-values-dossier.md` (37 cards) + the completed Religious Values meta-evaluation
> (`20260705-digests/20260705-religious-digest.md`: 401 candidates × 22 features, 14 traditions,
> 45 gate-passers, 9-model trials). `[stem]` = evidence card. RV cross-vendor trial numbers carry
> disclosed caveats (same-vendor scorer, blinding asymmetry, Gemini backfill) — treat vendor
> comparisons as suggestive; structural findings stand.

---

## 1. The state of the field in five numbers (RV meta-eval, n=401)

1. **59.6%** of the 47 gate-passing benchmarks are Islamic (χ²=64.96, V=0.53, p<0.001); **8 of 14
   traditions have ZERO viable benchmarks** (Judaism, Jainism, Taoism, Shinto, Ubuntu, Indigenous,
   Baha'i, Zoroastrianism). The asymmetry is *infrastructure* (publication pipelines r=0.74;
   shared-task communities), not formalizability (r=0.41, n.s.) — the field's Islam advantage traces
   to the Quranic-QA shared-task community, not to Islam being uniquely benchmarkable.
2. **27.7%** of gate-passers test genuine theological *reasoning* rather than recall (p=0.0015).
3. **30.0/100** — mean values-relevance score of gate-passing benchmarks on a 24-dimension rubric
   (d=−1.23; 0 of 16 reach 75): the field's strongest instruments are knowledge tasks wearing values
   labels (the "ELQV paradox": the #1-ranked benchmark is emotion-annotation of Quranic verses —
   sophisticated knowledge extraction, not values reasoning).
4. **93.75%** of assessed benchmarks treat their target religion as a monolith — no denominational or
   school-level distinction (Hanafi vs Ja'fari; Catholic natural law vs Reformed covenantal) — which
   forfeits the values-alignment claim, since values vary as much within traditions as between.
5. **93.3 points** — the spread produced by the one genuinely discriminative instrument in the trials
   (Arabic *fara'id* inheritance-law MCQ: 6.7%→100%), vs a trimodal ceiling/floor pathology for every
   rubric-scored instrument (no model in the 0.2–0.8 band on any K/R/V dimension).

## 2. The construct decomposition (the field's core confusion, and the fix)

Religious-AI evaluation conflates three constructs with different deployment meanings. **Design them
as separately scored layers and never let one buy credit for another:**

1. **Knowledge recall** (verse ID, term recognition, doctrine facts) — easiest to build and auto-score,
   which is why the field over-produces it; saturates first; also the layer where "sounding religious"
   lives (religion-specific vocabulary attribution is "piecemeal and not grounded" [2024-Hovy];
   religious-text fine-tuning gains may be vocabulary, not values [2024-Songyuan Liu]).
2. **Theological reasoning** — applying tradition-specific *methods* (usul al-fiqh, natural-law
   casuistry, karma-yoga analysis, halakhic argument) to novel scenarios. Only 27.7% of instruments
   touch it. The universal K<R<V response-length gradient (V/K up to 9.2×) shows models treat these as
   different constructs even when rubric accuracy is at ceiling.
3. **Values/behavioral alignment** — reasoning *from within* rather than *about* a tradition; refusing
   to endorse prohibited acts; acknowledging intra-tradition scholarly disagreement; not defaulting to
   another tradition's sources [2025-Lahmar-IslamTrust]. Distinct again from **bias/stereotype
   measurement** (construct independence confirmed in trials, r≈0.29).

## 3. Empirical bias landscape (what a religious-values benchmark must be able to detect)

- **Anti-Islam bias is the most replicated finding** across mask-filling, completion, image generation,
  emotion attribution, and internal representations (SAE Violence Association Index highest for Islam
  in all 5 models probed [2025-Mahran]; one AI interaction shifts human attitudes −0.23 for Islam,
  +0.31 for Christianity in an n=1,005 RCT [2025-Zhang]).
- **Bias direction is language-dependent** — the model's "default religion" flips with elicitation
  language (Bengali errors redirect to Islam 79–89%; English bias is Christianity-dominant
  [2025-Hossain-BRAND]; Arabic amplifies, Russian neutralizes [2025-Demidova]). **Every item in ≥2
  languages/scripts, with per-language bias-direction reporting.**
- **High aggregate accuracy can encode a biased prior** — the "accuracy-bias coupling paradox": 99%
  general-norm accuracy with 0% correct Buddhist attribution [2025-Hossain]. Report per-tradition
  disaggregation + misclassification directionality, never aggregates.
- **Differential refusal is a stigmatization signal** (55.61% refusal on Jewish personas vs 0% GPT-4o
  [2024-Hovy]) but conflates over-caution with bias — score it as its own axis with the four-way
  refusal taxonomy (doc 01, Adjudication 3).
- **Faith is the least-saturated values dimension wherever measured** (Flourishing-AI Faith mean 35/100
  across 28 models — the floor dimension [2025-Hilliard]) — durable headroom for designers (doc 04 §2).

## 4. What discriminates (the T2 recipe) and what doesn't

The RV project's single discriminative instrument combined: **(a) domain specificity** (inheritance
law with multi-step computation — *radd*, *'awl*, share redistribution), **(b) liturgical-language
presentation** (Arabic, not translation), **(c) exact-match verifiable answers** (no rubric ambiguity),
**(d) graded difficulty** (Beginner/Advanced). Generalize: every scriptural tradition has analogous
computable subdomains (halakhic calendrics/kashrut ratios, karmic-consequence casuistry, canon-law
impediments) — **this recipe transfers**.

What failed: 5-point holistic rubrics (ceiling at ≥0.93 for all models; an 82-character answer scored
0.933 — keyword rewarding); response length as depth proxy (vendor-dependent); single-run,
no-IRR, arbitrary-threshold scoring [2025-Hilliard's design flaws]. Fixes: 10-point exemplar-anchored
rubrics with explicit adequate-vs-excellent discrimination; hybrid architecture (MCQ floor + anchored
rubric + cautious depth metrics); trial-validate every instrument on ≥1 model before release (feature
metadata alone missed a benchmark with literally zero religious content).

## 5. Tradition strategy (where to build, and how)

| Status | Traditions | The move |
|---|---|---|
| STRONG | Islam (28/47 gate-passers) | raise construct quality: reasoning + denominational awareness (4 madhabs + Shia jurisprudence), not more knowledge QA |
| MODERATE | Christianity, Hinduism, Buddhism | escape the flaws of their flagship instruments (English-translation processing instead of Sanskrit; hate-detection mislabeled as values) — source-language, method-application items |
| CRITICAL GAP (corpora exist, zero benchmarks) | **Judaism** (Sefaria, Responsa, Talmudic dialectics — the reserved DLG format code is pointed here), Jainism | community-coordination problem, solvable in ~2–3 years via the shared-task playbook (the mechanism that made Islam STRONG); first shared task is the hardest, investment front-loaded |
| VOID, textual | Taoism, Confucianism (Chinese Text Project), Zoroastrianism, Sikhism (GurbaniDB), Baha'i | same playbook; digital corpora await conversion |
| VOID, oral/communal | Ubuntu, Indigenous, Shinto (practice-based) | **different architecture required**: community-governed protocols, participatory/relational/narrative assessment under CARE-principle data sovereignty; accept non-public results as the cost of epistemic sovereignty; a moratorium on externally-led benchmarks may be warranted until community-governed alternatives exist (RV call-to-action 3) |

**Epistemic sovereignty rules** (dossier §E10 + digest L11): in-tradition experts author and validate
items (NATIVE > CONSULTED > EXTERNAL positionality, disclosed); sacred texts are not "just data" —
interpretive frameworks are tradition-internal; verify ethnographically that a value governs actual
practice before encoding it as an item [2020-Galanos]; locale-specific axes (Region/Caste for South
Asia [2022-Shaily Bhatt]); treat liturgical languages as first-class, not "low-resource."

## 6. Design brief for the next religious-values benchmark (grounds `20-DESIGNS/04`)

- **Three-layer scoring** (knowledge / reasoning / values-behavioral) reported disaggregated, with the
  reasoning layer built from tradition-internal *methods* applied to novel scenarios.
- **Denominational resolution from day one** — specify the evaluative standard per item; score
  "doctrinal flattening" as an error; reward "scholars differ" abstention on genuinely disputed
  questions [2025-Lahmar].
- **The T2 recipe per tradition** for frontier discrimination (computable subdomains, liturgical
  language, exact-match).
- **Language as a measured variable** (≥2 languages/scripts per item; per-language bias direction;
  default-to-majority contrastive probes; Specific-vs-General scope items [2025-Hossain]).
- **Geometric-mean aggregation with negative-weighted floors** so no dimension masks an anti-value one
  [2025-Hilliard]; capability coupling in the same run to expose alignment tax [2021-Barikeri-REDDITBIAS].
- **Indirect elicitation battery** (creative completion, forced-outcome debate, persona×event
  factorials, differential-refusal analysis) alongside direct items — avoiding probes so extreme they
  saturate [2024-Elrod; 2025-Demidova].
- **Multi-turn pastoral/advisory dialogue** as the values-behavioral layer (uncovered format; connects
  to doc 06) — e.g., advice-giving under a specified tradition with the advisee's tradition revealed
  mid-conversation.
- **Cross-vendor protocol hygiene** (matched administration, independent scoring, blind gold labels,
  provenance documentation — the four elements RV's own caveats mandate).
- **Psychometric gates**: IRR reported (best-practice range in corpus: κ 0.87–0.96), pilot calibration,
  multi-run variance, and a validated-instrument adaptation where possible (no religious benchmark has
  ever applied an adapted Schwartz/PVQ — an open first).

**Drill-down:** dossier §B (evidence table, 37 cards), §D (REDDITBIAS/IslamTrust/FAI/BRAND exemplars;
2024-AI anti-pattern). RV digest §7 (16 lessons), §8 (file pointers incl. the 401×22 feature matrix
JSON, PRISMA flow, and trial data).
