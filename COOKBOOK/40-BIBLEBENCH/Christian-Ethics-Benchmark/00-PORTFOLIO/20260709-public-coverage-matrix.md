# WALKWORTHY Public-Split Coverage Matrix (post-holdout, Session O1)

<!-- WALKWORTHY-CANARY-7f3e2026 -->

**Generated:** 2026-07-09 (Opus Session O1, task 4 — after the holdout split).  
**Scope:** the PUBLIC split only = remaining seed-file items **+** spec-file Fable exemplars 
(exemplars ship inside the design specs, so they count toward published coverage). The private 
`HOLDOUT/` items (gitignored, charter §6.6) are excluded here by design.  
**Charter §3 gate:** every design must cover **≥10 areas with ≥2 public items each**.

## Per-design × area matrix (public = seed + exemplar)

| Design | A | B | C | D | E | F | G | H | I | J | K | L | M | N | ≥2 areas | gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 GOODSAMARITAN | 3 | 5 | 2 | 6 | 5 | 4 | 3 | 3 | 4 | · | · | 3 | 6 | 5 | **12** | ✅ |
| 02 TWOMASTERS | 3 | 3 | 3 | 2 | 2 | 5 | 4 | 2 | 3 | · | 2 | 4 | 3 | 4 | **13** | ✅ |
| 03 QUIETTONGUE | 3 | 3 | 3 | 2 | 3 | 4 | 3 | 3 | 2 | · | · | 3 | 3 | 1 | **11** | ✅ |
| 04 INNERWEIGHT | 2 | 3 | 2 | 4 | 2 | 3 | 3 | 3 | 4 | · | · | 2 | 3 | 2 | **12** | ✅ |
| 05 ORDOAMORIS | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | · | · | 2 | 4 | 3 | **12** | ✅ |
| 06 CROOKEDPATH | 3 | 2 | 2 | 3 | 3 | 3 | 2 | 2 | 2 | · | 3 | 2 | 2 | 2 | **13** | ✅ |
| 07 SEVENTYSEVEN | 2 | 3 | 2 | 3 | 3 | 2 | 3 | 2 | 4 | · | · | 3 | 4 | · | **11** | ✅ |
| 08 VOCATIONFORK | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | · | · | 2 | 4 | 4 | **12** | ✅ |
| 09 DOUBLEEDGE | 3 | 2 | 3 | 2 | 6 | 4 | 2 | 3 | 4 | · | · | 5 | 4 | · | **11** | ✅ |
| 10 STRANGERGATE | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 5 | · | 3 | · | 6 | · | **11** | ✅ |

*(· = area not used by that design; a design need not cover all 14. Bold = count of areas ≥2.)*

## Split & tier summary

| Design | public seed | exemplars | **public total** | holdout | held % | easy% (pub seed) | stratum (pub seed) |
|---|---|---|---|---|---|---|---|
| 01 GOODSAMARITAN | 44 | 5 | **49** | 22 | 33% | 20% | a:42 c:2 |
| 02 TWOMASTERS | 36 | 4 | **40** | 18 | 33% | 22% | a:36 |
| 03 QUIETTONGUE | 29 | 4 | **33** | 15 | 34% | 28% | a:29 |
| 04 INNERWEIGHT | 29 | 4 | **33** | 15 | 34% | 14% | a:29 |
| 05 ORDOAMORIS | 28 | 4 | **32** | 14 | 33% | 29% | a:19 c:9 |
| 06 CROOKEDPATH | 27 | 4 | **31** | 13 | 32% | 11% | a:20 c:7 |
| 07 SEVENTYSEVEN | 27 | 4 | **31** | 13 | 32% | 30% | a:27 |
| 08 VOCATIONFORK | 29 | 4 | **33** | 15 | 34% | 34% | a:28 c:1 |
| 09 DOUBLEEDGE | 34 | 4 | **38** | 17 | 33% | 32% | a:34 |
| 10 STRANGERGATE | 32 | 4 | **36** | 16 | 33% | 31% | a:32 |
| **TOTAL** | **315** | **41** | **356** | **158** | **33.4%** | — | — |

## Gate result & notes

- **Charter §3 gate: PASS for all 10 designs** — every design covers ≥10 areas with ≥2 public items.
- **03 QUIETTONGUE**: area(s) ['N'] at only 1 public item (still 11 areas ≥2 → gate holds). Pre-existing thinness, not caused by the split; candidate for future backfill.

- Public split = **356** items (315 public seeds + 41 spec exemplars); private holdout = **158** items (33.4% of the 473 seed pool, ≥30% charter floor met).
- Holdout stratified by area × difficulty × wave × author_model; both splits preserve the fable-vs-opus author-tier balance (pre-registered discrimination analysis) and the easy:hard ratio.
- Exemplars are counted in public coverage because they live in the git-tracked design specs (published); they were **not** part of the holdout split (specs are immutable design docs of record).
