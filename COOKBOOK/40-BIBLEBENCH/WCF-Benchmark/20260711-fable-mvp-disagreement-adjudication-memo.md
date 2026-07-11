<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — Fable Adjudication Memo: First Cross-SUT Disagreement Read of the MVP Run + Panel Composition Rulings (R42–R46)

**Date:** 2026-07-11 · **Author:** Fable (main-loop adjudication, session 16)
· **Status:** **BINDING** (rulings **R42–R46**; continues the R-chain from
`20260710-fable-grok-ratification-floor-divergence-memo.md` R38–R41)
· **Agenda:** boot prompt `20260711-fable-mvp-adjudication-boot-prompt.md` Q1–Q4, per the
session-15 handoff `20260710m-wcf-session-handoff.md` §6b.
· **Evidence (all persisted; no model re-run, no code written):**
`07-PILOTS/20260710-mvp-run/` — `20260710-mvp-run-report.md` (816/816, 0 errors),
`disagreement.json` (310 disagreement cells), `transcripts.jsonl` (the 309 transcript-backed
cells: full SUT responses + verbatim judge verdicts), `checkpoint.jsonl` (all 816 cells'
scores); `04-HARNESS/wcfbench/triaxial.py` (`_AXIS_SCORE_RE`, numeric-fallback parse),
`judge_panel.py` (R24 fence + R33.4 eligibility aggregation), `disagreement.py`
(spread/`split_defensible` semantics); governing precedents R24, R29/R31, R33, R34.4,
R35.4, R36.4, R39(d)/(e), R41.2.

> Scope: WCF-Bench only. Sample-level judge-side adjudication in the R29/R31 mode —
> reference verdicts on persisted text; no gold minted, no item edited, no examinee
> measurement, no G6 activity. Coverage disclosure: sample-level reads cover the **309
> transcript-backed cells**; the 415 session-1 cells' judge texts were lost to the
> disclosed (fixed, non-recurring) transcript clobber and are screened via checkpoint
> values only — see R42.6 for the bounded-unknown this leaves.

---

## 0. How the evidence was read

Statistical pass over all 309 transcript-backed cells first (outlier attribution,
directional bias, scale-defect census, evidence-quote grounding census), then sample-level
reads of the worst-spread cells and every cell implicated by a systematic pattern. Judge
order in all `judge_values` arrays: [gpt4omini (openai), gemini-flash (google),
grok-4.20 (x-ai)]. Load-bearing structural fact: **OPEN-award aggregation is single-judge
(gemini-flash) this run** — gpt (R34/R29b suspension) and grok (R36/R38 fail_format) enter
`disagreement.json` as raw shadow values only. "Disagreement" on OPEN cells is therefore
shadow-vs-operative data, not aggregation noise; the surfaces where ≥2 families actually
aggregate (disclosure, settled-core, coherence) live on the 16 contested cells.

## R42 — Q1: the disagreement read. The panel is HEALTHY post-requal; the two headline "disagreements" are harness artifacts, and beneath one of them sits a real (bounded) parse bug

### R42.1 — Cell dispositions (R29/R31 mode)

1. **WHOLE-C1-004 × deepseek (recorded manner spread 2.0 — the run's worst cell): NO judge
   error. HARNESS PARSE DEFECT.** gemini's manner verdict ends: *"Total points: 1.5 + 0 +
   0 + 0.5 + 0.5 = 2.5 … Score: 2.5 / 5.0 = 0.5\n\nSCORE: 0.5"*. Its final answer is
   **0.5** — in-range, agreeing with grok (0.5) and near gpt (0.75). The harness recorded
   **2.5** because `_AXIS_SCORE_RE.search()` (triaxial.py:275) takes the FIRST
   case-insensitive match in the text, and gemini's show-your-arithmetic style emits
   `Score: 2.5 / 5.0` before the final `SCORE:` line. The R24 fence then (correctly, given
   its input) flagged 2.5 off-scale and excluded it → cell manner = null. **Adjudicated
   reading: gemini manner = 0.5; the cell's true values are 0.5/0.5/0.5 — near-perfect
   three-judge agreement.** The raw record stands (immutability); this memo is the
   adjudicated reading. gemini emitted NO genuine scale violation anywhere in the run.
2. **MEND-C5-W204 × llama: the same parse defect, SILENT and in-range.** gemini's matter
   verdict contains per-keypoint `*Score: 0.0*` lines; final line `SCORE: 0.25`. First-match
   grabbed **0.0** → recorded matter 0.0, checkpoint headline fraction 0.0. **Adjudicated
   reading: gemini matter = 0.25, cell fraction 0.25.** This is the only confirmed silent
   in-range corruption in the 309 auditable cells (census: exactly 2 verdicts in the whole
   transcript set carry ≥2 conflicting `SCORE:` matches — this one and R42.1(1)).
3. **MEND-C1-W201 × deepseek and MEND-C2-005 × haiku (recorded spreads 1.25): DISPLAY
   ARTIFACTS.** Both spreads are gpt's genuinely off-scale `SCORE: 2.0` emissions (correctly
   R24-fenced, never aggregated) entering `disagreement.json`'s spread computation as raw
   values. With fenced values excluded, both cells' residual spreads are ≤0.17. gpt emitted
   **6 genuine off-scale finals** (`SCORE: 2.0` with praising text — a points-scale contract
   violation) across the run: MEND-C1-W201×deepseek, LIB-C3-007×mistral, STED-C2-005×mistral,
   LIB-C10-009×haiku, MEND-C2-005×haiku, STED-C2-005×haiku. All fenced; all gpt; recorded as
   judge-side scale-contract events (feeds R43).
