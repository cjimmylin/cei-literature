<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — Session O4-RUN Handoff (2026-07-10/11, Opus) → Jimmy labels / O5

**This session (Opus, EXECUTION):** ran the LIVE O4 measurement + built/validated the
descriptive rendering pipeline, caught + fixed a real mid-run scoring bug, produced the
dated PROVISIONAL report and the Part-A label sample. **NO gate VERDICTS, NO item kills, NO
release claims** (all O5). FIX-MECHANICS-ONLY held; no item edited from performance.

> **Bottom line (UPDATED — panel now COMPLETE):** full **6-model × 10-design panel =
> 2064/2064, 0 coverage gaps, 0 schema errors, $48.75**. The gemini-2.5-pro 07–10 402 block
> was cleared by a $20 OpenRouter top-up **plus** a backend `max_tokens` cap (the 402 was a
> per-request 65536-token *reservation* against the balance, not depletion). Final complete
> report = **`20260711b-o4-panel-report.md`** (supersedes the 94% `20260711-o4-panel-report.md`,
> which stays as an immutable snapshot). Part A drawn for **all 10 designs** (439 units). All
> pushed. Remaining is Jimmy/O5 only (labels, ratifications, gate adjudication).

---

## Commits this session (WALKWORTHY paths only; ≥3 sessions share the index)
- `d539e4961` tooling: merge_panel + render_o4_report
- `657631f8b` renderer partial-tolerance
- `cd51a7566` capability battery snapshot + handoff scaffold
- `a056e5a89` **fix: verdict_scalar None-safe (dropped 06/09 cells)** + 3 tests (258 green)
- `4a30e1a91` merged panel + dated PROVISIONAL O4 report
- `4d271e389` Part-A label sample (stable 01–06) + wave plan
- (+ this handoff finalize + memory)

## What LANDED (DONE)

### Step 0 — live validation slice (PASSED, zero bugs at the time)
Confirmed live on real records: 0 schema errors; per_admin twins (03/04/08/10), 09 per_seat,
07 terminal scored; all PR-3 fields populated; 06/09 references reach judges (proven offline
+ live). *Caveat that mattered:* the slice was stopped before SUT3 (claude) ran → it did NOT
exercise every SUT × design, which let the bug below through.

### Mid-run BUG found + fixed (a056e5a89)
`outcomes.verdict_scalar` crashed `float() … not NoneType` when a judge returned a **06
criterion** or **09 floor_compliance** as explicit `null`/non-numeric — `.get(k, default)`
doesn't default a present-but-null key, and the crash propagated through `score_item` so
`run_panel` dropped the WHOLE cell. Live impact: `claude-sonnet-4` dropped 5 of its 06 cells;
latent for all SUTs on 09. Root-caused + reproduced + fixed with `_safe_float` (mirrors the
existing 05/06-adjudicated guards); **+3 regression tests RED→GREEN, suite 258 passed**.
Panel restarted (resume); all 5 cells re-scored clean; final claude/gpt data 344/344, 0 errors.

### W6 — full panel (`runs/20260711-o4-panel/`, merged)
1937/2064 cells, **$37.81**, 17,394 calls, **0 schema errors, 0 classifier defects, 15 judge
defects (~0.4%)**. Per-SUT: gpt-4.1, claude-sonnet-4, deepseek, mistral-large, llama-3.3 =
**344/344 each, clean**. **gemini-2.5-pro = 217/344** (designs 01–06 complete; 07–10 =
127 cells un-run, all HTTP 402). Coverage: **designs 01–06 = full 6-model; 07–10 = 5-model.**

### W7 — dated report `00-PORTFOLIO/20260711-o4-panel-report.md` (DESCRIPTIVE / PROVISIONAL)
Gate READINGS only (verdicts=O5); scores PROVISIONAL pending G4; 06/09 pending G5. Loud
coverage-gap + per-model-coverage; G9 headlines (say_do_gap 03 / covert_overt_gap 08) incl.
nulls; home-advantage full-vs-minus-generator rows; S01 fallback + G3 power-limit
disclosures; adjudication exclusions per design×model. G1/G2/G3/G6/G8 compute; G4/G5/G7
PENDING. (Readings are descriptive only — do NOT quote as verdicts.)

