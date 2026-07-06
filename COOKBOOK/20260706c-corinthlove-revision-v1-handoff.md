# CORINTHLOVE Revision Session 1 (v1 briefs) — handoff

**Written by:** Opus revision session, 2026-07-06
**Scope executed:** §1 of `COOKBOOK/40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-OPUS-REVISION-INSTRUCTIONS.md` — v1 briefs 01–07 (CO-1, CO-2 on all seven; D-01…D-07 per brief; CO-10 crosswalk into the v1 portfolio).
**Git:** NOT committed, NOT pushed, index untouched (per instructions).

---

## 1. Edits applied per file

All targeted (no rewrites, no section renumbering). Each brief's frontmatter status stamped
`status: gate-revised 2026-07-05 (D-<nn>; CO-…) — awaiting Opus question-bank build`.

| File | Orders applied | Summary of edits |
|---|---|---|
| `CORINTHLOVE/DESIGNS/01-longsuffer.md` | **D-01, CO-1, CO-2, CO-12** | §4: added "Length–rung identification" (flat-provocation length-control arm + rung-position jitter) and "Antagonist protocol" (bounded pre-authored branch table) subsections. §5: RMST made primary survival summary, Cox/frailty demoted to secondary w/ mandatory PH diagnostics; CO-1 item-calibration bullet added. §8: removed "IRT-adapted pilot (2PL)" → native survival-model pilot. §3+§9 (CO-12): reframed "context-length reversion" as published multi-turn/long-context drift (GDM claim flagged unverified/not load-bearing). §12: split Phase A / Phase B; IRT pilot removed. |
| `CORINTHLOVE/DESIGNS/02-costlykind.md` | **D-02, CO-1, CO-2** | §5: c₅₀ now estimated/reported PER COST CURRENCY (pooling only if measurement-invariance supports it); CO-1 bullet added. §6: added consequence-model validity note (inter-author agreement ≥2 authors, 80% floor — Phase B). §12: Phase A/B split; IRT pilot → Phase B protocol; consequence-table agreement study → Phase B. |
| `CORINTHLOVE/DESIGNS/03-statusgame.md` | **D-03, CO-1, CO-2** | §3: incentive structure replaced — BOTH conditions reward ABSOLUTE team-output quality, Condition B differs only in framing language w/ zero payoff consequence + manipulation-check probe. §5: CO-1 bullet added. §7: dangling "10 ACQUIRE" → "10 NOISYGONG" (+superseded-per-§8 note). §8: added re-gate requirement (focused single-reviewer adversarial re-review before bank build). §12: Phase A/B split; manipulation-check probe (authoring, A); pilot + re-review → Phase B. |
| `CORINTHLOVE/DESIGNS/04-ledger.md` | **D-04, CO-1, CO-2** | §3: added offense-class restriction (pure-grudge cell EXCLUDES deception/dishonesty/betrayal; rational-updating Bayesian control analysis). §5: CO-1 bullet added. §12: Phase A/B split; pilot + rational-updating control analysis → Phase B. |
| `CORINTHLOVE/DESIGNS/05-truthgrace.md` | **D-05, CO-1, CO-2** | §5: PRIMARY replaced — joint (T,C) absolute coordinates; frontier/Pareto machinery conditional on empirical T–C tradeoff; **frontier-distance scalar removed as primary**; added judge-reliability-for-T bullet (κ floor 0.75); CO-1 bullet added. §6: T reworded from "mechanical" → "inventory-checked with judge-mediated assertion classification". §8: kill-gate moved off frontier-distance to joint (T,C)+T-decay. §12: Phase A/B split; 500 human-validated judgments + κ audit + pilot → Phase B. |
| `CORINTHLOVE/DESIGNS/06-rooftop.md` | **D-06, CO-1, CO-2** | §3/§9: novelty reframed — prior CI operationalizations (ConfAIde/PrivacyLens/AirGapAgent, "Opus: verify cites") cited; ROOFTOP's novelty = BIDIRECTIONAL axis. §4: added norm-authoring authority model (closed normative frame; inter-author 3-way-label reliability ≥3 authors 80% floor = Phase B ship gate). §5: CO-1 bullet added. §7: added mandated-reporting CALIBRATION subscale note. §12: Phase A/B split; pilot + reliability study + trap calibration → Phase B. |
| `CORINTHLOVE/DESIGNS/07-charitroc.md` | **D-07, CO-1, CO-2** | Major rework: parametric SDT (d′/criterion c) replaced with **empirical ordinal ROC / AUC per item family** (ordinal compliance/refusal/verification scale; family-stratified hierarchical pooling) across §3/§5/§8. §3/§5: operating point evaluated against explicit cost-ratio family (1:1/3:1/10:1). §5: Stage-3 updating SPLIT OUT as its own separately-reported metric; CO-1 bullet added. §7: "d′ recomputed per panel" → "discrimination (AUC) recomputed per panel". §10 podium claim rewritten. §11: `criterion_frozen_despite_cue` → `operating_point_frozen_despite_cue`. §9 related-work: single allowed "no parametric d′ assumed" contrast retained. §12: Phase A/B split; pilot + graded-engagement human calibration → Phase B. |
| `CORINTHLOVE/DESIGNS/00-10cbench-portfolio.md` | **CO-10 (+CO-1 spine consistency)** | Appended **§9 "Rubric→registry crosswalk (CO-10)"** verbatim table + caption. Also updated spine §3.3 to remove the `a<0.8` / 2PL / "test-information-peaks" ship-gate (aligning it with its own binding amendment §8.1 CO-1) — see Discrepancy note 1 below. Portfolio not status-stamped (it is a portfolio doc, not a brief). |

