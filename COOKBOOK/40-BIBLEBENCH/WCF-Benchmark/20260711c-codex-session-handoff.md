# WCF-Bench — Codex Session Handoff (2026-07-11c)

**On session open: load `project-dashboard.html` (Live-status first).**

**On session close: update the dashboard per `AGENTS.md §The project dashboard`.**

## Executive status

**MVP testable: NO.** Tasks 1–4 are complete. Task 5 has a complete but
`DRAFT_UNAPPROVED` 22-item registry awaiting human mapping review; no EPISODE run exists.
Task 6 remains blocked because the ruled as-is citation-gated scorer has no qualified
manifest surface and cannot meet the plan's uncited-paraphrase acceptance criterion. Paid
OpenRouter calls remain paused.

The execution-plan checkboxes remain:

- [x] Tasks 1–4.
- [ ] Task 5 — human registry approval, runner path, and 88-cell live run remain.
- [ ] Task 6 — eligibility/acceptance ruling and persisted re-read remain.

## Claude-mainline reconciliation

Claude's committed session-16 dashboard and boot-prompt work was merged into the isolated
Codex branch at merge commit `a677f246b`. It added the living-dashboard protocol and
re-entry documents; it did not contain a new R47+ ruling or paid-call authorization.

The audit result was negative for both current gates:

1. Task 5 is authorized only through the draft stage. Human review must approve or return
   item-specific corrections before activation.
2. Task 6 still needs an explicit qualified surface, or a formal decision to leave it
   blocked and revise its acceptance criteria. Silence or a newer file timestamp is not
   authorization.

Claude's untracked dashboard screenshots and all unrelated dirty files in the main checkout
were left untouched.

## Living dashboard

`project-dashboard.html` was synchronized in commit `2242355a7`:

- Live status now names the 20260711 Task-4 manifest, the zero-OPEN outcome, 492 tests,
  paid-call pause, and the two pending gates.
- Progress and Milestone A show Tasks 1–4 complete and Tasks 5–6 pending.
- S17–S19 were appended without altering Phases 1–5.
- Judge evolution, G4, quotability, critical path, fired format-bridge contingency, and
  budget rows now match the persisted evidence.
- Specification and quality reviews both approved the update.
- Strict HTML parsing, live-fact assertions, navigation anchors, self-containment, and
  frozen-history checks passed.

The app browser rejected direct navigation to the local `file:` URL under its URL policy;
the required dashboard state was therefore loaded and verified from source without a
browser workaround.

## Manifest, panel, and spend

- Manifest of record:
  `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-manifest.json`
- Eligible panel surfaces: Gemini/Google + Grok/xAI on coherence, disclosure, and
  `settled_core`.
- OPEN: zero eligible judges/families; candidate ladder closed.
- Task-4 internal actual: **$0.4878**.
- Task-4 key-side delta: **$0.4873**.
- This session's live spend: **$0.00**.

## Verification

Run from `04-HARNESS/`:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest tests/ -q
```

Final result: **492 passed in 7.82s**.

No frozen bank item, existing pilot artifact, or sibling-project working file was edited.

## Exact next actions

1. Human-review `04-HARNESS/config/episode-spec-registry.draft.json`; approve all 22
   mappings or return item-specific corrections.
2. Rule which qualified surface admits the existing citation-gated anchor-use prompt, or
   formally leave Task 6 blocked and revise its acceptance criteria accordingly.
3. Keep paid calls paused unless explicitly reauthorized after those gates clear.
