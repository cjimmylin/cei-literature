# WCF-Benchmark-v2 — Session 8 Boot Prompt (OAuth meta-judging study)

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

**Judge the judges.** Re-grade persisted session-7 SUT responses with two OAuth
judges that are NOT part of the benchmark — **J4 = Anthropic Opus via Claude
OAuth (`claude -p`)** and **J5 = OpenAI GPT-5.5-class via Codex OAuth
(`codex exec`)** — and quantify the impact of judging on the v2.4 findings.
Deliverable: **ONE consolidated report**,
`reports/20260717-session8-meta-judging-report.md` ("impact of judging").

Why this session exists: every v2.4 number — including the headline
**gpt-5-mini 78.39 > claude-haiku-4.5 72.48, paired gap 5.90 vs MDD80 5.41
(barely SIG)** — rests on one 3-judge panel (median of gemini-2.5-flash +
deepseek-chat + mistral-small-2603). Prior judge work (Stream B agreement, s5
house-style + kin DiDs, s7 gemini DiD) never re-derived the v2.4 findings under
independent judges. The kin symmetry is the design gift: **J4 is Anthropic-kin
to haiku (a SUT); J5 is OpenAI-kin to gpt-5-mini (a SUT); each OAuth judge
audits the other's kin**, with qwen as mutual non-kin control.

**Explicit non-goals:** NO new SUT runs (replay only — $0 OpenRouter; any
nonzero OpenRouter spend needs owner OK); no bank changes, no v2.5, no new
items; OAuth judges NEVER join the scoring panel or leaderboard tables (audit
instruments only; config-break rule applies); no pre-registration framing
(vault v1.x directive). All results EXPLORATORY / NON-QUOTABLE.

**Owner decisions locked (2026-07-17):** (1) J5 model = try `gpt-5.5` pin with
a 3-call smoke; if 400 invalid_request, fall back to verified `gpt-5.6-sol`
and DISCLOSE (same pattern as the s7 glm-4.7→glm-5 substitution). (2) Sample
scope = the priority ladder in Phase 1/2 below; J5 cuts from the bottom on
time; **every J5 sample must have a J4 twin**.

## Where things stand (as of 2026-07-17, commit `04785df06`)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (paths
  relative to it). Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python 3.14;
  the shared vault `.venv` is 3.9 and CANNOT run inspect-ai).
  `export OPENROUTER_API_KEY=dummy` suffices for imports/tests — this session
  needs NO live OpenRouter calls. **80 tests green**
  (`.venv-v2/bin/python -m pytest tests -q`).
- **Bank v2.4** (manifest `data/BANK-VERSION.json`): 265 main (199 v1 + 29 s6
  + 37 s7) + 22 episodes; frontier core = 66 `-N-` items. Panel = median of
  gemini-2.5-flash + deepseek-chat + mistral-small-2603; last-match `GRADE: N`
  parser; excellence gate ON (main); grader retry wrapper GRADER_ATTEMPTS=3 in
  `src/wcf_grading.py` (post-wrapper quorum drops 1/1,742).
- **1,931 replayable s7 samples.** Every sample persists (a) the GRADE-FREE
  grading prompt at `scores['multi_scorer'].metadata['grading'][0]['content']`
  (role=user; this is the byte-exact replay instrument, anti-leakage by
  construction) and (b) all three incumbent judges' parsed grades at
  `scores['multi_scorer'].metadata['panel']['values']` = [g1 gemini,
  g2 deepseek, g3 mistral-small] — so incumbent per-judge grades cost $0.
  Inventory by log dir:
  - `logs/20260716-session7-epochs-core/` — **594** (66 core items × 3 SUTs
    {qwen3.7-plus, claude-haiku-4.5, gpt-5-mini} × 3 epochs; the headline set)
  - `logs/20260716-session7-roster-{gemini,mistral,glm,minimax}-main/` — 4×265
    (full v2.4 main incl. the ~130 v1-derived ceiling items; single draw)
  - episode strata: `…-roster-*-episodes/` (3×22), `…-gemini-episodes/` (22),
    `…-roster-*-panel/` + `…-gemini-panel/` (4×9), `…-qwen-ramp/` (27)
  - `logs/20260716-session7-gate-main/` — 126 (42 s7 items × 3 SUTs)
