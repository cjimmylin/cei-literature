# BibleBench Paper-First Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make paper-first progress the binding, visible, and auditable default for every current and future benchmark under `COOKBOOK/40-BIBLEBENCH/`.

**Architecture:** A top-level charter supplies the policy, inherited agent instructions enforce it, a living critical-path register supplies benchmark contracts, and a self-contained dashboard exposes progress and drift. Templates and an append-only decision log make the workflow repeatable without rewriting historical handoffs. Existing benchmark dashboards remain locally authoritative and receive only additive links to the portfolio surface.

**Tech Stack:** Markdown, self-contained HTML/CSS, Git path-scoped staging, shell and Python standard-library validation.

---

## File map

| Path | Responsibility |
|---|---|
| `PAPER-FIRST-WORKFLOW.md` | Binding portfolio policy and stopping rules |
| `AGENTS.md` | Automatically loaded session obligations and precedence |
| `ACTIVE-CRITICAL-PATHS.md` | Living benchmark-specific contracts |
| `PAPER-FIRST-DECISIONS.md` | Append-only owner exceptions and workflow rulings |
| `templates/PAPER-CRITICAL-PATH-CONTRACT.md` | Reusable contract template |
| `templates/SESSION-OPEN-CLOSE.md` | Reusable session checklist and report |
| `project-dashboard.html` | Offline portfolio status and drift display |
| `Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html` | Additive portfolio link; preserve concurrent edits |
| `WCF-Benchmark/project-dashboard.html` | Additive portfolio link; preserve local structure |

The living register is the portfolio's current execution surface. Dated handoffs remain immutable, and future handoffs copy the applicable contract fields from the register.

### Task 1: Establish a conflict-safe baseline

**Files:**
- Inspect: `Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html`
- Inspect: `Christian-Ethics-Benchmark/AGENTS.md`
- Inspect: `WCF-Benchmark/project-dashboard.html`
- Inspect: `WCF-Benchmark/AGENTS.md`
- Inspect: `CORINTHLOVE/STATUS.md`

- [ ] **Step 1: Record the workspace state without changing it**

```bash
git status --short
git diff --name-only
git diff --cached --name-only
```

Expected: pre-existing changes may appear in WALKWORTHY or WCF files; the index and ownership of every target path are understood before staging.

- [ ] **Step 2: Record baseline hashes for additive-edit candidates**

```bash
shasum -a 256 \
  Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html \
  WCF-Benchmark/project-dashboard.html \
  CORINTHLOVE/STATUS.md
```

Expected: three hashes. Keep them in transient session notes, not a repository file.

- [ ] **Step 3: Load the approved policy and current active boundaries**

```bash
sed -n '1,240p' output/docs/superpowers/specs/2026-07-13-biblebench-paper-first-workflow-design.md
sed -n '1,180p' Christian-Ethics-Benchmark/00-PORTFOLIO/20260713-codex-o5-pr13-surface-stop-handoff.md
sed -n '1,180p' WCF-Benchmark/20260713c-codex-session34-handoff.md
sed -n '1,180p' CORINTHLOVE/STATUS.md
```

Expected: PF-001's design, WALKWORTHY's PR-13 boundary, WCF's state-only boundary, and CORINTHLOVE's current next action are visible.

- [ ] **Step 4: Apply the ownership stop rule**

If another task is actively modifying a target path, implement the new top-level files first. Re-read the live path after the other task finishes and make only the additive link patch. Never stage a pre-existing hunk.

### Task 2: Create the charter and inherited agent contract

**Files:**
- Create: `PAPER-FIRST-WORKFLOW.md`
- Create: `AGENTS.md`

- [ ] **Step 1: Create the binding portfolio charter**

Use the approved design as authority. Its operational core must read:

```markdown
# BibleBench Paper-First Workflow

**Authority:** Binding for every current and future benchmark under this directory.

## Decision rule

Work may block manuscript drafting, pilot evidence collection, analysis, or PDF
production only when an unresolved issue could materially compromise a registered
paper claim, evidentiary integrity, construct validity, reproducibility, safety, or
an approved spending boundary.

All other improvements are timeboxed, disclosed as limitations, or moved to the
post-pilot backlog.

## Owner exception

Deviation requires Jimmy's explicit approval recorded in
`PAPER-FIRST-DECISIONS.md` and `project-dashboard.html`, including reason, scope,
date, and expiration or completion condition.
```

