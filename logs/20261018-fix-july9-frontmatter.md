# 20261018 — Restore frontmatter values damaged by the 2026-07-09 bulk rewrite

**Script:** `PYTHON/fix_july9_frontmatter.py` (dry run by default; `--apply` to write; safe to re-run)
**Damaging commit:** `5caae838f` — "INNOVATION Cycle-1 CLOSED …" (2026-07-09)
**Restored from:** its parent `296fdf0b6`

---

## What happened

Commit `5caae838f` rewrote the frontmatter of all 2,385 papers that existed at the time
(the 52 acquisitions it added are separate). Comparing every frontmatter field before and
after the commit, with quote style and escaping ignored, these values changed:

| Field | Damage | Papers | Restored |
|-------|--------|--------|----------|
| `ethics_overall` | every value replaced with `No` (field is a 0–100 integer since 2026-03-13) | 2,385 | yes |
| `year` | replaced with `2025` (each previously matched its `YYYY-` filename prefix) | 1,270 | yes |
| `abstract` | truncated, mostly at the first embedded `\"` (e.g. 1,416 → 191 chars) | 40 | yes |
| `authors` | block lists emptied (`authors: `) | 4 | yes |
| `short_title` | blanked | 1 | yes |
| `title` | folded wrongly, last word lost | 1 | yes |
| `tags` | 17 P1 anchor block lists emptied — deliberate, see `INNOVATION/20260710-cycle1-close-handoff.md` | 17 | no |
| `local_pdf` / `pdf_extract` | stray `"N/A"` continuation line removed (cleanup) | 12 / 7 | no |

All other differences were formatting only (quote styles). No note bodies changed.
`validate_all_papers.py` reported 0 errors before and after the damage: it accepts legacy
`Yes`/`No` in `ethics_overall` and empty fields.

Likely cause: the acquisition templates in `INNOVATION/40-BUILDS/` default to
`ethics_overall: No` and a 2025 year, which matches the values stamped onto the legacy
papers. The script that applied them to existing records was not found in the committed files.

**Cause found (added later on 2026-10-18):** the library test suite. `.agent/tests/` overrode
`config.PAPERS_DIR` with a temp dir, but the `.agent/lib` modules had copied the path at import,
so the tests ran on the real `papers/`. `test_batch_update_papers` sets
`{"year": "2025", "ethics_overall": "No"}` on every paper it finds, through the
`parse_frontmatter` → `rebuild_frontmatter` round-trip, which strips quotes and cuts values at
the first embedded `"`. Running the suite in a session's local checkout reproduced the same
pattern (2,437 `ethics_overall` and 1,299 `year` lines changed, quote styles rewritten,
abstracts truncated); the uncommitted changes were reverted with `git checkout -- papers/`
and nothing was committed. The tests are now isolated (see
`_OPERATING-SYSTEM/Learnings/learnings-log.md`, 2026-10-18 root-cause entry).

## Method

For each paper present at `296fdf0b6`, `5caae838f` and the working tree, and for each field above
marked "yes":

- skip if the value is equal at `296fdf0b6` and `5caae838f` (ignoring quoting) — not damaged;
- skip if the current text differs from what `5caae838f` wrote — edited since (none were);
- otherwise write back the `296fdf0b6` value:
  - `year`, `ethics_overall`, `abstract`: the exact original line;
  - `authors`: the original names as the corpus-standard `authors: "A; B; C"` line
    (multi-item block lists fail `validate_all_papers.py`, per the July handoff note);
  - `title`, `short_title`, and one abstract that was a multi-line plain scalar: the original
    text as one valid quoted line.

Edits replace single whole lines inside the frontmatter with `re.subn(count=1, re.MULTILINE)`
(no parse → rebuild round-trip). The script asserts that no other line changes. No files were
moved or deleted.

## Results

| | Count |
|---|---|
| Papers changed | 2,385 |
| `ethics_overall` restored | 2,385 |
| `year` restored | 1,270 |
| `abstract` restored | 40 |
| `authors` restored | 4 |
| `title` / `short_title` restored | 1 / 1 |
| Skipped (edited since) | 0 |

Most common restorations: `ethics_overall` No → 0 (1,194), No → 100 (476), No → 15 (168);
`year` 2025 → 2024 (635), → 2023 (228), → 2022 (106), → 2026 (101).

Checks after applying:

- `git diff` touches only the six fields above (3,697 lines across 2,385 files; 2 files show as
  binary in git because their bodies already contained NUL bytes — checked with `git diff --text`).
- Every restored value equals the `296fdf0b6` value (quoting ignored): 46 / 46 for the
  rebuilt fields, exact lines for the rest.
- Re-running the script reports everything as already restored and changes nothing.
- `validate_all_papers.py`: 2,445 / 2,445 valid, 0 errors.
- Every paper's `year` now equals its filename year prefix (previously 1,270 mismatches).

## Not changed (follow-ups)

- 17 papers added on or after 2026-07-09 (Anthropic/OpenAI documents and other INNOVATION
  acquisitions) still carry template `Yes`/`No` in `ethics_overall`; they were never scored.
  Scoring them needs `ethics_scoring.score_paper()`, not this restore.
- `validate_all_papers.py` could reject non-integer values in the 0–100 score fields so that
  this kind of overwrite fails validation.
