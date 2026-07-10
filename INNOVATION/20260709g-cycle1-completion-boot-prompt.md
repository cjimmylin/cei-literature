# Cycle-1 Completion — Fable Orchestrator Session Boot Prompt

**Written:** 2026-07-09 (CLI-OAuth Fable session, at Jimmy's request). **Use with:** a fresh **Fable** session (`/clear` first); window closes ~2026-07-11. **Sequencing:** Jimmy has re-prioritized this ahead of Governance Symphony (which had been next per the exit-sequencing memo); Governance Symphony follows this session. Paste the block below verbatim.

---

This is a Fable-tier session run Playbook-C style (per `INNOVATION/00-CHARTER/03-reentry-guide.md`): Fable stays in the main loop ONLY to dispatch, adjudicate, spot-check, and close; ALL execution goes to parallel Opus/Sonnet agents with explicit `model=` in EXECUTION mode (verify each agent produced files, not plans — relaunch immediately if an agent returns a plan). Goal: **close every session-executable item left in Cycle 1** of `INNOVATION/07-opus-handoff.md`, so the only Cycle-1 residuals are Jimmy-tier.

**Remaining scope (verified 2026-07-09):** (a) item 1.2 remainder — ~40–45 P2 acquisitions by gap group + 2 non-arXiv P1 Anthropic blog posts + 6 non-arXiv P2 items; (b) item 1.4 FC-15 — P3 spec-citation upgrades + ledger reconciliation; (c) item 3.5 — Stage-4 documented-vs-live vocabulary reconciliation proposal (Jimmy sign-off queued, not self-approved). Read `INNOVATION/20260709f-cli-oauth-session-handoff.md` first for session-state context; PR queue check per Playbook C (PR-02 is open — do NOT self-approve it; it does not block this work).

## Lane A — P2 arXiv acquisitions (3–4 parallel Sonnet agents)

Source list: `INNOVATION/04-missing-literature.md` (gap-group sections G-01/02/03 … G-20/21/22/23; P1 anchors already ingested — skip anything already in `papers/`). First, in the main loop or via one quick Sonnet scout, enumerate the exact outstanding P2 set (my scout estimated ~40 arXiv items, ~10–12 with ⚠ flags); then partition into 3–4 batches of ~10–14 by gap group and dispatch in parallel. Each agent follows the PROVEN P1 workflow (`INNOVATION/40-BUILDS/20260709-p1-acquisition-log.md` + `40-BUILDS/p1_acquire.py` — reuse its functions):
1. **⚠ items: verify BEFORE download** — open `arxiv.org/abs/<id>`, confirm title/authors match the list entry; on mismatch, log a MISS and move on (never guess a corrected ID; queue misses for the report).
2. Fetch arXiv metadata → download PDF to `Lit-WS-PDFs/YYYY/YYYY-Author-Short Title.pdf` with the script's backoff (429 → 2^attempt×5 s) **plus a 5 s sleep between downloads** (multiple agents share one IP — this is mandatory).
3. PyMuPDF extract → `PDF Extracts/YYYY/…`; paper record → `papers/YYYY-Author-Short Title.md` with v1.5 dual-homed `research_topic` codes + `innovation_gap` field (P1 records are the template).
4. Log every item (hit/miss/⚠-resolution) to a per-agent dated log `40-BUILDS/20260710-p2-acquisition-log-<batch>.md`.
YAML safety: never parse/rebuild frontmatter round-trip; use the `re.subn` line-pattern (root CLAUDE.md). Do NOT run validate_all_papers per agent — once, at the end, main loop.

## Lane B — manual/web ingests (1 Opus agent, parallel with A)

Eight items, no arXiv IDs:
- **2 P1 Anthropic blog posts:** "Teaching Claude Why" (anthropic.com/research/teaching-claude-why, G-22) and "Agentic Misalignment" (anthropic.com/research/agentic-misalignment, G-16). Render → PDF via headless browser (Playwright MCP tools are available; `file://` is blocked for viewing but printing a live URL to PDF works — verify output is real content, not a bot-wall), file under `Lit-WS-PDFs/YYYY/`, hand-write extracts + paper records.
- **6 non-arXiv P2** from the "Non-arXiv / manual ingest" section (Nature warm-models paper, OpenAI Model Spec, Claude's Constitution, sabotage-risk pilot, Anthropic×OpenAI cross-lab eval, Claude system cards). **For the Model Spec and Constitution: do NOT re-fetch** — the vault already holds SHA-256-stamped retrievals at `40-BUILDS/rp01-registries/` (see `20260709-version-stamps.md`); create paper records that point at those registry copies and inherit their VERIFIED class. Paywalled/oversized items (Nature, system cards): ingest what is legitimately accessible; log the rest as DEFERRED with reason — never fabricate a record for content not actually obtained.

## Lane C — FC-15 citation upgrade (1 Opus agent; phase 1 parallel, phase 2 after Lane A)

Governing text: FC-15 in `INNOVATION/20260709-fable-p3-draft-screening.md`. The P3 draft is `40-BUILDS/p3-position-paper/20260709-draft-v0.md`; its embedded ledger (~41 ⚠ / 20 SEARCH-CONFIRMED / 0 VERIFIED rows) is the authoritative enumeration. **Do not edit draft-v0** (FC-15: record upgrades in the ledger, not the frozen draft): produce a NEW dated ledger file `40-BUILDS/p3-position-paper/20260710-ledger-v1.md` that (1) reconciles the 20/41-vs-23/47 count drift (distinct-source ledger wins; map prose tags to ledger rows), (2) upgrades the two spec citations to [VERIFIED] via the RP-01 registry stamps, and (3) **after Lane A/B complete**, upgrades every ledger row whose source was ingested this session (⚠ → VERIFIED only where the downloaded PDF's title/authors were confirmed; SEARCH-CONFIRMED → VERIFIED likewise; anything not ingested stays put). Every upgrade cites its evidence (registry stamp or vault PDF path). The P3 double gate is unchanged: pre-submission review still required before ANY external use.

## Lane D — item 3.5 vocabulary reconciliation (Sonnet inventory → Opus proposal; parallel with A)

Per handoff 3.5 and taxonomy proposal §9.2: the documented Stage-4 list in `_OPERATING-SYSTEM/Standards/classification-logic.md` doesn't match live usage ("Benchmarks & Datasets" used 0×; ≥8 live codes undocumented — Other 182, Social & Cultural Analysis 89, Truthfulness & Factuality 31, Computer Vision & Multimodal 31, Dialogue Systems 11, Bias & Fairness 12, Interpretability & Explainability 5, LLM Moral Reasoning 5, plus tail).
- **D1 (Sonnet):** fresh full inventory — every live `research_topic` value with counts across `papers/`, diffed against the documented list (including the 5 new v1.5 codes). Output: dated inventory table under `INNOVATION/`.
- **D2 (Opus, after D1):** new dated proposal `INNOVATION/20260710-stage4-vocab-reconciliation-proposal.md` — options (document-the-live-set / merge-and-migrate / deprecate-unused), migration cost per option, a recommendation, ready-to-apply patch, and fold in the deferred Patch D (stale `Version: 1.0` header bump, gated separately in the taxonomy proposal).
- **Fable adjudicates the recommendation**, then queues it as **PR-03** in `INNOVATION/PENDING-RULINGS.md` (standards file = Jimmy sign-off; do NOT apply the patch this session).

## Fable main-loop duties (do not delegate these)

1. Dispatch lanes A–D in parallel (A's 3–4 agents + B + C-phase-1 + D1 simultaneously); sequence C-phase-2 after A/B and D2 after D1.
2. **Adjudicate on return:** spot-check ≥8 random Lane-A/B ingests end-to-end (PDF exists and opens, extract non-empty, YAML fields right, `innovation_gap` correct, arXiv ID ↔ title match); audit Lane C upgrades (every [VERIFIED] claim must point at a real registry stamp or on-disk PDF — downgrade any that don't); screen Lane D's proposal before queueing PR-03. Relaunch any agent that planned instead of executed.
3. Run `../.venv/bin/python PYTHON/validate_all_papers.py` ONCE after all paper edits; fix-or-relaunch on errors.
4. Close the books: tick 1.2/1.4 in `07-opus-handoff.md` (1.4's residual = pre-submission gate; 3.5's residual = PR-03) and declare **Cycle 1 CLOSED (session-executable work = zero; residuals Jimmy-tier: PR-02, PR-03, keys)**; append DL entries to `00-CHARTER/04-decision-log.md`; update FABLE-WEEK (vault-root `.claude/`, separate repo) + the `innovation-portfolio-state` memory; write dated handoff `INNOVATION/20260710-cycle1-close-handoff.md`.
5. Commit + push BOTH repos, pathspec-limited: `git log -1` + `git diff --cached --name-only` first; `git commit -- <files>` only (parallel sessions share this index — it moved mid-session twice on 2026-07-09; untracked `p1_*.py`/acquisition files at `40-BUILDS/` top level belong to another session's history — leave them).

Hard rules: tiering per `~/.claude/CLAUDE.md` (explicit `model=` on every dispatch); no `rm` (RECYCLE-BIN; hook scans command strings — don't even echo deletion commands); report immutability (new dated files only); evidence classes travel with every citation; arXiv rate-limit discipline as specified; nothing ⚠ enters any record unverified.

---

**Why this prompt exists:** Cycle 1 was ~90% done after 2026-07-09 (design layer + wave-1 execution + CLI-OAuth bring-up). Jimmy asked for a dedicated Fable-orchestrated session to finish the remainder — mechanical batch work parallelized down-tier, with Fable adjudicating ingest quality, citation-upgrade evidence, and the vocab-reconciliation recommendation in-loop. After this session, Cycle 1 has no session-executable work left; everything else in the portfolio waits on Jimmy's gates (PR-02, PR-03, API keys, Gemini, GPU budget, raters).
