# WALKWORTHY — Session O4-BUILD Handoff (2026-07-10, Opus) → O4-RUN

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**This session (Opus, EXECUTION):** built the OFFLINE half of the O4-build work list against
the frozen 2026-07-10 Fable specs — W1, W2, W3, W5, W7-module + W4-wiring, all TDD, all
committed. The LIVE half (W3 probes, W6 panel) + the data-dependent O4 report (W7) + the W4
reference fixes are the next session (O4-RUN). Split taken deliberately (the seam the boot
prompt offered): the frozen §B metrics + PR-3 semantics are correctness-critical and the panel
is a paid, checkpoint-resumable run — better to land the build verified than rush it before a
$-run. **159 → 255 pytest green** (recorded/mock only; NO live call in the suite).

> ⚠️ This file REPLACES the pre-session O4-build handoff of the same date (the prior version
> was the work list; this is the post-build state). The authority stack (gate memo, PR-3 ruling,
> label protocol) is UNCHANGED and still binding.

---

## Commits this session (WALKWORTHY paths only; ≥3 sessions share the index)
- `086bf9cd2` W1 — ten §B metrics + per-admin/terminal judging
- `17a74dccb` W2 — PR-3 R1–R4 (refusal ruling)
- `9694b65ec` W3 + W4-wiring — PR-5 backend/probe + reference anchoring
- `74299be26` W5 — label tooling
- `6190216c3` W7-module — gates_o4 + W4 reference review

## What landed (DONE, tested, committed)

### W1 — `walkworthy/metrics.py` (ten §B primary metrics)
- S (0–100) + H (hard-tier [0,1]) per (design, model), each **per-judge AND adjudicated**,
  with disagreement/defect **exclusions counted + published** (PR-3 R3). `serialize_design`
  + `design_level_headline`; `run_design` stubs replaced (G9 headline gaps wired).
- **S₀₁ FALLBACK IS ACTIVE (decided, not results-driven):** the 01 bank has NO runnable
  cost-ladder families — every item carries a single `cost_level ∈ {1,2,3}`, cost-0 controls
  are inline prose (never administered), `pair_id` = same-cost beneficiary twins. Verified
  structurally (diagnostic in-session). S₀₁ = 100 × full_obedience rate; obedience-by-cost-level
  is the descriptive survival curve. **Report this loudly in the O4 report.**
- Supporting mechanics (all §B-mandated, no item edits): **per_admin** scoring unit for the
  paired twins 03/04/08/10 (the judge now scores EACH administration by label — the gap/delta
  metrics were uncomputable from `administrations[0]` alone); **per_turn also scores the 07
  terminal artifact**; `adjudication.py` (agreement→value / disagreement→null, near-agreement
  combined by mean of the two agreeing judges = **PR-6**, logged); builders extract
  `keyed_expressed` (03) + `keyed_motive` direction (04); `ordo_constraints.py` = judge-free 05
  CSR checker (92 consensus floors parsed; remedy-escapes + 21 unparsed lines disclosed).

### W2 — PR-3 R1–R4 (`refusal.py`, `outcomes.py`, `run.py`, `retag.py`)
- R1 engagement-override, R2 keyed-coupled refusal branch (`appropriate_refusal` +
  `refusal_reason: principled_noncompliance`; `pending_adjudication` placeholder — NOT a 5th
  cell), R3 `verdicts[0]` decoupling (`scalar_by_judge` + `scalar_adjudicated`; keyed_outcome +
  every tag from the ADJUDICATED load-bearing state). `outcomes.py` = single source of truth.
- R4 retro re-tag → **`00-PORTFOLIO/20260710-pr3-retag-analysis.md`** (immutable originals; no
  live calls). First clean split: pilot's 12 `unnecessary_refusal` → 2 principled_noncompliance
  + 5 R1-override helpful + 3 violating + 2 pending; 48 cells → `pending_adjudication` (honest
  R3 consequence of pilot judge-disagreement → wave-1 human labels resolve them).

### W3 — PR-5 backend + probe (`openrouter_backend.py`, `probe.py`)
- Empty-200 retry (capped exponential, N=3) + OpenRouter `provider` prefs (default
  `allow_fallbacks=True`). `probe.py` reliability probe (1 cell/design, 0.9 ok-rate floor).

### W5 — label tooling (`label_sample.py`, `judge_validation.py`)
- `label_sample.draw_part_a` (deterministic seed 20260710, stratified, blind, fail-loud) +
  blind CSV (Q-R1/Q-R2) + instruction packet + Part B exporter. `judge_validation` κ engine
  (GOODNESS-weighted / quadratic / unweighted per §4), ceiling, AC1 + raw guard, G4 gate,
  detector P/R.

