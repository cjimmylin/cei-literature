# WCF-Bench — Session 21 Handoff (Fable ratification + OPEN-surface adjudication)

**Date:** 2026-07-12 · **Agent:** Claude (Fable) · **Mode:** adjudication only (no live
calls, no code, $0 spend)

**On session open: load `project-dashboard.html` (Live-status first).**
**On session close: update the dashboard per `AGENTS.md §The project dashboard`.**

## Headline

The "zero OPEN-eligible families" crisis from Codex's Task-4 requalification **was ruled a
harness parser artifact, not judge failure** (`20260712-fable-ratification-memo.md`,
binding R47–R53). Sample-level read of the raw evidence proved: all 16 incumbent
award-consistency failures were `fail_format` caused by `willingness_to_grade` treating
the judges' **verbatim quote of the fixture's "No — I won't write it…" sentence** as a
refusal (`"i won't"` marker). Counterfactual re-parse: both incumbents matched the
pre-registered pattern **8/8 perfectly**. Artifact-corrected, the outcome is exactly
R44.5's anticipated branch (b): gemini single-family OPEN, ladder closed on the merits
(grok's discrimination 0/8 is real; cohere/nova failures are real).

Production scope: the same veto **nulled 155/1,700 judge verdicts (9.1%) in the MVP run
of record — all OPEN-kind, 65 cells**. All recoverable offline from persisted texts.

## What this session did

1. **Evidence:** read the full branch document chain; sample-read
   `07-PILOTS/20260711-format-bridge-requal/raw_verdicts.jsonl` (all 32 AC reps + raw
   calls); proved the artifact mechanism in code; ran the counterfactual re-parse;
   scanned the MVP transcripts (155 hits) and pre-bridge probe-stability (artifact
   present there too — gpt 6/6, mistral-small 6/6 of their AC fails).
2. **Binding memo:** `20260712-fable-ratification-memo.md` — R47 (artifact-invalidation +
   corrected manifest event + OPEN = PENDING-CORRECTION + ladder stays CLOSED), R48
   (willingness-veto fix directive), R49 (MVP OPEN re-parse directive), R50 (Tasks 1–4
   RATIFIED; interim rulings 2+3 concurred; paid-call pause remains), R51 (EPISODE
   mechanism ratified; 22 item mappings need judgment-tier review), R52 (Task 6 formally
   DEFERRED), R53 (MVP-testable redefined; reachable entirely offline).
3. **Provenance of the interim rulings** (PENDING-QUESTIONS "Rulings received
   2026-07-11"): not conclusively attributable from the repo; resolved by deciding each
   **de novo** — three concurred outright; ruling 1's manifest-of-record clause
   superseded on new material evidence only (memo §2 F-5).
4. **Verification:** branch suite independently rerun in a detached worktree — 492/492
   (focused requal 19/19); Task 1–3 diffs read directly and found conformant to
   R45.3/R45.4.
5. **Merge:** `codex/wcfbench-mvp-testable` → main (merge commit; one conflict in
   `project-dashboard.html`, resolved branch-copy-wins per boot prompt, mainline history
   preserved in git).
6. **Dashboard reconciled** for S21: Live-status, quotability (OPEN =
   PENDING-CORRECTION), judge table, R-chain (+R47–R53 row), G4 row, Milestone A (R53
   definition + W-item checklist), critical path, format-bridge contingency (FIRED →
   RESOLVED BY RULING), docs table, update log, §Instructions rewritten.
7. **Next boot prompt:** `20260712-codex-work-order-boot-prompt.md` (the §4 offline work
   order: W-R48 → W-R47.3 → W-R49 → W-R52.2).

## What remains (by owner)

- **Codex (next session):** the offline work order — parser fix + fixtures, corrected
  manifest event (escalate any divergence from memo §2), MVP OPEN re-parse + delta table,
  Task-6 plan-text alignment. Zero live calls.
- **Fable/Jimmy (judgment lane):** R51.2 EPISODE item-level review (22 mappings vs frozen
  bank — dedicated session); gated G1–G7 run pre-registration (spec text in the
  superseded `20260711-fable-next-session-boot-prompt.md` agenda item 2 remains valid;
  must incorporate R47) — **deferred from this session** (queue was cleared but the
  prereg deserves its own session with the corrected manifest in hand).
- **Jimmy:** paid-call reauthorization + Task-5 SUT roster confirmation (both upstream of
  the 88-cell EPISODE run); G6 rater recruitment (Milestone B).

## Known issues / deliberate non-actions

- Grok's pre-bridge AC `fail_format` 8/8 (R44.3's premise) is *very likely* the same
  artifact but unprovable — the third-family screen persisted no raw texts (memo §2 F-4
  is explicit about the inference status).
- No G1–G7 pre-registration was drafted (see above — deliberate).
- The as-executed Task-4 manifest remains the loaded manifest of record until W-R47.3
  lands; OPEN is not scorable in the interim (R47.5) — this is stated on the dashboard.
- MVP OPEN descriptive numbers (including the SUT ordering on OPEN-heavy designs) should
  be treated as under-correction until the W-R49 delta table exists.

## File map (this session's artifacts)

| File | What |
|---|---|
| `20260712-fable-ratification-memo.md` | Binding R47–R53 + findings of fact + §4 work order |
| `20260712-codex-work-order-boot-prompt.md` | Next-session boot prompt (Codex lane) |
| `20260712-wcf-session21-handoff.md` | This handoff |
| `project-dashboard.html` | Reconciled post-merge (sole undated live file) |

Verification command (from `04-HARNESS/`):
`/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q` → 492 passed.
