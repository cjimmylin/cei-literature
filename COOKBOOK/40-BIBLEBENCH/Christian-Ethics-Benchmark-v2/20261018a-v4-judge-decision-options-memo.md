# 20261018a — v4 judging-architecture options memo (stored evidence only; owner decisions pending)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-18 · **Spend:** $0. No model call was made, and no stored log was re-read.
This memo is built from committed reports and rulings only.
**Status: MEMO, which authorizes nothing.** It drafts the judging-architecture decision listed
as pending owner decision 2 in `20260806a-boot-prompt-v4a-authoring-remainder.md` §5. It also
records the related owner decisions (§5 items 1, 3, and 4, plus the holdout-history question) as
decision lines. Requested by the owner (relayed 2026-10-18) after a decision brief. Newest ruling
is still `RULINGS-APPLIED-20260802a`; this memo is not a ruling, and nothing in it is in force
until a new `RULINGS-APPLIED-*` file adopts it.
**Every number below is a probe or pilot diagnostic quoted from its source report. None is a
WALKWORTHY number, and none supports a comparative system claim.** Cost figures marked
*estimate* are projections, not measurements. They need a live-price preflight and a calibration
micro-run before any spend (the `-h` precedent).

---

## 1. The problem: the two pinned judges measure different things

The v4 instrument pins two judges (spec `20260731j-walkworthy-v4-design-spec.md` §4.2): judge-A is
`openai/gpt-4.1-nano`, and judge-B is `meta-llama/llama-3.3-70b-instruct`. The ratified gates rest
on their agreement. A dimension passes §5.4(c) only with contrast-sign agreement plus an item-level
cross-judge correlation of at least 0.30. A crossing reaches the confirmatory tier only with judge-B
sign agreement (§6.3), and the ship rule needs at least one confirmatory crossing (§6.7; ratified in
`RULINGS-APPLIED-20260731n.md` R1–R2). Both named crossings, X-1 and X-2, run a leg through the
judged design d04 (§6.1). The stored evidence says the two judges do not share a reading of the
constructs:

- **d02 (P-PRESSURE), hardened re-pilot** (`20260801c-d02-hardened-repilot-report.md` §2–3):
  - The judges agreed on the modal per-response "holds the keyed standard" read in only 9 of 81
    cells (11.1 pct).
  - judge-B never used "partial".
  - The mean hold read for claude45 was 0.242 under judge-A and 1.948 under judge-B, on a 0–2
    scale.
  - Cross-judge ranking τ-b moved from +1/3 in the first pilot to −1/3, which fails the ratified
    0.60 protocol gate (spec §2.5). Each judge is internally coherent, with 0 contradictions,
    which points to a construct-level split rather than noise.
  - The report names the levers as "judge selection/calibration or keyed-standard clarification"
    and leaves the choice to the owner (§3, §7).
- **d01 (P-OBEDIENCE), v4-T Claude-tier probe** (`20260802c-v4t-tier-probe-report.md` §2, §5–6):
  - judge-A recovered the expected Haiku < Sonnet < Opus gradient, with keyed-class rates of
    0.847, 0.908, and 0.990. Its Opus − Haiku interval excludes zero:
    +0.143 [+0.071, +0.224].
  - judge-B compressed all three tiers to 0.94–0.98 and found no gradient: Opus − Haiku is
    −0.020 [−0.063, +0.021].
  - Response-level raw agreement is 0.896, yet the item-level Opus − Haiku gap correlation
    between the judges is only Pearson 0.125. The disagreements sit exactly where the tier signal
    lives.
  - judge-B also produced 5 degenerate, unscorable outputs out of 294.
- **d07 (P-COUNSEL), v4-C determinate re-judge** (`20260731o-v4c-execution-report.md` §2):
  - Breaking the holistic label into three yes/no questions raised per-turn agreement from 0.388
    to 0.735 (κ 0.565).
  - The residual is q2 ("endorses continuing"): κ 0.282, with a yes-rate of 0.216 under judge-A
    against 0.057 under judge-B.
  - The anchored q2 definition (`20260802e-d07-anchored-q2-definition.md`) was written to fix
    this but has not been tested.
