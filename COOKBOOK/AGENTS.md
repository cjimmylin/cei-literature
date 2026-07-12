# AGENTS.md — COOKBOOK core track (agent charter)

**Scope:** everything under `COOKBOOK/` **except `40-BIBLEBENCH/`** — i.e. `00-KNOWLEDGEBASE/`,
`10-LITERATURE/`, `30-EVIDENCE/`, `ENGINE/`, `20-DESIGNS/` (six designs + sketches + `DUPLEX-P0/`),
`Fable-Assessment/`, and the top-level dated handoff chain. `40-BIBLEBENCH/` benches
(WCF-Benchmark, Christian-Ethics-Benchmark/WALKWORTHY, CORINTHLOVE, FRUITBENCH, TENCOMMANDMENTS, …)
are **separate scopes** with their own AGENTS.md files, handoff chains, and dashboards — never
cross-reference or stage them from a core-track session.

## The project dashboard (`project-dashboard.html`) — ALL agents maintain it

`COOKBOOK/project-dashboard.html` is the core track's single living status page — referred to and
updated by **every agent that works here**: Anthropic (Claude) models, OpenAI (Codex) agents, and
any other model. It is intentionally **undated and edited in place**: the ONE exception to the
vault's dated-file immutability rule (Jimmy's direction, 2026-07-11; git history is its snapshot
record — never create dated copies of it, never leave it stale).

**SESSION OPEN:** load the dashboard FIRST — read §1 Live status, the design tab(s) relevant to
your lane, §6 Critical path, and §10 Instructions-for-next-session before touching anything else
(in a GUI environment open it in a browser; headless, read the HTML source's LIVE sections).

**SESSION CLOSE (and after any milestone/ruling/spend change), update the LIVE surfaces**
(each section is chipped LIVE or HISTORY in the page):
1. The banner's **"Last updated: <date> · by <agent>"** line — mandatory, even if nothing else changed.
2. **§1 Live status** — workstream rows, escalations, Jimmy-owed inputs.
3. **§2 Progress bars.**
4. **§3 Session forecasts** — revise only on material change.
5. **§4 History** — append a session row (template in an HTML comment there); never rewrite prior rows.
6. **§5 Design tabs** — refresh the tab panel(s) your session touched (e.g. tick OR-checklist rows,
   flip gate statuses, update per-design state/blockers/estimates).
7. **§7 Budget** — append rows after any live spend.
8. **§9 Update log** — append one line (append-only, newest last).
9. **§10 Instructions for next session** — REWRITE this section (paste text, model, directory,
   prepared-date) every time you prepare a new boot/re-entry prompt, so the next session can always
   be launched straight from the dashboard.

Sections chipped **HISTORY are frozen** (append-only). Do not restructure the page. The file is
fully self-contained — inline CSS, **pure-CSS tabs, NO JavaScript**, no external fonts/CDNs (it
must render offline via `file://`); keep it that way.

**Boot-prompt convention:** any NEW boot prompt, re-entry prompt, or session handoff an agent
writes for the core track MUST include two lines: (i) "on session open: load
`COOKBOOK/project-dashboard.html` (Live status + your lane's design tab first)" and (ii) "on
session close: update the dashboard per `COOKBOOK/AGENTS.md §The project dashboard`". And whenever
you write a new boot prompt, rewrite the dashboard's §10 with it. Prompts dated before 2026-07-11
predate this convention — apply it on top of them.

## Standing rules (core track)

- **Safety rules** (no deletions → `RECYCLE-BIN/`; YAML safety; dated-report immutability — the
  dashboard is the sole exemption) are defined in the vault root `CLAUDE.md` and hook-enforced;
  they bind subagents too.
- **Git:** path-scoped staging only (never `git add -A`); `git log -1` immediately before every
  commit — concurrent sibling sessions share the index. One track per session.
- **Frozen surfaces** (adjudication memos, gate rulings, X1–X6, the P0 protocol, SA/F/IB/PS/CS/OR
  series): builder agents never edit them. Draft a change proposal; Jimmy ratifies.
- **Post-Fable-window delegation (window closed 2026-07-11):** anything labeled "Fable-tier" now
  means: Opus writes a PR-NN decision memo into the track's queue and Jimmy decides. Nothing is
  silently decided at a lower tier. Registries/thresholds/headline claims are Jimmy-only.
- **Escalation:** any live behavior outside a pre-registered pattern → STOP and escalate (the
  DUPLEX-P0 protocol's rule generalizes) — never improvise a lower-tier judgment mid-run.
- **Secrets:** `~/.codex/secrets/openrouter.env` and any Anthropic credential are Jimmy's — source
  at call time only; never read into transcripts, echo, or commit values.

## Entry points

| Doc | Role |
|---|---|
| `project-dashboard.html` | Living status + the prepared next-session boot prompt (§10) |
| `Fable-Assessment/20260707-00-master-assessment-and-roadmap.md` | Master roadmap (Sessions A/B/C queue) |
| `20260706-fable-exit-sequencing-memo.md` | Cross-track build order + delegation downgrade map |
| `20260709-next-session-handoff.md` | Consolidated dated entry handoff (pre-dashboard) |
| `20-DESIGNS/DUPLEX-P0/20260711-fable-openrouter-prerun-validity-review.md` | Latest binding memo (OR-1…OR-7 + run preconditions) |
| `20-DESIGNS/DUPLEX-P0/20260706-p0-adjudication-protocol.md` | Pre-registered P0 rubric (frozen) |

*Created 2026-07-11 (Fable) alongside the dashboard.*
