# WCF-Bench — Next-Session Boot Prompt (paste this to start the session)

> **Model: OPUS main loop** (`/model opus`). This is a build session — the Phase-3
> runner + examinee-prompt builder + response parser, from a clear spec, then a
> small live pilot. No Fable-tier judgment is queued here. **Reserve Fable** for the
> downstream task it is uniquely for: adjudicating the first real pilot's
> judge-disagreement clusters (a separate, later session — do it before the Fable
> window closes ~2026-07-11). Delegate mechanical sub-tasks (searches, variant
> authoring) to Sonnet/Haiku subagents with an explicit `model=`.

> **Scope lock: WCF-Bench ONLY.** Work stays inside `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/` (+ read-only `../WCF/` sources). Do NOT read/touch WALKWORTHY, INNOVATION, COOKBOOK/20-DESIGNS, or any sibling bench — the shared git index is LIVE with concurrent sessions (HEAD moved ~5× last session). `git log -1` before every commit; stage this project's paths explicitly; never `git add -A`. Keep benches un-cross-wired ([[biblebench-scope-isolation]]) — note WALKWORTHY independently built its own OpenRouter backend; do not merge them.

---

Continue the WCF-Bench project (Westminster-Standards values-alignment benchmark suite).

**First — read, in order:**
1. The memory note `wcf-bench-portfolio-state` (sessions 5 + 5b are the current state; the Phase-2 harness + expansion-2 YAML bank + the live OpenRouter backend all landed).
2. `20260709e-wcf-session-handoff.md` — session-5 execution summary (its "next queue" §2 predates the OpenRouter backend, so items about "cross-family clients" are now DONE; the rest stands).
3. `04-HARNESS/README.md` §"Phase 2 TODO" — the authoritative done/remaining list (**125 pytest green**).
4. `04-HARNESS/openrouter_smoke.py` + `04-HARNESS/wcfbench/openrouter_client.py` — the live backend + the hand-wired 2-item smoke this session builds on.
5. `00-OVERVIEW/20260706-shared-spine.md` §4 (scoring), §5 (perturbations), §10 (schema) — FROZEN.

**Current state (true as of session 5b, commit `87393657b`):**
- Harness Phase-2 COMPLETE + tested (loader, all mechanical scorers, judge infra + G4 battery, NARROWGATE episode state machine + defect-baseline calibration, triaxial). 125 pytest green, 0 network in tests.
- **Item bank:** `05-BANK-YAML/` = expansion-2 batch, **69/230 items**, lint-loads clean (the earlier ~161 items are prose-only — the documented mechanical remainder).
- **Real backend LIVE:** `OpenRouterModelClient` (one key → many families) is smoke-validated on real tokens across OpenAI/Anthropic/Meta. Key at `~/.codex/secrets/openrouter.env` (`source` it before live runs; NEVER commit it).

**The work, in order (mock-first, TDD, keep `04-HARNESS/tests/` green):**

1. **Examinee-prompt builder** — `ItemRecord → (system, user)` prompts: Track A (own-conduct framing) vs Track B (advisory), tier-appropriate, with a per-scorer **output-format contract** (ordinal → a `RANKING:` line; anchor → a cite-the-clause ask; refusal-gold items framed honestly) — WITHOUT leaking the gold/rubric into the prompt. A tested module (not the smoke's inline version).
2. **Robust response parser** — tolerant of real-model format variation (this session's lesson: claude-3-haiku wrote `RANKING: (a) < (b) < (c)`, not bare `a < b < c`). Extract rankings, verdicts, cited-anchor tokens; test against the observed formats. This is load-bearing — a brittle parser silently corrupts every score.
3. **Phase-3 runner** — `run(bank, models) → per-item ScoredItems → ReportingTensor`. Routes each item to its scorer by design/type (aggravate→ordinal, prooftext→anchor, narrowgate→episode, refusal co-score everywhere, triaxial on open responses via the judge path), records usage/cost, handles per-model + per-item errors without aborting the run. Mock-tested end-to-end first.
4. **Small live pilot** — a handful of items × 2–3 families through OpenRouter; validate the whole chain, cost, and sane numbers; **run the NARROWGATE defect-baseline on a LIVE model** (spine's Phase-2→3 gate: prove the harness detects a real defector before trusting a null). Resolve model IDs against `https://openrouter.ai/api/v1/models` (slugs drift — several 404'd last session).
5. **Stretch / next session:** perturbation-variant materialization (feed the flip-rate engine) + wire real OpenRouter judges and **run the G4 calibration battery on them (discard miscalibrated judges before trusting any judge score)**.

**Do NOT attempt (Jimmy-blocked / rulings):**
- **The OpenRouter-as-sanctioned-path ruling** — OpenRouter is a proxy; WCF keeps it **smoke/pilot-scale** until Jimmy rules whether it is the sanctioned path for the gated G1–G7 run (WALKWORTHY treats it as a measurement path — divergence for Jimmy to reconcile at the vault level).
- The G6 confessional panel (gold labels + the 4 `[DISPUTED]` confirmations + R1/R3/R4 + R20/R21 demote decisions); the MEND-C3-W202 attorney check.
- Do NOT relitigate rulings R1–R23. Do NOT transcribe the earlier waves unless explicitly asked (it's queued but item 2's runner is the higher-leverage unlock).

**Hard rules:** Westminster texts in `../WCF/` are the ONLY normative sources. No deletions (`mv` to RECYCLE-BIN). Report immutability (new dated files only). Frozen surfaces (spine, registry, R1–R23) change only via `[NEEDS-RULING]`. Canary `WCFBENCH-CANARY-c1647-x9k4q` once per released file; do not re-mint. Secrets never committed — `source ~/.codex/secrets/openrouter.env` at runtime only. End with a new dated handoff + atomic commit(s) + push.
