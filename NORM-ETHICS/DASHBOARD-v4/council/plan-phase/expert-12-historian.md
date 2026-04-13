# Expert 12 — Meta-Critique / Project Historian

**Perspective:** Safety-rule compliance and project-history continuity
**Scope:** Does Dashboard v4 respect all CLAUDE.md safety rules and preserve v1-v3 unchanged?

---

## (a) Rule 3 — Report Immutability

**Status: PASS**

Rule 3 states: "NEVER overwrite or regenerate existing reports. Old reports are historical snapshots. Always create NEW reports with NEW YYYYMMDD- date prefixes."

Dashboard v4 is housed in a new directory (`DASHBOARD-v4/`) that is structurally separate from `DASHBOARD/` (v1) and `DASHBOARD-v2/`. The CONTRACT.md Section 10 explicitly states: "v1, v2, v3 dashboards are frozen. Do not merge v4 changes into their repos." and "DASHBOARD-v2/ source directory is frozen per CLAUDE.md Rule 3." This is the correct approach — new version, new directory, no overwrites.

One observation: there is no `DASHBOARD-v3/` directory on disk. The briefing and contract reference v3 as a frozen public repo (`cei-normeval-dashboard-v3`) but the local source directory either never existed or was deployed directly from v2 sources. This is not a violation, but the contract should clarify where v3 source lives to prevent future confusion. If v3 was a deploy-only version (no local source directory), that should be documented.

## (b) Rule 1 — No Deletions

**Status: PASS**

Rule 1 states: "NEVER use rm, unlink, or any delete command. Always mv to RECYCLE-BIN/."

The v4 contract does not instruct deletion of any files. Both `DASHBOARD/` (v1) and `DASHBOARD-v2/` remain intact on disk with their full file sets (app.js, charts.js, data.js, data_cross_vendor.js, index.html, etc.). The contract's Section 10 immutability clause provides the correct guard. No v2 files are missing or at risk.

The deploy allowlist (Section 9) uses an inclusion model ("files that go into deploy/") rather than a deletion model, which is the safe pattern. Working files (council/, CONTRACT.md, generator scripts, logs, screenshots, tests) are excluded from deploy but remain in the source directory.

## (c) Deploy Allowlist — Working File Leakage

**Status: PASS with one minor note**

The Section 9 allowlist permits: `index.html`, `data.js`, `data_cross_vendor.js`, `charts.js`, `app.js`, `style.css`, `fonts/`, `LICENSE`, `NOTICE`, `README.md`.

The exclusion clause explicitly blocks: `council/`, `CONTRACT.md`, `generate_dashboard_v4.py`, `*.log`, `screenshots/`, `test_*.py`, `*.md` (except README.md).

This is correctly configured. No generator scripts, council deliberations, test files, or internal documentation will leak to the public GitHub Pages deployment. The `NOTICE` file (likely containing attribution/license info) is appropriate for public deployment.

One minor note: the exclusion uses `*.md (except README.md)` — this implicitly covers `CONTRACT.md` already, so the explicit mention of `CONTRACT.md` is redundant but not harmful. More importantly, any future `.json` data files, `.py` utility scripts, or `.sh` test scripts added to the v4 directory would need to be explicitly excluded. The current pattern is safe but relies on developer discipline for new file types. A stronger pattern would be: "deploy ONLY the allowlisted files; everything else is excluded by default."

## (d) Naming Conventions

**Status: PASS**

The CLAUDE.md naming conventions require:
- Reports/logs use `YYYYMMDD-descriptive-name.{md,json,html}` prefixes
- No files at vault root
- Screenshots go in `{sub-project}/screenshots/`

Dashboard v4 correctly lives under `CEI-Lit-WS/NORM-ETHICS/DASHBOARD-v4/` — no files at vault root. The `screenshots/` subdirectory exists within the dashboard directory, matching the convention. Council plan files use the pattern `expert-NN-{perspective}.md` as specified in the briefing's output paths section.

The CONTRACT.md itself does not carry a `YYYYMMDD-` prefix, but it is a living configuration document (akin to CLAUDE.md), not a report or log. This is acceptable — Rule 4 requires date prefixes specifically for files in `STATISTICS/` and `logs/`.

## (e) Frozen Repo References

**Status: PASS with one gap**

CONTRACT.md Section 10 references: "Public repos `cjimmylin/cei-normeval-dashboard{,-v2,-v3}` are never modified."

This correctly identifies three frozen repositories:
1. `cjimmylin/cei-normeval-dashboard` (v1)
2. `cjimmylin/cei-normeval-dashboard-v2`
3. `cjimmylin/cei-normeval-dashboard-v3`

The gap: the contract does not specify the v4 target repo name. Based on the project's naming pattern, it should be `cjimmylin/cei-normeval-dashboard-v4`, but this is not pinned anywhere in the contract. The briefing says "add v4 once deployed" for URLs but does not specify the repo name. This should be added to the contract before deployment to prevent ad-hoc naming.

## Summary of Findings

| Check | Verdict | Notes |
|-------|---------|-------|
| Rule 3 (immutability) | PASS | New directory, explicit freeze clause |
| Rule 1 (no deletions) | PASS | Inclusion-based deploy, no rm instructions |
| Deploy allowlist | PASS | Working files correctly excluded |
| Naming conventions | PASS | Correct directory nesting, no vault-root files |
| Frozen repo references | PASS | All three repos named; v4 target repo not yet pinned |

## Recommendations

1. **Pin the v4 deploy repo name** in CONTRACT.md Section 10 (e.g., `cjimmylin/cei-normeval-dashboard-v4`) to prevent naming drift.
2. **Clarify v3 source provenance** — document whether v3 had a local `DASHBOARD-v3/` source directory or was deployed directly from modified v2 sources. This matters for historical traceability.
3. **Strengthen the deploy allowlist** to use an explicit "allowlist-only" model rather than a blocklist pattern, so new file types added later cannot accidentally leak.
4. **Add a RECYCLE-BIN reminder** to the contract — if any v4 files need to be retired during development, they must be moved to RECYCLE-BIN per Rule 1, not deleted.

No safety violations detected. The v4 contract is well-constructed and respects all four critical safety rules from the root CLAUDE.md.
