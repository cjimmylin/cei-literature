# Dataset schema contract (v2, frozen 2026-07-15)

Both `tools/convert_banks.py` (producer) and `walkworthy_inspect/` (consumer) MUST
conform to this contract. Change it only by editing this file first.

## Files

- `datasets/public/design01.jsonl` … `design10.jsonl` — one JSON object per line
- `datasets/holdout/design01.jsonl` … — same shape, holdout items only
- Unit of a line = one **administration** (not one item). Single-administration
  designs emit one line per item.

## Line shape

```json
{
  "id": "WW-01-D01#base",
  "input": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ],
  "target": "<keyed behavior description used by the judge>",
  "metadata": {
    "item_id": "WW-01-D01",
    "design": "01-goodsamaritan",
    "admin": "base",
    "pair_id": null,
    "area": "D",
    "stratum": "a",
    "tier": "core",
    "difficulty": "hard",
    "anchors": ["..."],
    "variables": {},
    "wave": 1,
    "author_model": "fable",
    "runnable": true,
    "review_status": "ported-unreviewed",
    "canary": "WALKWORTHY-CANARY-7f3e2026",
    "keyed": {},
    "multiturn": null
  }
}
```

## Field rules

- `id` = `<item_id>#<admin>`; unique across public+holdout. `admin` values are
  design-specific (e.g. `base`, `say`/`do` (03), motive variants (04), `covert`/`overt`
  (08), `seat_A`/`seat_B` (09), deservingness arms (10), sympathetic-twin arms (01)).
  Single-admin designs use `base`.
- `pair_id`: shared string across sibling administrations/twins that a paired metric
  compares; `null` if unpaired. Metrics group by `pair_id`.
- `keyed`: design-specific scoring key, opaque to the loader — whatever the design's
  rubric needs (keyed action classes, allocation constraints for 05, the 7 criteria
  anchors for 06, matched-quality reference answers for 06/09, keypoints for 03, …).
  The scorer for design NN owns this shape and documents it in `walkworthy_inspect/rubrics.py`.
- `multiturn`: `null` for single-turn designs. For 02/07: an object with the scripted
  ladder — `{"turns": [...], "branch_table": {...}, "classifier_rubric": "..."}` —
  consumed only by the multi-turn solver. The solver for 02/07 owns this shape.
- `review_status`: `ported-unreviewed` at first conversion; the Phase-B review pass
  rewrites bank frontmatter so post-review conversions carry `reviewed-fixed`,
  `reviewed-clean`, or `killed` (with `runnable: false`).
- Non-runnable items (sketch exemplars, killed items) ARE emitted with
  `runnable: false`; the loader filters them out by default. Expected default public
  surface at first conversion: **344 runnable samples' worth of items** (verify
  script asserts per-design counts against the v1 O4 manifest).
- Every metadata object MUST carry the canary verbatim.
