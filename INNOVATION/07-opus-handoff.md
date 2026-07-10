# Opus Handoff — INNOVATION Execution Queue

**Written:** 2026-07-07 by Fable 5 (last planned Fable session of the window)
**For:** post-window Opus sessions (`/model opus`) · **Living doc:** checkbox-update in place (charter rule 1 exception)

## How to use this file

Work top-down within the current cycle. Every task names its tier — dispatch subagents with an explicit `model=` per the Fable-week/global tiering protocol (which remains good practice post-window: Sonnet/Haiku for mechanical work). Read the referenced RP brief *before* starting its tasks; briefs contain binding kill criteria (charter rule 2). When a task says "Fable-tier review," queue the artifact in a PENDING-RULINGS list per the succession-protocol pattern (`FRUITBENCH-REVIEWS/20260706-succession-protocol.md`) rather than self-approving — Jimmy adjudicates if no Fable window exists.

## Cycle 1 — key-independent (start immediately)

- [x] **1.1 Taxonomy codes (V2)** — **COMPLETE 2026-07-09: PR-01 RESOLVED (Jimmy: all 5 approved, option (b))**; patch + Stage-3 mirror applied to `classification-logic.md` (v1.5 row), validation 0 errors. Fable adjudication FC-1…FC-4.
- [ ] **1.2 Acquisitions (V1)** — **P1 DONE 2026-07-09: 17/17 anchors ingested** (4/4 ⚠ verified, 0 misses; log `40-BUILDS/20260709-p1-acquisition-log.md`; commit `296fdf0b6`). Remaining: (i) 2 non-arXiv P1 items (Anthropic blog posts "Teaching Claude Why" + "Agentic Misalignment") need print-to-PDF + manual records; (ii) P2 by gap group. Same rules: ⚠-verify before download, log misses. *Sonnet-tier batch work.*
- [x] **1.3 `fairgold` toolkit (RP-02 O2, T2)** — DONE 2026-07-09 (`40-BUILDS/rp02-fairgold/`, 49/49 tests, verified in-session). A1–A6 ratified; **FC-6 rider binds O1** (ranking-level disaggregation = inclusion criterion).
- [ ] **1.4 Position paper hardening (P3)** — draft-v0 DONE 2026-07-09 (`40-BUILDS/p3-position-paper/20260709-draft-v0.md`, 5,708 w, 0 VERIFIED / 23 SEARCH-CONFIRMED / 47 ⚠, ledgered; Fable screening FC-13…FC-15). Remains open: FC-15 spec-citation upgrade via RP-01 registries → 1.2-driven ledger upgrades (after PR-01) → pre-submission review before ANY external use.
- [x] **1.5 RP-04 O1 prep** — DONE 2026-07-09 (`40-BUILDS/rp04-corpus/`). **Headline: 0 real-model responses; RP-04 P2 fully key-gated** (FC-7). Strata + holdout rulings FC-8/FC-9; source-path erratum FC-10 (pilots live under `COOKBOOK/40-BIBLEBENCH/`).
- [x] **1.6 RP-01 O1** — DONE 2026-07-09 (`40-BUILDS/rp01-registries/`; Model Spec 2025-12-18 = 66 clauses, Constitution 2026-01 = 49; VERIFIED-class, SHA-256 stamped). Riders: FC-11 (O2 scores from anchors, not excerpts), FC-12 (re-verify currency at O2 start).

## Cycle 2 — keys arrive (Jimmy gate)

- [ ] **2.1 Shared runner (T1)** — one vendor-agnostic runner (Anthropic SDK + OpenAI; Gemini if key provided), caching + full transcript logging, rate-limit backoff from day one. Reuse THORNS harness spine patterns; respect its live-mode hard-block gates (S-1/S-2) for anything FRUITBENCH-derived. *Opus. This unblocks everything below.*
  - **2.1-provisional DONE 2026-07-09 (Fable session):** CLI-OAuth backends built + GO'd at `40-BUILDS/t1-runner-provisional/` (Anthropic `claude -p` + OpenAI `codex exec` WORKING with real tokens; Google BROKEN — tier retired server-side, Jimmy action). Governance: ruling `20260709d-…-provisional-ruling.md` (GREEN/YELLOW/RED lanes, `cli-oauth-provisional` provenance class, volume caps) + adjudication `20260709e-…-adjudication.md` (shim GO w/ conditions C1–C5; S1 machinery PASS, findings F1–F4 bind Cycle 2). S1 pilot report: `40-BUILDS/rp04-corpus/20260709-s1-pilot/`. API backends still drop in behind the same interface when keys land — the RED lane (subject-side headline runs) remains key-gated.
