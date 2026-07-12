# INNOVATION — Agent Instructions

**Scope:** this file governs work inside `CEI-Lit-WS/INNOVATION/` (the values-alignment
measurement-frontier lane: field map, gap atlas, RP-01…RP-10, deliverables P1–P3). It binds
**every agent** working this lane — Anthropic (Claude) models, OpenAI (Codex) agents, and any
other model. Vault-wide safety rules (no deletions → RECYCLE-BIN, YAML safety, report
immutability, staged-only commits) live in the root CLAUDE.md and are hook-enforced; lane
governance lives in `00-CHARTER/01-governance-protocol.md`.

## The project dashboard (`project-dashboard.html`) — ALL agents maintain it

`INNOVATION/project-dashboard.html` is the lane's single living status page — referred to and
updated by every agent that works here. It is intentionally **undated and edited in place**: the
lane's ONE exception to the dated-file immutability rule (Jimmy's direction 2026-07-11; charter
amendment `00-CHARTER/20260711-governance-amendment-dashboard.md`). Git history is its snapshot
record — never create dated copies of it, never leave it stale.

**SESSION OPEN:** read the dashboard FIRST (Live status, forecasts, cycle board, rulings ledger,
§Instructions-for-next-session), alongside this file and the latest dated handoff.

**SESSION CLOSE (and after any milestone/ruling change), update the LIVE surfaces** (sections are
chipped LIVE or HISTORY in the page):
1. The banner's **"Last updated: <date> · by <agent>"** line — mandatory, even if nothing else changed.
2. **⚡ Live status** and the 📍 YOU-ARE-HERE marker.
3. **Session forecasts** — revise only on material change.
4. **Cycle/queue board, rulings ledger, gate-protocols table, lanes, doc map** — whatever your
   session made stale.
5. **Append one row to the Changelog** (append-only, newest last).
6. **§Instructions for next session — REWRITE it** every time a new boot/re-entry prompt is
   prepared (paste text, model, directory, prepared-date), so the next session can always be
   launched straight from the dashboard.

Sections chipped **HISTORY are frozen** — append timeline entries, never rewrite past ones. Do not
restructure the page. Keep it fully self-contained (inline CSS, no JavaScript, no external
fonts/CDNs — must render offline via `file://`), and never put canary strings in it. The dashboard
summarizes and CITES dated reports; it never replaces them as the evidentiary record.

**Boot-prompt convention:** any NEW boot prompt, re-entry prompt, or session handoff written for
this lane MUST include two lines: (i) "on session open: read `INNOVATION/project-dashboard.html`
(Live status first)" and (ii) "on session close: update the dashboard per
`INNOVATION/AGENTS.md §The project dashboard`" — and whenever you write a new boot prompt, rewrite
the dashboard's §Instructions-for-next-session to match.

## Lane pointers

- Execution queue (living checkboxes): `07-opus-handoff.md` — work top-down within the open cycle.
- Decisions above session tier: queue in `PENDING-RULINGS.md` (PR-NN pattern); **never self-approve**.
- Decision log (living, append-only): `00-CHARTER/04-decision-log.md` (DL-NN, one line each).
- Kill criteria in RP briefs are binding; softening requires Jimmy — procedure in
  `20260711-fable-gate-protocols-memo.md` §7. Post-window Fable gates run as "Opus memo → Jimmy
  decides" per that memo.
- Evidence classes (`[VERIFIED]/[SEARCH-CONFIRMED]/[⚠]`) travel with every citation; nothing ⚠
  enters external prose as fact.
- Before acquiring any paper: grep `papers/` for the arXiv ID/title across the WHOLE vault, not
  just acquisition logs (DL-26 — duplicate-record lesson, 2026-07-11).
