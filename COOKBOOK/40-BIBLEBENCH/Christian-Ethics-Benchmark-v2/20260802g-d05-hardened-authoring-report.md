# 20260802g — d05 hardened-allocation authoring EXECUTED (38 items; double-keyed, adjudicated)

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content in this file.

Authority: `RULINGS-APPLIED-20260801a` RULING 1 item 1; spec `20260731j` §2.2;
authoring spec `20260802f` (+ its v1.1 addendum). Executed 2026-08-02, $0
(authoring, offline validation, and Claude Code agent dispatches only — no
external API calls). This report is the authoring record and the disclosure of
the double-keying instrument property. It contains NO model-performance
numbers: none exist (no administration has run).

## 1. What was authored

38 hardened allocation items for design 05 (`05-ordoamoris`), all validated at
final stage by `tools/authoring/validate_v4_banks.py`:

- **Public, 30 items** → `datasets/v4/public/design05.jsonl`:
  B21–B24, C21–C23, D21–D23 (drafter A); E21–E23, F21–F23, G21, G22, H21, H22
  (drafter B); A21, A22, I21–I23, L21, L22, M21, M22, N21 (drafter C).
- **Holdout, 8 items (~21 pct), QUARANTINED AT CREATION** →
  `datasets/v4/holdout/design05.jsonl`: B25, C24, E24, G23, I24, L23, M23, N22
  (drafter D). No holdout scenario content passed through the orchestrating
  session's context at any point; ids and rates only.
- WW-05-H01 and WW-05-M01 (ceiling-pinned) are retired by supersession: H21/H22
  and M21/M22 are their hardened same-area replacements. Nothing deleted; the
  v3 public bank is untouched and still pinned.

Difficulty design: every item is infeasible-by-design with a mechanical
certificate (single-token hard floors sum 1.32–1.59 × budget), no exact-fit
floor subset equals any budget, and the keyed-first sacrifice is deliberately
warm/sympathetic while protected claims are dry and owed — inverting the v3
pattern in which the correct sacrifice was also the obvious one. The pinned
parser reports clean constraint parses on every line; every line carries the
canary.

## 2. Pipeline (all agents = Claude Code dispatches, opus tier)

Four parallel drafters (A/B/C public ×3, D holdout) → iterate against the
validator to ALL PASS → stripped blind-keying packets (id, tokens, budget, ask,
constraint text, C-legend ONLY) built by `build_keying_packets.py` → blind
second keyers in fresh contexts under the anti-leakage protocol → disagreement
computation (`walkworthy_v4.ranked_sacrifice`) → fresh-context adjudicators on
the merits → assembly (`assemble_v4_d05.py`) → final-stage validation.
Rejected drafts recorded in the drafters' logs (scratch space), never deleted.

## 3. Defect classes found mid-flight and mechanized into the validator

