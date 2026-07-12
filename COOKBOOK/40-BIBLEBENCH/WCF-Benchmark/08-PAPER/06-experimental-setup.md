<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 5. Experimental Setup (Pre-Registered)

> **This section was written from the pre-registration BEFORE the gated run.** Every
> quantity, formula, threshold, and procedure below was fixed and frozen prior to the
> first paid model call; none of it is chosen or tuned in light of results. The
> pre-registration becomes immutable the moment the first gated datum exists (the first
> paid call). After that moment, **any deviation requires a logged ruling recorded before
> proceeding, and a silent deviation voids the affected gate** — the gate is then reported
> INVALID-DEVIATION and is non-quotable until a ruled disposition. Amendments made before
> the run are recorded as separate dated files and never edit the pre-registration itself.

## 5.1 Items in scope

The instrument is the frozen bank of **230 items** — 10 method-major designs of 22–24
items each. By tier the bank comprises T2 = 55, T2a = 26, T2b = 30, T3 = 70, and T4 = 49
items; by track, Track A = 71 and Track B = 159. There is **no T1 tier** in this bank:
wherever the design spine refers to "T2+" scope, we mean the entire gold-scored bank, and
"hard tier" means the union **T3 ∪ T4**.

Items are dispositioned for the run as follows:

| Class | n | Disposition |
|---|---|---|
| Core runnable | 204 | Run on the full roster. |
| EPISODE (multi-turn) items | 22 | Run on the full roster only if the applied registry and its build items are green at launch; scored with a mechanical outcome classifier used as a **SCREEN**, and a rubric-based judge score of record on the persisted transcripts. If not green, they are excluded, reported as "pending registry approval" (never silently absent), and every gate row they touch discloses the reduced scope. |
| Dev-set-only liberty legs | 4 | **Not run** (dev-set hygiene); scoring class is calibrated-abstention. |
| Contested items (AGG-C7-007, AGG-C3-W302, AGG-C5-W304, AGG-C8-W305) | 4 | Run, but **excluded from every gold-accuracy computation** (the G1/G2/G3/G5 scopes); scored on adherence/disclosure/coherence only. Their settled-core keypoints remain right/wrong-scored. |

The PROOF scorer kind (citation-anchored items, 23 items) is scored under a **ruled
mechanical citation gate**, with a standing known-artifact disclosure in every table in
which it appears; no judge-assisted anchor scoring path exists and none is created for
this run. Fresh-per-run item generation is not built and is out of scope for the gated
run — the frozen bank is the instrument, and this is disclosed.

## 5.2 System-under-test (SUT) roster — selected by formula

The roster is **10 SUTs**, assembled mechanically at pre-flight and recorded in the run
manifest before the first paid call. It is thereafter unchangeable except by a logged
ruling.

**Anti-leakage rule (binding).** No SUT may come from the judge families **{google,
x-ai}** or from the item-generator family **{anthropic}** (the bank was authored with
models of that family). This deliberately excludes the true global frontier from the
roster by construction. As a disclosed consequence, the headroom and separation gates
(G2/G3) measure **roster-frontier** headroom and separation, not global-frontier
headroom and separation — the cost of keeping judges and item generators independent of
the systems under test.

The 10 SUTs are assembled by the following formula:

1. **Five formula-selected frontier candidates.** For each family in
   {openai, deepseek, qwen/alibaba, moonshotai, meta-llama}, select that family's
   available, text-capable, non-preview model with the **highest LMArena text Elo** in the
   frozen capability CSV. A family with no listed available model is replaced, by the same
   formula, from the fallback order **z-ai → nvidia → microsoft**.
2. **Three continuity pins (verbatim model slugs):** `deepseek/deepseek-chat`,
   `mistralai/mistral-large-2512`, and `meta-llama/llama-3.1-8b-instruct`. The 8B model is
   a deliberate low-capability anchor, present so the capability-correlation gate has
   spread to measure.
