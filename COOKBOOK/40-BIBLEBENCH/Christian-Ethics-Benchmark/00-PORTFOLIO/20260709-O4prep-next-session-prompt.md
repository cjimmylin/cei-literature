# WALKWORTHY — Paste-Ready Boot Prompt for the Next Session (O4-prep: P0 pilot on OpenRouter)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Model: Opus** (`/model opus`). This is a clear-spec BUILD + RUN session (panel runner + the
P0 pilot on the validated OpenRouter measurement path), not judgment work. **Reserve the closing
Fable window (~to 2026-07-11) for the session AFTER this one** — adjudicating the P0 pilot's real
cross-model data vs the frozen §3 gates + ruling PR-3 + choosing/validating judge models. Copy the
block below into a fresh Opus session.

---

```
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) — Session O4-prep: build the multi-model PANEL RUNNER and run the §1 P0 PILOT (3 models × 5 items/design) on OpenRouter (the validated measurement path). EXECUTION mode: runnable code + a real pilot dataset + report, not a plan.

SCOPE LOCK: stay entirely within CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Do NOT touch, read for design input, or import from any sibling bench (WCF-Bench, FruitBench, CookBook, SermonMount, CorinthLove, DUPLEX, INNOVATION). Differentiate only vs published literature ([[biblebench-scope-isolation]]).

START by reading, in order:
1. 00-PORTFOLIO/20260709-O3-session-handoff.md — harness + O3 live-wiring state, findings M-1..M-5, PR-1..PR-4.
2. 00-PORTFOLIO/20260709-openrouter-pilot-report.md — the OpenRouter measurement path (DONE, validated, cost model, the judge-agreement finding).
3. 00-PORTFOLIO/20260709-O3-smoke-10design-report.md — all-10-design mechanics smoke (0 defects).
4. The authority stack: master plan §1 (P0 pilot spec) + §3 (frozen gates) + §3.3 (capability battery) + §3.4 (judge-validity gate); the normative charter (§6.5 cross-family judges, §6.6 holdout); harness/README.md.

AUTH / MEASUREMENT PATH: OpenRouter (a real paid API — NOT the subscription CLIs, which were smoke-only). Key at ~/.codex/secrets/openrouter.env (gitignored; loaded by walkworthy.openrouter_backend.load_openrouter_key; NEVER print/commit it). Cross-vendor through one key. ~$16 for a 3-model P0 pilot; a 6-model full-panel is ~$32 — cost is not a constraint.

BUILD (TDD; recorded-transport tests only, no live call in the suite):
- A resumable PANEL RUNNER (generalize smoke.run_smoke or add run_panel): all 344 runnable PUBLIC items × N SUT models; per-(item,model) checkpointing so a killed run resumes; IDs-only manifest + FIXED permutation seeds; cost-tracked (OpenRouter usage.cost). Reuse the validated pipeline (execute_item/score_item/_run_05_allocation/judge_item) unchanged; only fan out over models + items.
- Loader loads PUBLIC only (HARD-REFUSES HOLDOUT). No temperature/top_p/top_k (reasoning models 400).
- Judge JSON parsing + four-way refusal + strict-05 + branch classifier are already proven live across Claude/GPT/Gemini — do NOT re-litigate; wire, don't redesign.

RUN the P0 pilot (master plan §1): 3 SUT models (cross-vendor, e.g. one small + one mid + one frontier via OpenRouter slugs) × 5 items/design across all 10 designs. Judges = 2 cross-family models, both ≠ the Claude generator family (charter §6.5) — the O3 defaults were openai/gpt-5.6-terra + google/gemini-3.5-flash. FIX MECHANICS ONLY: do NOT edit items from model performance (contaminates difficulty calibration). Anything judgment-shaped → 00-PORTFOLIO/PENDING-RULINGS.md, parked.

ALSO (informs O4 judge selection, cheap): run a small JUDGE-PAIR COMPARISON — 2–3 candidate cross-family judge pairs scoring the SAME fixed set of pilot transcripts — and report per-design agreement. The O3/pilot data already flagged this is fragile (07 cross-family agreement hit 0.00 on a weak SUT). This is DIAGNOSTIC for O4; final judge choice + the §3.4 human-label validation are Fable/Jimmy items — do NOT finalize judges here.

DO NOT (parked — Fable/Jimmy, not this session):
- PR-3 ruling (refusal tagger ignores keyed_outcome; + the keyed_outcome-from-verdicts[0] coupling flagged in the pilot report).
- 06/09 matched-quality REFERENCE ANSWERS (M-3) — reference-anchored designs can't be neutrality-gated without them; run 06/09 in the pilot against the keyed anchor only and LABEL it provisional.
- ~60-item/design HUMAN LABELS for the §3.4 judge-validity gate.
- Final panel/model + release decisions.
Label ALL pilot numbers "P0 pilot — judges unvalidated (§3.4 pending); not a certified measurement."

REPO DISCIPLINE: ≥3 concurrent sessions share this git index — `git log -1` before staging, stage WALKWORTHY paths explicitly, never rewrite sibling commits. New reports = new YYYYMMDD- files (Report Immutability — never overwrite 20260709 runs/reports). No deletions (mv to RECYCLE-BIN/). runs/*/scored_items.jsonl gitignored. Checkpoint-commit after each component. Use the vault venv python (`../../../../.venv/bin/python`; `python` is NOT on PATH).

END WITH: run_panel code + tests, the P0 pilot dataset (runs/YYYYMMDD-p0-pilot/) + report + judge-pair comparison, a new dated handoff, a memory update, and a final commit. Next = a FABLE session (while the window is open, ~to 07-11): adjudicate the P0 pilot's real cross-model spread + judge-disagreement vs the frozen §3 gates, rule PR-3, choose+design-validation-for judge models, and design the §3.4 human-label protocol.
```

---

**Notes for Jimmy (not part of the prompt):**
- **Model = Opus** for this session (build + run; the Fable-week protocol sends execution to Opus).
- **Then Fable, within the window (~to 07-11):** the P0 pilot produces the first real multi-model
  data; adjudicating it + ruling PR-3 + choosing/validating judges + designing the human-label gate
  is the judgment-heavy work worth the closing Fable window. If you'd rather flip the order and spend
  your last Fable days on judgment FIRST (design the judge-selection experiment + human-label protocol
  + pre-register the panel, delegating execution to Opus subagents), that's defensible too — but the
  pilot data makes those calls sharper, so Opus-first is recommended.
- **Still owed by you regardless of order:** the ~60-item/design human labels (§3.4), the PR-3 ruling,
  and 06/09 reference answers (M-3). None are code; none are unblocked by OpenRouter.
```