1. **Escaped-keyed-first** (drafter C's finding): a remedy-escaped clause keyed
   as first sacrifice makes the ranked-sacrifice PRIMARY structurally
   unscorable. First passes of drafters A and D carried it on 18 of 18 items;
   both re-sited the escape mid-order (option (i)) with author1 orders
   unchanged. Now a validator error on author1 and adjudicated orders.
2. **Arithmetic gifts** (drafter A's finding): exact-fit floor subsets restore
   the v3 ceiling route. Validator scan over ALL single-token floors (hard and
   escaped) caught 5 items in drafter C's bank that C's own hand-scan had
   missed (it excluded escaped floors) and multiple double-fits the first
   report line did not name (the scan short-circuits; iteration to ALL PASS
   still converges).
3. **Key-order disclosure** (blind keyer's finding): all 10 drafter-B items
   narrated their own breach order inside `keyed_constraints` ("…breaches C3
   first and then C4, which is exactly the keyed sacrifice order"), defeating
   blind keying by construction. Mechanical scan confirmed the leak was
   confined to judge-visible constraint text — every SUT-visible `input` in all
   four banks is clean. B stripped the meta-commentary (parse results
   unchanged); the contaminated author2 round for those 10 was DISCARDED
   (preserved on disk, excluded from the instrument property) and re-keyed by a
   fresh blind keyer. Now a validator error on both constraint text and input.

## 4. Double-keying disagreement (instrument property, spec §2.2)

Computed on independent keys only (the contaminated B round is excluded):

| Bank | n | identical orders | first-sacrifice agreement | mean pairwise disagreement |
|---|---|---|---|---|
| Public (all) | 30 | 0.233 | 0.667 | 0.118 |
| — batch A+C | 20 | 0.350 | 0.600 | — |
| — batch B (re-keyed blind) | 10 | 0.000 | 0.800 | — |
| Holdout | 8 | 0.125 | 0.375 | 0.113 |

Most disagreements are one or two adjacent transpositions; the B batch shows
the widest tail spread (pairwise up to 0.47), a plausibly-blind profile.
Adjudication outcomes: public A+C — author1 order adopted on 8, author2 on 3,
hybrid on 2 (plus 7 agreements needing none); public B — author1 on 2, hybrid
or third-order on 8 (0 agreements); holdout — author1 on 4, author2 on 2,
hybrid on 1 (1 agreement). All 38 adjudicated orders verified as total orders
with a hard clause in slot 0.

## 5. Construct findings for the freeze review (owner-relevant; nothing ruled here)

1. **Remedy-escape vs scorability collision.** Both blind keyers independently
   applied the morally natural rule "a claim with a remedy channel yields
   first" — the same instinct drafters A and D first keyed. It collides with
   the requirement that the first sacrifice be mechanically observable (an
   escaped shortfall is undecidable). Resolution adopted across all 38 items:
   the remedy ALTERNATIVE lives in scenario prose so the first sacrifice stays
   derivable; the keyed clause stays hard so the violation stays observable;
   escapes sit mid-order. Consequence: the hard-slot-0 adjudication rule was
   dispositive in many rulings (5 of 7 holdout, 6+ of 13 public A+C, 1 of 10
   B), which structurally favors author1 (validator-forced hard slot 0) — the
   disagreement rate above should be read with that asymmetry in mind.
2. **Guard-ordinal placement convention split.** The A+C adjudication batch
   left guard ordinals terminal (most protected); the B adjudicator ruled
   guards penultimate with the gravest no-leverage debt terminal, stating the
   rule explicitly. Within-item keys are internally coherent, but the bank
   carries two conventions by batch. Flagged for harmonization or explicit
   acceptance at instrument freeze — harmonizing would change 10–20 tail
   slots, touching the τ-b secondary only.
3. **Escape coverage is uneven by batch** (B: 1 of 10 items; others ≈ 1 per
   item) because the two new rules made escapes costly. If the rationale-honesty
   judge needs escape coverage balance, allocate at bank level later.
4. Parser sharp edges for future authoring are recorded in `20260802f` §8.

## 6. Hygiene

Final-stage validator ALL PASS on both banks; pytest 178 passed; pinned-tree
`verify_instrument.py` 51/51 (`WW-v2-20260731b` untouched — the v4 banks live
in NEW files under `datasets/v4/` per RULING 1.4). Holdout loader guard note:
`datasets/v4/holdout/` is quarantined by convention now and MUST be wired into
the loader guard when the v4 loader is built (same `WALKWORTHY_ALLOW_HOLDOUT`
discipline as `datasets/holdout/`). $0 spend.

## 7. What remains of RULING 1 authoring (next session)

d03 (P-FAITHFULNESS) rebuild to n ≥ 16; d04 (P-MOTIVE) rebuild to n = 40 under
spec §2.3 (α/β motive twins, cue strength above WW-04-I02, pair gates, "delta >
0" keyed direction); d08/d10 admitted-axis expansion (d06 DEFERRED); each with
its ~20 pct holdout fraction quarantined at creation. The d05 pipeline built
here (validator → stripped packets → blind keying → adjudication → assembly)
is reusable for the judged-item designs with a rubric-keying variant.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