- **Judge-analysis baselines to cite (do not recompute):**
  `analysis/20260716-streamB-agreement-stats.json` (3-judge max pairwise MAD
  12.32, rank_flip False, single-grader unstable → panel adopted);
  `analysis/20260716-session5-panel-health.json` (house-style vs panel median:
  gemini −6.48 overall / −11.2 contested / −15.7 anchor; deepseek +1.18;
  mistral-small +1.95; gemini harshness is SUT-dependent);
  kin DiDs: deepseek self-kin +1.67 [+0.14,+3.27], mistral family +0.97 ns
  (`analysis/20260716-session5-kin-stats.json`), gemini +0.72 [−2.55,+4.22]
  (`analysis/20260716-session7-gemini-kin-did.json`). Item-discrimination
  context: `reports/20260716A-Report.md` (top discriminators COMP-N-015 spread
  70, COMP-N-020 45, CONT-N-022 39; v1 layer 60% ceiling).
- Session-7 consolidated report: `reports/20260716-session7-report.md`.

## OAuth channels (verified operational 2026-07-17; read these BEFORE coding)

### J5 — Codex CLI (`codex exec`, ChatGPT OAuth)

Canonical hardened adapter (READ AND ADAPT — do not modify v1):
`../WCF-Benchmark/04-HARNESS/wcfbench/codex_oauth_judge.py`. Empirical bringup
log with the rationale for every flag:
`../../../INNOVATION/40-BUILDS/t1-runner-provisional/20260709-cli-bringup-log.md`.
Invocation shape:

```
codex exec --ephemeral --ignore-user-config --ignore-rules \
  --sandbox read-only --skip-git-repo-check \
  -c model=<PIN> -c 'model_reasoning_effort="medium"' \
  -c 'web_search="disabled"' -c 'features.multi_agent=false' \
  --json --output-schema <schema.json> -o <out.txt> -C <empty-tmpdir> \
  PROMPT </dev/null
```

Hard-won gotchas (do not rediscover): stdin `</dev/null` is MANDATORY (else
hang on "Reading additional input from stdin"); explicit `gpt-5`/`gpt-5-codex`
400 on subscription accounts — `gpt-5.6-sol` verified working with explicit
pin, `gpt-5.5` pin UNTESTED (hence the smoke-first ruling); harmless stderr
noise (models-cache error) — signal is the JSONL event stream + `-o` file;
`turn.failed`/`error` events = failure, `turn.completed` required; reject any
tool-call events; **concurrency ONE**, exponential backoff on {"rate limit",
"429", "too many requests", "quota"}; NO unattended overnight bulk loops
(supervised background with completion checks); no temperature control —
reasoning-effort pin only, record it in the report header.

### J4 — Claude CLI (`claude -p`, Claude OAuth)

`claude -p --model opus` non-interactive; embed the replay grading prompt as
the user prompt (it is self-contained; no system flag needed). Reference
client: `../Christian-Ethics-Benchmark/harness/walkworthy/cli_backends.py`
(`ClaudeCLIClient` — note it embeds system content in the user prompt and has
an injectable subprocess runner for offline tests). Moderate parallelism
(≤4 workers). This is OAuth subscription, NOT the Anthropic API — compliant
with the vault agents-over-API directive. Record the resolved opus model id in
the report header.

### Both judges

- Feed the persisted grading prompt VERBATIM. Anti-leakage: judges never see
  panel values, each other's grades, or SUT identity; nothing appended except
  (if needed after smoke) a minimal output-format reminder, identical for both
  judges and disclosed.
- Parse: strict last-match `GRADE: N` (0–100), same regex as the harness
  (`src/wcf_grading.py` GRADE_PATTERN). Unparseable → exactly ONE re-prompt,
  then log as parse-failure. **Per-judge parse-fail rate is itself a result.**
- Raw grades: append-only JSONL per judge
  (`analysis/20260717-session8-{j4,j5}-raw.jsonl`: sample_key, stratum, grade,
  attempt, wall_ms, model_id) so interrupted runs RESUME (skip already-graded
  keys on restart).

## Work plan

### Phase 0 — ground state + smokes ($0 OpenRouter)

