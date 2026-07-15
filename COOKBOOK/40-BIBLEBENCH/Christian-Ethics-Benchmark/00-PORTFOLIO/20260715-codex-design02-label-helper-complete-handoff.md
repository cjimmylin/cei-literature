# WALKWORTHY Design 02 Labeling Helper — Complete Handoff

**Date:** 2026-07-15
**Agent:** Codex
**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`
**Branch:** `codex/walkworthy-design02-label-helper-spec`

## Outcome and paper-facing progress

The approved Design 02 labeling-helper plan is complete. The verified offline packet
removes the rate-limiting manual formatting and custody friction between the current
blank PUBLIC instruments and one complete PR-29 Design 02 intake:

- `labels/20260710-partA/design02-helper/02-primary-labeling.html` — Jimmy's 12-row,
  21-turn primary workflow;
- `labels/20260710-partA/design02-helper/02-reliability-labeling.html` — the isolated
  independent second-labeler four-row, seven-turn workflow;
- `labels/20260710-partA/design02-helper/02-finalization.html` — exact import,
  declaration, turn-disagreement adjudication, and export workflow;
- `labels/20260710-partA/design02-helper/README.md` — controlling human/Codex sequence.

The packet creates no benchmark result by itself. Labels remain **0/439** until the
human outputs are returned, verified, and imported. No G4 branch, Part-B conversion,
gate, status, verdict, manuscript/PDF result, or release claim changed.

## Frozen sources and committed artifacts

Source SHA-256 values independently reproduced:

- primary blind CSV:
  `1ace34dd8b33b06448c4d712edca4be0f4525e6223820ea4c68101736d2e147a`;
- reliability overlap blind CSV:
  `f448b339c1708ee5de252241e2ba03452283a2b965c1b294b9b680cca0669bee`.

Committed artifact SHA-256 values independently reproduced and match the Task 7
record:

- primary page:
  `e83070ba85c0d083b668edb5f8cb4814d4adb12713e1e35d7b1ab8799d3c260f`;
- reliability page:
  `9d3d4c1daf7809b72bcdb1c02675cb39e95664cae19e524708539816c23a9193`;
- finalizer:
  `7cbf45d1fef7221c94586f13f67cca5ce4a1ce79efae95ff82017bb2b0e3a04a`;
- README:
  `73510bd3fa6f9f9ccfa19a1f1124bfb74b55966ddc811aa9cc8279386dd9c277`.

No helper code or committed helper artifact changed during Task 8.

## Actual-page browser acceptance

Python Playwright launched the installed system Google Chrome and opened the three
**actual committed** HTML pages directly by `file://`; no server or generated
replacement page was used. Each page passed at **1280×900** and **390×844**:

- 6/6 page/viewport combinations loaded with zero console errors, page errors, failed
  requests, or HTTP(S) requests;
- body `scrollWidth` equaled `clientWidth` at both widths;
- keyboard focus produced a visible 3 px solid outline;
- the complete nonempty 1,994-character first response matched the embedded first turn
  on both labeling pages and remained readable at both widths;
- primary showed `Turn 1 of 21` and `Primary labeling draft`;
- reliability showed `Turn 1 of 7` and `Independent reliability draft`;
- review/export began gated; finalizer controls were visible and both exports disabled;
- a representative primary flow advanced exact turn 1 to turn 2 while export remained
  disabled;
- a valid primary/reliability fixture import exposed exactly the registered U000 turn-2
  disagreement; distinct custody metadata plus gold enabled both finalizer exports.

No screenshots or repository outputs were saved.

After the living update, the actual dashboard also parsed and passed direct
`file://` system-Chrome checks at 1280×900 and 390×844 with zero console errors,
page errors, failed requests, HTTP(S) requests, or page-level overflow. A dashboard-only
horizontal containment rule prevents its legacy wide, locally scrollable tables from
expanding the 390 px page; no table content or helper artifact changed.

## Fresh tests and independent boundaries

From `harness/`, using the absolute project virtual environment:

- focused helper + judge-validation + PR-29 suite: **90 passed in 103.69s**
  (**104.90s wall**);
- full suite: **750 passed, 1 skipped in 670.77s** (**672.31s wall**).

Both runs emitted only the known nonfatal macOS pytest temporary-folder cleanup
warning after the passing result.

Independent checks also passed:

- all two source and four committed artifact hashes matched exactly;
- a case-insensitive scan of all three HTML pages found zero model, judge, unblinding,
  HOLDOUT, OpenRouter, network API, remote URL, external script/style, or service-worker
  strings; decoded payload/schema boundaries remain covered by the passing tests;
- all three helper pages parsed as one complete HTML document with one doctype, html,
  head, and body surface;
- secret-pattern scan returned zero matches;
- `git diff --check` was clean before documentation edits.

## Human workflow and paper-conversion trigger

1. Jimmy opens `02-primary-labeling.html`, completes all 21 turns across 12 rows,
   reviews, and downloads the completed primary CSV.
2. An independent second labeler receives **only** `02-reliability-labeling.html` and
   the Design 02 instructions, completes all seven turns across four rows, reviews, and
   returns the completed reliability CSV. Do not disclose the primary page, CSV, or
   draft to that labeler.
3. Jimmy opens `02-finalization.html`, imports both CSVs, supplies distinct opaque IDs
   and ISO-8601 timestamps with offsets, adjudicates every displayed disagreement, and
   downloads `reliability-declaration.json` plus `adjudications.jsonl`.
4. Codex verifies exact frozen-source, committed-artifact, returned-output,
   declaration, and adjudication schemas; imports append-only without overwriting
   historical inputs; and runs PR-29/G4 → available Part B → the frozen
   status/verdict branch → immediate manuscript/PDF conversion.

The next paper-conversion trigger is therefore **one complete Design 02 packet**. A
partial return does not authorize G4 or manual CSV repair.

## Deferred nonblocking review suggestions

Task 7's CLI polish, clear-draft UI, finalizer static scan, and generator documentation
suggestions remain deliberately deferred as P2/P3. They do not alter the registered
packet, custody, browser acceptance, or paper conclusion; implementing them now would
violate the paper-first anti-tangent rule. No further helper engineering is planned.

## Boundaries and integration state

No live call, credential access, network access, paid spend, provider model, HOLDOUT
access, G7/OPEN6 work, PR-30 disposition, item/key/denominator change, frozen-rule
change, gate computation, verdict, public release, or scale-up occurred. OPEN6 remains
stopped and PR-30 remains separate.

The branch's helper sequence is:

`d938583a0 → fe9e074e7 → 023668406 → a76335014 → 042ca63ac →
87b6c178c → 32d63e6d1 → c044fe79c → 7065fe5ca → 9329ffc6e →
aa3771627 → 1e139bee9 → 12b262955 → c188972e7 → f13d9234c →
749baf6bf`.

Task 8 started from `749baf6bf4c256157fd5798e5b42bb2dd7841716`. Its closure
commit is `WALKWORTHY: hand off Design 02 labeling helper`. Per the controller's scope,
this worker does not push or rebase; the controller will perform final whole-feature
review and integration afterward.

## Re-entry

On session open: load `00-PORTFOLIO/project-dashboard.html` (Live status + §12 first).

On session close: update the dashboard per the local `AGENTS.md` project-dashboard
protocol, write a new dated handoff, and commit only explicit WALKWORTHY paths.
