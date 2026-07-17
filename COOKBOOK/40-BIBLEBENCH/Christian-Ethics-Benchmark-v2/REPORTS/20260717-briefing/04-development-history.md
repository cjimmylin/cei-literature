# WALKWORTHY v2 — Development History on Inspect AI

**Report 4 of 6 — internal owner briefing**
**Date:** 2026-07-17
**Status:** INTERNAL BRIEFING — not release evidence; v1 remains canonical (owner ruling `20260716-owner-ruling-v2-parallel.md`). Descriptive instrument narrative only.
**Canary:** WALKWORTHY-CANARY-7f3e2026

---

This report is the consolidated lab-notebook account of how the WALKWORTHY Christian-ethics benchmark was ported to Inspect AI as a parallel v2 harness over three working days (2026-07-15 through 2026-07-17). It is written for the owner reviewing scale-up readiness: what was built, what broke, what was fixed, and what was ruled, in the order it happened. The through-line is deliberately unflattering where it should be — the bug stories (the design-04 `abs()` metric inversion, the design-05 allocation field-path bug, the F8 vacuous-`ok` parser defect, the PRELIM-FAIL parity check) are given their space precisely because each one was caught *inside* the verification loop, before any number reached a claim. That the loop keeps catching things is the readiness argument.

Terminology note: throughout, an *administration* (or *admin*) is one seat / twin / motive arm / scripted conversation; a v1 *item* expands to one or more administrations in v2. "SUT" is the system-under-test; "judge-A" is `gpt-4.1-nano` and "judge-B" is `llama-3.3-70b-instruct` unless stated otherwise. The 10 designs are numbered 01–10; the corpus-distinctive slice is 04/05/10 (marked ◆ in the pilot).

---

## 1. Origin and design intent

WALKWORTHY v1 is a custom Python harness (`../Christian-Ethics-Benchmark/`) that had already produced release-grade evidence: a frozen O4 run manifest, a G4 label pass, and a gate battery. The v1 harness worked, but it was operationally heavy — roughly 32 modules plus 66 test files, a bespoke checkpoint/resume/panel runner (`panel.py`), per-vendor adapter code, and a mock dry-run driver. One v1 incident (PR-9 transcript loss) had cost a $27 re-execution of designs 02 and 07 because the harness did not persist every message of every sample.

The v2 question was narrow: does the Inspect AI framework fit WALKWORTHY well enough to be worth running as a *second* execution path? The `20260715-inspect-fit-assessment.md` memo answered "well." Inspect covered natively almost everything that made v1 painful: `.eval` logs persist every message automatically (including the 17-message design-02 ladders); retry/resume and `--max-connections` are built in; OpenRouter is a provider string plus one env var; a second cross-family judge costs only judge-tokens via `inspect score` over saved transcripts, with no SUT re-execution. The custom surface shrank to 8 package modules + 11 task files + 2 tools. Critically, the *measurement-defining intellectual assets* transferred verbatim — item banks, rubrics, refusal taxonomy, and the design-05 constraint-satisfaction (CSR) comparator (`ordo_constraints.py`, vendored unchanged). Nothing in the v1 design proved inexpressible on Inspect.

The port was built under a strict discipline: **v1 is read-only.** Every v2 artifact records "v1 folder untouched"; v1 sources are imported read-only for parity comparisons and never modified. The fit memo recommended v2 as a candidate for canonical status, contingent on two preconditions (judge-path replay parity; end-to-end 2-judge validation). That recommendation was **considered and explicitly not adopted.** On 2026-07-16 the owner ruled, verbatim:

> "we want to make v2 in parallel with v1 and allow for comparing in the future — so don't make v2 as canonical but as parallel."

The effect (recorded in `20260716-owner-ruling-v2-parallel.md`): v2 is a *parallel comparison instrument* indefinitely; v1 remains the canonical execution path for release-grade evidence; future v1↔v2 cross-harness comparisons are an intended use. Every downstream v2 report carries that scope in its table footers. This ruling is why nothing in the v2 line — however clean — is release evidence.

---

## 2. Day one — 2026-07-15: conversion, blind review, and the comparability preconditions

Day one was the bulk of the build: bank conversion, a ten-agent adversarial review, and the two comparability runs the fit memo had named as preconditions.