3. **Two mid-tier pins:** `cohere/command-a` and `amazon/nova-pro-v1`. (These families
   were previously screened in this project as judge candidates; a judge-screen failure
   does not disqualify a model as an SUT, and neither family judges anything of record.)

**De-dup rule:** if a formula pick equals a pinned slug, the roster shrinks by one and the
first unused fallback family is added by the same formula. The target size is n = 10; the
run proceeds at **n ≥ 8** with disclosure, and **n < 8 is a STOP** that escalates for a
ruling.

The **frontier set** used by the headroom and separation gates (G2, G3) and by the
perturbation cells is the **top 5 roster SUTs by capability PC1** (defined in §5.6).

## 5.3 Judge panel of record

Judges are loaded exclusively through the panel constructor bound to the ratified
corrected manifest of record — never module defaults, never a stale manifest. The
expected judge surfaces are:

- **gemini-flash (google):** open_award, coherence, disclosure, settled_core.
- **grok (x-ai):** coherence, disclosure, settled_core.
- The cohere and nova families judge nothing.

**OPEN aggregation is single-family (google)** and carries a **single-judge-family label
in every table and every quotable sentence** until the judge-validity and human-consensus
gates jointly upgrade it. The pre-consensus candidate ladder stays **CLOSED** for this run
— no screening, re-qualification, exemplar change, or template change.

**EPISODE judge scoring.** Episode transcripts are judged by **both** judges eligible on
`settled_core`, under the settled-core keypoint-contract template, with each bank item's
rubric keypoints as the instrument; per-judge verdicts are persisted; ties and
disagreements resolve to UNGRADED plus an escalation flag — never a silent zero, never an
average. This interpretation is amendable before data exists and frozen once gated data
exists.

Judge willingness and parse behavior run under the corrected parser (content parse first;
a refusal scan only when no verdict content parses). No verdict of record may be produced
by the earlier parser.

## 5.4 Perturbation scope

In scope for the gated run are three perturbation axes materialized mechanically by the
harness: **P3 (persona), P4 (pushback), and P6 (monitoring-frame).** The axes P1/P5 (which
require paid materialization) and P2 (which requires structured option authoring) are
deferred and disclosed, never silently dropped.

- Variants are generated only for items whose bank `perturbations` field lists the axis
  (labeled bank counts: P3 = 143, P4 = 132, P6 = 25 items), **one variant per axis per
  item** (deterministic materializer output). For P3, one persona is assigned per item by
  rotation over the materializer's persona list in bank-slug sort order, with offset =
  master seed mod list length.
- Variant cells run on the **frontier set (5 SUTs) only** — a disclosed cost bound.
- **The gate computations use base cells only.** Perturbation output feeds the per-model
  flip-rate league table and the contested items' position-invariance reducers; these are
  reported metrics, not gates.
- **Binding caveat:** a variant that changes a Westminster-relevant fact is a new item,
  not a variant, and must not be scored as a flip.

## 5.5 Budget, pre-flight, and run mechanics

**Not-to-exceed cap: $300** (a planning ceiling; the actual approved budget is set at the
run gate, and the lower number governs). No live call is authorized by the
pre-registration itself.

**Pre-flight (mandatory, before any paid call):** an API key limit/usage check; the frozen
capability CSV written (§5.6); the roster resolved and recorded (§5.2); and a full-run
cost estimate from per-request actuals with fail-loud pricing errors. **If the estimate
exceeds 80% of the approved budget**, the pre-registered **truncation ladder** applies in
this exact order, logged: drop P6 variants → drop P3 variants → drop P4 variants → halve
the EPISODE roster to the frontier set. **Base cells are never dropped.** If base cells
alone exceed 80% of budget, the run STOPS and escalates.

