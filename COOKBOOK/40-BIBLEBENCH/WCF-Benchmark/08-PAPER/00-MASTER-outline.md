<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench Paper — Master Outline & Section Briefs

**Created:** 2026-07-12 (Fable paper pre-draft session, per `20260712e-fable-paper-predraft-boot-prompt.md`)
**Lane:** WRITING ONLY. R1–R68 are settled; nothing here mints rulings, results, or numbers.
**Assembly order = file order.** One file per section; this file is the design doc of record.

---

## 1. Frozen editorial decisions (grill of 2026-07-12 — do not reopen without Jimmy)

| # | Decision | Ruling |
|---|----------|--------|
| E1 | Venue | **arXiv-only**, standalone preprint; no conference format constraints; no anonymization |
| E2 | Headline claim | **Twin co-equal contributions**: (1) WCF-Bench, a 230-item construct-disclosed benchmark; (2) the validity machinery (judge qualification, artifact forensics, pre-registered gates) as a reusable template |
| E3 | Intro framing | **Steerability / declared norms** leads — pluralistic-alignment positioning; construct disclosure per spine §1 is mandatory and unchanged ("accord with the Westminster Standards", NOT "is ethical") |
| E4 | Release posture | **Bank public** (canary embedded, do-not-train notice) + harness code public; **holdout/refresh set withheld** for contamination auditing |
| E5 | Authorship | **`[AUTHORS]` placeholder only**; decided at submission time. AI-assistance disclosure paragraph still required in §10 |
| E6 | Sibling benches | **No mention at all.** Fully standalone. No "broader program" sentence. Scope isolation absolute |
| E7 | Length | **No cap** — write to completeness; trim in a later pass |
| E8 | Layout | One file per section + this master outline |

## 2. Hard constraints (binding on every drafter and every later edit)

- **NO results, NO invented numbers.** Gated-run data does not exist yet.
- MVP-run numbers may appear ONLY inside §05's forensics case study, ONLY labeled
  **DESCRIPTIVE / PRE-GATE**, and only if transcribed from a memo (never recomputed).
- Every results table/figure template carries its validity labels: **R34.4** (OPEN scorer =
  single-family judge label) and **R52** (PROOF = judge-assisted upgrade disclosure).
- R-numbers may be cited as internal protocol references, but all prose must be readable
  with zero memo access.
- Citations in §03 must be real, verified papers; anything unverified is tagged
  `[VERIFY-CITATION]` and resolved before any release.
- Canary comment `<!-- WCFBENCH-CANARY-c1647-x9k4q -->` at the top of every file in
  `08-PAPER/`. Never re-mint.
- No sibling-bench names, no cross-references outside `WCF-Benchmark/`.

## 3. Placeholder & label conventions

- Result placeholders: `{{PREREG:<gate-or-artifact>.<field>}}` — the `<field>` names MUST
  be taken verbatim from `20260712c-fable-gated-run-prereg-memo.md` (R60–R66 gate
  computations and the R59 run design), so T4 outputs drop in mechanically.
  Examples: `{{PREREG:G1.r_squared}}`, `{{PREREG:G3.pairs_significant}}`,
  `{{PREREG:league.per_sut_composite}}`, `{{PREREG:P4.flip_rate}}`.
- Editorial placeholders: `[AUTHORS]`, `[DATE]`, `[REPO-URL]`, `[DATASET-DOI]`.
- Validity-label footnotes are part of the table *template*, not added later:
  every OPEN-track column footnoted "single-judge-family label (see §5.x)";
  every PROOF column footnoted "judge-assisted extraction (see §5.x)".
- Branch text in §08 is marked `[[IF G# PASS]]` / `[[IF G# FAIL]]` — both branches
  pre-written; the losing branch is deleted after T4, not rewritten. ACCEPTED EXTENSION
  (Fable review 2026-07-12): G4 additionally carries an `[[IF INCONCLUSIVE-LABELS]]`
  branch and G7 carries three states (pass / redundancy-flag / low-reliability), because
  the prereg itself defines those non-binary outcomes (R63 floor rule; R66 flag-no-veto).