**Bank conversion and the PRELIM-FAIL loop.** The v1 markdown banks were converted to JSONL (one line per administration) and checked for parity against the v1 O4 manifest at the item level. The first parity check *failed*. The superseded report — preserved, not deleted, at `RECYCLE-BIN/20260715-conversion-parity-report.PRELIM-FAIL.md` — carries `Overall: FAIL ❌` with the diagnostic ID-uniqueness check reading **4 duplicate ids** across the public+holdout surface. That failure was fixed, and the re-run report (`20260715-conversion-parity-report.md`) records the clean state: **344 runnable public items, exact per-design match to the O4 manifest** (01=49, 02=36, 03=33, 04=33, 05=32, 06=31, 07=27, 08=33, 09=34, 10=36); 835 unique IDs across public+holdout with **0 duplicates**; and the canary `WALKWORTHY-CANARY-7f3e2026` present in **835/835 lines (100%)**. The 11 non-runnable public items are sketch exemplars from the `*-SPEC` files (02/07/09) with no materializable model input; the run surface excludes them. The PRELIM-FAIL artifact is worth keeping visible: the verify-then-trust loop fired on the very first parity gate, and the preserved failure is the receipt.

**Ten-agent blind adversarial item review.** Ten parallel Opus agents (one per design) reviewed the converted banks blind and applied fixes to the v2 bank copies only. The ledger (`RULINGS-APPLIED.md`, per-design memos `REVIEWS/20260715-NN-*-v2review.md`, consolidated diff `REVIEWS/20260715-consolidated-diff.md`) records the totals: **510 items reviewed, 105 stamped fixed, 0 killed.** Every item now carries `review_status: reviewed-clean | reviewed-fixed | killed`; zero item IDs changed; canary preserved everywhere. The owner ratified all 105 fixes after reviewing the consolidated diff ("I have reviewed and authorized"). Two fixes are worth naming because they were latent measurement-breakers: design-05's parser-breaking accented allocation tokens (`é` → ASCII on A03/M04) would have mechanically zeroed CSR on those items; and design-07 received per-item `comfort_only`↔`faithful_counsel` discriminators on all items — a direct remedy for v1's 17.6% judge-agreement floor on that design.

**Post-review re-parity.** Because the 105 fixes touched bank content, parity was re-checked on the post-review datasets (`20260715b-conversion-parity-report-postreview.md`) — same PASS, same 344 exact match, same 835/835 canary. Re-checking after a content mutation rather than trusting the pre-review pass is the pattern the whole line follows.

**Live smoke.** With banks clean, a 10-design live smoke ran on real datasets: SUT `deepseek-chat` × judge `gpt-4.1-mini`, `--limit 2` per design (`20260715-live-smoke-report.md`). Result: **10/10 designs status=success, judge JSON parseable on every scored sample, zero provider failures, zero 402s, ≈$0.038 total** (against a <$1 target and $5 ceiling). The smoke also surfaced two things the team chose to document rather than paper over: the design-05 SUT emitted prose without the required strict `allocation: {}` block (format non-compliance = measurement signal, not a harness error — the CSR machinery itself verified correct on synthetic compliant answers at 0.5/0.8/1.0), and a *latent* parser edge in `parsers.py::reparse_allocation_response` that logged `allocation_ok=True/values={}` on a block-less answer. That parser edge was flagged here and did not get its full fix until F8 on day two — an honest carry-forward, not a silent one.

**Precondition #1 — judge-path replay parity.** The first fit-memo precondition asks whether v2's scorers reproduce v1's judge verdicts when the SUT response and judge model are held *fixed*. The replay harness (`20260715c-comparability-judgepath-report.md`, actual cost ≈$0.01) injected v1's stored SUT responses into v2's exact production scorer path (`_make_model_graded_scorer`, `assemble_rubric_prompt`, `parse_judge_json`) and re-judged with v1's judge-A slug (`gpt-4.1-nano`), no SUT call. Pooled field-cell exact agreement: **v2-scorer vs v1-judge-A = 73.2% (123/168)**, against the **v1-judge-A vs v1-judge-B natural baseline of 59.2% (100/169)** — v2 agrees with v1's judge-A *more* than v1's two judges agreed with each other (+14 pp). On 21 of 24 field×design cells, v2-vs-v1jA met or exceeded the v1 inter-judge baseline; the most diagnostic cell was design-09 `owes_direction`, where v2 reproduced judge-A perfectly (κ=1.00) while the two v1 judges agreed on only 1/3 of seats. The reading: residual disagreement is judge stochasticity, not a v2 prompt-assembly or parse defect. Designs 02 and 07 were *excluded* from this replay (v1 scored them per-turn; v2's model-graded scorer at that point read only the final completion) — an exclusion documented rather than force-aligned.

