# Codex GPT-5.4 Trial Replication

This folder contains Codex-authored GPT trial outputs for the cross-cultural benchmark corpus in `CULTURAL-GLOBAL/TRIALS/`.

Method:
- Source templates were the existing Opus trial JSON files.
- No SDK or API was used.
- The agent itself generated the GPT-5.4 outputs offline within this session.
- No existing files outside this folder were modified.

Artifacts:
- `generate_gpt54_trials.py`: Codex-local generator used for this run
- `manifest.json`: output inventory
- `20260404-trial-CC*-gpt54.json`: GPT-5.4 trial files

Notes:
- Filenames preserve the `20260404` cohort date to align with the existing benchmark run set.
- The top-level `model` field is `gpt-5.4`.
- The outputs are intentionally isolated from the existing validation, analysis, and dashboard pipeline.
