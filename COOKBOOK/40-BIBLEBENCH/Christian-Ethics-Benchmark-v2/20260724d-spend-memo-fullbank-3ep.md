# SPEND MEMO — WALKWORTHY v2 phase-5 ARM 1: full-bank run, 5 SUTs × 3 epochs, two judges

**Date:** 2026-07-24 · **Session:** phase-5 (boot prompt `20260724c-boot-prompt-phase5-fullbank-rescore-3ep.md`)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Status:** ✅ **AUTHORIZED 2026-07-24 by the owner (Jimmy), in-session.**
GO at **ceiling $16.00**; classifier §5 ruled **Option A** (nano carried forward,
current instrument lineage) — recorded in `RULINGS-APPLIED-20260724e.md`.
**Bank revision:** 2026-07-24b (public 344 items / 344 runnable / **563 administration lines**)

---

## 0. Executive summary

| Line | Figure |
|---|---|
| Expected all-in cost (bottom-up, live prices) | **$10.90** |
| Proposed authorized ceiling | **$16.00** |
| Carried-in estimate from the boot prompt | $14–17, ceiling ~$25 |
| Basis | Exact token counts from the 50 pilot eval logs, re-priced at 2026-07-24 live OpenRouter prices |

The bottom-up model comes in **below** the carried-in estimate. The boot prompt's
$14–17 was a forward projection; this memo replaces it with a measured one and
recommends a correspondingly tighter ceiling ($16, not $25).

**One item requires an owner ruling before any run call — see §5 (design-02/07 branch
classifier pin). It is cost-neutral but governance-blocking.**

---

## 1. Availability probes (executed — authorized as memo prep, ≤$0.01)

Twelve calls total (6 slugs × 2 passes; the first pass's parser hit a BSD `head`
incompatibility and was re-run). Aggregate probe spend **< $0.0002**.

| Role | Slug requested | HTTP | Resolved model | Verdict |
|---|---|:---:|---|:---:|
| SUT 1 | `openrouter/deepseek/deepseek-chat` | 200 | `deepseek/deepseek-chat` | ✅ |
| SUT 2 | `openrouter/mistralai/mistral-small-3.2-24b-instruct` | 200 | `mistralai/mistral-small-3.2-24b-instruct` | ✅ |
| SUT 3 | `openrouter/google/gemini-2.5-flash-lite` | 200 | `google/gemini-2.5-flash-lite` | ✅ |
| SUT 4 / judge-B | `openrouter/meta-llama/llama-3.3-70b-instruct` | 200 | `meta-llama/llama-3.3-70b-instruct` | ✅ |
| SUT 5 | `openrouter/openai/gpt-4.1-mini` | 200 | `openai/gpt-4.1-mini` | ✅ |
| judge-A + 02/07 classifier | `openrouter/openai/gpt-4.1-nano` | 200 | `openai/gpt-4.1-nano` | ✅ |

**No delistings. No silent aliasing** — every resolved `model` field equals the slug
requested, so the roster is intact and no substitution question arises (the boot
prompt's STOP condition does not fire).

Slugs taken from `logs/changed-items-smoke-20260724/run_matrix.sh` (the 5 SUT map and
the `-T judge_model=` pin) and corroborated against `20260716-pilot-report.md` §1 and
`REPORTS/20260717-briefing/02-evaluation.md` §"Judge-A (scoring + 02/07 branch
classifier)". Not reconstructed from memory.

## 2. Live prices, pinned 2026-07-24 (USD per 1M tokens)

Fetched from `https://openrouter.ai/api/v1/models`; all six present in catalog.

| Slug | prompt | completion | context |
|---|---:|---:|---:|
| `openai/gpt-4.1-nano` | 0.1000 | 0.4000 | 1,047,576 |
| `openai/gpt-4.1-mini` | 0.4000 | 1.6000 | 1,047,576 |
| `deepseek/deepseek-chat` | 0.2002 | 0.8001 | 163,840 |
| `mistralai/mistral-small-3.2-24b-instruct` | 0.1000 | 0.3000 | 256,000 |
| `google/gemini-2.5-flash-lite` | 0.1000 | 0.4000 | 1,048,576 |
| `meta-llama/llama-3.3-70b-instruct` | 0.1300 | 0.4000 | 131,072 |

## 3. The matrix

A billable unit is an **administration line**, not an item — designs 02/03/04/08/09/10
expand to multiple administrations per item (`20260724b-conversion-parity-report.md`
§1, whose tables are the 24b revision even though its internal header reads
2026-07-15).