Add the complete P0–P3 table, four-track status model, nine-step operating funnel, session duties, drift triggers, and the statement that this policy does not authorize spending or credential access.

- [ ] **Step 2: Create inherited agent instructions**

Include this exact operating contract:

```markdown
# AGENTS.md — BibleBench portfolio

## Binding paper-first workflow

Before work, read `PAPER-FIRST-WORKFLOW.md`, `project-dashboard.html`, and
`ACTIVE-CRITICAL-PATHS.md`.

At session opening, state the next paper-facing milestone, sufficiency gate,
open P0/P1 blocker, engineering timebox, and expected closing artifact.

P2/P3 findings do not block manuscript, pilot, analysis, or PDF work unless
Jimmy approves an exception recorded in `PAPER-FIRST-DECISIONS.md`.

At session close, report a paper-facing artifact, a removed or narrowed P0/P1
blocker, or an explicit escalation. Test counts and implementation volume do
not substitute for paper-facing progress.

No paid call, credential access, frozen-surface edit, or historical handoff
rewrite is authorized by this file.
```

Add precedence rules: safety, evidence integrity, frozen surfaces, and explicit owner rulings remain controlling. Benchmark-specific instructions may strengthen but not weaken the portfolio rule. Require path-scoped staging and preservation of unrelated work.

- [ ] **Step 3: Validate both contracts**

```bash
/opt/homebrew/bin/python3 - <<'PY'
from pathlib import Path
policy = Path('PAPER-FIRST-WORKFLOW.md').read_text()
agents = Path('AGENTS.md').read_text()
for token in [
    'every current and future benchmark', 'P0', 'P1', 'P2', 'P3',
    'manuscript', 'pilot evidence', 'PDF', 'explicit approval',
    'ON PATH', 'AT RISK', 'OFF PATH', 'does not authorize',
]:
    assert token in policy, token
for token in [
    'PAPER-FIRST-WORKFLOW.md', 'project-dashboard.html',
    'ACTIVE-CRITICAL-PATHS.md', 'P2/P3', 'paper-facing artifact',
    'path-scoped', 'No paid call',
]:
    assert token in agents, token
print('charter and agent contract: PASS')
PY
```

Expected: `charter and agent contract: PASS`.

- [ ] **Step 4: Commit only the two contracts**

```bash
git diff --check -- PAPER-FIRST-WORKFLOW.md AGENTS.md
git log -1 --oneline
git add -- PAPER-FIRST-WORKFLOW.md AGENTS.md
git diff --cached --name-only
git commit -m "BibleBench: adopt paper-first portfolio rules"
```

Expected: exactly the two named top-level files are staged.

### Task 3: Add templates, owner ruling, and active contracts

**Files:**
- Create: `templates/PAPER-CRITICAL-PATH-CONTRACT.md`
- Create: `templates/SESSION-OPEN-CLOSE.md`
- Create: `PAPER-FIRST-DECISIONS.md`
- Create: `ACTIVE-CRITICAL-PATHS.md`

- [ ] **Step 1: Create the reusable critical-path template**

```markdown
# Paper Critical-Path Contract

- `paper_claim_enabled`:
- `paper_deliverable`:
- `blocking_reason`: none, or one classified P0/P1 issue
- `minimum_sufficiency_gate`:
- `timebox`:
- `stop_condition`:
- `deferred_nonblocking_work`:
- `owner_approved_exception`: none, or a decision-log anchor

## Review disposition

- Open P0:
- Open P1:
- Deferred P2:
- Deferred P3:
```

State that blanks are allowed only in the template; copied live contracts require concrete values.

- [ ] **Step 2: Create the session template**

```markdown
# Paper-First Session Record

## Opening declaration

- Next paper-facing milestone:
- Sufficiency gate:
- Open P0/P1 blocker:
- Engineering timebox:
- Expected closing artifact:

## Closing disposition

- Paper-facing artifact produced:
- P0/P1 blocker removed or narrowed:
- Escalation, if neither occurred:
- P2/P3 work deferred:
- Dashboard and active contract updated:
```

