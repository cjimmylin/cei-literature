# Moral Psychology Benchmark Survey — Cookbook Digest

*Harvest of MORAL-PSYCH PAPER-v5 (the "Triple Bind" meta-evaluation). Source of every statistic below is the v5 sections and the 292-candidate feature matrix. Downstream benchmark designers can treat this as the distilled conclusion set — no need to re-read the paper.*

---

## 1. Project scope & method

The project is the first **full-coverage meta-evaluation of moral psychology benchmarks for LLM assessment**. It answers two questions: (a) how good is the existing benchmark landscape, and (b) do those benchmarks actually distinguish between the LLMs they evaluate.

**Corpus & extraction.** From a curated vault of **2,099 AI ethics papers**, a five-signal extraction pipeline (keyword scoring across 13 theories; explicit benchmark mentions; dataset indicators; methodology markers; theory-specific patterns) identified **292 unique benchmark candidates** spanning **13 moral psychology theories**. Extraction ran in two phases: Phase 1 applied the pipeline to the full vault (221 candidates); Phase 2 added a targeted non-Western sweep (+71 candidates, total 292 after filename dedup). The keyword scorer was expanded mid-study from **65 → 125 patterns**, which recovered 123 previously-invisible candidates and lifted process-theory detection from 4 → 34 candidates (~9x). Information availability: **245 candidates (83.9%) Tier A** (PDF extract + abstract), **47 (16.1%) Tier B** (abstract/metadata only). Source split: 221 phase1 / 71 phase2.

**Scoring.** All 292 candidates scored on a **162-feature framework** (158 active after excluding B5, B8, B9, C4). Only **17 features (Tiers A–C)** determine the quality composite; the other 141 (Tiers D–G) are characterization-only. The composite = **PD×0.50 + PE×0.30 + CI×0.20** (Psychological Depth / Practical Ease / Citation Impact), all features on 0–100. Scoring was batch-calibrated (5 stratified batches of ~59, three anchor benchmarks per batch, ±3-point anchor agreement across all batches). Null policy is deliberately restrictive: absence of a property = score 0 ("informative"), not null; genuine nulls only for D9/D20 (require LLM-administration data, ~35% of candidates). This conservative policy errs toward *underestimating* quality — strengthening the "landscape is weaker than assumed" thesis.

**Tiering.** Composites partitioned by **Jenks natural breaks (k=4)**: break points **[27.8, 43.05, 56.65]**, **GVF = 0.83**. Result: **Top 48 (16.4%), High 89 (30.5%), Med 72 (24.7%), Low 83 (28.4%)** — a bimodal, "hollow" landscape (modal tiers are the extremes). Sensitivity analysis across 5 weighting schemes: 72–84% of candidates retain tier; Spearman ρ > 0.92 between primary and every alternative; Top tier stays small (39–55), Low tier stays large (71–96). The triple bind is not a weighting artifact.

**Empirical phase.** **23 benchmarks** (~750 items each) administered to **9 models × 3 vendors** — Anthropic (Opus 4.6, Sonnet 4.6, Haiku 3.5), Google (Gemini 2.5 Flash-Lite / 2.5 Flash / 2.5 Pro / 3.1 Pro), OpenAI (GPT-5 Codex, GPT Mini) — at temperature 0, fresh context, N=1 per pair (207 unique administrations, 69 trial files). Convergence measured by coefficient of variation (CV) across the 9 models: non-discriminating <5%, weakly discriminating 5–15%, discriminating >15%. Four custom protocols (MP-CC cross-cultural, MP-DM dyadic, MP-DP dual-process, MP-SI social intuitionism) were built to cover theories with zero Top-tier instruments.

**Self-administration disclosure (load-bearing caveat):** the Claude family designed the framework AND served as 3 of 9 subjects, and one Opus orchestrator prompted all 9 models. Model-specific absolute values are therefore **hypothesis-generating, not confirming**; the *comparative* convergence finding survives because it holds across independently-built vendors.

---

## 2. Benchmark characterization framework (the feature axes)

