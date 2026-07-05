# 20260705 — COOKBOOK Session Handoff (Fable Week, Session 1)

**Session goal (user-approved plan):** build `CEI-Lit-WS/COOKBOOK/` — a values-alignment benchmark
knowledgebase + design portfolio dense enough for Opus to design new publication-grade benchmarks
after Fable access ends (~2026-07-11). Plan file: `~/.claude/plans/please-create-a-folder-zazzy-lake.md`.

## What was completed (all phases 0–6)

| Phase | Deliverable | Status |
|---|---|---|
| 0 | Corpus manifest (620 papers, filter documented) + AI-lab shortlist (61 of 343) | ✅ `30-EVIDENCE/20260705-corpus-manifest.json`, `-ailabs-shortlist.json` |
| 1 | 620 paper evidence cards + 57 lab cards + 4 sub-project digests (181-agent fan-out; Opus for 196 benchmark papers, Sonnet rest) | ✅ validated: 620/620 paper cards (1 accepted newsletter edge case), 57/61 lab (4 impossible — see data issues) |
| 1-gate | 32-card stratified adversarial fidelity audit | ✅ 30/32 clean; 2 FAILs fixed with extract-verified edits (Bang-2022 §9; University-2024 §3) |
| 2 | 13 theme dossiers (42 sub-aggregators + 12 mergers, Opus) | ✅ `30-EVIDENCE/20260705-dossiers/` (2.8–3.9k words each, card-stem cited) |
| 3 | 13 knowledgebase docs — Fable-authored | ✅ `00-KNOWLEDGEBASE/01–13` |
| 4 | 6 literature docs — Opus-drafted from Fable outlines | ✅ `10-LITERATURE/` |
| 5 | Design portfolio — Fable-authored: rationale + 6 full designs + 8 sketches | ✅ `20-DESIGNS/` |
| 6 | README (+ Opus usage guide), verification, this handoff | ✅ |

Counts verified on disk: 13 KB docs / 6 literature docs / 7 design docs + sketches file / 620 + 57
cards / 13 dossiers / 4 digests; ~47k words of synthesis+design deliverables. Total subagent spend
≈ 50M tokens across ~250 agents (2 rate-limit interruptions recovered via workflow resume; zero
work lost).

## What remains (next session queue, in order)

1. **Adversarial review of `20-DESIGNS/` (the deferred Phase 5 gate).** Protocol: one
   adversarial-reviewer (opus) per design ×2 lenses (novelty-vs-965-characterizations using the four
   feature-matrix JSONs; feasibility/validity attack using KB docs 01/03/04). Fable (if available) or
   Opus adjudicates verdicts; revise or promote understudy sketches (S4/S5 → Design 02; S6/S8 →
   Design 01) per the promotion rule in `20-DESIGNS/00`.
2. **Light review pass over `10-LITERATURE/`** (drafters self-verified stems; a spot-check of ~3
   claims/doc against dossiers suffices).
3. **Optional enrichment:** per-sketch expansion files; a `40-OPUS-PLAYBOOK` with worked example
   (run Design 03 DUPLEX pilot P1).
4. **Vault data fixes (upstream, housekeeping tier):** re-download 4 misextracted AI Labs PDFs
   (Anthropic Sabotage_Evaluations_2410.13161, Simple_Probes_2406.09569, Sleeper_Agents_2312.00752 —
   note: stems carry wrong arXiv IDs — and Google DeepMind Gemini_Safety_2403.04312); fix the
   CCAI/Sycophancy filename swap (`Anthropic-Collective_Constitutional_AI...2310.13548` contains the
   Sycophancy paper); 38 papers in the manifest have missing extracts (degraded cards used
   `paper_summary`) — list in `20260705-run-state.json` history / manifest `extract_quality`.

## Key facts for whoever resumes

- **Entry point:** `COOKBOOK/README.md` (includes the how-to-use guide for Opus and all caveats).
- **Recommended build order for designs:** DUPLEX (03) → CRUX (06) → UNMARKED (01); 02/04/05 need
  expert/community partnerships started early.
- **Machine layer is regenerable:** `PYTHON/` scripts (manifest builder, batch generator, card
  validator, card-index/routing) are idempotent and gap-fill safe; workflow scripts persisted under
  the session dir (runs `wf_d783352a-352` evidence fan-out, `wf_3beffcac-796` aggregation) support
  resume.
- **Caveat propagation rule:** always carry the four sub-project disclosures (NormEval F1–F7
  elicited; MP self-administration; RV same-vendor scoring; CG N_eff≈3.4) when citing their
  cross-vendor numbers. Landscape claims are solid.
- **Session interruptions:** two Claude rate-limit hits (~9:50am reset; ~90% of a 5h window at
  session end). All fan-outs are resume-safe; nothing pending except the review passes above.

## File inventory (git-tracked this commit)

`COOKBOOK/` complete tree (README, 00-KNOWLEDGEBASE ×13, 10-LITERATURE ×6, 20-DESIGNS ×7 +
SKETCHES, 30-EVIDENCE machine layer incl. 677 cards + dossiers + digests + manifests, PYTHON ×5,
this handoff).
