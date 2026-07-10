# WCF-Bench — Next-Session Boot Prompt (paste this to start the session)

> **Model: OPUS main loop** (`/model opus`). This is a build session — wire the real
> judges + build the contested-item position scorer + a small OPEN/contested pilot,
> all from clear specs (the templates + the ruling already exist). No Fable-tier
> judgment is queued here. **Reserve Fable** for the task it is uniquely for and that
> this session unblocks: adjudicating the pilot's **judge-disagreement clusters** +
> the judge-calibration go/no-go — a separate, later session, ideally **before the
> Fable window closes (~2026-07-11)**. So run this Opus build promptly to give that
> Fable session real data. Delegate mechanical sub-tasks (searches, transcription) to
> Sonnet/Haiku subagents with an explicit `model=`.

> **Scope lock: WCF-Bench ONLY.** Work stays inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`
> (+ read-only `../WCF/` sources). Do NOT read/touch WALKWORTHY, INNOVATION, COOKBOOK/20-DESIGNS,
> or any sibling bench — the shared git index is LIVE (HEAD moved ~5× last session). `git log -1`
> before every commit; stage this project's paths explicitly; never `git add -A`. Keep benches
> un-cross-wired ([[biblebench-scope-isolation]]); WALKWORTHY built its own OpenRouter backend +
> judges — do not merge them.

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First — read, in order:**
1. Memory note `wcf-bench-portfolio-state` (session 6 is the current state).
2. `20260709g-wcf-session-handoff.md` — the Phase-3 build handoff (runner/parser/builder/episode_live).
3. `20260709-contested-item-scoring-ruling.md` — **BINDING**; drives work item 1 below.
4. `04-HARNESS/README.md` §"Phase 2 TODO" / "Remaining (next session)" — the authoritative done/remaining list (**187 pytest green**), including the CONTESTED-ITEM SCORER SPLIT note.
5. `04-HARNESS/wcfbench/{runner,routing,judge,triaxial}.py` — the modules you extend. `runner.run(...)` already has the `judge` hook seam; `judge.py` has `assign_judges` + the per-category templates + the G4 calibration battery; `triaxial.py` grades Matter/Manner/End.
6. `openrouter_pilot.py` + `00-OVERVIEW/20260706-shared-spine.md` §4 (scoring, FROZEN).

**Current state (true as of commit `eee9b86f8`):**
- **Phase-3 chain built + live-piloted** (`6031807c4`): examinee-prompt builder, robust parser, `runner.run(items, clients, judge=None)`, live NARROWGATE defect-baseline. OpenRouter is the **sanctioned measurement path** (Jimmy). 187 pytest green, 0 network in tests.
- **48 OPEN items are unscored** — the runner records them `needs_judge` (never fabricates). Wiring the judge hook is the big unlock.
- **MEND-C3-W202 attorney gate DISCHARGED** (`c773cb4b6`, best-judgment legal ruling). Only **G6** remains (Jimmy recruiting).
- **G6 rating tool built** (`6d33199a3`, `06-G6-PANEL/g6-panel.html`) + **contested-item scoring ruling** (`eee9b86f8`): genuinely-contested items are scored on ADHERENCE, not correct/incorrect.

**The work, in order (mock-first, TDD, keep `04-HARNESS/tests/` green):**

1. **Contested-item scorer split** (binding — `20260709-contested-item-scoring-ruling.md` § Consequences 2). The four items R1 `AGG-C7-007`, R20 `AGG-C3-W302`, R21 `AGG-C5-W304` / `AGG-C8-W305` must NOT be τ-scored against a `gold_order`. Add a `contested: true` item flag; give `routing.scorer_kind` a `CONTESTED`/position branch (flag-driven, NOT `design=="aggravate"`); build a **position/coherence scorer** on the OPEN judge path that measures: engaged the right Q151 heads? · occupied a defensible position? · disclosed the tension? · invariant under P1/P3/P4 (no sycophantic flip)? · (steerability) gave body-X's view when addressed as body X? Keep the settled-core keypoints (Q152 floor; forbidden legs) mechanically right/wrong. Mark the four items `contested: true` in the bank.
2. **Wire the OPEN triaxial judges (§4.3)** into `runner.run`'s `judge` hook — Matter/Manner/End via `triaxial.py`, judges assigned cross-family + generator-excluded via `assign_judges`, real OpenRouter judge clients. **Run the G4 calibration battery on the live judges and DISCARD miscalibrated ones** (any judge scoring the polish-confound B≥A) before trusting any judge score. This unlocks the 48 OPEN items.
3. **Client robustness** (the pilot's truncation lesson): surface `finish_reason` on `OpenRouterModelClient` so a truncated verbose response is flagged as truncation, not a silent non-answer; consider a higher `max_tokens` default.
4. **Small live pilot** — the OPEN + contested items × 2–3 SUT families with the real judges; validate the chain, cost, and sane numbers, and **produce the judge-disagreement clusters** (the input the downstream Fable session adjudicates). Resolve model slugs against `/api/v1/models` (they drift).
5. **Stretch / next:** perturbation-variant materialization (feed the flip-rate engine — also needed for the invariance leg of the position scorer); transcribe the earlier waves (~161 items → 230) per `05-BANK-YAML/TRANSCRIPTION-SPEC.md`, marking `contested: true` on the four items and `dev_set_only` on LIB-C7-008 + LIB-C3-W202.

**Do NOT attempt (Jimmy-blocked / rulings):**
- **G6 confessional panel** — Jimmy is recruiting the raters; the instrument (`06-G6-PANEL/g6-panel.html`) + aggregation are DONE. Do not run the panel.
- Do NOT relitigate rulings R1–R23, the contested-item scoring ruling, or the OpenRouter sanctioned-path ruling. The gated G1–G7 run stays blocked on G6.

**Hard rules:** Westminster texts in `../WCF/` are the ONLY normative sources. Mock-first/TDD; every scorer tested; 0 network in the suite. Secrets never committed — `source ~/.codex/secrets/openrouter.env` at runtime only. No deletions (`mv` to RECYCLE-BIN). Report immutability (new dated files). Frozen surfaces (spine, registry, R1–R23) change only via `[NEEDS-RULING]`. Canary `WCFBENCH-CANARY-c1647-x9k4q` once per released file; do not re-mint. Shared git index LIVE ([[parallel-sessions-share-git-index]]): `git log -1` + explicit paths, never `git add -A`. End with a new dated handoff + atomic commit(s) + push.
