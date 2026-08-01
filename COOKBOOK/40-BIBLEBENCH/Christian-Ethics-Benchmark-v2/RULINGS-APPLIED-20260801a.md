# RULINGS APPLIED — 2026-08-01a: v4-C report §8 menu items 1–3 RATIFIED · d02 hardened re-pilot AUTHORIZED ($2.00, new session)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-08-01 · **Spend ceiling authorized: $2.00 (d02 re-pilot only; v4-A is $0).**
**Predecessor:** `RULINGS-APPLIED-20260731n.md` — its RULING 4 (v4-C) was executed and
CLOSED at $7.509 of $30.00; see report `20260731o-v4c-execution-report.md`. Nothing
of the v4-C ceiling carries forward.
**Subject:** owner ratification of the `20260731o` §8 next-ruling menu, items 1–4
(item 5, the B1+B2 scale, REMAINS OPEN), recorded from an interactive owner
decision, 2026-08-01.

---

## RULING 1 — v4-A AUTHORIZED ($0: no model calls, no piloting)

Menu item 1 ratified. Scope, per spec `20260731j` §7 v4-A row as informed by report
§4.3 and §6:

1. **Authoring:** §2.2 hardened-allocation expansion (~30 items; retire or harden
   WW-05-H01 / WW-05-M01); P-FAITHFULNESS (d03) REBUILD to n ≥ 16 and P-MOTIVE
   (d04) REBUILD to n = 40 under the §2.3 judged-item rules; admitted-axis
   expansion for **d08 (P-GUARDRAIL) and d10 (P-DESERVINGNESS) only — d06
   (P-PROCESS) is DEFERRED** pending harder items and the parse hardening below
   (report §4.3). Every new/rebuilt dimension reserves ~20 pct holdout fractions,
   quarantined at creation. Rejected items recorded, never deleted. Canary on every
   public bank line.
2. **Code deliverables, with tests:** (a) judge-B parse hardening
   (retry-on-parse-failure in the rescore tool; target complete-case retention at
   or above 85 pct everywhere — report §6.1); (b) **empty-completion exclusion,
   both halves** (scorers route empty/truncated completions to unscorable;
   administration stops losing answers to reasoning-budget exhaustion — report
   §6.2); (c) ranked-sacrifice scorer per §2.2 with independent double-keying;
   (d) the complete-case analysis upgrade and norming/reporting module (§3).
3. **Anchored q2 definition** for the d07 rubric (see RULING 2) is a v4-A authoring
   deliverable: written exemplar anchors for what counts as
   affirming/encouraging/blessing continuation.
4. Instrument discipline: `WW-v2-20260731b` and its verify chain stay intact; v4-A
   work builds the v4.0 instrument line per spec §5.1 (new instrument id at freeze;
   superseded stamps preserved). Any change that would break
   `tools/verify_instrument.py` on the stamped tree needs its own ruling first.
5. B1 remains separately ruled and must NOT launch before deliverables 2(a) and
   2(b) land (report §7 prerequisite finding).

## RULING 2 — d07 (P-COUNSEL) exits HOLD as REBUILD candidate, conditionally

Menu item 2 ratified as recommended in report §2: the v3 floor is recorded as
substantially a read-out artifact; the determinate three-question rubric restores
measurability (agreement 0.735, retention 98.8 pct, item-level r 0.66,
contrast-sign 9 of 10). The condition binds: **no d07 authoring proceeds past
candidate drafting until the anchored q2_endorses definition exists** (RULING 1.3),
and the rubric supports ordering-level reads only until q2 determinacy is
demonstrated at B1.

## RULING 3 — P-COMMITMENT recorded NOT ADVANCED

Menu item 3 ratified: the fact_presence read-out failed its construct micro-probe
(degenerate at both strata ends; three construct defects; report §5). P-COMMITMENT
leaves the v4.1 candidate list. Any revival requires artifact-production gating,
entailment-aware fact checks or state-the-number keying, truncation exclusion,
frontier-banded items — and a new ruling. The WW-03-L02 zero-floor stands recorded
as real model behavior.

## RULING 4 — d02 hardened BT re-pilot AUTHORIZED: $2.00 hard, NEW SESSION

Menu item 4 ratified with execution assigned to a fresh session via boot prompt
`20260801b-boot-prompt-d02-repilot-v4a-open.md`, which carries the full design.
Summary of what is authorized:

- Same stored final-turn responses as the first pilot (7 in-band items × 3 epochs ×
  6 frontier pairs × 2 orderings × 2 judges; the 3 empty gemini25pro cells stay
  excluded). ZERO SUT calls.
- Hardened judge protocol (the two confounds of report §3, addressed): explicit
  tie-eligibility anchor, explicit position-irrelevance instruction, and
  per-response structured verdicts before the comparison (strict JSON with
  r1/r2 holds-the-line reads plus the final verdict).
- **Ceiling: $2.00 hard** (first pilot cost $0.166; richer output roughly triples
  completion volume; margin well above 2×). Calibration micro-run first, projection
  against the ceiling, stop-and-report on breach. Same tooling lineage
  (`tools/audit/d02_davidson_bt_pilot.py` extended with a prompt-variant flag), new
  log root `logs/d02-btpilot2-20260801/`.
- Read-outs and pre-committed comparison criteria are in the boot prompt §4; all
  numbers remain pilot diagnostics — never WALKWORTHY numbers. The P-PRESSURE
  v4.0-scope decision returns to the owner with both pilots in hand.

## Standing

Item 5 of the report §8 menu (B1+B2 scale, ~$180–230) REMAINS OPEN; per `-n`
RULING 3 it returns to the owner — now with report §7 available, and naturally
after RULING 1's prerequisites and RULING 4's result exist. Newest-ruling-wins:
this file wins over `20260731m` and `20260731o` §8's "nothing here is authorized"
status line. Entry point for the next session: `20260801b`.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
