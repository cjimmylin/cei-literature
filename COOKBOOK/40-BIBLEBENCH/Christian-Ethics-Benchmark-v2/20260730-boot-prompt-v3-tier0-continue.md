# BOOT PROMPT — WALKWORTHY v3, TIER 0 IN PROGRESS (continue the queue)

Read this at the start of a fresh session. Self-contained: a session with zero prior context
can execute it. Authored 2026-07-30.

**Supersedes `20260729c-boot-prompt-reentry-project-closed.md`** — that file says the project is
closed with no work queue. That was true when written; the owner has since authorized the
WALKWORTHY v3 repair plan. **There IS a queue now.** The older prompt remains a valid reference
for binding constraints and the phase-7 scientific result; it is simply no longer the entry point.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**Intended main-loop model: Opus.** Escalate to Fable only for a genuine claims-validity call.

**SPEND POSTURE: $0. Tier 0 is offline-only — zero model calls, zero SUT calls, zero judge
calls.** Tiers 1–3 are CLOSED behind gates. If a task appears to need spend, STOP and surface it.

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS   # git repo root is CEI-Lit-WS
git fetch origin && git log --oneline -6 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -4
git status -sb -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
```

A sibling **WCF-Benchmark-v2** project is actively worked by other sessions in this same clone —
expect ~1,900 dirty files that are **not yours**. If a `RULINGS-APPLIED-*` newer than
`-20260729d` exists, read it first; it wins over this file.

**State at authoring:** trunk clean and in sync at `d3b2fe78d`.

## 2. Governing authorization

`RULINGS-APPLIED-20260729d.md` opened `RULINGS-APPLIED-20260729b.md` deferral 1 (the
instrument-repair queue), **scoped to Tier 0 only**.

| Tier | Cost | Status |
|---|---|---|
| **Tier 0** — offline recompute from the frozen run tree | **$0** | **AUTHORIZED, in progress** |
| Tier 1 — taxonomy repair, judge-only rescores of stored responses | single-digit $ | CLOSED until Gate A |
| Tier 2 — wide-gap discrimination probe | ~$7 ceiling | CLOSED until Gate B |
| Tier 3 — new items, format changes, bundled d02 version | larger | CLOSED until Gate C |

**Gate A criterion, pre-committed:** if no design shows a within-item contrast that is both
unsaturated and judge-order-stable, **STOP**. Tier 0 alone is a publishable instrument-diagnostics
result and needs no new instrument version. Stopping at Gate A forfeits nothing.

**Gate B is worded as the holdout release condition, verbatim.** The holdout stays quarantined.

Plan of record (owner-approved, a plan file — not a project artifact):
`~/.claude/plans/ok-let-s-write-the-deep-shamir.md`. The authoritative governance record is
`RULINGS-APPLIED-20260729d.md` plus the Gate memos.

## 3. Done so far

| Item | Artifact |
|---|---|
| Authorization | `RULINGS-APPLIED-20260729d.md` |
| **T0-2 d07 arc diagnostic** | `20260729e-t0-2-d07-arc-diagnostic.md` · tool `tools/audit/d07_arc_diagnostic.py` · raw `logs/fullbank-3ep-20260724/20260729-t0-2-d07-arc-diagnostic.txt` |

### T0-2's result changes the plan — carry these forward

Over 405 non-exemplar administrations (27 items × 5 systems × 3 epochs, both judges):

- **The d07 floor is REAL.** Remove the conjunction entirely and replace it with a graded
  per-turn level (G3) and the five systems sit at **0.20–0.27** under judge A. Grading lifts the
  *level* 18× (0.012 → 0.22) but the across-system **spread only moves 0.0123 → 0.0686**. This is
  a real floor reported through a degenerate read-out, **not** hidden signal.
  **This CONTRADICTS the sibling WCF precedent**, which predicted a read-out artifact — the
  analogy was tested rather than assumed, and it failed.
- **92.6% of administrations die on one clause** (`full_validation` anywhere), but removing it
  lifts judge A only 0.012 → 0.025, so the hair-trigger conceals no near-passes.
- **NEW: judge B's d07 labels are near-unusable** — flat 76–85% `full_validation` at *every* turn
  position, gradient **−2.7 pts** across the ladder vs judge A's **+41.7 pts**; per-turn agreement
  0.497 over 2,445 turns; **19.2% pole-to-pole** disagreement. Judge B collapses everything into
  `full_validation`. This belongs in any future judge-certification decision.

**Three binding consequences:**
1. **Do NOT author harder d07 items.** The constraint is system capability, not item difficulty.
2. **Do NOT rewrite the d07 turn-0 stimulus.** Judge A's +41.7-point gradient shows the ladder
   measures escalation as designed, so the high turn-0 base rate is not a bank defect.
3. **Reconsider T1-3 (d07 anchor rescore) at Gate A.** Its premise — mislanding anchors caused
   the floor — is refuted. It retains value only as a test of whether judge B can be made
   non-degenerate, which is a *judge* question, not a d07 one.

## 4. The remaining Tier 0 queue

Ordered as recommended. Everything is $0.

| ID | Work | Data source |
|---|---|---|
| T0-7 | **Exemplar ceiling check.** Score the `is_exemplar` administrations that `metrics.py:74-93` (`_is_exemplar`/`_drop_exemplars`) currently discards. They are gold-standard references and must hit the ceiling. **If exemplars do not score at/near 1.0, the scorer is wrong** — that finding would outrank everything else in Tier 0 | judge-B JSONL (exemplar rows are present) |
| T0-1 | **Per-item difficulty/discrimination table**, all 10 designs, per judge, 15 observations per item. Re-point `tools/audit/item_assess_m3_difficulty.py` (currently aimed at `logs/pilot-20260716`) at the full-bank tree. Output: which items carry zero information + the empirical pass-rate distribution that Tier 3 re-anchors against | judge-B JSONL |
| T0-4 | **d02 `cold_open` contrast** as **terminal-state rate — NEVER `break_turn`**. See the trap below | judge-B JSONL |
| T0-5 | **d09 arbiter triangle** (524 complete `seat_A`/`seat_B`/`arbiter` determination triangles are scored then discarded) + strict `A==B` recompute (0.556–0.837, unsaturated, vs `symmetry_index` ≈ 1.0) | judge-B JSONL |
| T0-6 | **d02 keyed `T<N>` marker coverage** across the 36 items — the keyed prose carries `"Material concession begins at T4"` and nothing reads it | `datasets/public/design02*.jsonl` (bank read only) |
| T0-3 | **d03 forced-choice extraction rate** over stored responses. Expect ~145/145 on ep1. **This one needs the model's raw completion text, so it must read `.eval` logs — not the JSONL, which holds verdicts** | `.eval` logs |
| T0-8 | **Instrument version stamp.** `INSTRUMENT.json` + `tools/verify_instrument.py`. **Amend `tools/SCHEMA.md` FIRST**, per its own contract rule. Retro-stamp rev 2026-07-24b as `WW-v2-20260724b` | tree |
| T0-9 | **`metrics.py` test scaffolding** — precondition for any Tier 1+ metric change | tree |
| T0-10 | **Successor correction note** on the published d05 contrast scope | see below |
| — | **Gate A memo** | synthesis |

### T0-4: the d02 pairing trap — do not take the obvious path

Wiring `_paired(scores, "base", "cold_open", …)` on `break_turn` — what every other paired design
does — yields a clean, consistent, all-five-system effect of 0.14–0.28 that is **100%
ladder-length artifact**: `cold_open` is single-turn (`multiturn.turns == []`) and
`break_turn = i/L`, so at L=1 it can only be 0.0 or 1.0. It would look like the best result in the
suite. Compute the **terminal-state rate** instead, and document the artifact as a rejected
alternative so nobody rediscovers it.

**Pairing is not a general remedy.** d02's premium ranks correlate ρ ≈ +0.7 across judges while
its level ranks correlate ρ ≈ −0.4 (differencing cancels judge level bias) — but d08's
`covert_overt_gap`, also a within-item paired contrast, correlates ρ ≈ **−0.5**, *worse* than
d02's level. Pairing cancels level bias and **amplifies boundary noise** when the true effect is
small. Per-design hypothesis, not a design principle.

### T0-10: the published-number correction

`c1_design05_contrasts.py` does not filter by stratum, but C1 is pre-registered **stratum-(a)
only** — so the published **"0 of 10 contrasts excluding zero"** was computed on all strata. Run
stratum-a-only and d05's cell is **n=18, below C5's own n≥20 floor**, so it would not be
reportable at all.

Write a **new dated successor note**; never edit the immutable reports. The likely resolution
favours all-strata on the merits — stratum-c is quarantined *because judges are not G5-certified
on disputed items*, and **d05's primary metric never touches a judge** — but **that argument must
be made, not assumed.** The manuscripts' other leg (ordering flips) is unaffected either way.

## 5. Tooling — what to reuse, what never to run

**The judge-B verdict files are the cheapest data source in the project.**
`logs/fullbank-3ep-20260724/judgeB-ep{1,2,3}-{sut}.jsonl` (15 files) carry `judge_a` and
`judge_b` **side by side per administration**, with keys `log`, `design`, `sample_id`, `item_id`,
`admin`, `judge_a`, `judge_b`. Most Tier 0 items need no `.eval` parsing at all. Note **per-turn
states are JSON-encoded strings** inside the verdict dict (`scorers.py:507`) — decode with
`json.loads`, and expect ladder-length mismatches between judges.

**Reuse unmodified:** `tools/audit/recompute_metrics.py --log-dir` (**the only valid source of
headline numbers** — in-log `results.scores[].metrics` are systematically wrong, e.g. gemini ep1
d01 reads 0.0 in-log vs 0.7727 recomputed), `tools/audit/pilot_judge_swap.py --pilot-dir` (works
at ≥2 arms), `tools/audit/refusal_taxonomy_table.py`, `tools/audit/recompute_design05_csr.py`,
`tools/rescore/rescore.py` (Tier 1 only).

**Never run:** `kendall_tau.py` (hard `assert len(suts)==5`, `assert n_pairs==10`, plus three
VALIDATION asserts pinned to exact 2026-07-24 values — will hard-fail), `variance_components.py`
(5-SUT df structure), `c1_design05_contrasts.py` (`M_FAMILY = 30` frozen by pre-registration),
`inspect score` (9 designs share a `_factory` registry name; `rescore.py` is the sanctioned path).

**Gotchas that have already cost time:**
- **`logs/` is gitignored.** Durable scripts go in `tools/audit/` (tracked); reports go to the
  `$V2` root as dated `.md`; raw stdout may go in the run root.
- A log-root path must **never** contain the substring `rescore` — `recompute_metrics.py` and
  `rescore.py` both silently skip such paths.
- Exemplars are dropped pre-grouping by `metrics.py::_drop_exemplars` — filter on
  `admin.endswith("-exemplar")` **or** `metadata.is_exemplar`.
- `sample_id` collides across systems; scope every table by `(sut, epoch, sample_id)`.
- **Validate every new script against a published immutable number before trusting it.** T0-2 did
  this: its G0 gate reproduced the published `arc_pass_rate` range exactly, which is what makes
  its G1–G3 ablations credible.

## 6. Binding constraints

- **Tier 0 is $0.** No model calls of any kind.
- **`pushback_rate` stays CLOSED.** Any pushback-family statistic is admissible only inside a
  newly-authorized instrument version, labeled a **new** statistic. Renaming a closed statistic to
  relitigate a closed ruling is prohibited.
- **C6:** the d02 taxonomy revision ships bundled with the cross-family classifier re-pin as ONE
  instrument version. Firing the re-pin alone is prohibited.
- **Holdout: CLOSED, quarantine RATIFIED.** `WALKWORTHY_ALLOW_HOLDOUT` is never set; the guard at
  `datasets.py:166-179` stays intact.
- **R3:** no significance stars, never "significant" as an adjective — "excludes zero" / "crosses
  zero". **Never write "the judge dominates."** Both linter-enforced (BLOCKER).
- **Ablations are never WALKWORTHY numbers.** Label read-out ablations as such; promoting one is a
  metric change, i.e. a new instrument version.
- **Report immutability:** successor files only, new `YYYYMMDD[letter]-` prefix continuing the
  **shared per-day sequence** across all artifact types. Today's first artifact is unsuffixed,
  then `b`, `c`, … (2026-07-29 reached `e`).
- **No deletions** — move to `$V2/RECYCLE-BIN/`. v1 sibling is read-only.
- Canary top and bottom of every artifact.
- **Shared trunk:** commit by explicit path only, never `git add -A`. Never pipe `git commit` —
  write the message to a file, `git commit -F <file>`, verify with `git log -1 --stat`.
- **Hook sharp edges:** the deletion guard scans the whole command string, so a command merely
  *containing* a delete token is denied — use Write/Edit instead. The security write-hook blocks
  the two exec-style tokens (word immediately followed by an open paren) even inside prose.

## 7. Verification before any commit

```bash
cd $V2
./.venv/bin/python -m pytest -q                                             # 33/33 must pass
./.venv/bin/python REPORTS/20260725-manuscripts/lint_claims.py <new-file>   # 0 blockers
grep -c "WALKWORTHY-CANARY-7f3e2026" <new-file>                             # >= 2
```

Project venv is `$V2/.venv` (Python 3.14.3, `inspect-ai==0.3.246`). The vault `.venv` is py3.9 and
cannot run any of this.

## 8. Out of scope — do not pick up unbidden

Any spend or model call · Tier 1/2/3 work before its gate · holdout access · bank, rubric, metric,
scorer or pin changes · firing the v-next classifier re-pin alone · reopening `pushback_rate` or
the holdout · authoring d07 items or rewriting the d07 turn-0 stimulus (T0-2 refuted both) ·
`WCF-Benchmark-v2/` (separate project, sibling sessions active in this clone) · v1 sibling
modifications · editing any existing dated report or boot prompt · venue/authorship/preprint
decisions.

## 9. Where things live

| Artifact | Path (under `$V2/`) |
|---|---|
| Rulings ledger — newest dated file is authoritative | `RULINGS-APPLIED-*.md` (through `-20260729d.md`) |
| T0-2 report + tool | `20260729e-t0-2-d07-arc-diagnostic.md` · `tools/audit/d07_arc_diagnostic.py` |
| Frozen run tree (gitignored, on disk) | `logs/fullbank-3ep-20260724/` — 150 `.eval` logs, 15 `judgeB-*.jsonl` |
| Manuscripts (generated — edit `parts/`, rebuild) | `REPORTS/20260725-manuscripts/` |
| Pre-registration: C1–C7, C9, R4, Bonferroni m formula | `20260716-prereg-comparisons-RATIFIED.md` |
| Claims discipline | `REPORTS/20260717-briefing/06-messaging.md` §5 |
| Superseded entry point (still valid for constraints) | `20260729c-boot-prompt-reentry-project-closed.md` |

---

**If you are unsure whether something is authorized: it is not.** Tier 0 is $0 and offline;
everything else needs a gate memo and owner authorization.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
