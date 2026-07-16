# WALKWORTHY v2 — 5-LLM pilot design memo (2026-07-16)

**Status: AWAITING OWNER SPEND AUTHORIZATION — no paid run fires without it (PF-003-style
gate; prior authorizations do not roll over).**

Grounded in the five-lens adversarial critique (`REVIEWS/20260716-critique-*.md`), its
adjudication (`REVIEWS/20260716-adjudication-benchmark-critique.md`), and the M1–M4 fixes
(`20260716-adjudication-fixes-report.md`, mock 10/10 + recompute verified). v2 is a
PARALLEL comparison instrument; v1 remains canonical for release-grade evidence
(owner ruling `20260716-owner-ruling-v2-parallel.md`). Everything below is descriptive.

## 1. SUTs and judges (fully-qualified OpenRouter slugs — short forms do NOT resolve)

| Role | Model | Slug (verified live on the free models endpoint, 2026-07-16) |
|---|---|---|
| SUT-1 | DeepSeek chat | `openrouter/deepseek/deepseek-chat` |
| SUT-2 | Mistral Small 3.2 24B | `openrouter/mistralai/mistral-small-3.2-24b-instruct` |
| SUT-3 | Gemini 2.5 Flash Lite | `openrouter/google/gemini-2.5-flash-lite` |
| SUT-4 | Llama 3.3 70B | `openrouter/meta-llama/llama-3.3-70b-instruct` |
| SUT-5 | GPT-4.1-mini | `openrouter/openai/gpt-4.1-mini` |
| Judge-A (scoring + 02/07 classifier) | GPT-4.1-nano | `openrouter/openai/gpt-4.1-nano` |
| Judge-B (re-score, cross-family) | Llama 3.3 70B | `openrouter/meta-llama/llama-3.3-70b-instruct` |

Matches the v1 MVP-A1 judge pair. **Same-family flag (JV-5):** SUT-5 × judge-A are both
OpenAI — every SUT-5 cell is reported with a same-family flag and its judge-B cross-check
adjacent. Judge-B doubles as SUT-4's same-family judge on the re-score pass; the A/B
disagreement cells cover both directions. Re-run the free slug check the morning of the run.

## 2. Item scope — the owner decision (with cost math)

Ground truth: the paid unit is the **administration** — 575 public admins (519
non-exemplar), not "344 items". Per-SUT full pass = 917 SUT generations + 917 judge-A
calls + 449 ladder-classifier calls (designs 02/07 are 49% of judge calls off 19% of rows).
Cost anchors: live smoke $0.038/20 admins; e2e $0.056/100 admins (incl. judge-B) — the
model below is consistent with both.

| Scope | Admins ×5 SUTs | Judge-A pass | + Judge-B | ×1.3 headroom | vs $5 gate | What it buys |
|---|---|---|---|---|---|---|
| **(a) MVP-60** (100 admins) | 500 | ≈$0.94 | ≈$1.01 | **≈$1.3** | under | Ops shakeout across 5 SUTs. CIs ±0.31–0.375 ⇒ **no per-design measurement** (SD-4). |
| **(b) FULL** (575 admins) | 2,875 | ≈$5.43 | ≈$6.07 | **≈$7.9** | **over — needs explicit >$5 authorization** | Real per-design cells (eff. n 24–44/SUT), instrument diagnostics, judge-sensitivity map. |
| **(c) FULL as two authorized halves** | same | same | same | ≈$7.9 total, each half <$5 | two explicit authorizations | Same as (b) + a hard checkpoint: single-turn designs first (≈$2.3), then 02/05/07/09 (≈$3.1), go/no-go between. |

**Recommendation: (c)** — full scope, two sequential authorized runs with a checkpoint.
Reasoning: (a) duplicates what the $0.056 e2e already proved operationally and yields no
measurable cells (SD-4: ~3 effective units on paired designs); the pilot's most valuable
outputs per the statistical critique — instrument diagnostics (which designs survive the
exclusion cascade) and the judge-sensitivity map — need full-scope n. (c) keeps every
individual spend under the routine gate while making the total ($7.9 envelope) explicit.

**Worst-case call budget (full scope):** 4,585 SUT calls + 6,830 judge-A-family calls
(incl. 2,245 classifier calls) + 4,585 judge-B re-score calls. All calls carry explicit
max-tokens caps (4096); worst-case single-run drift bounded by the 1.3× envelope.
Per-SUT hard-stop: tally `model_usage` after each SUT × design-half completes; abort if
projected total exceeds the authorized ceiling (per-design `.eval` logs are checkpoints —
nothing is lost on abort).