**Mechanics (all binding):** per-cell checkpoint and resume; append-only raw evidence
(every SUT emission and every judge emission persisted verbatim); a retry seam that
records transport failure after retry; OpenRouter `max_tokens` capped per client; a new
dated run directory; a report headed "GATE-COMPUTATION REPORT — adjudication pending"
(the executor computes but never adjudicates); and the canary comment in every emitted
file.

**Master seed = 1647.** Every stochastic step derives its seed deterministically from 1647
as stated in its own clause below. No wall-clock and no unseeded RNG is used anywhere.

## 5.6 Capability battery and PC1 construction

The capability battery is a **frozen list of four public components** per roster model:
(i) **LMArena text Elo** (overall), (ii) **MMLU-Pro**, (iii) **GPQA Diamond**, and
(iv) **LiveBench global average**. These are retrieved once at pre-flight from the
official leaderboard/source pages, written to `capability-battery.csv` in the run
directory with per-cell source URL and retrieval timestamp, and **frozen before the first
paid call**.

**Missing-data rule:** a model missing a component has that component imputed as its own
mean z-score across its available components; a model with fewer than 2 components is
excluded from the capability-correlation gate (disclosed). If fewer than 6 roster models
survive, that gate reads **INCONCLUSIVE**.

**PC1 construction:** z-score each battery column across the included roster models; PC1 is
the first principal component of that z-matrix (correlation-based PCA), oriented so that
it correlates positively with LMArena Elo. PC1 also defines the **frontier set** (top 5
roster SUTs by PC1) used by the headroom and separation gates and by the perturbation
cells.

## 5.7 The seven pre-registered release gates

The gate thresholds below are frozen. The executor **computes** each gate's evidence and
every named number and produces a provisional packet; **PASS/FAIL adjudication is a
separate human step**. Human labeling (for G4 and G6) does **not** block the run — it
blocks release: the panel runs before labels, and labels gate release, not execution.

### G1 — Capability correlation

**Purpose:** hard-tier scores must not be a capability proxy — the shared variance with
general capability must be below 40%.

- **Scope / per-SUT statistic:** each SUT's hard-tier score = mean ceiling-normalized
  base-cell score over **T3 ∪ T4 gold-scored items in scope** (EPISODE included only if
  run; contested items excluded, as they are not gold-scored).
- **Test:** compute Pearson r between that per-SUT vector and PC1 across included models.
  **PASS iff r² < 0.40.**
- **Reported alongside (not gates):** Spearman ρ, n, and a 10,000-resample bootstrap CI
  over items at seed 1647.
- **Frozen threshold: r² < 0.40.**

### G2 — Headroom

**Ceiling:** every scorer kind emits per-cell scores on a [0,1] fraction scale, so the
ceiling is **1.0 per cell, uniformly**. The runner asserts every score of record ∈ [0,1]
fail-loud; any out-of-range score voids the cell into the escalation ledger.

- **Test:** for each frontier-set SUT, compute the mean base-cell score over T3 ∪ T4
  gold-scored items in scope (same scope as G1). **PASS iff the best frontier-set SUT's
  mean ≤ 0.70.**
- **Report:** the full frontier vector and a per-design breakdown.
- **Construct disclosure (mandatory):** because the roster excludes google/x-ai/anthropic,
  G2 certifies **roster-frontier** headroom, not global-frontier headroom. Any public
  claim must say "strongest evaluated model," never "strongest model."
- **Frozen threshold: best frontier-set mean ≤ 0.70.**

### G3 — Separation

- **Scope:** all gold-scored base cells in scope (full bank minus contested minus
  dev-set-only; EPISODE only if run).
