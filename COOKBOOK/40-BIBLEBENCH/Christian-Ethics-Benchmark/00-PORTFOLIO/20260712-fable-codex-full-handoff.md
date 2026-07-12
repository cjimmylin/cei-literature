<!-- WALKWORTHY-CANARY-7f3e2026 -->
# WALKWORTHY — 2026-07-12 FULL HANDOFF: all future work → Codex (zero open judgment)

**Author:** Claude Fable, 2026-07-12 ruling session (authority check passed; Jimmy
present throughout). **Supersedes operationally:** `20260711g-codex-boot-prompt-and-reentry.md`
and every earlier boot prompt (`20260711i`/`m`, `20260712-fable-pr9-adjudication-boot-prompt.md`)
— all remain immutable records. **This is the single entry point for every future
WALKWORTHY session.** The paste-ready boot prompt is §8.

---

## 1. Why this handoff is different from the previous ones

Every prior handoff left open judgment (rulings pending, STOP triggers armed). As of
this session there is **none**: PR-9 is CLOSED, STOP-8 is DISCHARGED, and the entire
ratification backlog is RATIFIED. Everything that remains is mechanical execution
(Codex), human labor (Jimmy), or data-dependent branches whose actions are pre-decided
(FR-1..FR-17 + the G4 branch table + the release formula). No further Fable sessions are
planned; the one future review-worthy moment (P7 verdict-assembly review before release)
is pre-assigned to the **"Opus adversarial-review memo → Jimmy"** pattern.

## 2. State snapshot (all verified this session)

- Suite: **276 green**. O5 Phase 0 complete; forward transcript persistence FIXED and
  contract-tested; O5 paused before W1 — now UNBLOCKED (see §3).
- Grok-4 probe: **FAILED 0/10 (HTTP 404)** — evidence at
  `runs/20260711-o5-grok4-probe/probe_report.md`. **Never re-probe, never re-litigate.**
- Quantified surface (Codex, twice-verified): panel 2,064 records; full unresolved §B
  surface **3,172 `needs_adjudication` cells / 1,297 records**; the retired refusal-tag
  selector held 609 records / 1,767 cells; 20 non-tie-breakable pendings (11×05
  allocation-parse, 9×09 arbiter-first). Mistral own-family exposure on the full
  surface: **225 records / 580 cells**.
- Exact historical six-SUT 02/07 cost: **$26.681701** (378 records, 10,037 calls) — the
  re-execution baseline, not a price guarantee.
- Historical O4 run `runs/20260711-o4-panel/` (2,064/2,064, $48.75) is IMMUTABLE and
  still lacks 723/907 required 02/07 turn responses — hence the new run below.

## 3. Rulings issued/collected this session (the complete authority record)

| Ruling | Content | Doc |
|---|---|---|
| **FR-16** (Fable, ratified R-J11) | W1 = full 3,172-cell §B surface at FR-2 granularity; tie-breaker only on real two-judge disagreements; 05-parse → one bounded re-parse pass then Part-B; 09 arbiter-first → Part-B directly; **Part-B export is CELL-level** | `20260712-fable-FR16-w1-surface-ruling.md` |
| **R-J1** (Jimmy) | NEW immutable six-SUT 02/07 re-execution **AUTHORIZED** (~$26.68 baseline) | `20260712-fable-ruling-session-log.md` |
| **R-J2** (Jimmy) | **Mistral accepted** as tie-breaker (`mistralai/mistral-large-2512`); own-family Part-B burden (≤225 rec/580 cells) accepted; STOP-8 discharged | same |
| **R-J3/R-J4** (Jimmy) | C-4 G5 reference authoring ordered (done this session, §5); C-5 L7 rotation-list formalization **authorized** | same |
| **R-J5..R-J12** (Jimmy) | PR-1(c) · PR-2 · PR-3(§6.4) · PR-4 · PR-6(mean+sensitivity) · PR-8(FR-1..15) · FR-16 · W4 06-fixes — **ALL RATIFIED**; release language needs no "pending ratification" markers | same |
| **FR-17(a–c)** (Fable) | Part-B triage = Part-A wave order {02,07,01}→{03,04,05,06}→{08,09,10}; post-tie-breaker contested → cell-level Part-B (excluded if unlabeled, counts against FR-1); tie-breaker gets byte-identical rubric text | same, §3 |
| **FR-18(a–b)** (Fable) | G5 interpretation: consensus-tagged DSP cases use the attested METHOD split (06 K01); design-09's opposite-conclusion axis = the reported (unkeyed) DSP pole with keyed core + floors constant. Flagged for Jimmy with the promotion one-liner | `20260712-fable-G5-reference-review.md` §2 |

