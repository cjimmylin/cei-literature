# WALKWORTHY Session Handoff — 2026-07-06 (Fable design day)

<!-- WALKWORTHY-CANARY-7f3e2026 -->

## What this session produced (all committed in this folder)

**WALKWORTHY**: a brand-new family of 10 method-major benchmarks measuring whether LLMs *enact* the ethics of a declared 15-work Christian-ethics corpus. Everything below was produced 2026-07-06 in one Fable session (Fable = design/adjudication in main loop; Opus agents = mining/drafting/review/revision; Sonnet = deck).

| Deliverable | Location | State |
|---|---|---|
| Normative charter (whose ethics, 14-area registry, 3-stratum schema, DSP-1..12 dispute registry, tier rules, tagging schema) | `00-PORTFOLIO/20260706-normative-charter.md` | BINDING |
| Portfolio PRD (anti-saturation contract, scoring spine, targets) | `00-PORTFOLIO/20260706-portfolio-prd.md` | Done |
| 10 design specs w/ 41 Fable exemplar items | `DESIGNS/NN-<codename>.md` | Done, amended per FA-1..6 |
| 10 seed banks — **231 items** (272 test cases total w/ exemplars) | `DESIGNS/NN-<codename>-seeds.md` | Drafted → adversarially reviewed → revised (cycle 1 complete) |
| 14 area anchor packs (citation-verified against the books) | `ANCHOR-PACKS/area-*.md` | Done |
| 10 adversarial reviews + Fable adjudication memo | `REVIEWS/20260706-*.md` | Discharged |
| Opus item-writing playbook (recipe, lint, audits, quick cards, gates) | `00-PORTFOLIO/20260706-opus-item-playbook.md` | BINDING for new items |
| Master build plan w/ PRE-REGISTERED gates | `00-PORTFOLIO/20260706-master-plan.md` | Gates frozen |
| HTML deck (18 slides, self-contained) | `00-PORTFOLIO/20260706-walkworthy-deck.html` | Done (pre-review numbers; refresh at O6) |

## The 10 designs (method × headline metric)

01 GOODSAMARITAN costly obedience → collapse threshold + Samaritan gap · 02 TWOMASTERS temptation drift → erosion AUC + break-turn + cold-open delta · 03 QUIETTONGUE say-do pairs → divergence + shading rate · 04 INNERWEIGHT implicit motive pairs → sensitivity delta + inquiry rate · 05 ORDOAMORIS forced allocation → constraint satisfaction + ordering consistency · 06 CROOKEDPATH process-scored conflicts → 7-criterion rubric, conclusion-agnostic · 07 SEVENTYSEVEN pastoral dialogues → two-pole arc (capitulation × coldness Pareto) · 08 VOCATIONFORK covert embedded ethics → guardrail survival + covert-overt gap · 09 DOUBLEEDGE seat symmetry → symmetry index + power-tilt fingerprint · 10 STRANGERGATE deservingness pairs → mercy delta by cue type.

## Review cycle 1 (complete)

~215 items reviewed by 10 independent Opus reviewers → ~145 PASS / ~68 REVISE / 1 KILL (07-I03, area-I safety rule; replaced). Fable adjudication (`REVIEWS/20260706-fable-adjudication.md`) ratified all verdicts, issued 6 spec amendments (FA-1 remainder-criterion DSP-2 neutrality; FA-3 substantive floors vs token-gaming; FA-4 prudence-asymmetry diagnostic; FA-5 relational-move keypoints; FA-6 coverage matrix; FA-2 word-count) and 4 cross-cutting mandates (anchor-label normalization; facts_diff re-derivation; exemplar debt; no key-weakening). All 10 revision agents applied and self-verified. PENDING-RULINGS: none open.

## Session history note

The session hit its usage limit mid-flight (~22:25); all 10 drafters had written their banks (3 died before final self-QC — exactly those 3 banks showed the most mechanical review findings, validating the two-agent rule), and the first reviewer wave was lost and relaunched after reset. Checkpoint commit `dcabb4fe2` preserved pre-review state; final state committed after revisions.

## What remains (build order = master plan §1)

1. **Session O1 (Opus):** second-pass spot-review of revised banks (playbook §6 R2 on changed items only — cycle-1 reviewers saw pre-revision text); create gitignored `HOLDOUT/` and move every 3rd item per bank (stratified); verify with `git check-ignore`.
2. **Session O2 (Opus):** harness build per master plan §2 (mock-first; NO live calls). Vault has no shared runner — build fresh (Anthropic SDK + per-vendor adapters).
3. **Session O3–O6:** pilot → 6-model panel → pre-registered gate adjudication (§3, frozen) → findings + deck v2.
4. **Contested tier:** deliberately EMPTY in v1 banks (stratum-b = 0 by design). Bulk authoring per charter §5 + playbook, only after core tier is validated.
5. **Jimmy owes:** API keys (multi-vendor); 60-item/design human labels for judge validation (gate §3.4); any charter amendments; public release decisions.
6. **If a Fable window recurs:** best uses = adjudicating the first REAL panel results against the pre-registered gates; neutrality-gate failures; the paper's claims section.

## Known limits (disclose in any release)

Corpus is Protestant-dominant (charter §2 lists absences). Items are English-only, US-leaning surfaces (localization out of scope v1, no machine translation per playbook §8). Judge validity unproven until §3.4 human labels exist. All claims must use the charter's Law-7 language ("accords with the consensus of these named texts" — never "is ethical").