**Precondition #2 — end-to-end + 2-judge re-score.** The second precondition ran the 60-item MVP-A1 slice end-to-end on the post-review banks and validated the judge-B re-score path (`20260715d-e2e-and-two-judge-report.md`, actual spend ≈$0.056 against a $1 ceiling). All 60 MVP items resolved to 100 runnable administrations; all 10 designs completed `status=success`. This run also recorded a real Inspect friction point honestly: the `inspect score` CLI re-score path *did not work* for these custom scorers — two independent structural blockers (package-relative import breakage, and non-unique registry names because all 9 model-graded designs shared the `_factory` registry name). The sanctioned path became a custom script (`tools/rescore/rescore.py`) that imports the package properly so prompt assembly is byte-identical; the CLI blocker itself was queued for a real fix (delivered as polish item 3 on day two). The v2 judge-A/judge-B agreement per design landed in the same band as the v1 mistral baseline — high where v1 was high (design-01 0.75↔0.75), low where v1 was low (design-02 ~0.18↔0.20) — reproducing the v1 2-judge protocol's *behavior*, not just its plumbing. 76 of 242 cells flagged `needs_adjudication`, concentrated in design-09 (per-seat categoricals) and the multi-option designs.

**Methods docs.** Day one closed with the methods write-up (`METHODS/` — academic methods, operational methods, and an Inspect handoff).

---

## 3. Day two — 2026-07-16: the parallel ruling, polish, the benchmark critique, and the F-ledger

Day two spanned several sessions and did the heavy analytic work. It opened with the owner's parallel-not-canonical ruling (§1 above), which reframed everything that followed as *instrument diagnostics on a parallel harness*, never as evidence.

**Polish items.** In the same ruling the owner authorized three polish items ("please improve v2 with these polish items"), implemented in `20260716-polish-items-report.md` (live micro-check ≈$0.013 against a $0.15 ceiling):
- *Per-turn scoring for 02/07*: the ladder solver now records `{index, user_text, branch_state, response}` per turn, and a per-turn scorer judges each turn's response independently against the design rubric — restoring v1 fidelity (`break_turn`, `arc_shape` metrics reimplemented with v1 formulas verbatim). This closed the very gap that had forced 02/07 out of the day-one replay.
- *Metric-aggregation audit*: three real bugs surfaced. Design-03 `say_do_gap` had been reading *both* categories off *one* administration, structurally forcing the gap to 0 — fixed to pair `expressed_judgment` off the SAY admin and `revealed_artifact` off the DO admin. Design-08 `covert_overt_gap` returned `NaN` because exemplar admin variants polluted the covert/overt pairing — fixed by a universal exemplar-exclusion pass that runs before any grouping. The design-01 "0.00 obedience" figure turned out to be a *stale reporting error* in a stored log, not a code bug — the current metric recomputes 0.80 over the same stored scores; the honest empirical audit (an offline recompute over the e2e log) is written into the report rather than assumed.
- *Scorer registry naming*: the `_factory` name collision was fixed with 10 explicitly named `@scorer(name="designNN_scorer")` factories plus an editable-installable package, so native `inspect score` now resolves each design uniquely (verified live).

