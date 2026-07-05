# Religious Values Benchmark Survey — Distilled Digest for Benchmark Designers

*Source: `RELIGIOUS-VALUES/PAPER-V3/` (v3, 2026-04-13) + feature matrix v2 (2026-04-04) + Section 2 lit review (`RELIGIOUS-VALUES/PAPER/`). This digest harvests the sub-project's own conclusions; it does not re-derive or second-guess them. All quantitative claims are copied verbatim from the source.*

---

## 1. Project scope & method

This sub-project is the **first systematic meta-evaluation of religious values benchmarks for LLMs** — a survey that asks not "how do models score on religious benchmarks" but "do the benchmarks that claim to assess religious values alignment actually test that construct?" The central diagnosis: dozens of benchmarks claim to evaluate religious content, but they conflate three distinct constructs — **religious values alignment, religious knowledge recall, and stereotype/bias detection** — with very different deployment implications.

**Corpus assembly (two-stage, PRISMA-documented).**
- **Stage 1 (internal):** Screened the CEI Literature Vault (2,099 AI ethics papers, 2019–2026), intersecting religious-values scores (`rv_* ≥ 50`) with benchmark/eval/dataset flags. Supplemented by a full-text scan of 2,459 PDF extracts using co-occurrence of 43 tradition-specific theological keywords (halakha, dharma, sutra, kami, Ubuntu, ahimsa…) with benchmark vocabulary, plus a YAML near-miss scan (`0 < max(rv_*) < 50`).
- **Stage 2 (external):** 72 English-language queries across Semantic Scholar, arXiv, HuggingFace (mean 5.1 queries/tradition), returning 70 discoveries → 53 ingested after dedup (16 false positives, 1 duplicate).
- **Result:** **401 benchmark candidates** spanning **14 religious/philosophical traditions**. (29 papers using religion only as a demographic bias variable were excluded from scoring but retained in the count.)

**Scoring.** Each candidate characterized along **22 features** on a **3-axis framework** (RD / PE / CI, Section 2), combined into a composite. **Two hard gates** applied before ranking: **RD ≥ 30** (minimum theological depth) and **public data availability**.

**PRISMA flow:** 2,099 vault papers → 401 candidates → 47 pass both gates → 2 removed post-review (Break the Checkbox: zero religious content confirmed by trial T4; BuddhismEval: HuggingFace HTTP 401) → **45 gate-passers** → **25 tiered benchmarks** (12 Tier 1, 3 Tier 2, 10 Tier 3) via bootstrap tier assignment.

**Ranking robustness:** bootstrap resampling (**1,000 iterations across 61 weight configurations**), Dirichlet-sampled weights centered on (0.40, 0.35, 0.25), α = 20; each benchmark assigned an inclusion probability *p*.

