# INNOVATION — Next-Session Re-entry Prompt

**Written:** 2026-07-09 · paste the block below verbatim as the first message of the next session (any model tier; it self-routes).

---

Continue the INNOVATION workstream (outer-alignment gap portfolio) in `CEI-Lit-WS/INNOVATION/`. All design work is done and committed (`347f2afb9`); this session is execution.

Read, in order, before doing anything:
1. `INNOVATION/20260709-session-handoff.md` — current state, the work loop, binding constraints, Jimmy's gates
2. `INNOVATION/00-CHARTER/03-reentry-guide.md` — pick the playbook matching this session (A keys / B credential-blocked / C Fable-tier / D housekeeping)
3. `INNOVATION/07-opus-handoff.md` — the live queue; work it top-down within the current cycle

Then state which playbook applies and begin. Defaults unless I say otherwise this session:
- No API keys are available → Playbook B: execute Cycle 1 in order (1.1 taxonomy codes BEFORE 1.2 acquisitions; then 1.3 fairgold, 1.4 position paper, 1.5 RP-04 corpus prep, 1.6 spec clause registries). Delegate mechanical batches (acquisitions, extraction) to Sonnet-tier subagents with explicit `model=`.
- If this is a Fable session: Playbook C — adjudicate `INNOVATION/PENDING-RULINGS.md` (if present) and queued gate reviews first; do not spend Fable tokens on queue mechanics.

Hard rules (from `00-CHARTER/01-governance-protocol.md` — read it if you touch anything beyond the queue): kill criteria execute mechanically; kernel sections in dossiers are frozen (expansions append as `[OPUS-EXPANSION YYYYMMDD]`); ⚠-flagged arXiv IDs must be verified before download or citation; external prose cites VERIFIED sources only; no `rm` ever (RECYCLE-BIN); new dated files instead of edits to frozen docs; run `git log -1` before committing (parallel sessions share this repo).

End of session: check off completed items in `07-opus-handoff.md`, append one line to `00-CHARTER/04-decision-log.md`, write/refresh a dated handoff if state changed materially, commit + push.

---

**Why this prompt exists:** the 2026-07-07 Fable session front-loaded all judgment work (field map, gap atlas, 10 research programs with kill criteria, governance). Post-window sessions execute mechanically against those artifacts; ambiguity goes to `PENDING-RULINGS.md`, not improvisation.