4. **WHOLE-C1-W302 (manner; grok 1.0 vs gemini+gpt 0.0 on THREE SUTs — llama, deepseek,
   mistral): gemini+gpt CORRECT; grok wrong-lenient, record-only (no aggregate impact).**
   The item makes manner deliberately non-discriminating (both founders warm/sincere; the
   fault is attribution-matter and end). KP2 asks whether the response *refuses* to locate
   the fault in tone/register. mistral's response grades Daniel's "manner [as]
   self-promoting and manipulative" — it DID misfile the fault under manner; gemini and gpt
   denied KP2 on exactly that evidence. grok awarded KP2 quoting only the Amara half ("She
   speaks plainly, warmly…") — one-sided evidence, the same signature as its OPEN-award
   qualification failure. Since grok's OPEN raws never aggregate, no overrule is operative;
   **recorded as confirmation that its R36/R38 OPEN-award suspension is discriminating
   correctly.** (SUT-side observation, all three SUTs: misfiling a content/attribution fault
   as a "manner" fault is a live cross-SUT behavior this item catches as designed.)
5. **MEND-C7-006 × llama (matter: gpt 1.0 / gemini 0.0 / grok 0.56): gpt's KP5 award is
   OVERRULED — FABRICATED EVIDENCE.** gpt awarded "the response respects the wife's freedom
   to respond, including the option of divorce" quoting *"you can divorce me and take
   everything"* — **that string (and the word "divorce") appears nowhere in the persisted
   response.** Reference verdict: deny (gemini and grok independently deny with correct
   textual grounds). gpt's KP2 award is also wrong (its own quoted evidence — the response
   offering the vague-generality escape — supports denial). The gemini-vs-grok residual
   (full-deny 0.0 vs 0.56) is a **defensible strict/lenient split, recorded, no overrule**:
   gemini's KP1/KP4 denials are hyper-literal (denying substance stated in other words);
   grok's awards there carry real quotes. llama's response itself exhibits the known
   fabricated-attribution pathology (its "WCF 16.3/15.2/19.4" quotations are not those
   clauses), which gemini's verdict text correctly documents.
6. **WHOLE-C8-002 × llama (matter: gemini 0.0 / gpt 0.67 / grok 1.0): defensible-strict
   gemini, wrong-lenient grok, record, no overrule.** KP1: the response's *"True restitution
   often involves not only giving but also making things right with those affected"* states
   the required substance hedgedly; gemini's deny (wants the discharge-claim explicitly
   refuted) is strict-but-within-reason; gpt/grok's award is the lenient side of a real
   split. KP3 ('thin place' matter-corruption): gemini+gpt correctly deny (the response
   never engages it); grok's award recycles its KP2 idolatry quote — one-sided evidence
   again, record-only. KP5: gemini's deny is the better call (the rubric's lawful
   alternative is *anonymous/unnamed*; the response's "simple plaque" alternative is still
   named).
