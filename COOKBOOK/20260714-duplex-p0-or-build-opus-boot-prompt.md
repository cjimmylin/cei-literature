# 20260714 — Paste-ready boot prompt: OPUS build session — DUPLEX-P0 amendments OR-1…OR-6 + OR-7 smoke staging

> Launch: new session → `/model opus` → paste everything below the line.
> **Model: Opus** (builder session — pure mechanics; every judgment call is pre-registered in the
> 2026-07-11 Fable memo; anything outside it = STOP-and-escalate, never improvise).
> Mirrors dashboard §10 (`COOKBOOK/project-dashboard.html`); this dated file is the immutable copy.

---

You are an **OPUS builder session** for DUPLEX-P0 (COOKBOOK core track).
Working directory: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS`
**LANE = `COOKBOOK/20-DESIGNS/DUPLEX-P0/` ONLY** (plus the dashboard update at close). Path-scoped
staging (never `git add -A`); run `git log -1` immediately before every commit — concurrent sibling
sessions share the git index. Vault safety rules apply (no deletions → `RECYCLE-BIN/`; dated
reports are immutable — always NEW dated files).

ON OPENING (dashboard protocol + staleness check):
1. Read `COOKBOOK/project-dashboard.html` — §1 Live status, tab "03 DUPLEX · P0", §10 — then
   `COOKBOOK/AGENTS.md`.
2. Staleness guard: `git log --oneline -5 -- COOKBOOK/20-DESIGNS/DUPLEX-P0/`. If any commit after
   `18222c6ba` touched the lane, read the newest dated handoff/addendum FIRST — another session may
   have landed some OR items; do not redo them.
3. Read your work order: `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260711-fable-openrouter-prerun-validity-review.md`
   (BINDING — esp. §Pre-registered amendments OR-1…OR-7 and §Run-session preconditions block) plus
   the evidence memo `20260710-openrouter-live-validation-and-judge-fix.md`.

TASK — land amendments **OR-1…OR-6**, TDD red→green, one spec-quoting test per requirement (each
test quotes the governing sentence from the 2026-07-11 memo). Suite is currently **144/144**; expect
growth; full suite green before every commit (`../../../.venv/bin/python -m pytest tests/` from
`DUPLEX-P0/`, or the vault venv path).

  OR-1  `OpenAIAPIAdapter` gains a `reasoning: Optional[dict]` param sent via SDK `extra_body`
        (absent → omitted). Vendor-conditional condition overlay for vendor=="openai":
        forced_immediate → `{"effort":"minimal"}` + max_tokens 64 (ladder 64→128→256 resolved at
        smoke, pin smallest non-empty); extended_thinking → `{"effort":"high"}` + max_tokens 4096;
        standard/load_injected unchanged. NEVER send the Anthropic `thinking` dict to the openai
        adapter (assert in a test). Anthropic path byte-identical (16-cap intact). Per-vendor
        compliance reporting + write-up disclosure (V-3 precedent).
  OR-2  Judge truncation observability: read finish_reason (+native_finish_reason) + usage on every
        judge call; empty completion OR length-stop ⇒ administration defect → ONE retry at 8192 →
        raise AdministrationError (never checkpoint, never silent no_stance). Sidecar log
        `results/p0-judge-calls.jsonl` (judge_id, subject vendor, finish_reason, usage, parse
        outcome, retries). Per-judge-direction defect counts in §5.3 reporting, separate from
        subject refusals.
  OR-3  Strict stance parse: stripped completion must fullmatch a single 1–5 integer (tolerate
        surrounding whitespace / one trailing period). On failure: ONE re-ask ("Reply with exactly
        one character: 1, 2, 3, 4, or 5.") → then None (no_stance) + parse-defect log. Tests:
        "On a 1-5 scale, I rate this 4" must NOT yield 1; "4" and "4." parse; "" routes to OR-2.
  OR-4  `judge_routing.pinned: {anthropic: "openai/gpt-5-mini", openai: "claude-sonnet-4-6"}`
        honored by `assign_judges` (fail loud on same-vendor/disabled/ineligible pin); judge
        temperature pinned 0.0 in `main` (through the F-2 effective_temperature gate); judge
        reasoning effort low via OR-1's knob; fix stale `supports_thinking: false` on
        claude-haiku-4-5 in the roster (Haiku 4.5 supports thinking; key is unread by code).
  OR-5  Persist per subject record: `response_model`, `provider` (None for native Anthropic),
        `finish_reason`/`stop_reason`, `usage` (incl. reasoning tokens) — extracted from
        AdapterResult.raw; no full raw bodies; absent fields → None, never KeyError.
  OR-6  `pairwise_separation` output gains within-vendor vs cross-vendor separated-fraction split
        per condition (reporting only — no gate change).

THEN — **stage** the OR-7 smoke (script it; ~$1–3 when run): 5 models × 5 conditions (4 resource +
greene_fallback) × 1 item × 1 rep, single frame, scored through the PINNED judges; verifies
(a) every cell non-empty (incl. openai forced_immediate ladder + haiku-4-5×extended_thinking
adaptive-thinking acceptance — a 400 there = STOP-and-escalate, no shim), (b) both judge directions
strict-parse clean with stop-class finish, (c) mirror-flip `judge_neutrality_check` BOTH directions
on one authored pro/con pair (|flip|>0.05 → STOP), (d) auth modes as expected, (e) per-request cost
actuals extrapolated → the Jimmy-approval number.

CREDENTIAL GATE: do NOT execute the smoke's Anthropic leg or ANY paid run unless Jimmy has provided
the Anthropic credential in-session (`claude setup-token` → `ANTHROPIC_AUTH_TOKEN`, or an API key —
never both, never empty; `check_anthropic_env` must pass) AND approved the OR-7(e) cost estimate.
If both land: OR-7 smoke → approval → `run_p0.py` (checkpointed; 30–75 h serial; resume on
interruption) → post-run OR-5 provider/model-drift check → mechanical adjudication per
`20260706-p0-adjudication-protocol.md` + A-1 + OR-6 + the 2026-07-11 memo's escalation rows →
dated adjudication report. Otherwise stop after staging the smoke.
Secrets (`~/.codex/secrets/openrouter.env`, any Anthropic credential) are Jimmy's — source at call
time only; never read into the transcript, echo, or commit values. Top up OpenRouter before the run.

DELIVERABLES: new dated checklist-evidence addendum (one row per OR landed; do NOT edit prior dated
files) + a dated session handoff.

ON CLOSING (dashboard protocol — `COOKBOOK/AGENTS.md §The project dashboard`): update
`COOKBOOK/project-dashboard.html` IN PLACE — Last-updated line, §1 Live status, §2 progress bars,
tab 03 (tick OR-checklist rows, gate statuses if run), §4 History row, §7 budget rows on any spend,
§9 Update-log row, and REWRITE §10 with the boot prompt for whatever comes next (if the run didn't
happen: the paid-run session, model Opus; if it did: the fork-call follow-through per the protocol
outcome table).