| design | items | admin lines | × 5 SUTs | × 3 epochs | 3-epoch cost |
|---|---:|---:|---:|---:|---:|
| 01 goodsamaritan | 49 | 49 | 245 | 735 | $0.2922 |
| 02 twomasters | 36 | 72 | 360 | 1,080 | **$3.1353** |
| 03 quiettongue | 33 | 66 | 330 | 990 | $0.2223 |
| 04 innerweight | 33 | 60 | 300 | 900 | $0.2622 |
| 05 ordoamoris | 32 | 32 | 160 | 480 | $0.3630 |
| 06 crookedpath | 31 | 31 | 155 | 465 | $0.3564 |
| 07 seventyseven | 27 | 27 | 135 | 405 | **$1.7955** |
| 08 vocationfork | 33 | 66 | 330 | 990 | $0.3276 |
| 09 doubleedge | 34 | 88 | 440 | 1,320 | $0.8766 |
| 10 strangergate | 36 | 72 | 360 | 1,080 | $0.5664 |
| **TOTAL** | **344** | **563** | **2,815** | **8,445** | **$8.1975** |

**The two ladder designs are 60% of the bill.** 02 + 07 = $4.93 of $8.20. The driver is
the branch classifier: it re-reads the accumulated transcript at every branch turn, and
4.04M of judge-A/classifier's 6.65M input tokens across the whole bank come from those
two designs alone.

## 4. Bottom-up cost model

**Method.** Rather than project forward, this memo reads exact `model_usage` token
counts from the **50 pilot eval logs** (`logs/pilot-20260716/`, full 563-line bank ×
5 SUTs × 1 epoch, SUT + judge-A + classifier) and re-prices them at §2 live prices.

**Method validation.** The re-priced pilot total is **$2.7324** against the
$2.73 recorded in `20260716-pilot-report.md` §1, and the judge-B scaling yields
**$0.9009** against the recorded ≈$0.90 estimate. The extraction reproduces both
historical figures, and prices have not materially moved for this roster since
2026-07-16.

### Per-model, one epoch (5 SUTs, full bank)

| Model | role | input tok | output tok | USD |
|---|---|---:|---:|---:|
| `openai/gpt-4.1-nano` | judge-A + classifier | 6,648,950 | 91,268 | 0.7014 |
| `openai/gpt-4.1-mini` | SUT | 287,689 | 303,160 | 0.6001 |
| `deepseek/deepseek-chat` | SUT | 928,555 | 462,469 | 0.5559 |
| `google/gemini-2.5-flash-lite` | SUT | 1,026,483 | 869,862 | 0.4506 |
| `mistralai/mistral-small-3.2-24b-instruct` | SUT | 737,333 | 538,704 | 0.2353 |
| `meta-llama/llama-3.3-70b-instruct` | SUT | 594,409 | 279,318 | 0.1890 |
| **TOTAL** | | | | **2.7324** |

### Roll-up

| Component | 1 epoch | 3 epochs |
|---|---:|---:|
| SUT + judge-A + 02/07 classifier | $2.7324 | $8.1972 |
| judge-B full rescore (llama-3.3-70b, scaled off judge-A prompt volume) | $0.9009 | $2.7026 |
| **ALL-IN** | **$3.6333** | **$10.8998** |

### Ceiling derivation

| Component | $ |
|---|---:|
| Expected all-in | 10.90 |
| Retry / partial-rerun headroom (+25%) | 2.72 |
| design-08 post-anchor rubric — larger judge prompt (d08 judge = $0.027/epoch; even 2× adds ~$0.08/3ep) | 0.10 |
| Provider-routing and price-drift variance (+10%) | 1.09 |
| Rounding to a clean authorization | 1.19 |
| **PROPOSED CEILING** | **16.00** |

### Known deltas from the pilot basis (why this is an estimate, not a quote)

- **Bank rev 24b changed content, not volume.** Line count is 563 in both the pilot
  and 24b, so the administration matrix is unchanged. Four items' prompt text changed
  and three design-07 items became validly scorable (they previously *ran* and were
  *judged* — the keys were empty, so cost was already incurred). Volume effect ≈ 0.
- **design-08 anchors** (`RULINGS-APPLIED-20260724c.md`) add reference text to the d08
  judge prompt. Costed above; immaterial.
- **Wall-clock, not cost:** the pilot ran ≈24 min (half-1) / ≈50 min (half-2) at
  `--max-connections 4`, plus 25–45 min per judge-B pass. Three epochs serially is
  roughly a 4–6 hour envelope with the SUTs parallelised as in `run_matrix.sh`.

---

## 5. ⚠ BLOCKING GOVERNANCE ITEM — the design-02/07 branch classifier pin

**This is not a cost question.** It must be ruled before the run because it determines
whether the resulting design-02 cells are usable for the purpose the run exists to serve.

### The conflict

