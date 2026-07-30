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

## Instrument version stamp (added 2026-07-30, T0-8)

The dataset contract above fixes the *shape* of a line. It does not fix *which* bytes,
*which* scoring code, and *which* model pins were in force when a result was produced.
That second job belongs to the **instrument version stamp**.

### Location and identity

- The stamp lives at the repository root: `INSTRUMENT.json` — one file, one instrument
  version, machine-readable.
- `instrument_id` is the canonical name of an instrument version. Format:
  `WW-v2-<bank_revision>`, e.g. `WW-v2-20260724b`.
- `bank_revision` is the dated revision label of the public bank as cited by run
  reports and rulings memos, e.g. `2026-07-24b`.
- Any result, table, or claim that is compared against another result MUST be
  attributable to an `instrument_id`. Cells carrying different `instrument_id` values
  are different instruments and are not poolable, in the same sense as the C6
  no-cross-classifier-pooling rule in `20260716-prereg-comparisons-RATIFIED.md`.

### Field shape

`INSTRUMENT.json` is a single JSON object with these top-level keys:

| Key | Type | Meaning |
|---|---|---|
| `instrument_id` | string | canonical instrument version name |
| `bank_revision` | string | dated bank revision label |
| `stamped` | string | `YYYY-MM-DD` the stamp was written |
| `stamp_kind` | string | `retrospective` for a stamp applied to an already-frozen tree; `concurrent` for a stamp written at the time the components were frozen |
| `canary` | string | the bank canary, verbatim |
| `surface` | object | public-bank counts: `items`, `runnable`, `admin_lines`, plus a `per_design` map |
| `components` | object | map of repository-relative path → object with `sha256`, `bytes`, `role` |
| `pins` | object | model identities in force, each with a `model` slug and a `source` citation |
| `provenance` | object | pointers to the governing prereg, rulings, and run-report files |
| `holdout` | object | quarantine note; see below |
| `verifier` | string | path of the checker |

Rules on individual keys:

- `components` MUST hash the ten `datasets/public/design01.jsonl` … `design10.jsonl`
  files, the metric module, and the scorer / solver / rubric / dataset-loader modules
  under `walkworthy_inspect/`, together with the per-design task definitions under
  `tasks/`. Compiled `__pycache__` artifacts are never hashed. Hashes are sha256 over
  raw file bytes.
- Every entry under `pins` MUST carry a `source` field naming the file, and where
  applicable the section or symbol, that establishes the pin. A pin with no source is
  a contract violation. Where a pin was set by an explicit run-time override rather
  than by a code default, the entry records both, so that the stamp is never read as
  a claim about what the code would do unattended.
- `holdout` records that `datasets/holdout/` is quarantined: holdout files are NOT
  hashed into the stamp, are NOT counted in `surface`, and are NOT read by the
  checker. The stamp therefore covers the public surface only, and says so.

### The re-stamp rule

**A change to any pinned component requires a NEW `instrument_id`.** Pinned components
are: any hashed file under `components`, any model slug under `pins`, and the bank
surface counts under `surface`.

- Edit a design file, a scorer, a solver, a rubric, a task definition, or the metric
  module → new stamp. Change judge-A, judge-B, or the branch classifier → new stamp.
  Add or remove items → new stamp.
- The semantics of an existing `instrument_id` are never edited in place. An
  `instrument_id` that has been used to label a result is immutable as a claim about
  what that result was produced by.
- Mechanics are the narrow exception. Re-running the stamping process may rewrite
  `INSTRUMENT.json` — to add a newly recognised component, to correct a `source`
  citation, to fix a typo in a note — provided every hash, every count, and every
  model slug is byte-identical to what the file already asserted. If any of those
  three would move, it is not a re-stamp, it is a new instrument version.
- Superseded stamps are preserved rather than discarded, in keeping with the
  report-immutability convention used elsewhere in this repository.

### The checker

`tools/verify_instrument.py` is the checker, and is the only thing that decides whether
a working tree still matches its stamp. It is a standalone stdlib-only command, takes
no arguments, and can be run from any working directory. It recomputes every component
hash, recounts the public surface, and checks the canary, then prints a per-component
PASS or FAIL table. Exit status zero means every check passed; any nonzero exit means
the tree no longer matches its stamp and a new instrument version is owed.

The checker never reads `logs/` and never reads `datasets/holdout/`. It does not import
the eval framework, so it can be run in an environment with no model credentials
present and no network access — verifying a stamp costs nothing and calls no model.
