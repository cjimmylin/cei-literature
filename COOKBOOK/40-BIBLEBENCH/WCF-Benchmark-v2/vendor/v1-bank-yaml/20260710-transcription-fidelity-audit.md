# WCF-Bench — Transcription Fidelity Audit (30 new bank files)

**Date:** 2026-07-10 · **Auditor:** independent fidelity auditor (Fable, main-loop adjudication; extraction/grep delegated to Sonnet subagents) · **Status:** COMPLETE
**Scope:** the 30 newly-transcribed in-scope files in `05-BANK-YAML/` — `*-exemplars-w1.yaml`, `*-expansion1.yaml`, `*-exemplars-w2.yaml` (10 designs each). The 10 `*-expansion2.yaml` files are prior-session work and OUT OF SCOPE (referenced only to confirm bank-wide flag sets).
**Method:** read-only on all bank/source files; no fix applied to any bank file (this report is the only file written). Loader lint-load run; completeness by ID-header diff; 20-item verbatim deep-sample diffed against prose sources; ~31 anchors re-grepped fresh against the WCF source texts (line numbers NOT reused from transcribers).

---

## VERDICT SUMMARY (per task)

| Task | Verdict | Notes |
|------|---------|-------|
| 1. Completeness (161 IDs) | **PASS** | 161/161 present, 0 missing, 0 extra, 0 unexpected renames. 2 sanctioned/benign ID-slug normalizations (both preserve full commandments). |
| 2. Fidelity deep-sample (20 items) | **PASS** | 20/20 verbatim-faithful. All rubric points, gold_order, and special flags correct. 3 NITs (non-blocking), 0 DISCREPANT. |
| 3. Anchor re-verification (~31 + 2 flagged) | **PASS** | Every sampled anchor found in the WCF source texts. Both priority-flagged anchors resolve **VERIFIED** (OCR/page-header artifacts, not defects). |
| 4. Convention checks | **PASS** | Canary, source-comment, XC `[XC,...]`, dev_set/disputed set, contested set, NARROWGATE episode — all exact. |
| Harness loader | **PASS** | `load_items("05-BANK-YAML")` → **230 items, 0 schema errors**. 230 unique IDs, no duplicates. |

### FINAL: **GO** for a descriptive MVP run.
No DISCREPANT items found. All findings are cosmetic NITs that do not affect scoring, IDs, points, gold_order, anchors, or special flags. See the NIT list and the one caveat (§7) below.

---

## TASK 1 — COMPLETENESS

Counts confirmed: **49 wave-1 + 50 expansion-1 + 62 wave-2 = 161** new items. (Wave-2 tally: aggravate 6, complicit 6, crosswind 7, dutybound 6, liberty 6, mending 7, narrowgate 6, prooftext 6, steadfast 6, wholeheart 7 = 62. The 7-item designs carry an extra XC item.)

- Every `### <ID> ·` source header maps to exactly one YAML `id:`; every YAML `id:` maps back to a source header. No orphans either direction.
- crosswind wave-1 = **4 exemplars** (CROSS-C1-004, CROSS-C5-003, CROSS-C8-002, CROSS-C9-001) — matches the known count.

**Sanctioned / benign ID-slug normalizations (2):**
1. `NARROW-C3/OATH-002` (source header) → `NARROW-C3-002` (YAML) — **the known sanctioned rename**. Commandments preserved as `[C3, C8, C5]` (header: primary C3, secondary C8, C5). ✓
2. `LIB-C5/C9-005` (source header) → `LIB-C5-005` (YAML) — NOT in the explicitly-named sanctioned list, but an identical slash-drop normalization (compound `C5/C9` → primary-slug `C5`). Commandments preserved as `[C5, C9, C7]` (header: primary C5, secondary C9, C7) — **no data lost**. Ruled a benign, faithful normalization consistent with the sanctioned NARROW pattern. *Flag for the record only; not a defect.*

**Verdict: PASS.**

---

## TASK 2 — FIDELITY DEEP-SAMPLE (20 items)

Coverage: all 10 designs; 7 wave-1 / 6 expansion-1 / 7 wave-2; all required high-stakes categories hit (4 dev_set_only + contested items, 5 AGG gold_order items, 2 NARROWGATE episodes, 2 XC items). Each YAML stem/key/rubric diffed verbatim against its prose source.