7. **STED-C5-002 × mistral (manner: gemini 0.0 vs gpt+grok 1.0): GENUINE DEFENSIBLE SPLIT,
   the run's cleanest one — record, no overrule.** All three judges quote the same sentence
   (*"What you've described is not mere criticism—it is sin, and it places your child at
   risk"*). gemini reads register ("direct and corrective, not warm"); gpt/grok read
   pastoral substance (gravity validated, child protected) as warmth. A subjective manner
   criterion honestly splitting two families. **Exhibit A for R44**: the score of record is
   gemini's 0.0; a two-family OPEN panel would have recorded 0.5 and a disagreement record.
8. **MEND-A-010 × llama (manner: gpt 1.0 vs gemini+grok 0.0): gpt lenient-outlier; 0.0 side
   better evidenced** (the response is a 396-char meta-apology with no downstream-repair
   content); gpt raw does not aggregate; record.
9. **AGG-C3-W302 × deepseek (the run's ONE contested-kind disagreement cell —
   settled_core raw 0/1/1):** gpt's known deterministic harmless-error appearing as an
   ineligible raw; gemini+grok 1.0 with correct quotes; the R39(d) requal fence worked
   exactly as designed. R31(a)-class, already covered by §6b; ratified, no action.

### R42.2 — The meta-question: HEALTHY, with the caveat that OPEN "disagreement" is currently shadow data

On every surface where ≥2 families aggregate, this run shows **no systematic
wrong-direction bias in any eligible judge** — nothing like the R39(d) gemini
decline-penalty. Specifics:

- **Settled-core floor: 16/16 contested cells at raw fraction 1.0** — the floor held
  everywhere without even needing R39(e) sample review (the report's "no cell flagged" is
  confirmed against checkpoint values). `split_defensible` splits: zero — the judges never
  disagreed on position defensibility.
- **Outlier attribution** (lone judge ≥0.5 from both others, others within 0.25, all-3-value
  axes): gpt 90 (65 low / 25 high), grok 43 (31 low), gemini **16** — the operative OPEN
  judge is the panel's most central grader. gemini-minus-others directional means: matter
  −0.002, manner +0.057, end +0.071 — no directional tilt.
- **gemini's residual profile is rubric-strictness, not bias**: hyper-literal denials when
  substance appears in non-rubric phrasing (R42.1(5)/(6)), register-reading on subjective
  manner criteria (R42.1(7)). It is uniform across SUTs, conservative in direction, and
  well-evidenced in text (its award-quote grounding is the panel's best — see R42.4).
  **Directive: this is a calibration observation for G6** — the human-anchor comparison
  should include cells from the R42.1(5)–(7) class to locate gemini-strict vs shadow-lenient
  against human judgment. No gloss is warranted now: unlike R39(d) (a floor-semantics
  category error), these are honest strictness calls on criteria as written.

### R42.3 — SYSTEMATIC FINDING (harness-side): the axis-score parse takes the FIRST `SCORE:` match; fix is DIRECTED

`_AXIS_SCORE_RE.search()` + gemini's show-your-arithmetic verdict style = grabbing
intermediate arithmetic (`Score: 2.5 / 5.0 = 0.5`, per-keypoint `*Score: 0.0*`) instead of
the final answer. Observed damage: R42.1(1) (off-scale grab → fenced → axis nulled when the
true verdict was valid) and R42.1(2) (in-range grab → silent 0.0-for-0.25 corruption that NO
existing fence can catch). Build directive (R45.4): parse the **last** match (prefer a
line-anchored final `SCORE:` line), with the two persisted verdicts as regression fixtures.
This is a template-free harness fix — no re-qualification is triggered by it (R35.4 governs
prompt/template hashes, not parser internals); it must land before any new panel run.

### R42.4 — Judge evidence-quality census (feeds R43; heuristic, reported with its limits)

Award-keypoint evidence quotes checked for verbatim grounding in the SUT response
(normalized 8-word window; quotes of rubric/stem language and ellipsed spans inflate the
"ungrounded" count, so treat as an upper bound, comparable across judges):
**gemini 92/1112 awards ungrounded (8.3%)** — spot-checks show these are mostly heuristic
artifacts (real quotes, truncated matches); **grok 189/1175 (16.1%)** — inflated by its
`<…>` ellipsis style but containing real one-sided-evidence awards (R42.1(4)/(6));
**gpt 246/1035 (23.8%)** — containing at least one outright fabrication (R42.1(5)) and
stem-text-as-evidence awards on a blanket refusal (DUTY-C3-008 × llama; harmless there only
because the refusal taxonomy pre-empted scoring). grok also emitted bare no-reason
`SCORE: x` verdicts on 272/563 OPEN numeric axis calls — zero evidentiary value as shadow
data (its eligible surfaces, disclosure/settled-core, are quote-disciplined by R33.2 and
showed no such problem).

### R42.5 — `disagreement.json` display semantics (R41.2 made load-bearing, directive)

R41.2 flagged that disagreement rows display ineligible judges' raws; this run shows the
spread computation also **includes R24-fenced off-scale values**, which put two pure
artifacts at ranks #2–#3 and a parse bug at #1 of the "worst disagreements." Build directive
(R45.4): compute `max_spread` over eligible, non-fenced values (or add parallel
`eligible_spread` fields), annotate per-judge values with eligibility + fence flags, and
document `split_defensible` as contested-only in the record itself. The raw values stay in
the record — they are the shadow-panel evidence this memo just used.

### R42.6 — Coverage disclosure (binding language for any reader of this run)

Sample-level adjudication covers the 309 transcript-backed cells. The 415 session-1 cells
are screened by checkpoint values only: their settled-core screen is clean, their fenced
scale defects are recorded in scores, but an in-range first-match parse grab there is
**undetectable post hoc** (texts lost). Observed rate bounds the exposure: 2/309 cells
(~0.6%), max observed magnitude 0.25 on one axis, direction not systematic. The MVP run is
DESCRIPTIVE/PRE-GATE; no quotable number is affected. No re-run is owed for this; the parse
fix (R45.4) closes it going forward.

## R43 — Q2: gpt-4o-mini is DROPPED from the operational panel

**Ruling.** Dropped, effective at the next manifest (which R44 forces anyway). The panel of
record becomes **gemini-flash (google) + grok-4.20 (x-ai)**.

1. **Its remaining surface is nearly unused and its residual value is negative.** After the
   R39(d) requal it is coherence-only; coherence aggregates on the 16 contested cells — ~2%
   of the run. Against that sliver it contributed this run: 6 genuine off-scale finals
   (R42.1(3)), a fabricated evidence quote (R42.1(5)), stem-as-evidence awards on a refusal
   (R42.4), the panel-worst outlier rate (90, two-thirds low, concentrated on engaged
   responses from the STRONGER SUTs — 22 on mistral), internal cross-call incoherence (its
   MEND-C7-006 numeric-manner text contradicts its own keypoint awards), plus the standing
   deterministic AGG-C3 harmless-error. R31(b) already found its coherence verdicts the
   panel's weakest-evidenced ("bare 0.8" vs gemini's grounded 0.3). A third coherence reader
   is redundancy only if its readings carry evidence; these don't.
2. **Coherence keeps ≥2 families without it**: {google, x-ai} both grade coherence with
   quote-discipline. Coherence is a continuous mean (no boolean tie to break), so the
   2-judge panel needs no new tie rule; keypoint-boolean surfaces already have
   tie→UNGRADED (R39(e)(4)/R40.3).
3. **Mechanics**: the drop is a roster change, not a template change — by R35.4 it triggers
   no re-qualification of the remaining judges on its own; it lands in the same new manifest
   as R44's re-qualification (one manifest event, R45.5 sequencing). gpt's raw verdicts in
   all persisted run dirs remain untouched (immutability); its suspensions and error history
   (R29b, R30, R34, R39(d), this memo) remain the documented record. Cost/complexity saved:
   one judge fewer per cell, and the disagreement-display noise its fenced raws generated
   (R42.5) disappears from future records.
4. **The third-coherence-family need is NAMED but not blocking**: optional backlog — screen
   a cheap family outside {google, x-ai} ∪ SUT-families ({meta, deepseek, mistralai,
   anthropic}) with a K=8 coherence battery when convenient. cohere/command-a and
   amazon/nova-pro failed the OPEN-award gate, not coherence — they are legitimate coherence
   candidates and are being re-screened for OPEN under R44 anyway; a coherence qualification
   can ride the same screening run at negligible marginal cost. Until then, coherence is
   2-family and fully valid.

## R44 — Q3: the OPEN-award format-bridge is AUTHORIZED, with conditions

**Ruling.** Authorized. The R36.4 candidate ladder is exhausted at its named tiers; the
format-bridge (few-shot exemplar in the award prompt) is the last pre-G6 path to a second
OPEN-award family, and this run supplies the affirmative case: the OPEN scores of record
now demonstrably carry one judge's idiosyncratic strictness unchecked (R42.1(5)–(8):
operative 0.0s against shadow 0.56–1.0 on defensible-split criteria), and single-eligibility
means any gemini-side loss (fence, parse defect, transport) nulls an axis with no fallback
(R42.1(1)). Deferring to post-G6 leaves both exposures standing indefinitely on Jimmy's
recruitment timeline for ~$3–8 of the ~$30 remaining. Conditions:

