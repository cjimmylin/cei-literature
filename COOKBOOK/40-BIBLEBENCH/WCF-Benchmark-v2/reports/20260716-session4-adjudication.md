# WCF-Benchmark-v2 — Session 4 Adjudication Memo

> **EXPLORATORY / NON-QUOTABLE.** Fable main-loop adjudication of the 5-critic
> adversarial review (2026-07-16). Inputs: `reports/20260716-session4-critique-0{1..5}-*.md`
> (43 findings: 7 PILOT-BLOCKING, 19 MUST-FIX, 17 DEFER). Anti-leakage held: all five
> critics confirmed no peer-output reads.
>
> Disposition vocabulary: **FIX-NOW** (this session, before pilot) /
> **PILOT-OK-DISCLOSE** (pilot proceeds; disclosure mandatory in the session-4 report) /
> **DEFER** (recorded, not this session). Item-content edits are logged per-item in
> `reports/20260716-session4-item-edit-log.md` (Agent B appendix).

---

## 1. The design decision: grader-panel family collision (weakness #7 / GP-03)

**DECISION — keep the validated median-of-3 panel (gemini-2.5-flash + deepseek-chat +
mistral-small-2603); resolve the collision on the ROSTER side: pilot SUTs are drawn only
from families ∉ {google, deepseek, mistral}. The kin-delta measurement is DEFERRED.**

Rationale:
1. The panel is the only *characterized* instrument we have — the 452×3 matrix, the
   per-grader severity profile (gemini −8.6 vs the pair), and the MAD structure all
   describe THIS trio. Critic 2's option (b) (never-SUT panel) buys kin-freedom by
   swapping in two unvalidated graders, silently discarding every panel measurement made
   to date. That trade is bad while a kin-free roster is available.
2. Option (a) (per-SUT substitution) varies the instrument across the leaderboard —
   reintroducing exactly the grader-of-choice artifact the panel was adopted to remove.
3. A kin-free roster is cheap: 4 of 6 baseline SUTs (qwen3.7-plus, claude-haiku-4.5,
   llama-4-maverick, gpt-4o-mini) are non-kin, so continuity survives intact.
4. Consequence, disclosed: **deepseek-chat and mistral-large baselines are outside the
   panel-comparable set.** If a future session must rank a deepseek/mistral/google SUT,
   it must FIRST run the kin-delta experiment critic 2 specified (grade a kin SUT under
   the default panel vs a kin-free panel; no such data exists anywhere in the vault).
5. Critic 2's supporting evidence sharpens the stakes: deepseek+mistral-small are
   near-twins (MAD 8.2) and set the median in the large majority of samples, so kin
   contamination would flow straight into headline numbers. Roster-side avoidance makes
   that channel structurally impossible for this pilot.

## 2. Disposition table — all 43 findings

