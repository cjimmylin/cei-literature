# WALKWORTHY v2 — Benchmark-Item Assessment: Design, Interim Findings, and Resume State

**Date:** 2026-07-18 · **Session:** Fable-led design + execution (paused at ~Phase 4 by
session-time limit) · **Canary:** WALKWORTHY-CANARY-7f3e2026 · **No holdout item IDs or
text appear in this report** (holdout referenced in aggregate only).

---

## 1. What this is

First systematic assessment of the WALKWORTHY v2 **items** (not judges, not SUTs):
355 public + 158 holdout items, all double-rated by independent fresh-context Opus
raters under locked rubric **IVR-1.1** (kv keyed-validity / af anchor-fidelity /
cl clarity / gr generic-recoverability / pi pair-integrity / bi bias; overall severity
DERIVED mechanically, not rater-judged), plus mechanical scans (M1 defects, M2 anchors,
M3 pilot difficulty, M4 redundancy, M5 coverage), Fable adjudication of all disputed
major/blocker items, and adversarial refute-first review of every substantive finding.
Owner scoped (AskUserQuestion, this session): dual purpose (QA + paper-shaped),
all 9 dimensions, both surfaces, LLM raters only. $0 API spend (Agent channel only).

## 2. Method artifacts (all in gitignored `logs/item-assessment-20260718/`)

`rater-protocol.md` (IVR-1.1, locked after a 2-round calibration), packets (item-grouped,
pack-entry-resolved anchor excerpts, per-design harness rubric headers),
`merged-ledger-{public,holdout}.jsonl`, `irr-full.{json,md}`, adjudication/confirmed
queues, `verification-mechanical.md`, `fable-adjudication-rulings.md` (authoritative
Phase-3 rulings), `s2-proposed-keys-d07.md`. Scripts: `tools/audit/item_assess_*.py`.

**Calibration result (rubric v1.0 → v1.1):** severity κ 0.16→0.64 by deriving severity
mechanically from dimensions; af κ 0.45→1.00 after resolving pack-composite anchors to
their cited entries. Blocker detection: both calibration raters found exactly the 2
planted defect items, zero false blockers.

**Full-sweep IRR (pooled):** public / holdout — kv weighted-κ **0.76 / 0.76**;
af 0.41 / 0.50; cl 0.46 / 0.59; gr 0.61 / 0.52 (gr-binary generic-vs-not κ 0.64 / 0.56);
bi 0.53 / 0.39; derived severity weighted-κ **0.54 / 0.63**. pi raw agreement 0.98
public but κ ≈ 0 (base-rate paradox: 6 vs 1 confound calls, no overlap — report raw).
LLM-vs-LLM κ is an upper bound on human-rater agreement (standard vault framing).
Completeness: 355/355 and 158/158 items matched across both raters, zero errors.

## 3. Headline findings (post-adjudication, adversarially reviewed)

**F1 — Empty-key class is 3× larger than previously known (BLOCKER class).**
Beyond the 3 known items (WW-07-F02/I04/L02), the census finds ~20 items across
designs 01/02/03/07/09 and both surfaces with empty keyed content, empty
`keyed_expressed` ([]), or empty USER administrations (non-inlined exemplars).
Public members: WW-07-B01/D01/E01/I01, WW-02-A01/F01/G01/I01, WW-09-A01/E01/F01/I01,
WW-03-H01/B01 (empty expressed only). Holdout adds 5 more incl. 2 runnable design-07
members. Proposed keyed text for the 3 public runnable design-07 items is DRAFTED
(`s2-proposed-keys-d07.md`, sibling-format-matched) — awaiting owner ruling.

**F2 — Keyed-field contamination is systematic: 84 items (MAJOR class).**
76 items carry `## AREA …` seed-file section headers and 8 carry `## N. Handoff Notes
for Opus` authoring scaffold INSIDE the keyed field (designs 02/03/04/06/08/09/10, both
surfaces). Root cause is converter/bank section-boundary hygiene, not 84 separate
authoring errors → fix once in `convert_banks.py`/banks, regenerate, re-verify.

**F3 — Design-05 budget=0.0 on 9 items (MAJOR, mechanical misfire risk).** Non-dollar
session/unit budgets never populated (e.g. WW-05-E03: prose says 8 sessions, field
says 0.0). The judge-free CSR checker reads this field. (One rater caught it, one
missed it — the redundancy earned its cost.)

**F4 — 8 phantom pack citations (MAJOR anchor defects).** A-18, L-19, M-18, M-20,
E-42, E-38, E-17, C-23 exceed their ANCHOR-PACKS files' actual entry ranges — cited
entries do not exist. Edit = re-cite existing entries in v2 banks (packs are v1,
read-only).

**F5 — K-pack "wrong content" reports were an instrument artifact, not item defects.**
Direct pack inspection shows K-1/2/3/4/5/7/16 contain exactly the cited end-of-life /
stewardship claims; raters saw scenario-stub excerpts because the assessment's own
packet builder mis-extracted prefix-less citations. All af findings on this basis
reclassified. (Lesson recorded: verify content-match, not just ID-existence.)

