# FRUITBENCH — Session Handoff: THORNS (v2-02) P1 Build

**Written:** 2026-07-06 (Opus build session) · **For:** the next FRUITBENCH build session.
**Supersedes for status:** `20260706-NEXT-SESSION-HANDOFF.md` (that pointed here). **Authoritative status:** `20260706-POST-GATE-WORKLIST.md` §1 (now updated).

## What this session did

Built **THORNS (v2-02) P1** in EXECUTE mode. All deliverables on disk; one atomic commit of FRUITBENCH paths only.

**Real deliverables (no credentials needed):**
- `FRUITBENCH-v2/PILOTS/thorns/20260706-fresh-eyes-objections.md` — 11 builder objections (FO-8a), written before implementing.
- `FRUITBENCH-v2/PILOTS/thorns/20260706-feasibility-map.md` — full 9×15 feasibility audit (26 infeasible declared, 109 authorable) + the **frozen 20-cell slate** with per-cell dyad specs + quota proof.
- `FRUITBENCH-v2/ITEMS/thorns/` — **60-item bank** (bank/ + gold/ 2-file contamination split), `THORNS-AUTHORING-SPEC.md`, 5 batch logs. Static audit `HARNESS/thorns/audit_bank.py` = **all HARD checks pass**.
- `FRUITBENCH-v2/HARNESS/thorns/` — runnable harness: `audit_bank.py`, `model_adapters.py` (pluggable; live Anthropic/OpenAI adapters wired + role-family disjointness guard), `synthetic_reference.py`, `scorer.py` (MarkerScorer + JudgeScorer stub), `run_pilot.py`, `pilot_config.json`.
- `FRUITBENCH-v2/HARNESS/shared/` — `attacker-persona-v1.md` (FROZEN), `human-substitution-protocol.md` (FO-5).
- `FRUITBENCH-v2/PILOTS/thorns/20260706-p1-pilot-report.md` — **the authoritative writeup** (real vs synthetic clearly split), `20260706-mini-heatmap.md`, `20260706-pilot-results.json`.

**Adversarial review:** independent Opus reviewer, no KILLs; 5 FIX items applied + re-audited (F7 commitment-pinning ×2, villain-softening, CFT-distinctness, vicarious-attractor). 4 systemic notes → panel instructions (in the report §2).

**Real-model probe (N=4, single-vendor):** 3/3 aligned responses cleanly walk the fruit; the attacker-persona probe on envy-002 **still surfaced the flaw** — corroborates the D-21 ceiling-map risk (vice weakly attractive to frontier models). Report §3.

## Credential block (the one thing that gates the empirical result)

The P1 calibration/transfer/CFT gates need **live multi-vendor runs**; this environment has no API keys (only Anthropic SDK, no OpenAI). The gate numbers in `pilot-results.json` / `mini-heatmap.md` are from a **documented synthetic reference model — harness-validation only, NOT empirical**. To run the real pilot: report §6 (set `pilot_config.json` mode:live, supply keys, keep roles disjoint by family, wire cross-family judges into `JudgeScorer`, run the human-substitution sample). The harness is one config flag from a live run.

## Two items flagged for the second-pass Fable gate (FO-8, due after 3 P1s — this is P1 #1 of 3)

1. **Calibration-band aggregation is unspecified and moves G1.** Ensemble-mean band-pass (synthetic 63.3%) vs attacker-primary (55.0%) differ materially. The brief freezes the ensemble but not the aggregation. Fable should ratify mean / attacker-primary / max. (Report §4.1.)
2. **Frontier-attractiveness.** Telegraphed social-factional cells (S3: resentcorrect≈partisan; principals narrate the unfair ask) and the novel/limit cells (grievancefarm P9, paternalcrush W14) may need deeper embedding / higher payoff realism to move frontier models off the fruit floor. Only a credentialed run settles it. (Report §3, §4.)

## Next session (per build order 02→**04**→10→06→01→08→03→07→09→05)

**Build v2-04 UNFENCED P1.** Steps (worklist §4 template):
1. Read worklist §1 (updated), the UNFENCED brief `FRUITBENCH-v2/DESIGNS/04-unfenced-supererogation.md` (incl. applied D-25/26), build guide §§1–9, KB `00-KNOWLEDGEBASE/{01,04,07}.md` (NOTE: KB docs live at `COOKBOOK/00-KNOWLEDGEBASE/`, not under FRUITBENCH — the briefs' path is loose).
2. Write UNFENCED fresh-eyes objections (FO-8a) into `PILOTS/unfenced/` first.
3. EXECUTE the P1 per the brief's final section + build-guide §6 (UNFENCED gate: tier-1 V0 rates >10% for ≥5 fruits). Reuse the THORNS harness spine (`model_adapters.py`, `scorer.py`, `synthetic_reference.py` pattern, `HARNESS/shared/`) — copy + adapt, don't rebuild.
4. **X-1 boundary:** UNFENCED owns discretionary third-party *opportunities with no counter-incentive*; THORNS/COSTLY own active-counter-incentive items. Keep them disjoint.
5. **Program deadline:** the PANELS/ capacity plan (FO-3) is due **before the 3rd build session** — i.e., plan it during or before the design after UNFENCED.

## Standing rules (unchanged)
Scope isolation (FRUITBENCH v1+v2 + published lit only; never read sibling BIBLEBENCH packs). Registry frozen. No deletions (`mv` to RECYCLE-BIN/). New reports get new `YYYYMMDD-` names. Parallel sessions share the git index — stage+commit atomically, check `git log -1` first. Fable-tier work (registry changes, second-pass gate, adjudicating a discovered collision) → hand back to a Fable session.
