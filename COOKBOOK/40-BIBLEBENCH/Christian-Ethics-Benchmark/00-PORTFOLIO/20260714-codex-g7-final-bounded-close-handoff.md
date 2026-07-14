# WALKWORTHY — final bounded G7 close handoff

**Date:** 2026-07-14

**Agent:** Codex

**Disposition:** G7 `PENDING`; labels → G4 → verdicts → paper is the controlling path

## Paper-facing outcome

The already-authorized final 73 exact paraphrase-author replays are complete. All 73
returned HTTP 200 bodies containing Markdown-fenced JSON; all 73 correctly failed the
byte-frozen whole-body parser as `author_nonjson`. The bounded first-attempt-plus-replay
contract is therefore exhausted:

- author logical keys: 73;
- author POSTs: 146 = 73 first attempts + 73 exact replays;
- strict author outputs: 0;
- Jimmy semantic-review packets: 0;
- perturbed-SUT calls: 0;
- fixed paraphrase battery: 0/438 complete, 438/438 unresolved;
- G7 flip rate: not computed;
- G7 verdict: neither PASS nor FAIL; `PENDING`.

This outcome is now stated in `PAPER/06-results-scaffold.md`,
`PAPER/08-threats-to-validity.md`, and `PAPER/10-reproducibility.md`. The manuscript may
carry G7 as pending/a limitation; G7 must not delay a complete descriptive draft.

## Bounded execution and custody

The replay used the exact ratified Mistral payload/model/cap/provider ceiling for each
key, concurrency 1, explicit one-second pacing, and no hidden retry. No third author
call, repair, fence stripping, substitution, perturbed-SUT call, premium probe,
automatic scale-up, item/key/denominator change, or HOLDOUT access occurred.

- actual author spend: **$0.1250561**;
- reserved maximum booked: **$0.907200000**;
- accounted total: **$1.032256100**;
- remaining under the unchanged $30 NTE: **$28.967743900**.

Immutable replay outputs:

| Artifact | SHA-256 |
|---|---|
| `runs/20260713-o5-g7-a1/author-replay-checkpoint.json` | `13cbd4d839dd72012f57431af96687a9cff05aac420c694ad1422e6f29ebe0ef` |
| `runs/20260713-o5-g7-a1/jimmy-semantic-review-packets-replay.json` | `2d9b165e91ff53cbd929b3d459dbd1350057d9e5cb5957ba27e0f160d43dbcb0` |
| append-only `author-attempts.jsonl` | `f4aa23bb305bc89974370d0eefeda1fb484a6aa9d6ed86a7e72a99b7a6d87166` |
| append-only `author-custody.jsonl` | `291ef4ef1c60cd4b277899f8d8239515e7a92035ce7e21766f0191eecc286e0c` |

The first-attempt checkpoint and packet files remain byte-identical:

- `author-checkpoint.json`: `836bfb758ac7fc5331c4b2148c753e5d0605c13c5569eff6c3fe84ce324b95af`;
- `jimmy-semantic-review-packets.json`: `fc6e8e4384fe0d10d2a108b8a0056c7c2a69733d7a5d16446d2ab78762e1aea1`.

## Mechanics and verification

TDD added an exact-key, crash-safe replay/resume path to
`harness/walkworthy/g7_author_stage.py`. It verifies the registered first-artifact
prefixes/hashes, permits exactly one replay only from the registered replay-required
state, preserves earlier outcomes, contains per-key transport stops, and writes NEW
replay checkpoint/packet files without overwriting first-attempt reports. Independent
specification and code-quality reviews passed.

- focused replay tests: 15/15 passed;
- G7-focused suite: 139/139 passed;
- fresh full suite after the code change: **549/549 passed**.

## Controlling critical path

Human labels remain **0/439 Part-A units**; the post-PR-16 Part-B burden is **1,174
cells**. The next paper-conversion trigger is a completed label wave. Wave 1 is designs
`02/07/01` (84 Part-A units), with the registered reliability arm.

The next session must:

1. detect and validate filled label CSVs without loading HOLDOUT;
2. for every complete available wave, run the frozen G4 branch with explicit judge
   models, then mechanically recompute licensed statuses/verdict rows;
3. update the O5 report and PAPER results immediately for each completed wave;
4. run the design-09 FR-8 replacement-judge cascade only after design-09 labels permit
   it;
5. if no labels are filled, stop with **`O5 blocked on labeling`**—do not create more
   G7 engineering, calls, or ruling memos.

Any future specification gaps should be bundled into one preflight review. A genuinely
unregistered G7 behavior is documented once as G7 `PENDING` and that thread stops; no
serial PR chain is to be opened.

## Safety and ancillary work

No files were deleted, no frozen rule/report was edited, credentials were loaded only at
call time and never printed or committed, and HOLDOUT was never loaded. Empty runtime
`.lock` files remain untracked and must not be staged. The BibleBench portfolio dashboard
one directory above is stale but outside this scope lock; the local WALKWORTHY dashboard
is the authoritative updated surface for this handoff.
