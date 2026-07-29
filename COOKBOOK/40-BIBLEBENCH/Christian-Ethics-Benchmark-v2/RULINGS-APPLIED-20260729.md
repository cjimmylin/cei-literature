# RULINGS APPLIED — 2026-07-29 · §2 citation sweep and its two claim narrowings

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Spend:** $0 model spend. Web search and retrieval only; no runs, no bank/rubric/metric/code
change to the instrument. **Holdout untouched and still quarantined.**
**Supersedes nothing.** This ruling closes an item that phase 6 and phase 7 both carried
forward; it does not reopen or amend any prior ruling.

---

## 0 Session context — the boot prompt was stale

This session was launched against `20260725c-boot-prompt-phase6-paper-assembly.md`. That
prompt had **already been fully executed** (commit `e05322b4f`), as had its unlisted
successor `20260725d-boot-prompt-phase7-claims-adjudication.md` (commit `4be01c5f2`, plus
README state commit `12f2baae7`). Both of the prompt's adjudication questions (Q1 assembly
target, Q2 §7 disposition) were ruled in `RULINGS-APPLIED-20260725b.md`, and the three
escalated claims-validity questions in `RULINGS-APPLIED-20260725c.md`.

Re-executing it would have re-adjudicated settled questions and written a duplicate dated
ruling into an append-only ledger whose convention is *newest dated file is authoritative* —
a silent corruption rather than a loud failure. State was verified against git and the
working tree before any action was taken. **Boot prompts are snapshots of intent, not state;
verify before executing one.**

## 1 Correction to the carried gap count

Phase 7 recorded **10** open `[CITATION NEEDED]` markers. The true count was **8** genuine
bracketed gaps — 2 in paper (a) §2.2/§2.3, 6 in paper (b) §2.2/§2.4. The other two hits were
boilerplate prose in the injected bibliography preamble that *describes* the marker
convention (`assemble.py`), not gaps. Counting a convention-describing sentence as an
instance of the thing it describes is the same class of error as the U+2212-minus
false-negative and the `402`-inside-`47,402` false-positive already on file: **match on
structure, not on substring.**

## 2 RULING 1 — the §2 external citation sweep is AUTHORIZED (owner, this session)

The sweep was proposed at phase 6 and phase 7 and never authorized. It is now authorized and
executed. Six of the eight gaps closed with **pure citation insertion — no claim changed**:

| Gap | Closed with |
|---|---|
| (b) chance-corrected agreement foundations | Cohen (1960); Krippendorff (2019); Landis and Koch (1977) |
| (b) κ prevalence / base-rate paradox | Feinstein and Cicchetti (1990); Cicchetti and Feinstein (1990) |
| (b) generalizability theory ancestry of the §4 decomposition | Cronbach, Gleser, Nanda and Rajaratnam (1972); Brennan (2001) |
| (b) panels / juries of smaller judges | Verga et al. (2024) |
| (b) annotator-substitution economics | Gilardi, Alizadeh and Kubli (2023) |
| (a) minimal-pair / counterfactual twinning | Kaushik, Hovy and Lipton (2020); Gardner et al. (2020) |

Full bibliographic records, with retrieval dates, are in new **"External sources"** ledger
tables inside `parts/pa-04-related-work.md` and `parts/pb-04-related-work.md`. None of these
works is vault-resident; every one was retrieved and inspected directly.

**A bonus the sweep produced.** Landis and Koch advanced their interpretive bands as
acknowledged personal judgement, not on evidentiary grounds. Paper (b) §2.2 argues precisely
that a respectable coefficient is not a licence to proceed, so citing the canonical bands
*together with their unevidenced basis* strengthens the section's own argument rather than
merely filling a hole. This is now in the prose.

## 3 RULING 2 — both claim-bearing closures ADOPTED as scoped (owner, this session)

Two gaps could not be closed without changing what a paper claims, which the phase-6
fix-versus-escalate line reserves for the owner. Both were put with a recommendation and
**both were adopted as scoped. Both narrowings make the papers claim LESS, not more.**

**(a) The Christian-corpus novelty claim.** Previously: "no prior behavioral benchmark
anchors conduct to a named Christian-ethics corpus in this way." A counterexample search
found no counterexample but did find *neighbours*, so the old phrasing was broader than the
evidence. Now narrowed and grounded: Christian-anchored evaluation demonstrably exists — the
closest neighbour is the Gospel Coalition's AI Christian Benchmark (Sapp et al., 2025) — and
the claim is restricted to its defensible form: no prior **behavioral** benchmark anchored to
a **named corpus of Christian ethicists** rather than to a creed or confession. The
distinction is now stated on two explicit axes (doctrinal assent versus conduct under
pressure; creed versus named ethicist corpus) rather than asserted as bare novelty.

**(b) The cost-barrier sentence.** No published accounting of what it costs to *audit* a
judge, as distinct from what it costs to run one, could be located. The sentence now cites
the adjacent cost evidence (Verga's panel figure; Gilardi's per-annotation figure) and states
explicitly that the meta-evaluation cost barrier is grounded in **this study's own design
constraints, not in a citation** — "they are ours, not the literature's." The spend figures
are quoted with their true precision: $0 for both referee arms, and roughly $11 for the
full-bank run **of which $8.53 was metered exactly and the second-judge rescore is an
estimate** (not the bare "$11.23", which reads as exact when part of it is estimated).

## 4 Inspected and REJECTED — do not cite, do not rediscover

