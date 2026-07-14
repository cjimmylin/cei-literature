# WALKWORTHY — G7-A1 $0 Custody Core Complete / PR-26 Author-Contract Stop Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** CUSTODY CORE GREEN; PR-26 OPEN; NO CREDENTIAL/CALL/SPEND
**Scope:** WALKWORTHY O5 W5/G7-A1 only; PUBLIC/no-call mechanics

## Outcome

The authorized G7-A1 session began from a clean WALKWORTHY state. Both binding hashes
reproduced exactly before work:

- production manifest: `616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e`;
- production role manifest: `013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480`.

The required $0 custody core is implemented in `harness/walkworthy/g7_runner.py`, with
tests in `harness/tests/test_g7_runner.py`. It binds the exact PR-25 roster, role caps,
price ceilings, registered missing-cost maxima, 9,709-logical/971-replay/10,680-POST
limits, concurrency ≤2, and $30 hard NTE. It also provides:

- append-only start-before-transport / finish-after-transport custody with prompt and
  response bodies excluded from the spend ledger;
- exact default-transport request-byte hashes and one byte-identical replay before a
  thread stop;
- exact returned-model and numeric `usage.cost` validation, registered-maximum booking,
  conservative input-envelope checks, and post-custody NTE stops;
- cross-process locking, exact-key resume, registration-bound caps, chronological event
  validation, fresh atomic accounting snapshots, and process-safe immutable JSON writes;
- hidden OpenRouter retries pinned to zero.

No live phase orchestration, author prompt, semantic lint, scoring, or CLI was invented.

## TDD and review evidence

The implementation followed explicit RED→GREEN cycles:

1. initial missing module: expected `ModuleNotFoundError`;
2. first core: 14 focused tests green;
3. specification review found concurrency/payload/resume/chronology gaps; regression
   RED = 12 failures / 17 passes, then GREEN;
4. byte-identity review found canonical-vs-transmitted-byte mismatch; RED = 2 failures /
   29 passes, then GREEN;
5. code-quality review found input-envelope, stale-snapshot, and checkpoint-race gaps;
   RED = 5 failures / 31 passes, then GREEN = 36/36.

Final independent specification review: PASS. Final independent code-quality review:
APPROVED. Fresh verification:

- G7 custody/mechanics/OpenRouter regression: **119/119 passed**;
- complete harness suite: **505/505 passed in 152.65 s**.

Pytest emitted only its pre-existing macOS temporary-directory cleanup warning; exit
status was zero.

## Genuine STOP — PR-26

PR-18 B1 requires every Mistral-authored paraphrase to pass exact mechanical invariants
and the full semantic L1–L9 lint before any perturbed SUT call. The repository supplies
protected templates and an injected exact-Boolean lint interface, but it has no:

1. literal Mistral paraphrase-author prompt;
2. exact response schema/parser; or
3. authorized semantic reviewer for L5/L9 and the remaining L1–L9 checklist.

This is not a transport detail. Guessing it would create the measurement treatment and
semantic acceptance rule after the run order was authorized. PR-26 is therefore OPEN in
`PENDING-RULINGS.md`; the thread stopped before credential access.

Recommended owner line:

> Ratify PR-26 option 1: route the missing G7 paraphrase-author contract to one explicit
> Opus memo that freezes the literal Mistral prompt, exact JSON field-path schema/parser,
> operational L1–L9 checklist, and first/second author-output or lint-failure
> disposition; require Jimmy ratification of that memo and its artifact hash before any
> author or perturbed-SUT call; retain PR-18 B1 invariants, the fixed 73-item/438-cell
> denominator, and every PR-25 roster/replay/cost limit; no substitution, item
> replacement, denominator change, HOLDOUT access, or automatic scale-up.

If Jimmy does not ratify option 1, remain no-call and keep G7 PENDING.

## Custody / spend boundary

- `runs/20260713-o5-g7-a1/` remains absent.
- OpenRouter credentials were not sourced or read.
- Client POSTs: **0**.
- Session spend: **$0.00**.
- No HOLDOUT, label, MVP, item, key, denominator, frozen rule, or historical report was
  edited.
- Unrelated sibling-bench worktree changes were observed and preserved; none belongs to
  this session or may be staged.

## Paper-facing progress and next trigger

This session removed the paid-run custody implementation as a P0/P1 risk and narrowed
the remaining G7 blocker to one explicit authoring/semantic-review contract. It produced
no G7 evidence or paper value because no call was permissible. The next paper-conversion
trigger remains a fully adjudicated 438-cell surface for each battery; the existing 122
unresolved original cells still require Part B. Independently, each completed label wave
triggers its frozen G4 branch and incremental PAPER §6/O5 fill.

Ancillary work was limited to the exact custody core, its required reviews, PR-26, this
handoff, and the living dashboard because each directly protected the next paid command.

## Next session

Use dashboard §12. First obtain PR-26 option-1 ratification, then one explicit Opus
author-contract memo and Jimmy ratification of its exact artifact/hash. Do not source a
credential or create the G7-A1 production run before both gates close. After they close,
implement only the literal prompt/parser contract under TDD and resume the unchanged
PR-25(a) cheap-first execution order.

On session open: load the BibleBench paper-first surfaces read-only, then
`00-PORTFOLIO/project-dashboard.html` (Live status + §12 first), this handoff, PR-26 in
`PENDING-RULINGS.md`, PR-18 B1, and PR-25/25(a).

On session close: update `00-PORTFOLIO/project-dashboard.html`, write a NEW dated
handoff, and commit/push WALKWORTHY paths only with explicit pathspecs.