- **Field-key mapping caveat:** the prereg names quantities in prose, not machine keys;
  the `{{PREREG:*.<field>}}` tokens are this paper's structuring of those quantities
  (registry = §07's tables). When T4's gate report lands, its keys must be mapped/checked
  against §07 before fill — a mechanical step, but it must be done explicitly.
- Derived summary keys used ONLY in the abstract: `G4.min_kappa` = minimum over the §07
  G4 table's judge×surface κ cells. Any new derived key must be registered here.

## 4. Section files, status, and briefs

| File | Section | Status |
|------|---------|--------|
| 01-abstract-skeleton.md | Abstract | FABLE-REVIEWED |
| 02-introduction.md | Introduction | FABLE-REVIEWED |
| 03-related-work.md | Related work | FABLE-REVIEWED (3 citations independently verified by Codex, 2026-07-12) |
| 04-benchmark-design.md | Benchmark design | FABLE-REVIEWED (counts grep-verified vs bank) |
| 05-methods-validity.md | Validity methodology | FABLE-REVIEWED (24 figures memo-verified) |
| 06-experimental-setup.md | Experimental setup (pre-registered) | FABLE-REVIEWED (~40 thresholds prereg-verified) |
| 07-results-scaffold.md | Results (SCAFFOLD) | FABLE-REVIEWED (all 7 gates templated) |
| 08-discussion-scaffold.md | Discussion (SCAFFOLD, branch-structured) | FABLE-REVIEWED (17+ branches) |
| 09-limitations.md | Limitations | FABLE-REVIEWED |
| 10-ethics-release.md | Ethics & release statement | FABLE-REVIEWED |

**Review record (2026-07-12, this session):** independent Opus verifier cross-checked
§05 against the R42–R53 memos (24 figures, all verbatim + labeled), §06 against the
prereg (~40 items, zero deviations), §07 placeholder-by-placeholder (all quantities
prereg-defined, thresholds match). One MINOR fixed: §05's per-rep pass probability
restored from point-estimate 0.86 to the memo's 0.75–0.86 range. Abstract placeholder
keys aligned to §07's registry (`G2.best_frontier_mean`; new derived `G4.min_kappa`).
Mechanical sweep: canary in 11/11 files; zero sibling-bench mentions in paper text;
MVP numbers confined to §05.

*(Status values: BRIEF → DRAFTED → FABLE-REVIEWED → RESULTS-FILLED → FINAL.)*

### §01 Abstract skeleton
Twin-claim structure mirroring E2: one sentence steerability motivation → construct
disclosure → benchmark description (230 items, 10 method-major designs, two tracks) →
methodology claim (qualification/forensics/prereg as template) → bracketed result slots
(`{{PREREG:...}}`) → release sentence (E4). Keep ≤ 250 words when slots are filled.

### §02 Introduction
Order: (1) steerability problem — models are asked to represent specified normative
frameworks; can accord with a *fully specified* framework be measured? (2) why a
confessional standard is a strong test case (fixed, internally coherent, extensively
documented, centuries-stable — no moving target, no annotator-majority proxy);
(3) construct disclosure, verbatim register of spine §1; (4) twin contributions list;
(5) validity-first stance: pre-registered gates decide whether *any* league table is
released; (6) paper map. Sources: spine §1, prereg preamble, master-spec framing.

### §03 Related work
Four strands: (a) pluralistic alignment / steerability toward declared value systems;
(b) values-and-ethics benchmarks for LLMs (and religious-values evaluation where
published); (c) LLM-as-judge validity — qualification, agreement, bias, artifact
literature; (d) benchmark contamination + canary/do-not-train defenses. Each strand ends
with the differentiation sentence (what WCF-Bench does that the strand does not).
Real citations only; `[VERIFY-CITATION]` tags where uncertain. No sibling benches (E6).

### §04 Benchmark design
From spine + master spec + anchor registry + `01-DESIGNS/` + `05-BANK-YAML/`: construct
definition and anchor registry; the 230-item bank; the 10 method-major designs (one
subsection each: what the method isolates, item counts, scorer kind); tier ladder
(settled-core floor vs contested tiers, contested-item scoring per the 2026-07-09
ruling); the two tracks; scorer kinds incl. OPEN and PROOF (with their validity labels
introduced here, details in §05); perturbation battery (P3/P4/P6 scope per prereg);
contamination defenses (canary, holdout withholding, paraphrase battery). Include a
bank-composition table template (counts only — these exist and are citable from the
frozen bank, NOT results).

### §05 Validity methodology (the methodology contribution)
The R-chain rendered as methods, in four movements:
1. **Judge qualification** — K=8 battery design, re-qualification triggers, escalation
   ladder, drop rules (gpt-4o-mini drop as the worked example of the protocol firing),
   2-family coherence panel, format-bridge attempt and its closure.
2. **Parser-artifact forensics as a first-class validity activity** — the FIRST-match
   `SCORE:` parse bug and the willingness-veto false-fire (judges' mandatory verbatim
   quote of a refusal fixture tripping the veto): how "model disagreement" decomposed
   into harness artifacts; counterfactual re-parse as the diagnostic; the zero-OPEN
   outcome reversal. THE flagship case study — MVP numbers allowed here, DESCRIPTIVE/
   PRE-GATE labeled.
3. **Adjudication protocol** — binding rulings ledger, provisional packets, ratification
   separation (compute vs adjudicate vs ratify), living pre-registration.
4. **Pre-registered release gates** — G1–G7 in one paragraph each (what each gate
   catches), labels-gate-RELEASE-not-execution principle, silent-deviation-voids rule.
Sources: memos `20260710-fable-judge-calibration-adjudication-memo.md`,
`20260710e/h`, `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46),
`20260712-fable-ratification-memo.md` (R47–R53), prereg §gates.

### §06 Experimental setup (pre-registered)
A faithful transcription — not paraphrase — of the prereg: 10-SUT roster formula
(anti-leakage family exclusions; frontier = top-5 by capability PC1), judge panel of
record, seed 1647, perturbation scope, $300 NTE + truncation ladder, and the full
G1–G7 computation definitions with their frozen thresholds. State explicitly that this
section was written BEFORE the run, from the pre-registration, and that deviations void
gates. Source: `20260712c-fable-gated-run-prereg-memo.md` (R58–R68) only.

### §07 Results scaffold
No prose conclusions. Templates only: gate report table (G1–G7 × threshold ×
`{{PREREG:G#.*}}` × PASS/FAIL slot); league table template (per-SUT, per-design,
composite; validity-label footnotes per §3 conventions); perturbation flip-rate table;
judge-agreement table; cost/compliance table ($ vs NTE, truncation events). Every
placeholder keyed to a prereg field name. A header warning: "SCAFFOLD — contains no
data; populated only from the T4 gate report."

### §08 Discussion scaffold (branch-structured)
For each gate: `[[IF PASS]]` and `[[IF FAIL]]` interpretation paragraphs, pre-written
now so no interpretation is invented post-hoc. Plus results-independent discussion
that can be fully written: what the artifact-forensics episode implies for LLM-judge
benchmarks generally; why release-gating beats publish-and-caveat; generalization of
the method to other declared-norm corpora WITHOUT naming any (E6).

### §09 Limitations
From the record, results-independent: single-judge-family OPEN labeling (R34.4 ladder
closed after real fails); PROOF judge-assisted upgrade disclosure (R52); construct
scope (one confession, English, text-only); contested-tier interpretation bounds;
contamination residual despite defenses; MVP-vs-gated distinction (MVP was
harness-shakedown, not measurement); G6 human-rater dependency; cost ceiling as a
completeness bound.

### §10 Ethics & release statement
E4 release posture; canary + do-not-train policy; holdout withholding rationale;
construct disclosure repeated in plain terms (benchmark scores accord with a declared
confessional standard — a high score is not a claim of moral goodness, a low score not
an indictment); no human subjects in the results-independent portion, G6 rater protocol
described conditionally; AI-assistance disclosure paragraph (models used in harness
construction, adjudication support, and drafting; all binding decisions human-ratified);
`[AUTHORS]`, `[REPO-URL]`, `[DATASET-DOI]` placeholders.

## 5. Source-of-truth map

| Topic | File(s) (relative to `WCF-Benchmark/`) |
|-------|----------------------------------------|
| Construct & disclosure | `00-OVERVIEW/20260706-shared-spine.md` §1 |
| Bank / designs / tiers | `00-OVERVIEW/20260706-master-spec.md`, `00-OVERVIEW/20260706-westminster-anchor-registry.md`, `01-DESIGNS/`, `05-BANK-YAML/` |
| Contested-item scoring | `20260709-contested-item-scoring-ruling.md` |
| Judge qualification & drops | `20260710-fable-judge-calibration-adjudication-memo.md`, `20260710e-fable-postfix-adjudication-memo.md`, `20260710h-fable-probe-stability-adjudication-memo.md`, `20260710-fable-grok-ratification-floor-divergence-memo.md` |
| MVP forensics & panel health | `20260711-fable-mvp-disagreement-adjudication-memo.md` (R42–R46) |
| Parser-artifact reversal | `20260712-fable-ratification-memo.md` (R47–R53) |
| EPISODE registry rulings | `20260712-fable-episode-registry-review-memo.md` (R54–R57) |
| Pre-registration (setup + gates) | `20260712c-fable-gated-run-prereg-memo.md` (R58–R68) |

## 6. Process

Drafted by Opus section-drafters from these briefs (2026-07-12), Fable-reviewed in the
same session. Later sessions: results fill (post-T4, mechanical), adversarial review,
trim, arXiv packaging. Per E7 no length cap at this stage.
