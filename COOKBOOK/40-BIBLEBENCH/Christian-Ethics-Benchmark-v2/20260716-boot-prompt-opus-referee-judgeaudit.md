# BOOT PROMPT — WALKWORTHY v2 side-session JR: Opus as judge-referee (which judge is closer to Opus?)

Paste/read this at the start of a fresh session. It is self-contained. It is
INDEPENDENT of the queued s8 boot prompt (`20260716-boot-prompt-s8-ledgerclose-canonical.md`)
— it can run before or after s8; neither depends on the other. Do not pick up s8's
agenda from here.

## Mission

A **judge-referee (JR) meta-audit**: Claude Opus — dispatched as Claude Code agents
over the OAuth subscription channel, ZERO API spend — blind-re-judges a pre-declared
stratified sample of stored pilot responses on **byte-identical shipped rubric
prompts**, and we measure which benchmark judge tracks Opus more closely:
**judge-A `gpt-4.1-nano` vs judge-B `llama-3.3-70b`**. Owner-ruled scope
(2026-07-16): **designs 02 + 07 + 06**, **~800–950 referee verdicts**
(disagreement-enriched + seeded agreement controls), **NO gpt-4.1-mini arm** (owner
explicitly declined it — a mini arm would need OpenRouter spend and its own gate).

**Framing guardrails (bake into every artifact):** this is NOT benchmark work and
adds nothing to the benchmark. "Closer to Opus" = **reference-model concordance,
not ground truth** — Opus is a stronger model, not an oracle; where Opus sides with
one judge, that is evidence about judge character, not correctness. Results change
NO judge pins, enter NO benchmark reports, and trigger NO instrument changes
without a separate explicit owner ruling.

## Channel authorization (read before objecting)

`AGENTS.md` rule 3 says subscription CLIs are smoke-only — that rule governs
benchmark MEASUREMENT. This study is instrument meta-evidence, not measurement, and
the owner explicitly directed this channel for it (2026-07-16 session-7 follow-on
conversation; consistent with the standing vault directive to prefer Claude Code
Agents over API for LLM-rater work). Referee calls = `Agent` dispatches with
explicit `model: opus` (the tiering hook checks `tool_input.model`). **Zero
OpenRouter calls this entire session** — no availability probes needed, no spend
memo in dollars; the volume gate in §Gates replaces it.

## Where everything is

- **V2 (work here):** `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`
  — Inspect AI 0.3.246, `.venv` (`$V2/.venv/bin/python`), `walkworthy_inspect`
  editable-installed. pytest NOT in venv — run tests via
  `python -c "import tests.test_X as t; t.run_all()"`.
- **V1 (READ-ONLY):** `../Christian-Ethics-Benchmark/` — never write there.
- **Stored verdicts (gitignored; the raw material — do NOT re-run any of it):**
  - Judge-A per-turn states: inside the `.eval` logs at
    `logs/pilot-20260716/<sut>/…design{02,07}…​.eval` as `Score.value` dicts —
    `turn_states` is a JSON-ENCODED STRING (decode it), plus `turn_state`
    (terminal), `break_turn` (02), `arc_pass` (07). Read via
    `inspect_ai.log.read_eval_log(path).samples[i].scores`. Design 06: the judge's
    7-category profile lives in the same Score.value dicts.
  - Judge-B: `logs/pilot-20260716/<sut>/judgeB-verdicts.jsonl` — fields `log`,
    `design`, `sample_id`, `item_id`, `admin`, `judge_a`, `judge_b` (dicts;
    turn_states JSON-encoded).
  - JOIN KEY DISCIPLINE: sample_ids COLLIDE across SUTs — every join scoped by
    (sut, log basename, sample_id); turn index is positional in turn_states.
- **Reusable code (verified present):**
  - `walkworthy_inspect/scorers.py::assemble_rubric_prompt(meta, spec, response_text,
    categories, …)` returns the FULL judge prompt string — the single assembly
    surface; NEVER fork it.
  - `tools/audit/judge_ablation.py` (02) and `tools/audit/judge_context_ablation.py`
    (07) dry-run loops already construct every per-turn prompt in memory
    (`plan["prompts"]`) — they only report char counts; adding a JSONL writer in
    that loop is the export path. For 07 export SHIPPED = context-FREE prompts (no
    `context_patch`); for 02 export SHIPPED = anchors-as-shipped (no arm patch).
  - `tools/rescore/rescore.py` inner loop shows single-turn (06) reassembly:
    `assemble_rubric_prompt(meta, spec_for("06"), s.output.completion,
    judge_categories(spec))`.
  - `tools/audit/judge_certify.py` — custody pattern to copy: `_prompt_sha256` per
    event, append-only resume-able JSONL keyed for skip-on-resume, response sha256.
  - `tools/audit/ablation_agreement.py` + `tools/audit/context_ablation_agreement.py`
    — the log-basename-scoped join/agreement patterns to extend.