| ID | Sev (critic) | Disposition | Rationale (one line) |
|----|--------------|-------------|----------------------|
| CV-01 | PILOT-BLOCKING | **FIX-NOW (config)** | Pilot runs the median panel (v2.1 default); single-grader numbers never quoted standalone again; per-grader severity table disclosed. |
| CV-02 | PILOT-BLOCKING | **FIX-NOW (bank)** | Quarantine 5 turn-conditioned items; strip 3 control-twin criteria + renormalize; per-item log. Counterfactual criteria are unscoreable in single-completion mode. |
| CV-03 | MUST-FIX | **FIX-NOW (bank, conditional)** | Restore anchor clause text into the grading standard for anchor items IF the text exists in source YAML; else falls back to PILOT-OK-DISCLOSE. |
| CV-04 | MUST-FIX | **FIX-NOW (bank)** | Split the contested "decline + grounding" criterion into binary decline (1.0) + named-heads checklist (0.5). Merged with CG-02 (same items, same defect). |
| CV-05 | MUST-FIX | **DEFER + disclose** | 255 criteria across the bank — too large for this session; disclose the 23.6% double-barreled figure. Median panel does NOT fix this (critic 1's closing warning). |
| CV-06 | MUST-FIX | **PILOT-OK-DISCLOSE** | Report the honest discrimination figure (~28/204 items separate frontier models under a stable grader); item authoring is out of scope. |
| CV-07 | MUST-FIX | **PILOT-OK-DISCLOSE** | Same disclosure; panel reduces the grader-noise half of the confound. |
| CV-08 | DEFER | **PILOT-OK-DISCLOSE** | Median discards the lone gemini zero; effectively moot under panel config. |
| CV-09 | DEFER | **DEFER** | Ordinal partial-credit table is a v-next rubric improvement. |
| CV-10 | DEFER | **DEFER** | Document weighting logic before per-item scores are ever quoted. |
| GP-01 | PILOT-BLOCKING | **FIX-NOW (code)** | Last-match + word-boundary pattern; one line; closes the injection lever and matches Inspect's documented design. |
| GP-02 | MUST-FIX | **FIX-NOW (code)** | Neutralize the WCF template's custom markers in the SUT answer before grading (or adopt covered markers); verified injection chain with GP-01. |
| GP-03 | MUST-FIX | **DECIDED (§1)** | Keep panel; kin-free roster; defer kin-delta measurement; disclose. |
| GP-04 | MUST-FIX | **FIX-NOW (code)** | 0–100 guard, out-of-range → unscored (mirrors `regrade_graders.py`). |
| GP-05 | MUST-FIX | **FIX-NOW (code)** | Unified by the GP-01 fix — harness and analysis parser become byte-consistent. |
| GP-06 | MUST-FIX | **FIX-NOW (code)** | Panel-quorum + effective-panel-size metadata; non-numeric parsed values → unscored, never 0. |
| GP-07 | DEFER | **FIX-NOW (code, bundled)** | Same custom reducer records all three per-grader values in metadata — restores audit without re-runs. Upgraded from DEFER because it rides GP-06 for free. |
| GP-08 | DEFER | **FIX-NOW (code, bundled)** | Word-boundary guard is part of the GP-01 pattern. |
| GP-09 | DEFER | **DEFER** | Within-grader run-to-run MAD is a cheap future experiment; not blocking. |
| GP-10 | DEFER | **FIX-NOW (code)** | Relabel episode history "[BEGIN TRANSCRIPT]"; note final-turn duplication. Cheap, grader-facing. |
| GP-11 | DEFER | **FIX-NOW (tests)** | Pipeline tests pin last-match/clamp/injection/median-edge at $0 — required regression guard for every other fix. |
| EP-01 | MUST-FIX | **PILOT-OK-DISCLOSE + DEFER** | Reframe metric as "single-inflection pressure compliance" in all reporting; the 4-turn escalation subset is a designed future experiment. |
| EP-02 | MUST-FIX | **PILOT-OK-DISCLOSE** | Episode results reported as per-item profile + harm-class clusters; no scalar episode headline. |
| EP-03 | MUST-FIX | **FIX-NOW (config)** | Pilot episodes run under the median panel; old single-grader episode numbers carry the caveat. |
| EP-04 | DEFER | **FIX-NOW (code)** | Drop the vacuous `grouped(mean(),"tier")` on episodes (one line). |
| EP-05 | DEFER | **PILOT-OK-DISCLOSE** | Never splice the v2.1-discrimination claim (4o-mini/haiku/qwen runs) with the deepseek collapse (generic run). |
| EP-06 | DEFER | **DEFER** | Pressure-lever decomposition is a future diagnostic variant. |
| EP-07 | DEFER | **DEFER** | Telegraph risk empirically near-zero (0–2/22 meta-awareness); optional clean variant later. |
| CG-01 | MUST-FIX | **PILOT-OK-DISCLOSE + DEFER** | Pilot leaderboard carries a graded-answer-length column; qwen `<think>` asymmetry disclosed next to any qwen-#1 claim; truncation re-grade sensitivity deferred (costs live calls). |
| CG-02 | MUST-FIX | **FIX-NOW (bank)** | Merged with CV-04: gate decline credit on naming the specific incommensurable heads (4 contested + 3 AGG incomparable items). |
| CG-03 | DEFER | **FIX-NOW (bank, trivial) + disclose** | Tag the 7 hybrid items with `recall_hybrid` metadata in the converter so "conduct-only" is never overstated. |
| CG-04 | DEFER | **DEFER** | Future regrades capture `len()` of the post-strip completion per row. |
| CG-05 | DEFER | **PILOT-OK-DISCLOSE** | MCQ-leg contamination bounded ≤2/5–6 pts; disclose, no change. |
| ST-01 | PILOT-BLOCKING | **FIX-NOW (reporting)** | Session-4+ reporting standard: every mean carries ±SE; whole-number rounding; tier framing. Old reports are IMMUTABLE — fixes land in new reports only. |
| ST-02 | PILOT-BLOCKING | **FIX-NOW (reporting)** | Leaderboards reported as tiers with ties explicit ({qwen} > {haiku ≈ mistral > deepseek} > {llama ≈ 4o}). |
| ST-03 | PILOT-BLOCKING | **FIX-NOW (framing)** | No single→panel bridge exists; pilot numbers are panel-native on a different scale, stated plainly. Optional-if-budget: panel re-grade of stored qwen/llama responses to complete non-kin panel baselines. |
| ST-04 | PILOT-BLOCKING | **FIX-NOW (reporting)** | Contested (n=4): report 4 raw scores only, never means/ranks; growing n deferred. |
| ST-05 | MUST-FIX | **FIX-NOW (reporting)** | Strip family "leads on X" claims below 2·SE; only qwen-WHOLE and the llama COMP deficit survive. |
| ST-06 | MUST-FIX | **PILOT-OK-DISCLOSE** | Ceiling fraction (%=100) reported alongside every mean; harder items deferred. |
| ST-07 | MUST-FIX | **FIX-NOW (reporting)** | Episode results as count structure ("16/22 near-ceiling, 6/22 hard defections"), not midpoint means. |
| ST-08 | MUST-FIX | **FIX-NOW (reporting)** | Whole-number rounding + SE for all n<30 sub-bank means; ordinal between-model claims dropped. |
| ST-09 | DEFER | **FIX-NOW (reporting, trivial)** | Headline tags: [resolved] / [tier-tie] / [n-limited]. |
| ST-10 | DEFER | **PILOT-OK-DISCLOSE** | Grader-robustness claim scoped to the haiku>4o-mini gap only. |

## 3. Cross-critic conflicts adjudicated

1. **Verbosity: critic 1 (within-item coin flip, survived) vs critic 4 (CG-01 qwen
   asymmetry).** Not a contradiction — critic 1 tested length *within* the shared answer
   format; critic 4's concern is a *format* asymmetry unique to one SUT (two-stage
   reason-then-answer decode). Both stand. CG-01 stays disclosure-grade, not blocking:
   critic 4's own attack #3 found verbosity fails as a ranking driver, and the anchor
   +7.1 margin is equally consistent with real capability. The pilot mitigates by
   reporting the length column and never quoting a qwen-#1 without the caveat.
