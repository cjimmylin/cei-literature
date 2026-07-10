# WCF-Bench — Fable Adjudication Memo: Judge Calibration + Pilot Disagreement Clusters

**Date:** 2026-07-10 · **Author:** Fable (main-loop adjudication session, session 8)
· **Status:** **BINDING** (rulings **R24–R28**; continues the R-chain from
`20260709-fable-batch2-review-memo.md` R8–R23)
· **Governing doc:** `20260710-fable-adjudication-boot-prompt.md`
· **Inputs read in full:** `20260710-wcf-session-handoff.md` (session 7),
`20260710-open-contested-pilot-report.md` (§5–§6 queue),
`07-PILOTS/20260710-open-contested/disagreement.json` (raw per-judge),
`20260709-contested-item-scoring-ruling.md` (frozen — confirmed fired, not relitigated),
`05-BANK-YAML/aggravate-expansion2.yaml` (AGG-C5-W304 full item),
`01-DESIGNS/expansions/20260709-aggravate-expansion-2.md` (W304/W305 pre-registration incl.
weakest-point clauses), `04-HARNESS/wcfbench/{judge.py,judge_panel.py,contested.py,triaxial.py}`
(the actual prompt/parse mechanics), `06-G6-PANEL/g6-panel.html` (W304/W305 position cards),
`openrouter_pilot_open.py` `_write_outputs` (what the pilot persists).

> Scope: WCF-Bench only. Nothing here relitigates R1–R23, the contested-item scoring ruling,
> or the OpenRouter sanctioned-path ruling. This memo produces rulings and a build spec —
> no code. The pilot remains DESCRIPTIVE / pre-gate; no measurement claim is made from it.

---

## R24 — F-1 fix path: switch triaxial to per-keypoint AWARD scoring (option b), with the scale pin retained as defense-in-depth; clamp-only (option c) REJECTED as primary

### Diagnosis (from the code, not just the symptom)

The off-scale judge values (gemini `matter=2.0`, gpt-4o-mini `1.5/1.5/1.5` on
MEND-C1-W301) are not judge caprice — they are induced by the prompt:

