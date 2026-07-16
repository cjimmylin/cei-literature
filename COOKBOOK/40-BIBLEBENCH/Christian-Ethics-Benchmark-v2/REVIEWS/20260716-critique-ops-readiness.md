# Critique — OPS READINESS (refute-first) — WALKWORTHY v2 paid pilot

**Date:** 2026-07-16
**Lens:** Operational readiness to spend real money reliably on a 5-LLM pilot (Inspect AI
0.3.246, OpenRouter). Method: try to BREAK "the harness is ready to spend real money
reliably"; concede only what survives a steelman.
**Read:** `AGENTS.md`, `20260716-polish-items-report.md`, `20260715-inspect-fit-assessment.md`,
`20260715-live-smoke-report.md`, `20260715d-e2e-and-two-judge-report.md`,
`20260716-boot-prompt-adversarial-critique-and-pilot.md`, `tasks/*.py`,
`walkworthy_inspect/{solvers,scorers,metrics,datasets}.py`, `tools/audit/recompute_metrics.py`,
`tools/rescore/`, `datasets/public/*.jsonl`.
**No paid calls made.** Slug validity checked via the free unauthenticated
`openrouter.ai/api/v1/models` endpoint only.

---

## Ground-truth numbers established (used throughout)

- **Public dataset size: 575 admins total**, not 615 (my first `wc -l` summed a stray
  count; `cat datasets/public/design*.jsonl | wc -l` = **575**). Per design (admins):
  01=49, 02=76, 03=66, 04=60, 05=32, 06=31, 07=31, 08=66, 09=92, 10=72. Non-exemplar =
  519. This 575 (not "344") is the true unit count the pilot pays for — 344 is the *item*
  count; admin-expansion is a **1.67× multiplier** the boot prompt's "344" hides.
- **Ladder lengths** (turns incl. terminal ask), computed from `metadata.multiturn`:
  design02 min 0 / max **10** / mean **7.2** (40 multiturn admins); design07 min 0 / max
  **8** / mean **5.3** (31 admins). Each turn = 1 SUT generate + 1 per-turn judge call
  (`scorers.py::_make_per_turn_scorer` loops `for t in turns`) + 1 mid-solver classifier
  call per branched turn (`solvers.py::_classify_branch`, paid — it's `get_model(judge_model)`).
- **Per-SUT call counts, full 575** (computed): SUT generate calls **917**, judge-A calls
  **917**, classifier calls **449** → **1,366 paid judge-family calls/SUT** + 917 SUT calls.
  Designs 02+07 alone are 286+163 = **449 of the 917 judge calls (49%)** off only
  76+31 = 107 admins (19% of rows). The ladder multiplier is the dominant cost term.
- **Slug validity (free endpoint, 342 models live):** all 7 pilot slugs resolve **only in
  fully-qualified form** — `deepseek/deepseek-chat` ✅, `mistralai/mistral-small-3.2-24b-instruct`
  ✅, `google/gemini-2.5-flash-lite` ✅, `meta-llama/llama-3.3-70b-instruct` ✅,
  `openai/gpt-4.1-mini` ✅, `openai/gpt-4.1-nano` ✅, `openai/gpt-4o-mini` ✅ (fallback).

---

## COST MODEL (both scopes)

Per-admin $ derived from the live-smoke per-design table (`20260715-live-smoke-report.md`,
2 samples/design, deepseek SUT × gpt-4.1-mini judge), which already includes the ladder +
classifier calls for 02/07. Scaled linearly to full admin counts. Judge here = gpt-4.1-mini
in the anchor; the pilot's gpt-4.1-nano judge is *cheaper*, so these are conservative-high
on the judge side and conservative-low on the SUT side (deepseek is one of the cheaper SUTs;
gemini/llama/gpt-4.1-mini SUTs cost more per token).

| design | admins (full) | $/admin (smoke) | FULL $/SUT | MVP admins | MVP $/SUT |
|---|---:|---:|---:|---:|---:|
| 01 | 49 | 0.00125 | 0.061 | 6 | 0.0075 |
| 02 (ladder ~7.2) | 76 | 0.00445 | 0.338 | 12 | 0.053 |
| 03 | 66 | 0.00055 | 0.036 | 12 | 0.0066 |
| 04 | 60 | 0.00060 | 0.036 | 12 | 0.0072 |
| 05 | 32 | 0.00430 | 0.138 | 6 | 0.026 |
| 06 | 31 | 0.00185 | 0.057 | 6 | 0.011 |
| 07 (ladder ~5.3) | 31 | 0.00675 | 0.209 | 6 | 0.041 |
| 08 | 66 | 0.00045 | 0.030 | 12 | 0.0054 |
| 09 | 92 | 0.00125 | 0.115 | 16 | 0.020 |
| 10 | 72 | 0.00090 | 0.065 | 12 | 0.011 |
| **per SUT** | **575** | — | **≈ $1.08** | **100** | **≈ $0.19** |

| scope | judge-A pass (×5 SUT) | judge-B re-score (×5) | subtotal | ×1.3 retry/variance/costlier-SUTs | vs $5 ceiling |
|---|---:|---:|---:|---:|---|
| **MVP 100 admins** | ≈ **$0.94** | ≈ $0.07 | **≈ $1.01** | **≈ $1.3** | ✅ safe |
| **FULL 575 admins** | ≈ **$5.43** | ≈ $0.64 | **≈ $6.07** | **≈ $7.9** | ❌ **BREACH** |

Sanity check against observed: smoke 20 admins = $0.038 → $0.0019/admin blended; my
per-design decomposition gives $0.19/100-MVP-admins = $0.0019/admin — **consistent**. The
e2e run (100 admins, mistral SUT + nano judge, judge-B included) cost $0.056 total →
corroborates MVP-per-SUT ≈ $0.19 and judge-B ≈ $0.014/100 prompts.

**Dominant cost terms:** (1) the 02/07 ladder multiplier — 02 alone is $0.34/SUT at full,
5× any single-turn design; (2) design-05's long prose generations (4.6k out tokens/2
samples in smoke); (3) SUT-side token price — deepseek anchors low, so gemini-flash-lite /
gpt-4.1-mini / llama-70b SUTs push the real full number **above $5.4**. See OR-1.

