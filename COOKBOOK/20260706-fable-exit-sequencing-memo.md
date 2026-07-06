# 20260706 — Fable Exit-Sequencing Memo (Session 3 capstone, BINDING)

> **Provenance.** This is the Session-3 capstone the approved Fable Exit Plan
> (`COOKBOOK/20260706-fable-exit-plan.md`) named `20260710-fable-exit-sequencing-memo.md`.
> It is written 2026-07-06 — early — because every prerequisite landed the same day the plan
> was approved: all S2 gate items were discharged in their own parked threads, and all five
> tracks front-loaded their Fable governance before parking. **The `20260710-…` filename will
> not exist; this document is the master post-window reference.** Authored in a Fable session;
> inventory gathering delegated (Sonnet), all rulings here are Fable main-loop.
>
> **Authority.** BINDING alongside — never instead of — the per-track protocols it indexes.
> Where this memo and a per-track protocol both speak, the per-track protocol wins on its own
> track; this memo governs only (a) cross-track sequencing, (b) the post-window meaning of
> "Fable-tier" labels, and (c) the three gaps closed in §4. The 2026-07-05 adjudication memo
> and every 2026-07-06 BINDING ruling doc remain unrelitigatable by Opus sessions.

---

## §0 — Ledger: the exit plan is CLOSED

**Session 1 (2026-07-06):** DONE — P0 adjudication protocol (F1), post-execution rulings (F2),
six-design spot-check all-CLEAN (F3), R-1/R-2 executed. `c8ffec506..fbaa59bc8`.

**Session 2 (gate releases):** DONE — but in the parked per-track threads, not as a separate
sitting:
- TC scaffold spot-check **PASS** + TC-9 wave-1 **RELEASED** — `3849bf6a9`, protocols
  completed through `11d27c312`.
- CORINTHLOVE STATUSGAME **CONDITIONAL GO discharged by Fable** (session f front-load; memo
  `40-BIBLEBENCH/CORINTHLOVE-REVIEWS/20260706-statusgame-post-d03-re-review.md`, RG-1…RG-4
  binding). ⚠ Uncommitted at time of writing — see §5 item 1.

**Session 3 (this memo):** DONE — closes the pending-Fable inventory (§1), fixes the
cross-track build order (§2), the delegation downgrade map (§3), and the residual governance
gaps (§4). FABLE-WEEK.md and the `cookbook-project-state` memory now point here.

No further Fable sessions are REQUIRED before the window closes ~2026-07-11. §2.4 names the
single best discretionary use of any remaining window time.

---

## §1 — Pending-Fable inventory (R1–R4, B1–B8): defined and closed

The exit plan's verification clause referenced this inventory without enumerating it. It is
hereby defined as follows, and every item is closed with a named fallback:

