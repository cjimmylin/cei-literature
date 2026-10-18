# RULINGS APPLIED — 2026-10-18b: v4 judging re-judge package AUTHORIZED ($3.00 hard) · candidate judge chosen · D3–D7 remain OPEN

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-18 · **Spend ceiling authorized: $3.00 hard for the whole re-judge package
(projection AND actual).**
**Predecessor:** `RULINGS-APPLIED-20260802a.md`. Its RULING 1 (v4-T) was executed and CLOSED at
$0.1168 of $1.00 (report `20260802c`). Nothing of that ceiling carries forward.
**Subject:** the owner's ruling on memo `20261018a-v4-judge-decision-options-memo.md` §5, decisions
D1 and D2. The ruling reached the drafting session through the coordinating session on
2026-10-18 and is recorded here as relayed. D3–D7 were not ruled.

---

## RULING 1 — D1: option (e) AUTHORIZED, the memo's §3 recommended package, $3.00 HARD

Scope, exhaustive:

1. **Stage 0 ($0):** authoring and tooling only, with no model calls. The deliverables are listed
   in §Stage 0 below.
2. **Stage 1a, d02 anchored holds.** Judges A (`openai/gpt-4.1-nano`) and B
   (`meta-llama/llama-3.3-70b-instruct`) re-read the STORED hardened-census final-turn responses:
   7 items × 3 epochs × 6 pairs × 2 orderings, with empty cells excluded as in `20260801c`. The
   Stage-0 anchor block (`20261018c` §5) is inserted before Step 2. Everything else in the
   hardened protocol is unchanged.
3. **Stage 1b, d07 anchored q2.** Judges a and b re-read the STORED v4-C arcs (750 turns) with the
   `20260802e` §6 q2 block in place of the bare q2 line.
4. **Stage 2, one candidate judge (RULING 2) at k ≤ 10,** where k is the candidate's price relative
   to judge-A. It reads the STORED d02 hardened census under the UNCHANGED hardened prompt, and the
   STORED v4-T d01 responses (294) under the shipped rubric prompt. The candidate replaces no judge
   here: it is scored alongside the existing ledgers.
5. **Stage 3 (optional), referee arm,** at $0 API: Opus through a Claude Code agent and Sol through
   codex exec, following the JR precedent (`20260717-sol-referee-results.md`). It is NOT automated
   by the package runner and needs an owner direction at the time it runs.

**Spend and run rules:**
- The $3.00 hard ceiling applies across the whole package, to projection AND actual.
- Each paid block starts with a calibration micro-run.
- Stop-and-report on any breach: a projection over the remaining budget, a tool hard stop, a
  recorded per-job cost above the bound the in-flight reserve assumes, or a tool error.
- ZERO SUT calls: every stage re-reads stored responses.
- The holdout is never read. WALKWORTHY_ALLOW_HOLDOUT is never set, and holdout paths and markers
  are refused.
- The pre-committed read-outs file `20261018d-rejudge-precommitted-readouts.md` is committed BEFORE
  any paid call.

**Interpretation guardrails:**
- Every number is a diagnostic. None is a WALKWORTHY number, and none is ever pooled with
  reference runs.
- Nothing here changes an instrument pin, a judge pin, or a gate. `tools/audit/` is not pinned by
  `INSTRUMENT.json`, and `WW-v2-20260731b` is untouched.

## RULING 2 — D2: candidate judge

The owner had no preference, and the coordinating session chose **`qwen/qwen3-235b-a22b-2507`**
(Qwen3-235B-A22B instruct, non-thinking; Alibaba).

- **Vendor overlap:** none with the 7 reference models (spec `20260731j` §4.1) or with either
  pinned judge.
- **Price:** about 1–2× judge-A, to be re-verified at launch.
- **Price bound used by the tools:** $0.25 per M input tokens and $1.00 per M output tokens,
  labelled a **bound**. That is 2.5× judge-A's $0.10/$0.40 bound, within k ≤ 10. The bound prices a
  call only when OpenRouter returns no usage.cost, and it sizes the in-flight reserve.
- **Ledger label:** `judge-C`.

## Standing — D3–D7 remain OPEN

Memo `20261018a` §5 lists these; none is decided by this file:

- **D3:** d02's v4.0 scope.
- **D4:** the B1+B2 scale (still deferred; B1 still needs the v4-A authoring remainder).
- **D5:** the freeze-review conventions.
- **D6:** the holdout git-history question.
- **D7:** P-COMMITMENT, which stays not advanced per `-20260801a` RULING 3.

