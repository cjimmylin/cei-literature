# I-10 — Reward Models as Value-Laden Artifacts

**Tier 2** · **Gaps: G-04** · **Programs: RP-04** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## The idea                        [KERNEL — FROZEN]
Reward models inherit value dispositions from their pretrained base that survive identical preference training (family-signature biases: agency vs. communion), cannot represent full pluralistic value profiles, and are now openable with SAE toolchains — the RLHF pipeline's value bottleneck is an auditable artifact nobody audits.

## Key results
- **RMs inherit value biases from pretraining** (Christian, Kirk, Summerfield et al.; arXiv:2601.20838): Llama-family RMs prefer **agency**, Gemma-family prefer **communion**, *with identical preference data*; biases are "sticky" against post-training (Front B).
- **EVALUESTEER** (Ghate; arXiv:2510.06370, **IN-VAULT**): best RMs **<75%** accurate at matching full value+style profiles vs. **>99%** on isolated preferences — RMs cannot represent pluralistic value profiles.
- **Mechanistic toolchain:** SAFER (arXiv:2507.00665), reward-lens (⚠ arXiv:2604.26130 — linear attribution ≠ causal importance), optimal/pessimal-token probing (arXiv:2506.07326, FAccT).
- **Corpus baseline:** ~19 shallow RM mentions, none of this line (`02-gap-atlas.md` G-04).

## Mechanisms & caveats
RP-04 exists because of this idea: CEI's validated banks, administered as **preference-pair probes**, are the instrument upgrade the ad hoc RM literature needs. Judge models are RMs by another name — so the **dogfood audit** (running CEI's own scoring judges through the same science) is RP-04 phase 1. Family-signature biases mean **cross-vendor triangulation is not optional** in any judged CEI study (anti-leakage norms already require it; this is a second, independent reason). And base-model choice is a silent values choice that belongs in CEI's threat-model boilerplate. Caveats: EVALUESTEER is VERIFIED (in-vault); the inheritance result and SAFER/optimal-token toolchain are SEARCH-CONFIRMED; reward-lens is **⚠ UNCONFIRMED** (2604 flagged ID) with its "linear attribution ≠ causal importance" caveat kept visible. LLM-judge results carry the G-09 judge-corruption caveat.

## Implications for CEI practice   [KERNEL — FROZEN]
(a) RP-04 exists because of this idea; CEI banks as preference-pair probes are the instrument upgrade the literature needs. (b) Judge models are RMs by another name — the dogfood audit is the same science applied to CEI's own pipeline. (c) Family-signature biases imply cross-vendor triangulation is not optional in any judged CEI study (anti-leakage norms already require it; this is the second reason). (d) Base-model choice as silent values choice should appear in CEI's threat-model boilerplate.

## Cross-links
- **Gaps:** G-04 (RM values), G-05 (preference-data provenance), G-09 (judge corruption).
- **Ideas:** I-11 (reward hacking — the downstream character risk), I-07 (three-way consistency frame for judge audits).
- **Programs:** RP-04 HIDDENCURRICULUM (dogfood → open-RM audit → downstream transmission).
- **Field-map front:** B (training signal); watch-trigger: any lab publishes an RM value-audit methodology.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read Christian et al. 2601.20838; extract how preference data is held constant across base families (the M2 replication target).
- [ ] Deep-read the in-vault EVALUESTEER note; capture the <75% value+style benchmark as an RP-04 baseline.
- [ ] Convert a CEI bank slice into preference-pair format with polarity metadata and pilot on one open RM (RP-04 phase-1 dogfood dry run).
- [ ] Inventory open RM families (Tulu/OLMo/Qwen-derived) to identify the ≥3 needed for the family-vs-recipe variance decomposition (H2).
- [ ] Draft the "base-model choice = silent values choice" line for CEI threat-model boilerplate (implication (d)).
- [ ] ⚠ Verify reward-lens 2604.26130 before external citation; keep the linear-attribution caveat visible.

## Sources                         (evidence classes marked)
- RMs Inherit Value Biases (Christian et al.) — arXiv:2601.20838 — **SEARCH-CONFIRMED** — G-04 anchor.
- EVALUESTEER (Ghate) — arXiv:2510.06370 — **VERIFIED** (IN-VAULT: `papers/2025-Ghate-EVALUESTEER...md`).
- SAFER (RM mech interp) — arXiv:2507.00665 — **SEARCH-CONFIRMED**.
- Optimal/Pessimal Tokens (RM probing) — arXiv:2506.07326 (FAccT) — **SEARCH-CONFIRMED**.
- Reward-lens — arXiv:2604.26130 — **⚠ UNCONFIRMED** (2604 flagged ID).
- Corpus baseline (~19 shallow RM mentions) — **VERIFIED** (`../02-gap-atlas.md` G-04).
