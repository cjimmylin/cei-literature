# BOOT PROMPT — v4-A authoring remainder ($0 strictly) · owner decision points pending

Read this at the start of a fresh session. Self-contained: a session with zero
prior context can act correctly from it. Authored 2026-08-06, after the v4-A
execution session of 2026-08-02 (commits `13681e993` → `2c67334cb`).

**Supersedes `20260802d-boot-prompt-v4a-execution.md` as the entry point.**
Nothing there is retracted; its facts remain valid by reference. What changed
since: v4-A code deliverables 2(a)–2(d) EXECUTED, the anchored q2 definition
SHIPPED, and the d05 hardened expansion EXECUTED (38 items landed,
double-keyed, adjudicated). Do NOT re-do any of those.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.
`$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`

**SPEND POSTURE: $0 STRICTLY. The remaining v4-A work
(`RULINGS-APPLIED-20260801a` RULING 1) is authoring + offline validation with
NO model calls and NO piloting. There is no open spend authorization of any
size. Anything spend-bearing — any pilot of new items, any judge run, any OAuth
SUT call, B1/B2 — needs a new ruling first.**

---

## 1. Verify state before acting (30 seconds, do not skip)

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
git fetch origin && git log --oneline -6 -- COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/
ls -1 COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/RULINGS-APPLIED-*.md | tail -3
cd COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2
./.venv/bin/python -m pytest -q                    # 178 passed
./.venv/bin/python tools/verify_instrument.py      # ALL PASS 51/51 (WW-v2-20260731b)
./.venv/bin/python tools/authoring/validate_v4_banks.py --bank datasets/v4/public/design05.jsonl --stage final            # 30 lines ALL PASS
./.venv/bin/python tools/authoring/validate_v4_banks.py --bank datasets/v4/holdout/design05.jsonl --stage final --holdout # 8 lines ALL PASS
```

State at authoring: newest ruling `RULINGS-APPLIED-20260802a`; newest commit
`2c67334cb` (d05 banks + report `20260802g`). **If a `RULINGS-APPLIED-*` newer
than `-20260802a` exists, read it FIRST — it wins over this file.** Sibling
WCF-Benchmark-v2 is worked by other sessions in this clone; expect unrelated
dirty files.

## 2. What the 2026-08-02 session DID (do not re-derive or re-do)

1. **Code 2(a)–2(d) DONE** (`13681e993`; suite 115 → 178; pinned tree
   untouched): judge-B parse hardening with format-reminder retries + the
   ≥ 0.85 retention report in `tools/rescore/rescore.py` (same-prompt retry is
   PROVEN insufficient — regression fixture
   `tests/fixtures/judgeB_degenerate_20260802.jsonl`); empty/truncated-
   completion exclusion BOTH halves (`walkworthy_v4/completion_guard.py`,
   wired into all three rescore paths + the one-shot cap-escalation policy);
   ranked-sacrifice scorer (`walkworthy_v4/ranked_sacrifice.py`);
   complete-case + norming module (`walkworthy_v4/norming.py`).
   **Consequence: B1's two code prerequisites are CLEARED** (20260731o §7).
2. **Anchored q2 definition SHIPPED** (`55863df37`,
   `20260802e-d07-anchored-q2-definition.md`): decision rule + exemplar
   anchors + drop-in judge block. **RULING 2's condition is satisfied → d07
   candidate drafting is UNBLOCKED** (ordering-level reads only until B1).
3. **d05 hardened expansion EXECUTED** (`2a4e473aa`…`2c67334cb`): 30 public
   items in `datasets/v4/public/design05.jsonl` + 8 holdout in
   `datasets/v4/holdout/design05.jsonl` (quarantined at creation; never read
   them). WW-05-H01/M01 retired by supersession. Double-keying disagreement
   DISCLOSED in report `20260802g` §4 (public first-sacrifice agreement 0.667;
   holdout 0.375). Evidence record + construct findings: `20260802g`.

## 3. Facts not to re-derive (paid for on 2026-08-02)

1. **The reusable authoring pipeline** (all in `tools/authoring/`):
   `validate_v4_banks.py` (draft/final stages) → `build_keying_packets.py`
   (stripped blind-keying packets) → blind second keyers (fresh-context opus
   agents, anti-leakage protocol) → fresh adjudicators → `assemble_v4_d05.py`.
   Reuse for the remaining designs with a rubric-keying variant.
2. **Three mechanized defect classes** (validator enforces; do not relearn):
   escaped-keyed-first (breaks the ranked-sacrifice primary), arithmetic-gift
   exact-fit floor subsets (incl. escaped floors), key-order disclosure in
   constraint text (defeats blind keying — one keying round had to be
   discarded and re-fired). Agent self-reports of compliance are NOT evidence;
   only validator output is.
3. **Construct findings awaiting freeze review** (`20260802g` §5, owner-
   relevant, nothing ruled): remedy-escape vs scorability collision (adopted
   convention: alternative in scenario prose, keyed clause hard, escapes
   mid-order); hard-slot-0 adjudication asymmetry (favors author1 — read
   disagreement rates accordingly); guard-ordinal convention SPLIT between
   adjudication batches (A/C terminal vs B penultimate) — harmonize or accept
   at freeze.
4. **v4-T facts that still bear on authoring** (`20260802c`): d05 v3 public
   bank at CEILING (CSR 0.91–0.93) — the new banks aim above it; the d02
   construct-disagreement crux REPLICATED on d01 (judge choice is the binding
   measurement risk — owner decision, not a session's).
5. Bank/scoring entry points (read-only imports, never edit):
   `walkworthy_inspect/parsers.py`, `ordo_constraints.py`, `scorers.py`,
   `rubrics.py`. d05 allocation spec at `metadata.keyed.extras.allocation`.
   `tools/`, `walkworthy_v4/`, `datasets/v4/` are NOT pinned; `datasets/public/`,
   `datasets/holdout/`, `tasks/`, `walkworthy_inspect/` ARE pinned.

## 4. The task: v4-A authoring remainder (scope FIXED by `-20260801a` RULING 1.1)

Work order (any sub-block can be its own session; each dimension reserves
~20 pct holdout QUARANTINED AT CREATION; rejected items recorded, never
deleted; canary on every public line; new files under `datasets/v4/` only):

1. **d04 (P-MOTIVE) REBUILD to n = 40** under spec `20260731j` §2.3: α/β motive
   twins with cue strength EXCEEDING WW-04-I02 (which FAILED: judge-A mean
   delta −0.096); pair gate = bold `Shared` / `α cue` / `β cue` fields (absence
   of any one silently routes to single administration); keyed direction = the
   literal substring "delta > 0" in the keyed text; double-hazard construction.
2. **d03 (P-FAITHFULNESS) REBUILD to n ≥ 16** under §2.3 judged-item rules
   (double-hazard: keyed standard threatened from two directions, so neither
   blanket compliance nor blanket refusal scores).
3. **d08 (P-GUARDRAIL) + d10 (P-DESERVINGNESS) admitted-axis expansion** —
   these two ONLY; **d06 (P-PROCESS) is DEFERRED**. Note v4-C: d08's variance
   share sat below the df-null line (weakest candidate) and its apparent judge
   disagreement was manufactured by empty completions (now excluded by 2(b)) —
   author accordingly.
4. **d07 (P-COUNSEL) candidate drafting is now PERMITTED** (q2 anchor exists —
   author new items against `20260802e`'s q2 boundary from the start). Rubric
   stays ordering-level-only until q2 determinacy is demonstrated at B1.
5. Adapt the d05 pipeline per design: judged-item designs need a rubric-keying
   variant of the packet/double-key steps (key = judged rubric anchors rather
   than a sacrifice order); build the analogous validator checks BEFORE
   dispatching drafters — mechanical rules in code, not in prompts.
6. When building any v4 loader: wire `datasets/v4/holdout/` into the
   `WALKWORTHY_ALLOW_HOLDOUT` guard (same discipline as `datasets/holdout/`).

Deliverable hygiene: new dated files only; R3 linter on any new report
(`REPORTS/20260725-manuscripts/lint_claims.py`, 0 blockers); canary top+bottom;
pytest green before any commit; explicit-path commits, message via
`git commit -F <file>`, verify `git log -1 --stat`, then push.

## 5. Pending OWNER decisions (present when asked; do NOT act on them)

1. **B1+B2 scale (~$180–230)**: both code prerequisites now CLEARED; the
   decision returns to the owner with reports `20260731o` §7 and `20260802g`.
2. **Judging architecture**: the d02 construct-disagreement crux replicated on
   d01 (`20260802c` §5) — judge choice is the binding measurement risk. No
   unilateral judge swaps.
3. **P-PRESSURE (d02) v4.0 scope**: with the owner (both d02 pilots in hand).
4. **Freeze-review items from `20260802g` §5**: remedy-escape convention,
   guard-ordinal convention split, hard-slot-0 asymmetry; plus escape-coverage
   balance across the d05 bank if the rationale judge needs it.
5. P-COMMITMENT stays NOT ADVANCED (`-20260801a` RULING 3); revival needs a new
   ruling.

## 6. What a session may also do without a new ruling

- The §1 $0 checks; answer owner questions from committed artifacts
  (`20260802g` for the d05 authoring; `20260802c` tier probe; `20260801c` d02
  re-pilot; `20260731o` v4-C).
- Do NOT: make any model call (SUT/judge); launch B1/B2; read holdout (never
  set WALKWORTHY_ALLOW_HOLDOUT — includes `datasets/v4/holdout/`); edit pinned
  components; re-litigate the `-20260801a`/`-20260802a` adjudications; pool
  probe diagnostics with reference runs; quote any probe diagnostic as a
  WALKWORTHY number.

## 7. Binding constraints (by reference, unchanged)

All of `20260731f` §5 and `20260801b` §6: $0 default; holdout CLOSED; report
immutability (successor files); no deletions (RECYCLE-BIN); explicit-path
commits via `git commit -F`; canary top+bottom; R3 linter (0 blockers; a bold
span must never end on a digit; no "significant" as adjective); new-artifact
gates (lint · canary ≥ 2 · pytest if code touched · verify_instrument only if
pinned components touched, which needs a ruling first); deletion-guard and
exec-token hook sharp edges; parallel comparison dispatches follow the
anti-leakage skill (stripped packets, fresh contexts, attestations).

## 8. Where things live

| Artifact | Path |
|---|---|
| Rulings ledger (newest wins) | `$V2/RULINGS-APPLIED-*.md` through `-20260802a.md` |
| v4-A scope (authoritative) | `$V2/RULINGS-APPLIED-20260801a.md` RULING 1 |
| Spec (live, v0.4 ratified) | `$V2/20260731j-walkworthy-v4-design-spec.md` (§2.2, §2.3, §3, §5.1) |
| d05 authoring record + construct findings | `$V2/20260802g-d05-hardened-authoring-report.md` |
| d05 authoring spec (+ v1.1 addendum) | `$V2/20260802f-d05-hardened-authoring-spec.md` |
| q2 anchor (binding for d07 drafting) | `$V2/20260802e-d07-anchored-q2-definition.md` |
| v4 banks (landed) | `$V2/datasets/v4/public/design05.jsonl` · `$V2/datasets/v4/holdout/design05.jsonl` (quarantined) |
| Authoring pipeline | `$V2/tools/authoring/{validate_v4_banks,build_keying_packets,assemble_v4_d05}.py` |
| v4.0-line code | `$V2/walkworthy_v4/{completion_guard,ranked_sacrifice,norming}.py` |
| Reading order, recent chain | `20260731o` → `-20260801a` → `20260801c` → `-20260802a` → `20260802c` → `20260802d` → `20260802e/f/g` → this file |

---

**If you are unsure whether something is authorized: it is not.** This session
line is $0 strictly: authoring + offline validation only; every model call,
pilot, or scale decision waits for the owner.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
