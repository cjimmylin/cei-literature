# NormEval Digest — Meta-Evaluation of 54 Normative-Ethics Benchmarks (54 × 26 features, 9 LLMs, 3 vendors)

> Source project: `NORM-ETHICS/` — paper "Three Ethical Profiles, One Knowledge Ceiling"
> (v2.2-preliminary, 2026-04-13). This digest distills the completed project's conclusions for
> downstream benchmark designers. Quantitative claims are copied verbatim from the source; do not
> recompute. **Read the disclosure in §3 note before citing any cross-vendor number.**

---

## 1. Project scope & method

NormEval is the first systematic meta-evaluation of **normative-ethics benchmarks** for LLMs —
benchmarks that present models with morally valenced stimuli and score responses against one or more
normative frameworks (what one *ought* to do). It excludes descriptive ethics, metaethics,
safety/toxicity, and bias/fairness benchmarks (§6.2). The corpus spans **54 benchmarks published
2021–2026**, characterized along **26 features** grouped into 4 axes, of which **24 pass hard gates**
and **15 were empirically trialed (T1–T15)** on up to **9 models from 3 vendors**, producing **114
comparable items across 10 cross-vendor benchmarks**.

**Corpus assembly (§3.1)** was two-stage. Stage 1 mined the CEI Literature Vault (2,946 AI-ethics
papers): an initial query returned 41 papers tagged as normative-ethics benchmarks; manual review
confirmed 30 as genuine instruments (11 reclassified as borderline). Stage 2 ran a PRISMA-compliant
search across 7 databases (arXiv, Semantic Scholar, ACL Anthology, Google Scholar, PapersWithCode,
OpenReview, HuggingFace Hub) with 10 query sets, deliberately over-sampling care and contractarian
queries to counter anticipated voids. The search returned 30 external candidates after dedup; 13 met
all 4 inclusion criteria (peer-reviewed/preprint; explicit LLM normative evaluation; 2021–2026;
scoreable instrument). The final corpus of 54 grew from the seed of 30 via 12 previously-untagged
vault benchmarks + 5 new external papers ingested.

**Scoring pipeline (§3.2–3.3).** Each benchmark scored on 26 features (single rater = first author,
with calibration anchors for the highest-stakes feature). Three axis scores normalized to 0–100 feed
a composite:

- **ND = A2×25 + A6×20 + A1×15 + A3×15 + A5×15 + A4×10** (Normative Depth)
- **PE = B7×30 + B3×20 + B4×15 + B6×15 + B9×10 + B5×10** (Practical Ease)
- **CI = C2×35 + C4×30 + C3×20 + C5×15** (Citation Impact)
- **COMPOSITE = ND×0.40 + PE×0.35 + CI×0.25**

**Hard gates:** (1) ND ≥ 40 and (2) publicly available data. Of 54: 14 failed the ND gate alone, 21
lacked public data alone, 5 failed both → **24 pass both gates**. Weight sensitivity: re-ran rankings
under 18 alternative weight combos; Top 10 was **94% stable**, no benchmark moved > 3 rank positions.

**Trials (§3.4).** Phase 1 (T1–T5): 5 benchmarks × Claude Opus 4.6, 20–50 items each, spanning
composite Rank 1→10, to detect ceiling effects and validate composite-vs-discriminative power. Phase
2 (T6–T15): 10 benchmarks × 9 models (Anthropic: Opus 4.6, Sonnet 4.6, Haiku 4.5; OpenAI: GPT-5,
GPT-5-mini; Google: Gemini 2.5 Flash, 2.5 Flash-Lite, 2.5 Pro, 3.1 Pro), temperature = 0, identical
prompts → 114 comparable items. Scoring was **native to each benchmark** (never aggregated across
types): binary exact-match, expert rubric (0–4), framework-disaggregated accuracy, Likert scale
(OUS IH/IB), free-text behavioral coding, pluralistic-alignment scoring.

