# WALKWORTHY v2 Item Assessment — Report 02: Corpus-Anchor Verification (M2)

Canary: WALKWORTHY-CANARY-7f3e2026

**Generated:** 2026-07-18
**Assessment context:** This is part of the 2026-07-18 WALKWORTHY v2 item assessment
(355 public + 158 holdout items). The overview of assessment state and findings lives in
sibling report `20260718-00-assessment-state-and-findings.md`. This report covers
Module M2 (corpus-anchor verification) plus Check 4 of the mechanical verification pass
(pack-entry fidelity).

**Sources (verbatim, no recomputation):**
- `logs/item-assessment-20260718/m2-summary.md`
- `logs/item-assessment-20260718/m2-anchors-public.json` (resolve counts)
- `logs/item-assessment-20260718/verification-mechanical.md` (Check 4)

**Holdout handling:** No holdout item IDs and no holdout item text appear in this report.
Holdout is referenced only in aggregate.

---

## 1. M2 Method

Each item carries one or more **anchors** — references into the source corpus of
Christian-ethics reference works. M2 verifies anchors in three stages:

1. **Alias resolution.** Each anchor's leading alias (e.g. `POW`, `RAE`, a quoted book
   short-title) is matched against the known alias → corpus-book map. Anchors that begin
   with `-- area-X pack` or shorthand pack keys (`K-1`, `K-2`) are **structural
   multi-book pack references** with no single target file; these are flagged `PACK-REF`
   and are **by-design, not defects**. Aliases matched to a corpus book are `RESOLVED`;
   aliases not in the known map are `UNRESOLVED` (a defect).
2. **Locator search.** For a resolved anchor, M2 searches the target book text for the
   quoted title/locator, yielding `FOUND`, `FUZZY-FOUND`, `NO-LOCATOR`, or `NOT-FOUND`.
3. **Pack-entry resolution.** For pack-style shorthand citations (letter-N claim keys),
   the cited claim entry is resolved against the relevant area anchor-pack file (see §5).

---

## 2. Status Counts — Both Surfaces (Aggregate)

### 2.1 Public surface

- Total items: 575
- Total anchor instances (may repeat across items): 1799

**Resolve status (alias → book file):**

| Status | Count | Notes |
|--------|-------|-------|
| PACK-REF | 540 | structural multi-book pack ref (not a defect) |
| RESOLVED | 1257 | alias matched to a corpus book |
| UNRESOLVED | 2 | DEFECT — alias not in known map |

**Locator status:**

| Status | Count |
|--------|-------|
| FOUND | 1100 |
| FUZZY-FOUND | 43 |
| NO-LOCATOR | 109 |
| NOT-FOUND | 547 |

### 2.2 Holdout surface (aggregate only)

- Total items: 260
- Total anchor instances: 839

**Resolve status:**

| Status | Count | Notes |
|--------|-------|-------|
| PACK-REF | 250 | structural multi-book pack ref (not a defect) |
| RESOLVED | 588 | alias matched to a corpus book |
| UNRESOLVED | 1 | DEFECT — alias not in known map |

**Locator status:**

| Status | Count |
|--------|-------|
| FOUND | 549 |
| FUZZY-FOUND | 26 |
| NO-LOCATOR | 9 |
| NOT-FOUND | 255 |

---

## 3. Unresolvable Anchors (the DEFECT class)

Across both surfaces there are **3 unresolvable anchor instances**, comprising **2 unique
anchor strings**:

- **Public (2 instances, both on `WW-04-F01`):** the anchor string
  `RAE decision-model stakeholder step` resolves `UNRESOLVED`. This single anchor string
  appears twice in `WW-04-F01`'s anchor block (accounting for the public `UNRESOLVED`
  count of 2), so the M2 summary reports it as **1 unique** unresolved public anchor
  string. The alias `RAE` is in the known map, but the appended locator phrase does not
  resolve to a decision-model / stakeholder-step passage in the mapped Rae works.
- **Holdout (1 instance, aggregate only):** 1 unresolved anchor string on 1 holdout item
  (ID withheld). Per the M2 holdout summary it is a Rae `Moral Choices` chapter locator
  that does not resolve. Reported in aggregate only.

All three instances are locator/alias-map gaps on Rae references; none is a broken
pack-reference. `PACK-REF` anchors (540 public / 250 holdout) are by-design and are not
counted as defects.

---

## 4. L8 Scan and Bahnsen Inventory

### 4.1 L8 scan — 0 violations

The L8 flag detects **bare Scripture citations used as an anchor work-part** (a Scripture
reference standing in as if it were a corpus-book anchor). Result on both surfaces:

| Surface | L8 flags |
|---------|----------|
| Public | 0 |
| Holdout | 0 |

**None detected on either surface.** No item substitutes a bare Scripture citation for a
corpus-book anchor.

### 4.2 Bahnsen inventory — 0 citations (notable)

The Bahnsen inventory counts anchors that cite Bahnsen's work. Result on both surfaces:

| Surface | Bahnsen citations |
|---------|-------------------|
| Public | 0 |
| Holdout | 0 |

