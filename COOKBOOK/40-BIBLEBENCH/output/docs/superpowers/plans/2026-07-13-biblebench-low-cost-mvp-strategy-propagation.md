# BibleBench Low-Cost MVP Strategy Propagation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the approved three-model, $5-cap MVP paper strategy binding across the BibleBench portfolio without authorizing paid calls.

**Architecture:** Preserve the approved specification as the detailed source of truth, append one owner ruling, add one concise workflow phase, and make the consolidated critical path and dashboard point to the same immediate paper-shaped outcome. Do not edit benchmark-local run custody, unrelated benchmark contracts, or the manuscript worktree from this shared main workspace.

**Tech Stack:** Markdown governance files, self-contained static HTML dashboard, Git path-scoped commits.

---

### Task 1: Record the binding owner ruling

**Files:**
- Modify: `PAPER-FIRST-DECISIONS.md`
- Modify: `PAPER-FIRST-WORKFLOW.md`

- [ ] **Step 1: Append PF-002 to the decision log**

Append a ratified ruling that records exactly three inexpensive general-purpose models, a $5 hard cap, one C1-plus-probe surface across 48 episodes, single-expert provisional judging, exploratory-only claims, and a no-scale-before-paper-preview gate. State explicitly that the ruling does not itself authorize credentials or paid calls.

- [ ] **Step 2: Add the MVP preview phase to the workflow**

Add a concise section after the operating funnel. It must make the MVP paper preview the immediate portfolio priority and defer premium models, larger panels, all cue surfaces, capability twins, formal concordance, and durability engineering until the owner reviews the manuscript, results, tables, PDFs, and scale-up memo.

- [ ] **Step 3: Validate governance consistency**

Run:

```bash
grep -n "PF-002\|three inexpensive\|\$5" PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md
git diff --check -- PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md
```

Expected: PF-002 and the MVP phase are present; `git diff --check` exits 0.

### Task 2: Replace the consolidated pilot critical path

**Files:**
- Modify: `ACTIVE-CRITICAL-PATHS.md`

- [ ] **Step 1: Narrow the consolidated paper claim**

State that the first result is an exploratory feasibility and descriptive pilot across three inexpensive general-purpose models, not a ranking or definitive validation study.

- [ ] **Step 2: Register the exact MVP sufficiency gate**

Require the frozen 48-episode bank, minimally adequate single-expert provisional gold, one preregistered C1-plus-probe surface, three-model manifest, forecast at or below $3, absolute cap of $5, reproducible custody, and separate final paid-call authorization.

- [ ] **Step 3: Register the stop and deferral rules**

Stop after the manuscript, results, tables, PDFs, spend ledger, and scale-up memo exist. Defer additional or premium models, multi-judge panels, repeat reliability as a prerequisite, C0/C1/C2 contrasts, capability-twin execution, formal family estimates, composites, and production hardening.

- [ ] **Step 4: Validate the eight-field contract**

Run:

```bash
grep -n "paper_claim_enabled\|paper_deliverable\|blocking_reason\|minimum_sufficiency_gate\|timebox\|stop_condition\|deferred_nonblocking_work\|owner_approved_exception" ACTIVE-CRITICAL-PATHS.md
git diff --check -- ACTIVE-CRITICAL-PATHS.md
```

Expected: all eight fields remain present for each active contract; the consolidated contract contains the three-model and $5 boundaries.

### Task 3: Update the living dashboard

**Files:**
- Modify: `project-dashboard.html`

- [ ] **Step 1: Update live consolidated status**

Change the summary, four-track status, consolidated card, blocker surface, and exact next-session instruction so the immediate outcome is the low-cost paper preview. Keep WALKWORTHY and WCF content unchanged.

- [ ] **Step 2: Append the owner ruling to the history surface**

Append a 2026-07-13 PF-002 entry stating that Jimmy approved the three-model, $5-cap MVP paper strategy and deferred scale-up until after review of the complete paper-shaped artifact.

- [ ] **Step 3: Preserve dashboard constraints**

Confirm the dashboard remains self-contained, contains no JavaScript or external resources, and retains valid local links.

Run:

```bash
grep -n "PF-002\|\$5\|three" project-dashboard.html
! grep -nE '<script|https?://' project-dashboard.html
git diff --check -- project-dashboard.html
```

Expected: the ruling is visible; no script or external URL is present; diff check exits 0.

### Task 4: Verify and commit the propagation

**Files:**
- Verify: `PAPER-FIRST-DECISIONS.md`
- Verify: `PAPER-FIRST-WORKFLOW.md`
- Verify: `ACTIVE-CRITICAL-PATHS.md`
- Verify: `project-dashboard.html`

- [ ] **Step 1: Confirm no paid authority was introduced**

Run:

```bash
grep -n "does not.*authorize\|separate.*authorization\|No paid" PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md ACTIVE-CRITICAL-PATHS.md project-dashboard.html
```

Expected: the strategy ceiling is distinct from final paid-call authority.

- [ ] **Step 2: Review only the intended diff**

Run:

```bash
git diff -- PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md ACTIVE-CRITICAL-PATHS.md project-dashboard.html
git diff --check -- PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md ACTIVE-CRITICAL-PATHS.md project-dashboard.html
```

Expected: only the approved MVP strategy is propagated and the diff check exits 0.

- [ ] **Step 3: Commit with path-scoped staging**

Run:

```bash
git log -1 --oneline
git add -- PAPER-FIRST-DECISIONS.md PAPER-FIRST-WORKFLOW.md ACTIVE-CRITICAL-PATHS.md project-dashboard.html
git commit -m "BibleBench: ratify low-cost MVP paper strategy"
```

Expected: one commit contains only the four binding strategy surfaces.
