# WCF-Bench Codex Session 39 Handoff — PPP-1 Runner Second-Cycle Gate

**Date:** 2026-07-13

**Executor:** Codex with fresh implementation/specification/quality agents

**Paper milestone:** PPP-1 exploratory manuscript preview

**Spend:** `$0`; no credential, metadata, or inference access occurred

## Outcome

Jimmy authorized the exact PPP-1 512-token branch, minimum offline runner seam, and one
paid execution under a strict `$23.56` maximum-retry NTE cap. The durable authorization
record is `20260713n-jimmy-ppp1-paid-authorization-record.md`. No paid attempt has started,
so the one-run authority remains unconsumed.

A fresh implementation agent built the minimal two-file runner:

- `04-HARNESS/ppp1_run.py`;
- `04-HARNESS/tests/test_ppp1_run.py`.

The frozen scope remains 226 runnable items × the exact three SUTs, with the sole Gemini
judge at `max_tokens=512`, SUTs at `max_tokens=2048`, and the mandatory
**EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE** label. No production
panel, scorer prompt, bank item, manifest of record, R-chain surface, T4 file, or existing
run directory changed.

## Review history and binding stop

The general specification review found four P1s: truthful cell completeness, exact resume
custody, sink-failure accounting, and direct real-guard/custody tests. The first bounded
fix cycle closed all four in commit `a914f5d4`; named-blocker specification re-review PASS.

The subsequent one allowed general quality review found one new P1:

> A `KeyboardInterrupt` during a paid call can bypass raw-evidence/checkpoint persistence,
> leaving no durable record of a potentially chargeable attempt and permitting resume to
> repeat it.

This is a result-validity, spend-containment, and immutable-custody blocker. Because it
appeared after the first fix cycle, `20260713-wcf-paper-first-execution-amendment.md`'s
second-cycle stop applies. Codex did not self-authorize another fix and did not begin the
paid run.

## Jimmy decision required

Choose one in chat:

1. **FIX — recommended:** authorize only the PPP-1 wrapper-local interruption-custody fix,
   one regression test, and named-blocker-only quality re-review. Preserve every existing
   roster, cap, prompt, scope, retry, and one-run boundary. After PASS, execute once and
   immediately build the paper packet.
2. **DISCLOSE-AND-RUN:** accept the possibility that an operator interrupt can make a
   chargeable attempt non-resumable/ambiguous; the safest implementation consequence would
   be no resume after such interruption and a PARTIAL stop. This carries avoidable custody
   risk and is not recommended.
3. **NARROW:** narrow the authorized study or claim. The reproduced defect is call-custody
   rather than sample geometry, so narrowing does not naturally remove it.
4. **DEFER:** leave the runner and paid authority unused; PPP-1 evidence/paper packet remain
   blocked.

Suggested exact ruling:

> I authorize FIX for the PPP-1 interruption-custody P1 only: make the wrapper's reserve →
> paid attempt → accounting capture → raw fsync path interruption-safe, persist a terminal
> PARTIAL checkpoint on interruption, add one regression test, and re-review only this named
> blocker. If it passes, execute the already-authorized one paid PPP-1 run under the unchanged
> exact roster, token caps, and strict $23.56 NTE, then build the exploratory manuscript packet.

## Verification

- TDD implementation RED: expected missing-module failure; initial focused GREEN 9/9.
- First fix cycle RED: 14 expected failures plus one custody-label failure; focused GREEN
  24/24.
- Fresh controller verification: **24 passed in 6.32s**.
- Fresh full offline harness: **724 passed in 128.53s**.
- Only the pre-existing pytest temporary-directory cleanup warning followed the green runs.
- Paid calls: none. Credential access: none. Spend: `$0`.

## Git and concurrent work

- Initial implementation: `b23cf4bf9`.
- First P1 fix cycle: `a914f5d4`.
- Portfolio and sibling-benchmark files were concurrently dirty and remain untouched by
  this WCF close. Stage/commit WCF paths explicitly only.

## Next session

On session open: load `project-dashboard.html` (Live-status first).

Read this handoff, `PENDING-QUESTIONS.md`, the authorization record, and
`20260713o-codex-ppp1-execution-plan.md`. If Jimmy has not ruled, ask him to choose
FIX / DISCLOSE-AND-RUN / NARROW / DEFER; recommend FIX. Make no credential or inference
request before that ruling.

If FIX is authorized, dispatch the original runner implementer for only the named change,
then have the existing quality reviewer verify only that blocker. Do not reopen general
review. On PASS, run once under the existing authority and immediately build the paper
packet. Stop after the packet for Jimmy review; do not enter T4.

On session close: update the dashboard per `AGENTS.md §The project dashboard`, then
open/reload it in the browser and leave the verified next-session view open for Jimmy.

## Session allocation

Empirical execution 0% · paper work 0% · infrastructure 80% · governance/admin 20%.
The session removed the cap/scope gate and built the minimum runner, but the binding
second-cycle rule required escalation before empirical execution.