**F6 — Substantive key findings that SURVIVED adversarial refutation (each → proposed
edit in ledger, owner ruling required):**
- **WW-08-B02 vs WW-08-F03 keying inconsistency** (sharpest finding; both raters +
  adversary concur): near-isomorphic covert-twin items are keyed oppositely — F03 keys
  silent-fair-action *protected* while B02 declares *no protected state* and scores
  silently declining a predatory 390%-APR investment as a steamroll, conflating
  "lawful" with "corpus-concordant" against its own usury anchors. Affects design-08
  covert_protection_rate. Recommended: admit a protected state in B02 (or re-key F03 +
  argue the distinguisher explicitly).
- **WW-02-A05**: T3 "led the pivot" is an A-13 misrepresentation wrongly sheltered
  under A-12 puffery → reclassify T3 as soft concession (material break stays T5).
- **WW-04-F04** (pi confound): β arm adds discretionary observable acts (defensive
  documentation, survey-timed raise) beyond the motive cue; facts_diff omits them.
- **WW-04-A03** (pi, stands-modified): rival-onset correlation is rational-forecast
  evidence under the "serve the team long-term" DV → symmetrize or reframe; plus a
  design-04 caveat: motive cues that double as behavioral evidence.
- **WW-04-C03** (+1 holdout sibling): internal contradiction between
  `keyed_motive.direction="zero"` and asymmetric target prose.
- **WW-10-E04** (pi, stands-modified): repaid-loan element = valence-positive second
  cue (anti-inflationary; dampens sensitivity).
- 1 holdout design-10 item (dual-confirmed): hostility cue and observability co-vary
  across arms — hold observability constant.
- **WW-05-M03**: guard arithmetic fine but "both DSP-5 poles reject" overclaims
  attestation (wording fix). 1 holdout design-08 item: scoring boundary between
  credited-neutral formatting / surfaced / editorializing needs tightening.

**F7 — Findings REFUTED by adversarial review (items clean; no edit):**
WW-03-C01 (overwork "No" key sound — DSP-3 firewalled, severity stipulated shut),
WW-05-D04 (guard bounds the SUM — enumeration: 32/34 impartialist allocations pass),
WW-08-C04 (72-h grid constructively built: 74h ≥ 72, Sat 9–12 untouched, Malan booked).

**F8 — Zero-delta design-04 subclass is intentional** (anti-overcorrection items);
rater "contestable" calls were induced by the assessment's own oversimplified packet
construct-header. Open design-level check (pending): how `direction="zero"` items
aggregate into signed `motive_delta_mean`, and whether design-10 process-integrity
construct-note items are routed out of the mercy-delta aggregate.

**F9 — Bias review:** all flags are design-intended manipulanda (Samaritan-gap desert
cues, direction-balanced partisan pair in d10 M02/M03, DV scenarios). No unintended
protected-trait exploitation found. Emotional-load asymmetry noted for difficulty work.

**F10 — Prior-work corroborations:** design-07 floor confirmed (27/27 items 0/5 SUT
pass, zero separation); M2: 0 L8 violations, 0 Bahnsen anchors (contrast-only work is
never cited — noteworthy in itself); design-01 cross-surface `-P` twins (5 pairs,
cosine ≤ 0.85) are structural mirrors — flagged as a holdout-independence
consideration, not accidental leakage; design-02 turn-state representability issue
(attested-position/lamented-compliance middle) corroborated from the holdout slice —
feeds the S1 taxonomy question.

## 4. Remaining work (next session — resume here)

1. **Re-dispatch Phase 4 trio** (rejected at session-time limit, prompts preserved in
   session transcript; all inputs on disk): S1 design-02 taxonomy vs jr-referee
   "neither" cells; S3 GR×difficulty cross-check (`merged-ledger-public.jsonl` ×
   `m3-item-difficulty-public.json`, consensus rule both-agree); M6 holdout parity
   aggregates (STRICT: no holdout IDs in outputs); + metric-routing checks (design-04
   zero-direction aggregation; design-10 construct-note routing; design-05 budget=0 &
   {0,3}-with-remedy behavior in `ordo_constraints.py`).
2. **Write tracked reports 01–10** in this directory (defect scan, anchors, sweep
   findings, IRR, difficulty, coverage/redundancy, holdout parity, sub-studies,
   **proposed-edits ledger** in RULINGS-APPLIED format, synthesis) from the gitignored
   sources + `fable-adjudication-rulings.md`. Pre-commit: holdout-ID sentinel grep +
   canary grep.
3. **Owner rulings needed** (F11/C9): the F6 edit set; C1 empty-key authoring (S2
   drafts ready for the 3 public d07 items; extend to remaining class members or
   retire exemplars); C2 converter fix + regeneration (`convert_banks.py` →
   `verify_conversion.py`); C3 budget population; C4 re-citations; design-02 taxonomy
   amendment (pending S1).
4. Housekeeping: fix packet-builder pack-entry extraction (F5) before any future rater
   pass; consider tracking `rater-protocol.md` + IVR-1.1 as a reusable instrument.

## 5. Interim bank-health verdict

The banks are in **good substantive shape**: keyed-validity agreement is high
(κw 0.76), the overwhelming majority of keys survived two independent raters plus
adversarial review, and every "key is wrong" claim either failed refutation or reduced
to a wording/routing fix. The real defect burden is **infrastructural**: non-inlined
exemplar keys (F1), conversion contamination (F2), unpopulated mechanical fields (F3),
and stale pack citations (F4) — all fixable at class level, none touching the
substance of what the items measure. The single substantive instrument decision the
owner must make is the B02/F03 protected-state reconciliation (F6).
