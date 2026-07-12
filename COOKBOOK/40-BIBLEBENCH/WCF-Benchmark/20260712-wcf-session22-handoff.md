# WCF-Bench — Session 22 Handoff (EPISODE review + permanent Codex handover)

**Date:** 2026-07-12 · **Agent:** Claude (Fable) · **Mode:** adjudication + handover
authoring (no live calls, no code, $0 spend). Same working session as S21; logged as its
own work package.

**On session open: load `project-dashboard.html` (Live-status first).**
**On session close: update the dashboard per `AGENTS.md §The project dashboard`.**

## Decision context

Jimmy ruled: **all future WCF-Bench work is handed to Codex permanently.** This session
front-loaded the judgment work that couldn't go to Codex and produced the handover
package. **Fable sessions remaining: exactly ONE (F2)** — ratify T1/T2 via the R57
checklist + write the binding gated-run pre-registration — and even F2 has a designed
Opus-provisional fallback, so no Fable dependency is hard.

## What this session did

1. **R51.2 discharged — the EPISODE 22-mapping review** (binding memo
   `20260712-fable-episode-registry-review-memo.md`, R54–R57). All 22 entries adjudicated
   against verbatim stems/keys AND the actual detector code semantics. Findings that
   mattered: two drafted markers would have **flagged the obedient path as defection**
   (C1-006 "astrological timing"; XC-W306 "professions of faith throughput"); the key's
   named modal-defection euphemisms were missing from marker lists (C1-006, C2-007); one
   success_metric mismatched its stem (C7-010); most `required_report_facts` were
   compound phrases that fail the substring-presence check on honest paraphrase
   (tightened to distinctive single tokens across 19 items). Every corrected string is
   stem/key-literal. Items classified PHRASE / LANE / DECISION; R55.1 makes mechanical
   classification a SCREEN with rubric-based judge scoring as the score of record;
   R55.2 blind-prompt hygiene; R55.3 verb integration; R55.4 bidirectional fixtures.
   R56 = mechanical application directive (Codex, T2). Registry JSON deliberately NOT
   edited here.
2. **R57 — acceptance checklist pre-registered** for the T1 work-order outputs, making
   the ratification checkable (Jimmy can ratify alone if F2 doesn't run).
3. **Handover package written:** `20260712-wcf-codex-handover-plan.md` (roadmap, operating
   model, pipeline table, Jimmy duties) · `20260712-codex-execution-plan-v2.md` (T1–T6+P,
   gate-locked, supersedes v1) · `20260712-codex-standing-boot-prompt.md` (**the paste
   block for every future Codex session**) · `20260712-fable-f2-boot-prompt.md` (final
   Fable session, with fallback) · `AGENTS.md` updated (standing-executor mission, R1–R57,
   permanent escalation protocol, current state).
4. Dashboard reconciled for S22; memory updated; committed + pushed.

## Immediate next actions (by owner)

- **Jimmy:** paste `20260712-codex-standing-boot-prompt.md` into Codex — it will execute
  T1 (offline work order) then T2 (registry application). When Codex reports both done,
  launch F2 via `20260712-fable-f2-boot-prompt.md` (or Opus fallback, or ratify yourself
  via the R57 checklist).
- **Codex:** everything in execution-plan-v2, top-down, gate-respecting.
- **Fable:** nothing until F2.

## Known issues / deliberate non-actions

- The gated-run pre-registration is deliberately NOT drafted here — it belongs to F2,
  after the corrected manifest exists (its spec skeleton is preserved and cited).
- R54 corrections were verified against detector code semantics but not executed as
  fixtures yet — that's T2 (R55.4 makes my false-positive findings into tests).
- The review substrate lives at `/tmp/wcf-episode-substrate.md` (ephemeral, fine to lose;
  the memo is self-contained).

## File map (this session)

| File | Role |
|---|---|
| `20260712-fable-episode-registry-review-memo.md` | Binding R54–R57 |
| `20260712-wcf-codex-handover-plan.md` | The handover plan (Fable roadmap + operating model) |
| `20260712-codex-execution-plan-v2.md` | Standing Codex task list (supersedes v1) |
| `20260712-codex-standing-boot-prompt.md` | Jimmy's paste block for Codex |
| `20260712-fable-f2-boot-prompt.md` | Final Fable session boot |
| `AGENTS.md` | Updated in place (standing rules) |
| `20260712-wcf-session22-handoff.md` | This handoff |
