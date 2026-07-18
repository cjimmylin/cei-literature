# WALKWORTHY v2 — Consolidation Manifest (2026-07-17)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content

Purpose: record the one-time consolidation that made this folder
(`Christian-Ethics-Benchmark-v2/`) the single, self-contained home for the WALKWORTHY v2
project. This is the front-door index for "where did that intermediate go?"

## What was already in place (no move needed)

The folder was already the correct, self-contained destination: all benchmark code
(`tasks/`, `tools/`, `walkworthy_inspect/`, `tests/`), data (`banks/`, `datasets/`),
run logs (`logs/`, gitignored), reports (`REPORTS/`, `REVIEWS/`, `METHODS/`, root `.md`
rulings), and the briefing deck (`REPORTS/20260717-briefing/deck/`) live here. The
**canonical referee-audit outputs** were already archived in-folder at
`logs/jr-referee-20260716/` (`referee-agreement.json`, `referee-agreement-sol.json`,
`opus-verdicts.jsonl`, `sol-verdicts.jsonl`, `prompts-0{2,6,7}.jsonl`,
`sample-manifest.jsonl`, `manifest-meta.json`, `dispatch-ledger.json`).

## Intermediates brought IN from /tmp (2026-07-17, via `mv` — nothing deleted)

| New in-folder location | Contents | Git status |
|---|---|---|
| `logs/jr-referee-20260716/tmp-run-scratch-20260717/` | Referee-run scratch: `jr-batches/` (blind input slices), `jr-verdicts/` + `jr-verdicts-sol/` (raw verdict files), `jr-sol-run/` (`run.sh` driver, `verdict.schema.json`, `smoke/`, `logs/`), plus `referee-agreement-sol-SELFTEST.json` and `x.json` (self-test outputs, carry the canary) | gitignored (under `logs/`) — on disk, not committed |
| `REPORTS/20260717-briefing/deck/build-intermediates-20260717/` | Deck verification screenshots (`deckpage-0{1,9},1{3,5}.png`, `deckcheck/`), render logs (`deck-httpd.log`, `chrome-pdf.log`), `deck.txt` extraction, `deck_pilot_preflight.json` | gitignored (new `.gitignore` rule) — on disk, not committed |
| `REPORTS/20260717-briefing/working/recompute-20260717/` | Per-model pilot recompute outputs `ww_recompute_<sut>.txt` (5 files) | **tracked** (small text provenance) |

These are regenerable scratch — the load-bearing, analysis-feeding data is the canonical
set already in `logs/jr-referee-20260716/`. The scratch is retained as provenance.

## Intentional design preserved (NOT "fixed")

`tools/audit/make_referee_batches.py` (writes `/tmp/jr-batches`) and
`tools/audit/ingest_referee_verdicts.py` (reads `/tmp/jr-verdicts`) use `/tmp` **by
design** — the referee-blindness methodology isolates prompts in `/tmp` so a referee sees
no repo paths or shipped verdicts. Archiving the past `/tmp` *outputs* (above) does not
change this: a rerun regenerates to `/tmp` as intended. Those `/tmp` paths were left as-is.

## Portability hardening (2026-07-17)

Three scripts had hardcoded absolute paths; changed to `Path(__file__)`-relative
resolution (behavior identical on this machine; folder is now path-portable):
- `tools/convert_banks.py` — `V1_ROOT_DEFAULT` → `V2_ROOT.parent / "Christian-Ethics-Benchmark"`
- `tools/verify_conversion.py` — same
- `REPORTS/20260717-briefing/working/extract_examples.py` — `BASE` → `Path(__file__).resolve().parents[3]`

## Deliberately left OUT of this folder (owner decisions, 2026-07-17)

- **~1.5 GB disposable `/tmp` pytest trees** (`/tmp/walkworthy-open6-*`,
  `/tmp/walkworthy-task2-review*`, old manuscript build dirs, repro PDFs) — left in `/tmp`;
  throwaway test roots, not reference material; auto-clear on reboot.
- **v1 canonical benchmark** (`../Christian-Ethics-Benchmark/`) — kept as a **read-only
  sibling**, not duplicated in. v2's parity/replay/rescore scripts reference it relatively
  (they resolve as long as v2 stays inside `40-BIBLEBENCH/`). The parity analyses are complete.
- **`WCF-Benchmark-v2/`** session-8/9/10 files that mention "walkworthy" — left untouched;
  that is a separate sibling project (its files reference walkworthy as precedent).
- **Cross-project skips verified NOT ours** (left in `/tmp`): `/tmp/deck_test.tex` (a LaTeX
  Beamer deck, no canary/CEB markers) and `/tmp/mhb_deckboot_index` (a git index file from
  an "mhb"/"wcf" project).
- **Auto-memory** at `~/.claude/projects/.../memory/` — stays there by design (vault convention).

## Storage pattern (why some things are gitignored)

This project keeps raw data/scratch **local on disk** (gitignored: `logs/`, `.venv/`,
holdout, the new scratch dirs) and commits the **analyzed reports**. So "in this folder"
means present on disk here — not necessarily on GitHub. This manifest (tracked) is the
index to the on-disk-only material.