1. `tasks/design02_twomasters.py` and `tasks/design07_seventyseven.py` both construct
   `multiturn_ladder_solver(classifier_model=judge_model)`. **The branch classifier
   *is* the judge model** — there is no separate task parameter. Pin one, you pin both.
2. `20260716-prereg-comparisons-RATIFIED.md` **C6 / RULING 1d**: the classifier pin
   FREEZES at `gpt-4.1-nano` for the **current instrument lineage**; a classifier
   change is an instrument change; **no cross-classifier pooling ever**.
3. `20260716-design02-classifier-pin-decision.md` (owner-ruled, same date): the
   **v-next** design-02 instrument re-pins to a cross-family-corroborated classifier
   (`mistral-small-3.2` or `gemini-2.5-flash-lite`), **NOT nano** — because F3 found
   nano is the cross-family outlier: the two alternative families agree with each other
   at **0.902** but with nano at only **0.685–0.721**, and on **24.4% of branch turns
   both alternatives agree AGAINST nano**, concentrated in design-02 `refused→complied`
   swaps (nano over-calls "refused").

So: is this full-bank run the **current lineage** (nano) or the **v-next instrument**
(cross-family)? Both readings are defensible from the record, and the two rulings were
issued the same day for different scopes. The 2026-07-24 smoke ran nano — but a smoke
is explicitly descriptive-only and does not settle a lineage question.

### Why it matters more than usual here

The run's stated purpose includes producing the per-judge `pushback_rate` evidence base
for the deferred design-02 headline re-decision (`RULINGS-APPLIED-20260724d` condition
3). `pushback_rate` is a **design-02** metric, and design-02 is precisely where the nano
classifier is documented to misroute a quarter of branch turns. Evidence gathered under
a classifier known to over-call `refused` on that design is weaker evidence for that
specific decision — and under C6 it can never later be pooled with cross-family cells.

### Cost impact: none

| Classifier | 02+07 classifier+judge, 1 epoch | 3 epochs |
|---|---:|---:|
| `gpt-4.1-nano` (status quo) | $0.4169 | $1.2507 |
| `mistral-small-3.2` | $0.4136 | $1.2408 |
| `gemini-2.5-flash-lite` | $0.4169 | $1.2507 |

Identical to within a cent. **Choose on validity, not budget.**

### Options

- **Option A — carry nano forward (no code change).** Run exactly as the smoke did.
  This run is the *current lineage* on bank rev 24b. Design-02 cells inherit the
  documented nano refused-overcall as a known instrument property (cited to F3 + the
  pin-decision memo, as the pilot cells already are). The v-next re-pin stays unfired,
  a future instrument version. **Fastest; zero code risk; consistent with RULING 1d.**
  Cost: as modelled, $10.90.
- **Option B — honor the v-next re-pin (requires a code change + F11 ruling).**
  Decouple the classifier from the judge by adding a `classifier_model` task parameter
  to designs 02 and 07 (defaulting to `judge_model` so nothing else changes), pin it to
  `mistral-small-3.2`, keep judge-A = nano and judge-B = llama so the R4 two-judge
  discipline is untouched. This is an **instrument change under F11**: it needs an owner
  ruling recorded in a new dated `RULINGS-APPLIED` file, a test-suite touch, and it
  opens its own C9 line (02/07 cells not comparable to *any* prior run, pilot or smoke).
  The boot prompt fences code edits, so this option is only available by explicit owner
  override. Cost: $10.90 (unchanged).
- **Option C — run 8 designs now, defer 02/07.** Avoids the ruling entirely but
  forfeits the `pushback_rate` evidence that motivates the run. Cost: ≈$6.00 all-in
  (drops $4.93 of ladder spend). **Not recommended** — it removes the run's main purpose.

### ✅ OWNER RULING (2026-07-24, in-session): **Option A**

The classifier stays pinned at `openrouter/openai/gpt-4.1-nano` for this run. This run
is the **current instrument lineage** under C6/RULING 1d. Design-02 cells carry the
nano refused-overcall as a documented instrument property. The v-next cross-family
re-pin remains **unfired** and available as a future instrument version. No code change.
Recorded in `RULINGS-APPLIED-20260724e.md`.

**Recommendation (as presented): Option A.** RULING 1d is the more specific instruction for a run in
the existing lineage, the boot prompt explicitly expects no code edits, and the
resulting design-02 caveat is one this project already carries and cites. Option B is
the better *instrument*, but it is a different project step — properly its own gated
session with its own ruling, not a mid-flight amendment to a run authorization.

---

## 6. Claims envelope (binding on the run report)

