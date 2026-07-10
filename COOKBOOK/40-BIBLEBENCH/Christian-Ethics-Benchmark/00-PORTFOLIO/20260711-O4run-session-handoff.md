<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Session O4-RUN Handoff (2026-07-11, Opus) → Jimmy labels / O5

**This session (Opus, EXECUTION):** ran the LIVE O4 measurement and built/validated the
descriptive rendering pipeline. Step 0 (live validation slice) PASSED with zero bugs; the
full ≥6-model panel LAUNCHED (resumable). NO gate VERDICTS, NO item kills, NO release
claims were produced (all O5). FIX-MECHANICS-ONLY held; no item edited from performance.

> **Status line (update at panel completion):** panel = RUNNING at handoff-write time.
> See "Panel status" below; if this still says RUNNING, the panel did not finish in-session
> — resume per the commands here (nothing is lost; the run is per-(item,model) resumable).

---

## What LANDED this session

### Step 0 — live validation slice (DONE, zero bugs)
`runs/20260711-o4-validation/` (stopped after mechanics confirmed; scored_items gitignored).
Confirmed live, on real records (SUT1 = gpt-4.1 across all 10 designs + partial deepseek):
- **0 schema errors** across all records.
- **per_admin twins scored**: 03 (expressed/revealed), 04 (alpha/beta), 08 (overt/covert
  guardrail_state), 10 (N/U treatment/prudence/contempt/duality). **09 per_seat** (seat_A/
  seat_B floor_compliance + owes_direction). **07 terminal turn scored** (6-turn dialogue,
  last unit `terminal:true`).
- **PR-3 fields all present & populated**: `scalar_by_judge`, `scalar_adjudicated`,
  `refusal_reason`, `refusal_lexical`, `lexical_refusal_override` (per admin label).
- **06/09 references reach the judges** — proven offline deterministically (anchor text
  embedded in `assemble_rubric_prompt`; 06 = 7/31 anchored, 09 = 34/34) AND live (09
  anchored items scored).
- Minor note (non-blocking): the coarse illustrative `scalar_adjudicated` can differ from
  `scalar_by_judge` (03 case: [0.25,0.25]→0.5); it is explicitly "never a headline"
  (`outcomes.py`) — the §B metrics come from `per_unit`, not this scalar.

### Tooling built + validated (committed)
- `harness/render_o4_report.py` — DESCRIPTIVE/PROVISIONAL O4 report renderer over the
  tested `metrics.compute_all` + `gates_o4.compute_o4_gates`. Gate READINGS only
  (verdicts=O5). G9 headline (say_do_gap/covert_overt_gap) enforced; home-advantage
  full-vs-minus-generator rows; S01 fallback + G3 power-limit disclosures; PANEL-INCOMPLETE
  tolerant (loud banner; degrades G9 to a warning when a headline design is absent).
- `harness/merge_panel.py` — concatenate per-SUT resumable runs → one combined dir +
  aggregate cost/defects/schema errors (P0-pilot per-SUT→merged pattern).
- `harness/run_o4_panel.sh` — the panel launcher (6 per-SUT processes, resumable).
- **Full downstream pipeline dry-run PASSED on partial live data**: merge → metrics →
  gates_o4 (incl. G3 with the real capability composite + 6 models) → render →
  `label_sample` draw/CSV/packet all execute cleanly.

### Capability battery (§3.3) sourced for G3 (was never pinned)
`00-PORTFOLIO/20260711-capability-battery-scores.json` (+ `-SOURCES.md`): O4-time public
leaderboard snapshot, 6 models × 6 benchmarks, per-cell citations, 14/36 cells honestly
`null` (no fabrication). Composite = the FROZEN method (mean of min-max-normalized available
cells; RULER auto-dropped as a single-value column). Implied capability ranking (the
load-bearing output): **claude-sonnet-4 > gemini-2.5-pro > gpt-4.1 > deepseek > llama >
mistral**. Caveats (sparse coverage inflates claude 3/6-all-high; GAIA apples-to-oranges;
mistral-2512→2411 substitution; n=6 ⇒ ρ noisy) are carried into the report.

