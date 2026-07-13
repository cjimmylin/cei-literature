# WCF-Bench — Shadow Judge Bakeoff Design Amendment

**Date:** 2026-07-12

**Status:** Jimmy-approved amendment; no R-number assigned

**Amends:** `20260712n-shadow-judge-bakeoff-design.md` §3.2 and the corresponding
counts in §§5 and 7. Every other clause of the approved design remains unchanged.

## Finding that required the amendment

Implementation-plan inspection found that the immutable MVP transcript contains 309 OPEN
records but only one contested record. Across the compatible immutable pre-MVP evidence,
there are six unique contested `(item_id, sut_slug)` units—not eight. Reaching eight would
require new Gemini/Grok calls, duplicate units, or new SUT responses; all three violate the
approved shadow-study boundaries.

The apparent six-record `20260710-floor-rerun` set contains only three successful responses
(the three DeepSeek records are transport-error records with no usable response). The
mechanical compatible-source rule is therefore:

1. take the three valid final-template records from
   `07-PILOTS/20260710-floor-rerun/transcripts.jsonl`;
2. fill the three missing unique DeepSeek units from
   `07-PILOTS/20260710-r33-3judge/transcripts.jsonl`, whose transcript template hash is the
   same final value; and
3. report Gemini/Grok agreement only where that exact persisted response has the
   corresponding comparator verdict. Never join a comparator verdict from a different
   response text.

This source priority implements Jimmy's approved intent—use all six compatible immutable
contested units without incumbent reruns—while preventing a false cross-run comparator
join.

## Amended real-response sample

| Surface | Units | Source |
|---|---:|---|
| `open_award` | 8 | Corrected immutable MVP OPEN reparse |
| `coherence` | 8 | Corrected immutable MVP OPEN reparse; exactly one numeric fallback axis |
| `disclosure` | 6 | All six compatible immutable contested units under the source-priority rule above |
| `settled_core` | 6 | The same six compatible immutable contested units |

Total = **28 surface units** and **56 new candidate × surface verdicts**. The selection
seed, SHA-256 ordering, deduplication rule, exact candidate slugs, no-incumbent-call rule,
and $1.00 NTE remain unchanged.

## Done-when count correction

Replace the original “all 64 real-response shadow verdicts” ceiling with:

> All **56** amended real-response shadow verdicts are scored or error-recorded, with
> surface denominators reported explicitly as 8/8/6/6 and comparator-specific denominators
> reported wherever persisted incumbent evidence is absent.
