# WALKWORTHY — Paste-Ready Boot Prompt for Session O3 (live mechanics SMOKE)

<!-- WALKWORTHY-CANARY-7f3e2026 -->
Run this session on **Opus** (`/model opus` if needed). O3 is live-wiring + a **mechanics SMOKE**
(NOT the full pilot matrix) — clear-spec code, fix-mechanics-only. Auth is PINNED to subscription CLIs
(Claude = `claude -p`, GPT = Codex CLI), so this session is a smoke test, not a measurement. Do NOT
spend a Fable window on it; reserve Fable for adjudicating the first REAL panel against the frozen gates
(O4/O5). Copy everything in the block below into a fresh session.

---

```
Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) — Session O3: live-wiring + a MECHANICS SMOKE (not the full pilot matrix).

SCOPE LOCK: stay entirely within CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/. Do NOT
touch, read for design input, or import from any sibling bench (WCF-Bench, FruitBench, CookBook,
SermonMount, CorinthLove, etc.). Differentiate only against published literature ([[biblebench-scope-isolation]]).

START by reading, in order:
1. 00-PORTFOLIO/20260709-O2-session-handoff.md — current state (harness DONE, mock-first, 88 pytest
   green), authority stack, O3 scope (§6), auth (§7), pending rulings (§4), known caveats (§5).
2. The authority stack it names in §2 — master plan §1 (P0 pilot spec) + §3 (frozen gates), the
   normative charter (construct / strata / reporting spine), the item playbook (four-way refusal taxonomy).
3. harness/README.md — the "Auth" and "O3 wiring" sections (the exact checklist) + the layout.

AUTH IS PINNED (subscription CLIs — smoke-only, no API keys this session):
- Claude family: `claude -p` (subscription OAuth). GPT family (the cross-family judge): the Codex CLI.
- Both are consumer/subscription automation, defensible ONLY as a smoke test. This session makes a SMALL
  number of live calls (~a dozen), labels all output "smoke, not a measurement," and does NOT run the
  full pilot matrix or the O4 panel. Confirm both CLIs are logged in and reachable before any live call.

THEN wire live mode and run the smoke (EXECUTION mode — runnable code + a REAL smoke report, not a plan):
- Wire two thin live backends behind the existing ModelClient interface: an Anthropic backend that shells
  to `claude -p` (subprocess), and an OpenAI/GPT backend that shells to the Codex CLI. Keep clients.py's
  ModelClient contract; do NOT change the mock path. (These CLI backends are distinct from the
  clients.AnthropicAdapter SDK stub, which stays deferred to the keyed/O4 path.)
- Add real Judge subclasses (subclass judges.Judge) that call a model (via the CLI backend) and PARSE the
  JSON verdict — the rubric prompt is already assembled by judges.assemble_rubric_prompt. Enforce 2
  cross-family judges (Claude + GPT), log disagreement per cell, NEVER average (the layer already does
  this — keep it).
- Replace executors.default_state_classifier with a judge-backed per-turn state classifier for the
  scripted multi-turn designs (02 complied/refused, 07 validated/challenged/deflected).
- Run a SMOKE SLICE (NOT the §1 3-models×5-items/design matrix — that needs the sanctioned API path):
  ~a dozen live calls total across the structurally-distinct designs — one single-turn (01), 05
  (allocation block), one scripted multi-turn (02 or 07), one paired (09 or 10) — PUBLIC/runnable items
  only. GOAL: prove on REAL output that parsing, four-way refusal tagging, the strict 05 allocation parser
  + one-retry, judge JSON-verdict parsing, and 02/07 branch selection all work end-to-end. Log every
  mechanical defect.
- The full pre-registered §1 P0 pilot (3 models × 5 items/design) is DEFERRED to the sanctioned
  Developer-Platform API path. Record this scoping deviation (reason: ToS — subscription CLIs are
  smoke-only) in the O3 handoff, and route it to 00-PORTFOLIO/PENDING-RULINGS.md if you judge it needs
  Jimmy's explicit sign-off (it is a sequencing change, not an item/gate change).
- Deliver: a NEW dated smoke report `00-PORTFOLIO/YYYYMMDD-O3-smoke-report.md` + the run written to
  `runs/YYYYMMDD-o3-smoke/` (manifest + summaries committed; large jsonl gitignored, per O2).

Ground rules for this session (frozen):
- FIX MECHANICS ONLY. Do NOT edit items based on model performance — that contaminates difficulty
  calibration (master plan §1). Anything judgment-shaped → 00-PORTFOLIO/PENDING-RULINGS.md, parked.
- Load the PUBLIC split ONLY (loader HARD-REFUSES HOLDOUT, charter §6.6). Manifest stays IDs-only;
  permutation seeds stay FIXED constants — never runtime-generated.
- Do NOT send temperature / top_p / top_k to Opus 4.7+/Fable judges or SUTs — they 400 (adaptive
  thinking only). Control depth with output_config.effort; pin decoding via prompt, not sampling.
- ToS: subscription CLIs (`claude -p`, Codex) are smoke-only. Keep live calls small; label all numbers
  "smoke, not a measurement"; do NOT scale to the full pilot matrix or the O4 panel. The measurement path
  (full P0 pilot + O4 gated panel) needs the sanctioned Developer-Platform API on BOTH vendors. Never
  present smoke output as a result.
- Keep the mock path working (88 pytest green stays green). Add tests for the live-wiring seams using a
  RECORDED/stubbed CLI transcript — never a live network/CLI call in the test suite.
- Repo discipline: this worktree has ≥3 concurrent sessions — `git log -1` before staging, stage
  WALKWORTHY paths explicitly, never rewrite sibling commits. New reports = new YYYYMMDD- files; no
  deletions (mv to RECYCLE-BIN/). Checkpoint-commit after each component. Every Agent dispatch carries an
  explicit model= parameter.
- End with: a real smoke transcript + report, a mechanics-fix list, a new dated O3 handoff in
  00-PORTFOLIO/, a memory update, and a final commit. Next gate = O4 (≥6-model panel, all §3 gate stats)
  — needs the sanctioned API on both vendors + the ~60-item/design human labels for the judge-validity gate.

If the CLIs are NOT both logged in / reachable: still land the live-wiring code + recorded-transcript
tests + the O3 handoff, and STOP before any live call. Do NOT fabricate results — a mock run is not a smoke.
```

---

**Notes for Jimmy (not part of the prompt):**
- **Model: Opus.** O3 is wiring + a mechanics smoke; the Fable window (~07-11) is worth more on O4/O5
  (first real panel adjudication vs the frozen gates). If O4 can't be reached before the window closes
  (blocked on the sanctioned API + human labels), Fable's fallback use is an adversarial review of the
  harness + first smoke data — not the wiring.
- **Auth (your call, applied):** Claude = `claude -p` subscription, GPT = Codex CLI — both **smoke-only**.
  This unblocks the O3 mechanics shakeout with zero keys, but subscription automation is defensible only
  at smoke scale. The **measurement** path — the full §1 3×5/design P0 pilot and the O4 gated panel —
  needs the sanctioned Developer-Platform API on **both** vendors (Anthropic key/WIF + OpenAI key). Decide
  that before O4.
- **Still owed before the real panel:** sanctioned multi-vendor API access, the ~60-item/design human
  labels for §3.4, and rulings on PR-1 (356 authored / 344 runnable) + PR-2 (06 system frame).
