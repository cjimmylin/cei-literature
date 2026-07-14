# WALKWORTHY — PR-28 Closed / G7 Author First-Attempt Checkpoint Handoff

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Date:** 2026-07-13
**Agent:** Codex
**Status:** PR-28 CLOSED; 73/73 AUTHOR FIRST ATTEMPTS CUSTODIED; 73 EXACT REPLAYS NEXT
**Scope:** WALKWORTHY O5 W5/G7 author stage only; no perturbed-SUT calls

## Paper-facing outcome

Jimmy ratified PR-28 option 1. The immutable ruling is
`20260713y-jimmy-pr28-runtime-ruling.md`; `PENDING-RULINGS.md` now records PR-28 as
RATIFIED + CLOSED.

The frozen G7 author contract is implemented and independently reviewed. The exact
73-item PUBLIC author first-attempt stage then ran under the already-ratified PR-25/25(a)
order. It produced a complete first-attempt custody checkpoint, but no paraphrase reached
Jimmy's semantic review:

| Measure | Result |
|---|---:|
| Planned author keys | 73 |
| First attempts / POSTs | 73 / 73 |
| HTTP 429 provider failures | 50 |
| HTTP-200 strict-parser failures | 23 |
| Failure form for all HTTP-200 bodies | Markdown-fenced JSON (`author_nonjson`) |
| Jimmy-review pending | 0 |
| Replay required | 73 |
| Reported actual cost | $0.0280474 |
| Conservatively reserved cost | $0.907200000 |
| Remaining registered global NTE | $29.064752600 |

Every first response and failure is append-only custodied. No output was repaired or
partially accepted. The empty Jimmy packet export is truthful: zero items passed the
strict parser + Gate A, so no semantic judgment is yet requested.

This is not G7 evidence and licenses no paper statistic or verdict. The next
paper-conversion trigger remains a fully adjudicated fixed 438-cell surface per battery.

## Implemented mechanics and review evidence

New production modules:

- `harness/walkworthy/g7_author_contract.py` — exact frozen prompt, strict parser,
  canonical PR-28 key serialization, Gate A → registered L1–L9, PUBLIC Jimmy packets,
  fail-closed explicit review handling, and body-full author/review custody.
- `harness/walkworthy/g7_author_stage.py` — exact 73-key PUBLIC surface, first-attempt-only
  concurrency-two orchestration, immutable registration/checkpoint/packet exports, and
  crash-safe joined-ledger resume.

Narrow extensions:

- `g7_perturbation.py` retains protected non-role literals and exposes Gate A without
  changing the existing materialization result.
- `g7_runner.py` adds body-free `validation_pending`, validation outcomes, locked attempt
  snapshots, and idempotent pending reconciliation without changing any frozen roster,
  cap, provider ceiling, count, concurrency, or NTE constant.

TDD/review sequence:

1. initial missing-module RED;
2. prompt/parser/lint/lifecycle GREEN;
3. independent specification review found and closed three fail-closed applicability/
   custody defects;
4. independent quality review found and closed every two-ledger crash window;
5. author-stage RED→GREEN driver; independent specification PASS;
6. independent quality review found and closed the four pre-dispatch resume windows and
   non-callable-transport trap;
7. final independent quality review APPROVED.

Fresh final full suite: **543/543 passed in 100.02 s**. Only the pre-existing macOS
pytest temporary-directory cleanup warning appeared after the zero exit status.

## Immutable production artifacts

Directory: `runs/20260713-o5-g7-a1/`

| File | SHA-256 |
|---|---|
| `author-registration.json` | `1c7ff038d0228b02d22ac98872f44d3d1969d1b8b1bc38dbc37786e9092aefc2` |
| `author-attempts.jsonl` | `0853669ddbb75d4e504d3c167125c9f5bd8a5f59ed2cc718db692757f591279e` |
| `author-custody.jsonl` | `0e48560ec27651b265457c5eeeebf60c2d68c343a0fb62f1eb950d5d2ac20301` |
| `author-checkpoint.json` | `836bfb758ac7fc5331c4b2148c753e5d0605c13c5569eff6c3fe84ce324b95af` |
| `jimmy-semantic-review-packets.json` | `fc6e8e4384fe0d10d2a108b8a0056c7c2a69733d7a5d16446d2ab78762e1aea1` |

Frozen inputs reverified immediately before execution:

- author contract: `59caaa1c055dd1badd16694e078a91a40b18e4e1ebd9f6d15510f89e9f79b320`;
- role manifest (`harness/config/g7/production_role_manifest.json`):
  `013600bd2f1c34b7353319e98395aa8b1b5b921796d73a840e5ddc2138027480`;
- L7 inventory (`harness/walkworthy/l7_name_inventory.json`):
  `73711dd6ae89989ae0dfdad67a7a9516b84518eff0366e30fa061c70496b70b0`;
- deterministically derived PUBLIC production manifest (custodied in
  `author-registration.json`):
  `616d2e93491adcb8da9fc00664693cd8c4685a95fc36b6fc09816c32414edf0e`.

## Next session — exact author replays

No new ruling or paid authorization is required. All 73 keys are covered by the one
byte-identical replay already ratified in PR-25/26/27/28.

1. Extend the reviewed author-stage driver under TDD to issue exactly one replay for the
   73 `replay_required` keys and write **NEW** immutable replay checkpoint/packet files;
   never overwrite the first-attempt checkpoint or empty packet export.
2. Rebuild every request from the frozen sources and require the replay payload hash to
   equal attempt 1. Same model, 4,096 cap, provider ceiling, and raw payload bytes.
3. Use concurrency one and explicit paced scheduling for the 50 prior HTTP-429 keys;
   the 23 fenced-JSON keys remain strict-parser failures if repeated. Timing changes no
   payload byte and adds no hidden retry.
4. Any second transport/parser/Gate-A failure becomes `unresolved`; no third call,
   repair, substitution, item replacement, or denominator change.
5. Successful parser + Gate-A outputs remain `validation_pending`; export the exact
   PUBLIC packet for Jimmy. Stop before every perturbed-SUT call.

Jimmy can continue Part-A wave-1 and Part-B labeling independently. Jimmy is needed for
G7 only if a replay produces semantic-review packets.

## Safety / scope

- HOLDOUT was never loaded.
- No label, item, key, denominator, frozen gate, historical report, MVP artifact, or
  sibling benchmark was edited.
- No model substitution, extra probe, automatic scale-up, or perturbed-SUT call occurred.
- OpenRouter credentials were sourced only at call time and do not appear in committed
  artifacts.
- Empty `.lock` files are runtime locks and are intentionally not staged.

On the next session close: update the living dashboard, write a NEW dated handoff, and
commit/push only explicit WALKWORTHY paths with a fast-forward push.