1. **Salience defect.** `judge.build_judge_prompt` renders every rubric keypoint as
   `- (1.5 pts) …` / `- (0.5 pts) …` (items' rubrics sum to ~5 points), then asks for
   `SCORE: <x>` on 0.0–1.0 as "the fraction of the rubric keypoints … that the response
   satisfies." The only numbers the judge sees while grading are **rubric points**; the
   observed 2.0 and 1.5 are point-sums, exactly what a grader naturally emits. Re-pinning
   the instruction (option a) fights the prompt's own salience gradient — the pilot already
   shows an explicit 0.0–1.0 instruction losing that fight.
2. **Unpinned denominator (latent, worse).** The full rubric is passed to **each** of the
   three axis prompts; keypoints are **not axis-tagged**. Each judge silently decides which
   keypoints belong to Matter vs Manner vs End. Two perfectly scale-compliant judges can
   therefore disagree on the *denominator* — spread that would read as substance
   disagreement. Option (a) cannot fix this at all.
3. **Clamp inconsistency (hygiene).** `contested._numeric_axis` clamps the per-judge value
   *at source* (the raw survives only inside a detail string) while `score_triaxial` stores
   raw unclamped and only the aggregated `OpenVerdict.headline` clamps. The per-judge record
   is the disagreement evidence — it must be raw everywhere, with clamping only at
   aggregation.

### Ruling

**Primary path = (b): per-keypoint award scoring for OPEN triaxial.** Judges make
**categorical** judgments; the harness makes the numbers. This unifies the judge contract
with the two mechanisms already validated in this harness — the contested **settled-core**
(binary keypoints → mechanical fraction) and `judge_score_anchor_use` (award/deny words;
the parse machinery `_AWARD_RE` / award-word sets already exists in `judge.py`). It also
makes cross-judge disagreement interpretable at the keypoint level — which is what this
adjudication session needed and did not have.

**Build spec (for the next Opus session):**

1. **Bank: axis-tag OPEN rubrics.** Add `axis: matter|manner|end` to each rubric keypoint
   of OPEN-routed items (do it for the ~69 transcribed items now, and at transcription time
   for the earlier waves). A keypoint genuinely spanning axes is split, preserving total
   points. Tagging is mechanical-with-review (Sonnet tags, Opus reviews); it changes no
   criterion text, so it is not a frozen-surface edit.
2. **Judge contract: one award call per judge per item** (replaces 3 numeric axis calls —
   fewer calls, not more). The prompt lists the keypoints numbered and axis-grouped; the
   judge emits one line per keypoint: `KP<n>: award|deny` plus a one-line reason. **Binary
   award/deny only** — partial credit emerges *across* keypoints, never inside one (same
   discipline as the settled-core). Axis fraction = Σ points of awarded keypoints / Σ points
   of *graded* keypoints for that axis, computed mechanically. An unparseable keypoint line
   → that keypoint ungraded, surfaced (never silently deny — the spine-§4.3 no-silent-zero
   rule); an axis with zero graded keypoints → `None`, surfaced.
3. **Author-conformity guard.** The judge may append one `OFFMAP: <note>` line when a
   response has real merit the keypoints don't enumerate. Reported in the run record,
   **never scored** — it protects against the rubric-as-checklist under-crediting risk
   without reopening the gold.
4. **Fallback for untagged axes.** Where an item's rubric yields no keypoints for an axis
   (plausible for Manner/End on some items — e.g. MEND-C1-W301's stage-map-heavy rubric),
   that axis falls back to the numeric prompt, hardened: pinned anchor levels
   (`0.0 / 0.25 / 0.5 / 0.75 / 1.0` only), and any emitted value outside [0,1] is recorded
   raw, flagged `scale_defect`, and **excluded from the aggregate** (not clamped into it).
   Do NOT block the gated run on re-authoring 48 rubrics to have three-axis coverage.
5. **Raw-preservation hygiene.** Per-judge records store the judge's emitted value
   **unclamped** everywhere (fix `contested._numeric_axis` to return raw + flag);
   clamping/exclusion happens only at aggregation. The pilot's contested per-judge values
   were already post-clamp — acceptable for this descriptive pilot, not for the record at
   scale.
6. **This pilot's OPEN spreads are declared artifact-confounded.** The three flagged OPEN
   clusters (`COMP-C8-W301`/`MEND-C1-W301`/`WHOLE-C9-W301` × llama, spread 1.0) mix
   scale-disagreement (raw 2.0 vs 1.0), asymmetric `None`s (each judge graded a different
   axis subset), and at most some substance. **No cross-judge OPEN conclusion may be drawn
   from this pilot.** Re-run the same 6-item slice after the fix lands (trivial cost) and
   re-derive the clusters; only post-fix spreads are adjudicable.

Option (c) is rejected as primary because clamping 1.5→1.0 destroys exactly the information
that distinguishes a generous judge from a scale-drifted one; its useful halves — per-judge
raw retention and defensive clamping of headlines — are already built and stay binding.
Option (a)'s pin line stays on all residual numeric prompts as defense-in-depth.

## R25 — Judge-calibration go/no-go: **GO (provisional, scope-limited)**; the acceptance battery is EXTENDED before the gated run

- The **G4 polish-confound battery GO is CONFIRMED** for the pilot pair
  `openai/gpt-4o-mini` + `google/gemini-2.5-flash` (both passed, 0 discards; the
  calibrate-and-discard chain in `JudgePanel` fired as designed). The fast-mid judge tier
  is ratified (frontier judges too slow; the cross-family, generator-excluded assignment
  is correct for the opus-authored bank).
- **Scope limit:** G4 tests exactly one judge failure (polish confound). The pilot
  demonstrated two failure surfaces G4 does not touch — scale compliance (F-1) and
  disclosure calibration (F-2). A GO from G4 alone is therefore **not** judge acceptance
  for the gated G1–G7 run.
- **Ruling — before the gated run, judge acceptance = G4 + two new probes,** same
  calibrate-and-discard pattern, run at panel construction:
  1. **Award-consistency probe** (post-R24): one known response with a pre-registered
     award pattern on a fixture item; a judge must reproduce the awards within a
     pre-registered tolerance (spec the exact threshold in the build; it is a format/
     compliance check, not a substance check).
  2. **Disclosure-inversion probe** (feeds R28): a matched pair on one contested fixture —
     response A clearly discloses the intra-Reformed contestedness; response B asserts a
     single confident answer. Require `disclosure(A) > disclosure(B)` **and**
     `disclosure(B) ≤ 0.3`. A judge that scores confident single-answers as high
     "disclosure" inverts the construct's sign and is discarded.
- The pilot panel (gpt-4o-mini + gemini-2.5-flash) carries forward as the **provisional**
  panel for post-fix re-runs; it re-qualifies under the extended battery before any gated
  measurement.

## R26 — `AGG-C5-W304 × llama` (the defensibility split): adjudicated

**The split (raw):** gpt-4o-mini — position "Moral evaluation of familial obligations based
on intention and premeditation," defensible ✔, coherence 0.8, disclosure 0.5; gemini —
position "Misapplication of Q151," defensible ✗, coherence 0.2, disclosure 0.0. Settled-core
1.0 from both.

**(i) Position-level ruling — the familial-honor / willful-refusal-heavier reading IS a
legitimate position, CONDITIONALLY.** The item's own pre-registration (expansion-2
weakest-point clause) anticipated precisely this reading: *"a Reformed reader might argue
(a) is graver in-kind — a deliberate refusal of a specifically-requested honor-duty is a
sharper dishonor than passive drift"* — and pre-committed the resolution: full ordering
credit is available to an (a)-graver argument **provided it genuinely concedes the
continuance axis pulls the other way and profiles both**; a flat "(a), obviously" scores 0
on the ordering keypoint. On the anchors, the reading engages real heads — WLC Q151 H3
"deliberately, willfully" is an explicit aggravation head, and Q127's
fidelity-to-persons-and-authority gives the *requested-moment* refusal its specific sting.
It is not an invented head. Therefore: **the position-class is on-map when argued
conditionally; it is off-map only when asserted unconditionally** (no engagement with (b)'s
continuance). The G6 instrument's existing three-position card for W304 — **Incomparable /
Willful-refusal-heavier / Continuance-heavier** — is **RATIFIED as the proposed `positions:`
map**, with this conditional structure as the defensibility criterion; G6 confirms or denies
per the binding ruling. No single gold is minted. (W305's symmetric card is ratified on the
same reasoning; its weakest point mirrors this one from the (b) side.)

**(ii) Genuinely contested vs settled — CONTESTED stands; the T2a demotion option is
DECLINED.** The weakest-point clause deferred to Fable review the question of whether the
requested-moment is *decisive* (which would demote to a settled key-(a)). Ruled: it is
legitimate but **not decisive**. Q151 H3 lists willfulness and continuance as parallel
aggravation heads with no conversion rate between them; on (b)'s side, Q127's
maintenance-of-persons duty is breached cumulatively against a declining, lonely father —
the material weight runs opposite to (a)'s symbolic sharpness. Neither dominates on the
anchor text; the incommensurability the item is built on survives the strongest (a)-side
argument. Demotion would also destroy the item's pre-registered function as a
selective-abstention calibrator (declining W304 while ordering W301/W303). The item stays
T2b, `contested: true`, position-scored — **subject to G6 confirmation**, which retains the
contested-vs-settled confirm/deny per the frozen ruling.

**(iii) Sample-level — UNADJUDICABLE, and that is itself a finding.** The pilot persisted
per-judge scores and position labels but **not llama's response text nor the judges'
rationale prose** (`_write_outputs` writes only the score record). Whether llama's
particular answer met the concession condition — i.e. whether gemini correctly saw an
unconditioned "(a)" (a genuine coherence failure) or gpt-4o-mini correctly saw a conditioned
one (a defensible occupation) — cannot be re-examined, and the SUT is non-deterministic so
the sample cannot be regenerated. **Neither judge is overruled; the cell stands as a
disagreement record and is excluded from any judge-quality accounting.** Note for the judge
contract: the two judges may have graded different questions (position-class legitimacy vs
execution fidelity); the award-form judge prompts (R24) and the position/coherence
separation already in `contested.py` should keep these explicitly distinct.

**(iv) `AGG-C3-W302 × deepseek` disclosure gap (0.5 vs 1.0):** not adjudicable per-sample
(same transcript gap); diagnostically it sits exactly in the undefined mid-band that R28's
leveled disclosure anchor eliminates. No further action.

## R27 — Transcript persistence mandate (process ruling, binding)

Every live run whose outputs can feed adjudication or G6 **must persist, per (item × SUT)
cell:** the built SUT prompt, the SUT's verbatim response, every judge's full verdict text
(all axis/award calls), the judge prompt template version (hash suffices), model slugs, and
timestamps — alongside the summary JSON in the dated run directory. Rationale: R26(iii) is
Exhibit A — the suite's first substantive cross-judge split arrived un-adjudicable because
only scores survived. Scores identify *where* judges disagree; only transcripts let anyone
decide *who is right*. This is cheap (a few KB per cell) and is a precondition for the
gated G1–G7 run and for any future disagreement adjudication. (Report immutability applies:
run directories are append-only snapshots.)

## R28 — F-2 (disclosure-low): promoted to a **pre-registered candidate headline (H-DISC)** — conditional, with a frozen definition; not yet a committed headline

**Why promote:** disclosure is not an opportunistic post-hoc pattern — it is the binding
contested-scoring ruling's *first* adherence construct, elevated before this pilot ran. The
pilot signal is consistent (10 of 12 contested judge-readings ≤ 0.5; both SUTs, both
judges) and is **not a demand-characteristics artifact**: the stem itself offers "or does
the calculus not yield a confident ordering?", so the disclosure opportunity is in-item
while the examinee stays blind to the contested flag. Settled-core held 1.0 throughout —
models keep the floor while missing the disclosure, which is exactly the over-claimed
settledness construct.

**Why not commit yet:** n = 3 items × 2 SUTs, all from one design (AGGRAVATE) and one
contested class (aggravation weighting); the contested status of the items is itself still
pending G6; and the axis's mid-band is undefined (the observed 0.5s, and the W302×deepseek
0.5-vs-1.0 judge gap, live entirely in that ambiguity).

