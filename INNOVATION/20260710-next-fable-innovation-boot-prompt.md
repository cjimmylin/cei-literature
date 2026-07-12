# INNOVATION — Next Fable Session Boot Prompt (P3 gate + gate front-loading)

**Written:** 2026-07-10 (Cycle-1-close Fable session, at Jimmy's request — he re-sequenced INNOVATION ahead of Governance Symphony, which moves to the session after). **Use with:** a fresh **Fable** session (`/clear` first); window closes ~2026-07-11. Paste the block below verbatim.

---

This is a Fable-tier session run Playbook-C style, scoped to **ONE lane: `CEI-Lit-WS/INNOVATION/`**. Fable stays in the main loop to dispatch, adjudicate, and close; execution goes to Opus/Sonnet agents with explicit `model=` in EXECUTION mode (verify files, relaunch planners). Cycle 1 is CLOSED (2026-07-10) — this session does NEW work; do not reopen Cycle-1 bookkeeping.

**Step 0 — state sync (before dispatch):** read `INNOVATION/20260710-cycle1-close-handoff.md`, then `PENDING-RULINGS.md` (PR-02/PR-03 status), then `07-opus-handoff.md` Cycles 2–4 + gate list. Branches: **if API keys have landed** (gate #1), Cycle 2 opens — 2.2 HAWTHORNE's 20-pair Fable gate jumps to centerpiece and Mission B shrinks to fit; **if PR-03 is signed**, add a Sonnet agent to apply the §6 patch from `20260710-stage4-vocab-reconciliation-proposal.md` mechanically (+ validator, tick 3.5). Neither PR may be self-approved.

## Mission A — P3 pre-submission gate (centerpiece)

The position paper's double gate is: citation upgrades (DONE — ledger 52/64 VERIFIED) + **pre-submission adversarial review before ANY external use**. This session executes the review. External use remains Jimmy's decision regardless of verdict — this gate is necessary, not sufficient.

1. **A1 (1 Sonnet agent, parallel):** acquire the ledger's still-absent sources to maximize VERIFIED coverage before review. Enumerate the exact outstanding set from `40-BUILDS/p3-position-paper/20260710-ledger-v1.md` (snapshot as of 2026-07-10: S1, S8, S9=2501.09254, S10, S11, S13 Sheshadri, S15=2502.08640, W5=2510.06370, W26=2602.20710, W32=2604.09588; S3 is a 3-source bundle with 2 components missing). arXiv items use the proven pipeline (`40-BUILDS/p1_acquire.py` functions; verify-metadata-first, 5 s inter-download sleep, MISS on mismatch — never guess IDs); non-arXiv items: ingest what is legitimately accessible, else DEFERRED with reason. **Paper-record `tags:` field = empty scalar `tags: ` exactly** (the validator rejects multi-item block lists — 2026-07-10 lesson). Then produce `40-BUILDS/p3-position-paper/20260710-ledger-v2.md` (NEW dated file — do not edit ledger-v1) with evidence-gated upgrades only (ls-verified vault PDF + title match; W3's claim-divergence needs re-adjudication by Fable, not blind upgrade).
2. **A2 (2 Opus agents, parallel, refute-first):** independent adversarial reviews of the FROZEN draft `40-BUILDS/p3-position-paper/20260709-draft-v0.md` — reviewer 1: validity/evidence lens (every load-bearing claim vs its ledger row and evidence class; flag any claim resting on ⚠/SC rows or overstating a source); reviewer 2: novelty/positioning lens (claims vs the now-ingested corpus, including the 52 records acquired 2026-07-10; does the field map §-structure still hold?). Anti-leakage: reviewers work independently, no reading each other's output.
3. **A3 (Fable in-loop, do not delegate):** read draft-v0 yourself; adjudicate A2 findings against A1's final ledger; run `validate_all_papers.py` ONCE if A1 created records; write the binding verdict memo `INNOVATION/20260710-fable-p3-presubmission-review.md` — verdict ∈ {GO / CONDITIONAL-GO with enumerated required revisions / NO-GO with reasons}, each required revision tied to evidence. Revisions themselves are a post-window Opus work order producing a draft-v1 (draft-v0 stays frozen); include the work order in the memo.

## Mission B — front-load post-window Fable gates (the exit-sequencing pattern)

The queue embeds Fable-tier gates that will block post-window Opus: 2.2 HAWTHORNE 20-pair sample gate, 3.1 NOGOLD 30-item transcript review, 4.2 SAYDO 30-item sample gate, 4.3 CONCLAVE non-negotiables registries, and the standing "kill-criteria softening requires Fable/Jimmy" rule. Write ONE binding memo `INNOVATION/20260710-fable-gate-protocols-memo.md` converting each to a mechanical protocol: pre-registered acceptance criteria + rubric, "Opus memo → Jimmy decides" escalation, and what outcome auto-queues vs auto-proceeds. Ground each protocol in its RP brief's kill criteria (read the briefs — delegate extraction to a Sonnet scout if long, keep the criteria-setting judgment in-loop). Nothing in this memo may soften a kill criterion.

## Close the books

Dated handoff `INNOVATION/20260710-<x>-session-handoff.md`; DL entries in `00-CHARTER/04-decision-log.md`; update FABLE-WEEK (vault-root `.claude/`, separate repo — Governance Symphony is next after this); update the `innovation-portfolio-state` memory; commit both repos.

## Hard rules (non-negotiable)

- **Lane isolation (Jimmy, 2026-07-10): only touch files created in THIS session's lane** (+ the INNOVATION living files named above, FABLE-WEEK, memory). Other lanes' files, worktrees, and dirty state are off-limits even if they look finished or blocked.
- **Git:** stage only your own named files; verify `git diff --cached --name-only` against your list; plain `git commit` — NEVER `git add -A`, NEVER `git commit -- <directory>` (pathspec commits bypass staging — DL-22); `git log -1` before committing (HEAD moves mid-session; shared index, see [[parallel-sessions-share-git-index]]).
- Tiering per `~/.claude/CLAUDE.md` (explicit `model=` on every dispatch); no `rm` ever (RECYCLE-BIN; hook scans command strings); report immutability (new dated files only; ledger-v1 and draft-v0 are frozen); evidence classes travel with every citation; nothing ⚠ enters any record or the review memo as fact.

---

**Why this prompt exists:** after Cycle-1 close, the INNOVATION lane's only non-Jimmy residual is the P3 pre-submission gate — pure Fable judgment, now maximally fed by the upgraded ledger. Mission B ensures the window closing doesn't strand post-window Opus at the queue's embedded Fable gates. After this session: Governance Symphony (`CEI-AI-Statements/GENERATION3/20260709-fable-session-boot-prompt.md`), then everything else is Opus-executable or Jimmy-gated (PR-02, PR-03, keys, GPU, raters).