Still open by design: **PR-7** (G6 redefinition — next cycle only). Release sign-off
remains **Jimmy-only, always** (framework §6 trigger 9).

## 4. THE EXECUTION SEQUENCE (zero-judgment; never skip ahead; never reorder)

1. **Baseline:** `cd harness && pytest` → confirm 276 green before anything else.
2. **NEW immutable 02/07 re-execution** (Jimmy-authorized): six SUTs, the exact O4
   roster, designs 02+07 full surface, explicit model slugs on SUTs/judges/classifier
   (`panel.py` defaults ≠ frozen pair — FR-12). NEW dated run dir. Before treating the
   spend as complete: **verify every turn response is persisted against the
   data-contract test** added in the transcript-persistence fix. Budget guard: expect
   ~$27; if projected cost exceeds 2× baseline (~$55), STOP and ask Jimmy.
3. **TDD builds (may start before/parallel with step 2):**
   a. Cell-aware Part-B exporter per FR-16(d): one row per unresolved cell (turn/seat/
      pair/criterion-cell/item), parent-record context attached, wave-ordered per
      FR-17(a). Cell counts are the workload metric.
   b. Tie-breaker module per FR-16(b) + FR-17(c): input = cells with a real two-judge
      disagreement; model = `mistralai/mistral-large-2512` (explicit slug); rubric =
      byte-identical text the pair received; own-family (mistral-SUT) cells → Part-B,
      never tie-broken.
   c. 05 bounded re-parse pass per FR-16(c): regression-locked (no previously-parsed
      value may change); leftovers → Part-B.
4. **W1 adjudication:** run the tie-breaker over the full 3,172-cell surface (02/07
   cells from the NEW run of step 2; other designs from existing artifacts).
5. **W2:** §E Δ(J) home-advantage permutation test (10,000 resamples, α=0.01), per
   judge × design, on existing records. FR-7 separates severity offsets (not
   disqualifying) from own-family inflation (disqualifying, per-cell rerouting).
6. **W3:** post-adjudication recompute of all §B statistics + G1/G2/G3/G8 readings →
   NEW dated readings file (never overwrite `20260711b-…`). FR-1 completeness check
   per design×model (≤10% unresolved S-units) gates every verdict.
7. **W4:** G5 driver for 06/09 using the Fable-reviewed reference sets (§5) — blind
   scoring, >0.5 split rule, re-elicit once, persistent → disqualification cascade
   (FR-8). The ratified W4 06-fixes may now be promoted into `DESIGNS/06-*.md`.
8. **W5:** G7 perturbation batteries — paraphrase author `mistralai/mistral-large-2512`
   (FR-14, disclosed also-a-SUT), L7 rotation list (authorized R-J4 — formalize it
   machine-readable, TDD, before W5 needs it), lint L1–L9, flips on adjudicated
   outcomes, perturbed-cell disagreements through the same W1 path.