- [ ] **Step 3: Create the append-only decision log**

Its first record must be:

```markdown
## PF-001 — Portfolio-wide paper-first default

- Date: 2026-07-13
- Status: RATIFIED
- Owner: Jimmy Lin
- Scope: Every current and future benchmark under `40-BIBLEBENCH/`
- Decision: Use the dashboard plus the three-layer charter, agent-contract, and
  benchmark-contract design. An agent may deviate only with Jimmy's explicit,
  recorded approval.
- Expiration: none; superseded only by a later owner ruling.
```

Add an exception-record schema requiring ID, date, approver, reason, scope, affected paper milestone, expiration condition, and closing disposition.

- [ ] **Step 4: Create the living active-path register**

State that `ACTIVE-CRITICAL-PATHS.md` is edited in place and is the authoritative portfolio execution surface. Add complete eight-field contracts for:

1. **Consolidated pilot — FruitBench, CORINTHLOVE, 10CBench, SermonMount.** Deliverables: methods manuscript, 48 executable episodes, pilot tables, and PDFs. The P1 gate is complete geometry/schema/provenance/shared-scheduler validation. The timebox ends after one bounded integration review and one repair pass. P2/P3 hostile-deployment hardening is deferred.
2. **WALKWORTHY.** Preserve PR-13 as the current owner-ruling boundary. The register authorizes no paid resumption.
3. **WCF.** Preserve the state-only boundary and lack of T3/T4 authorization. The next safe paper-facing action is offline manuscript assembly or owner-supplied ruling/budget authority, not inferred execution.

For the consolidated pilot, use this minimum gate verbatim:

```markdown
- `minimum_sufficiency_gate`: 12 episodes per benchmark; 4 target, 4 null/foil,
  and 4 restraint/counterfeit; 34 common-life and 14 Christian-facing overall;
  C0/C1/C2, probe, answer contract, capability twin, failure poles, and exact
  provenance present; no open P0/P1 review finding.
```

Add the rule that every future benchmark must enter the register with a concrete paper deliverable, gate, timebox, and stop condition before engineering begins.

- [ ] **Step 5: Validate all governance records**

```bash
/opt/homebrew/bin/python3 - <<'PY'
from pathlib import Path
contract = Path('templates/PAPER-CRITICAL-PATH-CONTRACT.md').read_text()
session = Path('templates/SESSION-OPEN-CLOSE.md').read_text()
decisions = Path('PAPER-FIRST-DECISIONS.md').read_text()
active = Path('ACTIVE-CRITICAL-PATHS.md').read_text()
fields = [
    'paper_claim_enabled', 'paper_deliverable', 'blocking_reason',
    'minimum_sufficiency_gate', 'timebox', 'stop_condition',
    'deferred_nonblocking_work', 'owner_approved_exception',
]
assert all(field in contract for field in fields)
assert 'Opening declaration' in session and 'Closing disposition' in session
assert 'PF-001' in decisions and 'RATIFIED' in decisions and 'Jimmy Lin' in decisions
for heading in ['Consolidated', 'WALKWORTHY', 'WCF']:
    assert heading in active, heading
assert all(active.count(f'`{field}`') >= 3 for field in fields)
assert '48 executable episodes' in active
assert 'no paid' in active.lower()
print('templates, decisions, and active paths: PASS')
PY
```

Expected: `templates, decisions, and active paths: PASS`.

- [ ] **Step 6: Commit only the four governance paths**

```bash
git diff --check -- templates/PAPER-CRITICAL-PATH-CONTRACT.md templates/SESSION-OPEN-CLOSE.md PAPER-FIRST-DECISIONS.md ACTIVE-CRITICAL-PATHS.md
git log -1 --oneline
git add -- templates/PAPER-CRITICAL-PATH-CONTRACT.md templates/SESSION-OPEN-CLOSE.md PAPER-FIRST-DECISIONS.md ACTIVE-CRITICAL-PATHS.md
git diff --cached --name-only
git commit -m "BibleBench: register paper critical paths"
```

Expected: exactly the four named paths are staged.

### Task 4: Create the portfolio dashboard

