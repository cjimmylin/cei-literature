# CORINTHLOVE Revision Session 3 (v3 briefs) — handoff

**Executor:** Opus subagent, 2026-07-06. **Authority:** `40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-OPUS-REVISION-INSTRUCTIONS.md` §3 (+ §0 global rules). **Write scope:** `40-BIBLEBENCH/CORINTHLOVE-v3/DESIGNS/*.md` only (+ this handoff). Did NOT touch CORINTHLOVE-v2 (parallel session), CORINTHLOVE/DESIGNS, portfolios, 98 guides, git, or memory.

Targeted edits only — no rewrites, no section renumbering. Frozen C1–C16 registry (portfolio §3) untouched.

## Edits applied per brief (all stamped `status: gate-revised 2026-07-05 (…) — awaiting Opus question-bank build`)

- **01-crossroads — D-18 + ALL-TEN(CO-6b).** §2 + §5: primary scoring reframed to **direct key-based clause scoring**; 16-dim Thurstonian latent-profile model demoted to pre-registered exploratory analysis. §7(a): appended CO-6b family-gate alternative to the `≥8 clauses` gate. Stamp `(D-18; CO-6b)`.
- **02-weeklong — D-19 (major) + ALL-TEN(CO-6b).** Replaced the **tagged/untagged contrast** throughout (§2/§3/§5/§6.1/§6.3/§7/§8/§11) with the **salience-gradient design** (all scored windows seeded; exam-behavior signal = slope of window score on salience; filler = matched-salience unscored). §3 claim-language: "deployed behavior" → "sustained enacted profile under continuity". Descope (§5/§11): pilot **3 weeks × ~250 turns/model**, C9 control-week pairing on designated subset, generator assert **≥30 weeks (was ≥60)**, pilot_protocol 3 weeks (was ≥6). §7(a): CO-6b appended. Stamp `(D-19; CO-6b)`.
- **03-manymirrors — D-20 (major).** §4/§5/§6.1: replaced Latin-square-as-primary with **certified twin-structure pairs** (within-model hypocrisy indices over S/S′ twins; twin-equivalence error → index CIs; Latin-square retained only as cross-model calibration layer). §5/§7(a): **CT-CM removed as primary**, episode-level variance components (CO-6a L2) primary; CT-CM → limitations note (infeasible at n=10). §11 items 1/2/3/6 updated (twin-pair authoring, twin-pair role assignment, S↔S′ certification load-bearing, variance-components analysis). Stamp `(D-20)`.
- **04-witness — D-21.** §2: added **post-episode recall probe** (secondary/diagnostic channel; separates noticed-but-abstained from never-noticed; primary metrics stay action-based). §11 item 1: abstain-class "correct non-intervention" labels require **≥80% inter-rater agreement (3 raters)**; low-agreement → excluded/contested set. Stamp `(D-21)`.
- **05-agapegame — D-22.** §5 + §11 item 5: added **goodness-of-fit gate** — per-model posterior-predictive check of fitted strategy family vs. observed moves; poor-fit models reported **UNCLASSIFIABLE** with descriptive stats, never force-classified. Stamp `(D-22)`.
- **06-weighbridge — D-23.** §4/§11 item 3: conflict grid split into **12 core (confirmatory, full fractional-factorial) + 12 exploratory (descriptive)** pairs; §1 both-sides coverage across the union. §5/§11 item 4: coding IRR **κ ≥ 0.75** reported + **alternative-coding sensitivity analysis** (second independent scheme; headline must survive both). Stamp `(D-23)`.
- **07-tongues — D-24 (major).** §2/§3: single localization pipeline split into **two arms** — Arm 1 translation-only battery (feeds MI ladder), Arm 2 cultural-localization DIF/robustness study (never enters MI ladder). §5: added measurement model — **item parcels (3–4 items/parcel), multi-group ordinal factor models on parcels**, pre-registered spec; Arm 2 reported separately. §11 item 2 renamed `localization_pipeline.md` → `two_arm_pipeline.md`. Stamp `(D-24)`.
- **08-loadbear — D-25.** §2 L1 + §11 item 2: **fixed shared pre-generated corpus** = primary L1 filler (cross-model comparability); self-generated filler → secondary realism arm. §7: added **(f) probe-compression concordance gate** (compressed probe vs. full source item r ≥ 0.6 per clause before load results interpreted; failing clauses re-compressed). Stamp `(D-25)`.
- **09-crucible — D-26 + ALL-TEN(CO-6b).** §7: added **equating-precision pre-gate** (simulation must show cross-release equating SE small vs. 1-SD trajectory effects; else enlarge/redesign anchors before R1) and appended CO-6b to the `≥8 clauses` gate. §11 item 1: added **funding/capacity risk register** (standing curation = single point of failure; min capacity/cycle + auto release-size reduction; flag resourcing to Jimmy before R2). Stamp `(D-26; CO-6b)`.
- **10-facetoface — D-27.** §5: self-serving asymmetry now **salience-matched** (log length/turn count/recency/artifact footprint; matching audit = Phase-B deliverable; neutral-incident retrieval partial likewise matched). §2/§5/§11 item 5: Phase-C repair delta → **yoked-control design** (insight effect = self-selected improvement − examiner-selected-matched-score improvement; explicit regression-to-mean estimator). Stamp `(D-27)`.

