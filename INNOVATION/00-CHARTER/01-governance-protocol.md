# Governance Protocol — INNOVATION Portfolio

**Created:** 2026-07-07 · **Author:** Fable 5 · **Status:** BINDING
**Pattern source:** `FRUITBENCH-REVIEWS/20260706-succession-protocol.md` (adapted; that document governs FRUITBENCH — this one governs INNOVATION independently).

## 1. Decision rights (who may decide what)

| Decision class | Opus session | Fable-tier session | Jimmy |
|---|---|---|---|
| Execute an RP task as written in its brief | ✔ | ✔ | ✔ |
| Interpret ambiguity in a brief (log the interpretation in `04-decision-log.md`) | ✔ | ✔ | ✔ |
| Trigger a kill criterion when its condition is met | ✔ (MUST — mechanical) | ✔ | ✔ |
| Soften/waive a kill criterion; change a pre-registered effect size | ✘ | ✔ (logged) | ✔ |
| Approve external release (paper submission, dataset publication, public claim) | ✘ | ✔ recommends | ✔ decides |
| Add/retire a research program; re-rate a gap | ✘ (may propose) | ✔ (logged) | ✔ |
| Spend money (keys, GPU budget, panels) | ✘ | ✘ | ✔ |
| Modify this protocol | ✘ | ✘ (may draft) | ✔ |

"Fable-tier" = a session on the Fable model, or Jimmy acting as adjudicator when no Fable window exists (post ~2026-07-11 the default is Jimmy).

## 2. Kill-criteria adjudication

1. Kill criteria in RP briefs are **pre-registered**. When an Opus session's results meet a kill condition, the session executes the specified action (halt / downgrade / publish-the-null) *in the same session*, records it in `04-decision-log.md`, and does not continue the killed line "just to see."
2. Borderline cases (result within ±20% of the pre-registered threshold, or the measurement itself is disputable): do **not** self-adjudicate. File a PENDING-RULING (§3) and pause only the affected line — sibling tasks continue.
3. A kill is a result, not a failure. Killed lines get the same write-up quality as successes; several briefs explicitly note the null is publishable.

## 3. PENDING-RULINGS queue

- Location: create `INNOVATION/PENDING-RULINGS.md` on first use (living file, checkbox format).
- Entry format: `PR-NN · date · RP/doc · question · what's blocked · proposer's recommended ruling with reasoning`.
- The proposer's recommendation matters: the adjudicator (Fable-tier or Jimmy) should be able to rule with a yes/no.
- **PROVISIONAL rule** (imported from the FRUITBENCH succession protocol): if a ruling blocks all forward progress and the question is low-stakes-reversible, an Opus session may proceed on its own recommendation marked PROVISIONAL, flagging every downstream artifact with the PR-NN. High-stakes or irreversible questions (external claims, spending, kill-waivers) never go PROVISIONAL.

## 4. Amendment protocol

- Frozen snapshots (flat docs `00`–`06`, field-map deep dives, gap dossiers, idea dossiers as first authored): amendments are **new dated files** placed in the same folder (`YYYYMMDD-<target>-amendment.md`) stating what changes and why. Never in-place edits.
- Living files (this folder's `04-decision-log.md`, `../07-opus-handoff.md`, `PENDING-RULINGS.md`, dossier OPUS-EXPAND checklists): in-place appends/checkbox updates allowed; never delete prior entries.
- **Dossier expansion rule:** Opus sessions deepening a gap/idea dossier append new sections *below* the Fable kernel sections and mark them `## [OPUS-EXPANSION YYYYMMDD]`. Kernel sections (Statement, Why it matters, What closing looks like, CEI response / The idea, Implications for CEI) are frozen — disagreement goes through a PR, not an edit.

## 5. Standing review cadence

- **Bet review:** July 2027 per `10-FIELD-MAP/07-bets-registry.md` — new dated file scoring B1–B5 (+S-bets).
- **Atlas refresh:** when ≥5 gaps have materially changed state (tracked via decision log), a new dated gap-atlas revision is warranted — full-document, not per-gap edits.
- **Handoff hygiene:** every session touching INNOVATION appends one line to `04-decision-log.md` (date, session tier, what changed). This substitutes for per-session handoff docs *within* this folder; vault-level handoff rules still apply to the session as a whole.

## 6. Evidence discipline (applies to every INNOVATION output)

1. Citation classes: **VERIFIED** (fetched/confirmed), **SEARCH-CONFIRMED** (from sweeps, unfetched), **⚠ UNCONFIRMED** (flagged IDs in `../04-missing-literature.md`). External prose may cite VERIFIED only; internal docs may cite all three *with class visible*.
2. LLM-judge results always carry the G-09 (judge corruption) caveat in methods.
3. Synthetic/mock outputs are never reported as measurements (the SERMONMOUNT lesson) — label harness-validation as such, everywhere, without exception.
4. Counting claims (items, papers, effect Ns) are verified against source before appearing in prose (vault Data Integrity rule).