**Feature-matrix data summary** (from `20260404-normeval-expanded-feature-matrix.json`, 54 rows × 50
fields, verified by script): ND_score min 15.2 / median 55.4 / max 87.0 / mean 53.0; PE_score min
12.0 / median 66.5 / max 95.0 / mean 57.8; CI_score min 12.0 / median 25.8 / max 80.0 / mean 30.0;
COMPOSITE min 22.8 / median 49.3 / max 77.2 / mean 48.8. A1_count (traditions) median 2, max 5.
Dataset size (n=49 with data) median 1,000, max 257,609. Citation count median 4, max 843.
`passes_gates`=24. A3_reasoning: "judgment only"=31, "reasoning process"=10, "both"=8+5=13.
B1_format: Scenario-based 22, Mixed 20, Pairwise 4, MCQ 3, Open-ended 3, Binary 2. Domain: General
40, Healthcare/Medical 6, others singletons.

---

## 2. Benchmark characterization framework (the 26-feature × 4-axis taxonomy)

The reusable contribution for a designer is the **feature taxonomy** itself. Each axis and what it
captures:

**Axis A — Normative Depth (A1–A8): philosophical rigor.**
- A1 traditions tested (integer 1–5)
- A2 depth of ethical engagement (ordinal 1–5, keyword-mention → framework-grounded scenario) — **25% of ND**
- A3 judgment / reasoning / both (categorical J/R/B) — **15%**
- A4 treatment of moral uncertainty & disagreement (binary) — **10%**
- A5 pluralistic coverage of competing perspectives within one item set (ordinal 1–5) — **15%**
- A6 philosophical grounding quality (calibrated 1–5) — **20% of ND, the single most consequential feature**
- A7 cultural framing beyond Western/WEIRD (ordinal 1–3)
- A8 multilingual support (integer language count)

**A6 calibration anchors** (reusable): MoReBench = 5 (expert rubric, procedural reasoning under 5
named traditions); ETHICS = 3 (names traditions, operationalizes as classification without required
justification); Hui *Decoding Moral* = 1 (ethics vocabulary, no substantive engagement).

**Axis B — Practical Ease (B1–B9): implementability.** B1 task format; B2 dataset size; B3 public
data (binary) — **20% of PE**; B4 code availability — **15%**; B5 license; B6 harness compatibility
across 6 frameworks (integer 0–6) — **15%**; B7 overall implementability judgment (ordinal 1–5) —
**30%, PE's dominant term**; B8 scorer type (automated exact-match → expert rubric); B9 model
compatibility (API vs open-weight, 1–3).

**Axis C — Citation Impact (C1–C5): community uptake.** C1 raw citations; C2 age-normalized
citations/year — **35% of CI**; C3 venue tier (1–5); C4 downstream adoption count — **30%**; C5
leaderboard presence (binary).

**Axis D — Metadata (D1–D4): provenance.** Publication year, first-author affiliation, primary
language, domain focus (general / medical / legal / cultural).

Two derived constructs anchor the empirical half of the project: **five normative traditions** —
Virtue (V), Deontological (D), Utilitarian (U), Care (C), Contractarian (Co) — and the
**judgment-vs-reasoning** distinction (testing *what* a model concludes vs. *how* it reasons). A
third construct set emerges only cross-vendor: **ethical profiles** defined by Instrumental Harm
(IH, OUS subscale 1–7), Impartial Beneficence (IB, 1–7), Cognitive Bias Rate (CBR), and persuasion
resistance.

---

## 3. Key findings

