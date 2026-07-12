<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# WCF-Bench — Session 24 Handoff (F3, PAPER PRE-DRAFT, 2026-07-12)

**Session type:** Jimmy-directed WRITING session per `20260712e-fable-paper-predraft-boot-prompt.md`.
Writing lane only: R1–R68 untouched, no new R-numbers, no code, no live calls, no bank/gold
edits. The judgment ledger remains CLOSED. Codex T1/T2 verified NOT started at session open;
nothing here blocks or touches the Codex lane.

---

## 1. Frozen editorial decisions (Step-1 grill of Jimmy — the paper's constitution)

| # | Decision | Ruling |
|---|----------|--------|
| E1 | Venue | **arXiv-only** standalone preprint; no conference constraints; no anonymization |
| E2 | Headline claim | **Twin co-equal contributions**: the benchmark AND the validity machinery as a reusable template |
| E3 | Intro framing | **Steerability / declared norms** leads (pluralistic-alignment positioning); spine §1 construct disclosure unchanged |
| E4 | Release | **Bank public** (canary + do-not-train) + harness code; **holdout withheld** |
| E5 | Authorship | **`[AUTHORS]` placeholder only** — submission-time decision |
| E6 | Siblings | **No mention at all** — fully standalone, scope isolation absolute |
| E7 | Length | **No cap** — write to completeness, trim later |
| E8 | Layout | One file per section + master outline |

These are recorded in `08-PAPER/00-MASTER-outline.md` §1 and are not to be reopened
without Jimmy.

## 2. What was done

- **`08-PAPER/` created** (new): `00-MASTER-outline.md` (design doc of record: frozen
  decisions, hard constraints, placeholder conventions, per-section briefs, source map,
  review record) + 10 section files, ~18k words total.
- **Process:** Fable wrote the outline/briefs → 6 Opus section-drafters drafted in
  parallel from pinned sources → Fable review (mechanical constraint sweep + targeted
  reads) + an independent Opus verifier.
- **Verification results:** §05 — all 24 MVP figures verbatim from the R42–R53 memos,
  every one labeled DESCRIPTIVE/PRE-GATE at point of use; §06 — ~40 thresholds/formulas/
  rules checked against the prereg (R58–R68), zero deviations; §07 — every placeholder
  maps to a prereg-defined quantity, all 7 gates templated. Zero BLOCKERs. One MINOR
  fixed: §05 per-rep pass probability restored to the memo's 0.75–0.86 range.
- **Constraint sweep:** canary comment in 11/11 files; zero sibling-bench mentions in
  paper text; MVP numbers confined to §05; abstract placeholder keys aligned to §07's
  registry (`G2.best_frontier_mean`; derived `G4.min_kappa` registered in outline §3).
- **Accepted editorial extensions** (writing-lane, not rulings): §08 carries a G4
  `[[IF INCONCLUSIVE-LABELS]]` branch and three G7 states, because the prereg itself
  defines those non-binary outcomes (R63 floor rule; R66 flag-no-veto).

## 3. Open items (paper lane only)

1. **3 `[VERIFY-CITATION]` tags** in `03-related-work.md` (Scherrer et al. arXiv ID;
   Xu et al. 2024 author list; Zhang et al. 2024 author list) — resolve before any release.
2. **Field-key mapping check at T4 fill** (outline §3): the `{{PREREG:*.<field>}}` keys
   are paper-minted structurings of prereg prose quantities; T4's gate-report keys must
   be explicitly mapped against §07's tables before numbers drop in.
3. `[AUTHORS]` / `[REPO-URL]` / `[DATASET-DOI]` — submission-time.
4. **Post-T4 results fill** (mechanical, Opus-appropriate): fill placeholders from the
   gate report, delete losing `[[IF ...]]` branches (never rewrite), then adversarial
   review delivered as an Opus memo → Jimmy (per the standing gate-protocols pattern).
5. Optional pre-T4 Opus polish: citation resolution + prose trim (E7 says no cap now).

## 4. What this session did NOT do

No results minted, no numbers invented, no rulings, no gate changes, no harness/bank
changes, no paid calls, no Codex-lane interference. MVP numbers appear only inside
§05's forensics case study, transcribed and labeled.

## 5. Re-entry pointers

- **Paper lane:** `08-PAPER/00-MASTER-outline.md` (status board + review record) is the
  single entry point; section statuses are FABLE-REVIEWED, awaiting RESULTS-FILLED post-T4.
- **Project:** unchanged — Codex standing boot prompt `20260712-codex-standing-boot-prompt.md`;
  Claude re-entry protocol in `20260712d-wcf-session23-handoff.md` §4.
- Dashboard updated this session (S24 row, Milestone C 30%, §Instructions writing-lane
  paragraph rewritten).

**Canary:** `WCFBENCH-CANARY-c1647-x9k4q` (never re-minted).