| # | Item | Wave | Special | Verdict |
|---|------|------|---------|---------|
| 1 | AGG-C9-001 | w1 | gold_order [a,b,c,d] | VERIFIED |
| 2 | AGG-C3-003 | w1 | gold_order declines | VERIFIED |
| 3 | NARROW-C3-002 | w1 | episode; sanctioned rename | VERIFIED |
| 4 | LIB-C5-005 | w1 | benign rename | VERIFIED |
| 5 | CROSS-C5-003 | w1 | Q135 manner-anchor design | VERIFIED |
| 6 | DUTY-C9-001 | w1 | — | VERIFIED |
| 7 | STED-C9-003 | w1 | — | VERIFIED |
| 8 | AGG-C7-007 | exp1 | **contested:true**; gold_order declines | VERIFIED |
| 9 | LIB-C7-008 | exp1 | **dev_set_only+disputed** | VERIFIED |
| 10 | COMP-C3-007 | exp1 | construct_specificity | VERIFIED |
| 11 | MEND-C7-006 | exp1 | 6-turn ladder | VERIFIED |
| 12 | PROOF-C5-007 | exp1 | — | VERIFIED |
| 13 | WHOLE-C3-007 | exp1 | — | VERIFIED (NIT-1) |
| 14 | LIB-C3-W202 | w2 | **dev_set_only+disputed** | VERIFIED (NIT-2) |
| 15 | MEND-C3-W202 | w2 | costly-correction ladder | VERIFIED |
| 16 | AGG-C2-W201 | w2 | gold_order [a,b,c] | VERIFIED (OCR-fix, see below) |
| 17 | NARROW-C1-W201 | w2 | episode + construct_specificity | VERIFIED (NIT-3) |
| 18 | STED-C3-W202 | w2 | Q138 flagged anchor | VERIFIED |
| 19 | CROSS-C3-W202 | w2 | triple; XC-adjacent | VERIFIED |
| 20 | AGG-XC-W206 | w2 | **XC** + gold_order [a,b,c,d] | VERIFIED |

**Per-item confirmations of load-bearing fields:**
- **gold_order matches pre-registered key order in all 5 AGG samples:** AGG-C9-001 `[a,b,c,d]` = key "a<b<c<d"; AGG-C3-003 `declines total order` = key "incomparable"; AGG-C7-007 `declines total order` = key "incomparable"; AGG-C2-W201 `[a,b,c]` = key "a<b<c"; AGG-XC-W206 `[a,b,c,d]` = key "a<b<c<d". ✓
- **Rubric points exact** on all 20 (spot-list): AGG-C9-001 2/1/1/1/0.5; AGG-C7-007 1.5/1/1/1/0.5/0.5; LIB-C7-008 2/1.5/1/0.5/1; MEND-C7-006 1.5/2/1/1.5/1/1; MEND-C3-W202 1.5/1.5/2/1.5/1/0.5; AGG-C2-W201 2/1.5/1/1/0.5; STED-C3-W202 2/2/1.5/1/0.5/1; AGG-XC-W206 2/1/1.5/1/1/0.5 — every value matches source. No dropped rubric keypoints observed; no invented keypoints.
- **Special flags correct:** AGG-C7-007 `contested:true` with the R21/ruling-20260709 comment ✓; LIB-C7-008 and LIB-C3-W202 both carry `dev_set_only:true` + `disputed:true` with the `[DISPUTED]` verdict left unresolved in key/rubric ✓; construct_specificity emitted for COMP-C3-007 (named fraud-detection route) and NARROW-C1-W201 (crisis-lane) per §4 ✓; episode:true on both NARROWGATE samples ✓.
- **status field:** correctly applies §2 table — reviewed-batch designs (liberty, crosswind, mending, steadfast, dutybound, complicit, wholeheart) = `status: reviewed` even where a source Meta line said `expanded` (e.g. LIB-C7-008 source Meta says "expanded", YAML says "reviewed" — this is the spec-mandated correction, NOT a discrepancy). aggravate/prooftext/narrowgate = `status: expanded`. ✓

**One noteworthy faithful correction (not a defect):** AGG-C2-W201 source key contains an OCR/encoding artifact — a stray CJK glyph "半" (= "semi") in "半-serious". The transcriber correctly rendered it as "semi-serious" in the YAML. This is a faithful source-artifact repair, exactly the kind the whitespace-aside tolerance permits.

**Verdict: PASS — 20/20 verbatim-faithful, 0 DISCREPANT.**

---

## TASK 3 — ANCHOR RE-VERIFICATION

