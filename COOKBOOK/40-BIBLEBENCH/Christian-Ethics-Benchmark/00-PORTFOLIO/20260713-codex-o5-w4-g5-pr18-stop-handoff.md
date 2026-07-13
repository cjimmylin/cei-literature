# WALKWORTHY — O5 W4 G5 Complete / W5 PR-18 Stop Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Scope:** WALKWORTHY only
**Status:** W4 complete; W5 stopped on PR-18; O5 remains blocked on labels for G4 and verdicts

## Outcome first

W4 G5 is complete in the new immutable run
`runs/20260713-o5-g5-neutrality/`. The production run made 92 explicit-judge calls,
recorded zero provider/parse errors, and cost **$0.0368785**.

- Design 06: OpenAI PASS; Google PASS.
- Design 09: OpenAI PASS; Google **DISQUALIFIED** after the single registered
  two-pole re-elicitation. The persistent split was `WW-09-E02`, category
  `reasoning_method_quality`.
- The both-judge STOP trigger did not fire.
- FR-8 now strikes Google design-09 verdicts. A replacement judge must first pass G4
  on design-09 Part-A labels, then fully rejudge design 09 and rerun G5. Labels are
  currently 0/439, so that cascade cannot yet proceed.

W5 did not begin. Five production mechanics were not registered by the frozen stack;
they are logged as **PR-18 — OPEN / W5 STOPPED ON JIMMY** in
`00-PORTFOLIO/PENDING-RULINGS.md`. No G7 live call was made and HOLDOUT was never
loaded.

## W4 implementation and custody

New mechanics:

- `harness/walkworthy/g5_neutrality.py`
- `harness/tests/test_g5_neutrality.py`
- public promoted-pair parsing support in
  `harness/walkworthy/g5_reference_lint.py`

The driver fails closed on the promoted 20-pair hashes/lint, uses only the explicit
frozen judges `openai/gpt-4.1-mini` and `google/gemini-2.5-flash`, persists a write-once
manifest plus append-only success/error ledgers, runs exactly one two-pole
re-elicitation for each initial violation, and derives persistent disqualification
without defaults. Completed-run custody validation rejects mutation or incomplete
event histories.

Production record:

- manifest: `runs/20260713-o5-g5-neutrality/g5_manifest.json`
- success ledger: `runs/20260713-o5-g5-neutrality/g5_events.jsonl`
- error ledger: `runs/20260713-o5-g5-neutrality/g5_error_events.jsonl` (empty)
- summary: `runs/20260713-o5-g5-neutrality/g5_summary.json`
- initial calls: 80
- initial violations: 6
- re-elicitation calls: 12
- persistent violations: 1
- prompt/completion tokens: 77,801 / 4,589

The focused G5 suite is 21/21 green. Two independent reviews passed after custody and
partial-run-status fixes. The final repository suite is **365/365 green** in 62.82s.

## Rulings and stops

PR-17 is RATIFIED/CLOSED with Jimmy's verbatim direction:

> Ratify paper claims review routed Opus memo → Jimmy per
> 20260712-codex-paper-fill-boot-prompt.md (master-plan §5 conditional; Fable window
> closed).

PR-18 asks Jimmy to register before W5 implementation or calls:

1. easy/hard stratum rounding and allocation;
2. the exact paraphrase surface and executable meaning-preservation/lint contract;
3. reduction of name-swap and paraphrase batteries to one G7 result;
4. role extraction plus a design-wide no-reuse name registry; and
5. unresolved original/perturbed-cell denominator and Part-B handling.

The observed candidate surfaces are 59 items under per-stratum floor (with zero easy
items for designs 04/06), 73 under nearest integer, and 75 under ceiling. Codex did not
choose among them.

## Paper-facing state and next trigger

The W4 result is a release-lane artifact; no release verdict or unlicensed manuscript
claim was added. Claude's concurrently completed, Jimmy-ratified MVP-PILOT strategy is
preserved as a separate exploratory paper lane in
`20260713-walkworthy-mvp-paper-strategy-amendment.md`.

The next prepared session is the dashboard §12 **MVP-PILOT roster + budget
authorization plan**: verify current cheap-model availability/prices, name exactly
three SUTs and two cross-family judges, calculate worst-case spend, and ask Jimmy for
separate paid-run authorization. That session is documentation/pricing research only;
it must not access credentials or make a paid call.

The O5 release lane resumes only when either:

- Jimmy rules PR-18, allowing mechanical W5 implementation; or
- filled label waves exist, allowing G4 and the design-09 FR-8 replacement cascade.

## Safety and repository custody

- No report was overwritten; this handoff and the W4 run are new dated artifacts.
- HOLDOUT was never loaded.
- No file was deleted.
- The dashboard passed HTML parsing and self-containment checks. The in-app browser
  rejected its direct `file://` URL under browser security policy; no workaround was
  attempted.
- Only explicit WALKWORTHY paths may be staged. Concurrent sibling-benchmark and
  portfolio-root edits remain outside this session's commit.