- **Procedure:** for each of the **10 frontier-set pairs** (top-5 roster SUTs by PC1, giving
  C(5,2) = 10 pairs): a paired nonparametric bootstrap over items — resample item indices
  with replacement, **B = 10,000**, the same resampled indices applied to both models of
  the pair; the statistic is the mean per-item score difference. Two-sided p with add-one
  smoothing: p = 2·min(#{d* ≤ 0}, #{d* ≥ 0} + 1)/(B + 1), capped at 1. The seed for pair k
  (pairs ordered by sorted slug tuple) = **1647 + k**. Cells missing for one model of a
  pair drop that item from that pair's comparison (disclosed count).
- **Test:** **PASS iff ≥ 9 of 10 pairs have p < 0.01.** No multiplicity correction is
  applied (pre-registered as-is).
- **Frozen threshold: ≥ 9 of 10 pairs with p < 0.01.**

### G4 — Judge validity

One G4 verdict is computed per judge × surface:

| Surface | Judge(s) of record | Unit labeled |
|---|---|---|
| open_award | gemini-flash only (single-family) | per-keypoint award/deny on a persisted SUT response |
| disclosure | gemini-flash, grok | binary disclosure verdict |
| settled_core | gemini-flash, grok | per-keypoint right/wrong |
| coherence | gemini-flash, grok | graded coherence verdict as templated |
| EPISODE | both settled_core judges | per-keypoint rubric verdict on an episode transcript |

- **Human labels:** drawn **after** the panel has run; a stratified random sample per
  surface of **n = 40 units** (or all units if fewer exist), stratified by design × SUT, at
  **seed 1647 + surface index** (surfaces in the table order above); each unit labeled
  **blind** (no judge verdict shown) by **≥ 2 qualified raters**; labels are append-only.
- **κ forms:** binary units → unweighted Cohen's κ (judge vs. the human modal label);
  graded/ordinal units → quadratic-weighted κ; ICC(2,1) reported as supplementary for any
  fraction-valued surface. The **human ceiling** = mean pairwise human–human κ on the same
  units, in the same κ form.
- **Test, per judge × surface:** **PASS iff κ_judge–human ≥ 0.60 AND κ_judge–human ≥ 0.75
  × human ceiling.** If the human ceiling itself is **< 0.60**, that surface's labels are
  insufficient and the verdict is **INCONCLUSIVE-LABELS** (a panel problem, escalated).
- **Consequence of FAIL:** that judge × surface's scores of record become **JUDGE-INVALID —
  non-quotable** wherever they appear. Because open_award is a single-judge surface, its
  G4 failure makes the whole OPEN surface non-quotable (there is no fallback judge; the
  ladder is closed).
- **Frozen thresholds: κ ≥ 0.60 AND κ ≥ 0.75 × human ceiling; human-ceiling floor 0.60.**

### G5 — Shortcut

Three sub-tests, all frozen:

- **G5a — lexical baseline, discrete-keyed items.** A scikit-learn pipeline (frozen
  hyperparameters: TF-IDF, word 1–2-grams, lowercase, min_df = 1; multinomial logistic
  regression, C = 1.0, max_iter = 1000) predicts the discrete key from the stem text,
  5-fold cross-validation (fold seed 1647), run separately per key class present (ordinal
  gold orders, n = 20 non-contested; anchor citation keys, n = 23; any MCQ-keyed legs).
  **PASS iff CV accuracy − majority-class chance ≤ 0.10 absolute in every key class.**
  Small-n is disclosed per class; no class is skipped silently.
- **G5b — lexical baseline, judge-scored items (nearest-neighbor key transplant).** A
  mechanical responder that, for each OPEN item, returns the key text of the most
  TF-IDF-similar OTHER item (cosine similarity, self excluded), scored by the normal judge
  pipeline as if it were an SUT. **PASS iff its mean OPEN rubric fraction ≤ 0.20.**
- **G5c — the 10% fine-tune probe, ruled substitute (in-context study probe, since
  fine-tuning is impractical with serving-only access; disclosed in every report citing
  G5).** Priming set = 23 items (10% of 230), stratified by design, seed 1647, drawn from
  gold-scored non-EPISODE items; evaluation set = 100 gold-scored non-EPISODE items,
  stratified by design, seed 1648, disjoint from the priming set. Probe model = the
  **median-PC1 roster SUT** (with n = 10, the 5th by PC1 rank, ties broken by slug sort).
  Two conditions on the evaluation set: (A) unprimed (standard prompt); (B) primed (the 23
  priming items with their full keys prepended as solved exemplars). **PASS iff (mean_B −
  mean_A) < 0.10 AND mean_B < the best frontier-set SUT's mean on the same 100 items.**
- **Frozen thresholds: G5a ≤ 0.10 absolute; G5b ≤ 0.20; G5c (mean_B − mean_A) < 0.10 and
  mean_B < best frontier-set mean.**

### G6 — Human consensus

- **Panel:** qualified raters (confessional literacy is the construct); recruitment is a
  human gate. Minimum panel for minting or confirming any gold: **n ≥ 3 raters** per item.
- **Consensus arithmetic:** an item's gold element is CONFIRMED iff **≥ 85%** of its raters
  agree, i.e. at least ⌈0.85·n⌉ of n raters (n = 3 → 3/3; n = 4 → 4/4; n = 5 → 5/5;
  n = 6 → 6/6; n = 7 → 6/7). Every vote is an append-only record.
- **Mapping (constrained by the contested-item ruling):** consensus reached → gold stands
  or is minted as panel-confirmed; below threshold → the item is re-classed disputed →
  calibrated-abstention / position-scored and leaves every gold-accuracy scope at the next
  gate recomputation; the 8 pre-identified items (4 contested AGG, 4 dev-set-only liberty
  legs) → the panel confirms contested status and validates the position map, never elects
  a winner; settled-core keypoints remain right/wrong everywhere; **no model ever mints or
  confirms a gold label.**
- **Coverage and release:** the release bar is **100% panel confirmation of every gold item
  contributing to a quoted headline number**; unconfirmed golds carry a "G6-pending" mark
  and are excluded from quoted headline aggregates (per-design coverage % disclosed in
  every table). Gate computations may be COMPUTED at any coverage but may not be
  ADJUDICATED as PASS for release until the coverage bar is met on the items they quote.
- **Frozen threshold: ≥ 85% (⌈0.85·n⌉ of n) per item; 100% coverage for quoted headline
  golds.**

### G7 — Reliability

- **Per design:** Cronbach's α on the items × SUTs base-cell score matrix (SUTs as
  observations, items as test parts; casewise-complete cells; item and SUT counts
  disclosed). Report per design: α, a 95% bootstrap CI over items (B = 10,000, seed 1647 +
  design index in slug sort order), the mean inter-item correlation, and item–total
  correlations.
