# WALKWORTHY — Session O4-prep Handoff (2026-07-09, Opus)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Purpose:** re-entry doc after **Session O4-prep (multi-model PANEL RUNNER + the §1 P0 PILOT)
COMPLETE**. Supersedes the O3 handoff's "O4 needs the sanctioned API on both vendors" — the
OpenRouter measurement path + this pilot make the full panel a scale + human-labels question,
not an integration one. Next = a **FABLE** session: adjudicate the pilot vs the §3 gates, rule
PR-3, choose+validate O4 judges, design the §3.4 human-label protocol.

---

## 1. What O4-prep built (the pipeline is UNCHANGED — this is fan-out + bookkeeping)

The per-item pipeline (`_run_05_allocation` / `execute_item` / `score_item` / `judge_item`) was
already client-agnostic and tested; O4-prep only fans it over N SUT models and adds bookkeeping.

- **`walkworthy/panel.py`** (new) — the multi-model panel runner:
  - `select_panel_items(all_items, items_per_design)` — deterministic first-N-by-id per design
    (reproducible from the manifest's IDs); `None` → the full O4 split.
  - `run_panel(...)` — fans the pipeline over `sut_clients × items` with:
    (a) **per-`(item,model)` checkpoint + resume** — `scored_items.jsonl` IS the checkpoint;
        a killed run re-reads it, skips completed cells, continues (no re-call, no dup);
    (b) **cost tracking** — each item's real `usage.cost` delta on its record (`_panel_cost`),
        run + per-model totals summed from records (**resume-safe**);
    (c) **per-cell error handling** — a bad response (e.g. empty content) is logged as data
        (`panel_errors.jsonl` + `top.errors`) and the batch continues; the cell retries on resume;
    (d) aggregation → per-`(design,model)` cells, descriptive spread, judge-pair agreement,
        refusal accounting, cost → `panel_summary.json` + `panel_report.md`.
  - `main()` — `python -m walkworthy.panel --sut-models a,b,c --items-per-design 5 ...` (OpenRouter).
- **`manifest.build_manifest(..., items=)`** (additive) — a pilot manifest records the *selected*
  subset (50 IDs), not the whole 344 split.
- **`walkworthy/README.md`** — documents the OpenRouter measurement path + the panel runner.

**Tests: 145 → 159 pytest green** (+1 manifest, +13 panel; recorded-transport / mock only, NO
live call in the suite). `cd harness && …/.venv/bin/python -m pytest tests/ -q` → **159 passed**.

## 2. O4-prep DELIVERABLE — the §1 P0 pilot (first real cross-model data)

`runs/20260709-p0-pilot/` (merged) + curated report `00-PORTFOLIO/20260709-p0-pilot-report.md`.

- **3 cross-vendor SUTs × 5 items/design × 10 designs** = 150 cells, on OpenRouter.
  SUTs: `meta-llama/llama-3.1-8b-instruct` (small) · `deepseek/deepseek-chat` (mid) ·
  `mistralai/mistral-large-2512` (frontier). Judges: `openai/gpt-4.1-mini` +
  `google/gemini-2.5-flash` (cross-family, both ≠ the Claude generator).
- SUTs deliberately avoid the judge families AND the generator family (no self-preference /
  home-advantage confound in the first dataset).
- **150 records · 0 schema errors · 0 unresolved cell errors · 2 judge defects (of ~1,000
  cells) · overall judge agreement 0.65 · $0.63.** Result: deepseek-chat (75.9) ≈ mistral-large
  (71.1) ≫ llama-3.1-8b (51.7) on the mean per-design scalar; spread ≥15 on 7/10 designs;
  judge agreement lowest on the per-turn designs 02 (0.43) / 07 (0.49). See the report §1/§4.
- **DESCRIPTIVE / PRE-GATE** — the §3.4 human-label gate is not run, so no number is a benchmark
  result. FIX-MECHANICS-ONLY respected (no item edited from performance).

## 3. Two findings that shaped the run (both mechanics)

- **F-1 (judge tier):** frontier judges (`gpt-5.6-terra`) made per-turn designs (02/07, ~30
  calls/cell) project to *hours*; NOT rate-limiting (0× 429 instrumented) — it's SUT multi-turn
  generation + frontier-judge latency. Fixed with fast mid judges (`gpt-4.1-mini` + `gemini-2.5-flash`)
  + **per-SUT parallelism** (3 separate resumable runs, merged). Judge *choice* is the §3.4 gate's
  job, so pilot judge tier is a speed call, not a validity one.
- **F-2 (dead SUT):** `qwen/qwen-2.5-72b-instruct` returned `empty content (finish=None)` on
  45/50 cells via this OpenRouter provider → dropped, replaced with `deepseek/deepseek-chat`
  (probed reliable). Motivated **F-3: per-cell error handling** so one bad response can't kill a run.

## 4. Pending rulings (Jimmy / Fable-only) — `00-PORTFOLIO/PENDING-RULINGS.md`

- **PR-1 / PR-2** (O2) — unchanged. **PR-3** (O3) — refusal tag + `verdicts[0]` keyed-outcome
  coupling; the pilot's judge-divergence cells make this live. **PR-4** (O3) — pilot sequencing;
  this pilot substantially discharges the "run the P0 pilot" step (recommend ratify).
- **New (O4-prep):** an **empty-content-retry / provider-routing** backend enhancement is
  recommended before a long O4 panel (F-2) — a mechanics decision, parked for the O4 build.

## 5. Auth / measurement path (unchanged pins)

- **OpenRouter** = the measurement path: one key at `~/.codex/secrets/openrouter.env` (gitignored;
  `openrouter_backend.load_openrouter_key`; NEVER printed/committed). Cross-vendor via one key.
- Cost is not a constraint: this 150-cell pilot cost **$0.63** (1,254 calls); the full 344-item
  ≥6-model O4 panel is tens of dollars.
- Subscription CLIs remain smoke-only (ToS); the keyed SDK adapters in `clients.py` are moot for
  measurement (OpenRouter covers all vendors).

## 6. Next = Session O4 / the FABLE window (~to 07-11)

1. **Adjudicate** the pilot's real cross-model spread + judge-disagreement vs the frozen §3 gates
   (spread ≥15 / headroom <85% / capability ρ≤0.40 / κ). Descriptive numbers are in the report §1/§4.
2. **Rule PR-3** (refusal semantics + `verdicts[0]` coupling).
3. **Choose + validate O4 judge models** (validate against human labels BEFORE trusting any score).
4. **Design the §3.4 human-label protocol** (~60 items/design, stratified) — the long pole.
5. Then the O4 **build** (Opus): the empty-retry/provider backend, 06/09 reference answers (M-3),
   the ≥6-model full-split panel via `run_panel` (drop `--items-per-design`), all §3 gate stats.

## 7. Standing cautions (unchanged)

- **≥3 concurrent sessions share this git index.** Always `git log -1` before staging; stage
  WALKWORTHY paths explicitly; never rewrite sibling commits.
- No deletions (mv to RECYCLE-BIN); `HOLDOUT/` + `runs/*/scored_items.jsonl` gitignored; new
  reports = new `YYYYMMDD-` files. Loader HARD-REFUSES HOLDOUT (charter §6.6).
- Re-entry ignition for O4/Fable: this handoff + `20260709-p0-pilot-report.md` + the master-plan
  §1/§3 authority stack + the O3 handoff (harness lineage).

## 8. Commit
`8ca291d31` — WALKWORTHY O4-prep: panel runner + §1 P0 pilot (150 records). Staged WALKWORTHY
paths explicitly (sibling sessions share the index — [[parallel-sessions-share-git-index]]);
`scored_items.jsonl` gitignored/regenerable. The 3 per-model + qwen source runs are committed
for audit (qwen's `panel_errors.jsonl` is the F-2 evidence).
