# 20260709 — Paste-ready boot prompt: OPUS build of fix packages F-1…F-5 (DUPLEX-P0)

> Start the session with Opus (`/model opus`), `/clear` first, then paste everything below the
> line. This is a **mechanical build session** against a binding Fable spec — no judgment calls
> are open. All five fixes BLOCK the real P0 run.

---

You are an Opus builder session landing fix packages **F-1…F-5** from the binding Fable memo
`COOKBOOK/20-DESIGNS/DUPLEX-P0/20260709-fable-session-a-review.md` (Session-A validity review,
verdict CONDITIONAL-GO). The memo pre-specifies every fix narrowly; **anything you discover
outside F-1…F-5's scope is STOP-and-escalate** (adjudication-protocol rule), never an improvised
judgment.

**Staleness guard first:** `git log -1` — confirm the latest DUPLEX-P0 commit is `045de6ef2`
(Fable review) or a later F-fix commit; if a later session moved things, read its handoff before
touching code.

**Read first (in order):**
1. `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260709-fable-session-a-review.md` — the spec. SA-5/SA-6
   rulings + the F-1…F-5 fix-package table are your entire work order.
2. `COOKBOOK/20260709-fable-session-a-review-handoff.md` — session context.
3. `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260709-ws1-checklist-evidence.md` — the table format your
   evidence addendum must follow.

**Working dir:** `COOKBOOK/20-DESIGNS/DUPLEX-P0/`. Suite is currently **95/95 green**
(`../../../.venv/bin/python -m pytest tests/` — adjust the venv path from where you run). Every
fix lands **red→green**, and every new test QUOTES the governing sentence from the Fable memo
(or the adjudication protocol) in its docstring — the A1/A2 discipline. Do not weaken or delete
existing tests except where the memo explicitly overturns the behavior they assert (SA-5/SA-6:
the tests certifying `returncode!=0`→refusal and condition-name UNMEASURABLE keying are
superseded — replace them with memo-quoting ones).

**The five fixes (full specs in the memo — these are pointers, not the spec):**

- **F-1 (SA-5, adapters + orchestrator + reporting):** Codex `returncode!=0` = administration
  error → bounded retry w/ exponential backoff, then RAISE fail-loud; never a refusal, never
  checkpointed as complete. Codex `refusal_flag` always False; content refusal = scorer→None →
  `"no_stance"`. Anthropic adapter gets the same bounded retry for transient API errors
  (rate-limit/overloaded/network); `stop_reason=='refusal'` unchanged. Reporting: administration-
  error counts per vendor, SEPARATE from refusal counts, + vendor-asymmetry disclosure.
- **F-2 (SA-6, V-4 wiring):** implement the temperature drop for Anthropic `extended_thinking`
  (verify the CURRENT API constraint first — extended thinking rejects modified temperature; use
  the claude-api skill / docs, do not trust memory). Records carry `requested_temperature`,
  `effective_temperature`, `v4_temp_drop`. UNMEASURABLE iff SD≈0 AND all records in the
  (model, item, condition) cell have `v4_temp_drop=True`; caller override re-scoped to
  (model_id, condition) tuples — bare condition names removed. Required test: an SD≈0 Codex cell
  in the same condition codes DEAD, not UNMEASURABLE.
- **F-3 (SA-7):** M030 marker → exact-suffix (`endswith("-M030")`) or exact-ID match; new test
  loads the REAL bank JSON (`items/20260706-p0-item-bank.json`) and asserts the marker matches
  exactly one item (`DPX-P0-M030`).
- **F-4 (SA-8, entrypoint):** `run_p0.py` wiring roster adapters +
  `frames=["monitored","unmonitored"]`, `administer_greene_fallback=True`, `strict_prompts=True`,
  explicit `high_condition="extended_thinking"`/`low_condition="forced_immediate"` (SA-1.1),
  `min_effect=0.02` (SA-4.b), F-2-scoped unmeasurable override, bank via `load_item_bank`,
  obfuscation-QA gate BEFORE scoring. Tests: (i) constructed orchestrator carries exactly these
  flag values; (ii) mock-adapter smoke run entrypoint → records → all three gates end-to-end.
- **F-5 (A-1, gates):** per-item-grain G1 sensitivity, BOTH axes, exact formulas in memo §SA-2:
  `process_cv_item_grain` (per-item cross-model CV of |Δ|, ε-guarded, skipped items counted) and
  `content_cv_item_grain` (per-item cross-model CV of standard-condition mean stance), averaged
  over items; output both + a `sensitivity_reversed` flag; numeric PASS + reversal → verdict
  `PROVISIONAL` (same consequences as G1-b thin base). **A FAIL is never softened** — test that
  explicitly.

**After all five:** full suite green; write a NEW dated evidence addendum
`DUPLEX-P0/2026MMDD-f1-f5-checklist-evidence-addendum.md` (one row per fix, same columns as the
Session-A table — do NOT edit the existing dated table); then dispatch a **NON-BUILDING Opus
audit agent** (WS-1 §3 standing order; it must not have built the code) over the F-1 and F-2
diffs only, A1/A2 code-vs-spec grammar against the memo's SA-5/SA-6 sentences. Fix anything it
catches, re-green.

**Discipline:** parallel sessions share the git index — path-scoped staging only (never
`git add -A`), `git log -1` immediately before every commit, commit promptly per fix or per
coherent pair. No `rm` ever — `mv` to the nearest `RECYCLE-BIN/`. Do not relitigate frozen
rulings (2026-07-05 memo, CS/IB/PS series, the Fable review's ratifications). End with a dated
handoff (`COOKBOOK/2026MMDD-f1-f5-build-handoff.md`) + memory update
([[cookbook-project-state]]), and push.

**After this session:** DUPLEX-P0's remaining chain is credentials (Jimmy) → real P0 run via
`run_p0.py` → mechanical adjudication per the protocol as amended by A-1. Nothing else is open.
