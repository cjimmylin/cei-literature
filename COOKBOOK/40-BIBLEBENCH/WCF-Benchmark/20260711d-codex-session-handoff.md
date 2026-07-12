# WCF-Bench — Codex Session 20 Handoff

**Date:** 2026-07-11

**Branch:** `codex/wcfbench-mvp-testable`

**Mode:** offline-only; no OpenRouter calls or spend

## What changed

1. Executed the state-adaptive Step-0 load in
   `20260711-fable-next-session-boot-prompt.md` and compared Claude's latest mainline
   updates with the live Codex branch.
2. Merged main into the branch at merge commit `b22e4ed70`, preserving the newer WCF LIVE
   state while adopting Claude's dashboard §Instructions-for-next-session protocol.
3. Spot-checked Task 4 against R43/R44 and its Done-when criteria using the immutable
   report, manifest, raw evidence, runner, and focused tests.
4. Added `20260711-codex-provisional-adjudication-recommendations.md`. It recommends Task-4
   ratification and bounded Task-5/Task-6 dispositions, but is explicitly non-binding:
   R47+ numbers are reserved rather than assigned pending Jimmy/Fable ratification.
5. Added a provenance link to that packet in `PENDING-QUESTIONS.md`; no question or ruling
   status changed.
6. Added `20260711-fable-ratification-next-session-boot-prompt.md` and rewrote dashboard
   §Instructions for next session. The new order is: ratify/revise the Task-4–6 packet
   first; only after that queue clears, pre-register the gated G1–G7 run.
7. Updated all affected LIVE dashboard surfaces and appended session S20. No execution-plan
   checkbox changed: Tasks 1–4 remain complete; Tasks 5–6 remain unchecked.

## Evidence and current state

- Canonical manifest remains
  `07-PILOTS/20260711-format-bridge-requal/20260711-format-bridge-requal-manifest.json`.
- Its offline `JudgePanel` activates Gemini Flash and Grok 4.20 across two families for
  coherence, disclosure, and settled-core, with zero OPEN-eligible judges.
- The Task-4 raw file contains 297 completed invocations. Four Cohere errors are retry
  records inside three invocations; all resolved within the fixed retry limit.
- Task-4 cost remains `$0.4878` internal versus `$0.4873` key-side; no spend this session.
- The Task-5 registry remains a 22-entry `DRAFT_UNAPPROVED` review artifact.
- Task 6 remains blocked by the missing qualified anchor-use surface and by the mismatch
  between its uncited-paraphrase acceptance criterion and the ruled citation gate.

## Verification

- Focused Task-4 suite: 19/19 passed offline.
- Episode-registry plus judge suite: 38/38 passed offline.
- Full harness suite: 492/492 passed offline.
- Dashboard parsed with Python's HTML parser; required LIVE markers and next-session links
  are present.
- New memo and boot prompt are canary-free; `git diff --check -- .` is clean.

## Next action

Run `20260711-fable-ratification-next-session-boot-prompt.md` at Jimmy/Fable judgment tier.
The required decisions are listed in the provisional packet's ratification checklist.
Do not begin the G1–G7 pre-registration as the main deliverable until that live queue is
cleared. Do not make paid calls unless Jimmy separately authorizes an exact bounded run.

On session open: load `project-dashboard.html` (Live-status first).
On session close: update the dashboard per `AGENTS.md §The project dashboard`.

## Known issues / deliberate non-actions

- No binding R47+ memo was written because this Codex session is below the required
  Jimmy/Fable judgment tier.
- No bank item, prompt, qualification manifest, or immutable run/report was changed.
- Task 5 was not activated and Task 6 was not implemented.
- The gated G1–G7 run pre-registration was not started; this follows the boot prompt's
  state-adaptive priority ordering rather than leaving a partially drafted judgment file.
