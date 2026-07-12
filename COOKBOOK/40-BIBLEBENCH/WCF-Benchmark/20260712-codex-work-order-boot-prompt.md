# WCF-Bench — Codex Boot Prompt: R47–R53 Offline Work Order (paste to start the session)

Continue WCF-Bench, scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`.
**Work on `main` — the branch `codex/wcfbench-mvp-testable` is MERGED (do not reuse it;
create a new branch or work per your standard isolation).** Offline-only: **no paid
OpenRouter calls** — every task below is code + re-parse of already-persisted evidence.

On session open: load `project-dashboard.html` (Live-status first).
On session close: update the dashboard per `AGENTS.md §The project dashboard`.

## Step 0 — state load

1. Read `20260712-fable-ratification-memo.md` IN FULL — it is the binding R47–R53 ruling
   set and contains your §4 work order. Findings of fact are in its §2; do not re-derive
   or relitigate them, but DO verify your outputs against them (that's built into W-R47.3).
2. Read `AGENTS.md` (anti-rabbit-hole rules apply) and the dashboard's Live-status.
3. Suite baseline: 492 green on merged main (verify once before starting).

## The work order (memo §4, in this order)

### W-R48 — willingness-veto fix (R48.1–.3)

The refusal/willingness heuristic must never be tripped by quoted evidence. At **every**
call site of `willingness_to_grade` (award parse, `parse_judge_verdict`, the numeric-axis
paths in `triaxial.py` and `contested.py`, all probes): run the content parse FIRST — an
emission containing parseable verdict content (KP award/deny lines, a `SCORE:` line, or
`A:/B:` case scores) is definitionally willing; apply the marker scan only when no
verdict content parses. Defense in depth: exclude double-quoted spans from the marker
scan. Preserve true-decline behavior (an honest "I can't grade this" with no verdict
content stays unwilling — surfaced ungraded, never a silent 0).

**Fixtures (persist verbatim, R45.4-style):** (a) a gemini Task-4 award-consistency rep
(quotes "I won't", perfect verdict — MUST parse); (b) a genuine decline text (MUST stay
unwilling); (c) one production marker-hit verdict from the MVP run. Mock-first TDD; suite
green.

**Done when:** all three fixtures pass; every call site covered by a test; no template
hash changed (this is parser-side only, R48.3).

### W-R47.3 — corrected manifest event (offline)

New dated run directory (e.g. `07-PILOTS/20260712-artifact-corrected-requal/`). Re-derive
the full pass table by re-parsing the **same persisted Task-4 raw evidence**
(`07-PILOTS/20260711-format-bridge-requal/raw_verdicts.jsonl` — sole evidence source, cite
it in the manifest) under the W-R48 parser. Emit: corrected manifest (loads through
`JudgePanel(manifest=)`), report with the corrected K=8 pass/fail table and an explicit
"corrected manifest event under R47.3; supersedes the as-executed Task-4 manifest as
manifest of record" statement, and the R34.4 **single-family label** on OPEN.

**Expected (memo §2 F-1/F-2 — verify, don't assume):** gemini eligible on
`open_award + coherence + disclosure + settled_core`; grok on
`coherence + disclosure + settled_core`; cohere/nova none. **If your re-parse diverges
from the memo's expectation in ANY cell, STOP and escalate via `PENDING-QUESTIONS.md`.**
The Task-4 directory is immutable — nothing in it is edited.

**Done when:** manifest loads in production path; report written; divergence check clean
(or escalated); tests cover the re-parse path.

### W-R49 — MVP OPEN re-parse (offline, immutability-preserving)

New dated directory (e.g. `07-PILOTS/20260712-mvp-open-reparse/`). Re-parse ALL persisted
judge verdict texts of `07-PILOTS/20260710-mvp-run/transcripts.jsonl` under the W-R48
parser: corrected per-cell scores, a per-cell **delta table** (expect the 155 marker-hit
verdicts / 65 OPEN cells to move or confirm), a new dated report (still
DESCRIPTIVE/PRE-GATE), and a recomputed disagreement summary (`eligible_spread`).
**Escalation-only rule (R49.2):** any delta that would materially alter an R42
adjudication reading goes to `PENDING-QUESTIONS.md` — do not relitigate R42 in the
report. Footnote F-4 (pre-bridge probe-stability AC results carry the same artifact) for
the historical record; revise no historical manifest.

**Done when:** corrected report + delta table exist; original run dir untouched;
escalations (if any) filed.

### W-R52.2 — Task-6 plan-text alignment (doc only)

Rewrite the Task-6 section of `20260711-codex-execution-plan.md`'s live copy (or a dated
amendment note if the plan is treated as immutable — prefer a dated amendment) to match
R52: citation-gated contract as-is; judge-assisted-upgrade directive superseded; Task 6
DEFERRED; no code change.

### Close-out

Update `PENDING-QUESTIONS.md` statuses to cite R47–R53 by number. Update the dashboard
(Live-status, progress, Milestone A checkboxes W-R48/W-R47.3/W-R49, S-row, update log,
§Instructions for next session → the R51.2 EPISODE judgment session + G1–G7
pre-registration lane). New dated handoff. Commit explicit paths only (`git log -1`
first; never `git add -A`); push.

## Hard rules

No paid calls · no bank/gold edits · no exemplar/template changes · no new candidate
screening · no EPISODE activation (R51.2 review is NOT yours) · immutable records stay
immutable · canary `WCFBENCH-CANARY-c1647-x9k4q` never re-minted · escalate, don't
improvise.