| # | Item | Status | Governing artifact (fallback owner post-window) |
|---|------|--------|--------------------------------------------------|
| R1 | DUPLEX P0 adjudication | CLOSED | `20-DESIGNS/DUPLEX-P0/20260706-p0-adjudication-protocol.md` — Opus adjudicates from the outcome table; FAIL branch: Opus drafts re-scope, **Jimmy approves**; unlisted pattern: STOP → Jimmy |
| R2 | Post-execution rulings (02/04/05 drafts, CRUX, item bank) | CLOSED | `20-DESIGNS/REVIEWS/20260706-fable-rulings-post-execution.md` (BINDING; OA upgrade REQUIRED before P2 panel spend) |
| R3 | Six-design insurance spot-check | CLOSED | `20-DESIGNS/REVIEWS/20260706-six-design-spotcheck.md` — all six CLEAN; build-spend insurance satisfied |
| R4 | Exit-sequencing memo | CLOSED | **this document** |
| B1 | FRUITBENCH FO-8 second-pass gate | CLOSED | `FRUITBENCH-REVIEWS/20260706-fo8-gate-protocol.md` + `…-succession-protocol.md` — Opus mechanical; threshold deviations → PENDING-RULINGS → Jimmy |
| B2 | CORINTHLOVE megamatrix CO-6a/6b | CLOSED | `CORINTHLOVE-REVIEWS/20260706-fable-megamatrix-analysis-prespec.md` — frozen above its §8; deviations → Jimmy (§3 map) |
| B3 | TC-v2 PARAMOUR/PALTER P0-fail stops | CLOSED | `TENCOMMANDMENTS-REVIEWS/20260706-wave2-deferred-adjudication-protocol.md`; the two "live Fable ruling" clauses downgrade per §3 |
| B4 | TC-v3 deferred / P0-lite-fail stops (VILLAGE/PRISM/ASSEMBLY et al.) | CLOSED | same wave-2/deferred protocol — mechanical entry verdicts; unlisted outcomes → FABLE-QUEUE (post-window meaning: §3) |
| B5 | SERMONMOUNT WITNESS P1 gate | CLOSED | `SERMONMOUNT-v2/20260706-PARKED-opus-reentry-prompt.md` + pre-registration (G1–G5, §A1–A8); §A7 reserved judgments → collect-and-defer per §3 |
| B6 | Frozen-registry changes (C1–C16, F/W/P, S01–S40, TC registries) | CLOSED **here** | unified rule in §4.1 (no prior cross-track rule existed) |
| B7 | Delegation-tier downgrade map | CLOSED **here** | §3 |
| B8 | FABLE-WEEK.md + memory update | CLOSED | done this session (see handoff `COOKBOOK/20260706g-fable-exit-session-handoff.md`) |

---

## §2 — Cross-track build order (post-window Opus sessions)

Five tracks, all parked with Opus-executable re-entry prompts. Rules of engagement: one track
per Opus session; path-scoped commits; `git log -1` before every commit (parallel sessions
share the index); every session ends with a dated handoff in its own chain.

### §2.1 Immediately runnable (credential-independent) — priority order

Priority is by *unblocking leverage*: how much downstream work each session releases.

1. **FRUITBENCH — THORNS spine fixes S-1…S-5, S-10 → regression → copy** (re-entry:
   `FRUITBENCH-REVIEWS/…20260706-unfenced-build-handoff.md`). Highest leverage: the spine is
   copied by all 9 remaining v2 designs, and S-1/S-2 are the hard-block on live mode — this
   session must precede any credentialed FRUITBENCH run. Then 04 UNFENCED P1 (self-audit
   Part A mandatory per the P1 review protocol).
2. **SERMONMOUNT — MF-1…MF-8 fixes + pre-reg items 3–5** (re-entry:
   `SERMONMOUNT-v2/20260706-PARKED-opus-reentry-prompt.md`). Do this *before* keys arrive so
   the credential moment is not wasted; live P1 then applies the pre-registration mechanically.
3. **10CBench — ZEROSUM build** (wave-1 anchor; re-entry:
   `TENCOMMANDMENTS-REVIEWS/20260706-PARKED-opus-reentry-prompt.md`). Longest chain: wave-2
   release condition G needs ≥3 of 5 wave-1 designs through discrimination gates, so wave-1
   must start early even though its runs are credential-gated later.
4. **CORINTHLOVE — DIMGLASS bank build** (CO-8 order ① of ⑤; per session-f handoff §"what
   remains", each build followed by a rubric review session). Second-longest chain (5
   sequential banks feed the megamatrix), so interleave early.
5. **COOKBOOK core — nothing buildable without Jimmy.** CRUX P1 waits on the validation-survey
   greenlight; 02/04/05 drafts wait on human read-through; P0 waits on credentials. Do not
   spend Opus sessions here until an input lands.

After the first pass, continue each chain **round-robin, biased toward whichever chain is
currently blocking a credentialed run** (i.e., don't build TC design #3 while THORNS S-1/S-2
sit unfixed and keys are available).

