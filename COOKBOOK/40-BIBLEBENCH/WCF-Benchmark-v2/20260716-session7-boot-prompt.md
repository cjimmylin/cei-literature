# WCF-Benchmark-v2 — Session 7 Boot Prompt

> Paste this as the opening prompt of a fresh session. It is self-contained.
> Read this file top-to-bottom before touching anything.

## Mission

**Expand the frontier-core index (29 → ~65 items) with a 50-item authoring wave
concentrated in the two molds that demonstrably discriminate at the frontier,
gate it, freeze v2.4, then run the three-track measurement program: epochs on
the expanded core, the google SUT with its mandatory kin piggyback, and three
new roster SUTs.** Session-6 earned this scope with data: the frontier-core
index pulled tier-1 off the ceiling (means ~74) and separated tiers sharply,
but within-tier-1 it found **three-way parity** (qwen ≈ haiku ≈ gpt-5-mini,
gaps ≤ 1.1 vs MDD80 ≈ 11–15) — an honest result that is nonetheless
underpowered. Two levers shrink the MDD: more core items (this session's
authoring) and epochs (this session's measurement).

**Explicit non-goals:** no quoting v2.4 numbers against v2.3/v2.2/earlier
scales (each manifest is its own instrument); no new crosswind, aggravate, or
episode items *for frontier purposes* (s6 data: crosswind 0/8 and episodes 0/9
nonzero tier-1 gaps — both molds are RLHF-soluble at tier-1); no editing v1
YAML ever; no editing existing dated reports.

Owner decisions locked (2026-07-16): (1) budget ceiling **$20**, same
autonomous-run rule, token-attribution accounting; (2) authoring volume =
**~50 drafted** (25 contested wave-2 + 25 frontier-open); (3) measurement =
**all three tracks** (epochs + google/kin + new roster SUTs), priority in that
order, cut from the bottom.

## Where things stand (as of 2026-07-16, session-6 close, commit `126260619`)

- Project root: `CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (paths
  below relative to it). Harness: Inspect AI 0.3.246 in `.venv-v2/` (Python
  3.14; the shared vault `.venv` is 3.9 and CANNOT run inspect-ai). API key:
  `set -a && source ~/.codex/secrets/openrouter.env && set +a`. The key's
  total cap was raised 2026-07-16 after it blocked the first s6 roster attempt.
- **Bank = v2.3** (manifest `data/BANK-VERSION.json`): 228 main (199
  v1-derived + 29 session-6) + 22 episodes. Converter chain: v1 YAML →
  `yaml_to_jsonl.py` → session4 → session5 → session6 patches +
  `session6_new_items` (G4 filter inside `bank_items()`). Panel = median of
  gemini-2.5-flash + deepseek-chat + mistral-small-2603; last-match parser;
  excellence gate default ON (main only). **71 tests green**
  (`.venv-v2/bin/python -m pytest tests -q`; `export OPENROUTER_API_KEY=dummy`
  suffices for imports/tests).
- **s6 leaderboard** (`reports/20260716-session6-roster-leaderboard.md`, bank
  v2.3, EXPLORATORY): full-bank qwen3.7-plus 94.4 > claude-haiku-4.5 93.6 >
  gpt-5-mini 90.4 > deepseek-v3.2 87.6 ≫ gpt-4o-mini 76.9. **Frontier-core
  (29 items): gpt-5-mini 74.9 ≈ qwen 74.3 ≈ haiku 73.7 (all pairwise ns) ≫
  deepseek-v3.2 58.0 (SIG, kin-robust) ≈ 4o-mini 53.2.** Escalation panel
  (9 G4-excluded 4-turn episodes, STANDALONE by owner decision — never merged
  into the full-bank mean): haiku 100 / gpt-5-mini 100 / deepseek 96 /
  **qwen 91.9** (the only frontier model to slip on a ramp in either draw —
  draw-unstable, resolve with epochs) / 4o-mini 78.6.
- **What discriminates (s6 gate + roster evidence):** contested items are the
  frontier engine — 8/15 (53%) nonzero |qwen−haiku|, tier-1 means 71–75, the
  only never-saturating kind. Frontier-open runs 36% when built on the
  surgical-decline complicit and vow-vs-revisable steadfast sub-molds. Style
  models = the 18 nonzero-gap items in
  `analysis/20260716-session6-gate-results.json` (largest gaps: COMP-N-002 50,
  COMP-N-005 41.5, STED-N-003 36, COMP-N-008 35, COMP-N-007 33, CONT-N-005 30).
- **Key artifacts:** `reports/20260716-session6-authoring-brief.md` (M1–M5
  discrimination mechanisms + form-rules — REUSE as the drafting spec, amended
  per Phase 1 below), `reports/20260716-session6-review-adjudication.md` (kill
  classes + the D1c replacement spec — the contested wave-2 template),
  `reports/20260716-session6-report.md` (consolidated),
  `reports/20260716-session6-item-provenance-log.md`,
  `analysis/20260716-session6-roster-stats.json` (leaderboard + pairwise +
  quorum ledger), `analysis/compute_session6_roster_stats.py`,
  `analysis/session6_g1_check.py` + `analysis/session6_gate_eval.py` (adapt as
  s7 versions), kin method: `analysis/20260716-session5-kin-stats.json` +
  `reports/20260716-session5-v22-design.md` §6.
- Spend history: s3 $5.01 / s4 $10.32 / s5 ≤$7.68 / **s6 $9.86 attributed**
  (credits deltas ran 2–30× higher — shared-key concurrent sessions; the
  token-attribution method from `.eval` `stats.model_usage` is the sanctioned
  accounting).

## Work plan — author, gate, freeze, then the three-track program

### Phase 0 — ground state ($0)

Credits snapshot (upper bound only); 71 tests green; note the gemini-grader
transient (s6: 52/1,295 samples lost g1=gemini-2.5-flash, ~4%, evenly spread —
median absorbed all). **Rule for s7: if g1 failures exceed ~2% in the first
live run, add a retry wrapper at the `bounded_grader` layer (disclosed code
change; grading semantics unchanged); nova-pro-v1 is the validated kin-free
substitute if gemini degrades outright.**

### Phase 1 — authoring (~$0 API; the bulk of the session)

Target: **25 contested (CONT-N-023…047) + 25 frontier-open (~13 complicit
COMP-N-012…, ~12 steadfast STED-N-011…)** — ONLY the two proven frontier-open
sub-molds: complicit surgical-decline-with-deliverable and steadfast
vow-vs-revisable-distinction. Study the 18 nonzero-gap s6 items FIRST.

- **Provenance (binding):** new items in `data/session7_new_items.json` +
  loader `convert/session7_new_items.py` (mirror the session-6 loader
  including the `G4_EXCLUDED`/`bank_items()` pattern); every item carries
  `authored: session-7` + `author_batch`. Bank bumps to **v2.4 only at
  Phase 3.**
- **Form rules from birth** (the s6 brief §3–§4 applies wholesale) **plus the
  s6 kill lessons as hard rules:**
  - *Contested dominated-pair rule:* each side carries ≥1 UNCANCELLED WLC Q151
    aggravation the other lacks, on DIFFERENT heads (benchmark: CONT-N-013's
    H1+H4-vs-H3 shape). Never pair a mitigation-loaded side against a
    multi-aggravator side — 7 of 15 s6 contested drafts died exactly there.
    Drafters must write down the strongest case for "(a) worse" AND "(b)
    worse" per item and redesign if either clearly wins.
  - *No stem hedges:* "settle", "sort cleanly", "resolve", "incommensurable"
    are banned from stems; the asker demands a confident pick.
  - *Every item has a manner line* (an s6 drafter miss slipped BOTH blind
    reviewers and was caught only by the G1 script).
  - Single-judgment criteria; ≤6 rubric lines (≤8 contested); self-contained
    stems (never reference an "attached" artifact); R1 gates + R2 equivalence
    lists; no direct-lie forks; no unanchored quality adjectives.
- **Pipeline (same as s6 — it worked):** opus drafters (explicit `model` on
  every dispatch; agents EXECUTE files, not plans) → **≥2 blind adversarial
  reviewers per item** (item+rubric only; anti-leakage isolation; lens A =
  form/gradeability, lens B = construct/difficulty/doctrine) → **Fable
  adjudicates every kill/repair in the main loop** (s6 kill ratio was 14.8% —
  if nothing dies, the review was theater) → repair agents → fresh 2-reviewer
  round on any substantively-rebuilt content → G1 mechanical gate (adapt
  `analysis/session6_g1_check.py`) → G3 mockllm plumbing ($0).

### Phase 2 — frontier-core GO/NO-GO gate (~$2)

All accepted new items × **qwen3.7-plus + claude-haiku-4.5 + gpt-4o-mini**,
panel default, mockllm smoke first. **PRE-STATED criterion (unchanged from s6
for continuity — do not relitigate): GO ⟺ ≥⅓ of new items show nonzero
|qwen−haiku| AND unscored=0.** Floor check: all-SUT-zero items get re-reviewed,
not silently kept. NO-GO ⇒ one authoring iteration (Fable adjudicates what
failed), re-gate changed items only; still NO-GO ⇒ STOP, no measurement spend
on the new items (the three-track program may still run on the v2.3 core —
flag to owner first).

### Phase 3 — v2.4 freeze ($0)

Apply G4 strictly (an item enters the bank only if scoreable AND some tier-1
answer < 100 in the gate); set `G4_EXCLUDED` in the s7 loader; wire
`session7_new_items` into `convert/yaml_to_jsonl.py` (BANK_VERSION "v2.4",
sources list gains the 4th entry); regenerate; write the new manifest. Update
the two pinned tests (`tests/test_converter.py::test_jsonl_counts_and_split`,
`tests/test_session5.py::test_manifest_exists_and_wellformed` — same edits s6
made for v2.3) + add `tests/test_session7.py` (mirror `test_session6.py`).
All tests green before any measurement run.

### Phase 4 — three-track measurement (~$12–14; priority order, cut from the bottom; never cut items or epochs before SUTs)

1. **Epochs on the expanded frontier-core (~$5–6):** the full core (29 v2.3 +
   s7 survivors, ~60–65 items — they all live in `wcf_main.jsonl`; run them
   via a dedicated task or `--sample-id` selection) × the frontier trio
   (qwen3.7-plus, claude-haiku-4.5, gpt-5-mini) at **`--epochs 3`** (mean
   reducer). Deliverable: the within-tier-1 statement with epochs-shrunk MDD80
   (~√3 smaller per-item noise + more items ⇒ target MDD80 ≈ 5–6). Also:
   **qwen ramp instability probe** — `wcf_new_episodes` × qwen only ×
   `--epochs 3` (~$0.5) to resolve the 91.9-vs-100 draw flip.
2. **Google + mandatory kin piggyback (~$2.5):** gemini SUT (re-verify the
   live slug/price first) on the v2.4 bank, AND the gemini-free-panel DiD:
   re-grade a sample of gemini-SUT responses under panel = deepseek-chat +
   mistral-small-2603 + nova-pro-v1, with a non-kin control SUT, per the s5
   DiD method (`analysis/20260716-session5-kin-stats.json` is the reference
   implementation). **Google numbers are quotable ONLY after the DiD verdict**
   (s5 ruling; disclose the measured bound either way).
3. **New roster SUTs (~$5):** mistral-large-2512 (kin: disclose the measured
   +0.97 family bound), glm-4.7, minimax-m3 on the full v2.4 bank + episodes
   at `pressure_variant=item` + the standalone escalation panel. Re-verify all
   slugs/prices live before spending; forecast reasoning-verbose SUTs at 2.5×
   completion tokens.
- **Reporting form (binding):** v2.4 leaderboard = (a) full-bank mean +
  (b) frontier-core index (epochs-averaged where available, own MDD quoted) +
  (c) standalone escalation panel. Every table cites bank_version v2.4 +
  panel + parser. Kin disclosures: deepseek rows ±1.7; mistral rows the
  measured bound; google conditional on its DiD. Adapt
  `analysis/compute_session6_roster_stats.py` (note its LOG_DIRS constant and
  the panel-items-never-in-core assertion).

### Phase 5 — close ($0)

Consolidated `reports/2026MMDD-session7-report.md` (+ per-phase dated
reports); memory update
(`~/.claude/projects/-Users-jimmy-lin-Documents-CEI-Literature-Vault/memory/20260715-wcf-v2-inspect-build.md`
+ MEMORY.md index line); pathspec commit → `git pull --rebase --autostash` →
push → `git rev-list --count origin/main..HEAD` = 0.

## Binding conventions (do not relitigate)

1. All results **EXPLORATORY / NON-QUOTABLE**; 0–100 panel-median rubric
   conformity, NOT accuracy. No pre-registration framing (vault v1.x
   directive).
2. **Bank-versioning rule:** every number cites bank_version + panel + parser;
   different manifests never share a table without a config-break banner.
   v2.4 is a new scale.
3. **Kin rules (s5 ruling):** deepseek ±1.7 within-tier sensitivity; mistral
   bound disclosed; google quotable only after its own DiD (this session runs
   it). command-r-08-2024 never in audit panels; nova-pro-v1 is the validated
   substitute.
4. **Never quote single-draw item-level numbers**; epochs means are fine.
5. **No deletions ever** (`mv` to `RECYCLE-BIN/`); never edit `../WCF-Benchmark/`
   (v1) or existing dated reports; never touch the shared vault `.venv`; item
   changes ONLY via converter layers / new-item sources; per-item
   provenance/edit logs mandatory.
6. Handoff docs/skills RETIRED (2026-07-15): end with dated reports + commits +
   memory update only.
7. Git: nested repo `CEI-Lit-WS/`, shared trunk `main`, active parallel
   sessions. **Commit with explicit pathspecs**
   (`git commit -m "..." -- <paths>`). Leave existing stash entries alone.
8. Budget: proceed autonomously if total session forecast ≤ **$20**; ask Jimmy
   above that. **Account by token attribution from `.eval`
   `stats.model_usage`, never by credits delta alone** (s6: delta ran 2–30×
   over attributed due to concurrent same-key sessions). Pad forecasts:
   anchor-enlarged grading prompts, ~9% excellence-gate block, reasoning SUTs
   at 2.5×; s6 ran $2.3 over its roster forecast on qwen/gpt-5-mini reasoning
   tokens.
9. Model tiering per `~/.claude/CLAUDE.md`: explicit `model` on every
   dispatch; agents EXECUTE; anti-leakage isolation for comparison work;
   **Fable adjudicates in the main loop.**

## Gotchas (sessions 1–6; do not rediscover)

- `model_graded_qa(instructions="")` silently falls back to C/P/I — always
  pass the numeric instructions file.
- Multi-grader `model=[...]` reduces by MODE — degenerate on 0–100; the
  codebase uses `panel_median` (`src/wcf_grading.py`). Don't "simplify" it.
- `inspect score --model` overrides the SUT, not the grader — re-grade via
  replay of `scores[...].metadata['grading'][0]['content']` (grade-free by
  construction; this is also the kin-DiD mechanism).
- `eval-set -T task_args` apply to ALL tasks in the set → run main and
  episodes as SEPARATE eval-sets when passing episode-only args.
- `--limit N` = first N file-sorted samples (skewed); use `--sample-id` for
  diverse smokes. mockllm → all unscored = the PASS condition for plumbing.
- `OPENROUTER_API_KEY` must be in env even for imports/tests (dummy fine).
- Always `python -m pip`, never bare pip. Never `rm` — the vault hook denies
  whole commands containing deletion-pattern strings; rephrase.
- qwen3.7-plus: `<think>` prevalence flips between runs; most verbose SUT;
  reasoning-token cost driver. qwen under `inspect eval` can leave
  `status=started` partial logs — audit completeness, re-run missing
  `--sample-id`s, merge last-file-wins (s6 roster2 had none, s5 did).
- Panel provenance in `Score.metadata['panel']` = {n_valid, values},
  grader-ordered g1=gemini/g2=deepseek/g3=mistral-small. Keep the quorum
  check in every completeness audit. **s6: g1 (gemini) dropped ~4% of samples
  as a provider transient — evenly spread, median absorbed; see Phase-0 rule.**
- One grading standard (WHOLE-C8-W306) exceeds 6000 chars; excellence gate
  adds ~650 tokens/prompt — include both in cost forecasts.
- Heredoc + pipe collision: `curl ... | python - <<'EOF'` feeds the JSON to
  python as the script — fetch inside python (urllib) instead.
- Sub-threshold-outlier taxonomy leak: hard cutoffs misfile the same
  phenomenon one notch below — always look just under every threshold.
- **OpenRouter 403 "Key limit exceeded (total limit)" masquerades as eval-set
  retry churn** — every attempt errors and eval-set relaunches; STOP the runs
  (TaskStop) and check the key, don't wait it out (s6).
- **Credits-delta vs token-attribution can diverge 2–30×** under concurrent
  same-key sessions — attribute from `stats.model_usage` BEFORE any budget
  decision (s6).
- inspect_ai 0.3.246 has no `read_eval_log_headers` — use
  `read_eval_log(f, header_only=True)`.
- Background-eval agents may rest while their eval lives on: PID watcher +
  continuation dispatch, but check for self-resume duplicates first.
- Session-6 episodes machinery: items with `pressure_turns` (list of 3)
  ALWAYS run their 4-turn ramp in `scripted_dialogue` regardless of
  `pressure_variant`; old items are byte-identical. The 9 s7-relevant panel
  episodes live in `data/wcf_new_episodes.jsonl` via the `wcf_new_episodes`
  task.

## Acceptance checklist

- [ ] Phase-0 ground state + gemini-grader health rule applied if triggered.
- [ ] Authored-item inventory: drafted / killed / accepted per kind (25+25
      target), kill ratio stated; all accepted items pass G1–G3 with
      `authored: session-7` provenance.
- [ ] Gate run and judged against the PRE-STATED criterion (≥⅓ nonzero
      |qwen−haiku|, unscored=0); verdict + branch recorded.
- [ ] v2.4 manifest frozen (or NO-GO findings report); pinned tests updated +
      test_session7.py added; all green.
- [ ] Track 1: epochs×3 within-tier-1 statement on the expanded core with
      epochs-shrunk MDD80; qwen ramp-instability probe resolved.
- [ ] Track 2: google DiD verdict + explicit quotability ruling for the
      gemini SUT row.
- [ ] Track 3 (as budget allows): mistral-large / glm-4.7 / minimax-m3 rows
      with kin disclosures; cuts documented if made.
- [ ] v2.4 leaderboard delivered as full-bank mean + frontier-core index +
      standalone escalation panel, citing bank_version/panel/parser.
- [ ] Total spend ≤ $20 by token attribution (credits delta disclosed as
      upper bound); new dated reports; memory updated; pathspec commit →
      rebase → push → 0 unpushed.
