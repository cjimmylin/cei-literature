# 20260706 — Fable Exit Plan (approved; vault copy of record)

> **Provenance.** Authored and approved 2026-07-06 in a Fable session (plan-mode artifact,
> originally at `~/.claude/plans/since-i-won-t-have-curious-fog.md`; this vault copy is the copy
> of record). **Status at save time: Session 1 EXECUTED** (commits `c8ffec506..0e44e85c5`; see
> `20260706-fable-session1-handoff.md`). Session 2 = gate releases (TC scaffold spot-check +
> STATUSGAME sign-off, both READY). Session 3 = exit-sequencing memo by ~07-10.
> Session-status updates belong in the handoff chain, not edits to this plan.


## Context

Fable access ends ~2026-07-11. Per the tiering protocol, Fable's comparative advantage is
judgment (adjudication, adversarial review, pre-registration of decision rules); Opus executes.
Most remaining gates in the COOKBOOK/BibleBench portfolio will fire **after** the window closes
(DUPLEX P0 is credential-blocked; FRUITBENCH FO-8 and CORINTHLOVE megamatrix need pilots that
don't exist yet). So the strategy is: **convert every future Fable judgment into a binding,
pre-registered written rule now**, resolve the ready-now judgments, and release the gates whose
Opus prerequisites can finish inside the window if dispatched immediately.

**Scope (per Jimmy):** CEI-Lit-WS / COOKBOOK only (including `COOKBOOK/40-BIBLEBENCH/`).
CEI-AI-Statements (Governance Symphony centerpiece etc.) explicitly OUT — own sessions.
**Budget:** 3–5 Fable sessions. **P0 credentials:** assumed NOT provisioned in-window → pre-register.
**Parallel Opus:** yes — Jimmy dispatches prerequisite Opus sessions immediately.

## Fable Session 1 (this session) — binding decision artifacts, all READY NOW

### F1. DUPLEX P0 pre-registered adjudication protocol + Haiku-3.5 ruling
The single highest-leverage artifact: post-window Opus must be able to adjudicate P0 mechanically.
- **Read:** `COOKBOOK/20-DESIGNS/03-moralpsych-duplex.md` §6–7; `COOKBOOK/20-DESIGNS/DUPLEX-P0/runner/README.md`
  (open items); `COOKBOOK/20-DESIGNS/REVIEWS/20260705-adjudication-memo.md` (portfolio consequences).
- **Write:** `COOKBOOK/20-DESIGNS/DUPLEX-P0/20260706-p0-adjudication-protocol.md` containing:
  1. **Haiku-3.5 substitute ruling** (the open validity judgment): Haiku 3.5 — the model behind the
     motivating MP-DP effect — is retired (2026-02-19). Rule on substitute (`claude-haiku-4-5`) vs
     legacy-snapshot pin, AND the interpretive rule (e.g. "non-replication of MP-DP on a successor is
     NOT itself a P0 fail; only gates G1–G3 decide — MP-DP was motivation, not criterion").
  2. **Edge-case decision table**: 2-of-3 gates pass; G1 pass with high dead-cell fraction; G2 pass on
     exactly one manipulation; G3 fallback-only direction; Codex CLI cannot be constrained to
     single-turn (drop to 3 Anthropic subjects? → what that does to "cross-vendor"); Gemini still
     deferred at run time (5/9 subjects — is the KB04 §6.2 bar still meaningful?).
  3. **Action-on-outcome**: verbatim restatement of the pass/fail branch + what Opus may conclude
     alone vs what must be flagged to Jimmy.

### F2. Post-execution rulings memo (adjudicate what Opus built on 2026-07-06)
- **Read:** the three drafts (`COOKBOOK/20-DESIGNS/20260706-02-frameshift-subvariant-sheets.md`,
  `...04-intra-board-charters...md`, `...05-cultivate-codesign-brief...md` — each ends with documented
  assumptions: 5 + 8 + 8), `COOKBOOK/ENGINE/README.md` (limitations), a ~15-item stratified sample of
  `COOKBOOK/20-DESIGNS/DUPLEX-P0/items/20260706-p0-item-bank.md`.
- **Write:** `COOKBOOK/20-DESIGNS/REVIEWS/20260706-fable-rulings-post-execution.md` (D-order style,
  binding): accept/modify each documented assumption; rule on CRUX engine limitations (randomized
  balanced fraction acceptable for pilot? orthogonal-array upgrade required before P3? fine-tune-probe
  trainer wiring deadline); item-bank spot-verdict (obfuscation leaks, Greene-subset adequacy,
  monitored/unmonitored wrapper quality); FRAMESHIFT virtue-account recommendation
  (Hursthouse/Slote/Swanton — recommendation only, pick is Jimmy's).

### F3. Six-design insurance spot-check (predecessor queue item 4 — never done)
- **Read:** each of `COOKBOOK/20-DESIGNS/0{1..6}-*.md` — grep for X1–X6 sections + read each
  Critical-fix section against `REVIEWS/20260705-adjudication-memo.md`. Delegate the mechanical greps
  to a Sonnet agent; Fable reads only the judgment-relevant sections.
- **Write:** `COOKBOOK/20-DESIGNS/REVIEWS/20260706-six-design-spotcheck.md` (verdict per design:
  CLEAN / defect list).

### F0 (Jimmy, in parallel — enables Session 2)
Dispatch now, in separate Opus terminals:
- **TENCOMMANDMENTS Sessions A → B → C** per
  `COOKBOOK/40-BIBLEBENCH/TENCOMMANDMENTS-REVIEWS/20260706-revision-orders.md` (A first — it writes
  the 09-WITNESS / 10-APPETITE scaffolds that block everything).
- **CORINTHLOVE Revision Session 1** per `COOKBOOK/20260706-corinthlove-next-session-prompt.md`
  (includes the D-03 STATUSGAME fix + Opus re-review).
- (Stretch) **SERMONMOUNT WITNESS build** per `SERMONMOUNT-v2/20260706-next-session-handoff.md` —
  its P1 gate needs model runs, so only worth it if credentials appear.

## Fable Session 2 — gate releases (once F0 prerequisites land)

- **TC spot-check + TC-9 wave release** (the structurally most important BibleBench gate — nothing
  builds until it): read the two new scaffolds end-to-end + one revised design per session A/B/C,
  run the acceptance greps in `20260706-revision-orders.md` §spot-check, then either release the
  TC-9 first build wave (ZEROSUM→SKIM→PALTER→TABLETS→SOVEREIGN) or issue fix orders.
  **Write:** dated release/fix memo in `TENCOMMANDMENTS-REVIEWS/`.
- **CORINTHLOVE STATUSGAME sign-off**: read the Opus re-review of the D-03 revision; confirm the
  framing/incentive isolation. **Write:** sign-off note (dated, in `CORINTHLOVE-REVIEWS/`).
- If A/B/C are NOT done in time: skip; their release criteria are already mechanical (acceptance
  greps exist) — record in the exit memo (Session 3) that Opus may self-release on green greps +
  one Opus adversarial read, with Jimmy notified.

## Fable Session 3 (capstone, last session before ~07-11) — the exit memo

**Write:** `COOKBOOK/20260710-fable-exit-sequencing-memo.md` — the master "what Opus refers to
later" artifact:
1. **Cross-track build order** post-window (COOKBOOK core: P0-when-credentialed → branch → CRUX
   pilot; BibleBench: TC-9 wave, FRUITBENCH build order, SERMONMOUNT slate, CORINTHLOVE revisions),
   with explicit interleaving/priority when tracks compete for Opus sessions.
2. **Pre-registered fallback rules for every post-window Fable gate** — for each of: FRUITBENCH FO-8
   second-pass gate; CORINTHLOVE megamatrix (CO-6a); TENCOMMANDMENTS-v2 PARAMOUR/PALTER P0-fail
   stops; v3 VILLAGE/PRISM/ASSEMBLY P0-lite-fail stops; SERMONMOUNT WITNESS P1 gate; frozen-registry
   changes (C1–C16, F/W/P, S01–S40) — state: the mechanical rule Opus applies alone / what escalates
   to Jimmy / what simply waits (nothing is silently decided at a lower tier).
3. **Delegation-tier downgrade map**: which standing "Fable-tier" labels in handoffs/memories become
   "Opus + rule" vs "Jimmy" after the window.
4. Update `.claude/FABLE-WEEK.md` (mark items done/rolled-off) and the `cookbook-project-state`
   memory to point at the exit memo.

## Execution rules (all sessions)

- Fable stays in the main loop; delegate greps/formatting/file-assembly to Sonnet/Opus agents with
  explicit `model=`. No digest statistics recomputed — copy verbatim with the four disclosures.
- Every artifact: new dated `YYYYMMDD-` file (never edit existing reports), commit atomically
  (check `git log -1` first — parallel Opus sessions will be running!), push at session end,
  end each session with a dated handoff.
- The 2026-07-05 adjudication memo remains binding; none of these artifacts relitigate it.

## Verification

- Session 1: three artifacts exist under `COOKBOOK/20-DESIGNS/{DUPLEX-P0,REVIEWS}/`, committed +
  pushed; each ruling is actionable (an Opus session could apply it without asking anything).
- Session 2: TC-9 wave explicitly RELEASED or HELD-with-fix-orders in a dated memo; STATUSGAME
  signed off or bounced.
- Session 3: exit memo covers every item in the pending-Fable inventory (R1–R4, B1–B8) with a
  named fallback; FABLE-WEEK.md + memory updated; `git log` shows all sessions pushed.
