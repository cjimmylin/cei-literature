# WALKWORTHY v2 Item Assessment — Report 06: Coverage (M5) & Redundancy (M4)

Canary: WALKWORTHY-CANARY-7f3e2026

**Generated:** 2026-07-18
**Assessment context:** This is part of the 2026-07-18 WALKWORTHY v2 item assessment
(355 public + 158 holdout items). The overview of assessment state and findings lives in
sibling report `20260718-00-assessment-state-and-findings.md`. This report covers
Module M5 (coverage cross-tabs) and Module M4 (redundancy audit).

**Sources (verbatim, no recomputation):**
- `logs/item-assessment-20260718/m5-coverage-public.json`
- `logs/item-assessment-20260718/m1-m5-summary.md`
- `logs/item-assessment-20260718/m4-summary.md`

**Holdout handling:** No holdout item IDs and no holdout item text appear. Holdout is
referenced only in aggregate; where a public item mirrors a holdout item, the holdout
side is referred to only as "its holdout twin."

---

## 1. M5 Coverage — Public Surface

### 1.1 Totals

| Metric | Count |
|--------|-------|
| Total lines | 575 |
| Total items (unique item_id) | 355 |
| Total runnable items | 344 |
| Total runnable admin-lines | 563 |
| Stratum-c items (all designs) | 25 |

### 1.2 Per-design: items / lines / runnable lines

| Design | Items | Lines | Runnable lines |
|--------|-------|-------|----------------|
| 01 | 49 | 49 | 49 |
| 02 | 39 | 76 | 72 |
| 03 | 33 | 66 | 66 |
| 04 | 33 | 60 | 60 |
| 05 | 32 | 32 | 32 |
| 06 | 31 | 31 | 31 |
| 07 | 31 | 31 | 27 |
| 08 | 33 | 66 | 66 |
| 09 | 38 | 92 | 88 |
| 10 | 36 | 72 | 72 |

Designs 02/03/04/08/09/10 carry more lines than items (paired admin lines per item);
designs 01/05/06/07 are one line per item. Runnable-line shortfalls appear in 02 (72 of
76), 07 (27 of 31), and 09 (88 of 92) — the non-runnable rows are the base-exemplar /
empty-keyed admin lines documented in report `20260718-01`.

### 1.3 Area × design spread (public, line counts)

| Design | A | B | C | D | E | F | G | H | I | K | L | M | N |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | 3 | 5 | 2 | 6 | 5 | 4 | 3 | 3 | 4 | 0 | 3 | 6 | 5 |
| 02 | 5 | 6 | 6 | 4 | 4 | 9 | 7 | 4 | 5 | 4 | 8 | 6 | 8 |
| 03 | 6 | 6 | 6 | 4 | 6 | 8 | 6 | 6 | 4 | 0 | 6 | 6 | 2 |
| 04 | 4 | 5 | 4 | 7 | 3 | 6 | 6 | 5 | 7 | 0 | 4 | 5 | 4 |
| 05 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 0 | 2 | 4 | 3 |
| 06 | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 2 |
| 07 | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 4 | 0 | 3 | 4 | 0 |
| 08 | 4 | 6 | 6 | 4 | 6 | 6 | 4 | 4 | 6 | 0 | 4 | 8 | 8 |
| 09 | 7 | 5 | 7 | 5 | 15 | 7 | 6 | 8 | 9 | 0 | 13 | 10 | 0 |
| 10 | 6 | 6 | 4 | 6 | 6 | 6 | 6 | 4 | 10 | 6 | 0 | 12 | 0 |

**Area-coverage notes.** Area K is sparse: it appears only in designs 02, 06, and 10 (4,
3, 6 lines respectively) and is absent from the other seven designs. Area N is absent from
designs 07, 09, and 10. Areas E, L, and M are heaviest in design 09 (15, 13, 10 lines).

### 1.4 Stratum, tier, and difficulty distributions (public)

**Stratum distribution.** All designs are dominated by stratum-a; stratum-c is present in
four designs only:

| Design | stratum-a | stratum-c |
|--------|-----------|-----------|
| 01 | 47 | 2 |
| 05 | 21 | 11 |
| 06 | 21 | 10 |
| 08 | 64 | 2 |
| all others | (all stratum-a) | 0 |

**Total stratum-c public items = 25** (2 + 11 + 10 + 2), concentrated in designs 05 and
06.

**Tier distribution.** Every public item across all ten designs is tier `core`
(575 lines, all `core`). There is no non-core tier on the public surface.

**Difficulty distribution (easy / hard, line counts):**

| Design | easy | hard |
|--------|------|------|
| 01 | 10 | 39 |
| 02 | 16 | 60 |
| 03 | 16 | 50 |
| 04 | 8 | 52 |
| 05 | 8 | 24 |
| 06 | 3 | 28 |
| 07 | 8 | 23 |
| 08 | 20 | 46 |
| 09 | 27 | 65 |
| 10 | 20 | 52 |

Every design skews hard; design 06 is the most hard-weighted (3 easy vs 28 hard).

---

## 2. M4 Redundancy Audit

### 2.1 Method

