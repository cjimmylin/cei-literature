# WALKWORTHY Paper — Outline & Claims Skeleton

<!-- WALKWORTHY-CANARY-7f3e2026 -->
**Status:** DRAFT — living document (NOT dated-immutable; edit in place).
**Owner:** Fable (claims skeleton) per master-plan §5; section drafts per the owner column below.
**Created:** 2026-07-12, Fable paper-predraft session (Jimmy present).
**Rule of the file:** no section may assert a claim beyond what this skeleton licenses.
Release/submission decisions are **Jimmy-only** (master-plan §5).

---

## 0. Decisions log (grilled from Jimmy, 2026-07-12)

| Decision | Ruling |
|---|---|
| Venue/format | **arXiv-first preprint**, venue-agnostic; pick venue after results land |
| Length/shape | **Long-form technical report** (20–40 pp, everything in main body; venue condensation is a later separate pass) |
| Headline contribution | **The benchmark artifact itself** (D&B-style framing); governance + generalizability are supporting contributions |
| Generalizability framing | **Template for any tradition** with a canonical corpus — carefully hedged (exactly one instantiation exists) |
| Results scope | **Methods-first, results-light**: pilot + panel mechanics + gate outcomes only; full leaderboard deferred (fits FR-9 wave release; nothing in the paper depends on which designs clear) |
| Anonymization | **Anonymizable from the start**: no self-identifying prose; identifying strings live only in the swap block (§7) |
| AI-pipeline disclosure | **Minimal — ethics statement only** (Jimmy's call; Fable flagged under-disclosure risk 2026-07-12). Methods stay honest-but-neutral ("multi-stage authoring pipeline with adversarial review and human ratification; see Ethics Statement") — methods must never imply human item-authoring |

## 1. Paper identity

**Working title (candidate A, preferred):**
*WALKWORTHY: A Method-Major Benchmark Family for Measuring Behavioral Accordance with a Declared Corpus of Christian Ethics*

**Candidate B:** *Walk, Not Talk: A Gated, Pre-Registered Benchmark Family for Tradition-Specific Value Accordance in Language Models*

**One-sentence thesis:** We contribute a 10-design benchmark family that measures whether a model's *behavior* (not its stated values) accords with the consensus moral teaching of a named 15-work corpus of Christian ethics, governed end-to-end by pre-registered validity gates that determine — per design, per label wave — whether any score may be released at all.

## 2. Contribution claims (each tagged with the license that permits asserting it)

| # | Claim | License / condition | Status 2026-07-12 |
|---|---|---|---|
| **C1** | **The artifact**: 10 method-major designs; 356 authored / 344 runnable public items + 158-item private holdout (33.4% of 473 seed cases); 14-area registry; three-stratum ground-truth schema; 12-entry intra-corpus dispute (DSP) registry with per-position credit | Exists now — assertable as a *construction* claim. Any "valid measurement instrument" phrasing is CONDITIONED on gate outcomes (C5) | ✅ assertable (construction), ⏳ conditioned (validity) |
| **C2** | **The construct**: corpus-indexed behavioral-accordance construct (charter §1) — deliberately NOT "is the model ethical/Christian" (unbenchmarkable); contested-tier separation for societally-polarized doctrine (stratum b); "walk not talk" behavioral operationalization | Exists now (charter frozen 2026-07-06) — assertable as a design contribution | ✅ assertable |
| **C3** | **The governance**: G1–G10 gates pre-registered 2026-07-06 and frozen to exact computations 2026-07-10 *before any full-panel score existed*; frozen judge pair + escalation ladder + tie-breaker with home-advantage exclusion; release formula with 8-status vocabulary; wave-based release (FR-9); FIX-MECHANICS-ONLY discipline | Exists now — assertable as methodology. "The gates caught real problems" is assertable ONLY with the specific documented instances (05's G1+G2 FAIL, FR-5; proxy-scalar pilot lessons) | ✅ assertable (with instances) |
| **C4** | **The template**: the pipeline (corpus → area registry → stratum schema → method-major designs → gated release) instantiates for any normative tradition with a canonical corpus | HEDGED, always: exactly one instantiation exists; phrase as "designed to instantiate," never "shown to generalize" | ⚠️ hedge-locked |
| **C5** | **Empirical (results-light)**: feasibility numbers (2,064/2,064 panel records, 6 SUTs, $48.75, 0 schema errors); pilot findings AS DESCRIBED IN PREREG §D (descriptive, pre-gate); gate outcomes per design (status vocabulary) when the NEW dated readings file exists | Panel mechanics assertable now. Gate outcomes: ONLY from the post-W3 readings file; per-design scores ONLY for designs with status RELEASED + Jimmy sign-off | ⏳ scaffold only |
| **C6** | **Exploratory MVP preview**: the registered 60-item × 3-SUT × 2-cheap-judge lane executed end to end; descriptive model-by-design values, exclusions, custody, and limitations may be shown without rankings or release claims | Jimmy-ratified `20260713-walkworthy-mvp-paper-strategy-amendment.md` + completed `20260713-mvp-a1-descriptive-analysis.md`; every surface carries the MVP disclaimer | ✅ assertable as descriptive preview only |

**Forbidden everywhere (charter §1, verbatim ban):** "Model M is (un)ethical / (un)Christian / (mis)aligned with Christianity"; any cross-area scalar without worst-area alongside; any core-tier claim from contested-tier items or vice versa. **Approved claim templates** (use verbatim when results land): "Model M scores X on accordance with the consensus teaching of the WALKWORTHY source corpus in area Y under method Z"; "Models M1 and M2 diverge most in [area × method] cells."

## 3. Section map

| File | Section | Owner | Depends on results? |
|---|---|---|---|
| `00-title-abstract.md` | Title + abstract skeleton | Fable | Slots only |
| `01-introduction.md` | Intro + contributions | Fable | No |
| `02-related-work.md` | Related work (published lit ONLY) | Opus draft → Fable review | No |
| `03-benchmark-construction.md` | Corpus, registry, strata, designs, items, HOLDOUT, authoring pipeline | Opus draft → Fable review | No |
| `04-measurement-methodology.md` | Judges, adjudication, human labels, gates, prereg narrative | Opus draft → Fable review | No |
| `05-experimental-setup.md` | SUT panel, infra, costs | Opus draft → Fable review | No |
| `06-results-scaffold.md` | Results (placeholder tables, exact column schemas) | Fable scaffold → Codex mechanical fill | **Yes — fill from NEW dated readings file only** |
| `06a-mvp-exploratory-results.md` | Separate exploratory MVP table/figure preview | Codex mechanical fill → Opus memo → Jimmy | **Yes — MVP-A1 only; never merge into O5** |
| `07-discussion-stub.md` | Discussion angles + slots | Fable stub | Partially |
| `08-threats-to-validity.md` | Threats / limitations | Fable | No (updated after results) |
| `09-ethics-statement.md` | Ethics statement (carries the AI-pipeline disclosure) | Opus draft → Fable review | No |
| `10-reproducibility.md` | Reproducibility checklist + contamination policy | Opus draft → Fable review | No |

## 4. Fill-in protocol (post-results, mechanical)

1. Codex/Opus fills `06-results-scaffold.md` placeholders **only** from the NEW dated
   post-W3 readings file (never `20260711b-o4-panel-report.md`, superseded) and the O5
   gate-adjudication report.
2. Every filled number keeps its `<!-- source: <file> §<sec> -->` comment.
3. Release-formula statuses use the exhaustive vocabulary (framework §4): RELEASED ·
   BLOCKED-G4 · REWORK-RUBRIC · REWORK-DIFFICULTY · REDESIGN-REVIEW · CAPABILITY-WASHED ·
   ADJUDICATION-INCOMPLETE · JUDGE-DISQUALIFIED(G5).
4. No per-design score enters prose unless that design's status is RELEASED **and**
   Jimmy has signed off (release formula, last conjunct).
5. Abstract slots in `00-title-abstract.md` fill last.

## 5. Source documents (the paper narrates these; never contradict them)

- Charter: `00-PORTFOLIO/20260706-normative-charter.md` (construct, corpus, areas, strata, DSPs, reporting spine)
- Master plan: `00-PORTFOLIO/20260706-master-plan.md` (gates v0, roles — §5: paper claims = Fable; release = Jimmy)
- Prereg: `00-PORTFOLIO/20260710-fable-gate-prereg-pilot-adjudication.md` (§B statistics, §C gate rules, §D pilot adjudication, §E judge plan)
- O5 framework: `00-PORTFOLIO/20260711d-fable-o5-decision-framework.md` (FR-1..15, G4 branch table, release formula)
- Human labels: `00-PORTFOLIO/20260710-human-label-protocol.md` (Part A/B, κ forms, waves, ceiling)
- Panel report: `00-PORTFOLIO/20260711b-o4-panel-report.md` (mechanics/cost ONLY — its readings are superseded)
- Rulings: `20260712-fable-ruling-session-log.md`, `20260712-fable-codex-full-handoff.md` (FR-16/17/18, tie-breaker = mistral-large-2512)

## 6. Standing constraints (bind every section)

- **HOLDOUT:** never loaded, never quoted, never described beyond count/percentage/stratification variables.
- **Public items:** prefer paraphrase + counts over quotation (contamination). Verbatim examples come ONLY from the 12 non-runnable sketch exemplars (PR-1(c): illustrations, never run-surface) — mark them as such.
- **Canary:** `WALKWORTHY-CANARY-7f3e2026` comment in every PAPER/ file; the paper's contamination section documents the canary policy.
- **Scope:** differentiate against PUBLISHED LITERATURE ONLY. Never mention or compare to sibling benches in this vault.
- **No results asserted** anywhere outside the C5 license. Pilot numbers appear only with the prereg §D framing ("descriptive, pre-gate, proxy-scalar").
- **Contested tier is EMPTY in v1** (zero stratum-b items; O1 handoff §3). Every mention of the tier must mark it schema-complete-but-unpopulated; contested-tier readouts print "N/A (tier unpopulated)", never silently omitted, never implied populated.
- **Label waves of record** are FR-17(a): {02,07,01} → {03,04,05,06} → {08,09,10}. The human-label protocol §8's original wave-2/3 grouping is SUPERSEDED — never cite it for wave membership.
- **Anonymizable prose:** no author names, institution, repo URL, vault paths in section prose. Note: the name "WALKWORTHY" itself is searchable once the repo is public — standard benchmark-paper exposure; venue policies generally tolerate named artifacts; flagged for the venue decision.

## 7. De-anonymization swap block (only place identifying strings may appear)

```
[AUTHORS]       → (fill at arXiv submission)
[INSTITUTION]   → (fill at arXiv submission)
[REPO-URL]      → (fill at arXiv submission; public artifact release is Jimmy-only)
[CONTACT]       → ethicalintel2025@gmail.com (do not move into prose)
```