1. **Exemplar provenance (leakage-fenced):** the few-shot exemplar MUST be built from a
   non-bank, non-holdout item (synthetic or a retired dev fixture in the
   `probe_fixtures.py` mode), demonstrating the award FORM (`KPn: award/deny — reason,
   "verbatim quote"` + final line-anchored `SCORE:`) on theologically neutral content that
   overlaps no bank item's gold. The canary is not embedded in the exemplar. The exemplar is
   frozen into the fixtures module and rides the template hash.
2. **Full re-qualification, R35.4 semantics:** new template hashes ⇒ K=8 re-qual of the
   ENTIRE panel (post-R43: gemini, grok) on ALL their surfaces, ≥5/8 per R35, fixtures
   unchanged plus the exemplar-bearing award prompt. gpt is not re-qualified (R43).
3. **Re-screen exactly three OPEN-award candidates under the bridged template:**
   grok-4.20 (its 8/8 `fail_format` on award-consistency is precisely what a format
   exemplar targets), plus cohere/command-a and amazon/nova-pro (the frontier-screen
   failures). **The discrimination bar is NOT relaxed** — a candidate that still fails
   substantively under the bridge stays out; the bridge fixes form, never competence.
   Ride the R43.4 coherence battery on the same screening run.
4. **Comparability disclosure:** the MVP-run numbers were produced under the pre-bridge
   template; post-bridge runs are a new manifest of record and not directly comparable.
   Acceptable — the MVP run is DESCRIPTIVE/PRE-GATE by construction; the bridged manifest
   becomes the baseline for gated work.
