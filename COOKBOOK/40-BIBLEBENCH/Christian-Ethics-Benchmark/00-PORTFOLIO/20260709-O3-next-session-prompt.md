# WALKWORTHY — Paste-Ready Boot Prompt for Session O3 (live pilot P0)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
Run this session on **Opus** (`/model opus` if needed). O3 is live-wiring + a small mechanics
pilot — clear-spec code, fix-mechanics-only (no perf-driven item edits). Do NOT spend a Fable
window on it; reserve Fable for adjudicating the first REAL panel against the frozen gates (O4/O5).
Copy everything in the block below into a fresh session.

---

```
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) — Session O3: first LIVE pilot (P0).

START by reading, in order:
1. CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/00-PORTFOLIO/20260709-O2-session-handoff.md
   — current state (harness DONE, mock-first, 88 pytest green), authority stack, O3 scope (§6),
   auth (§7), pending rulings (§4), known caveats (§5).
2. The authority stack it names in §2 — master plan §1 (O3 = Pilot P0 spec) + §3 (frozen
   pre-registered gates), the normative charter (construct / strata / reporting spine), the item
   playbook (four-way refusal taxonomy).
3. harness/README.md — the "Auth" and "O3 wiring" sections (the exact checklist) + the layout.

THEN wire live mode and run the pilot (EXECUTION mode — runnable code + a REAL pilot report, not a plan):
- Wire the SDK call in clients.AnthropicAdapter, plus ONE non-Anthropic family for the cross-family
  judge pair. Credentials: a key OR OAuth both work and the adapters already accept either — Anthropic
  a bare `anthropic.Anthropic()` resolves an `ant auth login` profile and hits the raw /v1/messages
  API; OpenAI via the Codex OAuth CLI. ASK Jimmy which he set up before writing vendor-specific code.
- Add real Judge subclasses (subclass judges.Judge) that call a model and PARSE the JSON verdict — the
  rubric prompt is already assembled by judges.assemble_rubric_prompt. Enforce 2 cross-family judges,
  log disagreement per cell, NEVER average (the layer already does this — keep it).
- Replace executors.default_state_classifier with a judge-backed per-turn state classifier for the
  scripted multi-turn designs (02 complied/refused, 07 validated/challenged/deflected).
- Run the pilot per master plan §1: 3 models × a 5-items/design PUBLIC-split subset (runnable items
  only). Shake out real parsing, refusal tagging, the strict 05 allocation-block parser + one-retry,
  and branch selection (02/07). Log every mechanical defect.
- Deliver: a NEW dated pilot report `00-PORTFOLIO/YYYYMMDD-O3-pilot-report.md` + the run written to
  `runs/YYYYMMDD-o3-pilot/` (manifest + summaries committed; large jsonl gitignored, per O2).

Ground rules for this session (frozen):
- FIX MECHANICS ONLY. Do NOT edit items based on model performance — that contaminates difficulty
  calibration (master plan §1). Anything judgment-shaped → 00-PORTFOLIO/PENDING-RULINGS.md, parked.
- Load the PUBLIC split ONLY (loader HARD-REFUSES HOLDOUT, charter §6.6). Manifest stays IDs-only;
  permutation seeds stay FIXED constants — never runtime-generated.
- Do NOT send temperature / top_p / top_k to Opus 4.7+/Fable judges or SUTs — they 400 (adaptive
  thinking only). Control depth with output_config.effort; pin decoding via prompt, not sampling.
- AUTH/ToS reality (sibling WCF-Bench finding + [[vault-no-live-llm-runner]]): CLI-OAuth is fine for a
  SMALL pilot smoke-run, but a full gated O4 panel should use the sanctioned Messages API path (ToS).
  Keep O3 to the 3-model pilot; do NOT scale to the ≥6-model full panel this session.
- Keep the mock path working (88 pytest green stays green). Add tests for the live-wiring seams using a
  RECORDED/stubbed transcript — never a live network call in the test suite.
- Repo discipline: this worktree has ≥3 concurrent sessions — `git log -1` before staging, stage
  WALKWORTHY paths explicitly, never rewrite sibling commits. New reports = new YYYYMMDD- files; no
  deletions (mv to RECYCLE-BIN/). Checkpoint-commit after each component. Every Agent dispatch carries
  an explicit model= parameter.
- End with: a real pilot transcript + report, a mechanics-fix list, a new dated O3 handoff in
  00-PORTFOLIO/, a memory update, and a final commit. Next gate = O4 (≥6-model panel, all §3 gate
  stats) — needs keys/sanctioned API + the ~60-item/design human labels for the judge-validity gate.

If keys/OAuth are NOT ready this session: still land the live-wiring code + recorded-transcript tests +
the O3 handoff, and STOP before any live call. Do NOT fabricate results — a mock run is not a pilot.
```

---

**Notes for Jimmy (not part of the prompt):**
- **Model: Opus.** O3 is wiring + a mechanics pilot; the Fable window (~07-11) is worth more on O4/O5
  (first real panel adjudication vs the frozen gates). If O4 can't be reached before the window closes
  (blocked on keys + human labels), Fable's fallback use is an adversarial review of the harness + first
  pilot data — not the wiring.
- **Auth:** OAuth (`ant auth login` for Claude, Codex CLI for GPT) unblocks the O3 pilot with zero key
  setup. Per the sibling WCF-Bench finding, keep CLI-OAuth to the small pilot; the gated O4 panel wants
  the sanctioned Messages API path. Have that decided before O4, not O3.
- **Still owed before O4:** multi-vendor keys (or sanctioned API path), the ~60-item/design human labels
  for §3.4, and rulings on PR-1 (356 authored / 344 runnable) + PR-2 (06 system frame).
