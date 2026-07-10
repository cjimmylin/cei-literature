# Next session boot prompt — WALKWORTHY Fable adjudication (post-P0-pilot)

**Model: FABLE.** This is the judgment-heavy pre-O4 adjudication — gate-reading, the PR-3
ruling, judge selection + validation design, and the §3.4 human-label protocol — the work
the Fable-week protocol reserves for the main loop, and the window closes ~2026-07-11. Keep
Fable in the main loop for judgment; delegate every mechanical sub-task (re-reading the
150-record JSONL, recomputing a stat, drafting label-instrument boilerplate, grep/verify)
to Opus/Sonnet subagents with an explicit `model=`.

Start a fresh session, `/model` → Fable, then paste everything below the line.

---

Continue the WALKWORTHY benchmark project (Christian-ethics values-alignment benchmarks) —
FABLE ADJUDICATION session, after the §1 P0 pilot produced the first real cross-model data.
This is a JUDGMENT session: produce binding adjudication docs + rulings, NOT code (the O4
build is a later Opus session). No live model calls needed.

SCOPE LOCK: stay entirely within CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/.
Do NOT touch, read for input, or import from any sibling bench (WCF-Bench, FruitBench, CookBook,
SermonMount, CorinthLove, DUPLEX, INNOVATION). Differentiate only vs published literature.

START by reading, in order:
1. 00-PORTFOLIO/20260709-O4prep-session-handoff.md — the re-entry doc (what the panel runner +
   pilot are, findings F-1..F-4, the state).
2. 00-PORTFOLIO/20260709-p0-pilot-report.md — the pilot results being adjudicated (§1 scores +
   spread, §1b judge-pair agreement, §4 substantive signals, the ceiling/zero-variance flags).
3. runs/20260709-p0-pilot/panel_summary.json — machine-readable cells + design_spread + judge_pair
   + refusal_accounting + cost (delegate the read to a Sonnet subagent; get back the tables, not the raw).
4. Authority stack (FROZEN — do not amend without logging): master-plan §3 (the 10 pre-registered
   gates) + §4 (headline analyses = the real per-design primary metrics); the normative charter
   §6.4 (refusal semantics — load-bearing for PR-3), §6.5 (cross-family judges), §6.6 (holdout);
   the item playbook §7 (difficulty engineering); 00-PORTFOLIO/PENDING-RULINGS.md (PR-1..PR-5).

FRAME (critical — do not over-claim): the pilot is DESCRIPTIVE / PRE-GATE — n=5/design, 3 models,
judges NOT yet human-validated, and scores come from `run._scalarize` (a coarse illustrative map
from verdicts[0]), NOT the per-design §4 primary metrics. So this session does NOT issue a final
gate verdict (that needs the full O4 panel + human labels). It does the judgment that MUST precede
O4 while the data is fresh and Fable is available:

1. GATE PRE-REGISTRATION (the highest-value Fable output). For each §3 gate, freeze the EXACT O4
   computation + decision rule so O4 is mechanical: the statistic, the input metric (the real §4
   primary metric per design — NOT the pilot scalar), the threshold, and the failure→action path
   (difficulty ladder vs item-kill vs judge-disqualify). Flag the gap that the harness has
   `_scalarize` but NOT the §4 primary metrics (collapse_threshold, break_turn, say_do_gap,
   covert_overt_gap, symmetry_index, constraint_satisfaction_rate, …) — specify each so the O4
   build implements them. Produce a binding pre-registration memo (dated).

2. READ THE PILOT SIGNALS as watch-list, not verdict: the 03 zero-variance flag (all 3 = 60.0),
   the 04/05 ceiling flag (two models at 100 — and note 05's primary is judge-free allocation, not
   the rationale scalar), the 02/07 judge-divergence (agreement 0.43/0.49 on the per-turn designs).
   Decide what each implies for O4 (difficulty engineering? item-kill candidates to confirm at full
   n? judges untrustworthy on per-turn designs until validated?). Descriptive → O4 confirms.

3. RULE PR-3 (refusal taxonomy on principled non-compliance + the verdicts[0] keyed-outcome
   coupling). This is a charter §6.4 semantics judgment the pilot now informs (refusal accounting:
   helpful 111 / policy_violating_compliance 27 / unnecessary_refusal 12, some of the 12 being the
   mislabel). Adjudicate to a disposition (option a/b/c in PR-3) + specify the fix: derive the
   keyed_outcome from the ADJUDICATED value, not verdicts[0]. If the ruling needs a charter
   amendment, that stays Jimmy-only — flag it; otherwise record the Fable ruling in PENDING-RULINGS.

4. JUDGE MODELS for O4 + the §3.4 VALIDATION GATE. The pilot's judge divergence (fragile on per-turn
   designs) is the core validity signal. Decide: which judge models + how many for O4 (the pilot used
   fast mid gpt-4.1-mini + gemini-2.5-flash — is that the O4 pair, or add a third family / a stronger
   judge on the per-turn designs?); and the rule that NO score ships until judges pass §3.4 (κw ≥ 0.65
   AND ≥ 80% of the human-human ceiling) against the human labels. Pre-register this.

5. DESIGN the §3.4 HUMAN-LABEL PROTOCOL (the long pole — Jimmy executes). ~60 items/design stratified
   (area × difficulty × stratum), the labeling instrument (what a human scores per design's rubric),
   the human-human ceiling estimate (double-label a subset), the κw computation, and the adjudication
   of judge-vs-human. Deliver it so Jimmy can run the labeling with no further design.

FIX-MECHANICS-ONLY still holds: do NOT edit items from model performance. Anything that turns out to
need a charter amendment or a Jimmy-only call → PENDING-RULINGS, flagged, not guessed.

END WITH: (a) a binding gate-pre-registration + pilot-adjudication memo (dated); (b) the PR-3 ruling
in PENDING-RULINGS + the verdicts[0]-coupling fix spec; (c) the O4 judge-selection decision + §3.4
validation rule; (d) the §3.4 human-label protocol doc; (e) a dated handoff for the O4-BUILD Opus
session (which implements: the §4 primary metrics, PR-3 fix, PR-5 empty-retry/provider backend, 06/09
reference answers [M-3], then the ≥6-model full-split panel via `run_panel` — drop `--items-per-design`
— with all §3 gate stats); (f) a memory update + a final commit (stage WALKWORTHY paths explicitly —
sibling sessions share the index). Jimmy still owes: the human labels (the long pole) + any charter
ratifications.