---

## Findings

### OR-1 — FULL 344/575 × 5 SUTs breaches the $5 PF-003 ceiling on the base pass alone
**Severity: CRITICAL. Pilot-blocking: YES (for the FULL scope; MVP is fine).**
**Claim attacked:** boot prompt Phase 3 offers "full 344 vs 60-MVP" as an open choice with
"cost math"; the implication is either is affordable.
**Evidence:** full public = **575 admins** (`cat datasets/public/design*.jsonl | wc -l`),
not 344. Cost model above: base judge-A pass ≈ **$5.43** for 5 SUTs *before* judge-B and
*before* any retry/pricing headroom; with the standard 1.3× envelope ≈ **$7.9**. AGENTS.md
§4: "PF-003 $5 ceiling per unauthorized run; anything larger needs an explicit owner
authorization." Even *with* authorization, a single run that can drift from $5.4 to $8 on
provider-pricing variance is an unreliable spend.
**Refutation attempt:** "deepseek anchored the smoke cheap; nano judge is cheaper than the
mini anchor, so real cost is under $5." — Partly true on the judge side, but the SUT side
moves the *other* way: 4 of the 5 SUTs (gemini-flash-lite, llama-3.3-70b, gpt-4.1-mini,
mistral-small) are pricier per output token than deepseek-chat, and the full pass runs 917
SUT generations/SUT vs the smoke's 20. The judge saving doesn't cover a 46× volume increase
on costlier SUTs. **Survives.**
**Remedy:** Pilot on the **60-item MVP subset (100 admins, ≈ $1.3 all-in ×5)**, which the
critique lens itself recommends and which the e2e run already exercised. If FULL is wanted,
split into two authorized runs (single-turn designs ≈ $2.3/5-SUT; then 02/05/07/09 as a
second run), each independently under $5, OR get an explicit >$5 owner authorization with
the $7.9 envelope stated. Do NOT launch FULL under a routine $5 gate.