- **Earlier meta-audit with two strong referees** (`20260717-sol-referee-results.md` Findings 1–2
  and 5; companion `20260716-opus-referee-results.md`). This was $0 API spend, non-benchmark, and
  owner-directed.
  - On the d02 disagreement stratum, the Opus and GPT-5.6-Sol referees agreed with each other at
    0.735 (κ 0.653). Each agreed with each shipped judge at only 0.23–0.27.
  - On d07, both referees backed judge-B on 225 of 392 turns, against judge-A on 48.
  - Referee concordance is reference-model consensus, not ground truth (that report's own
    guardrail).
- **One limit on what a judge swap can do** (`RULINGS-APPLIED-20260729d.md` L56–63): the v3 d03
  headline sign was set by a prompt ambiguity, and "a stronger judge cannot fix an underdetermined
  referent."

**Net read.** Each judge fails on a different design. judge-B fails on d01 and d02 through ceiling
compression, no partial reads, and degenerate outputs. judge-A diverges from both referees on
d07. Rubric wording is also part of the problem on d02, d03, and d07. As configured, the B-phase
would spend about $180–230 (spec §7) on a gate whose judge-B sign-agreement requirement the stored
data already strains.

## 2. Options

| Option | What it is | What it needs | Cost and risk | Evidence |
|---|---|---|---|---|
| (a) Keep both judges and adjudicate disagreements | The pinned pair stays. Disagreeing cells go to an adjudicator: the owner, or a third model on those cells only | An adjudicator. A gate amendment if adjudicated values are to stand in for judge-B sign agreement, because §5.4(c) and §6.3 are ratified two-judge rules | $0 API if the owner adjudicates, but owner time scales with the disagreement count (d02: 72 of 81 cells disagree on the modal read). The adjudicator in effect becomes a third judge | The shipped pair diverges from strong-model consensus on d02 (referee arms) |
| (b) Replace one judge | Swap judge-B (or judge-A) for a pinned candidate model | The owner names a candidate; the documents name none. Stored-data validation (§3). A new instrument version at the v4.0 freeze (spec §5.1). Repricing of B1/B2. Complete-case retention of at least 85 pct (spec §4.2) | B-phase judging cost changes; see §4. **Which judge to swap depends on the design:** the d01/d02 evidence argues for replacing judge-B, but the d07 referee evidence argues against judge-A | §1 bullets 1–4 |
| (c) Add a third judge | Score by majority or median of three | Amendment of the ratified two-judge gates. Three-judge rescore tooling. One more judge's calls per phase. The subscription channels (Opus, Sol) are smoke-only for measurement (`AGENTS.md` rule 3), so a third instrument judge must be an API model | Higher B-phase judging cost; gate redesign needs owner ratification | Strong referees agreed with each other far more than with either shipped judge (§1 bullet 4) |
| (d) Change rubrics and anchors | Clarify keyed standards: a d02 "holds the keyed standard" anchor block in the style of `20260802e`, plus the existing anchored q2 for d07 | $0 authoring. Owner authorization to re-judge stored responses. The changes enter the v4.0 instrument at freeze | Cheapest option. Cannot repair a judge that is weak on clear items | d07's yes/no decomposition raised agreement from 0.388 to 0.735. The d03 ambiguity ruling. The d02 report names keyed-standard clarification as a lever |
| (e) Combination: test (d) and one (b) candidate on stored data, then decide | Stages 0–3 below | Decide a/b/c on the results | About $1.6 for the recommended package (estimate; §3) | All of the above |

**Candidate-selection criteria, if (b) or (c) is pursued.** The documents name no candidate, so
the owner chooses. The criteria below are drawn from rulings already on record:

1. **Vendor overlap with the 7 reference models (spec §4.1).** judge-A (OpenAI) already overlaps
   gpt-5 and gpt-4.1-mini. judge-B (Meta) has no overlap. Claude judges conflict with
   claude-sonnet-4.5 in the panel, and the v4-T ruling barred Claude judging Claude
   (`RULINGS-APPLIED-20260802a.md` R1.5).
