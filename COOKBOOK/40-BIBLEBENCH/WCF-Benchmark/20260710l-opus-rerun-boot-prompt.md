# WCF-Bench — Next-Session Boot Prompt (Opus build: R40 surgical re-run + R39(d) floor-gloss; paste after /model opus + /clear)

Continue WCF-Bench (scope-locked to `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/`). You are an
**Opus build session** executing the binding Fable memo
`20260710-fable-grok-ratification-floor-divergence-memo.md` (**R38–R41**, session 14 —
the governing doc; read it first, then the session-13 handoff `20260710j` for build
context). Headline state: grok-4.20 is RATIFIED as the second disclosure family (R30
condition 6 MET judge-side); the settled-core floor HOLDS at the sample level (the AGG-C8
aggregate 0.0 was adjudicated a judge+tie artifact); **nothing is model-blocked** — this
session is pure execution.

## Ordered worklist (from the memo's handoff section)

1. **R40.1 pre-flight:** source `~/.codex/secrets/openrouter.env`, check the key's
   limit/usage (`GET /api/v1/auth/key`). The floor-rerun deepseek 403s were
   `"Key limit exceeded"` (a key/credit condition, NOT provider routing). If the limit
   needs raising or a top-up → STOP the live half and surface to Jimmy; the harness fixes
   (item 2) can still proceed.
2. **R40.2–.3 harness fixes (mock-first, TDD, 366 green baseline):**
   - Retry-seam extension: one retry + short backoff on JSONDecodeError/unparseable
     verdict, empty emission, HTTP 402/403/429; post-retry failure recorded as
     `fail_transport_after_retry` (keep the `judges_discarded` record).
   - Settled-core keypoint tie among eligible judges → UNGRADED (`None`) + escalation
     flag, never a silent False (`judge_panel.py:360`).
3. **R40.4 surgical re-run (LIVE, ~cents; main loop, not a subagent shell):**
   persisted-text-first — (a) re-grade grok ONLY on the persisted AGG-C8-W305×llama
   response from `07-PILOTS/20260710-floor-rerun/transcripts.jsonl` (NO new SUT call);
   (b) re-grade all 3 judges on the persisted deepseek WHOLE-C9-W301 response; (c) fresh
   deepseek SUT calls ONLY for AGG-C3-W302/AGG-C5-W304/AGG-C8-W305; (d) llama arm NOT
   re-run. New dated run dir (append-only; `20260710-floor-rerun/` frozen). Combined
   manifest `07-PILOTS/20260710-third-family-screen/20260710-third-family-manifest.json`
   reused UNCHANGED — run this BEFORE any template edit.
4. **R40.5:** recompute the floor reading sample-level per R39(e) (raw aggregate = screen;
   any settled-core False → sample-level review before a floor claim); grok's parse
   behavior on the slice = the R38(3)(ii) ratification-confirmation data (≥2 post-retry
   parse losses reopens R38). Short dated report.
5. **R39(d) floor-gloss + settled-core probe (AFTER the re-run, it changes the prompt):**
   add the floor-gloss to the settled-core judge prompt (no-collapse = lazy-equivalence
   only, NOT principled decline-with-differentiation; Q152 = floor, not a calculus); mint
   the settled-core probe fixtures (persisted AGG-C8×llama → {kp1 correct, kp2 correct};
   persisted AGG-C3×llama → {floor correct}; synthetic true-collapse → {kp1 wrong}); add
   the settled-core prompt to `current_template_hashes()`; re-qualify the settled-core
   surface for all 3 judges (K=8, ≥5/8). Judge-side calibration only — no gold, examinee
   blind.
6. Then §5 transcription (session-11 handoff §3 protocol) or park with a handoff.

## Guardrails

Report immutability (new dated dirs/files only; never re-score a frozen dir). Canary
`WCFBENCH-CANARY-c1647-x9k4q` not re-minted. Shared git index LIVE (`git log -1` before
every commit; explicit paths; never `git add -A`; sibling dirty files off-limits). Secrets
sourced at runtime, never committed. No `rm` — `mv` to `RECYCLE-BIN/`. Live runs from the
session main loop. End with a dated handoff + update the `wcf-bench-portfolio-state`
memory note.

## Still Jimmy-blocked (surface, don't attempt)

G6 confessional panel (gates the gated G1–G7 run, H-DISC promotion — judge-side condition
now met, W304/W305 position maps, 4 LIB `[DISPUTED]` legs); OpenRouter key top-up if
pre-flight fails.