### O4 roster (SET, §E-compliant — from the 2026-07-11 reliability probe)
6 SUTs: `openai/gpt-4.1`, `google/gemini-2.5-pro`, `anthropic/claude-sonnet-4`,
`deepseek/deepseek-chat`, `mistralai/mistral-large-2512`, `meta-llama/llama-3.3-70b-instruct`.
Judges (frozen pair): `openai/gpt-4.1-mini` + `google/gemini-2.5-flash`. State classifier:
default `openai/gpt-5.6-terra` (pinned command leaves `--classifier-model` unset; proven
valid on OpenRouter). Tie-breaker (3rd family): `mistralai/mistral-large-2512` — **NOT
wired into `run_panel` this pass** (deferred, lower priority); disagreement cells land as
`pending_adjudication` → human Part-B (protocol §6). Home-advantage handled in the report
(full panel AND panel-minus-generator-family rows).

---

## Panel status (UPDATE at completion)

- **Run dirs:** `runs/20260711-o4-{gpt41,gemini25pro,claude-sonnet4,deepseek,mistral-large,llama33}/`
  (per-SUT, resumable) → merged into `runs/20260711-o4-panel/`.
- **PANEL STATUS:** _RUNNING at handoff-write time (~8% at write). FILL: final records / 2064,
  errors, cost, judge agreement._

### Resume / finish commands (idempotent; run from `harness/`)
```bash
# 1) RESUME the panel (re-run the launcher — each per-SUT scored_items.jsonl is the checkpoint)
bash run_o4_panel.sh
# 2) MERGE the 6 per-SUT dirs into the combined run
python merge_panel.py --out 20260711-o4-panel \
  --runs 20260711-o4-gpt41 20260711-o4-gemini25pro 20260711-o4-claude-sonnet4 \
         20260711-o4-deepseek 20260711-o4-mistral-large 20260711-o4-llama33
# 3) RENDER the descriptive report (PROVISIONAL — verdicts=O5)
python render_o4_report.py --run 20260711-o4-panel \
  --capability ../00-PORTFOLIO/20260711-capability-battery-scores.json \
  --panel 20260711-o4-panel --date 2026-07-11 \
  --out ../00-PORTFOLIO/20260711-o4-panel-report.md
# 4) DRAW Part A label sample (blind CSVs + instruction packets; ship wave 1 = 02/07/01)
python -m walkworthy.label_sample --run 20260711-o4-panel
```

---

## NEXT — Jimmy / O5 (NOT this session)
1. **Part A human labels** (~25–30 h; wave 1 = {02, 07, 01} first) + a 2nd labeler (or the
   disclosed test–retest fallback) → `judge_validation.py` → **G4** per design (RELEASE gate).
2. **06/09 blind reference scoring → G5** (06/09 stay PROVISIONAL until then).
3. **Perturbation batteries → G7.**
4. **O5 gate ADJUDICATION (Fable-preferred if a window recurs):** verdicts, kills/demotes,
   release per design; tie-breaker-judge wiring for `needs_adjudication` cells (or Part-B).
5. **5 one-liner ratifications:** PR-1(c "356 authored / 344 runnable"), PR-2 (ADVICE_SYSTEM
   frame), PR-3 (§6.4 interpretation), PR-4 (OpenRouter sanctioned), **PR-6** (near-agreement
   mean rule). None block.
6. **W4 fixes (deferred, low priority):** apply the review's mechanical relabels/re-anchors
   to A01/K01/E01 (+ re-key K01, + trim D01/L03/N01) in `…-W4-06-references-DRAFT.md` →
   Jimmy ratifies before they enter `DESIGNS/06-*.md`. 06 stays PROVISIONAL until G5 regardless.

## Standing cautions
- No gate VERDICTS / item kills / release claims here (all O5). FIX-MECHANICS-ONLY held.
- HOLDOUT never loaded (loader hard-refuses) / never committed. `runs/*/scored_items.jsonl`
  and `*-DRAFT.md` gitignored.
- ≥3 sessions share the git index: `git log -1` before staging; stage WALKWORTHY paths
  explicitly; never rewrite sibling commits; fast-forward pushes only.
