# WALKWORTHY Design 02 Dashboard Containment — Correction Handoff

**Date:** 2026-07-15
**Agent:** Codex
**Scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/`
**Branch:** `codex/walkworthy-design02-label-helper-spec`

## Correction and paper-facing state

The original `20260715-codex-design02-label-helper-complete-handoff.md` is an
immutable historical record and was not edited. Its dashboard statement that there
was zero page-level overflow was incomplete: the global
`.wrap { overflow-x: hidden }` rule masked oversized legacy tables by clipping them,
so the 390 px body width appeared contained while right-side table content was not
reachable.

The living dashboard now contains the narrow correction only:

- `.wrap` retains its width, margin, and padding but no longer hides horizontal
  overflow;
- `.panel` now uses
  `min-width: 0; overflow-x: auto; -webkit-overflow-scrolling: touch`, making wide
  tables locally scrollable;
- `.figureCard { min-width: 0 }` allows the one-column mobile grid to shrink, and
  `.flowPreview { overflow-x: auto }` exposes rather than clips compact previews;
- `.check .st` is 260 px wide so its existing nonwrapping status badges do not create
  orphan overflows outside a real scroll range.

The dashboard's 554/554 live-status wording is also corrected: this was the earlier
G7 closure suite, not a fresh or current full-suite run.

No helper source, generated helper artifact, frozen-source hash, committed-artifact
hash, test result, gate, label, adjudication, manuscript result, verdict, or release
state changed. The existing **90/90** focused result and **750 passed, 1 skipped**
full-suite result remain the helper evidence. Labels remain **0/439**.

## Browser and structural acceptance

Python Playwright launched the installed system Google Chrome and opened the actual
dashboard directly by `file://` at **1280×900** and **390×844**. Both viewport runs
had zero console errors, page errors, failed requests, or HTTP(S) requests.

- At 1280 px, body and document widths were each `1280/1280`; no element was
  oversized.
- At 390 px, body and document widths were each `390/390`. All 10 elements with
  `scrollWidth > clientWidth` had themselves or an ancestor with computed
  `overflow-x: auto` and a real scroll range.
- All nine tables wider than their panel had a reachable local right edge. Setting
  each owner to its maximum horizontal position produced positive `scrollLeft`
  values from 46 through 527 px; both compact previews likewise reached 40 px.
- The wrapper computes to `overflow-x: visible`, and the stylesheet contains no
  `overflow-x: hidden` clipping rule.

The dashboard parsed as HTML with 14 unique IDs and 30 resolving local/fragment
links. All 51 historical changelog rows were preserved, with exactly one new row
appended. The original completion handoff still has SHA-256
`2cce0cb4c76813cb5adaf7f8fa9310c86b3b37ab3b5078ddac437e59c6c05430`.

## External portfolio warning

The parent `../ACTIVE-CRITICAL-PATHS.md` contains pre-existing stale
PR-13/state-load-only wording. It is outside this WALKWORTHY task scope, was not
edited, and requires separate portfolio-authorized reconciliation before the next
Codex G4-import session interprets returned labels. This discrepancy does not block
humans from completing the authorized Design 02 packet.

The human workflow remains authorized and unchanged: Jimmy completes the primary
page; an independent labeler receives only the reliability page plus instructions;
Jimmy completes finalization and returns the four-file packet. A partial return still
does not authorize G4 or manual CSV repair.

## Boundaries and re-entry

No network call, credential access, paid call, HOLDOUT access, helper regeneration,
historical handoff rewrite, frozen-surface change, push, or rebase occurred.

On session open: load `00-PORTFOLIO/project-dashboard.html` (Live status + §12 first),
then this newest correction handoff and the immutable completion handoff.

On session close: update the dashboard per the local `AGENTS.md` project-dashboard
protocol, write a new dated handoff, and commit only explicit WALKWORTHY paths.