**The five-lens benchmark critique and its must-fixes.** A five-lens adversarial critique (statistical design, judge validity/gaming, ops readiness, construct validity, contested-tier fairness — `REVIEWS/20260716-critique-*.md`) was adjudicated (`REVIEWS/20260716-adjudication-benchmark-critique.md`), producing four code MUST-FIX items implemented in `20260716-adjudication-fixes-report.md` (zero live spend, mock + offline only):
- **M1 — the design-04 `abs()` port bug (the marquee catch).** v2 0.2.0 had reported `motive_sensitivity_index = mean(abs(alpha − beta))`. But v1 uses a *signed* delta and a keyed-directional correctness statistic — and **12 of 54 paired public admins are zero-keyed** (`keyed_motive.direction == "zero"`), for which `abs()` *inverts the key*: a model that correctly treated both motives alike scored as insensitive, and a motive-perverse model scored as sensitive. The fix restored v1's signed `motive_delta_mean` and `motive_correct_rate` (v1 `_04_correct` verbatim), retaining the abs index only as a labeled legacy companion. This bug was load-bearing on live data (§4): in the pilot, llama had the largest raw delta but the *lowest* keyed-correct rate — the retired abs headline would have crowned it "most motive-sensitive" for what was actually undirected motive reactivity.
- **M2** added Wilson 95% intervals and per-stratum (a / quarantined-c) recompute cells. **M3** added ladder branch-source provenance (`classifier` vs `heuristic`) so a classifier misroute is no longer indistinguishable from a confident call. **M4** added design-05 coverage denominators (`n_total` vs decidable `n`) and an evidence-derived non-compliance flag, routing around the unreliable raw `non_compliant` flag (the OR-7 parser edge — see F8).

**Design-07 state anchors.** Before the paid pilot, the owner ruled that the design-07 matched-quality reference-answer residual be closed first (`20260716-design07-reference-anchors-report.md`). Neither v1 nor v2 had ever built this (v1 had reference files for designs 06 and 09 only); the harness-side matched-quality state anchors were authored so they sat in every design-07 per-turn judge prompt.

**The full 5-SUT pilot.** The pilot (`20260716-pilot-design.md`, `20260716-pilot-report.md`) ran the full 575-admin scope × 5 SUTs (deepseek-chat, mistral-small, gemini-flash-lite, llama-3.3-70b, gpt-4.1-mini) as two sequential halves with a go/no-go checkpoint: **50/50 eval runs success**, zero 402s, **$2.73 exact SUT+judge-A + ≈$0.90 judge-B ≈ $3.63 total** against the authorized ≈$7.90 envelope (the cost model was ≈2× conservative). Two outputs matter for readiness:
- **The judge-swap finding (pre-committed rule R4).** Under the judge-B re-score, **all 9 comparable designs flip their naive SUT point-estimate ordering.** Per-design judge-A/judge-B exact agreement ranges from 0.21–0.26 (design-02 per-turn) to 0.67–0.87 (design-05). The pre-committed consequence: **the pilot supports NO SUT-vs-SUT ordering claim on any design** — every cell is an instrument reading with a judge-noise band. This is the pilot's most decision-relevant result: any future v2 measurement run must budget the 2-judge pass as a first-class component.
- **The design-05 alloc-spec bug — found, fixed, recovered.** The converter emitted the allocation spec at `keyed.extras.allocation`, but `design05_scorer` (and `rescore.py`) read top-level `keyed.allocation` — empty on 32/32 public items. *Every* previously observed all-`nan` CSR cell (in the e2e run and the pilot's stored scores alike) was this bug, not model behavior. Because CSR is judge-free, the true cells were recovered offline at zero re-run cost (`recompute_design05_csr.py`, csr_mean 0.84–0.94); both readers now fall back to `keyed.extras.allocation`. Design-07 was confirmed *floor-saturated* (all SUTs arc_pass 0.0, 0 exclusions — a real floor, not an artifact), and the branch classifier never fell back to the lexical heuristic (287/287 branched turns × 5 SUTs classifier-routed).

**The F-ledger wave.** With the pilot's diagnostics in hand, a sequence of pre-registered "F" experiments discharged the open instrument questions (sessions 5–7, each behind an explicit spend GO). Rather than narrate all eleven inline, the discharge status is tabulated in §5; the substantive findings were: F1 divergence tags **RATIFIED** (29 yes / 129 partial / 186 no); F9 solver-level format retry drove design-05 non-compliance from 79%/46% → **0%** on both SUTs; F2 anchor ablations showed anchors are a *small, judge-asymmetric* perturbation (≈5 points of the ~26-point 07-vs-02 agreement gap — the rest is the design-07 instrument itself); cross-harness Option A found no harness effect beyond the judge effect at this n; F5 certified all three judge candidates G5-neutral on designs 06/09; F3 found the classifier `nano` is the **cross-family outlier** — the two alternative families agree with each other at 0.902 but with nano at only ~0.70, disagreeing with nano on **24.4% of branch turns** (hardening F11's no-cross-classifier-pooling clause); F7 found prior-turn context moves **27% of judge-A / 11% of judge-B** turn verdicts but does not close the judge gap; F8 fixed the vacuous-`ok` parser defect (below); and F11 pre-registered comparisons were **RATIFIED** (C1 m=30, C2 m=70, C9 first-use rule) via the session-7 decision grid.

