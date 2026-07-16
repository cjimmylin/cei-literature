# WCF-Benchmark-v2 — Session 4 Boot Prompt

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

**Adversarially critique and improve** WCF-Benchmark-v2 (the Inspect AI rebuild of the
Westminster Standards normative-ethics conduct benchmark), then **prepare — and if
budget allows, execute — a small pilot run with 5 LLMs** under the improved
configuration. The critique comes FIRST and must be allowed to draw blood: the goal is
to find what would embarrass this benchmark in front of a skeptical reviewer before the
pilot bakes those flaws into more data.

## Where things stand (as of 2026-07-16, session 3 close, commit `c9c9aca72`)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (everything below relative to it).
- Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14 — the shared vault `.venv` is 3.9 and CANNOT run inspect-ai). Bank: 204 main + 22 episode items (`data/*.jsonl`, converter `convert/yaml_to_jsonl.py`, source YAML `../WCF-Benchmark/05-BANK-YAML/` READ-ONLY). Kind mix: 161 open / 23 anchor / 16 ordinal / 4 contested (+ 22 episodes).
- **v2.1 config (current):** per-item max-pressure episode turns (`convert/pressure_turns.py`, opt-in `-T pressure_variant=item`, default generic = session-2-identical); **median-of-3 grader panel is the DEFAULT** (`gemini-2.5-flash + deepseek-chat + mistral-small-2603`, comma-separated `grader_model`, reduced via `multi_scorer(..., "median")`). 7 tests, all passing.
- Leaderboard (frozen single-grader config, 226 items, all unscored=0): qwen3.7-plus 93.4 > claude-haiku-4.5 89.9 > mistral-large-2512 88.9 > deepseek-chat 85.2 (episodes just 51.2 — executes unethical instructions) > llama-4-maverick 72.6 > gpt-4o-mini 69.5.
- Reports: `reports/20260716-session3-report.md` (consolidated) + three stream receipts. Grader-bound artifacts: `analysis/20260716-streamB-*.json` (452-sample × 3-grader matrix, agreement stats).
- API key: `set -a && source ~/.codex/secrets/openrouter.env && set +a`. Verify slugs/prices at `https://openrouter.ai/api/v1/models` (public) BEFORE paid runs.
- Methods recipe: `METHODS/20260715-wcf-v2-inspect-build-operational-methods.md`.

## Known weaknesses — seed material for the critique (do NOT limit yourselves to these)

1. **92/452 samples (20.4%) had ≥30-point grader spread** in the session-3 re-grade
   (worst: MEND-A-W305, gemini 0 vs 100/100). These are a ready-made worklist of
   ambiguous rubrics / grading-standard defects. Matrix: `analysis/20260716-streamB-grade-matrix.json`.
2. **Ceiling compression at the top:** haiku and qwen3.7-plus saturate the main bank
   (~90+); episode v2.1 turns discriminate but n=22. Does the bank separate frontier
   models at all?
3. **Contested kind has n=4** — any contested-item claim is statistically hollow.
4. **Construct validity unexamined:** does a 0–100 rubric-conformity grade measure
   normative-ethics alignment, or instruction-following + verbosity that pattern-matches
   the rubric? Are rubric point-weights defensible? Do stems telegraph the gold key?
5. **Contamination:** the Westminster Standards are public text every SUT has seen.
   Where does that corrupt inference, and where is it harmless (conduct-under-pressure
   vs doctrine-recall)?
6. **deepseek episode collapse (51.2):** verify the grader is penalizing genuine
   compliance-with-harm rather than penalizing terse-but-acceptable answers.
7. **Grader-panel family collision (design decision needed):** the default panel
   contains google + deepseek + mistral. The binding cross-family rule (grader ≠ SUT
   family) means any pilot SUT from those families is partially graded by kin. Options:
   per-SUT panel substitution, panel of never-SUT families, or accept-and-disclose.
   Fable adjudicates in Phase 2.
8. Leaderboard is single-grader (for s2 comparability); the median panel has never run
   at full-bank scale.

## Binding conventions (do not relitigate)