80 tests green. Extraction script `analysis/session8_extract_replay.py` dumps
all needed rows to `analysis/20260717-session8-replay-rows.jsonl` (sample_key =
item_id|sut|epoch|logdir, stratum tag, prompt, panel values, prompt token
estimate). Pre-measure episode-prompt lengths; flag any that risk CLI context
truncation (analyze that stratum separately; exclude truncated from headline
analyses). Smoke both channels with 3 calls each on epochs-core samples:
- J5: attempt `-c model=gpt-5.5`; on 400 → fall back `gpt-5.6-sol`, DISCLOSE
  the ruling in the report header (this is the pre-agreed branch).
- J4: `claude -p --model opus`; confirm parseable GRADE output.
Record smoke transcripts under `analysis/20260717-session8-smoke/`.

### Phase 1 — J4 (Opus) superset run

Strata (all of): S1 epochs-core **594**; S2 ceiling stratum **~100** (from the
4 roster-main runs: sample ~25 v1-derived items that are ceiling per
`reports/20260716A-Report.md` methodology × 4 SUTs); S3 episodes **~85**
(roster episodes 3×22 subsample + panels + qwen-ramp subsample — include
multi-turn-history prompts deliberately). ≤4 workers, checkpointed, supervised.

### Phase 2 — J5 (GPT) priority ladder (serial, cut from the bottom)

1. S1a: epochs-core epoch-1 only, all 3 SUTs — **198**
2. S1b: epochs 2–3 for the haiku + gpt-5-mini pair — **+264 → 462** (gives
   3-epoch averaging on the headline pair)
3. S2': ceiling subsample — **+60 → 522**
4. S3': episode subsample — **+40 → 562**
Budget ~25 s/call effective; ~4–5 hr supervised for the full ladder. Every J5
sample already has its J4 twin from Phase 1 (assert this before analysis).

### Phase 3 — analysis ($0, logs + raw JSONL only)

One script family `analysis/compute_session8_meta_judging.py` →
`analysis/20260717-session8-meta-judging-stats.json`:

1. **House-style:** per-judge delta vs incumbent panel median on identical
   samples — J4, J5, and each incumbent (from persisted panel values) —
   overall + by mold (contested/complicit/steadfast/v1-kinds) + by SUT.
   Compare against the s5 baselines quoted above.
2. **5-judge reliability:** pairwise Spearman / ICC(2,k) / MAD across
   {gemini, deepseek, mistral-small, J4, J5}, overall and by mold (expect
   contested to be the low-agreement mold — test it).
3. **Headline sensitivity (PRIMARY):** recompute the gpt-5-mini−haiku paired
   per-item gap + MDD80 (2.80×SE convention, epochs-averaged where available)
   under: each incumbent alone / J4 alone / J5 alone / incumbent panel-3
   (reference) / 5-judge median. **Framing rule (pre-stated): single-judge
   rows are GAP-STABILITY evidence (sign + magnitude band) — expected
   single-judge MDD80 ≈ 7–8, so do NOT make per-judge significance claims.
   The 5-judge median is the one re-derivation that may tighten MDD80 below
   the panel-3 value; it is the headline sensitivity anchor.**
4. **Cross-kin DiD:** per-sample d = J4 − J5 on identical samples;
   τ̂ = (d̄_haiku − d̄_qwen) − (d̄_gpt5mini − d̄_qwen), qwen = mutual non-kin
   anchor. CI: item-clustered bootstrap (resample the 66 items with
   replacement, keep all SUT×epoch rows within an item, 5,000 reps, percentile
   95% CI). Positive τ̂ = symmetric mutual in-group favoritism. Also report
   the two one-sided components separately.
5. **Item-level artifact check:** for the top-10 s7 discriminators (COMP-N-015,
   COMP-N-020, CONT-N-022, COMP-N-008, COMP-N-022, COMP-N-004, COMP-N-007,
   COMP-N-023, COMP-N-024, COMP-N-021): does the per-item SUT spread persist
   under J4/J5, or is it an incumbent-judge artifact?
6. **GATE-cap consistency:** on cap-eligible samples (incumbent grades ≤40
   present), per-judge cap application rate + agreement matrix (grades ≤40 as
   the cap signal).
7. **Contamination bound (small):** blinded spot-check — for ~20 samples,
   strip stylistic tells if present and re-grade with one judge; report the
   delta as a bound on SUT-identity contamination of the kin estimate.

### Phase 4 — the ONE consolidated report