**F8 — the vacuous-`ok` parser fix.** The parser edge flagged in the day-one smoke got its source-level fix in `20260716-f8-parser-fix-note.md`. `reparse_allocation_response` returned `ok=True, non_compliant=False` on a block-less prose answer whenever the allocation spec was *degenerate* (`tokens=[]`, `budget<=0`): with no tokens, `all(candidates.values())` is vacuously True and `budget<=0` forces `sum_ok=True` — two degenerate-truth idioms composing into a false "compliant" flag. The fix requires a non-empty token spec for `ok` in both validators; the post-fix invariant is `ok=True ⇒ every required token has a parsed value`. A hard equivalence gate confirmed the recompute over both the pilot and F9 log sets was **byte-identical** pre/post fix (expected — with real token specs the vacuous path is unreachable), and an 8-test regression was added. v1 carries the identical edge and stays untouched; this is the one deliberate, documented v2 divergence from the verbatim port.

---

## 4. Day three — 2026-07-17: the Sol referee arm

The judge-referee (JR) meta-audit — a *non-benchmark* exercise that adds nothing to the instrument and changes no judge pins — began on day two with an Opus referee arm and completed on day three with a second, independent referee.

The framing guardrail is carried verbatim in every JR artifact and is worth restating: "closer to a referee" means *reference-model concordance, not ground truth*; a stronger model is not an oracle, and where a referee sides with one judge that is evidence about *judge character*, not correctness. The sample was frozen before any dispatch (`20260716-jr-sampling-precommit.md`, manifest sha `b2839b14…f5ef9f`, n=942, disagreement-enriched).

The **Opus** arm (`20260716-opus-referee-results.md`) ingested 942/942 blind verdicts via OAuth-channel Claude Code agents at **$0 API spend**, 0 hash rejects, 0 refusals. The **Sol** arm on day three (`20260717-sol-referee-results.md`) ran the same frozen 942-unit manifest through GPT-5.6-Sol via `codex exec` — again **$0 API spend**, and notably **all 39 batch dispatches complete and valid on the first pass** (0 re-asks, 0 hash rejects). The four-way findings:
- **Design 02 — REVISED.** The two referees agree with each *other* (Sol↔Opus 0.735 on the disagreement stratum) far more than with either shipped judge (0.23–0.27), and both referees land on the same neither-state on **83/200 units (41.5%)**. Arm 1 alone could not distinguish "taxonomy genuinely ambiguous" from "both shipped judges weak"; arm 2 shows it is substantially the latter — both shipped judges diverge from a strong-model consensus in different directions.
- **Design 07 — CORROBORATED.** Sol independently reproduces the Opus verdict: sides with judge-B 0.605 vs judge-A 0.138 (0.770 vs 0.146 excluding unscorable-affected items). Two independent stronger-model references now agree that on design-07, `gpt-4.1-nano` under-calls `full_validation` — a judge-A *character* finding, dual-confirmed.
- **Design 06 — SPLIT.** Sol does **not** replicate Opus's strict `principles` reading (Sol−Opus on `principles` = +0.40/+0.41); Opus's stricter design-06 principles scoring looks Opus-specific rather than a shared reference judgment.
- **Defect items — DUAL-CONFIRMED.** The named design-07 defect items surface in both referee arms.

None of this enters a benchmark report or moves an instrument; it is meta-evidence about the shipped judges, produced at zero API cost.

---

## 5. F-ledger summary

Each F-item is a pre-registered instrument question, discharged behind an explicit spend gate. Status as of 2026-07-17.

