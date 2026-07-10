# Vault Housekeeping — PNG Cleanup & Screenshot Convention
**Session date:** 2026-03-29
**Type:** Vault-level housekeeping (applies to all sub-projects)

---

## What happened this session

### Problem
23 PNG screenshot files had accumulated at the vault root (`/CEI-Literature-Vault/*.png`). The vault root is supposed to contain only the authorized sub-project directories and a small number of config files (see `CLAUDE.md` Critical Safety Rules).

### Root cause
Previous development sessions (dashboard verification with Playwright, UMAP/NMF analysis, ontology/genome tab checks) saved screenshots to the working directory without routing to a sub-project. No explicit rule existed for where PNGs belong.

---

## Changes made

### 1. Files moved
**21 files → `CEI-AI-Statements-v2/screenshots/`** (created new dir):
```
corr-fa-tab.png
cv-tab.png
explorer-tab-verification.png
genome-explorer-map.png
genome-explorer-table.png
genome-explorer-temporal.png
genome-umap-debug.png
genome-umap-v2.png
genome-v2-enforcement.png
genome-v2-findings-fixed.png
genome-v2-overview.png
genome-v2-policymap.png
genome-v2-policymap2.png
nmf-sfa-components.png
nmf-sfa-cv.png
nmf-sfa-tab-overview.png
nmf-tab.png
noc2b-subtab-verification.png
ontology-v2-tab0-overview.png
ontology-v2-tab4-network.png
overview-tab.png
```

**1 file → `CEI-Lit-WS/screenshots/`** (created new dir):
```
lit.png
```

### 2. CLAUDE.md updated
Added screenshot placement rule to the **Naming Conventions** section:
```
- Screenshots/PNGs: `{sub-project}/screenshots/descriptive-name.png` — NEVER at vault root
  - Papers vault screenshots → CEI-Lit-WS/screenshots/
  - Tapestry/genome/ontology/taxonomy screenshots → CEI-AI-Statements-v2/screenshots/
```

### 3. Memory updated
`memory/feedback_vault_root_placement.md` routing guide updated — the old entry ("Dashboard screenshots → inside the relevant dashboard dir") was replaced with explicit paths:
```
Screenshots/PNGs → CEI-AI-Statements-v2/screenshots/ for Tapestry/genome/ontology/taxonomy work;
                   CEI-Lit-WS/screenshots/ for papers vault work. NEVER at vault root.
```

---

## New screenshot convention (going forward)

| Context | Save to |
|---------|---------|
| Playwright dashboard verification (Tapestry, genome, ontology, taxonomy) | `CEI-AI-Statements-v2/screenshots/` |
| UMAP/NMF/analysis plots for Tapestry work | `CEI-AI-Statements-v2/screenshots/` |
| Papers vault dashboard verification | `CEI-Lit-WS/screenshots/` |
| EthicsMosaic work | `EthicsMosaic/screenshots/` (create if needed) |

**Naming:** use descriptive kebab-case names, e.g. `genome-v2-overview.png`, `noc2b-subtab-verification.png`.

---

## Vault root status
No PNG files remain at vault root. The vault root is clean.

---

## No open tasks
This was a self-contained housekeeping session. No follow-up work is required.