The 162-feature framework is organized into **seven tiers**. Only Tiers A–C feed the composite; D–G profile the instrument.

- **Tier A — Psychological Depth (6 features, A1–A6; 50% of composite).** A1 construct depth / # theories engaged; A2 construct operationalization quality (weight 0.25 of PD — the single heaviest feature); A3 dilemma complexity; A4 source-instrument validation (does it adapt a validated psychometric instrument?); A5 human-baseline availability; A6 construct-validity evidence (5-level ordinal — the crisis feature).
- **Tier B — Practical Ease (7 active, B1–B4/B6–B7/B10; 30%).** Task-format suitability, dataset size, data availability, code availability, harness compatibility, scorer complexity, LLM-administration fidelity.
- **Tier C — Citation Impact (4 active, C1–C3/C5; 20%).** Total citations, age-normalized velocity, venue tier, hub/leaderboard presence.
- **Tier D — Psychometric Rigor (24, D1–D24; characterization only).** Internal consistency, test-retest, factor structure, item analysis, invariance, IRT discrimination, response entropy, effect-size reporting, etc.
- **Tier E — LLM-Specific Validity (44, E1–E44; largest tier).** Recognition-endorsement discrimination, prompt/few-shot sensitivity, tokenization/context effects, adversarial robustness, sycophancy, contamination risk, model-version sensitivity, RLHF sensitivity, CoT transparency, etc.
- **Tier F — Cultural & Philosophical Breadth (44, F1–F44).** WEIRD-bias index, individualism-collectivism balance, indigenous/marginalized inclusion, colonial/power awareness, meta-ethical awareness, moral-uncertainty expression, reflective-equilibrium testing — the empirical base for the "culturally blind" arm.
- **Tier G — Theory Fidelity & Provenance (29, G1–G29).** Theory-version currency, does-it-test-what-it-claims, inter-theory bridge items, provenance/replication/licensing.

**Design principle to steal:** separate the *selection* composite (17 core quality features) from the *characterization* profile (141 features). Folding everything into one score dilutes the signal and makes a high score uninterpretable (could reflect any mix of rigor, breadth, LLM-validity). Discrimination-tier classification (CV-based) is a separate empirical axis layered on top.

---

## 3. Key findings (exact statistics)

The paper's thesis is a **triple bind**: the landscape is theoretically narrow, empirically undiscriminating, and culturally blind. Seven numbered claims:

1. **MFT quality dominance.** Moral Foundations Theory = 67/292 candidates (23% by volume) but holds **18 of 48 top-tier slots (37.5%)** and a **73% quality rate (49/67 top+high)** — ~6x the rate of non-Western traditions. Theory quality rates: MFT 73%, Schwartz 57%, Kohlberg 56%, Trolley 48%, Islamic 36%, Buddhist 12%, Intuitionist 100% (n=3), Dyadic 50% (n=2), Ubuntu 0%, Confucian 0%, Indigenous 0%, Identity 0%, Unclassified 36%. Cause is **infrastructure, not theoretical merit**: MFT uniquely owns two computational assets — MFQ-30 (validated 30-item questionnaire w/ norms across ≥11 countries) and MFTC (35,108 expert-annotated tweets). One asset → moderate quality; two → dominant; zero → zero.

2. **Construct-validity crisis.** A6 distribution across 292: Level 5 (multi-study) 13 (4%); Level 4 (single-study) 61 (21%); Level 3 (adapts w/o LLM revalidation) 49 (17%); Level 2 (face validity) 91 (31%); Level 1 (keyword) 78 (27%). **58% sit at Level 1 or 2** (up from 17% in the 55-benchmark subsample — a 3.4x jump). Median validity dropped from Level 3 → Level 2 under full coverage. The old optimistic picture was a top-of-distribution sampling artifact.