`reports/20260717-session8-meta-judging-report.md`, exactly this skeleton:
1. Executive summary + method (table: 5 judges × n graded / mean / house-style
   offset / parse-fail %; judge configs: model pins, effort, CLI versions)
2. House-style calibration (by mold + SUT; s5 baselines as reference rows)
3. Five-judge reliability (Spearman/ICC/MAD matrix, by mold)
4. **Headline sensitivity** (gap/SE/MDD80/sign table across judge configs —
   the decision-relevant table of the study)
5. Cross-kin symmetry (d̄ by SUT, τ̂, CI, components)
6. Item-level artifacts (top-10 discriminators × 5 judges)
7. GATE-cap consistency
8. Threats, limitations, and the recommended judging configuration for v2.5+
   (panel keep/change recommendation with evidence)
Every table cites bank v2.4 + panel + parser + judge configs. OAuth-judge
numbers never appear in a leaderboard-style table with panel-median rows
without an explicit instrument-difference banner.

### Phase 5 — close ($0)

Memory update (`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md`
+ MEMORY.md index line); pathspec commit →
`git pull --rebase --autostash` → push → `git rev-list --count
origin/main..HEAD` = 0. No handoff docs (retired 2026-07-15).

## Binding conventions (do not relitigate)

1. All results EXPLORATORY / NON-QUOTABLE; rubric conformity, not accuracy.
2. OAuth judges are AUDIT instruments — never merged into the panel, the
   leaderboard, or bank scoring; results live in the meta-judging report only.
3. Report immutability: new dated files only; never edit existing dated
   reports/JSONs. No deletions ever (`mv` to `RECYCLE-BIN/`). Never modify
   `../WCF-Benchmark/` (v1) or `../Christian-Ethics-Benchmark*/` — read-only
   references.
4. $0 OpenRouter this session (dummy key for imports); OAuth usage is
   subscription — respect concurrency-one + backoff on codex, ≤4 workers on
   claude, no unattended overnight loops.
5. Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel
   sessions — commit with explicit pathspecs; leave stash entries alone.
6. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every Agent
   dispatch; heavy lifting in scripts, Fable adjudicates in the main loop.
7. The two locked owner decisions (gpt-5.5-smoke-with-fallback; priority
   ladder) are binding — do not re-ask.

## Gotchas (carry-forward; do not rediscover)

- `read_eval_log(f, header_only=True)` — no `read_eval_log_headers` in 0.3.246.
- zsh: `echo ====` triggers =cmd expansion — quote it.
- Codex: stdin `</dev/null` mandatory; config drift is real — always
  `--ephemeral --ignore-user-config`; stderr noise harmless; 400 on wrong
  model pins is the failure mode the smoke exists for.
- Claude CLI: no system-prompt flag needed here — the replay prompt is
  self-contained; embed as user prompt (walkworthy `ClaudeCLIClient` pattern).
- The grading prompt contains the full rubric + anchors and can exceed 6k
  chars (WHOLE-C8-W306 is 6,103); episode prompts include multi-turn history —
  pre-measure lengths before the episode stratum.
- Panel `values` are grader-ordered [gemini, deepseek, mistral-small]; quorum
  metadata `n_valid` < 3 marks incumbent grader dropouts — exclude those
  samples from per-incumbent-judge comparisons (median-only samples), and say
  so in the report.
- Background agents may rest while their run lives on: checkpoint + resume by
  sample_key, check for duplicates before re-firing.

## Acceptance checklist

- [ ] Phase-0 smokes recorded; J5 model-pin ruling made and disclosed
      (gpt-5.5 or gpt-5.6-sol fallback).
- [ ] J4 superset graded (594 + ~100 + ~85; parse-fail rate reported).
- [ ] J5 ladder graded to at least S1a (198); rung reached documented; every
      J5 sample has a J4 twin.
- [ ] All 7 analyses computed into the stats JSON; headline-sensitivity table
      present with the gap-stability framing (no single-judge significance
      claims).
- [ ] Cross-kin τ̂ with item-clustered bootstrap CI reported.
- [ ] ONE consolidated report shipped at
      `reports/20260717-session8-meta-judging-report.md` with the 8-section
      skeleton; judge configs in the header.
- [ ] $0 OpenRouter spend confirmed; memory updated; pathspec commit → rebase
      → push → 0 unpushed.
