# 11 — Cultural and Linguistic Values: Methods for Benchmarking

> **CEI COOKBOOK · 00-KNOWLEDGEBASE.** Fable-authored (2026-07-05). Primary evidence:
> `20260705-cultural-linguistic-dossier.md` (~366 cards, the corpus's largest theme) + the completed
> Cultural-Global meta-evaluation (`20260705-digests/20260705-cultural-digest.md`: 218 benchmarks ×
> 13-dimension taxonomy, TOPSIS+ELECTRE ranking, 7 tradition-council audits). `[stem]` = evidence card.
> Cultural-Global cross-model numbers are descriptive only (N_eff≈3.4 disclosure); its landscape
> findings stand.

---

## 1. The state of the field in five numbers (Cultural-Global meta-eval, n=218)

1. **0/218** benchmarks report measurement invariance testing — the psychometric prerequisite for ANY
   valid cross-cultural score comparison. Without configural/metric invariance, "fairness=3" means
   different things to Western, Confucian, and Ubuntu respondents; every cross-cultural leaderboard in
   the field is semantically incoherent (the single most consequential finding).
2. **3/44 (6.8%)** non-Western moral concepts have any operational measure (*ren*, *li*, *ubuntu*);
   five traditions have ZERO measured concepts (Islamic 0/7, Dharmic 0/6, Buddhist 0/6,
   Indigenous/Relational 0/6, Buen Vivir 0/5) — *karma, maqasid, karuna, reciprocity, sumak kawsay*
   are invisible to the evaluation infrastructure.
3. **<7%** of benchmarks sit at the culturally-substantive × LLM-administrable intersection (two-cluster
   bifurcation: "Non-Western Focused" n=47 with near-zero administrability vs "LLM-Ready" n=168 with
   near-zero non-Western content). The TOPSIS #1 benchmark (Indigenous governance) has zero LLM
   administrability and zero data availability — depth and usability are negatively correlated, and
   the intersection is the entire design target.
4. **52.3%** of non-Western-focused benchmarks are created by Western institutions; 6.9% show any
   community participatory design; 0 Indigenous benchmarks are CARE-compliant; ecological scope 0.9%
   and intergenerational scope 0.0% of instruments.
5. **92.5%** (37/40 items in trials) — the knowledge-about vs reasoning-within gap: models describe a
   tradition accurately while resolving 100% (40/40) of value conflicts in the Western-liberal
   direction. The construct to measure is *reasoning-within*, and almost nothing measures it.

## 2. The WEIRD default (the measured phenomenon)

- Un-prompted LLMs answer like Americans regardless of prompt language, persona, or **model origin**
  (Chinese-made models included; nationality effect β=−.30 vs origin β=.03 [2025-Haslett]); alignment
  tracks web-content-per-country r=0.94, NOT model scale (r=0.13) [2025-Sukiennik]; Western-Europe WVS
  alignment ~3× Sub-Saharan Africa [2025-Mohammadi]; divergence *grows* with capability [2024-Kirgis]
  and RLHF moves models farther from human distributions [2024-Abdulhai].
- **Language ≠ culture**: prompting in Russian/Chinese/Turkish does not shift values toward those
  populations [2023-Durmus]; "English-from-Nigeria" ≠ "English-from-US" [2024-Tonneau-Geographies].
  Operationalizing culture via language (CultureLLM et al.) is a category error the corpus explicitly
  splits on — design must disentangle language, script, nationality, and religion as separate factorial
  variables.
- Cross-language **consistency** is the hidden catastrophe: a model can be ~97% "safe" per language yet
  44.74% consistent in *which* items it passes across languages [2024-Friedrich-M-ALERT]. Report
  inter-language exact-match/flip metrics, not just per-language scores.

## 3. Localization methodology (the ladder, weakest → strongest)

1. **Raw machine translation — never for value items.** MT imports source-culture norms
   [2025-Zhou-CrowS], silently destroys constructs in gendered languages (BBQ gender-neutrality
   required 15h of manual repair [2025-Satheesh-GG-BBQ]), and retains as little as 24–31% of bias
   signal [2026-Reaj].
2. **MT + quality-estimation filtering** (EuroGEST) — acceptable for scale, still norm-importing.
3. **Transcreation** — re-ground entities and referents (George Washington→Toussaint Louverture)
   [2024-Wynter-RTP-LX].
4. **Translate-filter-modify** — drop non-applicable categories, swap names, ADD locally-salient axes
   (caste, region) [2024-Sahoo-IndiBias].
5. **Native authoring** — items written by native speakers with per-item cultural-validity tags so
   models are scored only on locally-valid items (SHADES: 43 native speakers, 16 languages
   [2025-Al-SHADES]); hand-authoring doubles as contamination control [2025-Kumar-BengaliMoralBench].
6. **Survey-grounded native (gold standard)** — every stereotype/target validated by a
   demographically-balanced local survey, with human solvability gates and a "no stereotype exists"
   opt-out (KoBBQ's Simply-Transferred/Target-Modified/Sample-Removed/Newly-Created partition is the
   reusable template; machine-translated BBQ gives statistically different bias readings
   [2024-Jin-KoBBQ]); society-matched paired benchmarks (BBQ↔KoBBQ) enable cross-society comparison.

**Report a translation-retention rate** and treat liturgical/classical languages as first-class.

## 4. The measurement checklist unique to this domain

1. **Bias vs competence separation** — parallel neutral control sets (MBBQ [2024-Neplenbroek]);
   low-resource extraction failure masquerades as low bias [2025-Zhou; 2025-Arnob]; report per-language
   compliance/refusal rates before any values claim (models often "fail to provide meaningful answers"
   in Arabic/Bengali/Hindi [2025-Al]).
2. **Elicitation-language factorial** — input × reasoning language (reasoning language drives ~2× the
   instability [2025-Li-Untangling]); cross-script minimal pairs (Bengali→Romanized F1 0.80→0.39
   [2022-Das]; Simplified↔Traditional Chinese censorship bias [2025-Ahmed]); code-mixing and
   transliteration as the highest-headroom stress tier (SweEval transliterated harmful-compliance 0.92
   vs 0.19 English [2025-Kumar-SweEval]).
3. **Representative sampling** — evaluate at true base rates; the holdout-vs-representative gap is
   an order of magnitude (AP 87.2%→9.4% [2024-Tonneau-HateDay]).
4. **Localized axis taxonomy** — caste/region/military-service/marital-status where salient
   [2022-Shaily Bhatt; 2023-Lee-KoSBI]; culture-native value constructs as first-class dimensions
   (harmony/Doctrine-of-the-Mean [2023-Huang-FLAMES]; Confucian-plus-modern taxonomy [2024-Yu-CMoralEval]).
5. **Distributional ground truth with reported ceiling** (KorNAT SVA ceiling 0.450 [2024-Lee];
   deviation-ratio correction for the global-average default [2025-Sukiennik]); disagreement preserved
   (39.5% of offensiveness variance is individual vs 2.9% country [2023-Davani]).
6. **Grader bias audit** — Perspective scores German ~3× more toxic than its English translation
   [2024-Nogara]; judges are worse in low-resource languages [2024-Liu-JAILJUDGE]; use
   translation-as-content controls and cross-family judges (doc 07).
7. **Measurement invariance** — run MGCFA (configural → metric → scalar) before publishing any
   cross-cultural comparison; scope labels (monocultural/bicultural/multicultural/cross-cultural) must
   be *earned by demonstrated invariance*, not self-described (Cultural-Global council rec).

## 5. Reasoning-within, not knowledge-about (the frontier construct)

The Cultural-Global trials' sharpest result: models describe traditions accurately (knowledge) while
resolving 100% of value conflicts in the Western-liberal direction (expression). Design implications:

- **Liberal-compatibility filtering is the test**: models score 3–4/5 on non-Western positions that
  happen to converge with liberalism (Ubuntu care→welfare, zakat→redistribution, ahimsa→harm-reduction)
  and 0–1 on divergent ones (filial loyalty overriding impartial justice, svadharma role-duties,
  complementarian inheritance). A valid benchmark deliberately includes **divergent items** and
  penalizes silent Western-default resolution.
- **Unit-of-agency pluralism**: "what should the model do?" already imports individualism. Build
  community/relational units (Ubuntu *indaba* consensus where the deliberation IS the moral act;
  Confucian role-dyads; kinship structures) with process-scoring, not forced choice — forced choice
  strips exactly the deliberative quality these traditions evaluate (only 1 of 218 benchmarks uses a
  community unit; ecological scope 0.9%, intergenerational 0.0%).
- **Semantic sovereignty**: never score via English nearest-neighbor translation (righteousness≠yì,
  compassion≠karuṇā, justice≠ʿadl); tradition-internal experts author and validate (the
  IslamTrust/UbuntuGuard "counter-hegemonic" pattern — they lag on infrastructure precisely because
  they can't inherit the Western-paradigm tooling).
- **Framework transparency as a scored behavior**: can the model declare which normative framework it
  is reasoning within and switch on request? (Council rec 8; connects to doc 08's
  framework-as-manipulated-variable.)
- **NLP-on-texts ≠ ethics-of-tradition**: studying a tradition's corpus (sentiment on the Gita) is not
  engaging its ethics — the single largest false-positive pattern in tradition detection (keyword
  precision collapses to 0.167 for Buen Vivir vs 1.000 for Islamic jurisprudence terms).

## 6. Design brief for the next cultural-values benchmark (grounds `20-DESIGNS/05`)

- **Target the <7% intersection**: culturally substantive AND LLM-administrable — the entire unclaimed
  design space.
- **Interactive cultural adaptation** rather than static QA: multiturn scenarios where cultural context
  emerges progressively and the model must adapt (or ask); score adaptation trajectory, divergent-item
  handling, and default-resolution direction (connects to doc 06).
- **Survey-grounded native construction** per locale with the KoBBQ partition; society-matched pairs;
  measurement-invariance pipeline as a shipped artifact (the first benchmark to do MGCFA properly is
  instantly differentiated — 0/218 precedent).
- **Factorial language controls** (input × reasoning × script), inter-language consistency metrics,
  low-resource and code-mixed stress tiers.
- **Divergent-value items + reasoning-within scoring + unit-of-agency variants** (individual /
  relational / communal), with ecological and intergenerational scope as scored axes.
- **Community co-design with CARE compliance** for Indigenous content; positionality documented;
  veto-layer screening in any internal ranking (ELECTRE-style hard constraints prevented
  technically-slick monocultural instruments from topping the Cultural-Global leaderboard —
  Kendall W=0.9242 across weight schemes).
- **Benchmark nutrition label**: scope certification earned by invariance evidence, creator
  positionality, community-participation level, known limitations.

**Drill-down:** dossier §2 (six-axis decision table), §3 (nine disagreements incl. language-as-culture
and refusal-status splits), §4 (KoBBQ, KorNAT, SHADES, MBBQ, HateDay, MedES exemplars;
HKGAI/VC-LLM/LocalValueBench target-smuggling anti-patterns). Cultural digest §7 (17 lessons), §8
(file pointers incl. the 218-benchmark TOPSIS rankings JSON, 13-dim taxonomy, 7 tradition audits).