---

## 2. Discrepancies / judgment calls logged

1. **`a<0.8` lives in the portfolio spine, not in any brief.** CO-1's literal scope is "each brief's metrics/statistics section AND its §12 checklist," but the `a<0.8` / 2PL / "test information peaks at the frontier" ship-gate text existed only in portfolio `00` §3.3 (the shared hardening spine). Since portfolio §8.1 (CO-1) already **binds** that gate as "removed," I made a minimal consistency edit to §3.3 so the file is internally consistent and the session-level `a<0.8` removed-pattern grep clears. This is warranted by the file's own amendment, not an improvised design change. The one remaining `a<0.8` hit (portfolio line 99) is the CO-1 amendment record itself, which legitimately names the removed pattern (historical/change-order note).
2. **No brief contained the exact phrase "first operationalization of contextual integrity for agentic systems" (D-06a).** The novelty claim lived as §9's "operationalized for agents for the first time"; I replaced that phrasing with the ConfAIde/PrivacyLens/AirGapAgent positioning + bidirectional-axis novelty, and updated the §9 Novelty sentence. Substantively equivalent target; noting the wording difference.
3. **CO-2 "without changing individual items" — two minor additive touches.** Item (1) of the 04-LEDGER and (2) of some §12 lists gained a short parenthetical pointer to the applicable D-order (e.g., "with the D-04 offense-class restriction"); bundled items that mix authoring + human-annotation (e.g., 05's "mechanical T-scorer … with ≥500 human-validated judgments") were split across Phase A (scorer code) / Phase B (the human judgments) per CO-2's explicit "move to Phase B as a protocol document" rule. Item wording otherwise preserved.

No brief was skipped; every named target text was located.

---

## 3. §0.6 verification-grep output (captured)

```
(1) FORBIDDEN sibling bench names (TENCOMMANDMENTS|FRUITBENCH|SERMONMOUNT|DECALOGUE):
    Only pre-existing mentions in portfolio 00 line 5 (the scope-EXCLUSION note declaring them
    out of scope) — not cross-references introduced this session. CORINTHLOVE-v2/v3 references
    (lines 101/102, pre-existing §8 CO-9/CO-10; and §9 "v3 portfolio §3", "v2-10 ONEBODY") are
    ALLOWED folders per this workstream. → no forbidden cross-reference.

(1b) icmi-proceedings:                    0 hits.
     moral-compactness:                   3 pre-existing hits (portfolio lines 50, 91, 103), all in
     "treat as unverified hypothesis / must re-anchor" framing — NOT citations of the banned
     statistics. Compliant; none introduced this session.

(2) gate-revised frontmatter count:       7  (01,02,03,04,05,06,07) — matches session brief list.

(3) REMOVED pattern a<0.8 | a < 0.8:      1 hit = portfolio line 99 (the CO-1 amendment record
     naming the removed pattern). Spine gate §3.3 excised. ✓

(3b) frontier-distance (05-truthgrace):   2 hits, both stating it "is removed as a primary" (D-05
     removal notes), not usage-as-primary. ✓

(3c) parametric d′ (07-charitroc):        1 hit = line 54, the related-work "no parametric d′
     assumed" contrast — the ONLY location the grep note permits. ✓ (residual §7 "d′ recomputed
     per panel" was found and fixed → "discrimination (empirical ordinal AUC) recomputed per panel".)

(3d) residual "IRT pilot" / "2PL" in briefs 01–07:  0 hits. ✓

(4) YAML seed-block lint:  Brief 01 block parses. Briefs 02/04/05/06/07 seed blocks fail the strict
    parser on unquoted colons in prose stage_N values — CONFIRMED PRE-EXISTING at HEAD (identical
    failure set before this session). My only in-YAML edit (07 failure_modes rename) parses the
    same as HEAD. No new YAML breakage introduced. ✓
```

**Grep verdict: PASS.** All removed-pattern excisions confirmed; frontmatter count exact; no forbidden strings introduced; no new YAML breakage.

---

## 4. What the next session does

**Revision Session 2 (Opus)** — instructions doc **§2**: v2 briefs `CORINTHLOVE-v2/01…10` (D-08…D-17) + the v2 `98-opus-test-case-authoring-guide.md` CO-5 edits. Portfolio v2 `00` and v3 `00/98` already carry their gate amendments — do not edit further except where §2 names. End with a dated handoff (`COOKBOOK/2026MMDD*-corinthlove-revision-v2-handoff.md`) + pasted §0.6 grep output.

Then Revision Session 3 (§3, v3 briefs, D-18…D-27 + ALL-TEN family-level gate wording), then the STATUSGAME focused re-review, then bank building per CO-8 (DIMGLASS first).

**Deferred to Session 3 completion (per instructions §4.5):** memory update to `corinthlove-v2-portfolio-state.md` / `corinthlove-v3-portfolio-state.md` (revisions applied; next = STATUSGAME re-review, then DIMGLASS bank). Not done this session (v1-only scope).

**Binding rules unchanged:** 1 Corinthians 13 scope only; no `icmi-proceedings` "moral compactness" citations; no deletions (RECYCLE-BIN); no edits to dated STATISTICS files; commit/push only when Jimmy asks (check `git log -1` first).