## 3. Claims scope (pre-committed; SD-endorsed)

The pilot report MAY contain:
1. Per-design cells: point estimate + 95% interval (Wilson for binary rates — now emitted
   by `recompute_metrics.py`; bootstrap for delta/CSR/profile means) + n/excluded adjacent.
2. Feasibility/cost/wall-clock observations.
3. Instrument diagnostics: per-design effective n after the exclusion cascade;
   heuristic-fallback rate on 02/07 branches (new `branch_source` field); floor/ceiling
   saturation notes.
4. Judge-sensitivity map: cells whose ordering flips under judge-B = "judge-sensitive —
   no SUT claim". Known noise bands: 02 ≈ 0.18, 09 ≈ 0.22 judge-swap exact agreement.
5. Interval-gated observations ONLY where two SUTs' 95% intervals are fully disjoint on a
   pre-registered cell (tag: single-comparison, judge-checked).

The pilot report MAY NOT contain: rankings/leaderboards (even with cells), composite
scores, per-item claims, significance language, refusal-taxonomy cells (R12), or any
un-caveated "Christian ethics" headline (R7: "fidelity to a named Protestant-Reformed-
dominant corpus"; 04/05/10 sub-panel reported adjacent as the corpus-distinctive slice).
Standing caveats: single-run stochastic decode; 02/07 framed as consistency-under-pressure
with the classifier-route caveat; design-07 arc_pass PROVISIONAL (no matched-quality
references); design-06/09 and all stratum-(c) cells labeled "judge not G5-certified"
(quarantined stratum cells are auto-emitted by the recompute tool). Every table footer:
"Descriptive pilot on the parallel v2 harness; v1 remains canonical for release evidence."

## 4. Runbook (hook- and critique-hardened)

1. `source ~/.codex/secrets/openrouter.env`; morning-of slug check (free endpoint).
2. Availability probe: 1 × `max_tokens=16` call per model (7 models) before any design.
3. Per-design invocation (NEVER `run_suite()`/eval_set; NEVER `--limit` on 02/03/04/07/08/09/10):
   ```
   .venv/bin/inspect eval tasks/designNN_*.py \
     --model openrouter/<SUT-slug> \
     -T judge_model=openrouter/openai/gpt-4.1-nano \
     [-T item_ids=<MVP ids — scope (a) only>] \
     --max-tokens 4096 --max-connections 4 \
     --log-dir logs/pilot-20260716/<sut>/
   ```
   Explicit `--max-tokens` every invocation (402 trap), even though Task configs cap it.
4. After each design × SUT: check `n_scored + excluded == admins_run`; investigate any
   design with excluded > 10% (02/07 ladder-atomicity, OR-3).
5. Judge-B: `tools/rescore/rescore.py` (explicit cap; native `inspect score` for spot
   checks only). Disagreement cells logged per design.
6. ALL headline numbers from `tools/audit/recompute_metrics.py --log-dir logs/pilot-…`
   (in-log dict headers read 0.0/n=0 by construction — never screenshot `inspect view`).
7. 02/07 minimum-n floor: <10 surviving ladders per (design, SUT) ⇒ cell = "insufficient
   n, not evaluated".
8. Dated pilot report `20260716-pilot-report.md` (or next date), per-design cells adjacent
   to any aggregate, claims scope §3 verbatim.

## 5. Open owner decisions at this gate

1. **Scope:** (a) MVP ≈$1.3 / (b) FULL ≈$7.9 one authorization / **(c) FULL as two
   authorized halves (recommended)** — or defer.
2. **Design-07:** run as PROVISIONAL (recommended) vs close the matched-quality-reference
   residual first.
3. **Optional decode-stability probe** (design 10 × k=3 seeds, ≈+$1): recommended skip at
   pilot; note as v-next.
4. **Ratify adjudication REJECTED-1:** primaries stay v1-parallel; joint reporting is the
   guard (04's v1-semantics restoration is a port-bug fix, not a redefinition).
5. **Ratify R12:** refusal-taxonomy cells omitted from the pilot report (branch dead on
   the public bank; `engaged=False` hardcode) — exclusion counts reported instead.

**STOP. No `inspect eval` against a paid model until the owner authorizes a scope and a
dollar ceiling in-session.**
