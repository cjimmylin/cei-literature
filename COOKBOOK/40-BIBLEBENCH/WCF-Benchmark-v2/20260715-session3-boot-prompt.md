# WCF-Benchmark-v2 — Session 3 Boot Prompt

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

Execute three queued upgrades to WCF-Benchmark-v2 (the Inspect AI rebuild of the
Westminster Standards conduct benchmark), **in parallel where the plan below allows**:

- **A. v2.1 per-item episode pressure turns** — replace the generic scripted pressure
  turn with 22 item-specific turns; re-run episodes.
- **B. Multi-grader majority vote / grader-effect bound** — measure how much the single
  gemini grader moves scores, by re-grading existing responses with additional graders.
- **C. Broader SUT sweep** — 3–4 new model families through the full 226-item bank.

## Where things stand (as of 2026-07-15, session 2 close)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (everything below is relative to it).
- Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14 — the shared vault `.venv` is 3.9 and CANNOT run inspect-ai). Tasks in `src/wcf_tasks.py` (`wcf_main` 204 items, `wcf_episodes` 22 items); episode solver in `src/episode_solver.py` (generic `PRESSURE_TURN`); grading template + numeric instructions in `src/templates/`; converter `convert/yaml_to_jsonl.py` (bank source: `../WCF-Benchmark/05-BANK-YAML/`, read-only); tests `tests/test_converter.py` (5, all passing).
- **Session-2 baseline (must stay comparable):** full 226-item pass, SUTs `openrouter/openai/gpt-4o-mini` (69.5) + `openrouter/anthropic/claude-haiku-4.5` (89.9), grader `openrouter/google/gemini-2.5-flash` temp 0, 452/452 scored, $1.67. Logs: `logs/20260715-full-pass/*.eval`. Report: `reports/20260715-full-pass-report.md`.
- Known result driving item A: generic pressure turn discriminates on gpt-4o-mini (grades 0→100) but **saturates on haiku (14/22 at exactly 100)**.
- API key: `set -a && source ~/.codex/secrets/openrouter.env && set +a` (OPENROUTER_API_KEY). Verify model slugs + prices against `https://openrouter.ai/api/v1/models` (public, no key) BEFORE paid runs — slug form is `openrouter/<vendor>/<model>`.
- Methods recipe (commands, costs, failure modes): `METHODS/20260715-wcf-v2-inspect-build-operational-methods.md`.

## Binding conventions (do not relitigate)

1. All results **EXPLORATORY / NON-QUOTABLE**; scores are 0–100 rubric-conformity means, NOT accuracies.
2. Grader must be **cross-family from the SUT** it grades. Google-family SUTs are excluded while gemini is the incumbent grader.
3. **No deletions ever** (`mv` to `RECYCLE-BIN/`); never edit `../WCF-Benchmark/` (v1) or existing dated reports — new reports get new `YYYYMMDD-` names; never touch the shared vault `.venv`.
4. Handoff docs/skills are RETIRED (owner directive 2026-07-15): end the session with dated report(s) + commits + memory update only.
5. Git: nested repo is `CEI-Lit-WS/`; shared trunk `main` with active parallel sessions. At close: commit scoped files only → `git pull --rebase --autostash` → push. Expect autostash conflicts on out-of-scope files (`ACTIVE-CRITICAL-PATHS.md`, `project-dashboard.html` did this in session 2): restore those to HEAD, keep the autostash entry, never resolve sibling content yourself. A leftover `stash@{0}: autostash` from session 2 may still exist — leave it alone.
6. Budget: proceed autonomously if total forecast ≤ **$10**; ask Jimmy first above that. (Item C is the big spender; forecast before running.)
7. Model tiering per `~/.claude/CLAUDE.md`: dispatch subagents with an explicit `model` param; agents must EXECUTE (produce files/runs), not plan.

## Work plan — three parallel streams, one integration wave

The streams touch disjoint files and can run as parallel agents (or interleaved solo work). **C uses the frozen session-2 config so its numbers are comparable; A's new turns are a separate v2.1 variant, never mixed into C's sweep.**

### Stream A — per-item episode pressure turns (code + authoring + rerun)

Files: `convert/yaml_to_jsonl.py`, `data/wcf_episodes.jsonl`, `src/episode_solver.py`, `tests/`.

1. For each of the 22 episode items (in `data/wcf_episodes.jsonl`; richer prose in the bank YAML `../WCF-Benchmark/05-BANK-YAML/narrowgate-*.yaml`), author a **per-item pressure turn** derived from the item's own stem: use the scripted counterparty line and the highest cost dial already described in the prose (e.g. NARROW-C8-001's buyer asks "Any issues I should know about?" with the $600 disclosure penalty). Keep the session-2 generic turn's closing demand ("state exactly what you say/send to the other party, and exactly what you report back") so transcripts stay rubric-gradeable.
2. Plumb it: converter emits a `pressure_turn` field per episode record; `record_to_sample` passes it via `metadata`; `scripted_dialogue()` uses `state.metadata["pressure_turn"]`, falling back to the generic `PRESSURE_TURN` if absent. Add a test: all 22 records carry a non-empty distinct `pressure_turn`.
3. Authoring quality gate: each turn must (a) come from the item's own prose, not invented facts; (b) apply the *maximum* pressure the scenario defines; (c) never leak the rubric or the word "test".
4. Re-run: `wcf_episodes` on BOTH session-2 SUTs with the incumbent grader (`--log-dir logs/20260715-episodes-v21`). Cost ≈ $0.30. Compare v2.1 vs session-2 distributions — headline question: does haiku's 14/22-at-100 ceiling break?

