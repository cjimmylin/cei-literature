# G-04 — Reward-Model Values Science

**Stage B** · **Ratings S/T/F: H/H/H** · **Programs: RP-04 HIDDENCURRICULUM** · **Kernel:** Fable 5, 2026-07-07 (FROZEN) · **Body:** Opus draft 2026-07-07

## Statement                       [KERNEL — FROZEN]
Reward models — the narrow gate all RLHF values pass through — encode measurable value dispositions inherited from pretraining that preference data cannot scrub, and the vault's ~19 shallow RM mentions contain none of the 2025–26 auditing, probing, or mechanistic literature.

## Why it matters                  [KERNEL — FROZEN]
If base-model choice silently fixes the values a reward signal teaches (agency vs. communion signatures), then the industry's central value-installation mechanism has an unaudited upstream determinant. Severity H: this is invisible, systematic, and upstream of every preference-data investment. CEI-fit H: profiling RMs requires exactly what CEI has and RM papers lack — validated multi-trait, multi-tradition instruments.

## Evidence                        (corpus + field)
**Corpus baseline:** ~19 RM mentions across the vault, all shallow — none of the 2025–26 value-science line.

**Field:** every arrow in the RLHF value-transmission chain broke under scrutiny (Front B causal story). The pivotal result:
- **RMs inherit value biases from pretraining** (Christian, Kirk, Summerfield et al.; arXiv:2601.20838): Llama-family RMs systematically prefer "agency," Gemma-family "communion," **with identical preference data**; biases are "sticky" against post-training. Base-model choice silently chooses values.
- **EVALUESTEER** (Ghate; arXiv:2510.06370, IN-VAULT): best RMs <75% accurate at matching full value+style profiles vs. >99% on isolated preferences — RMs cannot represent pluralistic value profiles.
- **Auditing hidden objectives** (Anthropic; arXiv:2503.10965): a model trained to exploit 52 known RM errors was detectable by blind audit teams — RM-gaming is learnable as an objective and auditable.
- **Mechanistic toolchain:** SAFER (arXiv:2507.00665), reward-lens (⚠ arXiv:2604.26130 — linear attribution ≠ causal importance), optimal/pessimal-token probing (arXiv:2506.07326, FAccT).

## State of the art
The literature probes RMs **ad hoc**; there is no pre-use value audit for training signals, and RM→policy value transmission is uncharacterized — even its direction is unclear under overoptimization (Front B open problems). CEI's validated banks are exactly the multi-trait, multi-tradition probes this literature lacks. RP-04 sequences it deliberately: **dogfood first** (CEI's own judge pipelines are unaudited consumers of this gap), then run banks as preference-pair probes on ≥3 open RM families to replicate-or-refute the agency/communion inheritance on richer instruments, then attempt a downstream-transmission estimate (RM profile → trained-model bank score). Open pipelines (AI2 Tulu/OLMo) are the only place RM→policy transmission is externally studiable.

## What closing looks like         [KERNEL — FROZEN]
M1 — the RM-values cluster is acquired and a CEI judge-bias dogfood audit exists (RP-04 phase 1). M2 — CEI banks run as preference-pair probes on ≥3 open RM families; the inheritance result replicates (or fails) on richer instruments. M3 — an RM value-profile dataset is public and at least one downstream-transmission estimate (RM profile → trained-model bank score) exists.

## CEI response                    [KERNEL — FROZEN]
RP-04 HIDDENCURRICULUM. The dogfood phase is deliberately first: CEI's own scoring pipelines are unaudited consumers of exactly this gap.

## OPUS-EXPAND checklist           (LIVING)
- [ ] Deep-read Christian et al. 2601.20838 and summarize the agency/communion inheritance method (how they hold preference data constant across base families) into §State of the art — this is the M2 replication target.
- [ ] Note that EVALUESTEER (2510.06370) is already IN-VAULT; deep-read the vault note and extract the <75% value+style accuracy benchmark for reuse as an RP-04 baseline.
- [ ] Inventory open RM families with released weights (Tulu/OLMo/other) to identify the ≥3 needed for M2; add a candidate table.
- [ ] Convert a CEI bank slice into preference-pair format and pilot it on one open RM as a dogfood-audit dry run (RP-04 phase 1).
- [ ] ⚠ Verify reward-lens 2604.26130 before external citation; keep its "linear attribution ≠ causal importance" caveat visible.
- [ ] Check Front B watch-list trigger: any lab published an RM value-audit methodology? If so, run the RP-04 novelty check.

## Sources                         (evidence classes marked)
- RMs Inherit Value Biases (Christian et al.) — arXiv:2601.20838 — **SEARCH-CONFIRMED** — G-04 anchor.
- EVALUESTEER (Ghate) — arXiv:2510.06370 — **VERIFIED** (IN-VAULT: `papers/2025-Ghate-EVALUESTEER...md`).
- Auditing Hidden Objectives (Anthropic) — arXiv:2503.10965 — **SEARCH-CONFIRMED**.
- SAFER (RM mech interp) — arXiv:2507.00665 — **SEARCH-CONFIRMED**.
- Optimal/Pessimal Tokens (RM probing) — arXiv:2506.07326 (FAccT) — **SEARCH-CONFIRMED**.
- Reward-lens — arXiv:2604.26130 — **⚠ UNCONFIRMED** (2604 ID; verify-at-download).
- Corpus baseline (~19 shallow RM mentions) — **VERIFIED** (`../02-gap-atlas.md`).