| # | Source finding | What was done | Status | Discharging artifact |
|---|---|---|---|---|
| F1 | Divergence between "says right" and "does right" needs an operative construct | Divergence-tag sidecar built and ratified: 344 items = 29 yes / 129 partial / 186 no | **RATIFIED** | `20260716-owner-ruling-f1-and-spend-go.md`; `20260716-divergence-split-addendum.md` |
| F2 | Are the design-07 anchors (and keyed anchors generally) driving the judge-agreement story? | 3-arm ablation: 07-anchors-off (2a), answer-blind (2b), 02-anchors-on (2c) | **DISCHARGED** — anchors ≈5pt of the 07-vs-02 gap; anchor-dependence judge-asymmetric; gap is an instrument property | `20260716-f2-ablations-report.md`; `20260716-f2-2c-results.md` |
| F3 | Is the nano branch classifier idiosyncratic? | Re-classify 1,435 stored 02/07 branched turns with two alt families | **DISCHARGED** — alt-alt 0.902 vs alt-nano ~0.70; nano is the outlier on 24.4% of turns; no cross-classifier pooling | `20260716-f3-crossfamily-classifier-results.md`; `20260716-f3-classifier-sensitivity-report.md` |
| F4 | Refusal-taxonomy `engaged` override was dead code | Option B: derive `engaged`, report 4-way taxonomy as descriptive adjacent table, hard equivalence gate on primaries | **CLOSED at rung B** | `20260716-f4-optionB-engaged-derivation.md` |
| F5 | Judges 06/09 not G5-neutrality-certified in v2 | Port-equivalent G5 certification (40/40 vs v1) on 06/09 for all three candidates | **CERTIFIED** — nano, llama-3.3-70b, gpt-4.1-mini all pass both designs | `20260716-f5-certification-results.md`; `20260716-f5-judge-certify-port.md` |
| F6 | Both-poles-decline (DSP) policy | Not reached; coupled to F4 Option C, design-memo-first if ever activated | **OPEN (deferred)** | `20260716-owner-rulings-s7-decision-grid.md` |
| F7 | Design-07 per-turn judging may be order-blind (R11 flag) | Re-judge stored 07 turns with prior-turn context, both judges | **DISCHARGED** — context moves 27% of judge-A / 11% of judge-B verdicts but does NOT close the A/B gap | `20260716-f7-context-judging-results.md`; `20260716-f7-offline-assembly-report.md` |
| F8 | Vacuous-`ok` parser defect on degenerate allocation spec (OR-7) | Source-level fix requiring non-empty token spec for `ok`; byte-identical equivalence gate; 8-test regression | **FIXED** | `20260716-f8-parser-fix-note.md` |
| F9 | Design-05 format non-compliance (46–79%) blocks CSR coverage | Solver-level `_FORMAT_REMINDER` one-retry, live-validated on best/worst SUT | **VALIDATED** — non-compliance 79%/46% → 0%; CSR stable on widened coverage | `20260716-f9-microcheck-report.md` |
| F10 | SD-7(c) — decode-stability question on design 10 | Optional k=3 seed decode-stability probe, offered to the owner as a pilot add-on (+≈$1); adjudication recommendation: skip at pilot, note for v-next | **OPEN** — never fired; activation requires owner scoping + a new spend memo | `REVIEWS/20260716-adjudication-benchmark-critique.md` (F-ledger row F10 + recommendation §3) |
| F11 | No pre-registered comparison scaffold for future comparative claims | Comparison families + multiplicity frozen: C1 m=30, C2 m=70, C9 first-use rule | **RATIFIED** | `20260716-prereg-comparisons-RATIFIED.md`; `20260716-owner-rulings-s7-decision-grid.md` |

> Note on F10: no `f10`-named artifact exists in the vault because the item never fired — the adjudication ledger defines F10 as the optional k=3 seed decode-stability probe on design 10 (source finding SD-7(c)), offered as a pilot add-on and recommended skipped at pilot scale. It remains the only F-ledger item that is both scoped and entirely unexecuted. F6 (DSP) is likewise carried open rather than discharged.

---

## 6. Spend and governance