**IMPORTANT DISCLOSURE (from abstract + §6.1):** the non-Anthropic results (GPT-5, GPT-5-mini, all 4
Gemini) were generated by **in-context elicitation by a Claude/Codex sub-agent, NOT direct API calls**
to OpenAI or Google. Cross-vendor findings **F1–F7 are exploratory hypotheses** ("Claude's elicited
model of cross-vendor variation"), pending external replication. The **landscape claims C1–C5** and
**within-Anthropic trials T1–T5** are unaffected and empirically grounded.

### Landscape claims (C1–C5, n=54, empirically grounded)

1. **Ceiling effect (C1).** ETHICS [Hendrycks2021] produces **100% accuracy across all 9 models**
   (binomial, **p < 1×10⁻¹⁵**). Saturated; supports retirement from active evaluation.
2. **Consequentialist bias (C2).** LLMs achieve **77% utilitarian vs 50% deontological accuracy**
   (two-proportion **z = 2.17, p = 0.015, Cohen's h = 0.57**), a 27-point gap. Confirmed across
   vendors, magnitude h = 0.42 (Haiku) to 0.71 (GPT-5). Framework difficulty hierarchy on
   MoralReason-QA: **U = 77% (23/30) > V = 63% (19/30) > D = 50% (15/30)**; joint (all three correct)
   only **37% (11/30)**.
3. **Care/contractarian void (C3).** Only **2/54** benchmarks reach substantive care-ethics engagement
   (binomial vs 20% expected, **p < 0.001**) and **4/54** contractarian (**p < 0.01**). Zero
   dedicated care-ethics instruments grounded in Gilligan/Noddings/Tronto exist in the corpus.
4. **Reasoning deficit (C4).** Only **10/54 (18.5%)** test moral reasoning; **44 (81.5%)** test
   judgment only (binomial vs 50%, **p < 0.001, exact p = 6.3×10⁻⁶**). Three-category breakdown:
   judgment-only J = 22, both B = 12, reasoning-only R = 10.
5. **Data bottleneck (C5).** No significant ND difference between gate-passing and gate-failing
   benchmarks (**Mann-Whitney U = 287, p = 0.605, r = 0.07**; n₁=36 available, n₂=18 unavailable).
   Median ND is actually *higher* among unavailable (58.8) than available (53.0). The gate reflects
   **sociology, not quality**. Chakraborty, Rao, Zhou collectively = 235 ND points lost to the data gate.

**Landscape structure (§4.1).** Tradition coverage (any / substantive): Utilitarian 43/30,
Deontological 40/29, Virtue 28/18, Care 13/2, Contractarian ≈/4. Data availability: 36/54 (67%)
public (23 GitHub, 6 HuggingFace, 7 other); 18 (33%) none. **42/54 (78%) engage zero non-Western
ethical content.** Composite distribution is long-tailed: Rank 1 (77.2) → Rank 2 (70.2) gap = 7.0
(largest); the other 23 form a compressed continuum, median inter-rank gap in the bottom half = 1.2.

### Discriminative inversion (T1–T5, §4.4, grounded)

6. Discriminative power **inverts** composite rank:
   **MoReBench > MoralReason-QA > Moral Lens > DailyDilemmas > ETHICS.** ETHICS (Rank 1) produces
   *zero* discriminative power (100% ceiling); MoReBench (Rank 2) produces the highest (10% rubric
   coverage, 66/688 criteria met, with a 14.3-pt inter-tradition spread: Scanlonian 18.3% > Kantian
   13.3% > Act-utilitarian 8.7% > Gauthierian 5.5% > Virtue 4.0%). Cause: composite weights PE+CI =
   60%, properties orthogonal to (here negatively correlated with) discriminative power.
7. **Moral Lens refusal finding (T4):** on 40% of items (8/20) the model refused to choose — all on
   scenarios where gender, fitness, or SES was the sole 1:1 differentiator. Refusal is itself a
   normative position (egalitarian deontology) encoded by safety training.

### Cross-vendor findings (F1–F7, EXPLORATORY / elicited — see disclosure)

8. **F1 Three ethical profiles** that cluster by posture, not vendor: **Conservative** (GPT-5 IH=2.93,
   Opus IH=3.0), **Moderate** (Sonnet IH=3.2, GPT-5-mini IH=3.2), **Permissive** (Haiku + all 4
   Gemini, IH=4.47). IB stays flat (range 0.26: GPT-5 5.13, Sonnet 5.0, Haiku/Gemini 4.87) while IH
   ranges 1.54. **IB−IH gap** = diagnostic signature: GPT-5 2.20 (largest) > Sonnet 1.80 >
   Haiku/Gemini 0.40 (≈ trained utilitarian philosophers). Council 11/12 robust (psychometrics abstained).
9. **F2 Gemini identity.** All 4 Gemini models produce **byte-identical responses on all 114 items**;
   probability under independence ≈ **2⁻³⁴² ≈ 10⁻¹⁰³**. All 4 Gemini also = **100% identical to Claude
   Haiku 4.5** on all 114 items. Council 8/12 favored shared-infrastructure hypothesis for intra-Gemini.
10. **F3 Universal knowledge ceiling.** 4 benchmarks (T6 PrinciplismQA, T9 JETHICS, T11 MedEthicsQA,
    T15 ProMoral-Bench) = 100% for all 9 models → **44/114 items (38.6%) at difficulty = 1.0**,
    zero discriminating information. Effective battery = **70/114 items (61.4%)**.
11. **F4 Knowledge–judgment divergence** (council **unanimous 12/12**). Knowledge items: 0% variance,
    0/44 max pairwise disagreement. Judgment items: up to **33/55 (60%) disagreement** (GPT-5 vs
    Haiku). A construct-level split, not an item-difficulty artifact.
12. **F5 GPT-5 most conservative:** IH 2.93 (below lay range ~3.0–3.5), IB 5.13 (highest),
    IB−IH gap 2.20 (largest), CBR 46.2%, persuasion change 0%.
13. **F6 Clustering by profile, not vendor:** highest cross-vendor agreement Sonnet–GPT-5 **90.4%
    (103/114, κ≈0.72 "substantial")** *exceeds* intra-vendor Sonnet–Haiku **74.6% (κ≈0.18 "slight")**.
    Gap of 15.8 pts with non-overlapping CIs. GPT-5–GPT-5-mini 86.8%; Gemini intra-family 100%.
14. **F7 Persuasion resistance non-monotonic:** Opus 66.7% (2/3) > Haiku 33.3% (1/3) > Sonnet 0%
    (0/3); GPT-5 and GPT-5-mini also 0%. The most capable Anthropic model is the *most* persuadable.
    **Statistically fragile — only 3 items.**

### Care-ethics prototype (§3.6, Appendix H)

15. A Tronto-4-phase, 10-scenario, multi-turn care benchmark administered to Opus 4.6 scored **132/160
    rubric points = 82.5%**, mean 13.2/16 per scenario. Per-dimension: **Attentiveness 3.6 (strongest)
    > Responsibility 3.4 > Competence 3.2 > Responsiveness 2.8 (weakest)**. Single-turn pilot scored
    Responsiveness only 1.2/4.0 vs 2.8 multi-turn (+1.6) — proving multi-turn is a *structural
    requirement*, not a preference. The Responsiveness deficit maps to the "provider fallacy"
    [Kittay1999]: the model evaluates care from the caregiver's, not the recipient's, standpoint.

---

## 4. Scoring & validity methods — what worked / what failed

**Worked:**
- **Native per-benchmark scoring, never aggregated across metric types.** Preserved each instrument's
  construct (binary accuracy ≠ rubric score ≠ IH mean). Essential given the 15 benchmarks use
  fundamentally different paradigms.
- **A6 calibration anchors** (three benchmarks fixing 1/3/5) made the highest-weight, most-subjective
  feature defensible under single-rater scoring.
- **Hard gates + weight-sensitivity sweep (18 configs).** Top-10 94% stable → composite ordering is
  robust to weight choice even though the composite is a *poor* predictor of discriminative power.
- **Rubric-based procedural scoring (MoReBench, 688 criteria).** The only method that produced
  discriminative signal at the frontier; penalizes generic ethical language, rewards
  framework-specific methodology (categorical imperative, veil of ignorance, reasonable-rejectability).
- **OUS IH/IB decomposition** against the Kahane et al. (2012) reference populations. Separating
  positive (IB) from negative (IH) utilitarianism is what surfaced the three profiles.
- **Knowledge/judgment split reporting** — the council's only unanimous methodological recommendation.
- **Chance-corrected agreement (Cohen's κ, Clopper-Pearson CIs).** Sharpened rather than dissolved the
  cluster structure.

**Failed / limited:**
- **Composite rank as a quality signal.** Citation count and harness integration are poor proxies once
  the frontier passes a benchmark's ceiling; ETHICS ranks #1 yet discriminates nothing.
- **Single-rater feature scoring** — no inter-rater reliability (κ) computed; ND/reasoning/tradition
  features are the most subjective. Explicitly flagged as the top internal-validity concern.
- **Effective battery too small.** 70 discriminating items / 8 models ≈ 8.75 items/model, below the
  psychometric minimum of 10–15 [Nunnally1994]. Profile point estimates carry wide CIs; the
  Conservative–Moderate boundary (0.2 IH points) may dissolve with a larger battery.
- **Profiles over-concentrated:** T13 (OUS, 30 items) + T14 (Cognitive Biases, 22) = 52/70 (74.3%) of
  discriminating items → Dissent A.
- **Post-hoc battery.** The 114-item set was never designed as a unified instrument; no unidimensionality
  or Cronbach's-α assumptions hold. Positioned as *exploratory*, not confirmatory.
- **Codex-wrapper confound.** GPT-5 / GPT-5-mini accessed via Codex agent (elicitation), adding a
  system-prompt layer; their profiles are "the Codex product's profile," asymmetric with Claude/Gemini.
- **Temperature-0 constraint.** Gemini identity may be a deterministic-decoding artifact — untested at
  temp > 0. Persuasion (T7) rests on 3 items; Haiku T13 on a single administration.
- **Care ethics has no automated scorer.** Requires interpretive human judgment; single-rater, n=10,
  no ICC — a proof-of-concept, not validated.

---

## 5. Exemplar benchmarks (top-ranked; what / why-high / remaining flaws)

Top 10 by composite (from JSON, matches Table 2):

1. **ETHICS** [Hendrycks2021] — Composite **77.2** (ND 59.8, PE 95.0, CI 80.0). 130,000 items, 5
   categories, in 4 harnesses, 843 citations. High because of exceptional ease + citation, not depth.
   **Flaw: saturated — 100% on all 9 models, zero discriminative power; solvable by sentiment
   pattern-matching. Retire.**
2. **MoReBench** [Chiu2025] — **70.2** (ND **87.0 = highest in corpus**, PE 82.5, CI 26.3). Only
   benchmark with A6=5; tests *procedural* reasoning via a 688-criteria expert rubric across 4
   traditions incl. contractarianism. Highest discriminative power. **Flaw: low uptake (CI 26.3),
   expensive human rubric scoring, only 1/6 harness-accessible.**
3. **PrinciplismQA** [Hong2025] — **67.9** (ND 85.0). 3,648 items in biomedical principlism; one of
   only 2 substantive care-ethics benchmarks. **Flaw: knowledge-ceiling (100% all models); Western
   Beauchamp-Childress framing.**
4. **Moral Persuasion** [Huang2024] — **67.6** (ND 79.8). Compact 108 items testing whether framed
   moral arguments change a model's judgment — tests flexibility, not position. **Flaw: only 3 items
   reached the cross-vendor persuasion trial → fragile F7.**
5. **MoralReason-QA** [An2025] — **65.5** (ND 80.0). 2,040 items, 3 traditions, framework-specific
   reasoning traces (AAAI 2025). Source of the U>V>D difficulty hierarchy. **Flaw: high-ambiguity
   scenarios, joint accuracy only 37%.**
6. **Moral Lens** [Samway2025] — **63.5**. 640 self-driving scenarios classified into 16 rationales
   (EMNLP 2025). **Flaw: better as an alignment-bias detector than accuracy benchmark; 40% refusal
   rate with no standardized scoring.**
7. **Beyond Ethical Alignment / AMAeval** [Galatolo2025] — **61.7**. Only benchmark testing *abductive*
   moral reasoning; 1,090 scenarios (ECAI 2025).
8. **One Model Many Morals** [id 45] — **59.7**. Largest top-10 dataset (130,148 items), 6 languages,
   LLM-as-judge across 10 frameworks (ICLR 2026). First large-scale cross-linguistic normative benchmark.
9. **JETHICS** [Takeshita2025] — **59.4**. 78,000 Japanese items; only corpus benchmark engaging
   Confucian/Buddhist/Shinto concepts. **Flaw: ND inherited from ETHICS template; ceiling for all
   models → 0 discriminating info; administered in English here.**
10. **Pluralistic Moral Gap** [Russo2025] — **59.3** (ND 82.8, 3rd-highest). 1,618 items, graduated
    consensus levels; a constructivist benchmark that explicitly tests moral uncertainty. **Flaw: low
    PE (56.5) from operational complexity.**

Other notable: **Greatest Good / OUS** (Rank 16, the primary utilitarian instrument in the
cross-vendor analysis — validated Oxford Utilitarianism Scale, IH/IB subscales); **PNAS Cognitive
Biases** (Rank 18, 22 items but high discriminative power, top-tier venue); **DailyDilemmas** (Rank
11, deliberately no ground-truth — a value-profiling tool, not an accuracy benchmark).

---

## 6. Gaps & voids the project identified

1. **Care-ethics void.** 2/54 substantive; **zero dedicated** Gilligan/Noddings/Tronto instruments.
   Root cause is structural: 36/54 (67%) use single-turn vignettes; care ethics is relational,
   processual, multi-turn — incompatible with forced-choice format (§5.5, Appendix H).
2. **Contractarian void.** 4/54 substantive. **No standalone Rawlsian** benchmark (original position,
   veil of ignorance, difference principle) and **no standalone Scanlonian** (reasonable-rejectability)
   benchmark exists. Unlike care, this gap is *tractable* within existing scenario formats — its
   absence is sociological (trolley problems have more cultural salience than the veil of ignorance).
3. **Reasoning void.** 44/54 test judgment only; the field can't distinguish a model that reasons well
   from one that pattern-matches. Rubric-based reasoning scoring is expensive → path of least
   resistance produces judgment-only benchmarks.
4. **Non-Western void.** 78% engage zero non-Western content. The three profiles are profiles of
   *Western* moral reasoning; the IH–IB axis presupposes a utilitarian-deontological tension marginal
   to Confucian role ethics, Islamic maqasid al-shari'ah, Ubuntu, Indigenous frameworks. The entire
   IH band across 9 models = 2.93–4.47 on 1–7 — a narrow Western slice vs. the cross-national spread
   documented by Moral Machine across 130 countries [Awad2018].
5. **Moral-realism monoculture.** ~41/54 (76%) assume dilemmas have determinately correct answers —
   in tension with care ethics and pluralism, and both a cause and consequence of the tradition imbalance.
6. **Refusal-handling void.** No benchmark has a standardized refusal protocol; refusal rates vary 20+
   points across vendors, silently confounding reported accuracy.
7. **No shared index / literature dispersal.** 6/24 gate-passing benchmarks were newly identified
   external papers; surveys by Snoswell (69 papers) and Rismani (791 measures) each miss benchmarks in
   this corpus and vice versa. The field lacks a shared benchmark index.
8. **No graduation protocol.** The field has no mechanism to recognize and retire saturated benchmarks;
   ETHICS remains the primary normative component of HELM, DecodingTrust, TrustLLM.

---

## 7. LESSONS FOR DESIGNING NEW BENCHMARKS (the payoff)

Each lesson is traced to the finding/appendix that supports it.

**L1 — Test reasoning, not just judgment.** Only 10/54 test reasoning (C4, p<0.001). Rubric-based
procedural scoring (MoReBench, T2) is feasible and yields dramatically higher discriminative power
(10% rubric coverage vs 100% ETHICS ceiling). Design rubric criteria that require identifying
principles, articulating tradeoffs, and justifying with *framework-specific* methodology; penalize
generic ethical language. → Discussion Rec 1; T2/T3.

**L2 — Ship hard variants / adversarial splits on day one.** The ETHICS ceiling was predictable and
is *universal* (all 9 models, 44/114 items at difficulty 1.0). Release parametrically harder versions,
OOD splits, or adaptively-calibrated difficulty at launch to stay informative across ≥2 model
generations. → Rec 2; C1, F3.

**L3 — Prefer discriminative power over convenience metrics.** Composite rank *inverts* discriminative
power; 60% of composite rewards ease + citations, orthogonal to differentiation. Do NOT select
benchmarks by citation count or harness integration; measure whether the benchmark produces variance
across current frontier models. → §4.4 inversion.

**L4 — Separate knowledge and judgment metrics, with explicit item counts.** Aggregate accuracy
conflates capability (knowledge, converges to 100%) with alignment (judgment, diverges up to 60%). An
85% score decomposing to 100%/70% has entirely different deployment meaning than 85%/85%. Council's
*only unanimous* recommendation. → Rec 6; F4.

**L5 — Validate across ≥3 models and ≥2 vendors; report pairwise agreement.** Single-vendor
benchmarking cannot detect the profile phenomenon: a "model" finding (high IH) may be a "vendor"
finding, and a single-model finding (ETHICS ceiling) may be universal. Cost is modest (hours);
interpretive gains are large. → Rec 7; F1, F6. *(NB: in this project cross-vendor data were elicited,
not API-measured — so also: use direct APIs, not agent-wrapper elicitation, to avoid the Codex confound.)*

**L6 — Release data + code under a permissive license concurrent with publication.** 33% of benchmarks
have no public data, and unavailability is uncorrelated with quality (C5, p=0.605). Data unavailability
is *the* practical bottleneck — it blocks replication, harness inclusion, and visibility. → Rec 4; C5.

**L7 — Standardize refusal handling as a first-class metric.** Refusal is a normative position (T4:
40% refusal encoding egalitarian deontology) and varies 20+ points across vendors. Specify which items
are expected to elicit refusals, how they are scored, and report refusal rate alongside accuracy, with
include/exclude scoring variants. → Rec 5; §5.7, T4.

**L8 — For care ethics, build multi-turn relational scenarios with recipient-standpoint scoring.**
Single-turn vignettes structurally cannot test Competence or Responsiveness (single-turn Responsiveness
1.2/4.0 vs 2.8 multi-turn). Use Tronto's 4 phases (Attentiveness, Responsibility, Competence,
Responsiveness) as scorable dimensions; explicitly reveal the care-recipient's reaction in a later
turn and score whether the model adopts the recipient's standpoint (guards against the provider
fallacy). Accept that care ethics resists automated scoring — plan for LLM-as-judge + inter-rater ICC≥0.70.
→ Appendix H; C3.

**L9 — Cover all five traditions, or explicitly declare scope.** Corpus defaults to
utilitarian+deontological because those formalize into classification tasks; care and contractarian
require representing relationships and procedural reasoning. Declare excluded traditions so users don't
mistake partial for comprehensive coverage. Contractarian is *tractable now* — operationalize the
original position / reasonable-rejectability in existing scenario formats. → Rec 3; §4.1, §5.5.

**L10 — Design against the consequentialist-bias attractor.** Models are measurably better at
utilitarian (77%) than deontological (50%) reasoning, and share high IB but divergent IH. Include items
that isolate deontological duty-to-protect and instrumental-harm refusal (the "inaction=deontological"
heuristic fails on duty-to-protect scenarios), and use the IB−IH gap as a diagnostic. → C2; T3; §5.2–5.3.

**L11 — Use calibration anchors + multiple raters for subjective features.** The 26-feature scheme
worked but was single-rater with no κ. Fix the highest-weight subjective feature (A6) with 1/3/5
exemplar anchors; recruit ≥2 raters and report Cohen's κ (target ≥0.60) for ND, reasoning depth, and
tradition engagement. → §6.1 limitations.

**L12 — Size the discriminating battery, not the raw battery.** Ceiling items contribute zero
information; a battery of only discriminating items would be 61% shorter and 100% more informative.
Target ≥10–15 *discriminating* items per model [Nunnally1994]; avoid concentrating the signal in 1–2
sub-benchmarks (here 74.3% came from OUS+PNAS). → §5.1, §6.1; F3.

**L13 — Build for non-Western traditions as equal-status instruments.** Western-framed benchmarks
cannot be fixed by adding more of the same. Commission benchmarks grounded *within* Confucian, Islamic,
Ubuntu, Indigenous frameworks where the salient moral axis is not IH–IB. → §5.9; council 11/12.

**L14 — Adopt a benchmark graduation protocol.** When discriminative power drops below threshold across
k (≥3) consecutive frontier vendors, move the benchmark to verified-baseline status and exclude from
active suites; ship hard variants to extend life. → §5.1; C1/F3.

**L15 — Test at non-zero temperature and re-administer.** Temp-0 can manufacture artifacts (Gemini
byte-identity; single-administration IH anchors). Re-run at temp>0 to distinguish genuine convergence
from deterministic-decoding artifact. → §6.2; F2.

---

## 8. File pointers

**Paper draft (v2.2-preliminary):** `NORM-ETHICS/PAPER-v2.2/source/`
- `spine-…md` (title, 5 claims, 7 findings, glossary, figure/table map — best single overview)
- `methods-…md` (§3 pipeline, scoring formulas, trial protocol, statistical methods)
- `results-landscape-…md` (§4.1–4.2 landscape + full Top-24 ranking with per-benchmark notes)
- `results-trials-…md` (§4.3–4.4 T1–T5, discriminative inversion)
- `results-crossvendor-…md` (§4.5–4.6 F1–F7, agreement matrices)
- `discussion-…md` (§5.1–5.9, incl. the 7 benchmark-design recommendations in §5.8)
- `limitations-…md` (§6, incl. the revised elicitation disclosure — read before citing F1–F7)
- `abstract-…md`, `conclusion-…md`, `references-…md`, `appendix-k-prompt-provenance-…md`

**Supplement appendices:** `NORM-ETHICS/PAPER-v2/supplement/`
- `appendix-A-feature-matrix.md` — full 54×26 matrix (Table S1)
- `appendix-B-scoring-methodology.md` — formulas, calibration anchors, 18-config weight sensitivity (Table S2)
- `appendix-C-trials-T1-T5.md`, `appendix-D-trials-T6-T15.md` — per-item results (Tables S3–S17)
- `appendix-E-excluded-benchmarks.md` — the 30 gate-failing benchmarks with failure reasons (Table S18)
- `appendix-F-harness-matrix.md` — 54×6 harness compatibility (Table S19)
- `appendix-G-statistical-methods.md` — hypothesis tests C1–C5 + pairwise CIs (Tables S20–S21)
- `appendix-H-care-ethics-prototype.md` — Tronto 10-scenario prototype (Table S22)
- `appendix-I-v2-features.md` — v2 feature distributions + non-Western heatmap (Figures S1–S2)
- `appendix-J-council-deliberation.md` — 12-member council votes, 3 dissents, 10 recommendations

**Data:** `NORM-ETHICS/STATISTICS/20260404-normeval-expanded-feature-matrix.json` (54 rows × 50 fields —
the machine-readable feature matrix; fields incl. ND_score, PE_score, CI_score, COMPOSITE, gate_ND,
gate_data, passes_gates, A1–A8, B1–B9, C1–C5, D1–D4).

**Dashboards:** v1 https://cjimmylin.github.io/cei-normeval-dashboard/ · v2 …-v2/ · v3 …-v3/ ·
v4 …-v4/ (cold-readable, with glossary + preliminary-data disclosures).

---

*Digest generated 2026-07-05 for the CEI COOKBOOK evidence layer. All quantitative claims copied from
the v2.2-preliminary source; cross-vendor findings F1–F7 are elicited (not API-measured) and marked
exploratory per the source's own disclosure.*