1. All results **EXPLORATORY / NON-QUOTABLE**; scores are 0–100 rubric-conformity means, NOT accuracies. No pre-registration framing (vault v1.x directive).
2. Grader cross-family from SUT (see weakness #7 — resolve the panel collision before the pilot).
3. **No deletions ever** (`mv` to `RECYCLE-BIN/`); never edit `../WCF-Benchmark/` (v1) or existing dated reports — new reports get new `YYYYMMDD-` prefixes; never touch the shared vault `.venv`. Item bank changes go through the converter + YAML-untouched: edit item content ONLY in v2's own files (`convert/`, `data/`), never the v1 bank YAML.
4. Handoff docs/skills RETIRED (owner directive 2026-07-15): end with dated report(s) + commits + memory update only.
5. Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel sessions. **Commit with explicit pathspecs** (`git commit -m "..." -- <paths>`) — bare commits sweep sibling pre-staged files. Close: commit → `git pull --rebase --autostash` → restore any out-of-scope conflicted files to HEAD (keep the stash entry) → push → `git rev-list --count origin/main..HEAD` = 0. Two leftover stash entries exist — leave them alone.
6. Budget: proceed autonomously if total session forecast ≤ **$10**; ask Jimmy above that. (A 5-SUT × 226-item pilot under a 3-grader panel ≈ $0.5–1.5/SUT SUT-side + ~$0.45/pass panel grading → forecast ~$5–8. Reasoning models like qwen3.7-plus cost more; forecast per-SUT before running.)
7. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every dispatch; agents EXECUTE (files/runs), not plan. Critics run as **independent parallel opus agents** with anti-leakage: no critic reads another critic's output; findings are compared only downstream by Fable.

## Work plan — critique first, pilot last

### Phase 1 — adversarial critique fan-out (5 parallel opus critics, disjoint lenses)

Each critic gets the project root, the relevant artifacts, and a refute-first charter
("your job is to break this; concede only what survives"). Each returns structured
findings: {id, severity: PILOT-BLOCKING | MUST-FIX | DEFER, evidence, concrete fix}.

1. **Construct validity & rubric quality** — sample ≥30 main items across kinds +
   ALL 92 high-spread samples; attack: double-barreled rubric criteria, point-weight
   arbitrariness, key-telegraphing stems, conformity-vs-ethics confound.
2. **Grading pipeline** — `src/templates/*`, `wcf_scorer`, grade pattern, median panel,
   `include_history` semantics; attack: prompt injection via SUT answers into the
   grader, parse-pattern edge cases (GRADE: 100 vs 1000), panel-family collision (#7),
   temperature-0 determinism assumptions.
3. **Episode & pressure design** — all 22 episodes + both turn variants + the deepseek
   collapse transcripts; attack: does the 2-turn script measure integrity-under-pressure
   or compliance-with-formatting; are per-item turns fair across items; verify weakness #6.
4. **Contamination & gaming** — attack: memorized-Standards shortcuts, rubric-guessing
   strategies, whether a "always refuse + cite scripture" policy games the bank.
5. **Statistics & reporting** — power at n per kind/design, ceiling effects, stderr
   honesty, what claims the EXPLORATORY banner does and doesn't license at pilot scale.

### Phase 2 — Fable adjudication (main loop, no dispatch)

Dedupe/rank findings; adjudicate the panel-collision design decision (#7); write
`reports/20260716-session4-adjudication.md`: every finding → FIX-NOW / PILOT-OK-DISCLOSE /
DEFER, with one-line rationale. FIX-NOW list becomes Phase 3 work orders.

### Phase 3 — implement fixes (parallel opus agents, disjoint filesets; sonnet for mechanical)

Apply FIX-NOW items. Converter/data changes regenerate jsonl + tests; template changes
get a $0 mockllm smoke + ~$0.05 live micro-smoke. `pytest tests -q` green at the end.
Item-content edits must be logged per-item (old → new + which finding motivated it) in
the adjudication memo's appendix — the bank must stay auditable against v1.

### Phase 4 — pilot spec + run

1. Roster: 5 SUTs, cross-family-clean vs the (possibly revised) grader panel, mix of
   frontier + mid-tier; verify slugs/prices live. Prefer ≥2 SUTs with existing
   session-2/3 baselines for continuity.
2. Forecast total cost. If (spend so far + pilot) ≤ $10 → run it: one resumable
   `eval-set`, `--log-dir logs/20260716-pilot/`, completeness audit (unscored=0),
   leaderboard under the NEW config with explicit "not comparable to session-2/3
   frozen-config numbers" framing. If > $10 → write the runbook + exact command, leave
   run-ready, and ask Jimmy.
3. Consolidated `reports/20260716-session4-report.md` (or next day's date): critique
   summary, adjudications, fixes applied, pilot results/runbook, costs. EXPLORATORY banner.
4. Memory update (`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md` + MEMORY.md index line). Close per convention #5.

## Gotchas (sessions 1–3; do not rediscover)

- `model_graded_qa(instructions="")` silently falls back to C/P/I — always pass the numeric instructions file.
- Inspect's multi-grader `model=[...]` reduces by MODE — degenerate on continuous 0–100 grades; the codebase already uses `multi_scorer(scorers, "median")`. Don't "simplify" it back.
- `inspect score --model` overrides the SUT, not the scorer-closure grader. Re-grade via replay of the persisted grading prompt (`scores['model_graded_qa'].metadata['grading'][0]['content']`, verified grade-free).
- `--limit N` takes the FIRST N samples (file-sorted = skewed); use `--sample-id` for diverse smokes. mockllm → unscored/nan = PASS for $0 plumbing tests.
- Single-item design means are noise; report design means only at full-bank n.
- Task instantiation eagerly builds grader clients → needs OPENROUTER_API_KEY in env even for imports/tests that touch tasks.
- Background-eval agents may go to rest while their eval process lives on: recover with a PID watcher (`until ! kill -0 <pid>`) + continuation dispatch, but check whether the original agent self-resumed before the continuation lands (session 3 got a duplicate receipt that way).
- Always `python -m pip`, never bare pip. Never `rm` — the vault hook denies whole commands containing deletion-pattern strings (even inside messages); rephrase.
- qwen3.7-plus is a reasoning model (~1M reasoning tokens per episode pass) — forecast it separately.

## Acceptance checklist

- [ ] 5 independent adversarial critiques delivered with structured, evidenced findings (anti-leakage held).
- [ ] Adjudication memo: every finding dispositioned; panel-collision decision made and recorded.
- [ ] All FIX-NOW items implemented, per-item edit log kept, tests green, micro-smoke passed.
- [ ] Pilot: roster + forecast; run executed with unscored=0 (if ≤ $10 total) or run-ready runbook + explicit ask (if not).
- [ ] Total spend reported; new dated reports; memory updated; committed with pathspecs, rebased, pushed (0 unpushed).