### §2.2 The moment credentials land, the queue re-orders

**DUPLEX P0 jumps everything.** It is the only pending gate that decides a fork in the core
roadmap (pass → DUPLEX generator build; fail → CRUX build-first, already pre-registered).
Sequence: verify Codex `exec` single-turn flags → P1.5-style dead-cell prune → full P0 run →
adjudicate per the P0 protocol. Then, in order: SERMONMOUNT live P1 (pre-reg applies
mechanically), FRUITBENCH first REAL THORNS calibration, TC wave-1 runs as builds complete.

### §2.3 Jimmy's parallel critical path (independent of all Opus sessions)

1. **Commit approval for the CORINTHLOVE c–f set** (§5 item 1 — several B-item pointers in
   this memo dangle until committed).
2. **Credentials:** `ANTHROPIC_API_KEY`; Codex CLI OAuth; the Google/Gemini decision (P0's
   cross-vendor claim wants all 3 vendors; SERMONMOUNT's third judge family prefers Gemini).
3. **Humans:** G3 mini-norm (DUPLEX); TC panels; SERMONMOUNT human-baseline raters;
   CORINTHLOVE consultants/validators (TONGUES, CRUCIBLE, CROSSROADS/MANYMIRRORS).
4. **Vault-source decisions:** Gemini-Safety → arXiv 2403.13793 replacement OK?; the
   "Simple Probes / Sycophancy" conflated stem (needs an intended-source decision).
5. Human read-through of the 02/04/05 drafts and the P0 item bank before any panel/API spend.

### §2.4 If credentials land before ~2026-07-11 (discretionary Fable use)

Spend remaining window on **live-result adjudication only**, in this order: DUPLEX P0 branch
call → first real THORNS calibration → SERMONMOUNT live-P1 gates. Everything else is already
mechanical and would waste window on work Opus can do.

---

## §3 — Delegation-tier downgrade map (BINDING)

**The unified rule.** After ~2026-07-11, every label of the form "Fable-tier", "Fable
adjudicates", "live Fable ruling", "park to FABLE-QUEUE", or "wait for Fable" means exactly
this: **Opus prepares a decision memo — PR-NN format: question, evidence, ≥2 options, a
recommended least-committal interim path — files it to the owning track's queue, and Jimmy
decides.** Nothing is silently decided at a lower tier; if Jimmy defers, the item waits and
all dependent results carry a PROVISIONAL mark until resolved. If a future Fable window
opens, the queues are worked top-down under the existing protocols; this memo stays binding
until superseded by a Fable session.

Owning queues: FRUITBENCH → `FRUITBENCH-REVIEWS/20260706-PENDING-RULINGS.md` (append-only);
TC → `TENCOMMANDMENTS-REVIEWS/FABLE-QUEUE/` (dated memos); CORINTHLOVE → dated memo in
`CORINTHLOVE-REVIEWS/`; SERMONMOUNT → dated memo in `SERMONMOUNT-v2/` (§A7 items:
collect-and-defer, never one-off); COOKBOOK core → dated memo in `20-DESIGNS/REVIEWS/`.

Specific label conversions:

| Standing label (source) | Post-window owner |
|---|---|
| P0 pass/fail "Fable-tier if in-window" (core handoff) | Opus mechanical per P0 protocol; FAIL re-scope + any unlisted pattern → **Jimmy** |
| TC "Fable-level" kill criteria (KEEPER, PARAMOUR, GOLEM SA second-fail, TURNCOAT) | park to FABLE-QUEUE → **Jimmy** (memo first) |
| TC PALTER BT gate ≤2 families passing ("live Fable ruling before fallback framing") | **Jimmy** (memo first); wave continues on other designs meanwhile |
| SERMONMOUNT §A7 reserved judgments | collect-and-defer → **Jimmy** only if blocking; else wait |
| CORINTHLOVE CO-8-⑤ fail (MANYMIRRORS pause), prespec §8 amendments, shared panel <8 models | **Jimmy** (memo first); MANYMIRRORS stays paused meanwhile |
| FO-8 threshold deviations; attacker-persona re-norm; new D-orders; headline claims | **Jimmy only** (Opus may draft, never issue) — unchanged from succession protocol |
| Frozen-registry changes (any track) | **Jimmy only** — §4.1 |
| CRUX P3 gate-b probe-trainer wiring; OA-upgrade-before-P2 | Opus executes the R2 ruling as written; any relaxation → **Jimmy** |

**Hard floor (no memo substitutes for these):** registry edits, gate-threshold deviations,
headline/external claims, and the DUPLEX-deprioritization announcement are Jimmy-only acts;
an Opus memo is their input, never their execution.

---

## §4 — Gap closures (the three rulings new in this memo)

### §4.1 Unified frozen-registry rule (closes B6)

Frozen surfaces, all tracks: CORINTHLOVE C1–C16; FRUITBENCH F/W/P + `FRUITBENCH-v2/00-registry.md`
+ every brief's do-not-change ledger; SERMONMOUNT S01–S40 + LOCKED sections; the TC frozen
registries (incl. the v3 TC-7 registry); the locked design specs, the 2026-07-05 adjudication
memo, and all 2026-07-06 BINDING ruling docs. Rule, generalizing the FRUITBENCH succession
protocol vault-wide: **Opus never edits a frozen surface.** Opus may draft a change proposal
(PR-NN format) to the owning queue (§3); **Jimmy ratifies or defers**; until ratified,
dependent work takes the least-committal path and its results are marked PROVISIONAL. No
track's local rule is loosened by this generalization; where a local rule is stricter, it wins.

### §4.2 FABLE-QUEUE / "wait for Fable" semantics (closes the dangling-referent gap)

Defined in §3's unified rule. Explicitly: a queue entry is not a dead letter — filing one
obliges the filer to also name the interim path, and obliges the next session touching that
track to surface unresolved entries in its handoff. Queue entries never expire silently.

### §4.3 INTRA board-charter routing (closes GAP-1)

`20-DESIGNS/20260706-04-intra-board-charters-and-rater-protocol.md` is design-operationalization,
not a succession doc, and carried no routing rule. Ruling: Opus applies the charters as
written (composition, firewall, positionality standards); recruitment is Jimmy's; any
board-composition, arbitration, or veto-interpretation question not answered verbatim by the
charter or by the INTRA rulings in R2 (veto-after-κ, named arbiter pre-P1) → PR-NN memo to
`20-DESIGNS/REVIEWS/` → Jimmy. The charters doc joins the frozen surfaces of §4.1 once the
first rater is recruited under it (before that, Opus may still amend it via normal drafting
with a dated changelog).

---

## §5 — Standing cautions carried forward

1. **The CORINTHLOVE 2026-07-06 c–f artifact set is UNCOMMITTED** (three revision sets, the
   STATUSGAME re-review, the megamatrix prespec, the bank rubric, the session-f handoff).
   This memo's B2 and STATUSGAME pointers dangle until Jimmy approves that commit. If Jimmy
   declines any part, the affected pointer reverts to its pre-session-f state and the item
   re-opens as a Jimmy decision — flag in the next CORINTHLOVE handoff either way.
2. Parallel sessions share the git index: `git log -1` before every commit, path-scoped
   staging only, never `git add -A` at repo root.
3. Four sub-project disclosures whenever their numbers appear (NormEval F1–F7 elicited; MP
   self-administration; RV same-vendor; CG N_eff≈3.4). Digest statistics copied verbatim,
   never recomputed.
4. ⚠ Haiku 3.5 is retired; the P0 protocol's substitution ruling (`claude-haiku-4-5`, never
   pin) is already binding — no session should re-open it.
5. BibleBench scope isolation stands: each bench folder is its own scope; this memo indexes
   their gates but no session may cross-pollinate designs between benches.