Also unchanged:
- v4-A stays open at $0 under `RULINGS-APPLIED-20260801a` RULING 1.
- The entry point stays `20260806a-boot-prompt-v4a-authoring-remainder.md`; this file adds the
  package and its run guide.
- Newest-ruling-wins: this file wins over `-20260802a` and everything older.

## Stage 0 deliverables

These were written 2026-10-18 at $0, with no network call. They sit in the working tree,
uncommitted, pending owner review.

| Deliverable | Path |
|---|---|
| This ruling and the run guide | `RULINGS-APPLIED-20261018b.md` |
| d02 anchored-holds definition (Stage-0 draft for the v4.0 freeze) | `20261018c-d02-anchored-holds-definition.md` |
| Pre-committed read-outs (commit BEFORE any paid run) | `20261018d-rejudge-precommitted-readouts.md` |
| d02 tool: `anchored` prompt variant, `--judge`, `--only-judges`, `--price-bound`, `--ceiling` | `tools/audit/d02_davidson_bt_pilot.py` |
| d07 tool: `--q2-variant anchored` (the `20260802e` §6 block verbatim), `--judge {a\|b}=SLUG`, `--price-bound` | `tools/audit/d07_determinate_rubric.py` |
| tier tool `judge-d01`: `--judge`, `--only-judges`, `--price-bound`, `--responses`, `--log-root`, `--ceiling` | `tools/audit/tier_probe_claude_oauth.py` |
| One-command package runner (dry-run by default) | `tools/audit/rejudge_package_20261018b.py` |
| Offline tests (no network; synthetic fixtures built in pytest's temp dir) | `tests/test_rejudge_package_20261018b.py` |

All new flags default to the prior behaviour. With no new flag, each tool's prompts, request
bodies, ledgers, results files, and printed output were checked byte-identical against the
pre-change version. That check used a synthetic fixture, a mocked network, and a temp directory
outside the repo. Every override refuses to write into a closed ledger.

## Run guide (owner)

**Where:** the machine that holds the gitignored run trees, from the `Christian-Ethics-Benchmark-v2/`
root, with the project venv.

**Inputs the runner reads (read-only):**
- `logs/widegap-probe-20260731/`: the stored d02 and d07 transcripts, which Stages 1a, 1b and 2a
  re-read. Required.
- `logs/d02-btpilot2-20260801/verdicts.jsonl`: required for the comparisons.
- `logs/tier-probe-20260802/responses.jsonl` and `d01_judgments.jsonl`: required.
- `logs/d07-detrubric-20260731/records.jsonl`: optional; it lets the baseline be recomputed.
- The key file `~/.codex/secrets/openrouter.env`. It is read only by `--live`, passed to the tool
  subprocesses through their environment, never printed, and never written.

**Steps:**

1. Commit the Stage-0 files, including `20261018d`, before any paid run. Optionally run
   `./.venv/bin/python -m pytest -q`.
2. Dry run, $0 and no network:
   `./.venv/bin/python tools/audit/rejudge_package_20261018b.py`
   Expect "DRY RUN OK". The stage table should show about 468 / 1,500 / 234 / 294 calls and a
   projected total of about $0.68. That projection is an *estimate* from recorded per-call actuals,
   with the candidate projected at 2.5× judge-A, its bound ratio.
3. Live: `./.venv/bin/python tools/audit/rejudge_package_20261018b.py --live`
   - First, before any paid call, the runner re-verifies the launch prices as ruling D2 requires. It
     reads OpenRouter's free model list, confirms all three slugs are listed, and checks each live
     price against its bound and the candidate's k ≤ 10. It stops at $0 if any check fails.
   - Expect about $0.7 (an estimate). The hard cap is $3.00.
   - The command is resume-safe: re-running it skips recorded calls, and any re-run still counts
     against the same $3.00.
4. If it prints **STOPPED**, do not re-run before reading the stop reason in `run.log`.
   `--readouts-only` recomputes the read-outs from whatever ledgers exist, with no calls.

**What to send back:**
- `logs/rejudge-20261018b/summary.json`
- `logs/rejudge-20261018b/package_tally.json`
- `logs/rejudge-20261018b/run.log`
- The READ-OUTS block printed at the end.

A successor session then writes the dated execution report against `20261018d`, and D1's
architecture choice returns to the owner.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
