# 20260705b — COOKBOOK Handoff for Next Session (post-commit state)

**Read this first, then `COOKBOOK/README.md`.** This supersedes-and-extends
`20260705-cookbook-session-handoff.md` (the phase-by-phase build record — still accurate; do not edit it).

## State at end of 2026-07-05

- **COOKBOOK complete and pushed** (commits `2b5ecb41b` + this one, repo `cjimmylin/cei-literature`,
  branch `main`): 13 knowledgebase docs (`00-KNOWLEDGEBASE/`), 6 literature docs (`10-LITERATURE/`),
  6 full benchmark designs + 8 sketches (`20-DESIGNS/`), full evidence layer (620 paper cards +
  57 lab cards, 13 dossiers, 4 digests in `30-EVIDENCE/`), pipeline scripts (`PYTHON/`).
- **NEW since the build session: `40-BIBLEBENCH/`** — Jimmy's scripture-passage benchmark research
  (added 2026-07-05 afternoon, external deep-research reports from OpenAI + GDM per passage):
  - `CORINTHLOVE/` (1 Corinthians 13 — love/agape), `TENCOMMANDMENTS/`, `SERMONMOUNT/`,
    `FRUITBENCH/` (Galatians 5 fruit-of-the-spirit — most developed: has its own `DESIGNS/` with a
    portfolio doc + per-virtue designs 00–05, e.g. makrothumia/long-fuse patience, chara/even-keel).
  - Not yet integrated with the cookbook proper.

## Next-session queue (in priority order)

1. **Adversarial review gate over `20-DESIGNS/` (deferred Phase 5 gate).** Protocol: per design,
   2 adversarial-reviewer agents (opus) with distinct lenses — (a) novelty vs the 965 characterized
   benchmarks (check against the four feature-matrix JSONs listed in the digests' §8 file pointers),
   (b) feasibility/validity attack using KB docs 01/03/04. Adjudicate verdicts; revise; if a design
   fails, promote its understudy sketch (S4/S5→02, S6/S8→01; rule in `20-DESIGNS/00`).
2. **Integrate `40-BIBLEBENCH/` with the cookbook**: audit the four passage packs against the Seven
   Laws (`00-KNOWLEDGEBASE/01`) and the religious-values methods doc (`10`) + INTRA design (`04`) —
   especially: knowledge/reasoning/values three-layer separation, denominational conditioning
   (Catholic/Orthodox/Protestant readings of the same passage), saturation defenses, and the
   T2-recipe discriminative layer. Produce a review memo per pack + a reconciled
   FRUITBENCH-vs-DUPLEX/INTRA overlap map (fruit-of-the-spirit virtues ≈ dispositional-stability
   constructs → reuse DUPLEX's I-concord machinery).
3. **Light spot-check of `10-LITERATURE/`** (~3 claims/doc vs dossiers).
4. **Pilot kickoff**: Design 03 DUPLEX P1 (generator + 300 items) is sized for Opus sessions.
5. **Vault data fixes (housekeeper tier)**: 4 misextracted AI-lab PDFs + the CCAI/Sycophancy card
   filename swap (details in `20260705-cookbook-session-handoff.md` §"vault data fixes").

## Standing cautions

- Carry the four sub-project disclosures when citing cross-vendor numbers (NormEval F1–F7 elicited;
  MP self-administration; RV same-vendor scoring; CG N_eff≈3.4). Landscape claims are solid.
- Card page refs ±1–2 pp. Never recompute digest statistics — copy verbatim.
- Pre-existing untracked backlog in the repo (CULTURAL-GLOBAL/, MORAL-PSYCH/, NORM-ETHICS/,
  RELIGIOUS-VALUES/ working files, DASHBOARDS/, logs/) was deliberately NOT committed with COOKBOOK —
  it belongs to prior sub-project sessions; commit it from its own context if desired.
- Safety rules are hook-enforced (no rm; new dated reports, never edits; YAML lint). Delegation
  tiering per `~/.claude/CLAUDE.md` + `.claude/FABLE-WEEK.md` (Fable window ends ~2026-07-11).