3. **Theoretical absence.** **Dual Process Theory (~9 candidates, all Low tier) and Moral Identity Theory (2 candidates, all Low) have zero publication-ready benchmarks** despite combined citations >25,000 (Greene's 2001 fMRI paper >10,000; Aquino & Reed 2002 >3,000). Social Intuitionism was *misdetected* not missing (3 candidates, 100% quality once expanded scorer found "moral dumbfounding" vocabulary). Content-vs-process is the key axis: the landscape measures *what* models endorse (content) and neglects *how/when/why* (process).

4. **Cultural quality cliff.** Western mean quality rate **62% (93/149)** vs zero-quality traditions **0% (0/32)**. Ubuntu (13, 0%; best composite UbuntuGuard 35.1, mean 19.5), Confucian (13, 0%; composites 14.6–21.2, mean 18.1), Indigenous (4, 0%; mean 18.9), Identity (2, 0%). Islamic 36% is the intermediate case (codified jurisprudential texts as source material). Feature signature of the cliff: A4 (validated instrument) mean = 0.0 across Ubuntu/Confucian/Indigenous. Affected populations: >3 billion people (~40% of humanity) whose dominant moral frameworks the landscape cannot evaluate at any quality level.

5. **Human-baseline deficit doubled.** No-human-data rose from **18% → 34%** (100/292) under full coverage; population norms dropped 42% → **15% (43/292)**. Baseline-by-tier is steep and monotonic: Top 0% no-data / 50% population norms; Low **96% no-data** / 0% population norms. Baselines are inherited from validated instruments — no instrument, no baseline.

6. **Temporal stagnation.** Quality rate by period: pre-2020 **75%** (n=8), 2020–2022 **48%** (n=27), 2023–2026 **46%** (n=257) — flat despite **9.5x volume growth** vs pre-2020. Top-tier-only rate falls harder: 50% → 37% → 13%. Of the 257 recent candidates, 139 (54%) are Med/Low. Scaling without learning. "Hidden gems" the original subsample missed: Jiao LLM Ethics Benchmark 81.3, KorNAT 69.0, Scruples 67.0, Hendrycks Shared Human Values 67.0, ValueBench 65.8.

7. **RLHF moral fingerprint (cross-vendor).** Of 23 benchmarks, **~10 (43%) produce zero cross-model variation**; only 6 (26%) discriminate at all, 4 (17%) enough to interpret. Effective battery size ≈ 6, not 23. **Six universal signatures shared by all 9/9 models**: (1) WEIRD-liberal foundation bias (Ind/Bind ratio 2.43–2.83, humans span 0.5–3.5); (2) purity floor (~1.0 on 0–5; no human group scores at floor, secular Europeans ~2.0–2.5); (3) authority-deference suppression (win rate **exactly 0.29**, most invariant finding); (4) ethical-consistency ceiling (ECI = 1.0 on trolley; humans 0.4–0.7); (5) post-conventional default (DIT P-score 60–85, teacher-persona 90.0 for all; human adults 30–50); (6) deontological refusal asymmetry (personal-harm accept 0.10–0.50, impersonal ~0.95). **Quality predicts convergence, not discrimination: r = −0.83.** The best instruments (MFQ-30, Moral Machine, TracingMF) most emphatically confirm homogeneity. Median CV across the battery ≈ 2.1%.

---

## 4. Scoring & validity methods — what worked / what failed

**Worked:**
- **Jenks natural breaks (k=4)** over arbitrary thresholds — GVF 0.83 confirmed genuine distributional structure; robust to weighting (ρ > 0.92).
- **Separating composite (17) from characterization (141)** — kept the selection signal interpretable.
- **Restrictive null policy** (absence = 0) — produced a conservative, defensible landscape estimate.
- **Batch calibration with anchors** (Moral Machine high ~78.45, Value Kaleidoscope mid ~61.6, low anchor 15–25) — kept 46,136 score cells consistent (±3 pts).
- **Expanded keyword scorer** (65→125) — corrected a real detection bias; but note it changes counts, so findings are scorer-version-specific.
- **Confidence grades recorded but NOT used to downweight** — avoided circularity (would have penalized recent + non-Western work, the very categories under study).
- **Cross-vendor CV analysis** — the discrimination-tier framing (zero/floor/fixed/ceiling mechanisms) cleanly separated informative from redundant benchmarks.

**Failed / exposed as inadequate:**
- **Content-level instruments cannot discriminate models.** 43% zero variation; MFQ-30, Moral Machine (40M human judgments) both return CV≈0 across 9 models. Better/more precise content instruments will *confirm* convergence, not break it — the problem is dimensionality, not sensitivity.
- **DIT as a "development" measure fails for LLMs.** Non-monotonic with size (Sonnet 85 > Opus 75 > Haiku 60) and collapses to 90.0 under teacher persona — it measures alignment calibration, not development. Kohlberg's framework is a category error for entities that don't develop.
- **Instrument recognition destroys construct validity.** MP22: all 9 models hit 100% foundation-ID accuracy — they reverse-engineer the psychometric structure of public tests (Messick threat).
- **Moral dumbfounding doesn't transfer.** LLM rate 20–30% vs human 50–70%; autoregressive generation disfavors "I can't explain why." Rationalization rate fixed at 0.40 for all 9 — a generation property, not a trait.
- **N=1, single-orchestrator, self-administration** — no variance estimates; ~N=30/pair needed for inference. All model-specific numbers are hypothesis-generating.

---

## 5. Exemplar benchmarks (top-ranked)

Top of the composite distribution (from the matrix + Table T5/hidden-gems):

- **Jiao LLM Ethics Benchmark (2025, composite 81.3, MFT+Trolley)** — highest in the landscape. Three-dimensional system integrating MFQ + World Values Survey + standardized dilemmas, population norms, open GitHub codebase, multi-instrument validation. Published in *Nature Scientific Reports*. Ranked high on all three sub-scores. Flaw: recency caps citation impact; still self-administration-susceptible.
- **Language Model Alignment in Multilingual Trolley (2024, 79.17, Trolley)** — multilingual trolley battery; strong practical infrastructure.
- **Moral Machine Experiment (Awad 2018, 71.73, Trolley)** — the high calibration anchor; >40M decisions from 233 countries = unmatched population norms (A5). Flaw: returns CV=0.000 across all 9 models — perfect human baseline, zero model discrimination; a memorized position, not judgment under uncertainty.
- **KorNAT (2024, 69.0, non-English)** — Korean benchmark, top-tier; proves the cliff is *infrastructure*, not culture — a non-Western research community that built validated local instruments first. The escape-hatch exemplar.
- **Aligning AI with Shared Human Values / Hendrycks ETHICS (2021, 67.05) & Scruples (Lourie 2021, 67.03)** — theory-agnostic, crowdsourced/multi-source moral judgments. Show engineering rigor (large data, open access) can substitute for psychometric inheritance. Flaw: no single-theory grounding, so they broaden *applied* not *theoretical* coverage.
- **Islamic top-tier: QIAS/Bouchekif 60.55, Ghaly 58.45, "Sacred or Synthetic?" 58.43** — best non-Western tradition; leverage codified jurisprudential corpora.
- **Process-protocol standout: MP-DP dual-process** — the ONLY battery instrument that cleanly separated a model (Haiku CoT effect +0.125 / +25pp; all 8 others 0.000). CV 3.00 = 93x the mean top-tier CV. Not psychometrically polished, but probes a dimension RLHF doesn't homogenize.

Established battery instruments worth reusing: MFQ-30 (MP2), DIT (MP3), Moral Foundations Vignettes (MP4, 65.55), Multilingual DIT (64.90), Value Kaleidoscope (MP11), Social Chemistry 101 (MP17), M3oralBench (MP20).

---

## 6. Gaps & voids the project identified

- **Process-level theories are absent where discrimination lives.** Dual Process (0 quality), Moral Identity (0), Dyadic (n=2), Social Intuitionism (n=3 only). These ask *how/when/why* — and are precisely the instruments that separate models.
- **Motivation is unmeasured.** No benchmark evaluates whether a model's moral outputs are integrated into a self-consistent agency (moral identity theory) — a question that is *more* revealing for systems simulating a self.
- **Purity/sanctity is unevaluable.** All models floor at ~1.0; ~5B people organize moral life partly around purity/sanctity/divine obligation. No instrument engages this axis meaningfully.
- **Non-Western traditions have no psychometric infrastructure.** No validated Ubuntu / Confucian / Indigenous questionnaire, no annotated corpus, no population norms. 32 candidates, 0 usable.
- **Human baselines missing for a third of the landscape** (100/292) and 85% lack population norms — scores without interpretive anchors = pseudo-evaluation.
- **Format void:** the landscape is content-classification and Likert-heavy; it lacks process manipulations (cognitive load, deliberation resources, agent-patient structure, multi-turn Socratic challenge, persona manipulation used *diagnostically*).
- **No governance gatekeeper** enforces validation standards — the crisis is partly institutional.

---

## 7. LESSONS FOR DESIGNING NEW BENCHMARKS (the payoff)

Each lesson is traced to the finding/section that supports it.

1. **Build process-level probes, not another content instrument.** [Claim 3 + Claim 7 + §7.1.2] Content instruments returned 43% zero-variation and quality correlates with convergence at r=−0.83. The single discriminating instrument (MP-DP, CV 3.00) manipulated *reasoning process* (zero-shot vs CoT). Design manipulations of deliberative resources, cognitive load, agent-patient structure — measure *how* a judgment forms, not just what it is.

2. **A new benchmark is only worth building if it can discriminate.** [Claim 7, Table T13] Report cross-model CV as a first-class validity metric. If frontier models all score the same, the instrument measures a trained constant, not a differentiating trait. Target the process/architectural dimensions RLHF does not homogenize.

3. **Do not reuse public, recognizable items for frontier models.** [§7.7.1, MP22 = 100% foundation-ID] Models reverse-engineer psychometric structure. Obfuscate/reword items to preserve construct while defeating recognition; hold out private variants.

4. **Require construct validity ≥ Level 4 and state it.** [Claim 2 → Recommendation 2] 58% of the landscape is Level 1–2 (uninterpretable). Include at least single-study validation (factor structure or convergent/discriminant evidence). Publish the A6 level explicitly.

5. **Ship human baselines — ideally population norms.** [Claim 5 → Recommendation 3] 34% have none; a raw model score (e.g. "84% ethical") is meaningless without a human distribution. Every Top-tier instrument has baselines; inherit them from a validated source instrument or collect them.

6. **Inherit infrastructure deliberately; if none exists, build the instrument first.** [Claim 1 + §7.2] Quality is infrastructure-determined (validated questionnaire + annotated corpus + norms). For a new tradition, the first deliverable is a *validated assessment instrument*, not a benchmark paper — a multi-year prerequisite (the KorNAT sequence). Effort without infrastructure lands in Med/Low.

7. **For non-Western / underrepresented traditions, follow the KorNAT/Islamic playbook.** [Claim 4, §7.5.3] The barrier is infrastructure, not culture. Partner with in-tradition scholars + psychometricians + computational linguists; exploit codified source corpora where they exist (jurisprudential texts worked for Islamic 36%). Do not port a Western instrument onto a non-Western tradition.

8. **Separate a small selection composite from a large characterization profile.** [§3.2.1] Keep the "should I use this?" score to a few high-signal features (depth, usability, recognition); score everything else for profiling but keep it out of the headline number.

9. **Use data-driven tiering (Jenks), report GVF, and run a weighting sensitivity analysis.** [§3.3.2/§3.3.4] Avoid arbitrary thresholds; demonstrate rank stability (ρ) across alternative weightings so conclusions aren't a weighting artifact.

10. **Treat absence as informative (score 0), record confidence separately, and never downweight low-confidence to avoid circularity.** [§3.2.5–3.2.6] Especially when studying whether the landscape disadvantages recent/non-Western work.

11. **Power the empirical study: N≥30 per model-benchmark pair, temperature + prompt perturbation.** [§7.7.3] N=1 point estimates cannot support inference; a 10-point DIT gap may be within test-retest noise.

12. **Eliminate the orchestrator/self-administration confound.** [§3.5, §7.7.1–7.7.2] Use vendor-neutral direct-API orchestration with independently-designed prompt templates; never let one model family design the framework AND be a subject if absolute values matter. Cross-vendor replication is what saves comparative findings.

13. **Don't misapply human developmental/trait frameworks to LLMs.** [§5.3.1, §5.4.4] DIT "stage," moral "development," dumbfounding are cognitive-architecture-bound. Reframe outputs as calibration/default properties, and test whether the construct even transfers before interpreting the number.

14. **Prefer format diversity within a battery.** [§3.4.2] ~750 items across Likert / MCQ / forced-choice / scenario / free-text / behavioral / persona / multi-turn Socratic — so convergence can't be dismissed as a single-format training artifact. Persona manipulation (MP18) is a powerful *diagnostic*: models can produce non-WEIRD profiles on demand (Ind/Bind 2.5→0.63–0.84 under East-Asian persona), proving defaults are alignment-set, not knowledge-limited.

15. **Report quality tier + discrimination tier transparently.** [Recommendation 5] "Passes 47 benchmarks" is a quality illusion if they are Level-1 keyword instruments. Standardized tier disclosure lets downstream users weight evidence.

---

## 8. File pointers

- **Feature matrix (292 × 158):** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/20260405-full-292-feature-matrix.json` (keys: `summary` {total, jenks_breaks, tier_counts}, `matrix` [292 entries: file, short_title, year, info_tier, theories, source, publication, scores{feature→{score,confidence,evidence}}, composites{PD,PE,CI,COMPOSITE}, tier]).
- **Paper v5 sections:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/PAPER-v5/sections/`
  - `20260413-methodology-v5.md` (framework, composite formula, Jenks, cross-vendor design, self-admin disclosure)
  - `20260413-results-landscape-claims1-3-v5.md` (MFT dominance Table T5; validity crisis Table T6; theoretical absence Table T7)
  - `20260413-results-landscape-claims4-6-v5.md` (cultural cliff Table 8; baseline deficit Tables 9/10a; stagnation Table 10b; hidden gems Table 11)
  - `20260413-results-empirical-v5.md` (Claim 7; discrimination tiers T13; six signatures T14; theory-by-theory T17–T21; DIT paradox T15/T16; Haiku CoT)
  - `20260413-results-integrated-v5.md`, `20260413-discussion-v5.md` (triple-bind synthesis, infrastructure determinism §7.2, RLHF-as-curriculum §7.4, 7 recommendations Tables T28/T29, limitations §7.7), `20260413-introduction-v5.md`, `20260413-abstract-v5.md`, `20260413-conclusion-v5.md`
- **Supplementary:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/PAPER-v5/supplementary/` (`20260413-supp-methods-v5.md`, `20260413-supp-tables-v5.md`, `20260413-supp-figures-v5.md`)
- **Cross-vendor analysis + data:** `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH/ANALYSIS/` — `20260404-cross-vendor-council-analysis{,-part1,-part2}.md`, `20260404-cross-vendor-dashboard-data.json`, `20260404-analyses-A-C.json` / `-D.json` / `-E-H.json`, `20260405-tier-assignment.json`, build scripts `20260404-run-analyses-AC.py` / `20260404-build-analyses-D.py`.

*Anchor numbers to re-cite exactly: 2,099 corpus; 292 candidates; 13 theories; 162 features (158 active, 17 composite); Jenks [27.8, 43.05, 56.65] GVF 0.83; tiers 48/89/72/83; MFT 73% & 18/48; validity 58% Level 1–2; DPT/Identity 0 publication-ready; non-Western 0% (32 candidates); baseline 18%→34%; quality flat 75%/48%/46% at 9.5x volume; 6 RLHF signatures 9/9; 43% zero-variation; authority win 0.29; r=−0.83.*