1. **C9 — first-ever numbers on bank rev 2026-07-24b.** These are *new data on a new
   bank*. Consequently the pre-registered comparison families **C1 (m=30) and C2
   (m=70)** are reportable **as pre-registered** — not under the mandatory "post-hoc on
   pilot data — hypothesis-generating" label that binds everything computed on
   2026-07-16 logs. This is a substantive gain and is stated here *before* first use, as
   C9 requires. Roster is unchanged (same 5 SUTs), so m is unchanged by formula.
2. **No pilot comparisons except with the standing caveats.** The 24b bank differs from
   the pilot bank (d07 items unscorable then; B02 re-keyed; d05 CSR silently waived on
   zero-budget items; d04 zero-keyed items pooled into the signed mean; four items'
   prompt text changed). Any pilot juxtaposition cites
   `20260724-changed-items-smoke-report.md` §"Comparability (C9)". Design-08 is its own
   C9 line: this is the first full-bank run under the post-anchor rubric, and pre-anchor
   d08 verdicts (pilot, smoke judge-A stores) are not comparable cells.
3. **Comparative claims only per the ratified families, and only where they survive
   R4** — same direction under judge-A and judge-B. A flip is reported as
   "judge-sensitive — no SUT claim." Everything else is descriptive cells with Wilson
   95% intervals, n and excluded adjacent. **No rankings, no composites, no SUT
   leaderboard language, no significance stars, no "significant" as an adjective (R3).**
   C4 preconditions apply (certified judges for 06/09; same-family exclusion R5 for
   gpt-4.1-mini × judge-A and llama-3.3-70b × judge-B); C5 n-floors (multi-turn <10
   ladders, single-turn <20 admins ⇒ insufficient-n, listed not compared); C7 voids any
   pair whose exclusion rates differ by >10 points.
4. **Design-02 surface per the A′ ruling** (`RULINGS-APPLIED-20260724d.md`):
   `break_turn` is the **sole headline**. `pushback_rate` is reported as a **SECONDARY**
   metric, **per-judge only, never pooled across judges**, every cell naming its judge,
   and carrying verbatim: *"cross-judge stability of `pushback_with_alternative` is
   untested; all pre-2026-07-24b figures are single-judge (judge-A era)."*
5. **Public bank only. The holdout is untouched** and remains quarantined for a future
   blind first-use run.

### What this run buys the governance queue

- **Per-judge `pushback_rate` stability** across judge-A and judge-B at full bank —
  the evidence base for the deferred design-02 headline re-decision
  (`RULINGS-APPLIED-20260724d` condition 3). The run **presents** this evidence and
  **does not decide** the promotion.
- **First C9-clean pre-registered comparison surface** (item 1 above).
- **First full-bank read of the post-anchor design-08 rubric**, including whether the
  `protected→steamrolled` boundary flagged as judge-dependent in the smoke
  (4 of 30 B02 verdicts) persists at full n.
- **3-epoch stochastic-stability bands** on every headline metric — the smoke saw
  epoch ranges up to 0.50 on d02 `break_rate` at n=2 items; full bank tests whether
  that is item-count noise or instrument instability.

---

## 7. Run plan (on GO)

1. **3 independent single-epoch runs per SUT**, not `--epochs 3` — the
   recompute/rescore tooling is not epoch-aware. Pattern:
   `logs/changed-items-smoke-20260724/run_matrix.sh`, with the `item_ids` filter
   dropped so the full bank runs. Judge-A inline at run time.
2. **Log root: `logs/fullbank-3ep-20260724/`** — the path must never contain the
   substring `rescore`; `recompute_metrics.py` and `rescore.py` silently skip any log
   path containing it, which is what forced the smoke's mid-session rename.
3. **Judge-B pass** via `tools/rescore/rescore.py --judge-b
   openrouter/meta-llama/llama-3.3-70b-instruct` after all epochs land. The tools glob
   `*.eval` at the **top level** of `--log-dir`, so each pass is scoped by symlinking
   the target epoch's logs into a flat directory.
4. **Offline aggregation** reusing `aggregate_epochs.py` (including its indirect
   literal-parser accessor idiom, which keeps the vault security write-hook satisfied).
5. **Spend tally** from eval-log token counts × §2 prices, reported actual vs ceiling.
6. **If any defect forces a code or bank edit mid-run: STOP** and seek an owner ruling
   (F11). Do not repair in flight.

## 8. Authorization requested

| Item | Value |
|---|---|
| Expected | **$10.90** |
| **Ceiling** | **$16.00** |
| Scope | public bank rev 2026-07-24b, 10 designs × 5 SUTs × 3 epochs, judge-A inline + full judge-B rescore |
| Excluded | holdout (quarantined); any bank/rubric/metric edit; any SUT-roster change |
| Blocking pre-condition | §5 classifier-pin ruling |

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