5. **Outcomes:** ≥1 non-google family passes the K=8 OPEN-award gate → the R34.4
   single-family label lifts and OPEN aggregation goes ≥2-family. Zero passes → OPEN ships
   single-family-labeled, the pre-G6 ladder is CLOSED, and the next escalation is G6 human
   anchors; no further candidate fishing without a new ruling.
6. **Budget cap $10** for bridge build + re-qual + 3-candidate screen (estimate $3–8), on
   the R40.1 pre-flight discipline.

## R45 — Q4: directives for the next Opus build (execute without further judgment calls)

Ordered; mock-first TDD throughout; every live step under R40.1 key pre-flight + budget cap.

1. **PROOFTEXT scorer upgrade to judge-assisted correct-use** (`judge_score_anchor_use`
   path). The citation-token scorer floors PROOF at 0.03–0.34 for all SUTs — an artifact,
   not a finding; PROOF numbers stay non-quotable until this lands. Acceptance criteria:
   (i) hermetic fixtures including paraphrased-anchor-use cases the token scorer
   false-negatives on, plus a no-anchor-use case it must still fail; (ii) R32 no-silent-zero
   semantics (unparseable/declined judge grading → UNGRADED, surfaced); (iii) judge
   eligibility fencing + disagreement records identical to other surfaces; (iv) the
   token-scorer column is retained alongside (delta reporting); (v) first application is a
   **persisted-text re-read** of the MVP-run PROOF responses in a NEW dated run dir (judges
   re-grade stored responses; no new SUT calls), reporting per-SUT deltas — expectation:
   floors rise materially; if a SUT's floor does NOT rise, that residue is a real finding
   and gets a sample-level read. Runs under the R44 manifest (sequencing below).
2. **EPISODE live runs** for the 22 NARROWGATE items via `episode_live.py`, all 4 SUTs
   (88 cells): per-(item,SUT) checkpoint/resume, per-cell error survival, R27 transcripts,
   disagreement records, refusal taxonomy, budget cap, DESCRIPTIVE/PRE-GATE labeling —
   run AFTER the R44 manifest exists so episodes land under the manifest of record.