Every paid run in the v2 line was authorized ahead of compute, ran under a hard NTE ceiling, and reported exact-or-estimated actuals against that ceiling. Cumulative live spend across the entire three-day build is well under $10; the two referee arms — the most compute-heavy exercises by token count — cost **$0 in API spend** by running on subscription/OAuth channels.

| Authorized run | Ceiling | Actual | Authorization / gate |
|---|---|---|---|
| Live smoke (10 designs, deepseek × gpt-4.1-mini) | <$1 (hard $5) | **$0.038** | AGENTS §4 live-smoke authorization |
| Judge-path replay (precondition #1) | $0.50 | **≈$0.01** (upper bound $0.0134) | owner-ratified comparability slice |
| E2e + 2-judge re-score (precondition #2) | $1.00 | **≈$0.056** | owner-ratified comparability slice |
| Polish-item live micro-check | $0.15 | **≈$0.013** | polish authorization (parallel ruling) |
| Full 5-SUT pilot | ≈$7.90 envelope | **$3.63** ($2.73 exact + ≈$0.90 judge-B est.) | pilot STOP-gate ruling, scope (c) |
| Session-5 GO (F9 + F2-2a/2b + cross-harness) | $2.45 (sum of item ceilings) | **~$0.9–1.5** | `20260716-owner-ruling-f1-and-spend-go.md` ("yes f1 ratify and go to spend") |
| Session-6 GO (F5 certification + F3 classifier) | $1.15 | **~$0.30** | `20260716-spend-memo-f5-f3.md` GO ("ok to spend") |
| Session-7 GO (F7 context + F2-2c) | $5.50 (F7 $4.00 + F2-2c $1.50) | **~$1.05–2.01** | `20260716-spend-memo-f7.md` GO ("GO + also fire F2-2c") |
| G5 certification calls (within F5) | — | **≈$0.02–0.04** | folded into session-6 GO |
| JR meta-audit — Opus arm | — | **$0** API (≈4.4M subscription tokens) | `20260716-jr-sampling-precommit.md` (OAuth channel, non-benchmark) |
| JR meta-audit — Sol arm | — | **$0** API | `20260717-sol-referee-results.md` (`codex exec` subscription channel) |

The governance pattern is consistent and worth naming as the readiness feature it is:
- **Precommit-before-compute.** Spend memos, sampling manifests (the JR sha-frozen manifest), and cross-harness mappings are frozen and hashed *before* the first dispatch; re-asks reuse the frozen prompts only.
- **Explicit GO gates.** No paid call runs without a dated owner ruling; each session's GO is *closed* at session end with no rollover ("the session-6 GO is CLOSED … nothing rolls over").
- **Owner rulings as dated memos.** Every substantive decision — parallel-not-canonical, the 105-fix ratification, F1 ratification, the session-7 decision grid, F11 ratification — is a dated, immutable memo with the verbatim ruling quoted.
- **402-trap discipline.** Every call carries an explicit `max-tokens`; an availability probe (max_tokens=16) runs before any authorized run.

---

## 7. What the process caught

The single most important thing to carry into a scale-up decision is not any one number — it is that the layered review/pilot/meta-audit stack caught every one of the following *before* it could reach a public claim, and that the parallel-not-canonical ruling means none of these was ever release evidence in the first place:

- **105 item-level fixes** applied under the 10-agent blind adversarial review (510 reviewed, 0 killed) — including the design-05 accented-token parser breaker and the design-07 discriminator additions.
- **2 metric-semantics bugs** caught by the benchmark critique and metric audit: the design-04 `abs()` inversion (12/54 zero-keyed pairs mis-scored under the retired metric) and the design-03 `say_do_gap` structural-zero (both categories read off one administration).
- **1 parser defect** (F8 vacuous-`ok` on a degenerate allocation spec), flagged latent in the day-one smoke and fixed source-level with a byte-identical equivalence gate.
- **1 alloc-spec field-path bug** (design-05 `keyed.extras.allocation` vs `keyed.allocation`) that had silently zeroed *every* CSR cell across the e2e and pilot runs — recovered offline at zero re-run cost.
- **1 parity FAIL** (the PRELIM-FAIL, 4 duplicate ids) caught on the first conversion gate and preserved as a receipt.
- **3 design-07 defect items** independently surfaced and dual-confirmed across the Opus and Sol referee arms.
- **1 classifier outlier** (nano diverging from two independent families on 24.4% of branch turns), which hardened the no-cross-classifier-pooling rule rather than silently biasing 02/07 stimuli.
- **The judge-swap invariant**: the pilot's own finding that all 9 comparable designs flip naive ordering under a judge change, converted immediately into a pre-committed rule (R4) that forbids SUT-ordering claims absent a two-judge-stable direction.

Every item above was surfaced by the verification loop, not by a downstream consumer of a shipped number. That is the argument for the process, and it is the argument the owner should weigh when deciding how far to scale v2.

---

## Sources

All paths relative to `.../CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`.

- `20260715-inspect-fit-assessment.md` — Inspect-fit verdict; parallel-first framing
- `20260715-conversion-parity-report.md` — post-fix parity PASS (344 exact, 835/835 canary)
- `RECYCLE-BIN/20260715-conversion-parity-report.PRELIM-FAIL.md` — the preserved FAIL (4 duplicate ids)
- `RULINGS-APPLIED.md`; `REVIEWS/20260715-NN-*-v2review.md`; `REVIEWS/20260715-consolidated-diff.md` — 510 reviewed / 105 fixed / 0 killed
- `20260715b-conversion-parity-report-postreview.md` — post-review re-parity PASS
- `20260715-live-smoke-report.md` — 10/10 designs, $0.038, latent parser flag
- `20260715c-comparability-judgepath-report.md` — judge-path replay parity (73.2% vs 59.2%)
- `20260715d-e2e-and-two-judge-report.md` — e2e + 2-judge re-score (precondition #2)
- `METHODS/20260715-walkworthy-v2-inspect-*.md` — methods + handoff docs
- `20260716-owner-ruling-v2-parallel.md` — parallel-not-canonical ruling (quoted)
- `20260716-polish-items-report.md` — per-turn scoring, metric fixes, scorer registry
- `REVIEWS/20260716-critique-*.md`; `REVIEWS/20260716-adjudication-benchmark-critique.md`; `20260716-adjudication-fixes-report.md` — five-lens critique + M1–M4 (design-04 abs() fix)
- `20260716-design07-reference-anchors-report.md` — design-07 state anchors closed pre-pilot
- `20260716-pilot-design.md`; `20260716-pilot-report.md` — 5-SUT pilot (50/50, $3.63, judge-swap R4, design-05 alloc-spec bug)
- `20260716-owner-ruling-f1-and-spend-go.md`; `20260716-spend-memo-f9-f2-crossharness.md` — F1 ratification + session-5 GO
- `20260716-f9-microcheck-report.md` — F9 format retry (79%/46% → 0%)
- `20260716-f2-ablations-report.md`; `20260716-f2-2c-results.md` — F2 anchor ablations
- `20260716-crossharness-results.md`; `20260716-crossharness-design.md`; `20260716-crossharness-mapping-precommit.md` — cross-harness Option A
- `20260716-spend-memo-f5-f3.md`; `20260716-f5-certification-results.md`; `20260716-f5-judge-certify-port.md` — F5 G5 certification
- `20260716-f3-crossfamily-classifier-results.md`; `20260716-f3-classifier-sensitivity-report.md` — F3 nano outlier (24.4%; 0.902 alt-alt)
- `20260716-f4-optionB-engaged-derivation.md`; `20260716-f4-refusal-taxonomy-options.md` — F4 Option B
- `20260716-spend-memo-f7.md`; `20260716-f7-context-judging-results.md`; `20260716-f7-offline-assembly-report.md` — F7 context judging (27%/11%)
- `20260716-f8-parser-fix-note.md` — F8 vacuous-ok parser fix
- `20260716-prereg-comparisons-RATIFIED.md`; `20260716-prereg-comparisons-draft.md`; `20260716-owner-rulings-s7-decision-grid.md`; `20260716-design02-classifier-pin-decision.md` — F11 + session-7 grid
- `20260716-jr-sampling-precommit.md`; `20260716-opus-referee-results.md` — JR Opus arm (942/942, $0)
- `20260717-sol-referee-results.md` — JR Sol arm (942/942 first-pass, $0; 02 revised / 07 corroborated / 06 split / defects dual-confirmed)
