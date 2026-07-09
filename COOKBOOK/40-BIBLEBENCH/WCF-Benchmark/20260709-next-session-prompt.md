# WCF-Bench — Next-Session Prompt (paste this to start the session)

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First action — read the handoff, it governs everything:**
`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/20260709-next-session-handoff.md`

Then, before writing anything, load in this order:
1. `00-OVERVIEW/20260706-shared-spine.md` (binding methodology)
2. `00-OVERVIEW/20260706-westminster-anchor-registry.md` (citation rules + the Q1–113 source-split sharp edge)
3. `20260706-fable-review-memo.md` + `20260707-fable-review-addendum.md` (binding rulings R1–R7 — do not relitigate)
4. `03-OPUS-GUIDE/20260706-item-authoring-guide.md` (binding authoring protocol)

**This session's work, in order (details in handoff §4):**
1. Deck visual check via local HTTP + Playwright (`02-DECK/`).
2. Flesh-out batch 1: expand item banks by imitating the wave-2 Fable exemplars in `01-DESIGNS/exemplars-wave2/` — each exemplar ends with an "Opus note" that is its flesh-out recipe. Start with designs 03 AGGRAVATE → 10 NARROWGATE → 07 PROOFTEXT. New items go in NEW dated files under `01-DESIGNS/expansions/` (never edit existing files). Check spec §6 + wave-2 file + expansion file for scenario collisions before authoring each design.
3. If capacity remains: begin the mock-first harness skeleton per `00-OVERVIEW/20260706-build-plan.md` Phase 2, in a new `04-HARNESS/` directory. NO live API calls — the vault has no keys.
4. Close: new dated session handoff, atomic commit (this project's paths only; check `git log -1` first — parallel sessions share the index), push.

**Hard rules:** Westminster texts in `../WCF/` are the only normative sources; grep-verify every anchor (Q1–113 via `LargerCatechismwithScriptureProofs1 copy.txt`); no cross-referencing sibling benches; no deletions; `[NEEDS-RULING]` for anything a registry clause can't ground — never guess a key. Items blocked on Jimmy (API keys, G6 rater panel, rulings R1/R3/R4, attorney check on MEND-C3-W202) are listed in handoff §5 — do not attempt them.

---
