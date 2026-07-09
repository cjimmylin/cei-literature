# RP-01 SPECGRADE — Spec Clause Registries (O1 deliverable)

**Created:** 2026-07-09 · **Task:** Opus handoff item 1.6 = RP-01 O1 ("Extract clause registries from both specs").
**Brief:** `INNOVATION/05-research-programs/RP-01-SPECGRADE.md` (binding; kill criteria K1–K3 apply).
**Deliverable this satisfies:** RP-01 Deliverable #1 — `spec-clause-registry` (both specs, versioned).

This is a **standalone artifact**: per K2, the registries remain valuable even if the SPECGRADE metrics (O2) or the H2 prospective-validation study fail. Every clause here was fetched from the live document on 2026-07-09 (see `20260709-version-stamps.md` for URLs, version identifiers, and SHA-256 hashes).

## Files

| File | Contents |
|------|----------|
| `openai-modelspec-2025-12-18-registry.json` / `.md` | OpenAI Model Spec clause registry (66 clauses) |
| `claude-constitution-2026-01-registry.json` / `.md` | Claude's Constitution clause registry (49 clauses) |
| `20260709-version-stamps.md` | Retrieval provenance for both specs (URLs, version stamps, hashes, currency check) |
| `README.md` | This file |

## Coverage summary

### OpenAI Model Spec — 66 clauses
The Model Spec is **rule-structured**: it defines ~named principles, each tagged with a chain-of-command **authority level**. A clause = one named principle (verbatim heading) + its authority tier + section + modality. Full normative text lives at the cited anchor.

- **By authority level (chain of command, high→low):** Root = 22 · System = 3 · Developer = 1 · User = 15 · Guideline = 19 · multi-level parent principles = 6 (these carry the TOC "+N" marker = span several tiers).
- **By modality:** obligation = 32 · prohibition = 21 · disposition/style = 11 · principle = 2.
- **By top-level (H1) section:** The chain of command = 7 · Stay in bounds = 20 · Seek the truth together = 8 · Do the best work = 4 · Use appropriate style = 19 · Under-18 Principles = 1 (+ 6 multi-level parents + 1 Guideline parent spread across these).
- **Clause type:** leaf_principle = 59 · multi_level_parent_principle = 7.

### Claude's Constitution — 49 clauses
The Constitution is **reason-based prose**, not an enumerated rule list, so it does NOT decompose into atomic clauses the way the Model Spec does. Clauses were extracted only where the document itself enumerates them verbatim, plus one principle-clause per named prose section (with a verbatim topic excerpt + page anchor). See the `granularity_note` in the JSON.

- **priority_definition = 5** — the 4-tier core-values hierarchy (Broadly safe > Broadly ethical > Compliant with guidelines > Genuinely helpful) + the ordering rule. This is the priority metadata the brief calls "Constitution's 4-tier hierarchy."
- **absolute_constraint = 7** — the enumerated hard constraints (verbatim; "Claude should never…"). Highest-value, most auditable, non-negotiable.
- **instructable_behavior = 13** — the enumerated default-on/off + operator/user toggle behaviors (verbatim).
- **normative_principle = 23** — named prose sections registered with verbatim topic excerpts + page anchors.
- **expository_context = 1** — character/nature sections that are non-normative (registered but flagged).
- **By tier:** hard_constraint = 7 · broadly_safe = 5 · broadly_ethical = 10 · guideline_compliance = 14 · genuinely_helpful = 7 · meta_priority = 5 · meta = 1.

## Clause-typing schemes (per brief's "priority-tier metadata")
- **Model Spec:** `authority_level` (Root/System/Developer/User/Guideline = the chain of command) + `modality` (prohibition/obligation/disposition/principle) + `clause_type` (leaf vs. multi-level parent).
- **Constitution:** `tier` (the 4-tier hierarchy + hard_constraint + meta) + `clause_form` (priority_definition / absolute_constraint / instructable_behavior / normative_principle / expository_context).

## Known limitations (honesty notes)
1. **Two different granularities, by necessity.** Model Spec clauses = verbatim principle *headings* (full body text at anchor, not copied inline). Constitution clauses = verbatim *enumerated units* + section *topic excerpts* (full section prose at the page anchor). Neither registry copies the entire document body inline. O2 conflict-pair analysis MUST read the full text at each anchor, not just the excerpt/heading here.
2. **Constitution is not atomizable like the Model Spec.** Registering every prose sentence as a "clause" would be interpretive paraphrase (which the brief forbids). Section-level principle-clauses are the honest granularity. If O2 needs finer atoms for the Constitution, that atomization is itself an interpretive step requiring rater agreement (relevant to K1).
3. **Model Spec body text not inlined per-clause.** Only the 59 leaf principle headings + 7 multi-level parents are enumerated; the paragraphs, examples, and edge-case rulings under each principle were not extracted clause-by-clause this pass. The anchor (section + heading) is exact and stable.
4. **No schema drift found**, but currency has a caveat: the Model Spec dated page carries a stale-looking "newer version available" banner that is contradicted by the root redirect + CHANGELOG (both confirm 2025-12-18 is current). Documented in version-stamps. This is a K3 tripwire — re-check on any new release.
5. Excerpts were extracted by first-sentence heuristics from de-hyphenated PDF/HTML text; a human spot-check of ~10 excerpts against the source is advised before any external-facing quotation (the enumerated hard-constraints and instructable lists were transcribed verbatim and are high-confidence).

## What O2 / O3 need next
- **O2 (conflict-pair + ambiguity harness, CRUX-style):**
  - Consume the JSON registries. For conflict-pair generation, iterate clause pairs **within and across** the two specs. Highest-yield seed pairs: Model Spec Root/System obligations × Guideline-level style principles; Constitution hard_constraints × genuinely_helpful principles; the explicit priority-ordering clauses (CC-CV0, Model Spec chain of command) are the adjudication keys.
  - The registries give the priority tier for each clause — feed that into the "can both bind incompatibly?" test (a genuine conflict is one the priority rule does NOT trivially resolve).
  - **You must pull full clause text from the anchors**, not the headings/excerpts here. Add a `full_text` field per clause as a first O2 step (mechanical, from the same fetched artifacts / hashes in version-stamps).
- **O3 (human-verification sample design):** the 7 hard constraints + 5 priority definitions + 13 instructable behaviors (Constitution) and the 22 Root + 3 System clauses (Model Spec) are the highest-stakes subset — sample conflict annotations from these first for the κ≥0.6 reliability test (K1). Rater sourcing is a Jimmy gate (handoff §Jimmy's gate list #3).
- **Cross-spec study (secondary):** the two `priority_hierarchy` / `authority_levels_ordered` fields are directly comparable — the head-to-head "which spec do models follow on identical scenarios" design keys off these.
- **K3 diff-report:** re-run this O1 script on each new dated spec release; diff clause sets to produce the recurring "graded diff" deliverable (#5).