2. **Critic 2's panel recommendation (option b) vs this memo's roster-side resolution.**
   Overruled in favor of the validated instrument — see §1. The critic's own strongest
   evidence (deepseek/mistral near-twin dominance of the median) argues for keeping the
   characterized panel away from kin SUTs, not for replacing two of its members.
3. **Critic 5's "fix the reports first" vs Report Immutability (safety rule 3).** All
   reporting fixes are forward-only: they define the session-4 report standard. Session-3
   reports stand as historical snapshots; the session-4 report notes the corrections.
4. **deepseek 51.2:** critic 3 CONFIRMS the behavior (11/11 genuine compliance-with-harm,
   verbatim admissions); critic 5 shows the *number* is a 6-zero bimodal midpoint with
   ±9.4 SE. Both adopted: the finding is real and reportable as a count structure, the
   scalar is not.

## 4. FIX-NOW work orders (Phase 3)

**Agent A — grading pipeline (fileset: `src/wcf_tasks.py`, `src/templates/*`, new
`tests/test_grading.py`):** GP-01+GP-05+GP-08 (last-match word-boundary pattern),
GP-02 (marker neutralization), GP-04 (0–100 guard → unscored), GP-06+GP-07 (quorum +
per-grader metadata reducer), GP-10 (episode transcript relabel), EP-04 (drop vacuous
tier grouping), GP-11 (regression tests for all of the above). $0 mockllm smoke.

**Agent B — item bank via converter (fileset: `convert/yaml_to_jsonl.py`, `data/*.jsonl`
regeneration, `tests/test_converter.py`, `reports/20260716-session4-item-edit-log.md`):**
CV-02 (quarantine 5 turn-conditioned items: MEND-A-003, MEND-A-010, MEND-A-W305,
DUTY-C6-002, DUTY-C7-009; strip control-twin criteria from 3 anchors incl. PROOF-C1-W306
+ renormalize), CV-04+CG-02 (decline-credit gating on 4 contested + 3 AGG incomparable
items), CV-03 (anchor clause text into grading standard, conditional on YAML content),
CG-03 (tag 7 hybrid items). Source YAML remains UNTOUCHED; every edit logged old→new
with motivating finding ID.

**Reporting standard (Phase 4, main loop):** ST-01/02/04/05/07/08/09 + all
PILOT-OK-DISCLOSE items enter the session-4 report template as a guardrails section
(licensed vs forbidden claims, per critic 5's draft).

## 5. Pilot consequences (Phase 4 preview)

- Roster: 5 SUTs from non-kin families — qwen3.7-plus, claude-haiku-4.5, gpt-4o-mini,
  llama-4-maverick (4 continuity baselines) + 1 fresh non-kin family (xai/moonshot/etc.,
  slug + price verified live before commit).
- Config: median-of-3 panel, per-item pressure variant decision recorded at runbook time,
  patched bank (~199 main + 22 episodes after quarantine). Numbers are panel-native,
  patched-bank, new-parser — **not comparable to any session-2/3 frozen-config number**,
  and the report says so in the header.
- Forecast before run; ≤$10 total session spend → run; else runbook + ask Jimmy.

*Adjudicated in the Fable main loop, session 4, 2026-07-16.*
