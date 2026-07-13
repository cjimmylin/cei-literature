# BibleBench Paper Lane Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a source-verified, venue-neutral BibleBench design-and-methods manuscript with reproducibility, ethics, limitations, and data-card appendices while preserving the pre-empirical claim boundary.

**Architecture:** `manuscript.md` is the canonical paper source and `references.bib` is its only external bibliography. Focused appendices live beside the manuscript and are checked by existing paper-artifact tests plus new citation-integrity tests. Repository records remain design provenance and are not presented as external scholarship.

**Tech Stack:** Markdown, BibTeX, Python 3.11+, pytest, standard library.

---

### Task 1: Lock the citation and manuscript contracts

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_paper_artifacts.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_manuscript_readiness.py`

- [ ] **Step 1: Write failing contract tests**

Add tests that extract `[@key]` and `[@key; @key]` citations, require every key in `references.bib`, require DOI/URL/eprint for every external entry, require the sections `Related Work`, `Construct and Theological Frame`, `MVP Protocol`, `Planned Analysis`, `Ethics`, `Limitations`, `Results`, and `Discussion`, and assert exactly one `PENDING_EMPIRICAL_RUN` occurrence. Use this concrete core:

```python
def test_manuscript_has_one_empirical_sentinel(paper_root: Path) -> None:
    text = (paper_root / "manuscript.md").read_text(encoding="utf-8")
    assert text.count("PENDING_EMPIRICAL_RUN") == 1

def test_external_bib_entries_have_stable_identifier(paper_root: Path) -> None:
    bib = (paper_root / "references.bib").read_text(encoding="utf-8")
    for entry in split_bib_entries(bib):
        if "localprovenance = {true}" not in entry.lower():
            assert any(field in entry.lower() for field in ("doi =", "url =", "eprint ="))
```

- [ ] **Step 2: Run the focused tests and verify failure**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_manuscript_readiness.py tests/test_paper_artifacts.py -q`

Expected: FAIL because external scholarship and the submission-shaped section contract are incomplete.

- [ ] **Step 3: Keep the test parser narrow and deterministic**

Implement only the BibTeX splitting and citation-key extraction needed by the repository's current syntax. Reject duplicate keys, unresolved keys, and citation-like tokens that are not bibliography references.

- [ ] **Step 4: Re-run to confirm only content failures remain**

Run the command from Step 2. Expected: tests execute deterministically and fail on missing manuscript/bibliography content, not parser errors.

### Task 2: Verify sources and write Related Work

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/references.bib`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/manuscript.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/SOURCE-VERIFICATION.md`

- [ ] **Step 1: Verify primary sources**

Use publisher, proceedings, DOI, or arXiv primary pages to verify at least two sources in each of these five groups: behavioral/agentic evaluation; stated versus enacted values; LLM-as-judge and human adjudication; construct validity/psychometrics; and Christian/biblical AI ethics or digital theology. Record title, authors, year, stable identifier, verification URL, and manuscript use in `SOURCE-VERIFICATION.md`. Do not cite search-result pages, blog summaries, or repository handoffs as external scholarship.

- [ ] **Step 2: Add complete BibTeX records**

Every new key must have exact author/title/year plus one stable `doi`, `url`, or `eprint`. Preserve existing local records and mark them `localprovenance = {true}`.

- [ ] **Step 3: Replace the incomplete Related Work scaffold**

Write a synthesis organized around the five source groups. Explicitly distinguish observable behavior from value self-description, automated judging from founding human gold, and construct coverage from model ranking. Avoid novelty, consensus, superiority, and performance claims.

- [ ] **Step 4: Run citation tests**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_manuscript_readiness.py tests/test_paper_artifacts.py -q`

Expected: all citation-resolution and stable-identifier tests PASS.

### Task 3: Align the manuscript with PF-002

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/manuscript.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/claims-registry.yaml`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/limitations-register.md`

- [ ] **Step 1: Replace superseded pilot geometry**

The manuscript must state exactly three inexpensive general-purpose models, 48 episodes, one C1 primary plus one matched probe, and 288 logical calls. Remove the superseded four-model/C0-C1-C2 language from the active MVP protocol while retaining it only where clearly labeled as deferred design history.

- [ ] **Step 2: Enforce the claims boundary**

Register only descriptive, exploratory claims. Explicitly exclude leaderboards, best-model claims, composites, family-level estimates, cue effects, capability-adjusted attribution, and Christian-consensus claims.

- [ ] **Step 3: Update Results and Discussion scaffolds**

Keep exactly one Results sentinel and provide prose slots for completion/missingness, module-native vectors, strata, action/probe consistency, red lines, and judge confidence. The Discussion scaffold must separate findings, alternative explanations, theological scope, and future multi-judge validation.

- [ ] **Step 4: Run focused tests**

Run the Task 2 test command. Expected: PASS.

### Task 4: Add appendices and finish the paper lane

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/appendix-reproducibility.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/appendix-ethics.md`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PAPER/appendix-data-card.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_manuscript_readiness.py`

- [ ] **Step 1: Add appendix contract tests**

Require reproducibility hashes/environment/custody/freeze steps; ethics scope/risks/mitigations/authority boundaries; and data-card motivation/composition/collection/annotation/intended-use/out-of-scope/maintenance fields.

- [ ] **Step 2: Write the three appendices**

Use only current repository facts. State that model evidence, multi-judge validation, and final gold do not yet exist. Include no credentials, private repeat mapping, or suggested human judgments.

- [ ] **Step 3: Run the paper test set**

Run: `cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT && /opt/homebrew/bin/python3 -m pytest tests/test_manuscript_readiness.py tests/test_paper_artifacts.py tests/test_methods_pdf.py -q`

Expected: PASS.

- [ ] **Step 4: Commit the lane**

Run `git log -1 --oneline`, path-stage only the paper files and the two test files, then commit with `BibleBench: prepare submission-shaped design manuscript`.
