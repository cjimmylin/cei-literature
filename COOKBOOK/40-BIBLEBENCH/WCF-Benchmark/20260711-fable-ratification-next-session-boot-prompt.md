# WCF-Bench — Ratification / Then Gate-Prereg Boot Prompt

Continue WCF-Bench, scope-locked to
`COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`, at the judgment tier.

On session open: load `project-dashboard.html` (Live-status first).
On session close: update the dashboard per `AGENTS.md §The project dashboard`.

## Step 0 — state load

1. Read `AGENTS.md` and the dashboard's Live-status, progress, gate board, open
   escalations, and §Instructions for next session.
2. Check `git log --oneline -15 -- COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` and the branch
   `codex/wcfbench-mvp-testable` for newer commits.
3. Read, in order:
   - `20260711-codex-provisional-adjudication-recommendations.md`
   - `PENDING-QUESTIONS.md`
   - the latest `*codex-session-handoff.md`
   - Task 4–6 and §Progress in `20260711-codex-execution-plan.md`
   - R43–R46 in `20260711-fable-mvp-disagreement-adjudication-memo.md`
4. Spot-check immutable Task-4 evidence only if needed to decide; do not rerun it.

## Deliverable 1 — ratify or revise the provisional packet

Jimmy/Fable decides the packet's four checklist items. If ratified, write a new dated
binding memo continuing at R47+ that states, without reinterpretation:

- whether Task 4 is ratified as compliant, with the current manifest retained, zero OPEN
  eligibility explicit, and the candidate ladder closed;
- whether the 22-entry EPISODE registry remains `DRAFT_UNAPPROVED` or has completed
  item-level human approval/corrections;
- the exact Task-6 qualified surface and acceptance criteria compatible with the ruled
  citation-gated scorer, or a formal Task-6 deferral; and
- whether the paid-call pause remains in force. No paid call is authorized by this prompt.

If operating below Jimmy/Fable tier, do not assign R numbers or overrule anything. Record
recommendations only and leave the questions pending.

## Deliverable 2 — only after Deliverable 1 clears the live queue

Then execute Agenda item 2 of `20260711-fable-next-session-boot-prompt.md`: prepare the
gated G1–G7 run pre-registration. It must be binding only at Jimmy/Fable tier; otherwise
mark it `PROVISIONAL — pending Jimmy ratification` and reserve rather than assign R numbers.
No live calls are needed or authorized.

Do not start G6, edit the bank, modify prompts, change the manifest, activate the EPISODE
registry by inference, or make paid OpenRouter calls. Preserve all run/report directories.

## Close

Update all required LIVE dashboard surfaces, write a new dated handoff and next boot
prompt, rewrite dashboard §Instructions for next session, run offline verification, then
commit and fast-forward push explicit WCF-Benchmark paths only.
