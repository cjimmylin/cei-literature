# BOOT PROMPT — v4-A execution ($0 strictly) · owner decision points pending

Read this at the start of a fresh session. Self-contained: a session with zero
prior context can act correctly from it. Authored 2026-08-02, immediately after
the v4-T tier probe was executed and its report landed (commit `52d5a26e9`).

**Supersedes `20260802b-boot-prompt-v4t-claude-tier-probe.md` as the entry
point.** Nothing there is retracted; its facts remain valid by reference. What
changed since: the v4-T Claude-tier probe was EXECUTED and DISCHARGED — SUT
census 486/486 on subscription OAuth ($0 external), d01 judging $0.1168 of the
$1.00 ceiling, evidence record `20260802c-v4t-tier-probe-report.md`. Do NOT
re-run the probe.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0 STRICTLY. v4-A (`RULINGS-APPLIED-20260801a` RULING 1) is
authoring + code with NO model calls and NO piloting. There is no open spend
authorization of any size. Anything spend-bearing — including any pilot of new
items, any judge run, any OAuth SUT call — needs a new ruling first.**

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
git fetch origin && git log --oneline -6 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
cd COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2
./.venv/bin/python -m pytest -q                    # 115 passed
./.venv/bin/python tools/verify_instrument.py      # ALL PASS 51/51 (WW-v2-20260731b)
```

State at authoring: newest ruling `RULINGS-APPLIED-20260802a`; newest commit
`52d5a26e9` (v4-T report `20260802c` + `tools/audit/tier_probe_claude_oauth.py`).
**If a `RULINGS-APPLIED-*` newer than `-20260802a` exists, read it FIRST — it
wins over this file.** Sibling WCF-Benchmark-v2 is worked by other sessions in
this clone; expect unrelated dirty files.

## 2. Governing state

| Thing | Status |
|---|---|
| v3 | STOPPED at Gate A, unchanged; published record = claims about WW-v2-20260724b |
| v4 spec `20260731j` v0.4 | RATIFIED (`-20260731n`); live-edit under version banners |
| v4-C | EXECUTED + CLOSED ($7.509 of $30.00); record `20260731o` |
| d02 hardened re-pilot | EXECUTED + DISCHARGED; record `20260801c`; do NOT re-run |
| v4-T tier probe | EXECUTED + DISCHARGED ($0 SUT + $0.1168 judging); record `20260802c`; do NOT re-run |
| **This session's task** | **v4-A execution (§4) — $0 strictly** (`-20260801a` RULING 1) |
| P-PRESSURE v4.0 scope | with the OWNER (both d02 pilots in hand; v4-T did not move it) |
| Judging architecture | OWNER-relevant new fact: d02 crux REPLICATED on d01 (`20260802c` §5) — surface it when the owner engages; no unilateral judge swaps |
| B1+B2 scale (~$180–230) | OPEN — owner decides later; B1 must NOT launch before v4-A code fixes 2(a)+2(b) land |
| d07 (P-COUNSEL) | conditional HOLD-exit (`-20260801a` RULING 2): NO candidate drafting until the anchored q2 definition exists |
| P-COMMITMENT | NOT ADVANCED (`-20260801a` RULING 3); revival needs a new ruling |

## 3. Facts not to re-derive (paid for on 2026-08-01/02)

1. **v4-T findings that BEAR on v4-A work** (full record `20260802c`):
   - Judge-B (llama-3.3-70b) produced degenerate/unparseable output on 5 of 294
     fresh d01 responses — the exact failure the 2(a) parse-hardening
     deliverable targets. Out-of-sample confirmation, not a new defect.
   - The d02 construct-disagreement crux REPLICATED: judges agree response-level
     (0.896) but their tier contrasts are nearly uncorrelated; judge-A saw a
     monotone Haiku→Sonnet→Opus gradient on d01 (Opus−Haiku +0.143, CI excludes
     zero), judge-B saw none. Judge choice is the binding measurement risk.
   - The d05 PUBLIC bank is at CEILING for current Claude tiers (CSR 0.91–0.93
     everywhere, all contrasts null). §2.2 hardened-allocation authoring should
     aim substantially harder than the existing public items; the only tier
     signal d05 produced was format compliance (haiku 42% first-pass format
     failures vs 31–33%).
   - All 49 d01 items key `full_obedience` (verified against every
     `keyed_behavior` string — 14 open with pair-reference phrasing but all
     define it).
2. **An OAuth SUT harness now exists**: `tools/audit/tier_probe_claude_oauth.py`
   (census / score-d05 / judge-d01 / analyze subcommands, resume-safe ledgers,
   $-ceiling discipline). If a future ruling authorizes another probe, port from
   there — but running it is NOT authorized by this file.
3. **Bank/scoring entry points** (read-only imports, never edit):
   `walkworthy_inspect/parsers.py` (`reparse_allocation_response`),
   `ordo_constraints.py` (`item_csr`), `scorers.py`
   (`assemble_rubric_prompt`), `rubrics.py` (`spec_for`, `judge_categories`).
   d05 allocation spec lives at `metadata.keyed.extras.allocation`
   (NOT top-level `keyed.allocation`).
4. **`tools/audit/` is NOT pinned** by `INSTRUMENT.json`. Pinned (do not edit
   without a ruling): `datasets/public/*.jsonl`, `tasks/*.py`,
   `walkworthy_inspect/*.py`.
5. **Rescore tooling for 2(a)**: the judge-B parse failures live in the rescore
   path — find the retry seam in the rescore tool named by report `20260731o`
   §6.1 (complete-case retention target ≥ 85% everywhere).

## 4. The task: v4-A execution (scope FIXED by `-20260801a` RULING 1 — do not re-litigate)

Work order (code first — 2(a)+2(b) gate B1; authoring is larger and can span
sessions):

1. **Code deliverables, with tests (RULING 1.2):**
   (a) judge-B parse hardening — retry-on-parse-failure in the rescore tool;
       target complete-case retention ≥ 85% everywhere (report `20260731o` §6.1;
       v4-T's 5/294 degenerate outputs are a ready-made regression fixture —
       run-tree rows in `logs/tier-probe-20260802/d01_judgments.jsonl`, raw
       field, gitignored but on disk).
   (b) empty-completion exclusion, BOTH halves — scorers route empty/truncated
       completions to unscorable; administration stops losing answers to
       reasoning-budget exhaustion (report §6.2).
   (c) ranked-sacrifice scorer per spec §2.2 with independent double-keying.
   (d) complete-case analysis upgrade + norming/reporting module (spec §3).
   Tests accompany each; the 115-test suite grows, it never shrinks or breaks.
2. **Anchored q2 definition (RULING 1.3):** written exemplar anchors for what
   counts as affirming/encouraging/blessing continuation (d07 rubric). This is
   an authoring deliverable — prose + exemplars, no model calls. d07 candidate
   drafting stays BLOCKED until this exists.
3. **Authoring (RULING 1.1):** §2.2 hardened-allocation expansion (~30 items;
   retire or harden WW-05-H01 / WW-05-M01 — and note fact 1: aim above the
   current ceiling); P-FAITHFULNESS (d03) REBUILD to n ≥ 16; P-MOTIVE (d04)
   REBUILD to n = 40 under spec §2.3 judged-item rules; admitted-axis expansion
   for d08 (P-GUARDRAIL) and d10 (P-DESERVINGNESS) ONLY — d06 (P-PROCESS)
   is DEFERRED. Every new/rebuilt dimension reserves ~20% holdout fractions,
   QUARANTINED AT CREATION (write new holdout items into the quarantine
   locations without ever reading existing holdout content; never set
   WALKWORTHY_ALLOW_HOLDOUT). Rejected items recorded, never deleted. Canary on
   every public bank line.
4. **Instrument discipline (RULING 1.4):** `WW-v2-20260731b` and its verify
   chain stay intact — new banks/scorers build the v4.0 line per spec §5.1 (new
   instrument id at freeze; superseded stamps preserved). Anything that would
   break `tools/verify_instrument.py` on the stamped tree needs its own ruling
   FIRST. Practical consequence: new-item banks go in NEW files/dirs, not into
   the pinned `datasets/public/*.jsonl`.

Deliverable hygiene: new dated files only; run the R3 linter on any new report
(`REPORTS/20260725-manuscripts/lint_claims.py`, 0 blockers); canary top+bottom;
pytest green before any commit; explicit-path commits with message via
`git commit -F <file>`, verify `git log -1 --stat`, then push.

## 5. What a session may also do without a new ruling

- Answer owner questions from committed artifacts (`20260802c` for the tier
  probe; `20260801c` for the d02 re-pilot; `20260731o` for v4-C).
- Present the pending owner decision menu when asked: P-PRESSURE scope, B1+B2
  scale, judging architecture in light of the replicated crux.
- The §1 $0 checks; maintain the entry-point chain (new dated files only; dated
  files immutable; spec `20260731j` stays live-edit under version banners).
- Do NOT: make any model call (SUT, judge, or otherwise); launch B1/B2; touch
  or read holdout (never set WALKWORTHY_ALLOW_HOLDOUT); re-run the d02 re-pilot
  or the v4-T probe; edit pinned components without a ruling; re-litigate the
  `20260731k`/`20260731l`/`-20260801a`/`-20260802a` adjudications; draft d07
  candidates before the anchored q2 definition lands; quote any probe
  diagnostic as a WALKWORTHY number or pool probe numbers with reference runs.

## 6. Binding constraints (by reference, unchanged)

All of `20260731f` §5 and `20260801b` §6: $0 default; holdout CLOSED; report
immutability (successor files); no deletions (RECYCLE-BIN); explicit-path
commits, message via `git commit -F`, verify `git log -1 --stat`; canary
top+bottom; R3 linter (0 blockers; a bold span must never end on a digit; no
"significant" as adjective); new-artifact gates (lint · canary ≥ 2 · pytest if
code touched · verify_instrument only if pinned components touched, which needs
a ruling first); deletion-guard and exec-token hook sharp edges.

## 7. Where things live

| Artifact | Path |
|---|---|
| Rulings ledger (newest wins) | `$V2/RULINGS-APPLIED-*.md` through `-20260802a.md` |
| v4-A scope (authoritative) | `$V2/RULINGS-APPLIED-20260801a.md` RULING 1 (+ RULING 2 for the q2 condition) |
| Spec (live, v0.4 ratified) | `$V2/20260731j-walkworthy-v4-design-spec.md` (§2.2, §2.3, §3, §5.1, §7) |
| v4-C report (names the 2(a)/2(b) defects) | `$V2/20260731o-v4c-execution-report.md` §6.1, §6.2, §7 |
| v4-T probe record + harness | `$V2/20260802c-v4t-tier-probe-report.md` · `$V2/tools/audit/tier_probe_claude_oauth.py` · run tree `$V2/logs/tier-probe-20260802/` (gitignored) |
| d02 discharge record | `$V2/20260801c-d02-hardened-repilot-report.md` |
| Bank files (pinned, read-only) | `$V2/datasets/public/design01.jsonl` … `design10.jsonl` |
| Scoring/judge entry points | `$V2/walkworthy_inspect/` (import, never edit) |
| Reading order, recent chain | `20260731o` → `-20260801a` → `20260801b` → `20260801c` → `-20260802a` → `20260802b` → `20260802c` → this file |

---

**If you are unsure whether something is authorized: it is not.** This session
is $0 strictly: v4-A code + authoring only; every model call, pilot, or scale
decision waits for the owner.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
