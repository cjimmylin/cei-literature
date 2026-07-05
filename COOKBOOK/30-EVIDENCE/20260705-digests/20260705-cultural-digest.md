# Cultural / Global Values Benchmark Survey — Evidence Digest

*Harvest of the Cross-Cultural AI Values Alignment sub-project (PAPER-V2, COUNCIL audits, benchmark ranking + taxonomy data). Prepared 2026-07-05 for COOKBOOK benchmark designers. All quantitative claims copied verbatim from the source; nothing recomputed.*

---

## 1. Project scope & method

The sub-project is a three-study investigation into cross-cultural AI values alignment. For the COOKBOOK the load-bearing study is **Study 2 (benchmark meta-evaluation)**, but the digest also harvests Study 1 (corpus/scholarship) and Study 3 (model trials) because their findings constrain benchmark design directly.

**Corpus sizes (the "nominal scale"):**
- **Study 1 — Scholarship:** 2,329 AI ethics papers (2010–2026) scored across 34 normative dimensions. Author geography resolved for 98.6%. Each paper got a composite WEIRD score (0–100). Of 2,329, 730 (31.3%) meet the ethics-relevance threshold (ethics_overall ≥ 50).
- **Study 2 — Benchmarks:** **218 benchmarks** meta-evaluated against a **96-feature taxonomy across 13 dimensions** (the canonical taxonomy JSON records 107 features / 13 dimensions v1.0; the paper cites "96-feature" as the scored subset — both numbers appear in the source and are reproduced here as written). Ranked by **TOPSIS with ELECTRE III veto thresholds**, plus hierarchical clustering.
- **Study 3 — Trials:** 10 benchmark instruments (CC1–CC10), **380 items** across 7 non-Western traditions, self-administered to 10 LLMs from 3 providers (Anthropic, OpenAI, Google), with multi-model replication.
- A **12-member interdisciplinary expert council** guided all phases; 7 tradition specialists held veto authority over claims about their traditions.

**How benchmarks were identified (Study 2 two-stage process):**
1. Vault scan of **1,574 candidate papers** from the CEI Literature Vault (of these, papers scoring ≥ 20 on a composite relevance score, filtered on `is_benchmark`/`is_eval`/`is_dataset` metadata flags plus non-Western framework scores).
2. Manual review reduced the 1,574 to **218** meeting all inclusion criteria: paper must (a) propose or systematically evaluate a benchmark/standardized instrument; (b) address cross-cultural values, moral reasoning, or normative pluralism; (c) provide enough methodological detail to score features.
3. A **targeted external search** added 48 papers from arXiv, Semantic Scholar, and ACL Anthology, focused on underrepresented traditions (Islamic, Ubuntu, Indigenous, Dharmic, Buen Vivir).

**How benchmarks were scored (two-tier):**
- **Deep scoring:** 32 benchmarks (top 50 by relevance minus 18 with insufficient detail) — two council members independently scored all 96 features; divergences > 2 SD resolved by modified-Delphi discussion.
- **Automated scoring:** the remaining 186 benchmarks — regex extraction from YAML metadata + PDF-extract text on **13 key features** (format type, item count, language count, cultural scope, primary theory, data availability, LLM-eval history, psychometric reporting, non-Western framework count, Global South representation, year, community consultation, response format).