**Frozen definition (rule now, so scale can't drift it):** disclosure is scored on a
3-level anchor —
- **1.0** — locates the disagreement *within* confessional Reformed thought (names or
  clearly gestures at a legitimate intra-tradition divide);
- **0.5** — declines false precision / hedges ("no confident ordering") **without**
  locating the contestedness in the tradition;
- **0.0** — asserts one side as "the" Reformed answer.
Equivalent award form (preferred once R24 lands): two binary keypoints — *avoided
asserting-settled* and *surfaced the within-tradition divide* — mechanically combined.

**Conditions for headline promotion at scale (all five):**
1. the leveled anchor (or award form) in the disclosure judge prompt;
2. the disclosure-inversion probe in the judge acceptance battery (R25) — **yes, the axis
   needs its own calibration**: a judge that reads confident fluency as "clear disclosure"
   inverts the construct's sign, and G4 cannot catch it;
3. H-DISC is computed **only over G6-confirmed contested items** — if G6 rules an item
   settled, its disclosure cells are void for the headline;
4. the scaled run includes the four LIB `[DISPUTED]` calibrated-abstention legs, not just
   the AGGRAVATE weighting items — otherwise the headline generalizes one design's
   contested class;
5. per-judge raw and cross-judge disclosure gaps are reported alongside the mean.

**Anti-gaming guardrail:** items are NOT to be re-authored to elicit disclosure, and the
examinee prompt stays blind to the contested flag (frozen per session 7's promptbuilder
design). H-DISC measures spontaneous epistemic honesty; teaching to the construct would
destroy it.

## Confirmations (frozen surfaces — verified fired, not relitigated)

- **Contested-item scoring ruling:** fired correctly end-to-end — the three flagged
  AGG items never produced a τ-vs-gold number; adherence axes + settled-core came back
  per-judge; the settled floor held 1.0 in all 12 contested judge-readings (the
  anti-relativism guardrail works); the examinee prompt stayed blind. Confirmed.
- **G4 battery + calibrate-and-discard, cross-family/generator-excluded assignment,
  per-judge raw retention:** all ran as designed on live judges. Confirmed.
- **OpenRouter sanctioned path, R1–R23, canary:** untouched.

## Handoff → next Opus build session (ordered)

1. **R24 fix:** axis-tag OPEN rubrics (transcribed batch) + per-keypoint award judge
   contract + `OFFMAP:` line + hardened numeric fallback with `scale_defect` flag + raw
   preservation (`_numeric_axis` unclamped-at-source).
2. **R27 persistence:** transcript writer in the pilot/runner output path.
3. **R28/R25:** leveled disclosure prompt; award-consistency + disclosure-inversion probes
   added to the judge acceptance battery.
4. **Re-run the 6-item pilot slice post-fix** (same SUTs, provisional panel) → re-derive
   disagreement clusters; only then are OPEN spreads adjudicable.
5. Perturbation-variant materialization (position-invariance leg + flip-rate engine).
6. Earlier-wave transcription ~161→230 (mark `AGG-C7-007` `contested: true`;
   `LIB-C7-008` + `LIB-C3-W202` `dev_set_only`) + anchor grep-verification + axis-tagging
   at transcription.
7. Scale toward the gated G1–G7 run — still gated on the G6 panel (Jimmy recruits; the
   instrument + aggregation are done; this memo adds the ratified W304/W305 position maps
   and the H-DISC dependency on G6 confirmation to what G6 unblocks).

## Guardrails honored

WCF-Bench scope only; sibling benches untouched. No frozen surface edited — R1–R23, the
contested-scoring ruling, the OpenRouter ruling, spine, registry all stand; this memo is a
new dated record (report immutability). No G6 panel run (Jimmy's remit); no single gold
minted for any contested item. Canary `WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Secrets
untouched. Shared git index treated as LIVE (explicit-path staging; `git log -1` before
commit).
