# WALKWORTHY — Paper (a) Skeleton and Source Map

**Date:** 2026-07-24 · **Status:** ASSEMBLY SKELETON (phase-4 ARM 2)
**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content
**Authored by:** phase-4 session, per `20260724b-boot-prompt-phase4-next-arms.md`

---

## 0. Which paper this is

Per `REPORTS/20260717-briefing/06-messaging.md`, two papers are planned:

- **Paper (a)** — benchmark design + (deferred) leaderboard: *WALKWORTHY: A Behavioral
  Benchmark for Christian-Ethics-Aligned Conduct in Language Models, Anchored to a Named
  Ethics Corpus*. Draft abstract exists (06-messaging §3).
- **Paper (b)** — judge-sensitivity / two-referee meta-audit methods note
  (06-messaging §4; ranked the *more* publishable of the two in §2).

**This skeleton assembles paper (a).** Rationale: the phase-4 boot prompt anchors
assembly around the v1.1 validity section
(`REPORTS/20260724-paper-validity-section-draft.md`), and that section is validity
evidence *about the item bank* — it has no home in paper (b). Paper (b) remains viable
and shares sources; its skeleton is future work and mostly already exists as
`REPORTS/20260717-briefing/03-meta-judging.md` + 06-messaging §4.

**Binding claims discipline for every section:** 06-messaging §5 ("What NOT to claim")
items 1–7 apply verbatim — no SUT rankings from pilot data (C9/R1/R3), no
referee-proves-truth claims, no pooled referee agreement without strata, no
religious-authority claims (concordance with the named 15-work registry only), v2 is
parallel-not-canonical, no cross-classifier pooling (C6), no comparative reading of
F2-2c/F3. Additionally: the C9 discontinuity at bank rev 2026-07-24b (validity draft
§X.8 limitation 3) and the design-08 judge-rubric revision line
(`RULINGS-APPLIED-20260724c.md`) fence every pilot-era number quoted anywhere in the
manuscript. Manuscript stays **venue-generic and author-generic** (vault-standing
pattern; no venue/author decision has been made for this project).

---

## 1. Manuscript outline

Readiness legend: **READY** = feeder sources are near-complete prose; **PARTIAL** =
numbers/claims exist but need assembly or reframing; **GAP** = no source exists yet.

### §1 Introduction — PARTIAL
Framing: behavioral evaluation against a *named, specified* corpus rather than generic
harmlessness or "Christianity"; contribution = the instrument + methodology + one
judge-robust capability observation (design-07 floor), leaderboard explicitly deferred.
- Feeds: 06-messaging §3 abstract (near-verbatim seed), §1 headline (for the
  judge-sensitivity motivation), 01-benchmark-card §what-it-measures.
- Pending adjudication: how much of the judge-sensitivity result to *preview* here vs
  cede to paper (b) — recommend one paragraph + citation of (b), no numbers.

### §2 Related work — GAP
Value-laden / religious-values benchmarks, LLM-as-judge reliability literature,
corpus-anchored evaluation. No source file exists.
- Feeds: vault literature (2,043-paper AI-ethics vault; `RELIGIOUS-VALUES/BACKGROUND/`
  extracts are candidate seeds), external search needed.
- Pending: literature sweep — cheapest to do last, once claims are frozen.

### §3 The corpus and the construct — READY (draft target, this session)
The 15-work Protestant-Reformed-dominant registry; anchoring rules (chapter/entry-level
anchors; direct Scripture anchoring disallowed by construction; one work
contrast-only); what "aligned" means (behavioral concordance with the registry, never
theological truth); public/holdout split.
- Feeds: 01-benchmark-card (primary), METHODS/20260715-…-academic-methods.md,
  06-messaging §5 item 4 (framing guardrails).

### §4 The ten behavioral designs — READY (draft target, this session)
One subsection per design (01–10): construct, mechanics (paired administration,
escalation ladders, covert/overt arms, dispute-seat symmetry…), scored surface,
item counts (344 runnable public / 563 admin lines / 158-item holdout at bank rev
2026-07-24b), CV-1 corpus-distinctiveness annotation (04/05/10 candidate-distinct;
stated as annotation, not finding).
- Feeds: 01-benchmark-card (primary), tools/SCHEMA.md, 20260724b-conversion-parity-report.

### §5 Item development, review, and revision history — PARTIAL
Authoring from v1; Phase-B adversarial review (510 reviewed / 105 fixed / 0 removed,
`RULINGS-APPLIED.md`); the 2026-07-18 double-rated item assessment (513 items, IVR-1.1)
summarized *as process* here (results live in §8); PE-1..25 governed disposition and
bank rev 2026-07-24b (`RULINGS-APPLIED-20260724.md`/`-20260724b.md`).
- Pending: compress three rulings ledgers into one process narrative; keep the
  full ledger as supplementary material.

### §6 Harness, scoring, and measurement rules — PARTIAL
Inspect AI port; model-graded scoring + judge-free CSR (design 05); the 2-judge
cross-family rule R4 and its origin (all-9-designs ordering flip under judge swap —
*cited as motivation, no pilot leaderboard numbers*); pinned classifier rule C6;
pre-registered comparison protocol and first-use rule C9.
- Feeds: METHODS academic + operational docs, 20260716-prereg-comparisons-RATIFIED.md,
  20260716-pilot-report.md (ops sections), F8 parser-fix note, F9 retry micro-check.