2. **Parse reliability:** retention of at least 85 pct.
3. **A pinned OpenRouter slug, re-verified at launch.**
4. **Effect on B-phase cost (§4).**

## 3. Proposed re-judge plan on stored responses (for owner authorization)

**Precondition.** The stored responses live in gitignored run trees: `logs/d02-btpilot2-20260801/`,
`logs/tier-probe-20260802/`, `logs/d07-detrubric-20260731/`, and their probe sources. These are
not in every checkout, so the plan must run on the clone that holds them. No SUT calls are made,
and the holdout is never read.

**Stage 0 ($0, authoring and tooling).**
- Write a d02 keyed-standard anchor block.
- Add a judge-override flag and price entry to the three audit tools. Each hardcodes the two
  judges today: `tools/audit/d02_davidson_bt_pilot.py` L112–119, `d07_determinate_rubric.py`
  L86–92, and `tier_probe_claude_oauth.py` L107–112. `tools/audit/` is not pinned.
- Pre-commit the read-outs below.
- Use new log roots only.

**Paid stages.** Cost basis is the per-call actuals recorded in the project's own reports. The
judge-A price of $0.10/$0.40 per M tokens is recorded at `tools/audit/d02_davidson_bt_pilot.py`
L118.

| Stage | Stored units | Judges | Calls | Cost basis | Cost (estimate) |
|---|---|---|---|---|---|
| 1a. d02 under the new anchor | Hardened census: 7 items × 3 epochs × 6 pairs × 2 orderings, minus the 3 empty cells (234 per judge) | A + B | 468 | Same census cost $0.1776 actual (`20260801c` §6) | about $0.18 |
| 1b. d07 under the anchored q2 | 750 turns, 135 arcs | A + B | 1,552 | Same census cost $0.221 actual (`20260731o` §1) | about $0.22 |
| 2. One candidate judge on d02 + d01 | 234 d02 comparisons + 294 v4-T d01 responses | candidate | 528 | judge-A per call: about $0.00025 on d02 (calculated as $0.0581 / 234) and about $0.0002 on d01 (calculated as ($0.1168 − $0.003 calibration) / 588) | Scales with the candidate's price relative to judge-A (k = price multiple): k = 1 → about $0.12; k = 10 → about $1.2. A reasoning-class model at about $0.03 per call → about $16. The $0.03 is inferred from the ~3,400 completion tokens per call at $10 per M measured for gpt-5 as a SUT (`RULINGS-APPLIED-20260731h.md`) |
| 2+. (optional) Candidate on d07 | 776 turns | candidate | 776 | v4-C about $0.00014 per call per judge | k = 10 → about $1.1; reasoning-class → about $23 |
| 3. Referee arm (optional) | Same units | Opus (Claude Code agent) + Sol (codex) | — | JR precedent: $0 API (`RULINGS-APPLIED-20260729.md` L81) | $0 API (uses subscription capacity). Non-benchmark reference only, owner-directed as the JR arms were |

**Recommended package:**
- Stage 0, Stage 1, Stage 2 with one candidate at k ≤ 10, and Stage 3.
- Projected cost is about $1.6 or less (estimate).
- **Proposed hard ceiling: $3.00.** That is about 2× the projection, the project's usual margin.
- Calibration micro-run before each paid block; stop and report on any ceiling breach.
- If the owner also wants a reasoning-class candidate tested, add about $16 for d02 + d01 (about
  $39 with d07; both estimates). Set that ceiling after its calibration run, at 2× the calibrated
  projection.

**Pre-committed read-outs (proposed; diagnostics only, never WALKWORTHY numbers):**
1. Complete-case retention of at least 85 pct for every judge, per spec §4.2.
2. d01: does candidate × judge-A meet the §5.4(c) form? That means item-level r of at least 0.30,
   plus sign agreement on the Opus − Haiku and Opus − Sonnet contrasts. Report the known-groups
   gradient with an item-clustered bootstrap, as in `20260802c`.
3. d02: per-response modal hold-read agreement with each judge, and with the referee consensus if
   Stage 3 runs (baseline: 9 of 81). Cross-judge BT τ-b is reported as a diagnostic only: at n = 4
   the lattice cannot support a gate reading (`20260801c` §5).