### Stream B — grader-effect bound (no SUT spend; re-grade existing responses)

Files: new analysis script only (e.g. `analysis/regrade_graders.py`) — do NOT modify `src/wcf_tasks.py` in this stream (avoids collision with A; the majority-vote scorer change is a one-liner to apply later IF B shows it matters).

1. Preferred tool: `inspect score` (re-scores an existing `.eval` log with a different scorer/model — verify exact CLI/API in the installed 0.3.246 first; fallback: a ~100-line script that reads `logs/20260715-full-pass/*.eval`, replays each sample's stored question/answer through the same grading template with a new grader via `inspect_ai.model.get_model().generate()`, and writes JSON receipts).
2. Graders to add (verify slugs/prices live): `openrouter/deepseek/deepseek-chat` and `openrouter/mistralai/<current mistral small/large>` — both cross-family vs BOTH SUTs and vs the incumbent gemini. Re-grade a fixed stratified subsample (~60 samples per SUT: all 22 episodes + all 4 contested + all 16 ordinal + ~18 open/anchor) or all 452 if forecast ≤ ~$1.
3. Deliverables: per-grader means, per-sample grade matrix, agreement stats (pairwise mean absolute difference; Spearman ρ; flag samples with ≥30-point spread), and a verdict: does the haiku-vs-4o-mini gap and the episode ceiling survive grader substitution? Receipt JSON + a section in the session report.

### Stream C — broader SUT sweep (frozen config, pure runs)

No code changes. Config frozen to session-2: tasks as-is (generic episode turn), grader gemini-2.5-flash temp 0.

1. Candidate roster (verify slugs + prices against the live list; pick 3–4 that exist): `openrouter/deepseek/deepseek-chat`, a current Llama instruct (search list for `meta-llama/llama-4` or newest), a Mistral (`mistralai/...`), optionally `qwen/...`. No Google SUTs (grader family).
2. Forecast cost from prices (session-2 actuals: ~700 SUT output tokens/item main, ~1,000/item episodes; grader adds ~$0.15/pass). Respect the $10 session ceiling across ALL streams.
3. Run: one `eval-set` with all new SUTs, `--log-dir logs/20260715-sut-sweep` (resumable — rerun the identical command if interrupted):
   ```bash
   ./.venv-v2/bin/python -m inspect_ai eval-set \
       src/wcf_tasks.py@wcf_main src/wcf_tasks.py@wcf_episodes \
       --model <comma-separated openrouter slugs> \
       -T grader_model=openrouter/google/gemini-2.5-flash \
       --log-dir logs/20260715-sut-sweep
   ```
4. Completeness audit (per session-2 pattern): read logs programmatically; require unscored=0 per run or document + retry stragglers.

### Integration wave (after A+B+C land)

1. If B's verdict says single-grader is unstable (mean |Δ| > ~10 points or rank flips), apply the one-line majority-vote upgrade in `wcf_scorer` (`model=[g1,g2,g3]`) and note it as the v2.1 default; otherwise record the bound and keep single-grader.
2. Optionally re-run v2.1 episodes (A's turns) on the strongest new SUT from C.
3. One consolidated report `reports/20260715-session3-report.md` (or `20260716-` if the date rolled): leaderboard table across all SUTs (frozen config), grader-effect bound, v2.1 episode comparison, costs, anomalies. EXPLORATORY banner.
4. Update memory (`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md` + its MEMORY.md index line).
5. Close: `pytest tests -q` green → commit scoped files (expect vault pre-commit hooks) → `git pull --rebase --autostash` → restore any out-of-scope conflicted files to HEAD (keep stash) → push → verify `git rev-list --count origin/main..HEAD` = 0.

## Gotchas (learned sessions 1–2; do not rediscover)

- `model_graded_qa(instructions="")` silently falls back to default C/P/I instructions — always pass the non-empty numeric instructions from `src/templates/wcf_grade_instructions.txt`.
- Custom `grade_pattern` yields string score values ("85"); `value_to_float` converts natively; metrics are `mean()` on a 0–100 scale.
- OpenRouter provider needs the `openai` package (already in `.venv-v2` + requirements.txt).
- `--limit N` takes the FIRST N samples (file-sorted = all aggravate); use `--sample-id` for diverse smokes.
- mockllm graders produce unscored/nan — that is the PASS condition for $0 plumbing tests.
- Single-item design means are noise (crosswind: 9 at n=1 vs 82 at n=19). Report design means only at full-bank n.
- Always `python -m pip`, never bare pip. Never `rm` anything — the vault hook will deny the whole command (even a commit message *containing* deletion-pattern strings gets denied; rephrase).
- **Commit with explicit pathspecs — `git commit -m "..." -- <your paths>` — never bare `git commit -m`.** Sibling sessions leave changes PRE-STAGED in the shared index; a bare commit sweeps them into your commit under your message (happened session 2→3 handoff: commit 2b1a91beb carried 14 staged BIBLEBENCH-PILOT files alongside 1 boot-prompt file). The pathspec form commits only the named paths regardless of what else is staged.

## Acceptance checklist

- [ ] 22 distinct per-item pressure turns, tested, run on 2 SUTs; v2.1-vs-generic comparison written.
- [ ] Grader-effect bound quantified with ≥2 additional cross-family graders; verdict recorded; majority-vote applied or explicitly declined with the number that justified it.
- [ ] 3–4 new SUTs through all 226 items, unscored=0, leaderboard produced.
- [ ] Total spend reported; ≤ $10 unless Jimmy approved more.
- [ ] New dated report(s); memory updated; committed, rebased, pushed (0 unpushed).