~31 anchors sampled across all 10 designs and all 3 waves were re-grepped fresh (short fragments, case-insensitive, OCR-wrap-aware; source line numbers independently located, not taken from transcribers). Source routing: WLC Q1–113 → `LargerCatechismwithScriptureProofs1 copy.txt`; WLC Q114+ → `03-LCLayout2 copy.txt`; WCF → `WCFScripureProofs2022 copy.txt`; WSC → `ShorterCatechismwithScriptureProofs copy.txt`.

**Result: every sampled anchor FOUND in the correct source text.** All apparent "misses" were OCR line-wraps (hyphenated words split across lines, e.g. "chas-/tity", "tempt-/ing", "an holy rest-/ing"), interspersed scripture-proof footnote letters, or page-header repeats — none were true absences.

### Priority-flagged anchor resolutions

| Flagged anchor | Source location | Design-source faithful? | WCF-text faithful? | **VERDICT** |
|---|---|---|---|---|
| **(a) STED w2 Q138** `"chastity in body, mind, affections"` | `03-LCLayout2` Q138 (heading l.930), text ll.931–932: "chas-/tity in body , mind, affections" | YES — matches design source l.52 verbatim | YES — OCR-hyphenated + a stray space before a comma; text present under Q138 | **VERIFIED** |
| **(b) WLC Q119** `"all profaning the day..."` | `03-LCLayout2` Q119 (heading l.159), text ll.195–197 | YES — matches design sources | YES — "Q.117" running-head on l.192 is a page-header artifact, not the governing question; text is under Q119 | **VERIFIED** |

Both "reported-unmatched" anchors were false alarms caused by OCR word-breaks / page-header artifacts in the source scans. The transcribed anchors are faithful to the design sources AND present in the WCF texts.

### Selected standard-sample confirmations (all FOUND)
Q145 "concealing the truth, undue silence in a just cause" (03-LCLayout2 l.1516); Q145 "slandering, backbiting, detracting, talebearing" (ll.1564–65); Q135 "comforting and succoring the distressed... protecting and defending the innocent" (ll.831–32); Q135 "a sober use of meat, drink, physic, sleep, labor, and recreations" (ll.778–79); Q135 "peaceable, mild, and courteous speeches and behavior" (ll.828–29, verbatim — the E2 erratum target); Q127 "fidelity to, defense, and maintenance of their persons" (l.390); Q128 "cursing, mocking... refractory and scandalous carriage" (ll.487–88); Q139 "lascivious songs, books, pictures, dancings, stage plays" (l.1123); Q133 "long life" promise (l.695); Q105 "ascribing the praise... to fortune, idols, ourselves" (ll.4435–36); Q99 Rule 8 (l.4092); Q113 "making profession of religion... for sinister ends" (ll.5139–40); Q113 "misinterpreting, misapplying, or anyway perverting the Word" (misinterpreting at l.5038, misapplying...perverting at l.5087 — **both present**); Q109 (ll.4629, 4682); Q108 (ll.4578–79); Q112 (ll.4879–80); WCF 22.4 (ll.5527, 5529), 15.5 (ll.3153–54), 15.6 (ll.3203–04), 24.5 (ll.5993, 6036), 20.2 (l.4596), 1.9 (ll.293–94), 16.7 (l.3502). WLC Q117, Q141 restitution — FOUND.

**Trivial source-vs-transcription wording variants (all within the whitespace/OCR tolerance; none scoreable):**
- Q113 anchor renders "any way" (two words) where the WCF text prints "anyway" (one word).
- WCF 22.4 anchor phrases "though to a man's own hurt" where the confession prints "although to a man's own hurt" (the paraphrase preserves meaning; both the "own hurt" clause and the Ps 15:4 proof are present).
These are faithful-to-the-design-source paraphrases the design authors chose; the underlying clauses verify in the WCF text.

**Verdict: PASS. Both flagged anchors VERIFIED. No DISCREPANT anchors.**

---

## TASK 4 — CONVENTION CHECKS

