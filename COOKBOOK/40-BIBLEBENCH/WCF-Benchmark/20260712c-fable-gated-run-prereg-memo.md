<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — BINDING Gated-Run Pre-Registration (G1–G7) + Session Findings (R58–R68)

**Date:** 2026-07-12 · **Tier:** Fable (binding) · **Session:** S23 (the F2 session of
`20260712b-fable-prereg-boot-prompt.md`; the final planned Fable session)
**Extends:** R1–R57. **Relitigates nothing.** Skeleton source: `20260711-fable-next-session-boot-prompt.md`
agenda item 2, updated for R47/R52/R53/R54–R57. Rigor precedent (content never cross-wired):
the WALKWORTHY gate pre-registration.
**Status of this document:** the T4 gate "binding pre-registration memo exists"
(`20260712-codex-execution-plan-v2.md`) is DISCHARGED by this memo, subject to R58.3.

---

## §1 State findings (Step 0, verified this session)

1. **Codex T1/T2 have not started.** No commits on `codex/wcfbench-mvp-testable` after
   `d7e534aa8`; no codex session handoff newer than `20260711d`; no corrected-manifest or
   re-parse run directory exists; execution-plan-v2 boxes all unchecked; dashboard
   Live-status still reads "MVP testable: NO — pending 3 directed offline Codex work items."
2. **PENDING-QUESTIONS.md** contains nothing new since S22; all entries cite rulings
   already issued (R47–R53 statuses to be updated by Codex T1 step 5). Nothing to
   adjudicate this session.
3. Consequently **Part A (ratification) remains OPEN** — see R58.1/R58.2 — and this memo's
   main deliverable (Part B, the pre-registration) is written **conditioned on the R57
   checklist** per R58.3, exactly as the boot prompt directs.

---

## §2 Rulings

### R58 — Ratification disposition + conditionality of this pre-registration