### W7-module — `gates_o4.py` (report deferred)
- G1/G2/G3(+perm p)/G6/G8 compute; G4/G5/G7 return PENDING. Validated on mock records.

### W4 — PARTIAL
- **Wiring DONE:** `references.bank_reference_provider` (06 refs + 09 determination/extraction
  anchors) wired into the panel's CLIJudges (previously built with NO provider — 06/09 were
  scored unanchored). 7/10 06 DSP pairs + 34/38 09 structures anchor now.
- **Authoring DRAFTED + REVIEWED (two-agent rule), NOT in the bank:** 3 missing DSP pairs
  (A01/K01/E01) drafted → `…-W4-06-references-DRAFT.md` (gitignored staging). Adversarial
  review → **`…-W4-06-references-REVIEW.md` (committed)**: all 3 = **REVISE** (attestation
  defects — K01 manufactures a verdict-split the corpus carries only as a method-split, a
  neutrality risk; A01/E01 mis-cited traditions), + existing-pair length flags D01/L03/N01.
  Fixes are mechanical (quoted in the review) + K01 needs a re-key. **06 stays PROVISIONAL
  until G5 regardless.**

---

## NEXT SESSION (O4-RUN) — do in this order

**Prereq (Jimmy):** OpenRouter key at `~/.codex/secrets/openrouter.env` (never print/commit).
Budget: pilot was $0.63/150 cells → full 344×≥6 panel = tens of dollars (F-1: 02/07 dominate
wall-clock; use per-SUT parallel resumable runs + the fast judges).

1. **W3 probe (LIVE):** `python -m walkworthy.probe --models <candidate SUTs + x-ai/grok-4>`
   → drop any below the 0.9 ok-rate floor (F-2). Commit the probe report.
2. **W6 panel (LIVE):** `python -m walkworthy.panel --items-per-design 0 --sut-models <≥6
   roster: OpenAI + Google + Claude-family + deepseek/mistral/llama/grok as probes allow>
   --judge1-model openai/gpt-4.1-mini --judge2-model google/gemini-2.5-flash --panel
   20260711-o4-panel --kind o4-panel`. Full split (344). Checkpoint-resumable (re-run same
   command to continue). **Tie-breaker judge (§E) on `needs_adjudication` cells with
   own-family exclusion is NOT yet wired into `run_panel`** — either wire it (a `run_panel`
   enhancement: after the pair, re-judge disagreement cells with the 3rd family, skip
   own-family SUT cells → human Part-B) or run the pair now and adjudicate disagreements via
   Part-B. Home-advantage: compute G1–G3 on the full panel AND panel-minus-generator-family;
   both rows (§E).
3. **W7 report (needs panel data):** `metrics.compute_all(panel_records, items)` →
   `gates_o4.compute_o4_gates(...)` (read the pinned capability composite via
   `capability_battery.py` at run time for G3) → render a NEW dated O4 report
   (`00-PORTFOLIO/20260711-o4-panel-report.md`): descriptive gate READINGS, **verdicts at O5**,
   scores PROVISIONAL pending G4, 06/09 additionally pending G5. State the S₀₁ fallback + the
   G3 power limitation loudly. G9 must headline say_do_gap(03) + covert_overt_gap(08).
4. **W5 draw (needs panel data):** `python -m walkworthy.label_sample --run 20260711-o4-panel`
   → `labels/…-partA-blind.csv` + instruction packets (draw anchors from the O3 smokes).
   Ship wave 1 = {02, 07, 01} to Jimmy (protocol §8).
5. **W4 fixes:** apply the review's mechanical relabels to A01/K01/E01 + re-key K01 + trim
   D01/L03/N01 length → Jimmy ratifies before they enter `DESIGNS/06-*.md`.

## Jimmy owes (NOT the build)
- Part A labels (~25–30 h, wave plan) + a 2nd labeler (or the disclosed test–retest fallback).
- 4 one-liner ratifications: PR-1(c), PR-2(ADVICE_SYSTEM), PR-3(§6.4-interpretation),
  PR-4(OpenRouter sanctioned). **+ new: PR-6** (near-agreement mean rule) — recommend ratify,
  does not block.
- The OpenRouter key.

## Standing cautions
- FIX-MECHANICS-ONLY held: no item edited from performance; the 06 refs are NOT in the bank.
- No gate VERDICTS, no item kills, no release claims (all O5/Jimmy).
- `git log -1` before staging; stage WALKWORTHY paths explicitly; never rewrite sibling commits.
- HOLDOUT never loaded/committed; `runs/*/scored_items.jsonl` gitignored; `*-DRAFT.md` gitignored.
- O5 is Fable-preferred (gate adjudication) if a window recurs.