### OR-2 — `run_suite()` / eval_set path passes no max_tokens and no explicit retry config → 402 + resumption risk
**Severity: MAJOR. Pilot-blocking: YES if the pilot uses `run_suite()`/eval_set; NO if it
uses per-task `inspect eval --max-tokens`.**
**Claim attacked:** "AGENTS §1 402 trap is handled; always explicit max-tokens."
**Evidence:** `tasks/walkworthy_suite.py::run_suite` calls `eval_set(tasks=…, model=…,
log_dir=…, limit=…)` with **no `GenerateConfig`/max_tokens** and **no `retry_*` args**
(inspect exposes `retry_attempts`, `retry_on_error`, `fail_on_error`, etc. — none set).
The per-task `Task(config=GenerateConfig(max_tokens=4096))` *does* cap the SUT (verified in
all 10 task files), so 402-safety survives **only because the cap is baked into the Task
config** — the runner adds nothing. But: the classifier and judge calls inside
`solvers.py`/`scorers.py` are separate `get_model(...).generate(config=GenerateConfig(
max_tokens=…))` calls with their own caps (DEFAULT_MAX_TOKENS / JUDGE_MAX_TOKENS = 4096) —
also safe. The residual risk is **the CLI path**: `inspect eval tasks/walkworthy_suite.py
--model X` without `--max-tokens` inherits the Task config cap, but any *ad-hoc* single-task
CLI invocation a hurried operator types without `--max-tokens` and without the Task cap
(e.g. a raw `get_model().generate()` probe) reserves up to 65536 and 402s.
**Refutation attempt:** "the Task config caps it, so max-tokens is always present." — True for
the packaged tasks, but the AGENTS rule is about *invocation discipline*, and the smoke/e2e
reports both passed explicit `--max-tokens` on the CLI anyway (belt + suspenders). The
eval_set path silently drops that belt: no explicit cap at the run layer, no retry policy,
so a transient provider 429/5xx mid-run is handled by inspect defaults the operator never
chose. **Survives as a discipline/observability gap, not a guaranteed failure.**
**Remedy:** For the pilot, invoke **per-design** `inspect eval tasks/designNN_*.py --model …
-T judge_model=… --max-tokens 4096 --max-connections 4 --log-dir logs/pilot-YYYYMMDD/`
(the exact smoke/e2e shape, proven at $0.038/$0.056). If eval_set is used, set explicit
`retry_attempts`/`fail_on_error=False` and pass max_tokens via task args. Mandate explicit
`--max-tokens` in the pilot runbook even though the Task cap exists.

### OR-3 — Mid-ladder failure on 02/07 corrupts the administration; no pair/ladder atomicity
**Severity: MAJOR. Pilot-blocking: NO (but must be a documented analysis-exclusion rule).**
**Claim attacked:** "Inspect built-in retry/resume covers failures" (fit memo §1).
**Evidence:** the 02/07 ladder is a single Inspect *sample* whose solver
(`multiturn_ladder_solver`) makes up to 10 sequential SUT generations + classifier calls
inside one `solve()`. Inspect retries at the **sample** level, so a provider 5xx on turn 7
of 8 re-runs the whole sample from turn 0 — fresh stochastic generations for turns 1–6, so
a *retried* ladder is not the same administration a partially-completed one was. If it fails
permanently, `store["ww_turns"]` may be short/empty; the per-turn scorer then hits
`_reconstruct_turns_from_messages` (fallback) and any `None`/`unscorable` turn makes
`break_turn`/`arc_shape` **exclude the whole item** (`metrics.py`, verbatim v1 rule). So a
half-failed ladder silently *drops the item* rather than biasing it — good — but it shrinks
02/07's already-small per-item n.
**Refutation attempt:** "exclusion-on-partial is correct and safe." — Correct for validity,
but for **ops reliability** it means 02/07 can quietly lose samples under provider flakiness
and the operator won't notice without checking `n`/`excluded` in the recompute output. The
`n=0` header artifact (OR-5) compounds this: a reader can't tell "excluded by design" from
"whole design failed." **Survives as a monitoring requirement.**
**Remedy:** After the run, for 02/07 assert `n_scored + excluded == admins_run` from
`recompute_metrics.py`; investigate any `excluded > ~10%`. Consider `--max-connections`
low (≤4) for 02/07 to reduce provider throttling on the long ladders.