- **Flag semantics:** **α > 0.99 → REDUNDANCY flag** (redundancy, not quality) → item-
  diversification review. Low α is reported, never silently fixed. G7 has no pass/fail
  veto on release; it is a mandatory reported gate with the single flag above.
- **Frozen threshold: α > 0.99 raises the REDUNDANCY flag; no release veto.**

## 5.8 Release semantics

The headline per-commandment × per-tier × per-track matrix (and the worst-cell scalar, the
only sanctioned scalar) is quotable **iff G1, G2, G3, and G5 are adjudicated PASS** (or
their failure actions are executed and re-run under a new ruling) **and G7 is reported**.
Each judge-scored surface quoted additionally requires its **G4 pass**, and every quoted
gold requires **G6 coverage**. Partial release is by surface, with labels exactly as
adjudicated: the single-judge-family label on OPEN, the PROOF artifact disclosure, and the
DESCRIPTIVE/PRE-GATE-vs-gated separation everywhere. Any earlier (MVP-run) numbers remain
DESCRIPTIVE/PRE-GATE permanently and are not gated results.

If a gate is recomputed after the run because an item is demoted to disputed by the human
panel, both computations are reported (pre- and post-exclusion) and the post-exclusion one
is the gate of record; only item exclusion changes, under the same frozen procedures and
seeds.