M4 computes pairwise text similarity (word cosine and character cosine) within each
design, on each surface, and across surfaces (public × holdout). A pair is **flagged**
when its word cosine **> 0.75 AND above that design's p99**. Top-5 pairs per design are
always shown regardless of threshold.

**Summary counts (verbatim):**

| Surface | Total flagged pairs |
|---------|---------------------|
| Public within-design | 11 |
| Holdout within-design | 1 |
| Cross-surface (public × holdout) | 5 |

### 2.2 Public within-design — 11 flagged pairs

The 11 public flags fall in two designs: **8 in design-01** and **3 in design-09**.

**design-01 (8 flagged) — intentional paired `-P` variants.** Design-01 items ship in
base / `-P` paired form; each base item and its `-P` twin are near-duplicates by
construction (the `-P` variant is an intended paraphrase/perturbation of the same
scenario). The high-cosine pairs are these intended paired variants — they are **not**
accidental redundancy. The top pairs (all base ↔ `-P` twins):

| Pair | Word cos | Char cos |
|------|----------|----------|
| WW-01-F02 ↔ WW-01-F02-P | 0.8782 | 0.9371 |
| WW-01-N02 ↔ WW-01-N02-P | 0.8347 | 0.8952 |
| WW-01-I02 ↔ WW-01-I02-P | 0.8340 | 0.9137 |
| WW-01-G02 ↔ WW-01-G02-P | 0.8276 | 0.9083 |
| WW-01-A05 ↔ WW-01-A05-P | 0.8264 | 0.9027 |

(Design-01 max within-design word cosine = 0.8782; flagged = 8. The top 5 are shown; all
flagged design-01 pairs are of the same base ↔ `-P` intended-paired-variant form.)

**design-09 (3 flagged) — rubric-boilerplate cluster.** The three design-09 flags are a
mutual triangle among base-exemplar admin lines whose keyed field carries the shared
externalized-rubric boilerplate (`[09-doubleedge ... keyed behavior not inlined ...
walkworthy_inspect/rubrics.py]`):

| Pair | Word cos | Char cos |
|------|----------|----------|
| WW-09-E01 ↔ WW-09-I01 | 0.8625 | 0.9221 |
| WW-09-E01 ↔ WW-09-A01 | 0.8625 | 0.9221 |
| WW-09-I01 ↔ WW-09-A01 | 0.8625 | 0.9221 |

The high similarity here is **rubric-boilerplate**, not content overlap: these are the
design-09 base exemplars (the empty-user-role rows from report `20260718-01`) that share
identical externalized-rubric text. Design-07 shows the same boilerplate signature in its
top-5 (WW-07-E01/B01/I01/D01 mutual word cosine 0.7696) but **none of design-07's pairs
clear its p99** (p99 = 0.7696), so design-07 contributes **0** flags — the boilerplate
cluster there sits exactly at the distribution edge rather than above it.

### 2.3 Holdout within-design — 1 flagged pair (aggregate)

**1 flagged holdout within-design pair** in design-01 (max word cosine 0.7933). Per the
holdout protocol, the IDs are not reproduced; it is one holdout design-01 base ↔ `-P`
paired variant, structurally the same intended-pair pattern as the public design-01
flags.

### 2.4 Cross-surface (public × holdout) — 5 flagged pairs, all design-01

The 5 cross-surface flags are all in design-01 and are **public↔holdout structural
mirrors**: a public design-01 item and its holdout counterpart share the design-01
scaffold (objective-first obedience framing) closely enough to clear the threshold, with
word cosine up to **0.8458**.

The public-side item of the top cross-surface pair is nameable — **WW-01-B01** — but the
holdout-side ID is **not** named; it is referred to only as **its holdout twin**. Per the
M4 cross-surface table, design-01 shows **5 flagged** cross-surface pairs (word cosine
range up to 0.8458), each a public design-01 item paired with its holdout twin.

**Holdout-independence consideration (flagged).** These 5 design-01 cross-surface
mirrors mean that a public design-01 item and its holdout twin are structurally very
close (cosine up to 0.85). This is a **holdout-independence consideration**: if a SUT
author or evaluator can inspect the public design-01 items, the closely-mirrored holdout
design-01 items are partially inferable. The similarity is driven by the shared design-01
objective-first scaffold rather than by leaked specifics, but the near-twin structure
warrants review before treating the design-01 holdout slice as fully independent of the
public slice. No other design shows any cross-surface flag (all other designs: 0 flagged).

---

## 3. Summary

- **M5 coverage:** 355 public items / 575 lines / 344 runnable items; 25 stratum-c items
  (concentrated in designs 05 and 06); all items tier `core`; every design skews hard.
  Area K is sparse (designs 02/06/10 only); areas E/L/M peak in design 09.
- **M4 redundancy:** 11 public within-design flags (8 design-01 intended `-P` paired
  variants + 3 design-09 rubric-boilerplate); 1 holdout within-design flag (aggregate);
  **5 cross-surface design-01 public↔holdout mirrors** (cosine up to 0.85, public-side
  WW-01-B01 nameable, holdout side referred to only as its holdout twin).
- **Flagged for follow-up:** the 5 design-01 cross-surface near-twins as a
  holdout-independence consideration.

Canary: WALKWORTHY-CANARY-7f3e2026
