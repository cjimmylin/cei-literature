# WCF-Benchmark-v2 — Folder Index

Single-glance map of this project. WCF-Bench-v2 is a discriminating **Christian-ethics
conduct benchmark** (Westminster Standards) evaluated on Inspect AI, with a validated
strong judge panel (strict-v2 template, opus + GPT-5.6-Sol mean-of-2, single-packet
mode, panel ICC(2,1)=0.985) and a frontier leaderboard.

**Current state (2026-07-31, end s19):** bank v2.5 frozen (scored bank **345** — the
"317" in s16 docs is a ratified-corrected double-count); strict-v3 candidate REJECTED
at its bench gate (auto-revert; see `analysis/20260725-session17-v3-gate-adjudication.md`);
**Scenario A full run COMPLETE** (5,175/5,175 responses, both judge arms) and the
mandatory judge-gap triage executed (90-cell blind audit, 90% idiom rate — see
`analysis/20260731-session19-judge-gap-triage.md`). **First QUOTABLE results report
shipped:** `reports/20260731-session19-quotable-results-report.md` — every earlier
report/artifact (s1–s18) stays EXPLORATORY and must not be cited as SUT evidence.
**Session 20: full v1.x paper draft landed** (venue-generic, no venue/DOI/author list):
`reports/20260731-session20-v1x-paper-draft.md` — every number traces to the s19 report
or `analysis/session20_composition_stats.py`'s reproducible bank-composition figures; all
6 s19 disclosures plus the strict-v3 episode carried into its own Limitations & Methods
Integrity section. Committed + pushed (`629bcdbc1`, `900645023`). **Owner accepted the
draft (2026-07-31)** — 12pp PDF built via `reports/20260731-session20-build-pdf.py`
(pandoc→typst, same pipeline as the s9 briefing): `reports/20260731-session20-v1x-paper-draft.pdf`
(gitignored, disk-only; build script committed `6f750bac6`). No session-21 boot prompt
written yet — next step is the owner's to name.

**This folder is self-contained** — every artifact, dataset, script, and deliverable lives
inside it, and (as of 2026-07-17) the one runtime dependency on the v1 sibling has been
vendored in (see `vendor/`). Nothing outside the folder points into it, so it can be moved,
archived, or handed off as a single unit.

## Folder map

| Path | What's here |
|------|-------------|
| `README.md` | Original project readme |
| `INDEX.md` | This file — the navigation entry point |
| `20260715-session3` … `20260725-session18-fullrun-completion-boot-prompt.md` | Session boot-prompts (chronological build log; newest = the next session's entry point) |
| `DECK/` | **Session-10 summary deck** — `…-readiness-deck.md` (source) → `build-deck.py` → `.html` → `.pdf` |
| `reports/` | 40+ session reports + the **6 session-9 readiness reports** (`20260717-session9-0{1..6}-*.md`) + `build-pdf.py` → 34pp briefing PDF |
| `METHODS/` | Academic + operational methods write-ups and handoff |
| `src/` | Core benchmark library: `wcf_tasks.py`, `wcf_grading.py`, `prompt_frames.py`, `episode_solver.py`, `templates/` |
| `convert/` | Data pipeline: `yaml_to_jsonl.py` (bank → datasets) + per-session patch/new-item scripts |
| `analysis/` | 23 per-session stat scripts + their JSON/JSONL/CSV outputs + review subfolders |
| `data/` | Generated item bank: `wcf_main.jsonl`, `wcf_episodes.jsonl`, drafts, `BANK-VERSION.json` |
| `tests/` | Pytest suite (converter, grading, sessions 5–7) |
| `logs/` | Inspect-AI eval run logs (33 run-sets, 126 `.eval` + manifests) + session evidence dirs: `20260724-session16-{pilot,stability}/`, `20260725-session16-b3-audit/`, `20260725-session17-bench-v3/` (v3 gate evidence), `20260725-session17-fullrun/` (**live Scenario-A run**: RUN-MANIFEST, responses, dual-judge verdicts) |
| `vendor/v1-bank-yaml/` | **Frozen copy of the v1 item-bank YAML** the converter reads (see `vendor/README.md`) |
| `.venv-v2/` | Python virtualenv (gitignored; rebuild via `requirements.txt`) — 258 MB |
| `RECYCLE-BIN/`, `reports/RECYCLE-BIN/` | Superseded files (never deleted, per vault rule) |

## Rebuild each deliverable

| Deliverable | Command (run from this folder root) |
|-------------|-------------------------------------|
| Datasets (`data/wcf_main.jsonl`, `wcf_episodes.jsonl`) | `.venv-v2/bin/python convert/yaml_to_jsonl.py` (reads `vendor/v1-bank-yaml/`) |
| Session-9 briefing PDF (34pp) | `.venv-v2/bin/python reports/20260717-session9-build-pdf.py` (pandoc → Typst) |
| Session-10 deck HTML | `python3 DECK/20260717-session10-build-deck.py` |
| Session-10 deck PDF | Chrome headless `--print-to-pdf` on `DECK/…-readiness-deck.html?print` (one slide/page via `body.print` CSS) |
| Analysis stats | `.venv-v2/bin/python analysis/<compute_*.py>` (paths now anchor to this folder) |

## Git / artifact notes

- Tracked in the `CEI-Lit-WS` repo (shared trunk `main`).
- **PDFs are gitignored** (root `.gitignore` `*.pdf`) — on-disk only, regenerable via the build scripts above.
- `.venv-v2/`, `__pycache__/`, `*.pyc`, `.pytest_cache/` gitignored locally.
- The session-10 deck `.html` is tracked; both PDFs are not.

## Provenance / external touch-points

- `vendor/v1-bank-yaml/` is a **frozen copy** of `../WCF-Benchmark/05-BANK-YAML/` (the v1
  predecessor), taken 2026-07-17. The converter reads the vendored copy, so re-running the
  pipeline no longer requires the v1 sibling. The upstream copy stays canonical.
- Documentation (boot-prompts, METHODS, README) still *mentions* `../WCF-Benchmark/` and
  `../Christian-Ethics-Benchmark*/` as historical context / read-only reference — these are
  narrative pointers, not runtime dependencies.
- `logs/*/logs.json` embed absolute dataset paths from when the evals ran (historical;
  only relevant if you re-index/replay old eval logs).
