# 10CBench Current State

**Updated:** 2026-07-11

## Operational state

**Goal:** Finish ZEROSUM, SKIM, PALTER, TABLETS, and SOVEREIGN as reproducible, resumable OpenRouter benchmarks, validate first with cheap models, and freeze exact later scale-up commands.

**Current benchmark:** PALTER

**Current milestone:** Review and integrate the credential-free PALTER Phase 1 bank/BT contract and shared OpenRouter core, then complete PALTER's mechanical scorer, audits, synthetic validation, cheap smoke, and resumable diagnostic.

**Last completed milestone:** SKIM engineering closeout — the staged `feat(skim): close cheap provider-limited diagnostic` commit.

**Latest verified artifact:** SKIM provider-limited diagnostic snapshot, SHA-256 `47a2e5166b6e83414029f72e7054dfa80c813e83cd660b0ebc2637e49e93e8d9`. It is explicitly incomplete, resumable, and ineligible for empirical decisions.

## Preserved SKIM run

2,002 of 2,400 schedule rows are hash-chained and preserved: 1,983 valid terminal rows and 19 parked rows. The first two cheap models are complete at 800/800 each; the cheap Mistral diagnostic is at 402/800 and remains resumable at schedule index 2002. Spend is `$0.032953218` across 2,032 paid-call equivalents under the `$1.00` hard cap.

The cheap Mistral/DeepInfra endpoint repeatedly returned HTTP 429 after 5- and 15-minute cooldowns. The run was closed as provider-limited rather than cycling for hours. Its checkpoint/event evidence is preserved locally and in the hash-bound archive; it can be resumed later without substituting the frozen model/provider pair.

## PALTER entry state

Credential-free Phase 1 is present but not yet committed:

- 40 deterministic cores and 240 aligned public/private/runtime records;
- 20-composition blinded BT packet, four compositions per family;
- BT import remains fail-closed until at least 12 complete readers/composition, at least two named judge families, and Spearman `>= 0.6` in every family;
- human BT, editorial band certification, and PR-claim authorization remain `NOT_RUN`;
- 23 focused tests and compile validation passed before integration review.

The benchmark-neutral OpenRouter core is also present but uncommitted. Its 34 tests plus 171 shared-custody tests passed. It has not made any network or paid calls.

**Exact next command:**

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python -m pytest -q \
  TENCOMMANDMENTS/harness/openrouter/tests \
  TENCOMMANDMENTS/harness/custody_stack/tests/test_custody_stack.py \
  TENCOMMANDMENTS-v2/DESIGNS/09-palter/tests
```

Run from `COOKBOOK/40-BIBLEBENCH` in the active worktree.

## Acceptance criteria for the current milestone

- PALTER bank/gold/runtime counts, hashes, public/private separation, and BT sample balance replay exactly.
- Lies route to LY before PR scoring; PR remains excess over the no-incentive twin; two-sided bands and the material-harm floor are mechanical.
- BT cannot become `PASS` from incomplete, synthetic, single-family, or under-reader evidence.
- Shared transport remains benchmark-neutral, provider-pinned, fail-closed on cost, 429-only retry, and hash-chain resumable.
- Credential-free schema, leakage, replay, lexical/length, and cost preflight pass.
- Synthetic full-schedule validation completes without external calls and cannot authorize empirical claims.
- A small cheap-model smoke completes before any larger cheap diagnostic; no expensive model is called.
- Exact smoke, resume, analysis, and non-executed scale-preflight commands are documented.
- The PALTER suite runs once before its commit.

## External blockers and boundaries

No blocker prevents PALTER engineering work or a cheap transport smoke. The human belief-transfer study is `NOT_RUN` and blocks PR claims, the full BT-authorized diagnostic, and publication claims; it must never be fabricated or bypassed. The official/larger model roster and its spend ceiling remain unfrozen and must not be executed.

## Deferred publication-only work

- PALTER human BT study and editorial probe-band certification.
- Professional/human baselines and official multi-seed evidence across benchmarks.
- Real-LLM 10% fine-tune probes and frozen external capability PC1 evidence.
- SKIM's remaining 398 cheap Mistral rows unless a later resume is operationally useful.
- Any hardening without a demonstrated false-pass, leakage, duplicate-call, scoring, or bank-identity risk.

**Next benchmarks:** TABLETS, then SOVEREIGN.

**Re-entry file:** `TENCOMMANDMENTS-REVIEWS/20260706-PARKED-opus-reentry-prompt.md`