**Files:**
- Create: `project-dashboard.html`

- [ ] **Step 1: Build a self-contained, no-JavaScript dashboard**

The header must include:

```html
<header>
  <p class="eyebrow">BibleBench portfolio</p>
  <h1>Paper-first critical path</h1>
  <p>Last updated: 2026-07-13 · by Codex</p>
  <span class="status on-path">ON PATH</span>
</header>
```

Add sections for portfolio summary; manuscript, executable-bank, evidence, and PDF progress; status cards for the consolidated pilot, WALKWORTHY, and WCF; open P0/P1 blockers; deferred P2/P3 hardening; spend checkpoints; owner exceptions; drift rules; and exact next-session instructions.

Each status card must show the next paper-facing milestone, all four progress tracks, blocker, timebox, deferred hardening, spend, owner exception, and a link to `ACTIVE-CRITICAL-PATHS.md`.

Use inline CSS only. Do not add JavaScript, CDNs, external fonts, remote images, or external stylesheets.

- [ ] **Step 2: Validate HTML and policy fields**

```bash
/opt/homebrew/bin/python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path

class Parser(HTMLParser):
    pass

text = Path('project-dashboard.html').read_text()
Parser().feed(text)
required = [
    'Paper-first critical path', 'ON PATH', 'AT RISK', 'OFF PATH',
    'Manuscript', 'Executable bank', 'Evidence', 'PDF',
    'P0/P1', 'P2/P3', 'Engineering timebox', 'Spend',
    'Owner exception', 'ACTIVE-CRITICAL-PATHS.md',
]
missing = [token for token in required if token not in text]
assert not missing, missing
lower = text.lower()
assert '<script' not in lower
assert 'http://' not in lower and 'https://' not in lower
assert '<link' not in lower
print('portfolio dashboard: PASS')
PY
```

Expected: `portfolio dashboard: PASS`.

- [ ] **Step 3: Perform visual verification**

Open `COOKBOOK/40-BIBLEBENCH/project-dashboard.html` in the in-app browser if local-file policy permits. Check desktop and narrow widths for overlap, readable cards, status labels distinguishable without color alone, and resolving local links. If browser policy blocks local files, record the established exception and use source/structure verification; do not invent a bypass.

- [ ] **Step 4: Commit only the dashboard**

```bash
git diff --check -- project-dashboard.html
git log -1 --oneline
git add -- project-dashboard.html
git diff --cached --name-only
git commit -m "BibleBench: add paper-first portfolio dashboard"
```

Expected: only the top-level dashboard is staged.

### Task 5: Link existing dashboards without absorbing concurrent work

**Files:**
- Modify: `Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html`
- Modify: `WCF-Benchmark/project-dashboard.html`

- [ ] **Step 1: Re-read live files and isolate pre-existing diffs**

```bash
git status --short -- Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html WCF-Benchmark/project-dashboard.html
git diff -- Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html
git diff -- WCF-Benchmark/project-dashboard.html
```

Expected: all pre-existing hunks are visible. If ownership is unclear, leave the local file unchanged and record the missing link as a follow-up.

- [ ] **Step 2: Add one visible relative link to each header or live navigation**

WALKWORTHY:

```html
<a class="portfolio-link" href="../../project-dashboard.html">BibleBench paper-first portfolio dashboard</a>
```

WCF:

```html
<a class="portfolio-link" href="../project-dashboard.html">BibleBench paper-first portfolio dashboard</a>
```

Reuse existing styling where possible and do not restructure frozen history.

- [ ] **Step 3: Verify links and no-JavaScript preservation**

```bash
/opt/homebrew/bin/python3 - <<'PY'
from pathlib import Path
checks = {
    Path('Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html'): '../../project-dashboard.html',
    Path('WCF-Benchmark/project-dashboard.html'): '../project-dashboard.html',
}
for path, href in checks.items():
    text = path.read_text()
    assert href in text, (path, href)
    assert '<script' not in text.lower(), path
print('local dashboard links: PASS')
PY
```

Expected: `local dashboard links: PASS`.

- [ ] **Step 4: Stage only the new link hunks**

Use `git add -p` for any dirty file and accept only the portfolio-link hunk. Then run:

```bash
git diff --cached --check
git diff --cached --name-only
git diff --cached -- Christian-Ethics-Benchmark/00-PORTFOLIO/project-dashboard.html WCF-Benchmark/project-dashboard.html
```

Expected: the cached diff contains only the two links and inseparable local styling. No session-status or evidence hunk is staged.

- [ ] **Step 5: Commit only if isolation is proven**

```bash
git log -1 --oneline
git commit -m "BibleBench: link local dashboards to paper path"
```

Expected: a scoped link-only commit. If isolation is not proven, skip this commit and document the follow-up.

### Task 6: Run acceptance checks and close the rollout

**Files:**
- Verify: `PAPER-FIRST-WORKFLOW.md`
- Verify: `AGENTS.md`
- Verify: `ACTIVE-CRITICAL-PATHS.md`
- Verify: `PAPER-FIRST-DECISIONS.md`
- Verify: `templates/PAPER-CRITICAL-PATH-CONTRACT.md`
- Verify: `templates/SESSION-OPEN-CLOSE.md`
- Verify: `project-dashboard.html`

- [ ] **Step 1: Run the complete documentation contract check**

```bash
/opt/homebrew/bin/python3 - <<'PY'
from pathlib import Path
paths = [
    Path('PAPER-FIRST-WORKFLOW.md'), Path('AGENTS.md'),
    Path('ACTIVE-CRITICAL-PATHS.md'), Path('PAPER-FIRST-DECISIONS.md'),
    Path('templates/PAPER-CRITICAL-PATH-CONTRACT.md'),
    Path('templates/SESSION-OPEN-CLOSE.md'), Path('project-dashboard.html'),
]
assert all(path.is_file() and path.stat().st_size > 0 for path in paths)
joined = '\n'.join(path.read_text() for path in paths)
for token in [
    'paper_claim_enabled', 'minimum_sufficiency_gate',
    'owner_approved_exception', 'P0', 'P1', 'P2', 'P3',
    'ON PATH', 'AT RISK', 'OFF PATH',
    'manuscript', 'pilot', 'PDF', 'timebox',
]:
    assert token.lower() in joined.lower(), token
assert 'PF-001' in Path('PAPER-FIRST-DECISIONS.md').read_text()
print('paper-first portfolio acceptance: PASS')
PY
```

Expected: `paper-first portfolio acceptance: PASS`.

- [ ] **Step 2: Verify scope and history preservation**

```bash
git status --short
git log --oneline -8
git show --stat --oneline HEAD
```

Expected: pre-existing unrelated modifications may remain. Rollout commits contain no run ledger, checkpoint, raw evidence, dated historical handoff, or secret path.

- [ ] **Step 3: Perform the two-minute re-entry test**

Using only `AGENTS.md` and `project-dashboard.html`, identify the next consolidated-pilot artifact, its P1 sufficiency blocker, timebox and stop condition, no-spend boundary, and exact continuation file. All five must be available in under two minutes.

- [ ] **Step 4: Update the living surfaces to the actual completion state**

Set the dashboard's last-updated line, critical-path health, and update log. Update `ACTIVE-CRITICAL-PATHS.md` only if rollout uncovered a real P0/P1 blocker or owner-approved exception. Do not turn documentation observations into new paper prerequisites.

- [ ] **Step 5: Commit a final living-state change only if needed**

```bash
git diff --check -- project-dashboard.html ACTIVE-CRITICAL-PATHS.md
git log -1 --oneline
git add -- project-dashboard.html ACTIVE-CRITICAL-PATHS.md
git diff --cached --name-only
git commit -m "BibleBench: close paper-first workflow rollout"
```

Expected: only the two living surfaces are staged. Do not create an empty commit.

## Execution boundaries

- Make no live model, network, or paid calls.
- Do not read credentials or secret values.
- Do not rewrite dated handoffs or frozen decision records.
- Do not stage pre-existing run, evidence, checkpoint, dashboard, or agent-instruction changes.
- Treat the central dashboard and active register as living surfaces and the decision log as append-only.
- Stop and escalate if a local-dashboard link cannot be isolated from another task's changes.
- Do not expand this documentation rollout into benchmark-engine hardening.