**R58.1** T1/T2 ratification **remains open**. Nothing here anticipates or substitutes for
it. The **R57 checklist is the sole ratification instrument**; **Jimmy may ratify alone**
on that checklist (R57's own provision) — no further Fable session is required. A checklist
failure is a bounded correction order to Codex per R57 ("escalation, never improvisation").

**R58.2** Until that ratification: MVP testable stays **NO** (R53 conditions unmet); OPEN
stays **PENDING-CORRECTION** (R47.5); the manifest of record remains the as-executed Task-4
manifest, superseded by the R47.3 corrected manifest **when it lands and is ratified**.

**R58.3 — Conditionality clause.** This pre-registration is **valid iff the R57 checklist
later passes unmodified**. If the checklist ever fails:
- ONLY the manifest-dependent clauses reopen — the **G4 surface table (R63)** and the
  **judge plan (R59.4)** — and their amendment requires Jimmy or a judgment-tier ruling;
- everything else in this memo **stands as written** (R59 run design except §R59.4,
  R60–R62, R64–R66, R67, R68).
No clause of this memo may be executed against a manifest other than the ratified R47.3
corrected manifest of record.

---

### R59 — The gated-run (T4) design

#### R59.1 Items in scope

The frozen bank of **230 items** (10 designs × 22–24; tiers T2 = 55, T2a = 26, T2b = 30,
T3 = 70, T4 = 49; tracks A = 71 / B = 159; counts verified against `05-BANK-YAML/` this
session). Disposition:

| Class | n | Disposition in T4 |
|---|---|---|
| Core runnable | 204 | Run, full roster |
| EPISODE (all NARROWGATE, all T4) | 22 | Run on the full roster **iff** the T2-applied approved registry + the R55.2/R55.3 build items are green at launch; scored per R55.1 (mechanical `classify_outcome` = SCREEN; score of record = rubric-based judge scoring on persisted transcripts). **Else:** excluded, reported "pending registry approval" (never silently absent), and every gate row they touch discloses the shrunken scope. |
| `dev_set_only` (the 4 `[DISPUTED]` liberty legs) | 4 | **Not run** (dev-set hygiene stands, as in the MVP run); their scoring class is calibrated-abstention per the contested-item ruling. |
| `contested: true` (AGG-C7-007, AGG-C3-W302, AGG-C5-W304, AGG-C8-W305) | 4 | Run, but **excluded from every gold-accuracy computation** (G1/G2/G3/G5 scopes); scored adherence/disclosure/coherence-only per `20260709-contested-item-scoring-ruling.md`. Their settled-core keypoints remain right/wrong-scored. |

**No T1 tier exists in this bank.** Wherever the spine says "T2+", this memo means the
entire gold-scored bank (all tiers present). "Hard tier" means **T3 ∪ T4**.
PROOF (ANCHOR kind, 23 items) is scored under the **R52 ruled mechanical citation gate**
with the standing known-artifact disclosure in every table it appears in; no judge-assisted
anchor path exists (R52.2) and none is created here. Fresh-per-run generation (spine §6)
is NOT built and is **out of scope** for T4 — the frozen bank is the instrument; disclosed.

#### R59.2 SUT roster (anti-leakage binding; names by formula, not judgment)

**Anti-leakage rule (binding):** no SUT from the judge families **{google, x-ai}** or the
item-generator family **{anthropic}** (bank authored by Fable/Opus). This excludes the
true global frontier from the roster by construction; G2/G3 therefore measure
**roster-frontier** headroom/separation — a deliberate, disclosed cost of judge and
generator independence (see R61.3).

**Roster = 10 SUTs**, assembled mechanically at pre-flight:

- **Five formula-selected frontier candidates** — for each family in
  {openai, deepseek, qwen/alibaba, moonshotai, meta-llama}: the family's
  OpenRouter-available, text-capable, non-preview model with the **highest LMArena text
  Elo** in the frozen capability CSV (R60.2). A family with no LMArena-listed available
  model is replaced from the fallback order **z-ai → nvidia → microsoft** (same formula).
- **Three MVP-continuity pins (verbatim slugs):** `deepseek/deepseek-chat`,
  `mistralai/mistral-large-2512`, `meta-llama/llama-3.1-8b-instruct` (the 8B model is the
  deliberate low-capability anchor G1 needs for spread).
- **Two mid-tier pins:** `cohere/command-a`, `amazon/nova-pro-v1` (families already
  screened in this project as judges — judge-screen failure does not disqualify a model
  as an SUT; neither family judges anything of record).
- **De-dup rule:** if a formula pick equals a pinned slug, the roster shrinks by one and
  the first unused fallback family is added by the same formula. Target n = 10; the run
  proceeds at n ≥ 8 with disclosure; n < 8 = STOP, escalate to Jimmy.

Roster membership is fixed at pre-flight, recorded in the run manifest **before the first
paid call**, and thereafter unchangeable except by logged Jimmy ruling (R67). The
**frontier set** for G2/G3 = the top **5** roster SUTs by capability PC1 (R60.3).

#### R59.3 Perturbation scope

In scope for T4: **P3 (persona), P4 (pushback), P6 (monitoring-frame)** — exactly the
axes `wcfbench/perturbation.py` materializes mechanically (built + tested). Deferred to
T5 (disclosed, never silently dropped): **P1/P5** (need paid LLM materialization —
Jimmy's authorization lane) and **P2** (needs structured option authoring).

- Variants are generated only for items whose bank `perturbations` field lists the axis
  (bank counts: P3 = 143, P4 = 132, P6 = 25 labeled items); **one variant per axis per
  item** (deterministic materializer output; for P3, one persona assigned per item by
  rotation over the materializer's persona list in bank-slug sort order, offset = master
  seed mod list length).
- Variant cells run on the **frontier set (5 SUTs) only** (cost bound, disclosed).
- **Gate computations (G1–G7) use base cells only.** Perturbation output feeds the
  per-model **flip-rate league table** (spine §5, `InvarianceLeagueTable`) and the
  contested items' position-invariance reducers — reported metrics, not gates.
- The Q99-Rule-5 caveat is restated as binding: a variant that changes a
  Westminster-relevant fact is a new item, not a variant, and must not be scored as a flip.

#### R59.4 Judge plan (manifest-dependent; reopens only per R58.3)

- Judges load **exclusively via `JudgePanel(manifest=<the ratified R47.3 corrected
  manifest of record>)`** — never module defaults, never a stale manifest (R47.5).
- Expected surfaces (= R57 checklist expectation): **gemini-flash (google)** on
  `open_award + coherence + disclosure + settled_core`; **grok (x-ai)** on
  `coherence + disclosure + settled_core`; cohere/nova none.
- **OPEN aggregation is single-family (google)** and carries the **R34.4 single-family
  label in every table and every quotable sentence** until G4+G6 upgrade it. The pre-G6
  candidate ladder stays **CLOSED** (R47.4) — no screening, no re-qualification, no
  exemplar or template change in T4.
- **EPISODE judge scoring (pinned interpretation of R55.1):** episode transcripts are
  judged by **both** judges eligible on `settled_core`, under the settled-core
  keypoint-contract template of record, with the bank item's rubric keypoints as the
  instrument; per-judge verdicts persisted; ties/disagreements per R39(e)(4)
  (tie → UNGRADED + escalation flag, never a silent 0, never averaged). This is an
  interpretation, flagged per protocol: amendable pre-data by Jimmy without voiding
  anything; frozen once gated data exists.
- Judge willingness/parse behavior runs under the **R48-fixed parser** (content parse
  first; refusal scan only when no verdict content parses). No verdict of record may be
  produced by a pre-R48 parser.

#### R59.5 Budget, pre-flight, mechanics

- **Not-to-exceed cap: $300** (planning ceiling; Jimmy sets the actual approved budget at
  the T4 gate — his number governs if lower). Paid-call pause (R50.2) remains in force
  until that authorization; nothing in this memo starts a run.
- **R40.1 pre-flight (mandatory, before any paid call):** `GET /api/v1/auth/key`
  limit/usage check (top-up = Jimmy item; run waits); frozen capability CSV written
  (R60.2); roster resolved + recorded (R59.2); full-run cost estimate from per-request
  actuals machinery (R45.3, fail-loud `PricingError`, key-side reconciliation). If the
  estimate exceeds **80% of the approved budget**, the pre-registered truncation ladder
  applies *in this order, logged*: drop P6 variants → drop P3 variants → drop P4 variants
  → halve EPISODE roster to the frontier set. **Base cells are never dropped.** If base
  cells alone exceed 80% of budget: STOP, escalate to Jimmy.
- **Mechanics (all binding):** per-cell checkpoint/resume; append-only raw evidence
  (every SUT emission + every judge emission persisted verbatim); retry seam per R40(2)
  with `fail_transport_after_retry` recorded; OpenRouter `max_tokens` capped per client
  (the 402-reservation gotcha); new dated run directory; report headed **GATE-COMPUTATION
  REPORT — adjudication pending** (Codex computes, never adjudicates, R67.4); canary in
  every emitted file.
- **Master seed = 1647.** Every stochastic step below derives its seed deterministically
  from 1647 as stated in its own clause. No wall-clock, no unseeded RNG anywhere.

---

### R60 — Gate G1 · Capability correlation (pinned computation)

**R60.1 Purpose-check:** hard-tier scores must not be a capability proxy —
pass = shared variance with general capability **< 40%**.

**R60.2 The capability battery (frozen list):** four public components per roster model —
(i) **LMArena text Elo** (overall), (ii) **MMLU-Pro**, (iii) **GPQA Diamond**,
(iv) **LiveBench global average** — retrieved once at pre-flight from the official
leaderboard/source pages, written to `capability-battery.csv` in the run directory with
per-cell source URL + retrieval timestamp, **frozen before the first paid call**.
Missing-data rule: a model missing a component gets that component imputed as its own
mean z-score across its available components; a model with **< 2** components is excluded
from G1 (disclosed). If fewer than **6** roster models survive, G1 = **INCONCLUSIVE**
(escalation, not silent pass/fail).

**R60.3 PC1 construction:** z-score each battery column across the included roster
models; PC1 = first principal component of that z-matrix (correlation-based PCA);
orient PC1 so it correlates positively with LMArena Elo. PC1 also defines the
**frontier set** (top 5 roster SUTs by PC1) used by G2/G3 and R59.3.

**R60.4 The test:** per-SUT hard-tier score = mean ceiling-normalized base-cell score over
**T3 ∪ T4 gold-scored items in scope** (EPISODE included iff run; contested excluded —
they are not gold-scored). Compute Pearson r between that vector and PC1 across included
models. **PASS iff r² < 0.40.** Report alongside (not gates): Spearman ρ, n, and a 10,000-
resample bootstrap CI over items (seed 1647). Failure action per spine: redesign the
offending tier — a judgment-tier order, not a Codex improvisation.

---

### R61 — Gate G2 · Headroom (pinned computation)

**R61.1 Ceiling:** every scorer kind in this harness already emits per-cell scores on a
[0,1] fraction scale (OPEN rubric fraction, ORDINAL normalized ordinal agreement, ANCHOR
citation fraction, EPISODE judge rubric fraction). **Ceiling = 1.0 per cell, uniformly.**
The runner asserts every score of record ∈ [0,1] fail-loud; any out-of-range score voids
the cell into the escalation ledger (this guard is load-bearing: R42.3's off-scale raws).

**R61.2 The test:** for each frontier-set SUT, mean base-cell score over T3 ∪ T4
gold-scored items in scope (same scope as R60.4). **PASS iff the best frontier-set SUT's
mean ≤ 0.70.** Report the full frontier vector and per-design breakdown.

**R61.3 Construct disclosure (mandatory in the report):** because R59.2 excludes
google/x-ai/anthropic, G2 certifies **roster-frontier** headroom, not global-frontier
headroom. Any public claim must say "strongest evaluated model," never "strongest model."
Failure action per spine: adversarial filtration pass / difficulty-reservoir raise —
judgment-tier order.

---

### R62 — Gate G3 · Separation (pinned computation)

**R62.1 Scope:** all gold-scored base cells in scope (the full bank minus contested minus
dev-set-only; EPISODE iff run) — this is the spine's "T2+" given the bank has no T1.

**R62.2 Procedure:** for each of the **10 frontier-set pairs** (top-5 roster SUTs by PC1,
C(5,2) = 10): paired nonparametric bootstrap over items — resample item indices with
replacement, **B = 10,000**, the same resampled indices applied to both models of the
pair; statistic = mean per-item score difference. Two-sided p with add-one smoothing:
p = 2·min(#{d* ≤ 0}, #{d* ≥ 0} + 1)/(B + 1), capped at 1. Seed for pair k (pairs ordered
by sorted slug tuple) = **1647 + k**. Cells missing for one model of a pair drop that
item from that pair's comparison (disclosed count).

**R62.3 The test:** **PASS iff ≥ 9 of 10 pairs have p < 0.01** (that is the ≥90% criterion
at this pair count; stated numerically so no rounding judgment is needed). No multiplicity
correction (pre-registered as-is, matching the spine's stated criterion). Failure action
per spine: kill dead items (>99% uniform response — the uniformity table is part of the
gate report) and rewrite — judgment-tier order.

---

### R63 — Gate G4 · Judge validity (manifest-dependent; reopens only per R58.3)

**R63.1 Surfaces under test (one G4 verdict per judge × surface):**

| Surface | Judge(s) of record | Unit labeled |
|---|---|---|
| open_award | gemini-flash only (single-family, R34.4) | per-keypoint award/deny on a persisted SUT response |
| disclosure | gemini-flash, grok | binary disclosure verdict |
| settled_core | gemini-flash, grok | per-keypoint right/wrong |
| coherence | gemini-flash, grok | graded coherence verdict as templated |
| EPISODE (R55.1) | both settled_core judges (R59.4) | per-keypoint rubric verdict on an episode transcript |

**R63.2 Human labels:** drawn **after** the T4 panel has run (labels gate release, not
execution — R67.2); stratified random sample per surface, **n = 40 units** per surface
(or all units if fewer exist), stratified by design × SUT, **seed 1647 + surface index**
(surfaces in the table order above); each unit labeled **blind** (no judge verdict shown)
by **≥ 2 qualified raters** (G6 panel qualification, R65.1). Rater UI = the `06-G6-PANEL`
tool lineage; labels are append-only records.

**R63.3 κ forms (pinned):** binary units → unweighted Cohen's κ (judge vs. the human
modal label); graded/ordinal units (triaxial 0/0.5/1, coherence grades) →
quadratic-weighted κ; report ICC(2,1) as supplementary for any fraction-valued surface.
**Human ceiling** = mean pairwise human–human κ on the same units, same κ form.

**R63.4 The test, per judge × surface:** **PASS iff κ_judge–human ≥ 0.60 AND
κ_judge–human ≥ 0.75 × human ceiling.** If the human ceiling itself is **< 0.60**, the
surface's labels are insufficient — verdict **INCONCLUSIVE-LABELS** (a G6/panel problem,
not judge failure; escalation to Jimmy).

**R63.5 Consequence of FAIL:** that judge × surface's scores of record become
**JUDGE-INVALID — non-quotable** wherever they appear; the failure action (rubric
re-anchor → new manifest event, per spine) is a judgment-tier order. A single-judge
surface (open_award) failing G4 makes the whole OPEN surface non-quotable — there is no
fallback judge (ladder CLOSED; the escalation is G6 human anchors, per R47.4).

---

### R64 — Gate G5 · Shortcut (pinned computation; substitute ruled and disclosed)

**R64.1 G5a — lexical baseline, discrete-keyed items:** scikit-learn pipeline (frozen
hyperparameters: TF-IDF, word 1–2-grams, lowercase, min_df = 1; multinomial logistic
regression, C = 1.0, max_iter = 1000) predicting the discrete key from the stem text,
5-fold cross-validation (fold seed 1647), run separately per key class present in the
bank (ordinal gold orders [ORDINAL, n = 20 non-contested]; anchor citation keys [ANCHOR,
n = 23]; any MCQ-keyed legs). **PASS iff CV accuracy − majority-class chance ≤ 0.10
absolute in every key class.** Small-n is disclosed per class; no class is skipped
silently.

**R64.2 G5b — lexical baseline, judge-scored items (nearest-neighbor key transplant):**
a mechanical responder that, for each OPEN item, returns the **key text of the most
TF-IDF-similar OTHER item** (cosine similarity, same vectorizer family, self excluded),
scored by the normal judge pipeline as if it were an SUT. **PASS iff its mean OPEN rubric
fraction ≤ 0.20.** (Threshold is a pre-registered convention: a surface-similarity
responder must stay near the floor. Its judge calls are inside the R59.5 budget.)

**R64.3 G5c — the 10%-fine-tune probe, ruled substitute (fine-tuning is impractical: no
FT infrastructure, OpenRouter serving only; substitution authorized by the boot prompt
and disclosed in every report that cites G5):** an **in-context study probe**. Priming
set = 23 items (10% of 230), stratified by design, **seed 1647**, drawn from gold-scored
non-EPISODE items; evaluation set = 100 gold-scored non-EPISODE items, stratified by
design, **seed 1648**, disjoint from the priming set. Probe model = the **median-PC1
roster SUT** (n = 10 → the 5th by PC1 rank, ties broken by slug sort). Two conditions on
the evaluation set: (A) unprimed (standard prompt); (B) primed — the 23 priming items
with their full keys prepended as solved exemplars. **PASS iff (mean_B − mean_A) < 0.10
AND mean_B < the best frontier-set SUT's mean on the same 100 items.** A FAIL means
surface patterns leak the keys → item surgery (judgment-tier order per spine).

---

### R65 — Gate G6 · Human consensus (pinned mapping; constrained by the contested ruling)

**R65.1 Panel:** qualified raters per spine §7 (ministers/elders/students of confessional
Reformed bodies or equivalent — confessional literacy is the construct, not a bias).
Recruitment is **Jimmy's** (standing human gate). Minimum panel for minting/confirming
any gold: **n ≥ 3 raters** per item.

**R65.2 Consensus arithmetic:** an item's gold element is CONFIRMED iff **≥ 85%** of its
raters agree with it, i.e. at least ⌈0.85·n⌉ of n raters (n = 3 → 3/3; n = 4 → 4/4;
n = 5 → 5/5; n = 6 → 6/6; n = 7 → 6/7). Every vote is an append-only record.

**R65.3 Mapping (constrained by `20260709-contested-item-scoring-ruling.md`):**
- consensus reached → gold stands (or is minted) as panel-confirmed;
- below threshold → the item is re-classed **`[DISPUTED]`** → calibrated-abstention /
  position-scored; it leaves every gold-accuracy scope (G1/G2/G3/G5) at the next gate
  recomputation (pre-registered exclusion — R67.3);
- the **8 pre-identified items** (4 contested AGG + 4 dev-set-only LIB legs): the panel's
  task is to **confirm contested status and validate the position map — never to elect a
  winner**. Settled-core keypoints (Q152 floor; undisputed forbidden legs) remain
  right/wrong everywhere.
- **No LLM ever mints or confirms a gold label.** G6 labels enter only through the panel
  records.

**R65.4 Coverage and release:** the G6 release bar is **100% panel confirmation of every
gold item contributing to a quoted headline number**; unconfirmed golds carry
`author-gold (G6-pending)` and are excluded from quoted headline aggregates (per-design
coverage % disclosed in every table). Gate computations may be COMPUTED at any coverage
(they are functions of scores, not labels) but may not be ADJUDICATED as PASS for release
until the coverage bar is met on the items they quote.

---

### R66 — Gate G7 · Reliability (pinned computation)

**R66.1** Per design: **Cronbach's α** on the items × SUTs base-cell score matrix (SUTs
as observations, items as test parts; casewise-complete cells; item and SUT counts
disclosed). Report per design: α, 95% bootstrap CI over items (B = 10,000, seed 1647 +
design index in slug sort order), mean inter-item correlation, and item–total
correlations.

**R66.2** **α > 0.99 → REDUNDANCY flag** (spine: redundancy, not quality) → item-
diversification review (judgment-tier). Low α is reported, never silently "fixed"; with
n = 10 observations the CI does the honesty work. G7 has no pass/fail veto on release; it
is a mandatory reported gate with the single flag semantics above.

---

### R67 — Freeze, deviation, adjudication, and release semantics

**R67.1 Freeze:** this pre-registration is **FROZEN the moment the first gated datum
exists** (= the first paid T4 call). Before that moment, amendments are judgment-tier
only (Jimmy, or a ratified provisional packet), recorded as a new dated amendment file —
this memo is never edited. After that moment: **any deviation requires a logged Jimmy
ruling BEFORE proceeding; a silent deviation voids the affected gate** (the gate reads
INVALID-DEVIATION, non-quotable, until a ruled disposition).

**R67.2 T4 gate-line refinement (rules the execution-plan-v2 T4 line precisely):**
- **Execution gates** (to start the run): this memo valid per R58.3 (R57 checklist
  passed) + Jimmy's paid-call reauthorization and budget + roster resolution (R59.2)
  + R40.1 pre-flight.
- **Adjudication/release gates** (to quote anything): G6 labels per R65.4 + G4 labels per
  R63.2 + gate adjudication per R67.4.
Human labeling therefore does **not** block the run; it blocks release — the WALKWORTHY
"panel runs before labels; labels gate release" ordering, adopted here as ruling. The
dashboard mirrors this refinement; the dated plan file is not edited.

**R67.3 Post-run G6 reclassification:** an item demoted to `[DISPUTED]` after the run is
excluded from all gold-accuracy gate scopes and those gates are **recomputed under this
memo's frozen procedures** (same seeds; item exclusion is the only change). Both
computations are reported (pre- and post-exclusion); the post-exclusion one is the gate
of record.

**R67.4 Adjudication:** Codex **computes** the gate report (per-gate evidence, every
number this memo names, no adjudication, R-numbers never assigned) + a provisional
packet. **Gate PASS/FAIL rulings are judgment-tier: Jimmy is the ratifier of record**
(provisional packets with RESERVED R-numbers; no further Fable session is planned).

**R67.5 Release semantics:** the headline per-commandment × per-tier × per-track matrix
(and the worst-cell scalar — still the only sanctioned scalar, spine §4.6) is quotable
iff **G1, G2, G3, G5 adjudicated PASS** (or their failure actions executed and re-run
under a new ruling) **and G7 reported**; each judge-scored surface quoted additionally
requires its **G4 pass**; every quoted gold requires **G6 coverage** (R65.4). Partial
release is by surface with labels exactly as adjudicated: R34.4 single-family label on
OPEN; the R52 PROOF artifact disclosure; DESCRIPTIVE/PRE-GATE vs. gated separation
everywhere. MVP-run numbers remain DESCRIPTIVE/PRE-GATE forever (R49.2).

---

### R68 — Close-out of planned Fable involvement

**R68.1** With this memo, the planned Fable judgment ledger for WCF-Bench is **complete**:
R1–R57 closed everything prior; R58–R67 close the gated-run pre-registration. **This was
the final planned Fable session.** Future judgment needs route: Codex provisional packet
(RESERVED R-numbers) → **Jimmy, ratifier of record**. An Opus session may draft
(PROVISIONAL, reserved numbers) if analysis beyond Codex's lane is ever needed.

**R68.2** Standing division of labor (unchanged, restated for the record): **Codex** =
standing executor (`20260712-codex-standing-boot-prompt.md` → execution-plan-v2 top-down;
T1 → T2 → [T2.5 = R57 ratification, Jimmy] → T3 gates → T4 under this memo). **Jimmy** =
the remaining human gates: R57 ratification (may ratify alone), paid-call reauthorization
+ T3 roster, T4 budget, G6 recruitment + labeling (R65), G4 co-labeling (R63), gate
adjudication (R67.4). The handover plan's F2 row is discharged via the dashboard (the
dated plan file is not edited).

**R68.3** Nothing in this memo authorizes a live call, edits a bank item, mints a gold,
screens a judge candidate, or modifies any immutable record.

---

**Canary:** `WCFBENCH-CANARY-c1647-x9k4q` (never re-minted).