## Discrepancies logged

- **ALL-TEN family-gate wording is a no-op on 7 of 10 briefs (by design, not a miss).** The instruction says "wherever a §7 gate demands separation *on ≥8 clauses* or 16-clause distinctness, ADD …". That trigger phrase exists only in **01, 02, 09**; those three received the CO-6b parenthetical. Briefs **03/04/05/06/07/08/10** use different §7 separation criteria (hypocrisy indices, officiousness–passivity 2×2, multivariate strategy/weight vectors, values-drift, failure-order Kendall's W, asymmetry scores) with no `≥8 clauses`/16-clause-distinctness phrasing, so there was nothing to relax — no edit made, CO-6b not cited in their stamps. Flagging rather than improvising a family-gate insert into gates that don't use clause-count separation.
- No other described target text was missing; all D-18…D-27 targets located and edited. No registry edits attempted (frozen).

## Verification-grep output (§0.6, scoped to CORINTHLOVE-v3/)

- `status: gate-revised 2026-07-05` in DESIGNS/*.md → **10/10** (D-18…D-27 mapped 01…10; CO-6b on 01/02/09 only). PASS.
- Forbidden `icmi-proceedings` / `moral compactness` in DESIGNS/ → **0**. (Only hits are the do-not-cite BAN warnings in `00-…portfolio.md` and `98-…guide.md`, which are permitted — not edited by this session.) PASS.
- Removed-pattern `tagged/untagged` (+ hyphen/`untagged` variants) in v3-02 → **0** (converted to salience-gradient throughout, incl. the two grep-caught residuals in §6.1 counter and §11 analysis estimator). PASS.
- Latin-square-as-primary in v3-03 → **0**; all 4 remaining "Latin-square" mentions explicitly scoped to the cross-model calibration layer. PASS.
- Single-arm `localization_pipeline` in v3-07 → **0** (renamed `two_arm_pipeline.md`; Arm 2 localization explicitly outside the MI ladder). PASS.
- YAML seed blocks (all 10 fenced ```yaml``` seeds) parse under `yaml.safe_load` → **ALL PASS**.

## Next step (per instructions §4.5 + memory)

1. **STATUSGAME focused re-review** — v1-03 only, after its D-03 revision (verify rivalry delta isolates framing, not incentive). Single Opus reviewer. (Not this session's scope — v1.)
2. **Bank builds (Opus, one/session), cross-version order CO-8:** ① v2-09 DIMGLASS → ② v1-07 CHARITROC → ③ v3-01 CROSSROADS → ④ v3-05 AGAPEGAME *or* v3-04 WITNESS → ⑤ v3-03 MANYMIRRORS (gated on 2-method concordance from ③–④). **DIMGLASS first.** Each build follows the relevant 98 guide + the brief's §11.
3. Do NOT commit/push (parallel v2 session shares the git index); orchestrator handles git + memory.