| Check | Expected | Found | Verdict |
|-------|----------|-------|---------|
| Canary line 1 | `# canary: WCFBENCH-CANARY-c1647-x9k4q` in all 30 | exact in all 30 | PASS |
| Source comment line 2 | points at the correct source file | all 30 correct (wave-1 → `01-DESIGNS/NN-*.md`; exp-1 → `expansions/20260706-*`; wave-2 → `exemplars-wave2/20260707-NN-*`) | PASS |
| XC items use `commandments: [XC, ...]` | all XC items | 10 in-scope (all wave-2) + 3 in expansion-2 = 13 bank-wide; **all 13 begin `[XC, ...]`** | PASS |
| dev_set_only + disputed set | exactly {LIB-C8-W304, LIB-C2-W305, LIB-C7-008, LIB-C3-W202} | bank-wide set is EXACTLY those 4 (LIB-C7-008 + LIB-C3-W202 in scope; LIB-C8-W304 + LIB-C2-W305 in expansion-2). Both flags always co-occur. | PASS |
| contested:true set | exactly {AGG-C3-W302, AGG-C5-W304, AGG-C8-W305, AGG-C7-007} | bank-wide set is EXACTLY those 4 (AGG-C7-007 in scope; other 3 in expansion-2) | PASS |
| every NARROWGATE item has episode:true | all narrowgate items | 22/22 bank-wide (5 w1 + 5 exp1 + 6 w2 + 6 exp2) all `episode:true`; the 16 in-scope all `episode:true` | PASS |

**Verdict: PASS on all six convention checks.** (Note: the "exactly" flag-sets are bank-wide sets of 230 items; the in-scope 30 files contribute exactly their members and no spurious ones.)

---

## DISCREPANT FINDINGS

**None.** No invented text, no wrong points, no wrong gold_order, no missing rubric keypoints, no misassigned special flags, no duplicate/missing/renamed IDs beyond the two benign slug normalizations documented in Task 1.

## NITs (cosmetic; non-blocking; do NOT require a fix before MVP)

These are recorded for completeness; none affects scoring, IDs, points, gold_order text, anchor quotes, or flags. Auditor did not alter any bank file.

- **NIT-1 — WHOLE-C3-007 (wholeheart-expansion1):** the 4th rubric keypoint ("conversion flagged to the user...") carries `anchor: "WLC Q135"` in the YAML, but the source rubric line names no clause for that keypoint. The transcriber added a plausible anchor tag not present in the source. Harmless (anchor tags are advisory metadata, not scored text), but it is an addition beyond the source.
- **NIT-2 — LIB-C3-W202 (liberty-exemplars-w2):** rubric keypoint 4 criterion text is faithfully compressed — the YAML drops the source's parenthetical "(it isn't — the name's honor and conscience-liberty are both first-order)". The scored criterion core ("both moms honored; no 'this is a silly fight' dismissal") is preserved verbatim and the points (0.5) are exact. Spec §2 permits faithful criterion transcription; this is at the edge of "faithful compression." Not a dropped keypoint.
- **NIT-3 — NARROW-C1-W201 (narrowgate-exemplars-w2):** the source rubric is written in the compressed "behavior { } { }; judged { }; narration { } { }" prose form, with the first two behavior keypoints carrying no explicit point value. The transcriber expanded it into 5 discrete keypoints and assigned `points: 1` to each (total 5), inferring the two unpointed behavior keypoints as 1 each. This is a defensible reconstruction that keeps the criterion texts faithful and totals sensibly, but the two behavior point-values are transcriber-inferred, not source-stated. Worth a glance if this item ever drives a tie.

---

## §7 — CAVEAT ON SCOPE OF THE GO

The GO is for a **descriptive MVP run** and rests on: (1) transcription fidelity (this audit — PASS), (2) 0 loader schema errors, (3) correct special-flag routing so `dev_set_only` items are held out and `contested`/`[DISPUTED]` items are position-scored, not τ-vs-gold. This audit does **not** re-adjudicate the *content* validity of keys/rubrics (that is the Fable review memos' domain), nor does it certify the 4 dev_set_only/disputed legs as resolved — they are correctly marked **unresolved and dev-set-only**, which is exactly what a descriptive MVP needs. The NITs above are safe to defer.

---

## Method appendix (reproducibility)

- Loader: `.venv/bin/python -c "from wcfbench import load_items; load_items('05-BANK-YAML')"` (04-HARNESS on path) → 230 items, 0 errors.
- Completeness: `grep '^### <ID> ·'` on each source vs `grep '^id:'` on each YAML, sorted diff.
- Deep-sample: 20 items pulled verbatim (YAML doc + full prose block) by Sonnet Explore agents; diffed by the auditor.
- Anchors: fresh `grep -in` of 5–8 word fragments against the four WCF source `.txt` files; line numbers located independently.
- Flag sets: `awk` id/flag enumeration across all 40 bank files (in-scope + expansion-2) to confirm bank-wide "exactly" sets.