- [ ] **2.2 RP-07 HAWTHORNE run** — O1 item pairs (**Fable-tier gate on 20-pair sample before scale**) → O2–O4 → P1 short paper draft. *Opus; the Wave-1 flagship.*
- [ ] **2.3 RP-04 phase 1 run** — re-score frozen corpus with 3+ judge families → judge-bias memo (P2). **Pre-commit honored: if biases threaten published CEI verdicts, robustness pass on affected benches is mandatory, not optional.** *Opus.*

## Cycle 3 — strategic builds

- [ ] **3.1 RP-03 NOGOLD** — O1 item generation via CRUX engine + tiering → O2 harness → O4 dry-run at 30 items → **STOP: Fable-tier transcript review required before main run** (queue if no window). *Opus.*
- [ ] **3.2 RP-09 SEISMOGRAPH O1–O3** — trait-coverage matrix; short-form extraction + equivalence pilot; organism acquisition (needs GPU-inference budget sign-off — Jimmy gate). *Opus + Sonnet inventory.*
- [ ] **3.3 RP-01 O2–O3** — conflict/ambiguity harness + human-verification sample design (rater sourcing = Jimmy gate). *Opus.*
- [ ] **3.4 COOKBOOK cross-links (V3)** — new dated pointer notes in COOKBOOK (never edit existing reports); S1/S3 upgrade-path notes referencing RP-05/RP-10. *Sonnet.*
- [ ] **3.5 Stage-4 vocabulary reconciliation** *(added 2026-07-09, Fable FC-2)* — documented Stage-4 list vs live `research_topic` usage are out of sync ("Benchmarks & Datasets" used 0×; ≥8 live codes undocumented — see taxonomy proposal §9.2). New dated proposal + Jimmy sign-off (standards file). *Sonnet inventory, Opus proposal.*

## Cycle 4+ — long poles (start when their gates clear)

- [ ] **4.1 RP-05 DRIFTLAB** — after FRUITBENCH spine fixes land + runner exists; power analysis (O4) before any long runs.
- [ ] **4.2 RP-06 SAYDO** — O1 triplet authoring can start earlier (**Fable-tier gate on 30-item sample**); main run after runner.
- [ ] **4.3 RP-08 CONCLAVE** — O1 fidelity gates for 4–6 traditions first; **K1 is a hard gate — no deliberation runs until agents pass**. Non-negotiables registries (O4) queue for Fable-tier/Jimmy review.
- [ ] **4.4 RP-02 invariance study** — after O1 inventory identifies ≥3 usable disaggregated datasets (else brief's K2 downgrade applies).
- [ ] **4.5 RP-10 COMMONS** — after DRIFTLAB infra exists; pilot before scale (O4 budget curve).
- [ ] **4.6 Bet review (V4)** — 2027-07: score B1–B5 from `01-field-map-2026.md` §6 in a new dated note.

## Standing constraints (do not relax)

1. Kill criteria in RP briefs are binding; execute mechanically; softening requires Fable-tier/Jimmy ruling.
2. Judge-corruption caveat (G-09) cited in methods of every judge-using study.
3. Report immutability everywhere; INNOVATION updates are new dated files (except this queue's checkboxes).
4. No `rm` — RECYCLE-BIN only (hook-enforced). Validate YAML after any batch paper edits (`PYTHON/validate_all_papers.py`).
5. Synthetic-data caveats travel with all RP-08 Phase-A and any MockModel outputs — never present harness-validation as measurement (the SERMONMOUNT lesson).
6. Anti-leakage discipline for cross-vendor comparisons (`dispatching-parallel-agents` skill norms).

## Jimmy's gate list (blocking, in priority order)

1. **API keys** (Anthropic + OpenAI min; Gemini ideal) — blocks Cycle 2 entirely.
2. **GPU-inference budget** (rented endpoints; no training) — blocks RP-09 validation + RP-04 phase 2.
3. **Human raters/panels** — blocks RP-01 O3, RP-08 Phase B.
4. **D6 licensing decision** (evidence-card corpus release) — blocks nothing; unlocks a cheap high-visibility artifact.
5. **C1 workshop decision** — only after P1–P3 exist.

## Known issues / honesty notes

- Sweep-derived citations: top anchors fetch-verified; secondary items search-confirmed only; ~25 ⚠ IDs in `04-missing-literature.md` need confirm-at-download. Nothing ⚠ goes into external prose unverified.
- The gap atlas's grep-count evidence is directional, not exhaustive (title/abstract matching undercounts).
- 2026 arXiv IDs from sweeps (26xx.*) could not be independently re-verified this session; the missing-lit agent flagged them rather than dropping them.
- This folder was authored in one Fable session; the field map's §6 bets are the built-in error-correction mechanism — keep the 2027-07 review.