### OR-4 — Pair-splitting via `--limit`; the pair-safe path exists but must be mandated
**Severity: MINOR (mitigated). Pilot-blocking: NO.**
**Claim attacked:** residual (c) "pair-aware `--limit` helper missing."
**Evidence:** `--limit N` truncates at the sample level with no `pair_id` awareness (fit memo
§3.2), so it *can* split say/do (03), covert/overt (08), seat_A/B (09), alpha/beta (04),
N/U (10) pairs → paired metrics report `incomplete_pairs` and drop the item. **However**,
the real fix already shipped: `datasets.py::load_design(item_ids=…)` + the `-T item_ids=`
task arg keep **all administrations of a matched item** (verified: e2e run used the 60 MVP
item_ids and expanded them to exactly 100 clean admins). So the pilot has a pair-safe
selector; `--limit` is the trap, `item_ids` is the tool.
**Refutation attempt:** "then there's no issue." — Only if the runbook forbids `--limit` for
pilots. The helper's absence means an operator reaching for the obvious `--limit 60` on a
paired design (03/04/08/09/10) gets silently wrong pairing. **Survives as a discipline rule.**
**Remedy:** Pilot runbook: **never `--limit` on 03/04/08/09/10** (and 02/07 not paired but
ladder-atomic); scope via `-T item_ids=<comma-list>` only. For the MVP use the exact 60
item_ids from `../Christian-Ethics-Benchmark/runs/20260713-mvp-a1/manifest.json` (already
validated). If a per-design count cap is truly needed, pass item_ids in admin-group multiples.

### OR-5 — n=0 / dict-scalar headline: real misread risk; recompute path covers all 10, is authoritative
**Severity: MAJOR (reporting-integrity). Pilot-blocking: NO — but a hard reporting rule.**
**Claim attacked:** residuals (b)+(e) "n=0 display artifact / dict-score headline 0.0 are cosmetic."
**Evidence:** Inspect defaults the scalar headline to 0.0 and shows `n=0/excluded=2` in the
Task header for dict-valued scores (fit memo §3.1; polish report §4 note for 02/07). This is
**not cosmetic for a pilot report**: the live micro-check showed the in-log header reading
`n=0/excluded=2` while the true recomputed values were break_turn 0.4375 / arc_pass 0.0. A
reader who screenshots `inspect view` into a pilot report publishes 0.0 for a real 0.44.
**Coverage check (I verified):** `PRIMARY_METRICS` has keys `['01'..'10']` — the sanctioned
`tools/audit/recompute_metrics.py` recomputes **all 10** designs' headline from stored
Score dicts, free/deterministic, and prints OLD-vs-NEW. So the authoritative path exists and
is complete.
**Refutation attempt:** "recompute is the sanctioned path, so the header is harmless." — True
*if the discipline holds*, but the failure mode is human: two numbers exist for the same
metric (the wrong one is the eye-catching header). The polish report itself had to footnote
this three times. **Survives as a live misreport hazard requiring a hard rule.**
**Remedy:** Pilot report rule: **every headline number comes from `recompute_metrics.py
--log-dir logs/pilot-…`; never from the `inspect view`/Task header.** Put the recompute table
in the report and explicitly annotate that in-log dict headlines read 0.0 by construction.

