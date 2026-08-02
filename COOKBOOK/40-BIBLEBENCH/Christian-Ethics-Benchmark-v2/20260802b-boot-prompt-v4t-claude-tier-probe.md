# BOOT PROMPT — v4-T Claude-tier differentiation probe (AUTHORIZED: OAuth SUTs $0 · judging $1.00) · v4-A OPEN ($0)

Read this at the start of a fresh session. Self-contained: a session with zero
prior context can act correctly from it. Authored 2026-08-02, immediately after
`RULINGS-APPLIED-20260802a` landed.

**Supersedes `20260801b-boot-prompt-d02-repilot-v4a-open.md` as the entry point.**
Nothing there is retracted; its facts remain valid by reference. What changed
since: the d02 hardened re-pilot was EXECUTED and DISCHARGED at $0.178 of $2.00
(report `20260801c-d02-hardened-repilot-report.md`, commit `aa4ebd9d9` — headline:
mechanical confounds fixed, but the judges disagree at the CONSTRUCT level, modal
per-cell hold agreement 9/81; P-PRESSURE scope decision back with the owner), and
the owner authorized v4-T (`RULINGS-APPLIED-20260802a`).

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: SUT administration runs on Claude Code subscription OAuth ($0
external spend). $1.00 hard ceiling authorized for exactly one block — the d01
judge calls (§4.6). v4-A is open but strictly $0. Everything else needs a new
ruling.**

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
git fetch origin && git log --oneline -6 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
cd COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2
./.venv/bin/python -m pytest -q                    # 115 passed
./.venv/bin/python tools/verify_instrument.py      # ALL PASS 51/51 (WW-v2-20260731b)
claude --version                                   # CLI present (OAuth channel)
```

State at authoring: newest ruling `RULINGS-APPLIED-20260802a`; newest commit
`aa4ebd9d9` (d02 re-pilot + report 20260801c), then the commit carrying
`-20260802a` + this file. **If a `RULINGS-APPLIED-*` newer than `-20260802a`
exists, read it FIRST — it wins over this file.** Sibling WCF-Benchmark-v2 is
worked by other sessions in this clone; expect unrelated dirty files.

## 2. Governing state

| Thing | Status |
|---|---|
| v3 | STOPPED at Gate A, unchanged; published record = claims about WW-v2-20260724b |
| v4 spec `20260731j` v0.4 | RATIFIED (`-20260731n`) |
| v4-C | EXECUTED + CLOSED ($7.509 of $30.00); record `20260731o` |
| d02 hardened re-pilot | EXECUTED + DISCHARGED ($0.178 of $2.00); record `20260801c`; do NOT re-run |
| P-PRESSURE v4.0 scope | with the OWNER, both pilots in hand; v4-T neither advances nor closes it |
| v4-A | OPEN, $0 (`-20260801a` RULING 1): authoring + 4 code deliverables |
| **This session's task** | **v4-T tier probe (§4): OAuth SUT runs $0 external; d01 judging $1.00 hard** (`-20260802a` RULING 1) |
| B1+B2 scale (~$180–230) | OPEN — owner decides later; B1 must NOT launch before the two v4-A code fixes land |

## 3. Facts not to re-derive (paid for on 2026-08-01/02)

1. **The OAuth channel already exists** — port, do not reinvent:
   `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/wcfbench/cli_client.py`
   (`CLIModelClient`). Pattern: `claude -p <prompt> --model <full-id>
   --output-format json`, with (a) `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`
   unset in the child env so subscription OAuth is used (its probe confirmed
   `apiKeySource: none`); (b) hygiene flags `--tools "" --strict-mcp-config
   --permission-mode dontAsk --max-turns 1 --setting-sources ""` so the SUT is
   the model, not an agent loop; (c) a clean CLAUDE.md-free temp cwd so vault
   memory cannot steer the SUT; (d) parse the `type: result` JSON event for
   `.result` text and `.total_cost_usd`. Known caveats recorded in its
   docstring: keep OAuth runs to modest scale (ToS), no temperature/seed
   control, roughly 10k tokens of per-call harness overhead.
2. **Pin full model ids; never aliases** (aliases float to newest release). The
   three SUTs: `claude-haiku-4-5-20251001`, `claude-sonnet-5`, `claude-opus-5`.
3. **Bank facts:** `datasets/public/design01.jsonl` = 49 admin lines,
   model-graded (judge categories per `walkworthy_inspect/rubrics.py`: d01 →
   `action_class` categorical + `rationale_quality` ordinal 0–2).
   `datasets/public/design05.jsonl` = 32 admin lines, JUDGE-FREE primary:
   `walkworthy_inspect/parsers.reparse_allocation_response` +
   `walkworthy_inspect/ordo_constraints.item_csr` compute constraint-satisfaction
   programmatically. Both designs are single-turn; each item carries its own
   system framing as `input[0]` (role `system`) and user text as `input[1]`.
   Every sample has `metadata.canary`; holdout lives in `datasets/holdout/` and
   `banks-holdout/` — NEVER read either.
4. **`tools/audit/` is NOT pinned** by `INSTRUMENT.json`; new probe tooling there
   does not touch instrument identity. Pinned (do not edit):
   `datasets/public/*.jsonl`, `tasks/*.py`, `walkworthy_inspect/*.py`.
5. **Judge-prompt reuse:** `scorers.assemble_rubric_prompt` + `rubrics.py` are
   importable as plain Python without inspect_ai (pattern:
   `tools/audit/export_referee_prompts.py`). The OpenRouter REST + Ledger +
   calibration/projection machinery to copy is in
   `tools/audit/d02_davidson_bt_pilot.py` (`openrouter_call`, `call_cost`,
   `Ledger`). Credentials: `source ~/.codex/secrets/openrouter.env` (nothing
   auto-loads).
6. **Constant-harness argument (the probe's validity spine):** the CLI overhead
   is identical for all three tiers, so tier CONTRASTS are interpretable even
   though absolute levels are not comparable to the inspect_ai reference runs.
   Corollary: v4-T numbers must NEVER be pooled with reference-run numbers.
7. **d02 crux for context:** the two pinned judges are internally coherent but
   disagree at the construct level (per-response hold reads agree on 9 of 81
   cells). §4.7 criterion 4 checks whether that replicates on Claude tiers.

## 4. The task: v4-T tier probe (design is FIXED — do not re-litigate)

Known-groups validity probe: do d01/d05 items differentiate Haiku 4.5, Sonnet 5,
Opus 5 — a capability gradient known in advance? Informative either way: strong
differentiation supports item validity; weak differentiation on d05 (objective
scoring) vs d01 (judged scoring) localizes whether the weakness is in items or
judges.

1. **Harness:** new `tools/audit/tier_probe_claude_oauth.py`, porting the
   `CLIModelClient` pattern (fact 1). Before the first call, verify against the
   installed CLI (`claude -p --help`) that every hygiene flag still exists, and
   whether print mode supports `--system-prompt`. Item framing: use
   `--system-prompt <item system text>` if supported; otherwise prepend the
   framing to the user prompt under a fixed delimiter. Either way, record the
   mode in every ledger row and keep it CONSTANT for the entire run.
2. **Census:** (49 + 32) admin lines × 3 models × 2 epochs = **486 SUT calls**.
   Epochs are re-administrations at default temperature (no temperature control
   in the CLI — disclosed, not fixable). Modest parallelism (≤4 concurrent
   subprocesses); resume-safe append-only JSONL
   `logs/tier-probe-20260802/responses.jsonl`, key
   `(design, item, admin, model, epoch)`; a log root must never contain the
   substring "rescore". Holdout tripwire + canary check on every sample read.
   Record `.total_cost_usd` per call (informational — subscription). If the run
   must survive the session, use the nohup poll-loop daemon pattern with a DONE
   sentinel; otherwise in-session with resume safety is fine.
3. **Calibration micro-run first:** 1 d01 item + 1 d05 item × 3 models × 1 epoch
   = 6 calls. Confirms each pinned model id resolves, output JSON parses, d05
   allocation text parses, and projects wall-clock for 486 calls. STOP and
   report if any model id fails to resolve.
4. **d05 scoring ($0):** import the fact-3 entry points read-only; compute CSR
   per response. Mirror the instrument's format-retry convention: if the
   allocation does not parse, ONE re-administration with a format reminder
   appended; record `attempts`; still-unparseable → `unscorable`, never a crash.
5. **d01 judging ($1.00 hard):** assemble judge prompts offline via
   `assemble_rubric_prompt`; judge-A `openai/gpt-4.1-nano` + judge-B
   `meta-llama/llama-3.3-70b-instruct`, OpenRouter REST, temperature 0. Full
   judge census 294 responses × 2 judges = 588 calls. Run discipline copied from
   the d02 tool: calibration micro-run (one item's 6 responses × 2 judges = 12
   calls), measure `usage.cost`, project the 588; STOP and report if projection
   exceeds $1.00; hard stop at $1.00 actual; resume-safe JSONL under the same
   log root; one parse retry then unscorable.
6. **Score definitions (pre-committed):** d05 primary = `item_csr` CSR (0–1).
   d01 primary = binary match of judged `action_class` against the item's keyed
   class; d01 secondary = `rationale_quality` (0–2). Verify the exact keyed-class
   field location in the bank metadata before coding the match (do not guess);
   if no unambiguous keyed class exists for an item, exclude it from the primary
   and report the exclusion count.
7. **Report (new dated file `20260802c-…` or later letter; live report
   immutability rules) — pre-committed read-out criteria:**
   - Pooled tier contrast per design: Opus-minus-Haiku mean-score gap with an
     item-clustered bootstrap confidence interval; report whether the interval
     excludes zero. Same for Opus-minus-Sonnet and Sonnet-minus-Haiku
     (secondary).
   - Per-item discrimination: share of items with mean(Opus) > mean(Haiku);
     share strictly monotone Opus > Sonnet > Haiku. Disclose the coarseness of
     3-tier orderings (6 possible orderings per item).
   - d05 CSR by tier, plus parse-failure and refusal rates by tier.
   - d01 cross-judge agreement on the tier contrasts: design-level contrast SIGN
     agreement + item-level score correlation between judges — the
     out-of-sample check on the d02 construct-disagreement crux (fact 7).
   - Report which of d05 (objective) vs d01 (judged) shows the stronger
     gradient, and what that localizes.
   All numbers are probe diagnostics — never WALKWORTHY numbers; never pooled
   with inspect_ai reference runs; cross-family judges by design (no
   Claude-judging-Claude reads); the subscription-OAuth modest-scale caveat and
   the no-temperature-control limitation are disclosed in the report.

## 5. What a session may also do without a new ruling

- v4-A work per `-20260801a` RULING 1 — $0 strictly: candidate authoring, the
  two named code fixes (judge-B parse hardening; empty-completion exclusion),
  the anchored q2 definition, ranked-sacrifice scorer + tests. Instrument
  discipline: `WW-v2-20260731b` verify chain must stay green; anything that
  would break `verify_instrument.py` on the stamped tree needs its own ruling
  first (spec §5.1 — v4.0 is a NEW instrument id at freeze).
- Answer owner questions from committed artifacts; the §1 $0 checks; maintain
  the entry-point chain (new dated files only; dated files are immutable; the
  spec `20260731j` stays live-edit under version banners).
- Do NOT: launch B1/B2; touch holdout (never set WALKWORTHY_ALLOW_HOLDOUT);
  re-run the d02 re-pilot; exceed $1.00 on judging; scale the OAuth channel
  beyond the §4 census without a new ruling; re-litigate the `20260731k`/
  `20260731l`/`-20260801a` adjudications; pool v4-T numbers with reference
  runs; quote any diagnostic as a WALKWORTHY number.

## 6. Binding constraints (by reference, unchanged)

All of `20260731f` §5 and `20260801b` §6: $0 default; holdout CLOSED; report
immutability (successor files); no deletions (RECYCLE-BIN); explicit-path
commits, message via `git commit -F`, verify `git log -1 --stat`; canary
top+bottom; R3 linter (`REPORTS/20260725-manuscripts/lint_claims.py`, 0
blockers; a bold span must never end on a digit; no "significant" as adjective);
new-artifact gates (lint · canary ≥ 2 · pytest 115 if code touched ·
verify_instrument only if pinned components touched, which needs a ruling
first); deletion-guard and exec-token hook sharp edges; probe numbers are
diagnostics only.

## 7. Where things live

| Artifact | Path |
|---|---|
| Rulings ledger (newest wins) | `$V2/RULINGS-APPLIED-*.md` through `-20260802a.md` |
| OAuth channel to port | `COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS/wcfbench/cli_client.py` (+ `04-HARNESS/tests/test_cli_client.py` for the hermetic subprocess-mock test pattern) |
| Bank files (read-only) | `$V2/datasets/public/design01.jsonl`, `design05.jsonl` |
| d05 scoring entry points | `$V2/walkworthy_inspect/parsers.py`, `ordo_constraints.py` (import, never edit) |
| Judge prompt assembly | `$V2/walkworthy_inspect/scorers.py` (`assemble_rubric_prompt`) + `rubrics.py`; offline pattern `$V2/tools/audit/export_referee_prompts.py` |
| OpenRouter + Ledger machinery to copy | `$V2/tools/audit/d02_davidson_bt_pilot.py` |
| d02 discharge record | `$V2/20260801c-d02-hardened-repilot-report.md` (+ run tree, gitignored: `logs/d02-btpilot2-20260801/`) |
| Spec (live, v0.4 ratified) | `$V2/20260731j-walkworthy-v4-design-spec.md` |
| Reading order, recent chain | `20260731o` → `-20260801a` → `20260801b` → `20260801c` → `-20260802a` → this file |
| Prior entry points (still valid for their facts) | `20260801b` (d02 re-pilot + v4-A), `20260731m` (v4 program), `20260731f` (v3 record) |

---

**If you are unsure whether something is authorized: it is not.** This session's
spend-bearing block is the §4.5 judging at $1.00; SUT administration is
subscription OAuth at the §4 census exactly; v4-A is open at $0; everything else
waits for the owner.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