4. d07: q2 κ against the 0.282 baseline, and the pole-flip rate against 10.9 pct.

Referee concordance is reference-model consensus, not ground truth, and strata are never pooled.

## 4. What the choice does to B-phase cost (estimate)

The spec costs each of B1 and B2 at about $90–115 (§7), mostly SUT sampling. One phase is roughly
7 models × ~150 items × 3 runs, about 3,150 judged administrations per judge. Multi-turn designs
judged per turn add more. The *estimates* below use this project's recorded per-call figures:

- **Current pins:** judging costs about $1–3 per phase.
- **A k = 10 judge replacing or added to the pair:** about $8 more per phase.
- **A reasoning-class judge at about $0.03 per call:** about $95 more per phase, which roughly
  doubles a phase's cost.

These figures should be repriced in the B1 ruling.

## 5. Owner decision lines

| # | Decision | Options | Recommendation (one-line reason) | Source |
|---|---|---|---|---|
| D1 | Judging architecture | (a) keep and adjudicate · (b) replace one · (c) add a third · (d) rubrics and anchors · (e) test (d) and one (b) candidate first | **(e): authorize the §3 recommended package at a $3.00 hard ceiling, then decide among a, b, and c on its results.** The cheapest way to de-risk about $180–230 of B-phase spend | `20260806a` §5 item 2; §1–4 above |
| D2 | Which candidate judge to test | Owner names one model, or authorizes a $0 shortlist by the §2 criteria | Name one non-Claude model at k ≤ 10 with no reference-panel vendor overlap. The documents name none | §2 |
| D3 | P-PRESSURE (d02) in v4.0 | Keep with a judge or anchor fix · redesign · drop from v4.0 to a later version | **Drop from v4.0, but keep its stored responses as the D1 test bed.** It missed the 0.60 gate in both pilots, the split is construct-level, the ship rule does not depend on d02 (`20260731o` §3), and multi-turn administration costs about 3× (spec §4.3) | `20260806a` §5 item 3; `20260801c` §7 |
| D4 | B1+B2 scale (~$180–230) | Approve now (B1 and B2 each still need a hard-ceiling ruling) · approve B1 only (~$90–115) later · keep deferred · stop at the declared-ladder fallback (spec §6.7) | **Keep deferred; revisit as "B1 only" after D1 is ruled and the v4-A authoring remainder is done.** Waiting costs nothing, because B1 needs d03, d04, d08, and d10 items that do not exist yet. Even a clean B2 has only about 0.75–0.80 power per crossing's d04 leg (spec §6.6) | `20260806a` §5 item 1; `20260731o` §7; `RULINGS-APPLIED-20260731n.md` R3 |
| D5 | Freeze-review conventions | Accept as adopted · harmonize · revisit | **Accept the remedy-escape convention, and disclose the hard-slot-0 adjudication asymmetry, as already reported. Choose one guard-ordinal convention before B1, so no keys change after results are visible.** The documents do not say which convention is correct. Harmonizing touches 10–20 tail slots and only the τ-b secondary. Balance escape coverage at bank level only if the rationale judge needs it | `20260806a` §5 item 4; `20260802g-d05-hardened-authoring-report.md` §5 |
| D6 | Holdout in pushed git history: 8 d05 holdout items in commits from `2c67334cb` onward, untracked since `31dc22c42` | Purge (rewrite the history of a trunk shared with sibling projects) · accept and replace the 8 items with fresh holdout items, quarantined at creation ($0 authoring) · accept and disclose only | **Accept and replace, and record the exposure. Do not rewrite shared history.** Replacing costs $0 and keeps the holdout blind. Repo visibility is not documented; if the remote is private, disclosure alone may suffice | `AGENTS.md` item 6 |
| D7 | P-COMMITMENT | Stays not advanced · revive | No action needed; revival needs a new ruling and the four prerequisites already listed | `RULINGS-APPLIED-20260801a.md` R3 |

Unchanged by this memo: v4-A stays open at $0 under `RULINGS-APPLIED-20260801a` R1. The
`20260806a` boot prompt remains the entry point. The holdout stays closed. No pinned component is
touched.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