### W5 — Part A label sample `labels/20260710-partA/`
282 blind units across the **stable full-6-model designs 01–06** (01=60, 02=12, 03=60, 04=60,
05=30, 06=60) + instruction packets + provenance jsonl + `00-WAVE-PLAN-README.md`. **Wave 1
ships {01, 02} now** (stable); **07–10 DEFERRED** until gemini completes (drawing now would
force a re-draw / waste labels).

### Capability battery for G3 (`00-PORTFOLIO/20260711-capability-battery-scores.json` + SOURCES)
O4-time public snapshot, 6×6, cited, 14/36 cells honestly null. Frozen composite method
(min-max-normalized available cells; RULER auto-dropped as single-value). Ranking:
claude-sonnet-4 > gemini-2.5-pro > gpt-4.1 > deepseek > llama > mistral.

---

## THE 402 BLOCKER — RESOLVED (gemini 07–10 complete)
The 402 "requires more credits" was a per-request **reservation** (OpenRouter reserves
`max_tokens × output-price` against the balance up front; the backend sent no cap, so it
reserved each model's default 65536 → ~$0.65/call, tripping 402 whenever the balance dipped
below that even though actual cost is cents). Cleared by BOTH: (1) Jimmy's **$20 top-up**;
(2) a backend hardening — **`DEFAULT_MAX_TOKENS = 32768` cap** in `openrouter_backend.py`
(commit `522deba32`; measurement-neutral — 32768 > every observed response, global per-cell
max ~32.5k; +3 TDD tests, suite 261 green). gemini-2.5-pro's 07–10 then completed via a
2-way per-design split (`--designs 08,09` main dir + `--designs 10` a `-b` dir) with an
auto-retry loop that shrugged off a transient **DNS blip** (`nodename nor servname`) and the
one runaway-generation cell `WW-08-E01` (recovered on retry). **Panel = 2064/2064.**
The merge that produced the final panel (for reference / any future re-render):
```bash
python merge_panel.py --out 20260711-o4-panel --runs 20260711-o4-gpt41 20260711-o4-gemini25pro \
  20260711-o4-gemini25pro-b 20260711-o4-claude-sonnet4 20260711-o4-deepseek \
  20260711-o4-mistral-large 20260711-o4-llama33   # note the extra gemini25pro-b split dir
```

## NEXT — Jimmy / O5 (NOT this session)
1. ~~Top up credits → complete gemini~~ **DONE this session** (panel 2064/2064; final report
   `20260711b-o4-panel-report.md`; Part A drawn for all 10 designs).
2. **Part A human labels** (~25–30 h; wave 1 = {02, 07, 01} — all ready in
   `labels/20260710-partA/`) + a 2nd labeler (or disclosed test–retest) →
   `judge_validation.py` → **G4** per design (RELEASE gate).
3. **06/09 blind reference scoring → G5**; **perturbation batteries → G7.**
4. **O5 gate ADJUDICATION (Fable-preferred):** verdicts, kills/demotes, release per design;
   tie-breaker-judge wiring for `needs_adjudication` cells (or Part-B).
5. **5 one-liner ratifications:** PR-1(c), PR-2(ADVICE_SYSTEM), PR-3(§6.4), PR-4(OpenRouter),
   PR-6(near-agreement mean). None block.
6. **W4 fixes (deferred, low priority):** mechanical relabels/re-anchors to A01/K01/E01 (+re-key
   K01, +trim D01/L03/N01) in `…-W4-06-references-DRAFT.md` → Jimmy ratifies before they enter
   `DESIGNS/06-*.md`. 06 stays PROVISIONAL until G5 regardless.

## Standing cautions
- No gate VERDICTS / item kills / release claims here (all O5). FIX-MECHANICS-ONLY held.
- HOLDOUT never loaded / never committed. `runs/*/scored_items.jsonl` + `*-DRAFT.md` gitignored.
- ≥3 sessions share the git index: `git log -1` before staging; stage WALKWORTHY paths
  explicitly; never rewrite sibling commits; fast-forward pushes only.
- Report immutability: the re-render after gemini completes must be a NEW dated file
  (`20260711b-…`), never an overwrite of `20260711-o4-panel-report.md`.