9. **P5:** G4 per label wave as Jimmy's Part-A labels land (`judge_validation.py`,
   κ table, branch per the frozen G4 branch table). **P6:** Part-B export → Jimmy
   labels → final recompute. **P7:** verdict assembly per the frozen release formula →
   O5 report (NEW dated) → **hand the report to an Opus adversarial-review session →
   memo → Jimmy sign-off.** Labels absent at P5 time → stop at P4-complete and report
   "O5 blocked on labeling" (framework §6 trigger 10).

**Parallel lanes while any step waits:** exporter/tie-breaker TDD, 05 re-parse, L7
list, W4 06-fix promotion, dashboard upkeep.

## 5. G5 reference status (C-4 lane)

Drafted this session by two Opus agents under the two-agent rule and adversarially
reviewed by Fable in the main loop. Drafts (gitignored): 
`00-PORTFOLIO/20260712-G5-06-references-DRAFT.md` (7 carried+fixed + 3 new pairs +
executable FA-1 lint spec) and `00-PORTFOLIO/20260712-G5-09-references-DRAFT.md`
(opposite-conclusion arbiter pairs, all DSP cases). Fable review notes:
`00-PORTFOLIO/20260712-fable-G5-reference-review.md` — **verdict GO, conditional on
its §4 directed mechanical items (a)–(d)** (L-6 D01 fact-verify, K03 CHECK-4 scrutiny,
D01/L03 trims, executable FA-1 lint RED→GREEN), which Codex executes before any G5
run. FR-18(a)/(b) rule the two G5 interpretation gaps (method-split for
consensus-tagged cases; 09's reported-pole surface). **Promotion into the run
configuration requires Jimmy's one-liner after he reads the review notes** ("G5
reference sets approved for gate use, FR-18 ratified") — log it in PENDING-RULINGS
when given. Until promoted, the G5 driver (step 7) may be BUILT and mock-tested but
not run for record.

## 6. Jimmy's remaining obligations (labor, not decisions)

1. Part-A labels: 439 blind units, 3 waves (wave 1 = {02,07,01}, 84 units), ~25–30 h.
2. Part-B labels: ≤580 own-family cells + FR-17(b) residue, wave-ordered (FR-17(a)).
3. 2nd-labeler recruitment (or declare the disclosed test–retest fallback).
4. G5-reference promotion one-liner (§5).
5. OpenRouter balance ≥ ~$30 before step 2 (the 32768 cap is in place; see AGENTS.md
   OpenRouter gotcha).
6. Release sign-off at P7 (always his).

## 7. Guardrails (unchanged, restated once)

FROZEN, interpret-only: prereg §B/§C/§E + FR-1..FR-17 + the G4 branch table + release
formula. FIX-MECHANICS-ONLY (no item edited from model performance). Report
immutability: NEW dated files, never overwrite (`project-dashboard.html` is the sole
exemption — update IN PLACE per its header protocol). HOLDOUT never loaded. Never
delete — `mv` to `RECYCLE-BIN/`. Shared git index: `git log -1` AND
`git diff --cached --name-only` before staging; explicit WALKWORTHY pathspecs;
fast-forward pushes only. Explicit model slugs on every judge/classifier/tie-breaker/
paraphrase call. STOP-AND-ASK triggers: framework §6 items 2–7 and 10 remain live
(data-dependent); item 9 (release) is Jimmy-only; items 1 and 8 are resolved. Anything
judgment-shaped that is not pre-decided → ask Jimmy in-session and log verbatim in
PENDING-RULINGS, or park it there. **Codex never rules.**

## 8. BOOT PROMPT (paste into every future Codex session)

```text
WALKWORTHY O5 execution session. SCOPE LOCK: work ONLY inside
CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark/ — no sibling benches,
never load HOLDOUT/, never delete (mv to RECYCLE-BIN/).

ON OPENING: read (1) 00-PORTFOLIO/project-dashboard.html (Live status + §12), (2) the
NEWEST dated handoff in 00-PORTFOLIO/ (state may have moved past this prompt — skip
anything already done), (3) 00-PORTFOLIO/20260712-fable-codex-full-handoff.md (THE
plan; its §4 sequence is binding), (4) PENDING-RULINGS.md, (5) AGENTS.md. Build specs:
20260711e (transition package), 20260711d (FR-1..FR-15 + G4 branch table + release
formula), 20260712-fable-FR16-w1-surface-ruling.md + 20260712-fable-ruling-session-log.md
(FR-16/FR-17 + Jimmy rulings R-J1..R-J12). FROZEN — interpret, never rewrite:
20260710-fable-gate-prereg-pilot-adjudication.md §B/§C/§E.

ALL JUDGMENT IS PRE-MADE. PR-9 closed; STOP-8 discharged; every PR ratified. You never
rule: anything judgment-shaped not covered by FR-1..FR-17/the G4 branch table → ask
Jimmy if present (log his words verbatim in PENDING-RULINGS) or park it there and work
another lane. Grok-4 is DEAD (0/10) — never re-probe. Tie-breaker =
mistralai/mistral-large-2512, explicit slug, byte-identical rubric, own-family cells →
Part-B. W1 surface = ALL 3,172 needs_adjudication cells (FR-16), NOT the 609-record
selector.

EXECUTE handoff §4 IN ORDER: 276-test baseline → NEW immutable 02/07 six-SUT
re-execution (Jimmy-authorized ~$26.68; verify full-turn persistence via the
data-contract test; STOP if projected >$55) → TDD cell-aware Part-B exporter +
tie-breaker + 05 re-parse → W1 → W2 Δ(J) → W3 recompute (NEW dated) → W4 G5 (refs need
Jimmy's promotion one-liner first) → W5 G7 (formalize the L7 list first — authorized) →
P5 G4 per label wave → P6 Part-B → P7 verdicts → Opus review memo → Jimmy. Never skip
ahead; work parallel lanes (exporter TDD, 05 re-parse, L7 list, W4 06-fix promotion)
when blocked.

CONSTRAINTS: report immutability (NEW dated files; dashboard = sole in-place
exemption); FIX-MECHANICS-ONLY; explicit model slugs everywhere (panel.py defaults ≠
frozen pair); shared git index — git log -1 AND git diff --cached --name-only before
staging, explicit WALKWORTHY pathspecs, fast-forward pushes only; no gate verdict
until FR-1's ≤10% completeness holds on the design; labels absent at P5 → stop at
P4-complete, report "blocked on labeling".

ON CLOSING: update project-dashboard.html IN PLACE (Live status, §12 next-session
instructions, Last-updated, Changelog row); write a NEW dated handoff; commit +
fast-forward push WALKWORTHY paths only.
```

## 9. Claude/Fable re-entry protocol (if ever needed)

Read the NEWEST dated handoff + dashboard FIRST — Codex sessions land frequently; the
state will have moved. Claude's role is **review and escalation adjudication only**
(e.g. a framework §6 trigger fired, or the P7 report review) — never redo or re-derive
Codex's mechanical work. All prior rulings stand; new rulings require Jimmy or a
delegated window, logged in PENDING-RULINGS.

## 10. File map (this session's additions)

- `20260712-fable-FR16-w1-surface-ruling.md` — FR-16 (ratified)
- `20260712-fable-ruling-session-log.md` — R-J1..R-J12 verbatim + FR-17(a–c)
- `20260712-fable-G5-reference-review.md` — Fable adversarial review of the G5 drafts
- `20260712-G5-06-references-DRAFT.md` / `20260712-G5-09-references-DRAFT.md` —
  gitignored reference drafts (pending Jimmy promotion)
- `PENDING-RULINGS.md` — all annotations (PR-9 CLOSED; PR-1/2/3/4/6/8 RATIFIED)
- `AGENTS.md` — re-pointed to this handoff
- `project-dashboard.html` — updated in place (§12 = the §8 boot prompt)
- this handoff

*Session made zero live API calls; spend $0. HOLDOUT untouched. Sibling benches untouched.*