**Implementation trials (the empirical layer no prior religious-AI survey attempted):**
- **65-item construct validity battery** (15 Knowledge + 15 Reasoning + 25 Values + 10 Bias) across Islam, Christianity, Hinduism.
- **30-item Arabic MCQ** on Islamic inheritance law (*fara'id*), sampled (seed=42) from the 12,450-item `bouchekif/inheritance_evaluation` dataset, stratified 15 Beginner / 15 Advanced, 6 options (A–F), Arabic script.
- Administered to **9 models from 3 vendors** (Anthropic: Opus, Sonnet, Haiku; OpenAI: GPT-Codex, Codex-Mini; Google: Gemini 2.5 Flash-Lite/Flash/Pro, Gemini 3.1 Pro).
- **All 8 empirical claims subjected to formal statistical testing.**

**Three disclosed caveats (recur throughout):** (1) T2 blinding asymmetry — Claude-family T2 ran with gold labels visible (upper-bound estimates); OpenAI/Gemini blind. (2) Same-vendor scorer bias — all rubric scoring by Claude Opus 4.6, including Claude responses. (3) Gemini data provenance — backfilled template extraction, not interactive API.

---

## 2. Benchmark characterization framework (the reusable asset)

The **3-axis, 22-feature scoring framework** is the project's primary transferable artifact. Axis scores normalized to 0–100; **COMPOSITE = RD × 0.40 + PE × 0.35 + CI × 0.25**. Weight rationale: RD highest (40%) because the survey specifically evaluates *theological* depth; PE second (35%) because inaccessible data cannot be verified/replicated; CI lowest (25%) to avoid over-rewarding incumbency (73% of candidates are 2024–2026).

**Axis 1 — Religious/Theological Depth (RD).** Six weighted features; formula `RD = R2×25 + R6×20 + R1×15 + R3×15 + R5×15 + R4×10`:
- **R1 Tradition Count** (1–14, w15) — number of traditions evaluated.
- **R2 Theological Depth** (1–5 ordinal, **w25**, highest) — genuine engagement vs. surface mention. Calibrated against 3 anchors: IslamicMMLU (R2=4, fiqh-level, 4 madhabs) at the top; Break the Checkbox (R2=2, multi-religion MCQ, shallow) middle; general cultural surveys (R2=1) floor.
- **R3 Scriptural Grounding** (0–5, w15) — reliance on primary sacred texts; +1 source-language bonus for original liturgical language (Arabic, Sanskrit, Hebrew, Pali, Classical Chinese).
- **R4 Denominational Awareness** (0–3, w10) — Sunni/Shia, Catholic/Protestant, Theravada/Mahayana distinctions.
- **R5 Pluralistic Coverage** (0–5, w15) — multiple traditions on shared moral questions.
- **R6 Expert Validation** (0–5, **w20**, 2nd highest) — theologian/community-expert involvement; strongest available proxy for construct validity.

**Axis 2 — Practical Ease (PE).** Ten features (6 weighted, 4 informational); formula `PE = P7×30 + P3×25 + P9×15 + P10×10 + P5×10 + P4×10`:
- **P1 Task Format** (12-code taxonomy, unweighted), **P2 Dataset Size** (unweighted).
- **P3 Data Availability** (**w25**) — public repo access; the single largest reproducibility barrier.
- **P4 Code Availability** (w10), **P5 License Terms** (w10).
- **P7 Implementability** (0–10, **w30**, highest PE) — harness compatibility, docs, integration ease.
- **P8 Scorer Type** (unweighted), **P9 Model Compatibility** (w15, open+closed), **P10 Language Coverage** (w10, with liturgical-language normalization so Arabic/Sanskrit/Hebrew/Pali/Classical Chinese/Tibetan are not penalized as "low-resource").
- (P6 deliberately absent — skipped in design; numbering gap preserved.)

**Axis 3 — Citation Impact (CI).** Six features (2 unweighted); formula `CI = C2×30 + C4×25 + C3×20 + C6×15 + C5×10`:
- **C1 Raw Citations** (unweighted), **C2 Citations/Year** (**w30**, age-normalized).
- **C3 Venue Tier** (w20), **C4 Downstream Adoption** (**w25**, papers that *use* it, not merely cite), **C5 Leaderboard Presence** (w10), **C6 Community Engagement** (w15, shared tasks/workshops).

**12-code Task Format taxonomy (P1),** organized by harness compatibility: *High* — MCQ, MRC, BIN, SHT, TXT; *Medium* — SCN, PSY, MIX; *Low* — OPN, MTN, RAG, MUL. A 13th code (DLG, dialectical/Talmudic reasoning) is reserved for future use.

**Seven meta-evaluation criteria** (what numeric scoring can't capture): (1) Content Validity (theological reasoning vs. recall, from a 20-item sample), (2) Discriminative Power (ceiling ≥90% / floor <30%), (3) Cultural Authenticity (NATIVE / CONSULTED / EXTERNAL author positionality), (4) Reproducibility (5-item checklist: data, code, metrics, prompts, IAA), (5) Complementarity (1–5 unique dimensions added), (6) Construct Coverage (maps to: knowledge, reasoning, values, sensitivity, pluralism, contextualization), (7) Annotation Quality (expert theologian → author self-annotation).

**Six-dimension construct model** used in trials and rubrics: **Knowledge** (0/0.5/1.0), **Reasoning** (0–3), **Values** (0–5, reasoning *from within* vs. *about* a tradition), **Bias** (0–3, stereotype avoidance with nuance).

---

## 3. Key findings (quantitative claims copied exactly)

**Claim battery (Table 4).** Four claims supported, one marginal, three revised:

1. **Tradition asymmetry (SUPPORTED).** χ² = 64.96, Cramér's V = 0.53, p < 0.001. Islam accounts for **28 of 47 gate-passers (59.6%)** and **9 of 12 Tier 1 benchmarks**, vs. 7.1% expected under uniform. Conservative corpus-proportional test also rejects null (χ² = 21.84, V = 0.30, p = 0.0006). **8 of 14 traditions have zero viable benchmarks:** Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, Zoroastrianism.

2. **Knowledge–reasoning conflation (SUPPORTED).** Only **27.7% (13/47)** of gate-passers test genuine theological reasoning rather than factual recall; binomial p = 0.0015 (95% CI [0.000, 0.403]).

3. **Data availability bottleneck (SUPPORTED).** **170 of 401 candidates (42%)** have no publicly accessible evaluation data. The two gates together eliminate **354/401 (88.3%)**; the data gate alone eliminates **77%** of the corpus. Among 47 gate-passers, all 47 have accessible data (binomial p < 0.001 vs. 58% null). Data accessibility is the single strongest predictor of gate passage.

4. **Structural epistemic injustice (REVISED).** Logistic regression Pseudo-R² = 0.068; tradition family **not** significant (p = 0.112). English-language publication OR = 1.76 (p = 0.097); venue tier OR = 1.34 (p = 0.148). Revision: injustice operates through **publication infrastructure (r = 0.74)**, not the scoring framework. It is *pre-framework, not intra-framework*.

5. **Field recency (MARGINAL).** 28/47 gate-passers (59.6%) date from 2024+; binomial p = 0.121. Descriptively, **73% of all 401 candidates date from 2024–2026**; median year 2024 (bootstrap CI [2023, 2024]).

6. **WEIRD bias (REVISED — direction reversed).** Fisher's exact OR = 0.58, p = 0.090. **Non-WEIRD traditions pass at 14.4% (30/209) vs. WEIRD at 8.9% (17/192)** — reversal driven by Islamic dominance (Islam contributes 28 of 30 non-WEIRD gate-passers). The WEIRD/non-WEIRD dichotomy is too coarse to capture infrastructure-specific mechanisms.

7. **Bias–values conflation (REVISED).** Among 47 gate-passers: 10 bias-adjacent, 13 values-focused, 24 mixed. Binomial on the 23 pure-category (10 vs. 13): p = 0.678. Conceptually supported by construct independence in trials (Sonnet r = 0.288; both OpenAI models r < 0.30). Reframed as a **design-level** problem, not a population-level imbalance.

8. **Values relevance failure (SUPPORTED — STRONGEST RESULT).** Among **16 gate-passing benchmarks** on a 24-dimension values relevance rubric, **mean A3 = 30.0/100 (SD = 16.2)**, significantly below midpoint: t(15) = −4.93, p = 0.000181, **Cohen's d = −1.23** (large). Wilcoxon W = 5.0, p = 0.00061. Only **3 of 16 (18.8%)** score above 50; **0 of 16** reach 75 (binomial p = 0.000015). Bonferroni-adjusted threshold α_adj = 0.05/8 = 0.00625; Claims 1, 2, 3, 8 survive correction.

**Ranking findings.** Composite spread across all tiers = **12.1 points (52.0 to 39.9)**; leading normative-ethics benchmark scores 77.2 by comparison. Highest observed (ELQV, 52.0) = only 52% of the theoretical max of 100. Mean bootstrap CI width = **15.87 points** (covers 71.2% of the spread); mean Kendall's τ = 0.773 across 61 weight configs → tier structure stable, within-tier ordering provisional.

**Cross-model construct-validity findings (Claude family):**
- **Universal K < R < V response-length gradient** across all 9 model–tradition cells. Aggregate V/K ratios: Opus 3.41×, Sonnet 3.59×, Haiku 9.18× (gradient steepest for the weakest model). Highest single cell: Christianity-Haiku 13.91×.
- **Rubric ceiling effect.** All three Claude models score ≥ 0.93 on Knowledge/Reasoning/Values/Bias; Opus Values 0.933 is the sole sub-ceiling cell (3 deductions, all for shifting to an *external* analytical register). The rubric cannot distinguish Opus (T2 = 100%) from Haiku (T2 = 76.7%).
- **Bias–values independence.** Sonnet r = 0.288 (independent); Opus 0.706 and Haiku 0.701 are ceiling/extremes artifacts.
- **T2 Arabic MCQ discriminates:** Opus 100%, Sonnet 100%, Haiku 76.7% (Beginner 80% / Advanced 73.3%).

**Cross-vendor findings (9 models) — three behavioral modes:**
- **Mode 1, Differentiated Engagement (Claude):** gradient holds, rubric ≥ 0.93, T2 76.7–100%.
- **Mode 2, Compressed Accuracy (OpenAI Codex):** near-ceiling rubric (0.867–1.0) with responses **5–80× shorter** (K = 78–82 chars); GPT-Codex T2 100%, Codex-Mini 86.7%. GPT-Codex does not maintain the gradient.
- **Mode 3, Template Refusal (Gemini):** all four score **0.0 on Knowledge/Reasoning/Values** (nonzero only on Bias, 0.567–1.0); no gradient; T2 6.7–20% (at/below the 16.7% chance floor). Caveat: may be a backfill artifact.
- **T2 spread = 93.3 percentage points** (6.7% Gem-Pro → 100% Opus/Sonnet/GPT-Codex); vendor-mean T2: Anthropic 92.2%, OpenAI 93.3%, Gemini 11.7%. Rubric distribution is **trimodal** (ceiling/near-ceiling/floor) with **no model in the 0.2–0.8 range** on any K/R/V dimension — a measurement pathology.
- Anomalies: Codex-Mini reversed difficulty (Beginner 80% < Advanced 93.3%); Gemini Pro 0% on T2 Beginner (below chance).

**Structural predictors (Section 5.6):** publication infrastructure r = 0.74 (p < 0.01); community practice norms r = 0.58; **formalizability r = 0.41 (p > 0.05, NOT significant)** — contradicting the intuition that some traditions are inherently un-benchmarkable.

---

## 4. Scoring & validity methods that worked / that failed

**Worked:**
- **Hard gates as a decisive filter.** RD ≥ 30 + public data cut 88.3% of candidates and cleanly separated substantive from incidental engagement. The RD distribution is bimodal (mass at 15–25, gap before 30+), making 30 a natural break, not an arbitrary threshold.
- **Bootstrap tiering over point rankings.** Because the composite spread (12.1) is *smaller* than the mean CI width (15.87), a single ranking would be spurious. Inclusion-probability tiers (Robust p≥0.80 / Likely 0.30–0.80 / Contested 0.01–0.30) communicate real uncertainty.
- **The T2 Arabic MCQ** — the *only* genuinely discriminative instrument. Its power comes from three properties: **domain specificity** (fara'id requires specialized rules), **non-English presentation** (Arabic liturgical language), **exact-match scoring** (no rubric ambiguity). Advanced items require multi-step math (LCM, share redistribution, *radd*, *'awl*) that resists rule-recall.
- **Response length as a construct-differentiation signal** (K < R < V) — surfaced a distinction the rubric could not, since it appears even when accuracy is at ceiling.
- **Implementation trials as a complement to feature scoring** — trial T4 caught Break the Checkbox (Pew survey items via Hofstede dimensions, zero religious content; "Islam/Christianity" tags were country-demographic artifacts); the HTTP 401 check caught BuddhismEval. Feature-level scoring alone would have kept both.
- **R2 calibration anchors + floor-correction mechanisms.** After fixing an R2 bug that had assigned minimum depth to 85.3% of candidates, three mechanisms (classification-based floors, keyword count thresholds, title-match boosting) restored discrimination among the top 30% — precisely the gate-passers that matter.

**Failed / insufficient:**
- **Rubric-based accuracy scoring is non-discriminative at the frontier.** 5-point rubrics saturate; an 82-character Codex response scored 0.933, implying the rubric rewards **keyword presence**, not depth. In IRT terms, items had near-zero discrimination parameters.
- **Response length ≠ reasoning depth** — a proxy only; a verbose model could inflate length. Vendor-dependent (absent in Gemini, marginal in one OpenAI model), so not yet a universal construct signal.
- **Single-author scoring without inter-rater reliability** — the most consequential limitation. R2 and R6 use keyword heuristics, not expert theological judgment. Rankings should be treated as hypotheses; *structural* findings are more robust.
- **English-only external search** (72 queries, no Google Scholar/PapersWithCode, HuggingFace API returned zero) — 401 is a **lower bound**; non-English benchmarks (Hebrew, Classical Chinese, Sanskrit, Pali) undercounted.
- **Same-vendor scoring + T2 blinding asymmetry + Gemini backfill** — jointly make cross-vendor comparisons **suggestive, not confirmatory**. Claude results likely most favorable, Gemini least reliable.
- **12-code format taxonomy** — descriptive, not theoretically grounded; several benchmarks needed the MIX residual; no DLG code for dialectical reasoning.
- **Data availability is temporally unstable** — a snapshot, not permanent (BuddhismEval demonstrated this).

---

## 5. Exemplar benchmarks (top-ranked; what/why/flaws)

*(Composite/RD/PE/CI from the paper's Table 2 tiered ranking and feature matrix v2.)*

- **ELQV** (2025, Islam, RAG) — **Composite 52.0, highest in corpus; RD = 62.0 (highest); p = 1.000** (appears under every weight config). 2,100 Quranic verses annotated for emotional valence by PhD experts in Arabic linguistics/Islamic law; R3 = 5 (scriptural), R6 = 3 (expert). **Flaw — the "ELQV paradox":** it is fundamentally a **knowledge-extraction task** ("what emotion does this verse convey?"), *not* values reasoning. The field's top instrument is a sophisticated knowledge task; its ranking reveals current priorities. PE = 60.0 (RAG needs harness adaptation).

- **Domain-Specific LLMs (Islamic)** (2023, MIX) — Composite 50.4, p = 1.000. High practical ease (PE = 76.0).

- **AceGPT** (2023, Islam, MIX) — Composite 47.4, p = 0.999. Localized Arabic LLM evaluation; benefits from Arabic NLP infrastructure.

- **Religious Hate Speech Taxonomy** (2022, Islam, MIX) — Composite 46.8, p = 0.999.

- **Bhagavad Gita Sentiment** (2022, Hinduism, TXT) — Composite 47.1, p = 0.973; highest-scoring non-Islamic Tier 1 entry. **Flaw:** processes **English translations**, not the original Devanagari/Sanskrit; tests sentiment annotation, not ethical reasoning within *dharma*/*karma*/*guna* frameworks.

- **PapersPlease** (2025, Islam, SCN, Composite 45.4); **PRISM Alignment** (2025, Islam, MTN, 45.0); **Sometimes the Model doth Preach** (2025, Islam, MIX, 44.2); **HAQA and QUQA** (2023, Islam, MIX, 44.7) — the Quranic-QA-adjacent cluster that lifts Islam's PE via shared-task data-release norms.

- **Ancient Wisdom Modern Tools** (2025, Buddhism, RAG) — Composite 44.0, p = 0.901; leading Buddhist entry.

- **Antisemitism Detection** (2022, Christianity, MIX) — Composite 44.1, the **sole Christian Tier 1** entry. **Flaw:** it is a hate-speech *detection* (fairness) task, not values alignment.

- **Tier 2:** WYWEB (43.0) and C3Bench (42.9), both Buddhism via Classical Chinese; FaithBench (41.6, Christianity). **Tier 3 (10):** Quran-MD, Gospel Coalition (highest Christian RD = 54.3), IslamTrust, SinhalaMMLU, Islam QA, SEA-Guard (sole PSY format), DharmicData, GurbaniDB/BaniDB (2010, Sikhism — a scriptural *database*, not a purpose-built benchmark), etc.

**Cross-cutting flaw:** only **5 of 25 tiered benchmarks** demonstrate genuine theological depth (ELQV, Islamic Inheritance Law, QIAS 2025, Gospel Coalition, GurbaniDB/BaniDB). **15 of 16 A3-assessed benchmarks (93.75%) treat their target religion as a monolith** — no denomination/school distinction — undermining any values-alignment claim, since values vary as much within traditions as between them.

---

## 6. Gaps & voids identified

**Uncovered traditions (the 6/14 pattern — status classes: STRONG / MODERATE / WEAK / CRITICAL GAP / VOID):**
- STRONG: Islam (113 candidates, 28 gate-passers, 9 Tier 1).
- MODERATE: Christianity (117 / 6 / 1), Hinduism (43 / 5 / 1), Buddhism (31 / 3 / 1).
- WEAK: Sikhism (9 / 2 / 0), Confucianism (25 / 1 / 0).
- **CRITICAL GAP** (candidates exist, zero gate-passers): **Judaism (25 / 0)** — despite Bar-Ilan Responsa (1960s), Sefaria, Talmudic-logic formalization; **Jainism (59 / 0)** — largest false-positive pool, nearly all triggered by the *ahimsa* keyword.
- **VOID** (zero or near-zero candidates and zero gate-passers): Taoism (4 / 0), Shinto (2 / 0), Ubuntu Philosophy (5 / 0), Indigenous Spirituality (18 / 0), Zoroastrianism (4 / 0), **Baha'i (0 candidates — entirely invisible to the pipeline).**

*(Feature-matrix v2 raw tradition counts differ slightly from the paper's final numbers — e.g. Jainism 47, Hinduism 25, Buddhism 14, Judaism 9, Indigenous 16 — because the matrix is the pre-reclassification snapshot with an "Unknown" bucket of 30; the paper's Table 3 reflects manually verified assignments. Use the paper's Table 3 numbers, cited above, for reporting.)*

**Uncovered constructs:** genuine **theological reasoning** (only 27.7% of gate-passers); **values alignment** (mean A3 = 30.0/100; none ≥ 75); **denominational/intra-tradition diversity** (93.75% treat religion as monolith); **multi-turn pastoral dialogue**; **contextualization** to novel scenarios.

**Uncovered formats.** Among 45 gate-passers only 6 of 12 format codes appear; **MIX** dominates (methodological immaturity — ad hoc combination, not principled design). Absent: BIN, MRC, OPN, SHT, OUT, IRT. Notably, **no validated psychometric instrument** (adapted Schwartz SVS / PVQ) is applied to any religious values benchmark, despite success in secular values measurement; only SEA-Guard uses a PSY format.

**Uncovered languages** among gate-passers: Hebrew, Persian, Turkish, Urdu, Indonesian, Thai, Yoruba.

**Two distinct obstacle types (must not be conflated):** (a) **Community coordination problem** — textual traditions with digital corpora but no shared-task pipeline (Judaism/Sefaria, Confucianism/Daozang & Chinese Classics, Taoism, Hinduism/Sanskrit tools). Addressable in ~2–3 years with workshop investment. (b) **Structural epistemic exclusion** — oral/communal/practice-based traditions (Indigenous, Ubuntu, Shinto) where the pipeline's prerequisites (textual corpora, propositional formalization, individual-response formats, open licenses) are epistemically inappropriate, compounded by CARE-principle data sovereignty.

---

## 7. LESSONS FOR DESIGNING NEW BENCHMARKS (the payoff)

Each lesson is traced to the finding that supports it.

1. **Separate three constructs explicitly and report them disaggregated: knowledge recall ≠ bias/fairness ≠ values reasoning.** *(From the central thesis + Claim 8, mean A3 = 30.0/100, d = −1.23; §5.5.)* Most instruments claiming "religious values" actually test knowledge or bias. Design items that require reasoning *from within* a tradition's normative framework (0–5 Values rubric), and disaggregate scores so downstream consumers cannot mistake knowledge certification for reasoning competence.

2. **Prioritize reasoning items over recall items.** *(Claim 2: only 27.7% test reasoning, p = 0.0015; §5.2.)* Recall (verse ID, term recognition) is easiest to construct and auto-score, which is exactly why the field over-produces it. Include items demanding application of tradition-specific methods (usul al-fiqh, natural law, karma yoga) to novel scenarios.

3. **Build in denominational/intra-tradition distinctions from the start.** *(Finding: 15/16 = 93.75% treat religion as monolith; §5.5.)* Specify the evaluative standard (Hanafi vs. Ja'fari; Catholic natural law vs. Reformed covenantal). A benchmark that scores "generically Islamic/Christian" output has not measured values alignment — it rewards "doctrinal flattening."

4. **Use domain-specific, non-English, exact-match items to defeat the frontier ceiling.** *(T2 = the sole discriminative instrument; 93.3-pt spread vs. trimodal rubric; §5.3.)* The T2 recipe — specialized domain + liturgical language + single verifiable answer + genuine difficulty variation — produced a continuous discrimination scale where rubrics produced ceiling/floor. Prefer verifiable-answer formats for frontier discrimination.

5. **Adopt hybrid evaluation architectures; don't rely on rubric accuracy alone.** *(Rubric ceiling paradox: all Claude ≥ 0.93; Codex 0.933 on an 82-char response; §5.3.)* Combine (a) MCQ accuracy floors, (b) redesigned rubrics — **10-point exemplar-anchored scales, not 5-point** — with explicit adequate-vs-excellent discrimination, and (c) response-depth metrics interpreted cautiously.

6. **Treat data availability as the primary practical constraint — and mandate durable, versioned public release.** *(Claim 3: 42% unavailable; data gate cut 77%; BuddhismEval HTTP 401; §4.1.)* Availability is the strongest predictor of usability and is temporally unstable; require persistent hosting and periodic re-verification, not a one-time link.

7. **Weight theological depth above convenience and citation.** *(RD 40% / PE 35% / CI 25% rationale; §3.3.)* Weighting PE/CI equal to RD would let well-resourced, high-citation "religion-as-demographic-label" benchmarks dominate. If the target construct is depth, weight depth.

8. **Expert (in-tradition) validation is the best available construct-validity proxy — budget for it.** *(R6 weighted 2nd-highest; Cultural Authenticity NATIVE/CONSULTED/EXTERNAL criterion; §2.4 sacred-text ethics.)* Sacred texts are not "just data"; interpretive frameworks are tradition-internal. Involve theologians in item construction and gold-standard annotation.

9. **Use the shared-task pipeline model to overcome the depth–ease tradeoff.** *(Islam's PE advantage traced to the Quranic QA community since 2019; RD–PE tradeoff only broken inside that cluster; §5.1, §5.7.)* Coordinated data-release + evaluation protocols + community participation is *the* mechanism that converts theological resources into gate-passing benchmarks. The **first shared task is the hardest**; investment is front-loaded (year-1 workshop/annotation/venue), then declines.

10. **Don't assume a tradition is "un-benchmarkable" — the barrier is infrastructure, not formalizability.** *(Formalizability r = 0.41, n.s.; infrastructure r = 0.74; §5.6.)* Judaism, Confucianism, Taoism, Hinduism have rich digital corpora (Sefaria, Chinese Text Project, Digital Corpus of Sanskrit) awaiting conversion; realistic 2–3 year timeline with coordination.

11. **For oral/communal/practice-based traditions, use fundamentally different evaluation architectures — not more MCQs.** *(Structural epistemic exclusion + CARE Principles; §5.7, Conclusion call 3.)* Community-governed protocols, participatory/relational assessment, narrative-based evaluation. Accept that some results will be non-public/non-replicable as a cost of epistemic sovereignty. Guard against *nominal governance*; a moratorium on externally led benchmark development for oral traditions may be warranted until community-governed alternatives exist.

12. **Establish cross-vendor evaluation standards before making vendor claims.** *(Three behavioral modes; three disclosed caveats; §5.4, Conclusion call 4.)* Required elements: **matched administration protocols** (no interactive-vs-backfilled asymmetry), **independent cross-vendor rubric scoring** (avoid same-vendor scorer bias), **blind protocols** (withhold gold labels), and **explicit data-provenance documentation**. Absent these, cross-vendor religious-competence claims are uninterpretable.

13. **Report ranking uncertainty; don't publish a single point ranking.** *(Composite spread 12.1 < mean CI width 15.87; τ = 0.773; §4.2, §5.8.)* Use inclusion-probability tiers; treat tier membership as meaningful and within-tier order as provisional.

14. **Validate feature-level scores with implementation trials.** *(T4 caught Break the Checkbox's zero religious content; HTTP-401 caught BuddhismEval; §4.2.)* Feature scoring can be fooled by demographic-artifact tags; administer items to at least one model to confirm the benchmark tests what its metadata claims.

15. **Design for language/liturgical fairness in scoring.** *(P10 + R3 liturgical-language normalization correcting WEIRD bias; Claim 6 reversal shows coarse WEIRD framing misleads; §3.2, §4.4.)* Treat Arabic/Sanskrit/Hebrew/Pali/Classical Chinese as equivalent to English, not "low-resource," and search in-language — English-only search undercounts and CI weighting privileges English venues.

16. **Beware response-length as a depth proxy and rubric keyword-gaming.** *(Length gradient vendor-dependent; Codex near-ceiling at 5–80× shorter; §5.4.)* Length ≠ depth; a low-threshold rubric may reward keyword presence. Validate that longer/scored-high responses contain substantive tradition-specific reasoning.

---

## 8. File pointers (for drill-down)

**Paper (v3, canonical):** `RELIGIOUS-VALUES/PAPER-V3/`
- `00-abstract.md`, `01-methods.md` (framework, gates, trial protocol, stat plan, 12 limitations), `02-results.md` (Tables 1–11: tiered ranking, claim battery, cross-model & cross-vendor trials), `03-discussion.md` (§5.1–5.9 interpretation + 17 limitations), `04-conclusion.md` (4 calls to action, future work), `05-supp-methods.md`, `06-supp-results.md` (SR6/SR8 robustness checks), `07-supp-tables.md`, `08-supp-figures.md`, `20260413-religious-values-paper-v3.pdf`, `figures/`.

**Literature review:** `RELIGIOUS-VALUES/PAPER/section2-litreview-part1.md` (2.1 eval/alignment/psychometrics, 2.2 religious/cultural values, 2.3 bias/fairness) and `section2-litreview-part2.md` (2.4 computational sacred texts, 2.5 Indigenous/African/marginalized, 2.6 contribution).

**Feature matrix (primary data asset):** `RELIGIOUS-VALUES/data/20260404-religious-benchmark-feature-matrix-v2.json` — 401 entries × 22 features + composites + gate flags; keys include `RD_score`/`PE_score`/`CI_score`/`COMPOSITE`, `passes_gates`, `D5_primary_tradition`. (v1: `20260403-religious-benchmark-feature-matrix.json`.)

**Supporting data:** `20260403-religious-benchmark-candidates.json`, `20260403-religious-values-top15.json`, `20260403-format-taxonomy.json`, `20260403-external-search-results.json`, `20260403-ingest-report.json`, `20260404-claim-robustness-tests.json`, `20260404-bias-values-items.json`, `20260404-Task1_MCQ_Test_gold_labels.csv`, `20260404-citation-chain-discoveries.json`.

**Trial outputs:** `RELIGIOUS-VALUES/trials/`, plus per-model dirs `Codex/`, `Codex-Mini/`, `gemini-2.5-flash{,-lite}/`, `gemini-2.5-pro/`, `gemini-3.1-pro/`; cross-model report `PAPER/20260404-cross-model-construct-validity-report.md`.

**Dashboards:** `RELIGIOUS-VALUES/dashboard/` — latest `20260430-religious-values-dashboard-v8.html` (also v7/v6/v5/v3/v2); `dashboard/review-council-v7`.

**Review/council:** `PAPER/20260404-council-*` (D01 critique + tracking, deliberation full review, session6 composition); `PAPER-V3/review-council/`.

**Reports & session handoffs:** `RELIGIOUS-VALUES/reports/`; `PAPER/2026040*-rv-session*-handoff.md` (sessions 5–15) and `20260430-rv-dashboard-v8-handoff.md`.
