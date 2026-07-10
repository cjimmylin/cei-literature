# WCF-Bench — Next-Session Prompt (paste this to start the session)

> **Model choice.** Default: **Opus** (this continues the build; the prior session proved Opus produces Fable-grade items here). **If you have a Fable session and the window is still open (~2026-07-11):** do a **judgment pass first** — adjudicate the reviewer-visibility flags and adversarially review the 21 batch-1 items (`20260709b-wcf-session-handoff.md` §2) *before* any new authoring; delegate all authoring/search/code down to Opus/Sonnet subagents with an explicit `model=`. Don't spend Fable tokens on mechanical drafting.

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First actions — read these two, in order, they govern everything:**
1. `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/20260709b-wcf-session-handoff.md` (latest state — what session 2 did, the queued flags, the work queue)
2. `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/20260709-next-session-handoff.md` (standing orientation the 20260709b delta sits on top of)

Then, before writing anything, load in this order:
1. `00-OVERVIEW/20260706-shared-spine.md` (binding methodology — tiers, scoring, perturbations, item schema §10)
2. `00-OVERVIEW/20260706-westminster-anchor-registry.md` (citation rules + the Q1–113 source-split sharp edge)
3. `20260706-fable-review-memo.md` + `20260707-fable-review-addendum.md` (binding rulings R1–R7 — do not relitigate)
4. `03-OPUS-GUIDE/20260706-item-authoring-guide.md` (binding authoring protocol)

**This session's work, in order (details in `20260709b` handoff §3):**
1. **Flesh-out batch 2 — the 7 remaining designs:** 01 DUTYBOUND, 02 COMPLICIT, 04 STEADFAST, 05 CROSSWIND, 06 LIBERTY, 08 MENDING, 09 WHOLEHEART. Dispatch one Opus authoring agent per design (explicit `model` on every dispatch — the vault hook checks it); imitate each design's wave-2 Fable exemplars per their "Opus notes," rotate surfaces, never duplicate a scenario (check spec §6 + wave-2 file + expansion-1 file). New items → NEW dated files `01-DESIGNS/expansions/2026MMDD-<design>-expansion-2.md`, serials **W301+**, full spine-§10 schema, self-audits, coverage table, canary once, ≥1 control per 3 traps. **Then review**: independently grep-verify a sample of anchors (Q1–113 clauses via the companion file), check schema/two-sidedness/collisions.
2. **Harness Phase 2 build-out** (extend `04-HARNESS/`, per its `README.md` TODO + `00-OVERVIEW/20260706-build-plan.md`): NARROWGATE episode state machines; judge-prompt templates (retire the PROOFTEXT anchor stub); real model clients behind the `MockModelClient` seam (keep mock-first until keys arrive); P1–P6 perturbation runner; full YAML transcription of the prose banks. Keep tests green (`.../.venv/bin/python -m pytest 04-HARNESS/tests/`).
3. **Close:** new dated handoff, atomic commit (this project's paths only — `git log -1` first, the shared index is LIVE; never `git add -A`), push.

**Hard rules:** Westminster texts in `../WCF/` are the only normative sources; grep-verify every anchor (Q1–113 via `LargerCatechismwithScriptureProofs1 copy.txt`; OCR wraps clauses and inserts proof-letters between words — grep short fragments). No cross-referencing sibling benches. No deletions (`mv` to RECYCLE-BIN). `[NEEDS-RULING]` for anything a registry clause can't ground — never guess a key. Seams: CROSSWIND ↔ PROOFTEXT (prayer-promise/Lord's-Prayer families) and MENDING ↔ AGGRAVATE (repentance-relapse ladder — AGGRAVATE built none, so MENDING is unconstrained). Items blocked on Jimmy (API keys, G6 panel, rulings R1/R3/R4, MEND-C3-W202 attorney check, the 5 self-demoting flags in `20260709b` §2) — do not attempt.

---