- Pending adjudication: how much F-ledger detail belongs in-paper vs appendix —
  recommend: R4/C6/C9 in body; F2/F3/F5/F7 one-paragraph summaries + appendix pointers.

### §7 Pilot administration (descriptive) — PARTIAL, C9-sensitive
The 5-SUT, 563-admin pilot reported as *instrument readings*: per-design cells with
intervals, judge-A/B agreement bands (0.21–0.87 by design), design-07 floor saturation
(arc_pass 0.000 all SUTs, 0 exclusions, judge-robust) as the one capability
observation, design-05 CSR. NO rankings, NO composites (messaging §5 item 1).
- Feeds: 20260716-pilot-report.md, 20260716-pilot-design.md (pre-committed claim
  envelope), briefing 02-evaluation.md.
- Pending adjudication: whether §7 survives at all if a full-bank rescore (phase-4
  ARM 1) lands on rev 2026-07-24b first — if it does, pilot becomes a
  development-history subsection and the rescore becomes §7. Flag at assembly time.

### §8 Validity evidence — READY (transplant)
The v1.1 draft transplants near-verbatim: X.1 overview → X.7 post-fix verification.
- Feeds: REPORTS/20260724-paper-validity-section-draft.md (v1.1; adversarially
  reviewed; carries its own source map and two editor-trap comments — strip the
  `<!-- src -->` comments only at final transplant, per owner ruling).

### §9 Limitations and non-claims — READY (merge)
Validity draft §X.8 (five limitations) ∪ messaging §5 (seven non-claims) — merge,
dedupe (C9 appears in both), and add: pilot predates bank rev 2026-07-24b; design-08
judge verdicts pre/post rubric-anchor are separate comparability lines
(RULINGS-APPLIED-20260724c); pushback_rate figures are single-judge-era
(20260724-pushback-rate-first-look.md footer caveat), and per the A′ ruling
(RULINGS-APPLIED-20260724d, same-day) pushback_rate is a reported SECONDARY design-02
metric — per-judge only, never pooled, cross-judge-stability caveat standing — with
break_turn the sole headline; the paper's §7 design-02 cells must follow that surface.

### §10 Future work — READY (compress)
Full-bank C9-clean run (phase-4 ARM 1, separately gated); frontier SUTs on the
design-07 floor; discriminant-validity test to upgrade CV-1 from annotation to
finding; third judge; holdout first-use.
- Feeds: briefing 05-next-steps.md (gap ladder), 06-messaging "what would flesh it
  out" notes per finding.

### Supplementary material — PARTIAL
IVR-1.1 rater protocol (METHODS/20260724-rater-protocol-IVR-1.1.md); PE-1..25 ledger;
per-design agreement tables; consolidated defect ledger (messaging finding #6 asks for
one dated ledger — currently assembled from six reports; build at assembly time).

---

## 2. Section → source map (feeder inventory)

| Section | Primary sources | Secondary |
|---|---|---|
| §1 Intro | 06-messaging §1/§3 | 01-benchmark-card |
| §2 Related | — (GAP) | vault RELIGIOUS-VALUES extracts |
| §3 Corpus/construct | 01-benchmark-card | METHODS academic; messaging §5.4 |
| §4 Ten designs | 01-benchmark-card | tools/SCHEMA.md; 20260724b-parity |
| §5 Item development | RULINGS-APPLIED (×3); item-assessment 00/09/10 | 20260716-polish-items-report |
| §6 Methods/rules | METHODS (×2); prereg-RATIFIED | pilot-report ops; F8/F9 notes |
| §7 Pilot (descriptive) | 20260716-pilot-report; pilot-design | briefing 02-evaluation |
| §8 Validity | 20260724-paper-validity-section-draft (v1.1) | its own source map (8 files) |
| §9 Limitations | validity §X.8; 06-messaging §5 | RULINGS-APPLIED-20260724c; first-look footer |
| §10 Future work | briefing 05-next-steps | 06-messaging flesh-out notes |
| Supp. | IVR-1.1; PE ledger | six-report defect trail |

Paper (b) sources (not consumed here, reserved): briefing 03-meta-judging,
opus/sol-referee results, F2/F2-2c, F3, F5, jr-sampling-precommit.

---

## 3. Next-most-ready section — adjudication

**Chosen: §3 + §4 (corpus/construct + ten designs), drafted this session.**
Rationale: (i) 01-benchmark-card is near-complete feedstock written for exactly this
purpose; (ii) all numbers are stable bank-census facts (344/563/158 at rev
2026-07-24b) — no C9 exposure, no judge-sensitivity caveats to thread; (iii) §8 is
already done (v1.1), and §3–§4 is what §8 structurally leans on (the GR gradient and
defect taxonomy presuppose the reader knows the designs). Runner-up was §6 (methods),
deferred because the F-ledger in-paper-vs-appendix adjudication (above) should be
owner-visible before drafting effort is spent.

Output file: `REPORTS/20260724c-paper-design-section-draft.md` (manuscript-drafter,
opus, from this skeleton's spec; adversarially reviewed before landing — the section
is number-bearing).

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