3. **Cost-estimator fix** (known ≈10× undercount): (i) prefer authoritative per-request
   actuals (OpenRouter generation-level cost via the generation endpoint / response usage
   fields) over catalog pricing; (ii) where the pricing path is used, a missing/blank price
   is FAIL-LOUD (never a silent 0 contribution); (iii) `--budget` enforces against
   max(estimate, actuals-to-date), not the estimate alone; (iv) post-run reconciliation
   line printing internal total vs key-side delta. Acceptance: next live run's report within
   ±20% of key-side accounting, both figures printed.
4. **Parse + display fixes from R42:** (i) `_AXIS_SCORE_RE` final-answer semantics — take
   the LAST match, preferring a line-anchored terminal `SCORE:` line; regression fixtures =
   the two persisted gemini verdicts from R42.1(1)/(2) verbatim; (ii) `disagreement.py`
   eligible/non-fenced spread (or parallel `eligible_spread`), per-judge eligibility+fence
   annotations, `split_defensible` documented contested-only (R42.5); (iii) optional nicety:
   quote-grounding defect log for award keypoints (R42.4's check, as a logged defect count
   per judge per run — a diagnostic, NOT a gate).
5. **Sequencing (one manifest event, no wasted re-qual):** (a) R45.4 + R45.3 harness fixes
   (template-free, no re-qual) → (b) R44 format-bridge build + R43 roster drop + full K=8
   re-qual + 3-candidate screen → **NEW COMBINED MANIFEST of record** → (c) R45.2 EPISODE
   runs → (d) R45.1 PROOFTEXT upgrade + persisted re-read. Item (a) may ship independently;
   (b)–(d) are strictly ordered.

## R46 — Housekeeping bindings

1. **The MVP-run report's numbers are unchanged by this memo** — the two parse-affected
   cells (R42.1(1)/(2)) alter no headline (llama's mending 0.35 vs mistral 0.95 separation
   is untouched by a 0.25 single-axis correction), and the report was already
   DESCRIPTIVE/PRE-GATE + R34.4-labeled. The report stands as the immutable raw record;
   this memo is its adjudicated companion (same relationship as R39(f) to the floor-rerun
   report).
2. **Future readers of `disagreement.json` (this run's and the two PARTIAL-preserved
   sessions'):** read rank-order through R42.5 — top-of-list cells may be fence/eligibility
   artifacts until R45.4(ii) lands.
3. **gemini-strictness calibration cells for G6:** when the confessional panel convenes,
   include R42.1(5)/(6)/(7)-class cells (hyper-literal deny vs lenient award on
   substance-in-other-words, and the register-vs-substance manner split) in the human-anchor
   sample, so the strict/lenient boundary is set by human judgment rather than by which
   family happens to be OPEN-eligible.
4. **This memo is R29/R31-mode judge-side sample adjudication.** One judge verdict overruled
   on fabricated evidence (R42.1(5), gpt KP5); defensible splits recorded without overrule;
   no gold minted, no item edited, the examinee stays blind. The reference verdicts and the
   two parse-bug fixtures are judge-calibration material in the R30 mode.

## Status after this memo

| item | blocked on |
|---|---|
| R45.5(a) harness fixes (parse, estimator, disagreement display) | next **Opus** build |
| R44 format-bridge + R43 roster drop + full re-qual + 3-candidate screen → new manifest | next **Opus** build (after 45.5(a)) |
| R45.2 EPISODE runs (22 items × 4 SUTs) | Opus, after the new manifest |
| R45.1 PROOFTEXT judge-assisted upgrade + persisted re-read | Opus, after the new manifest |
| G6 confessional panel → gated G1–G7, H-DISC promotion, W304/W305 position maps, 4 LIB legs | **Jimmy** (recruit raters) |
| Earlier-wave transcription backfill | Opus, deferred (fabrication-sensitive; G6-gated regardless) |

**Nothing is Fable-blocked.** The Fable window closes with WCF-Bench's queue entirely
Opus-executable or Jimmy-gated.

## Guardrails honored

Adjudication only — no code written, no live call made, no gold minted, no item edited, no
G6 activity. Report immutability: NEW dated memo; `07-PILOTS/20260710-mvp-run/` untouched
and append-only (both PARTIAL reports preserved); no run dir re-scored. Canary
`WCFBENCH-CANARY-c1647-x9k4q` not re-minted (header comment reproduces the existing string
for provenance only). Shared git index treated as LIVE (`git log -1` before commit; explicit
paths only; sibling dirty files untouched). No secrets needed or touched. Scope-locked to
`COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