The counterexample search surfaced *"What the Models Already Know: 67 Billion Tokens of
Christian Moral Reasoning in the Pretraining Corpus"* — attributed to Tim Hwang, "Institute
for a Christian Machine Intelligence", ICMI Working Paper No. 6, dated 2026-04-03, at
`icmi-proceedings.com`. It was fetched and inspected: **no DOI, no ISSN, no editorial board,
no programme committee, no peer-review attestation, no companion papers indexed**, and the
domain is unrelated to the ACM conference whose acronym it borrows.

**The delivery mechanism is the part worth recording.** Its central quantitative claim —
that Christian moral reasoning in pretraining data exceeds every other tradition by an order
of magnitude — arrived **pre-summarised as established fact by the search layer**, with no
hedge about the venue. Phase 6's anti-fabrication control was *"give the drafter no web
access, so it cannot cite what it has not opened."* That control does not cover a web-enabled
main loop: **retrieval does not confer provenance, and a search summary launders an unvetted
claim into declarative prose.** The check that caught it was fetching the page and asking
what publication apparatus is actually present — the same "verify the document, not the
filename" rule already on file from the vault citation defects.

**Standing rule added:** a source discovered through search is not citable until its
publication apparatus has been inspected directly. Rejections get recorded, so a later
session cannot read the absence of a note as evidence the source was never checked.

## 5 New vault citation defect found — extends the standing ledger

Adds to `20260725-citation-metadata-findings.md` and the auto-memory note on vault citation
defects. **Not remediated here — vault citation remediation is a separate scope.**

- **`CEI-Lit-WS/papers/2025-Coalition-The Gospel Coalition AI Christian Benchmark.md`** has a
  populated metadata record (its `first_author` is Casey Sapp, so the filename token
  "Coalition" is a byline mismatch of the known class) **but its PDF extract is an empty
  shell**: `PDF Extracts/2025/2025-Coalition-…md` reports `pages: 0` with a blank content
  block. Its `external_pdf` field points at a `core.ac.uk` download ID that is not plausibly
  a ministry report. **The vault copy cannot support a citation**; the paper (a) ledger
  therefore cites the live report and records the empty extract explicitly.
- Independently re-confirmed two mismatches the phase-6 ledger already documents — the
  *Religious Bias Landscape* extract filed under "Hamid" is by Abrar, Oeshy, Kabir and
  Ananiadou; the *Measuring Spiritual Values* extract filed under "Buyl" is by Liu et al.
  The phase-6 drafter's ledger was right on both counts.

## 6 Verification performed

- Manuscripts rebuilt from parts via `assemble.py`. **Both remain generated files — edit the
  parts, never the manuscript.** Paper (a) 18,151 → **18,686 words**; paper (b) 14,426 →
  **15,190 words**.
- `lint_claims.py`: **16 files, 0 blockers**, 5 warnings. The only new warning is the Gilardi
  work's *actual title* in a ledger table, which trips the ranking-language heuristic; the
  remainder pre-date this session.
- **Test suite 33/33 pass** (project venv, py3.14).
- **Zero bracketed `[CITATION NEEDED]` markers remain** in any part file or either manuscript.
- Canary present in both manuscripts.
- Provenance statements corrected where the sweep made them false: the injected bibliography
  preamble in `assemble.py` claimed every entry was verified against a *vault* file, which
  ceased to be true; it now names both channels. The manuscripts README's "not done at v0.1"
  note is updated to closed.

## 7 Carried forward UNCHANGED — not reopened by this ruling

- **Holdout: recommended NOT to spend.** Quarantined, untouched by this session. Its blind
  first use remains a one-shot asset.
  **Update, same day —** this recommendation was **elevated to a ruling** by a concurrent
  session in `RULINGS-APPLIED-20260729b.md` (commit `636dc9950`): the quarantine is now
  **RATIFIED**, with release conditioned on a repaired instrument version demonstrating
  discrimination. That file cites *this* §7 as the recommendation it elevates, so this
  paragraph is left standing as written rather than rewritten — the cross-reference must
  continue to resolve. **The holdout question is CLOSED; do not re-raise it as open.**
- **`pushback_rate` CLOSED** (A′ affirmed, `RULINGS-APPLIED-20260725.md`).
- **RULING 1 and RULING 2 of `RULINGS-APPLIED-20260725c.md`** (df-proportional reference
  line, descriptive only; Kendall τ alongside binary flips) remain in force and untouched.
- **Classifier pinned at `gpt-4.1-nano`**; the v-next re-pin still bundles with the d02
  taxonomy revision as one instrument version (C6).
- **Bank revision 2026-07-24b.** No instrument change in this session.
- **Instrument-repair queue** unchanged: d02 taxonomy, d08 boundary, d07 needs harder
  systems, d03 may be judge-defined.
- **Supplementary material still unassembled**; no venue or authorship decision made.

## 8 FLAGGED, NOT FIXED — pre-existing staleness in the manuscripts README

Outside this session's authorized scope; surfaced for a later decision. Two statements in
`REPORTS/20260725-manuscripts/README.md` pre-date `RULINGS-APPLIED-20260725c.md` and now
contradict it:

1. Its **"Framing correction — do not undo it"** section still states the claim as *"the
   judges disagree about the ordering in every judged design."* RULING 1 replaced that with
   *"models differ on most designs; on a minority the judges clearly disagree about the
   ordering; on the rest the systems are too tightly spaced for either judge to resolve."*
   (The prohibition on "the judge dominates" in that same section **does** survive.)
2. Its evidence-division note says paper (a) §9 **"cites the 8-of-8 interaction"** — but
   "non-zero in 8 of 8" was **WITHDRAWN as evidential** by RULING 1.

The manuscript prose itself is correct on both points; only this working README is stale. It
is nonetheless the operating instruction for whoever rebuilds next, and as written it directs
them to restore a withdrawn claim.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