**This is a notable fact and is stated explicitly:** Bahnsen (theonomy) is a
**contrast-only** author in this benchmark — the corpus uses it as a foil/contrast
position for named tradition splits — and it is **never cited as a positive anchor** on
either surface. The zero here is therefore a design-consistency confirmation, not a
coverage gap: the item bank does not lean on the contrast-only author as source authority.

---

## 5. Pack-Entry Fidelity (Verification Check 4)

### 5.1 Phantom pack citations — 8 confirmed missing

Eight pack citations flagged by raters as "not found in pack file" were re-verified
mechanically, restricting the search to the claims section (§2) of each area pack and
applying all four extraction patterns. All eight confirm as **`PACK-FILE-MISSING-ENTRY`**
— the cited claim number exceeds the maximum claim number present in that pack file:

| citation | pack file | max claim in pack | numbering scheme | verdict |
|----------|-----------|-------------------|------------------|---------|
| A-18 | area-A-truth-telling-speech.md | 14 | plain-N | PACK-FILE-MISSING-ENTRY |
| L-19 | area-L-civil-authority.md | 17 | plain-N | PACK-FILE-MISSING-ENTRY |
| M-18 | area-M-church-community-hospitality.md | 16 | C-prefix | PACK-FILE-MISSING-ENTRY |
| M-20 | area-M-church-community-hospitality.md | 16 | C-prefix | PACK-FILE-MISSING-ENTRY |
| E-42 | area-E-enemy-love-forgiveness.md | 15 | C-prefix | PACK-FILE-MISSING-ENTRY |
| E-38 | area-E-enemy-love-forgiveness.md | 15 | C-prefix | PACK-FILE-MISSING-ENTRY |
| E-17 | area-E-enemy-love-forgiveness.md | 15 | C-prefix | PACK-FILE-MISSING-ENTRY |
| C-23 | area-C-work-vocation-rest.md | 17 | plain-N | PACK-FILE-MISSING-ENTRY |

Each cited number is strictly greater than the pack's maximum claim number (e.g. `A-18`
against a pack whose claims run to A-14; `E-42` against a pack running to E-15). These are
genuine phantom citations: the anchor points at a claim entry that does not exist in the
corresponding area pack.

### 5.2 Corrected K-pack verdict — cited K-entries verified correct

An earlier reporting pass in this assessment flagged the area-K citations
(`WW-06-K03`, `WW-06-K04`, `WW-10-K03`, `WW-10-K05`) as citing "wrong content." **That
earlier verdict is corrected.** On mechanical re-verification, every cited K-entry
resolves to the correct claims-section entry at the pack level:

| item | cited K-entries | verdict |
|------|-----------------|---------|
| WW-06-K03 | K-3, K-16, K-7 | BANK-CITATION-OK |
| WW-06-K04 | K-1, K-2, K-3, K-16 | BANK-CITATION-OK |
| WW-10-K03 | K-1, K-2, K-4, K-5 | BANK-CITATION-OK |
| WW-10-K05 | K-1, K-2, K-4, K-5 | BANK-CITATION-OK |

The area-K pack numbers its claims section (§2) as `**K-N (tag).**` consecutively K-1
through K-22, while the scenario-motifs section (§6) uses a separate plain-integer
numbering (1..18). These are **separate numbering spaces**: `K-3` unambiguously resolves
to claim K-3 in §2, not scenario 3 in §6. A cross-check of the packet-builder regex
(`_extract_pack_entry` in `item_assess_build_packets.py`) confirmed **no scenario-index
cross-section ambiguity** — for letter-N areas like K, the letter-N pattern fires first,
and the claims section precedes the scenario section in every pack file.

**The lesson (stated for the record):** the earlier "wrong content" K-pack reports were a
**packet-builder extraction artifact of this assessment**, not a defect in the item bank.
The builder that assembled the review packets extracted the wrong span when it verified
by ID existence rather than by content match. The corrected rule is: **verify
content-match, not ID-existence.** When the packet builder was made to compare the cited
claim's actual text against the pack entry (rather than merely confirming an entry with
that ID exists somewhere in the file), all four K citations verified correct.

---

## 6. Summary

- Anchor resolution is clean: **2 public + 1 holdout** unresolvable anchor instances
  (2 unique strings, all Rae locator/alias-map gaps); `PACK-REF` anchors (540 public /
  250 holdout) are by-design.
- **L8 = 0** on both surfaces (no bare-Scripture-as-anchor); **Bahnsen = 0** on both
  surfaces (contrast-only author never cited as anchor — a notable design-consistency
  fact).
- **8 phantom pack citations** confirmed as `PACK-FILE-MISSING-ENTRY` (cited number >
  pack max): A-18, L-19, M-18, M-20, E-42, E-38, E-17, C-23.
- **K-pack verdict corrected:** the 4 cited K-item citations are `BANK-CITATION-OK` at
  the pack level; the earlier "wrong content" reports were a packet-builder extraction
  artifact of this assessment. Verify content-match, not ID-existence.

Canary: WALKWORTHY-CANARY-7f3e2026
