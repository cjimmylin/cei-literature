# WCF-Bench — Codex Session Handoff (2026-07-11b)

## Executive status

**MVP testable: NO.** The four user rulings in `PENDING-QUESTIONS.md` have been applied
without reinterpretation. Task 5 now has a complete, inert 22-item registry draft for
human review. Task 6's scorer behavior is fixed to the existing citation-gated contract,
but its manifest eligibility remains unruled. No paid calls were made.

Execution-plan progress remains truthful and unchanged:

- [x] Tasks 1–4 complete.
- [ ] Task 5 — live 88-cell EPISODE run not authorized and registry not human-approved.
- [ ] Task 6 — live persisted re-read not authorized; anchor-use eligibility unspecified.

## Rulings applied

1. The Task-4 manifest remains the manifest of record and the candidate ladder is closed.
2. Codex was authorized to draft, but not approve or activate, the EPISODE registry.
3. All paid calls are paused; offline work only.
4. Task 6 must use the current citation-gated `judge_score_anchor_use` behavior as-is.

`PENDING-QUESTIONS.md` now separates these resolved rulings from the two remaining gates:
human approval of the Task-5 draft and a qualified manifest surface for Task 6.

## Task 5 — EPISODE registry draft

Commits:

- `d1c0bd060` — initial 22-item review draft and fail-closed loader.
- `30f3ba5c0` — approval, detector-field, and driver-verb hardening after code review.

Files:

- `04-HARNESS/config/episode-spec-registry.draft.json`
- `04-HARNESS/wcfbench/episode_registry.py`
- `04-HARNESS/tests/test_episode_registry.py`

The draft covers exactly the 22 frozen `episode: true` items. Each entry contains an
`EpisodeSpec` mapping, a `bank.stem`-only blind prompt source, mapping rationale, and known
limitations. It is explicitly `DRAFT_UNAPPROVED`; ordinary loading and spec construction
fail closed. Approval requires a reviewer, review timestamp, and every item marked
approved. The draft is not imported by a runner and creates no run directory.

Human review must adjudicate each entry's `mapping_basis` and `known_limitations`. Only
after approval should a later session build the 88-cell checkpoint/transcript/report path.

## Task 6 — ruled behavior and remaining blocker

No Task-6 code was changed. The current citation gate remains untouched as directed.

The bounded offline trace established:

- The Task-4 manifest defines only `open_award`, `disclosure`, `coherence`, and
  `settled_core`; it has no anchor-use eligibility or template hash.
- Mapping anchor use to any of those surfaces would invent a new ruling. `open_award` also
  has zero eligible judges.
- The existing citation-gated scorer never sends uncited anchors to a judge, so it cannot
  satisfy the execution plan's uncited-paraphrase recovery fixture or expected floor rise.

The narrowed remaining question is recorded in `PENDING-QUESTIONS.md`: identify the
qualified surface, if any, and align Task-6 acceptance criteria with the ruled as-is gate.
The persisted re-read remains additionally paused by the no-paid-calls ruling.

## Manifest and spend

- Manifest of record:
  `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-manifest.json`
- Task-4 outcome: zero OPEN-eligible families; candidate ladder closed.
- Internal Task-4 spend: **$0.4878**.
- Key-side Task-4 delta: **$0.4873**.
- This session's additional spend: **$0.00**.

## Verification

Run from `04-HARNESS/`:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q
```

Fresh result after the review repairs: **492 passed in 5.95s**.

Additional review gates:

- Task-5 specification review: approved.
- Task-5 code-quality review: approved after all three Important findings were repaired.
- Frozen bank and existing `07-PILOTS/` history were not edited.
- No network or OpenRouter calls were made.

## Exact next actions

1. Human-review the 22 registry entries; approve or return specific item mappings.
2. Keep paid calls paused unless explicitly reauthorized.
3. Rule which qualified surface admits the existing anchor-use prompt, or leave Task 6
   blocked and revise its acceptance criteria to match the citation-gated behavior.