### OR-6 — Design-07 missing matched-quality reference answers: bias risk, not noise, but bounded
**Severity: MINOR-to-MAJOR (design-07 only). Pilot-blocking: NO — flag 07 as provisional.**
**Claim attacked:** residual (a) "07 harness-side reference answers not done — fold into lens."
**Evidence:** `scorers.py::_references` populates matched-quality reference anchors for
designs **06 and 09 only** (06 from `keyed.extras.reference_answers`, 09 from
`keyed_determinations`+`floor_violations`). Design 07 is a per-turn ladder scorer
(`_make_per_turn_scorer`) and `spec.reference_anchored` gates the reference block; 07's judge
prompt therefore judges each turn's `turn_state` against the rubric + keyed anchor **without**
matched-quality references. Effect on a paid run NOW: not noise and not a crash — it's a
potential **neutrality/leniency bias** in the per-turn state classification (no "a
well-executed attested position must not be penalized" anchor), which shifts arc_pass. It
does not corrupt other designs and does not affect cost.
**Refutation attempt:** "07 uses turn_state, not a reference-scored category, so references are
inapplicable." — Partly fair: 07's construct is arc *shape* over states, and the smoke showed
07 states populate. But the absence means 07's judged states carry a known un-audited bias the
other reference-anchored design (06/09) don't; at n=6 (MVP) or n=31 (full) that bias isn't
averaged out. **Survives as: report design-07 as PROVISIONAL.**
**Remedy:** Either close the 07 reference-answer residual before the run, or (cheaper) run 07
but mark its arc_pass_rate PROVISIONAL in the pilot report with a one-line caveat; exclude 07
from any cross-design synthesis. Owner call.

### OR-7 — design-05 parser edge (`allocation_ok=True/values={}`) mislabels format-noncompliance
**Severity: MINOR. Pilot-blocking: NO.**
**Claim attacked:** residual (f) "parser edge is latent/harmless."
**Evidence:** `reparse_allocation_response` logs `allocation_ok=True, non_compliant=False,
allocation_values={}` on a block-less prose answer (smoke report §"Latent parser note"),
inconsistent with an offline re-parse (`ok=False, non_compliant=True, csr=0.0`). CSR itself
still comes out correct (empty allocation → no CSR → `unscorable`), so the **headline
`csr_mean` is unaffected**, but the per-sample `allocation_ok`/`non_compliant` metadata is
wrong — and design-05's whole point in this SUT tier is *format-compliance as measurement
signal*. A pilot that tabulates "non_compliant count" off that flag under-reports
non-compliance.
**Refutation attempt:** "csr_mean is right, so it doesn't matter." — For the headline, true.
For the format-compliance *secondary* signal (which the smoke explicitly called measurement
signal), the flag is load-bearing and wrong. **Survives, low severity.**
**Remedy:** In the 05 report, derive non-compliance from `csr==unscorable && empty
allocation_values`, not from the `non_compliant` flag; or fix the parser recovery path. Note
it in the runbook.

### OR-8 — judge-B via native `inspect score` has no `--max-tokens` flag → relies on internal cap
**Severity: MINOR. Pilot-blocking: NO (the internal cap covers it).**
**Claim attacked:** "native `inspect score` re-score path is 402-safe."
**Evidence:** e2e report §94: "`inspect score` has no `--max-tokens` flag, so a CLI path
would have to rely on the scorer's internal `JUDGE_MAX_TOKENS=4096` cap." Verified:
`scorers.py` judge/classifier calls all pass `GenerateConfig(max_tokens=JUDGE_MAX_TOKENS=4096)`.
So `inspect score` IS 402-safe *because the scorer hardcodes the cap* — but the operator has
no CLI lever, and if a future scorer edit drops the internal cap, `inspect score` silently
loses 402-protection with no CLI override available.
**Refutation attempt:** "cap is present, so it's safe." — True today. **Survives only as a
fragility note:** the e2e report already declared `tools/rescore/rescore.py` (which passes an
explicit cap) the *sanctioned* judge-B path over native `inspect score`.
**Remedy:** Use `tools/rescore/rescore.py` for judge-B (explicit cap, proven at $0.014/100).
Keep native `inspect score` for spot checks only.

### OR-9 — Wall-clock / throughput: deepseek + long ladders are slow; connection sizing unstated
**Severity: MINOR. Pilot-blocking: NO.**
**Claim attacked:** "harness completes reliably."
**Evidence:** smoke report §"Provider failures": "`deepseek-chat` throughput is slow but
every eval completed." Full pass = 917 SUT calls + 1,366 judge-family calls **per SUT** ×5 =
~11,400 calls total. At `--max-connections 4` and slow SUTs, the 02/07 ladders (sequential
within a sample) dominate wall-clock. No wall-clock estimate exists in any report.
**Refutation attempt:** "it completed in the smoke." — At 20 admins. 575×5 is 144× the calls;
no timing data extrapolates cleanly, and a multi-hour run raises mid-run 402/rate-limit
exposure (OR-2). **Survives as an un估imated risk.**
**Remedy:** MVP scope keeps this to ~500 admins total (bounded). Set `--max-connections 4`,
run designs sequentially (per-task invocation), log wall-clock per design in the pilot report,
and checkpoint by keeping per-design `.eval` logs (already the pattern).

---

## What survives (concessions kept minimal)

- **OR-1 (CRITICAL, blocking for FULL):** FULL = 575 admins, ≈$5.4 base ×5 → ≈$7.9 envelope,
  breaches the $5 gate. MVP (100 admins, ≈$1.3 all-in) is safe. **The pilot must be MVP, or
  FULL needs an explicit >$5 authorization and/or a two-run split.**
- **OR-2 (MAJOR):** use per-design `inspect eval --max-tokens 4096 --max-connections 4`; the
  eval_set/run_suite path lacks explicit cap + retry config.
- **OR-3 (MAJOR):** 02/07 ladders are sample-atomic; monitor `excluded` counts.
- **OR-5 (MAJOR):** all headlines from `recompute_metrics.py` (covers all 10), never the
  in-log 0.0 dict header.
- **OR-4 / OR-6 / OR-7 / OR-8 / OR-9 (MINOR):** pair-safe `item_ids` selector (no `--limit`
  on paired designs); design-07 arc_pass PROVISIONAL; 05 non_compliant flag unreliable;
  judge-B via `tools/rescore/rescore.py`; bound wall-clock via MVP + sequential per-design.

**Conceded as genuinely ready:** all 7 model slugs are currently valid (fully-qualified);
Task configs carry the 4096 max_tokens cap (402-safe by construction); the offline recompute
path is complete and free; the `item_ids` pair-safe selector works; judge-B re-score is
validated end-to-end; two live spends ($0.038, $0.056) landed with zero 402s/failures. The
harness IS ready — **for the MVP scope, run per-design, reported off recompute.** It is NOT
ready to fire the FULL 575×5 pass under a routine $5 gate.

---

## Pre-pilot ops checklist (feeds the pilot design memo)

1. **Scope = 60-item MVP (100 admins), not FULL 575** — unless owner authorizes >$5 with the
   $7.9 envelope stated and a two-run split. State "575 admins, not 344 items" in the memo.
2. **Slugs fully-qualified:** `deepseek/deepseek-chat`, `mistralai/mistral-small-3.2-24b-instruct`,
   `google/gemini-2.5-flash-lite`, `meta-llama/llama-3.3-70b-instruct`, `openai/gpt-4.1-mini`
   (SUTs); judges `openai/gpt-4.1-nano` (A) + `meta-llama/llama-3.3-70b-instruct` (B).
   Re-run the free `openrouter/api/v1/models` slug check the morning of the run (deprecation drift).
3. **Invocation:** per-design `inspect eval tasks/designNN_*.py --model <SUT>
   -T judge_model=openrouter/openai/gpt-4.1-nano -T item_ids=<60 MVP ids>
   --max-tokens 4096 --max-connections 4 --log-dir logs/pilot-YYYYMMDD/<sut-slug>/`.
   **Explicit `--max-tokens` every time. Never `--limit` on 03/04/08/09/10.**
4. **Availability probe first:** 1 tiny `max_tokens=16` call per model (7 models) before any
   full design — the smoke's proven pattern; catches slug drift / 402 for cents.
5. **Judge-B:** `tools/rescore/rescore.py` (explicit cap), not native `inspect score`.
6. **Reporting:** every headline from `tools/audit/recompute_metrics.py --log-dir logs/pilot-…`;
   include the recompute table; annotate the in-log 0.0 dict headers as artifacts; assert
   `n_scored + excluded == admins_run` per design (esp. 02/07).
7. **Provisional flags:** design-07 arc_pass PROVISIONAL (no matched-quality references);
   design-05 non-compliance derived from `csr==unscorable`, not the `non_compliant` flag.
8. **Spend guard:** hard-stop after each SUT completes; tally running cost from each log's
   `model_usage`; abort if projected total > authorized ceiling. Per-design `.eval` logs are
   the checkpoints — nothing is lost on abort.
9. **Cost envelope to authorize:** MVP ×5 ≈ **$1.3 all-in** (base $0.94 + judge-B $0.07 +
   30% headroom). If FULL: ≈ **$7.9** — request explicitly.
