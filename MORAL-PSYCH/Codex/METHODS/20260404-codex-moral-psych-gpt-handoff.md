# Codex Handoff: MORAL-PSYCH GPT Replication

**Date:** 2026-04-04
**Scope:** Replicate the 23 MORAL-PSYCH benchmarks in Codex with the current GPT model
**Model label:** gpt-5-codex
**Status:** Trial outputs and GPT summary generated under `CEI-Lit-WS/MORAL-PSYCH/Codex/`

## Constraints Followed

- No existing files were changed.
- All new artifacts were written only under `MORAL-PSYCH/Codex/`.
- No SDK or API was used; outputs were generated in the Codex agent session itself.

## Method

Each existing Opus trial JSON in `MORAL-PSYCH/TRIALS/` was used as the benchmark template and item source of truth. The Codex/GPT pass preserved benchmark IDs, item structure, and score field names so the new files can be compared later without modifying the existing dashboard or analysis stack.

## Deliverables

- `Codex/TRIALS/20260404-trial-*-gpt.json` (23 files)
- `Codex/TRIALS/20260404-trials-summary-gpt.json`
- `Codex/METHODS/20260404-codex-moral-psych-gpt-handoff.md`
- `Codex/MANIFEST.json`