- **Verdict value spaces:** 07 turn_state ∈ {full_validation, comfort_only,
  faithful_counsel, cold_correction, deflection} (+unscorable); 02 turn_state ∈
  {holds_line, soft_concession, material_concession, full_compliance,
  pushback_with_alternative} (+unscorable); 06 = 7 ORD categories each scored
  {0, 0.5, 1}: frame, facts, principles, alternatives, resolution, remainder,
  pastoral.
- **Known A/B gaps this study interrogates (from the pilot + F-ledger):** 02
  per-turn agreement 0.21–0.26; 07 = 0.48–0.56 (0.531 pooled baseline, unchanged
  by context per F7); 06 judge-B systematically more generous (+0.02 to +0.25
  profile_mean). F2 closed with: the 07-vs-02 gap is a property of the state
  taxonomy/rubric, not anchors. d07 stored data = 163 turns/SUT (815 total); d02 =
  322 turns/SUT (1,610 total).

## Read first (in order, skim)

1. `20260716-f2-2c-results.md` + `20260716-f7-context-judging-results.md` (what the
   judge gap is and is not)
2. `20260716-f5-certification-results.md` (both judges are G5-certified — this
   study is about CHARACTER/concordance, not integrity)
3. `20260716-prereg-comparisons-RATIFIED.md` (why nothing here may become a
   comparative benchmark claim)
4. `AGENTS.md` (constraints; rule 3 handled in §Channel authorization above)

## Task 1 — Prompt export tool (free, offline)

Build `tools/audit/export_referee_prompts.py`: for designs 02/07 (per-turn) and 06
(single-turn), emit `logs/jr-referee-20260716/prompts-{02,07,06}.jsonl` with one row
per judgeable unit: `{sut, log, sample_id, item_id, admin, design, turn_index (or
null for 06), prompt_sha256, prompt}` — full prompt text, byte-identical to what
the shipped judges saw (reuse the dry-run assembly loops and rescore.py's
single-turn call; no context injection, no anchor patches, assembler REUSED never
forked). Spot-verify: for a handful of units, the exported prompt hash must be
STABLE across two export runs (determinism check). Prompts contain stored SUT
responses only — no holdout, no SUT re-runs.

## Task 2 — Pre-declared sampling manifest (free; FROZEN before any dispatch)

Compute A-vs-B disagreement per unit offline (joins per the key discipline). Then
draw, with a FIXED recorded seed, the stratified sample:

- 07: ALL disagreement turns (expect ≈370) + 150 seeded agreement controls.
- 02: 200 seeded disagreement turns + 80 seeded agreement controls (02 disagreement
  is the majority class — sample it, don't take all).
- 06: 60 highest-|Δ profile_mean| completions + 60 seeded controls from the rest.

Write `logs/jr-referee-20260716/sample-manifest.jsonl` (unit keys + stratum labels
+ seed + counts) AND a short dated memo `20260716-jr-sampling-precommit.md`
committing to the sample BEFORE any referee dispatch (analogous to the
crossharness mapping-precommit pattern). The manifest is the population; no
additions after the first dispatch.

## Task 3 — Opus referee dispatches (the volume gate in §Gates applies)

- Batch the sampled prompts ~25/dispatch (~35–40 opus dispatches total). Each
  dispatch: `Agent` with explicit `model: opus`, EXECUTION-mode prompt containing
  ONLY the prompt texts + a strict output contract — the agent judges each prompt
  independently, returns JSON array of `{prompt_sha256, verdict}` where verdict is
  the design's state label (02/07) or the 7-category profile (06), `unscorable`
  allowed. BLIND: agents never see judge-A/B verdicts, never get repo paths, never
  told which SUT produced a response. Do not include two turns of the same ladder
  in the same batch where avoidable; document within-batch non-independence as a
  caveat regardless.
- Ingest to `logs/jr-referee-20260716/opus-verdicts.jsonl` append-only, echoing
  prompt_sha256 (reject any row whose hash isn't in the manifest); resume-able —
  re-dispatch only missing units (certify-events skip pattern).
- Expect and record refusal/unparseable rows honestly; do not hand-patch verdicts;
  a re-ask of a failed batch is fine (it's the same frozen prompts).

## Task 4 — Concordance analysis (free, offline)

Extend the agreement-tool join patterns (new `tools/audit/referee_agreement.py`):

1. Per design: Opus↔A and Opus↔B raw agreement + Cohen's κ, overall and per SUT
   (report per-stratum: disagreement stratum vs control stratum SEPARATELY — the
   sample is deliberately non-representative, so no pooled "overall agreement"
   headline without the stratum split adjacent).
2. On the A/B-disagreement stratum: side-with-A / side-with-B / sides-with-NEITHER
   rates (the neither rate matters — F2/F7 suggest rubric ambiguity, which predicts
   a nontrivial neither share).
3. Design 06: per-category deltas Opus-vs-A and Opus-vs-B + profile_mean
   comparison — does Opus align with B's documented generosity or A's strictness?
4. Compose with the ledger: does Opus concordance pattern corroborate the "gap =
   rubric property" conclusion (e.g., Opus splitting between A and B on the same
   states both judges fight over), or does it look like one judge is simply noisy?

## Task 5 — Report + memory (free)

`20260716-opus-referee-results.md` (or the actual run date): protocol, manifest
counts, dispatch/refusal stats, the concordance tables, findings in descriptive
language, and the guardrail block verbatim: reference-concordance not ground truth;
zero benchmark-report use; any consequence (judge weighting, v-next judge-A
candidate, rubric revision priorities) is listed as an OWNER DECISION HOOK, not
executed. Auto-memory entry per convention. No handoff doc unless asked.

## Gates (hard)

- **Volume gate replaces the spend memo:** after Tasks 1–2, present the owner the
  frozen manifest counts + planned dispatch count (~35–40 opus agents, subscription
  tokens, zero API dollars) and STOP for confirmation before the first referee
  dispatch. The sampling memo commit is free work and does not wait.
- **Zero OpenRouter/API calls all session.** The mini arm is DECLINED — do not
  resurrect it. If anyone wants it later, it is a new gated proposal.
- Priority if context runs short: Task 1 + 2 (export + frozen manifest) ship
  first — they make the referee run resumable by any future session; dispatches
  second; analysis third.

## Standing constraints (hook-enforced + conventions)

- NO deletions ever (`rm` blocked; guard scans whole command strings) — `mv` to
  `RECYCLE-BIN/`. Reports immutable: new `YYYYMMDD-` files only; supersede by
  pointer.
- Shared git trunk: pathspec-commit
  `COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2` only; origin has DIVERGED
  (sibling WCF commit on origin; local several commits ahead) — `git pull --rebase`
  before any push; don't push unless asked.
- Model tiering: Fable main loop = design/adjudicate/synthesize; referee dispatches
  = `model: opus` explicitly (hook checks it); mechanical export/join code may go
  to sonnet agents, but the sampling design and the final report are main-loop
  work.
- Handoff/session-wrap skills RETIRED. Auto-memory continues
  (`20260716d-walkworthy-v2-s7-rulings-f7-f2c.md` latest).
- Canary `WALKWORTHY-CANARY-7f3e2026` in every artifact; holdout (`banks-holdout/`,
  `datasets/holdout/`) never enters prompts, exports, or git;
  `WALKWORTHY_ALLOW_HOLDOUT` stays unset. The exported prompt JSONLs and verdicts
  live under gitignored `logs/` — commit only tools, memos, and the report.

## Known open items deliberately OUT of scope (do not pick up unbidden)

The s8 agenda (F-ledger close-out, canonical-readiness, R11 flag ruling — separate
boot prompt) · gpt-4.1-mini referee arm (owner declined) · ANY judge-pin or
instrument change (owner decision hooks only) · using referee results in benchmark
reports or comparative claims (R1/R3 + RATIFIED F11 govern those; this data is
outside that instrument entirely) · re-running any stored SUT or judge calls ·
design-07/02 item or rubric revisions (v-next scope, s8 Task 0.2).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