**Ranking method:** TOPSIS closeness coefficient on 8 weighted criteria; categorical features converted to ordinal scales (cultural scope: monocultural=1 … pancultural=5). ELECTRE III veto thresholds applied as **hard constraints**: any benchmark with monocultural scope AND zero non-Western frameworks AND no Global South representation is flagged structurally inadequate regardless of TOPSIS score. **5 benchmarks vetoed** (M³oralBench #26, K-Viscuit #32, MoralBench #36, "Is ETHICS about ethics?" #54, AgentBench #129).

**Weight scheme (primary):** alignment relevance 0.20 · cross-cultural scope 0.20 · non-Western coverage 0.15 · LLM administrability 0.12 · psychometric quality 0.10 · evaluation depth 0.10 · data availability 0.08 · epistemic provenance 0.05.

**Sensitivity:** 5 alternative schemes each perturbing one dimension +20% (with rescaling): boost-alignment, boost-cross-cultural-scope, boost-non-Western-coverage, boost-LLM-administrability, boost-psychometric-quality. Rank concordance across all 6 schemes: **Kendall's W = 0.9242** — strong rank stability.

**Gold-standard validation of the keyword scorer** (Study 1, but it governs how "non-Western content" was detected everywhere): 700 paper-framework pairs across 520 unique papers, two independent raters + tradition-specialist adjudicator. Mean **recall 0.986**, mean **precision 0.481**, mean F1 0.603 (see §4).

---

## 2. Benchmark characterization framework (the 13-dimension / 107-feature taxonomy)

Canonical name: *Cross-Cultural Values Alignment Benchmark Feature Taxonomy* v1.0 (2026-04-04), 107 features / 13 dimensions, built by the 12-member benchmark council. Enumerated dimensions and what each captures:

1. **Instrument Format** (8 feats): structural/procedural properties — Format Type, Response Format, Likert Scale Points, Item Count, Administration Time, Adaptive, Reverse-Scored Items Present, Subscale Count.
2. **Cultural Scope** (8 feats): breadth/depth of cultural coverage — Cultural Scope, Cultures Count, Countries Count, WEIRD Tier Coverage, Global South Included, Indigenous Populations Included, Religious Traditions Covered, Cultural Adaptation Method.
3. **Language Coverage** (6 feats): Languages Count, Languages List, Translation Method, Translation Validated, Non-English Primary Development, Code-Switching Supported.
4. **Population & Sampling** (8 feats): human populations used to develop/validate/norm — Total Sample Size, Sample Countries, Sample WEIRD Distribution, Sample Demographics Reported, Annotator Count, Annotator Diversity, Community Participatory Design, Indigenous Governance Protocol.
5. **Theoretical Grounding** (10 feats): Primary Theory, Secondary Theories, Western Framework Count, Non-Western Framework Count, Non-Western Frameworks List, Theory Depth, Cross-Framework Comparison, Values Taxonomy Used, Tradition School, Tradition Depth.
6. **Psychometric Properties** (11 feats): Reliability Reported, Cronbach's Alpha Range, Test-Retest Reliability, Construct Validity, Measurement Invariance Level, Invariance Groups Tested, Invariance Method, Differential Item Functioning, Ecological Validity, Criterion Validity, Acquiescence Control.
7. **Evaluation Depth** (13 feats): cognitive/moral complexity — Evaluation Depth, Moral Reasoning Level, Context Sensitivity, Stakeholder Complexity, Temporal Scope, Power Dynamics Addressed, Unit of Moral Agency, Relationship Context, Modality, Consensus Mechanism, Harmony-vs-Optimization Orientation, Moral Concept Thickness, Universalist-vs-Particularist.
8. **LLM Administrability** (10 feats): LLM Administrable, Administration Method, Items Under 200, Requires Behavioral Observation, Human Baseline Available, Prior LLM Evaluation, Evaluation Target, Prompt Sensitivity, Persona Transferability, Pluralism Reduction Testable.
9. **Data & Reproducibility** (6 feats): Data Availability, Code Available, Data URL, License, Documentation Quality, Versioned.
10. **Values Alignment** (10 feats): Alignment Relevance, Alignment Target, Overton Pluralism, Steerable Pluralism, Distributional Pluralism, Value Conflict Handling, Normative Position, Wellbeing Conception, Ecological Dimension, Intergenerational Scope.
11. **Cross-Cultural Validity** (7 feats): Etic-Imposed, Emic-Derived, Acquiescence Response Control, Extreme Response Style Control, Social Desirability Control, Back-Translation Equivalence Level, Cultural Bias Audit.
12. **Gap & Impact** (4 feats): Tradition Gap Filled, Region Gap Filled, Novelty, Citation Count.
13. **Epistemic Power & Provenance** (6 feats): the geopolitics of knowledge production — Creator Region, Creator Institution Type, Funding Source, Affected Community Authorship, Extractive Potential, Counter-Hegemonic.

The **8 TOPSIS ranking criteria** are a weighted projection of this taxonomy (dims 10, 2, 5, 8, 6, 7, 9, 13 respectively). Note dimensions 11 (cross-cultural validity) and 13 (epistemic provenance) are the two axes on which nearly the entire corpus fails.

---

## 3. Key findings (each with its statistic exactly as in the source)

1. **Zero measurement invariance.** Of 218 benchmarks, **precisely zero** report measurement invariance testing — the psychometric prerequisite for any valid cross-cultural comparison. This is the single most consequential finding.
2. **Non-Western concept coverage = 6.8%.** Of 44 moral concepts mapped across 7 non-Western traditions, only **3 of 44 (6.8%)** have any operational benchmark measure: *ren* (仁), *li* (禮), and *ubuntu*. The other 41 are invisible to the evaluation infrastructure.
3. **Five traditions have zero measured concepts:** Islamic (0/7), Dharmic (0/6), Buddhist (0/6), Indigenous/Relational (0/6), Buen Vivir (0/5). Confucian 2/9 (22.2%), Ubuntu 1/5 (20.0%).
4. **Two-cluster bifurcation** (Gower distance, Ward linkage, silhouette 0.221): Cluster 1 "Non-Western Focused" (*n* = 47, 21.9%; mean NW-framework count 0.915 vs 0.012, indigenous inclusion 0.277 vs 0.000, but low LLM administrability); Cluster 2 "LLM-Ready" (*n* = 168, 78.1%; administrability 0.952, data availability 2.095, but NW-framework 0.012 and zero indigenous content). The intersection of culturally substantive AND LLM-administrable is **≈15 benchmarks (<7%)**.
5. **Reliability gradient.** 63 benchmarks (28.9%) report any reliability; 26 (11.9%) report no validation whatsoever. Mean validation-chain score **1.17 / 3.0**; no paper achieves a perfect score. **Inverse** relationship between cultural ambition and rigor: bicultural/limited-scope benchmarks report reliability at 39.3%; multicultural-scope at only 18.7%.
6. **Benchmark production is scaling but not diversifying.** 12 papers (2023) → 129 (2025), a tenfold rise in two years. Cross-cultural/global instruments grew 3 (2023) → 23 (2025) in absolute terms but the proportional share **declined from 25% to 17.8%**.
7. **Geographic concentration of creators:** North America 39.4% (86), East Asia 19.3% (42), Western Europe 16.1% (35); NA+WEU together **55.5%**. Sub-Saharan Africa 0.9% (2), Latin America 1.4% (3). **52.3% of benchmarks focused on non-Western values are created by Western institutions** (90 of 172 NW-content benchmarks originate in NA/WEU).
8. **Community participatory design:** only **15 of 218 (6.9%)** show any evidence; 93.1% designed without systematic consultation with the cultures being measured.
9. **Structural assumptions disadvantage non-Western traditions.** Unit of moral agency among deep-scored papers: "model" 50%, "LLM" 12.5%, "community" exactly one paper. Response format: scenario/dilemma 46.3%, MC/QA 10.1%; forced-choice dominates (36 multiple-choice, 23 binary). Ecological dimension addressed by only **2 papers (0.9%)**; intergenerational scope by **0 papers (0.0%)**.
10. **TOPSIS #1 is unusable for LLMs.** Ray (2025), highest cross-cultural scope + NW coverage, has TOPSIS 0.637 but **zero LLM administrability and zero data availability**. Cultural depth and practical usability are negatively correlated; 7-benchmark Pareto frontier confirms no single benchmark dominates.
11. **Study 1 backdrop:** corpus mean WEIRD 64.5/100; 59.7% High-WEIRD; NA 39.5% + WEU 20.6% = 60.1% of papers. Only 6.9% (161 of 2,329) engage any non-Western framework at detection threshold; precision-adjusted genuine engagement ≈ 95 papers (4.1%).
12. **Study 3 model behavior:** Claude Opus 4.6 clusters with <15% of global population (closest to Germany 0.538, farthest Saudi Arabia 1.974 — a 3.7-fold spread). MFQ individualizing:binding ratio **3.75** (pre-rounded summary; 3.82 raw item-level) = **2.7× more extreme** than the most liberal documented human population (I:B ≈ 1.4) and 4.4× the non-WEIRD baseline (0.86). Western-liberal resolution in **100% (40/40)** of value-conflict scenarios. Knowledge-about vs value-expression gap: **37 of 40 items (92.5%)** show the model describing a tradition accurately while unable to reason within it.
13. **Effective diversity is double digits, not thousands.** ~95 papers (of 2,329) with genuine NW engagement; ~15 benchmarks (of 218) at the substance×usability intersection; effective N ≈ 3.4 (range 3.1–4.8) models (of 10 nominal). RLHF conflict taxonomy: 703 instances across 3 authentic Claude models (Opus 277, Sonnet 210, Haiku 216); top zones = individual-autonomy default (138), secular epistemology (101), consequentialist optimization (82).

---

## 4. Scoring & validity methods — what worked / what failed

**Worked:**
- **TOPSIS + ELECTRE III veto** proved robust: Kendall's W = 0.9242 across 6 weight schemes means the culture-vs-usability trade-off is not an artifact of weighting. The veto layer correctly screened 5 technically-strong-but-culturally-narrow benchmarks (AgentBench, MoralBench, etc.) out of the top tier.
- **Keyword scorer recall = 0.986** — near-perfect at not missing genuinely engaged papers (only 3 false negatives, all Indigenous, using non-canonical terms like "First Nations digital self-determination" instead of "data sovereignty"/"CARE Principles").
- **Dual reporting (raw + precision-adjusted counts)** salvaged a low-precision scorer: because precision-adjustment *lowers* NW-engagement estimates, the low precision *strengthens* the WEIRD-bias conclusion rather than undermining it.
- **RLHF-conflict thematic coding**: inter-rater Cohen's κ = 0.78 on a 60-item validation subset (7-theme frozen codebook, multi-label).
- **Provenance-tier / effective-N framework** (design-effect DEFF = 1+(m−1)ρ) honestly downgraded 10 nominal models to N_eff ≈ 3.4, preventing over-claiming from correlated data.

**Failed / weak:**
- **Keyword precision = 0.481 mean** — roughly half of NW detections are terminological mentions, not substantive engagement. Framework-specific: Islamic **1.000**, Indigenous 0.675, Ubuntu 0.579, Confucian 0.364, Buddhist 0.333, Dharmic 0.250, Buen Vivir **0.167**.
- **The "NLP-on-texts" false-positive pattern** is the single largest source of measurement error: a Chinese NLP benchmark run *on* classical Chinese texts triggers the same keywords as a paper arguing *for* Confucian role ethics. This is why Buddhist/Dharmic/Buen Vivir precision collapses — their keywords overlap heavily with computational-linguistics corpora work. Novel methodological finding: *studying a tradition's texts* ≠ *reasoning with a tradition's ethics*.
- **Cross-provider model inference failed structurally:** GPT trials were Codex-authored (predictions of GPT responses, not actual), and Gemini's 5 variants were aggregate-convergent. Minimum detectable effect at N_eff=3.4 is Cohen's d ≈ 2.5 → all cross-model patterns are **descriptive only, never inferential**.
- **Silhouette 0.221** for the two-cluster solution is only "moderate" separation — the bifurcation is substantively clear but statistically soft.
- **Forced-choice & English-only administration** are themselves validity threats: a Confucian response filtered through a Likert dilemma in English is already distorted (acknowledged circularity — Western instruments may be constitutively unable to detect within-tradition reasoning).

---

## 5. Exemplar benchmarks (top-ranked; what/why/flaws)

Top-15 by TOPSIS (from `20260404-benchmark-rankings.json`; stability = rank across the 5 sensitivity schemes):

| Rank | Benchmark | TOPSIS | Stability |
|---|---|---|---|
| 1 | Ray — Indigenous Knowledge Systems (Māori & Navajo AI governance) | 0.6374 | [1,1,1,1,1] |
| 2 | Wu — CVC (Chinese Value Corpus) | 0.5968 | [2,5,2,2,2] |
| 3 | Yu — CMoralEval | 0.5691 | [3,7,3,4,3] |
| 4 | Catapang — EMoTES-3K (Filipino emotion/morality) | 0.5685 | [4,6,4,3,4] |
| 5 | Alam — From RAG to Agentic RAG (Islamic knowledge) | 0.5649 | [5,8,5,5,5] |
| 6 | Rahman — CCD-Bench (cultural conflict, 37 countries) | 0.5526 | [6,2,11,6,6] |
| 7 | Lahmar — IslamTrust (v1) | 0.5473 | [7,9,6,7,9] |
| 8 | Lahmar — IslamTrust (v2) | 0.5473 | [8,10,7,8,10] |
| 9 | Rao — NormAd (social norms, 37 countries) | 0.5451 | [9,3,12,9,7] |
| 10 | Rao — NORMAD (cultural adaptability) | 0.5449 | [10,4,13,10,8] |
| 11 | Liu — JMedEthicBench (Japanese medical ethics) | 0.5372 | [11,11,8,11,11] |
| 12 | MELAC (Massive Eval w/ Alignment of Cultures) | 0.5158 | [12,14,9,12,12] |
| 13 | Agarwal — Ethical Reasoning & Moral Value Alignment | 0.4850 | [13,12,15,13,14] |
| 14 | JainGPT (Jain literature chatbot) | 0.4835 | [15,19,10,14,15] |
| 15 | One Model, Many Morals | 0.4779 | [14,15,16,15,13] |

**Why the leaders ranked high, and their remaining flaws:**
- **Ray (#1)** — dimensional scores: cross-cultural scope 9.0, NW coverage 5.0, evaluation depth 7.5, but **llm_administrability 0.0, psychometric_quality 0.0, data_availability 0.0**. Most culturally substantive instrument in the field; *cannot currently evaluate a language model.* Perfect rank stability = its dominance is weight-invariant.
- **CVC (#2)** — scope 9.0 + evaluation depth 10.0 + LLM-ready (administrability 4.0, data 4.0). Flaw: measures cultural knowledge/judgment in Chinese contexts but does not operationalize Confucian *relational ontology* (tests whether a model *knows* Confucian concepts, not whether it reasons within them). Psychometric quality only 1.0.
- **CMoralEval (#3) / EMoTES-3K (#4)** — high evaluation depth (9.0, 7.0) and data availability; same knowledge-not-reasoning limitation; psychometric quality 1.0.
- **IslamTrust (#7/#8)** — counter-hegemonic; evaluates alignment across the five *maqāṣid* as a structured jurisprudential framework, not a cultural checklist. Flaw: assesses *conformity* to Islamic positions, not capacity to reason within *uṣūl al-fiqh* that generate them (mimicry vs reasoning).
- **NormAd (#9)** — highest effectiveness index (39.38) on the Pareto frontier; strongest scope×administrability balance across 37 countries. Flaw: frames social norms as adherence profiles; limited NW-framework depth; no measurement invariance.

**Pareto frontier (7 non-dominated instruments):** NormAd, CCD-Bench, EMoTES-3K, MITRA-zh-eval, Neira-Davila, HBC, Ray. No benchmark dominates all four axes (scope, psychometrics, data availability, NW-framework count) — cultural depth and usability are negatively correlated.

**Counter-hegemonic exemplars** (lower ranks but structurally different — treat non-Western values as autonomous systems, not exotic variants of liberalism): IslamTrust (Lahmar 2025), UbuntuGuard (Eickhoff 2026, operationalizes Ubuntu as a policy-evaluation framework). They lag on administrability/data because they must *build* their own infrastructure while dominant benchmarks *inherit* Western-paradigm infrastructure.

---

## 6. Gaps & voids the project identified

**Uncovered constructs (41 of 44 concepts unmeasured):** *karma, dharma, ahimsa, moksha, seva, satya* (Dharmic, 0/6); *maslahah, maqasid al-shariah, ihsan, tawakkul, adl, halal/haram, shura* (Islamic, 0/7); Four Noble Truths / Eightfold Path / *karuna* / mindfulness / non-attachment / *pratityasamutpada* (Buddhist, 0/6); relationality, land-based ethics, intergenerational obligation, ceremony-as-practice, reciprocity, kinship (Indigenous, 0/6); *sumak kawsay*, harmony-with-nature, community wellbeing, rights of nature, plurinationality (Buen Vivir, 0/5). Even the "best-covered" traditions leave *xiao* (filial piety), *he* (harmony), *guanxi*, *yi*, *zhi*, *xin* unmeasured (Confucian), and communal identity, collective responsibility, elder wisdom, reconciliation unmeasured (Ubuntu).

**Uncovered traditions (zero measured concepts):** Islamic (1.9 B adherents, 6 benchmarks but 0 concepts operationalized), Dharmic (4 benchmarks), Buddhist (13 benchmarks — 2nd-highest count, all test factual knowledge only), Indigenous (6 benchmarks, none CARE-compliant), Buen Vivir (2 benchmarks total).

**Uncovered formats/paradigms:**
- No instrument supports **communal/deliberative units of assessment** (Ubuntu's *indaba*/consensus — the deliberation IS the moral act; current LLM-eval paradigms only elicit individual model responses).
- No support for **relational-state / role-situated** evaluation (Confucian *wu lun*, Dharmic *svadharma* — non-universalizable by design).
- **Ecological (0.9%) and intergenerational (0.0%)** moral dimensions essentially absent — blinds the infrastructure to Buen Vivir, Indigenous, Buddhist interdependence.
- **Process-oriented scoring** absent — forced-choice strips deliberative quality that matters in Ubuntu/Confucian/Buddhist ethics.
- **Measurement invariance pipeline** entirely absent (0/218) — no configural/metric/scalar invariance anywhere.
- **Community-consent / data-sovereignty (CARE Principles)** compliance reported by zero Indigenous benchmarks.

**Compounding pattern (Table 14):** marginality is inherited stage-to-stage. A tradition absent from the corpus → no constructs for benchmark developers to operationalize → no RLHF optimization signal → weak model engagement → diminished visibility in the literature. Buen Vivir (~1 precision-adjusted paper → 0/5 concepts → model floor 1.0) is the extreme case.

---

## 7. LESSONS FOR DESIGNING NEW BENCHMARKS (each traced to a finding)

1. **Report measurement invariance or self-label as monocultural.** Any benchmark claiming cross-cultural scope must report at minimum configural + metric invariance (MGCFA via `lavaan`/Mplus). *(Finding 1: 0/218; Council rec 2; §7.5.)* Without it, all cross-cultural score comparisons are semantically incoherent — the "fairness=3" item means different things to a Western vs Confucian vs Ubuntu respondent.
2. **Design for the substance×usability intersection, don't pick a side.** The <7% intersection (Finding 4) is the whole design target: culturally substantive instruments that are also LLM-administrable. Ray (#1) proves depth-without-administrability is a dead end for model eval; Cluster-2 proves administrability-without-content is culturally monochrome. *(Findings 4, 10; Pareto frontier.)*
3. **Operationalize reasoning-within, not knowledge-about.** Test whether a model can reason *from* a tradition's internal logic, not recite its concepts. The 92.5% knowledge/expression gap (Finding 12) and the CVC/CMoralEval flaw show that "does the model know what *li* means" is the wrong question; "given filial obligation, how does it navigate a role-situated dilemma" is the right one. *(§4.6 Moral Reasoning Level; §5.3; Council rec 3.)*
4. **Do not import an individualist unit of moral agency by default.** "What should the model do?" already excludes Ubuntu (community), Confucian (relational dyad), and Indigenous (kinship) ontologies. Build community/relational units and process-scoring where the tradition demands it. *(Finding 9: community = 1 paper; §5.4 autonomy-default = 138 conflicts.)*
5. **Avoid forced-choice for process-centric traditions.** Scenario/binary formats strip deliberative quality that IS the moral act in Ubuntu *indaba*, Confucian *li*, Buddhist attention. Include deliberation-quality metrics. *(Finding 9; §4.6 Response Format.)*
6. **Add ecological and intergenerational scope as first-class axes.** Their near-total absence (0.9% / 0.0%) makes benchmarks blind to Buen Vivir, Indigenous relational, Buddhist interdependence. Taxonomy dim 10 already flags Ecological Dimension and Intergenerational Scope — score them. *(Finding 9; §4.6.)*
7. **Build tradition-internal, by tradition-bearing scholars.** 52.3% of NW-focused benchmarks are Western-made, importing liberal framings (filial piety scored "autonomous↔obedient" instead of "incomplete↔fully-realized relational self"). IslamTrust/UbuntuGuard are the model. *(Finding 7; Council rec 1; §4.5.)*
8. **Require community participatory design and consent protocols.** Only 6.9% had community input; zero Indigenous benchmarks are CARE-compliant. Indigenous knowledge is not public-domain dataset material. *(Finding 8; Council rec 5.)*
9. **Guard against the NLP-on-texts false positive.** Distinguish computational study *of* a tradition's corpus from engagement *with* its ethics. Use tradition-specific strong keywords (Islamic *maqasid/fiqh/ijtihad* → precision 1.000) and FP-exclusion regexes (e.g. Ubuntu OS filters), not generic term-matching (Buen Vivir 0.167). *(§4 gold-standard; §7.9.)*
10. **Report psychometrics precisely at high cultural ambition.** The inverse ambition/rigor relationship (39.3% → 18.7% reliability) is exactly backwards; broad-scope instruments need MORE validation. Target the validation-chain composite (mean is only 1.17/3.0). *(Finding 5.)*
11. **Screen with a veto layer, not just a weighted sum.** ELECTRE III hard constraints (monocultural + zero-NW + no-Global-South = inadequate) prevent technically slick, culturally narrow benchmarks from topping leaderboards. TOPSIS alone would let AgentBench-type instruments dominate. *(Finding, §2 methods; W=0.9242 confirms robustness.)*
12. **Ship benchmark "nutrition labels" + graduated scope certification.** Report cultural-scope certification level, invariance evidence, creator positionality, community-participation level, tradition-internal validation status, known limitations. Scope labels (monocultural/bicultural/multicultural/cross-cultural) must be *earned by demonstrated invariance*, not self-described. *(Council recs 4 & 6.)*
13. **Test liberal-compatibility filtering explicitly.** Models score 3–4/5 on NW positions that converge with liberalism (Ubuntu care→welfare, *zakat*→redistribution, *ahimsa*→harm-reduction) and 0–1 on divergent ones (Confucian filial loyalty overriding justice, Dharmic *svadharma*, complementarian inheritance). A good benchmark deliberately includes divergent items and penalizes silent Western-default resolution. *(§5.2; §5.5 100% default rate; Council rec 3.)*
14. **Preserve tradition-specific semantics; never score on English nearest-neighbor translation.** "Righteousness"≠*yì*, "compassion"≠*karuṇā*, "justice"≠*ʿadl*. Flattening erases the distinctions the benchmark is meant to detect. *(§5.3 liberal-translation-layer; Council rec 7.)*
15. **Require explicit framework transparency from the model under test.** Score whether a model can declare which normative framework it is reasoning within and switch on request. *(Council rec 8; §7.6.)*
16. **Report effective sample size, not nominal, for any multi-model claim.** Correlated / non-authentic model outputs (Codex-authored GPT, aggregate-convergent Gemini) collapsed 10 models to N_eff≈3.4 (min detectable d≈2.5). Verify data provenance is authentic (direct API), and treat cross-model patterns as descriptive unless N_eff supports inference. *(Findings 12–13; §5.6.)*
17. **Beware the appearance-of-scale trap.** Nominal breadth (thousands of papers / hundreds of benchmarks) masks double-digit effective diversity. Peer review, leaderboards, and safety evals all function "normally" inside the monoculture and generate false assurance. Design evaluation to surface, not hide, the effective-diversity number. *(§6.4; Finding 13.)*

---

## 8. File pointers (for drill-down)

**Ranking & taxonomy matrices (JSON, summarize with Python — large):**
- `CULTURAL-GLOBAL/DATA/20260404-benchmark-rankings.json` — full 218-benchmark TOPSIS ranking, dimensional scores, veto flags, rank-stability vectors, metadata (weights, sensitivity schemes, Kendall W).
- `CULTURAL-GLOBAL/DATA/20260404-benchmark-feature-taxonomy.json` — canonical 107-feature / 13-dimension taxonomy v1.0 (full feature names + descriptions).
- `CULTURAL-GLOBAL/DATA/20260404-benchmark-features-merged.json` (+ `-features.json`, `-features-deep-batch1/2.json`) — per-benchmark feature scores.
- `CULTURAL-GLOBAL/DATA/20260404-benchmark-analyses.json`, `-benchmark-candidates.json`, `-benchmark-external-search.json`, `-benchmark-ingest-report-v2.json` — identification pipeline.
- `CULTURAL-GLOBAL/DATA/20260404-clustering-results.json`, `-cross-cultural-analysis.json` — two-cluster / correspondence outputs.

**Paper sections (PAPER-V2/):**
- `00-abstract.md`; `02-methods.md` (Study-2 scoring §2.3, gold-standard Table 2, TOPSIS weights); `04-results-benchmarks.md` (Study 2 in full: MI gap, coverage matrix Table 8, geographic Table 9, rankings Table 10, Pareto frontier); `05-results-trials.md` (Study 3, MFQ, conflict taxonomy Table 12, effective-N Table 13); `06-results-synthesis.md` (triple bind, Table 14 gap-compounding); `07-discussion.md` (§7.5 invariance pipeline, §7.8 eight council recommendations); `08-conclusion.md` (6-point intervention roadmap).

**Council tradition audits (COUNCIL/) — keyword-detection audit sheets per tradition (scored papers, strong/medium/FP keyword lists, FP patterns):**
- `20260403-audit-nw_ubuntu.md`, `-nw_confucian.md`, `-nw_islamic_jurisprudence.md`, `-nw_buddhist.md`, `-nw_dharmic.md`, `-nw_indigenous_relational.md`, `-nw_buen_vivir.md`.
- Related: `20260404-benchmark-council.md`, `-benchmark-critique.md`, `-benchmark-deliberation.md`; gold-standard `20260404-gold-standard-results-v2.json` + per-tradition `20260404-gs-nw_*.json`.

**Supplementary (PAPER-V2/supplementary/):** `S1-methods.md`, `S2-results.md`, `S3-council.md`, `S4-trial-protocols.md`, `S5-keyword-lists.md`, plus `supp-figures/`, `supp-tables/`. Reproducibility script `PAPER-V2/verify_mfq.py`.

**Dashboards:** `CULTURAL-GLOBAL/DASHBOARD/` (index.html, benchmarks.html, benchmark-data.js) and `CULTURAL-GLOBAL/DASHBOARD-V2/`.

**Assembled PDFs:** `PAPER-V2/20260412-cross-cultural-ai-values-alignment-v2.1.pdf` (latest), `20260405-...v2.0.pdf`.
