# Codex Handoff: MORAL-PSYCH GPT Mini Replication

**Date:** 2026-04-04
**Scope:** Replicate the 23 MORAL-PSYCH benchmarks in Codex with the mini model
**Model label:** gpt-mini
**Status:** Trial outputs and GPT mini summary generated under `CEI-Lit-WS/MORAL-PSYCH/Codex-mini/`

## Constraints Followed

- No existing files were changed.
- All new artifacts were written only under `MORAL-PSYCH/Codex-mini/`.
- No SDK or API was used; outputs were generated in the Codex agent session itself.

## Method

Each existing Opus trial JSON in `MORAL-PSYCH/TRIALS/` was used as the benchmark template and item source of truth. The Codex/GPT mini pass preserved benchmark IDs, item structure, and score field names so the new files can be compared later without modifying the existing dashboard or analysis stack.

## Deliverables

- `Codex-mini/TRIALS/20260404-trial-*-gpt-mini.json` (23 files)
- `Codex-mini/TRIALS/20260404-trials-summary-gpt-mini.json`
- `Codex-mini/METHODS/20260404-codex-moral-psych-gpt-mini-handoff.md`
- `Codex-mini/MANIFEST.json`
