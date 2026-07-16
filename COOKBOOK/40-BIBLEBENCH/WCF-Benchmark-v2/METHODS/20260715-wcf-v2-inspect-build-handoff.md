# Handoff — WCF-Benchmark-v2 built on Inspect AI (2026-07-15)

**Session scope:** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (new folder, created this session)
**Status at close:** COMPLETE for the session's goal — Inspect AI port built, offline-verified, and live-smoked. EXPLORATORY governance throughout.

## What Was Done

### 1. Design + user alignment (grilling)
Explored v1 (`WCF-Benchmark/`, 230-item YAML bank, abandoned bespoke harness) + `WCF/` source corpus + Inspect AI 0.3.246. User locked six decisions via two AskUserQuestion rounds: (1) all 226 runnable items; (2) simplest-viable scoring — everything through `model_graded_qa` vs key+rubric, no Kendall-τ/triaxial/refusal scorers; (3) episodes as a simple 2-turn scripted-pressure dialogue (the only custom solver); (4) fixed separate cross-family grader, temp 0, configurable; (5) mockllm first then ~$1 OpenRouter smoke; (6) lightweight restart — no gates/pre-reg, `.eval` logs are the audit trail.

### 2. Build (18 files, ~450 lines)
- `convert/yaml_to_jsonl.py` — bank → `data/wcf_main.jsonl` (204) + `data/wcf_episodes.jsonl` (22); routing precedence ported exactly from v1 `routing.py` (episode → contested → ordinal → anchor → open). Kind mix: 16 ordinal / 161 open / 4 contested / 23 anchor.
- `src/prompt_frames.py` — EXAMINEE_SYSTEM, Track A/B frames, RANKING/ANCHOR asks ported verbatim from v1 `promptbuilder.py`.
- `src/wcf_tasks.py` — `@task wcf_main` + `@task wcf_episodes`; grader as `-T grader_model=...` task arg; 0–100 numeric grade contract; `grouped(mean(), design/tier)` breakdowns.
- `src/episode_solver.py` — generate → generic scripted pressure turn → generate; grader sees full transcript (`include_history=True`).
- `tests/test_converter.py` — 5 tests (counts/leakage/schema/vocab/routing), all passing.
- Dedicated venv `.venv-v2` (Python 3.14.3) — the shared vault `.venv` is 3.9.6 and cannot run inspect-ai.

### 3. Verification + live smoke
mockllm end-to-end for both tasks ($0), then three live OpenRouter runs (SUT `openai/gpt-4o-mini`, grader `google/gemini-2.5-flash` @ temp 0): 15 aggravate items, 9 one-per-design items, 5 episodes. **29/29 samples produced parseable `GRADE: <0-100>` lines. Total cost ≈ $0.05.** Details: `reports/20260715-v2-live-smoke-report.md`.

## Findings

- **The Inspect port eliminates v1's entire harness-failure class.** 29/29 grade extraction on first attempt (v1: chronic parser drift, unscored cascades); resume/custody handled natively by Inspect (v1's open double-spend P1 cannot occur); full-bank single-SUT pass extrapolates to ~$0.40–0.60 (v1 T4 forecast: $278+).
- **Per-design spread is directionally consistent with the v1 design thesis** (n tiny, exploratory): gpt-4o-mini scored crosswind 9, complicit 30, prooftext 45 vs dutybound/mending/wholeheart 100 — gap-shaped designs resist saturation.
- **Episode grades bimodal on n=5** (0, 20, 100, 100, 100) — the generic pressure turn discriminates, but watch whether it is too blunt across all 22.
- **Data corrections vs prior documentation:** bank has 4 contested items (not 3); tiers are {T2,T2a,T2b,T3,T4} (no T1); `episode:` is a bare boolean (pressure scenario lives in stem prose).

## User Decisions (verbatim-anchored)

All six locked decisions listed in §1 above were explicit AskUserQuestion selections. Notably: user chose "All 226 runnable items" over the recommended 204-first, "Simplest viable" scoring over the recommended staged-fidelity, and "Simple 2–3 turn scripted dialogue" for episodes (resolving the all-items × simplest-scoring tension). OpenRouter key supplied via `~/.codex/secrets/openrouter.env` (user pointer).

## Remaining Work

- **P1 — Full 226-item pass** on 1–2 SUTs (~$1–2 at smoke prices). One command per task; consider `inspect eval-set` for multi-model + auto-resume.
- **P2 — Review episode pressure-turn bluntness** after full 22-episode run; per-item scripted turns are the v2.1 upgrade path if the generic turn saturates.
- **P3 — Staged-fidelity upgrades** (deliberately deferred): custom Kendall-τ scorer for the 16 ordinal items; per-axis rubric sub-scores; contested-item breakdown reporting; refusal taxonomy.
- **P4 — Grader robustness**: single grader now; `model_graded_qa(model=[...])` majority vote is a one-line upgrade when wanted.

## Open Decisions for Next Session

1. Run the full 226-item pass now, and on which SUT roster?
2. Adopt `inspect eval-set` multi-model comparison (which models, which grader)?
3. Does v2 ever inherit any v1 governance (pre-reg, quotability gates), and at what milestone?

## File Locations

| File | Location | Purpose |
|---|---|---|
| Tasks | `WCF-Benchmark-v2/src/wcf_tasks.py` | `wcf_main` + `wcf_episodes` Inspect tasks |
| Converter | `WCF-Benchmark-v2/convert/yaml_to_jsonl.py` | Bank YAML → JSONL (regenerable) |
| Datasets | `WCF-Benchmark-v2/data/*.jsonl` | 204 + 22 items |
| Grading template | `WCF-Benchmark-v2/src/templates/` | Template + numeric instructions |
| Smoke report | `WCF-Benchmark-v2/reports/20260715-v2-live-smoke-report.md` | First live results (EXPLORATORY) |
| Audit trail | `WCF-Benchmark-v2/logs/*.eval` | 5 Inspect logs (2 mockllm + 3 live) |
| Run instructions | `WCF-Benchmark-v2/README.md` | Env, commands, conventions |

## Known Issues

- **Parallel sessions on `main`:** remote was 57 commits ahead at handoff; zero collision with this scope (remote touched no `WCF-Benchmark-v2/` paths) — auto-narrowed to our files only. Out-of-scope uncommitted files exist (BIBLEBENCH-PILOT, ACTIVE-CRITICAL-PATHS.md, etc., from sibling sessions) and were NOT committed.
- **Log timestamps are UTC** (`2026-07-16T05:39` = 2026-07-15 local evening); report filenames use local date per vault convention.
- **`.venv-v2` (258 MB) and `.env` are git-ignored** — rebuild venv from `requirements.txt` on a new machine.
- **Metric scale**: all reported means are 0–100 (grader-normalized rubric points), NOT accuracies — the Inspect viewer column reads "mean".
- A sibling session ported another benchmark ("walkworthy") to Inspect today per memory index — potential convergence of patterns worth cross-reading later.
