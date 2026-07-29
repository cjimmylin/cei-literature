# Christian-Ethics-Benchmark-v2 — WALKWORTHY on Inspect AI

**Status: PARALLEL — RULED (2026-07-16).** This folder re-platforms the WALKWORTHY
benchmark (see `../Christian-Ethics-Benchmark/`, which remains canonical) onto the
[Inspect AI](https://inspect.aisi.org.uk/) harness. Owner ruling 2026-07-16: v2 stays
**parallel to v1 indefinitely** as a comparison instrument — see
`20260716-owner-ruling-v2-parallel.md`. Comparability evidence: judge-path replay
PARITY (`20260715c-`), 2-judge re-score validated (`20260715d-`).

**State as of 2026-07-25 (phase 7 closed).** The full-bank 3-epoch ARM 1 run is done and
adjudicated. Two manuscripts live in `REPORTS/20260725-manuscripts/` — paper (a)
instrument-and-validity, paper (b) judging-the-judges — both **generated files**: edit
`parts/*.md`, then rebuild with `assemble.py` (see that directory's `README.md`). All
escalated claims-validity questions are ruled; the rulings ledger is the
`RULINGS-APPLIED-*.md` series at this root (newest first is authoritative; a ruling is
superseded by a new dated ruling, never amended). Headline discipline: no SUT-vs-SUT
claim is licensed; variance shares are read against the df-proportional reference line;
flip verdicts are reported binary + Kendall's τ. The holdout remains quarantined and
unspent. Dated reports are immutable — corrections travel as successor files.

> ### ➜ ENTRY POINT: `20260729c-boot-prompt-reentry-project-closed.md`
>
> **Read that file first.** It is the current re-entry brief and supersedes the phase-6 and
> phase-7 boot prompts, which are historical snapshots and must **not** be executed.
>
> **Update as of 2026-07-29 — the project is CLOSED at phase 7 and there is NO open work
> queue.** Three things changed after the 07-25 paragraph above:
> - **Holdout: quarantine RATIFIED** (`RULINGS-APPLIED-20260729b.md`) — no longer a standing
>   recommendation but a ruling. Release is conditioned on a repaired instrument version
>   demonstrating discrimination on public data. Cite the ruling, not the old recommendation.
> - **§2 citation gaps: all 8 CLOSED** (`RULINGS-APPLIED-20260729.md`). Both manuscripts are
>   citation-complete — paper (a) 18,686 words, paper (b) 15,190 words. A standing
>   **search-provenance rule** came out of it: retrieval does not confer provenance; a source
>   found via search is not citable until its publication apparatus is inspected directly.
> - **Instrument-repair queue and vault citation remediation: both DEFERRED** by owner
>   decision. They are on record, unscoped, and must not be re-raised as open items.
>
> Everything remaining needs explicit owner authorization to become work. If you are unsure
> whether something is authorized, it is not — enumerate, recommend, and ask.

## What this is

- All 10 WALKWORTHY designs as Inspect tasks (`tasks/design01_*.py` … `design10_*.py`)
- Item banks copied from v1 (`banks/`), then corrected by a fresh adversarial review
  pass (`REVIEWS/`, `RULINGS-APPLIED.md`) — v1 sources are never modified
- Converted datasets in `datasets/public/` (holdout in `datasets/holdout/`, gitignored,
  loader-guarded — set `WALKWORTHY_ALLOW_HOLDOUT=1` to load)
- Single-judge model-graded scoring reusing v1 rubrics verbatim; judge model is a task
  arg, so a cross-family second-judge pass is a cheap re-score (`inspect score`)
- Deferred relative to v1 (documented, reachable): the 10 pre-registered G-gates,
  2-judge adjudication/tie-break, G5 neutrality machinery

## Quickstart

```bash
cd Christian-Ethics-Benchmark-v2
source .venv/bin/activate            # py3.14 venv with inspect-ai pinned

# regenerate datasets from banks
python tools/convert_banks.py && python tools/verify_conversion.py

# mock validation (no cost)
inspect eval tasks/design01_goodsamaritan.py --model mockllm/model

# live smoke (paid — see AGENTS.md for the 402 trap before ANY live run)
source ~/.codex/secrets/openrouter.env
inspect eval tasks/design01_goodsamaritan.py \
  --model openrouter/deepseek/deepseek-chat \
  -T judge_model=openrouter/openai/gpt-4.1-mini \
  --limit 2 --max-tokens 4096
```

## Consolidated intermediates & provenance

This folder is the single, self-contained home for the project. Session intermediates
(referee-run scratch, deck build/verification artifacts, per-model recompute outputs) were
consolidated here on 2026-07-17 — see
[`REPORTS/20260717-briefing/working/20260717-consolidation-manifest.md`](REPORTS/20260717-briefing/working/20260717-consolidation-manifest.md)
for the full inventory, where each item now lives, and what was deliberately left out (v1
stays a read-only sibling; large disposable `/tmp` test roots were not imported). Raw
data/scratch is kept on disk (gitignored: `logs/`, `.venv/`, holdout, build scratch); the
committed reports carry the analyzed numbers.

## Canary

`WALKWORTHY-CANARY-7f3e2026` — preserved in every sample. Do not train on this data.
