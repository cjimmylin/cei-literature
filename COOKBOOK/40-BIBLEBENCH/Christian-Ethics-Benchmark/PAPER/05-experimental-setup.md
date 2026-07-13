<!-- WALKWORTHY-CANARY-7f3e2026 -->
# 5. Experimental Setup

**Status:** DRAFT — living document. **Owner:** Opus draft, pending Fable adversarial review.

This section documents the measurement infrastructure: the run harness, the model-access
gateway, the panel of systems-under-test (SUTs), the pilot and full-panel runs with their
costs, and the public capability battery used by the capability-wash gate. We report
mechanics, composition, and cost only. No score, gate reading, or model ranking appears in
this section; those belong to the results and methodology sections, and are governed by the
release formula. A standing point of this section is that gated, tradition-specific
benchmarking at panel scale is inexpensive — a feasibility fact we regard as a contribution
in its own right.

## 5.1 Harness architecture

The harness is a manifest-driven Python package with a mock-first test discipline. A run is
fully specified by a manifest that lists *item identifiers* — never item text — together with
the SUT slugs, the judge and classifier slugs, the fixed permutation seeds (carried as
manifest constants, so every counterbalancing and ordering decision is reproducible from the
manifest alone), and the capability-battery snapshot. Item text lives only in the private
bank and is resolved at run time by identifier, which keeps run configuration free of the
material we must protect from contamination.

Each of the ten designs has its own executor matched to its administration mode: single-turn
executors; scripted multi-turn executors that walk a branch table (the classifier selects the
next scripted branch from the SUT's turn state); and paired-session executors that administer
two sessions under isolation guarantees — the two members of a pair land in *different*
requests and are order-permuted, so a model cannot condition one session's answer on the
other. Designs that use an arbiter administer additional probe turns. Every executor emits a
strict output block that is validated by a dedicated parser; on a malformed block the parser
issues exactly one retry, and a persistent non-compliance is *logged as data* rather than
silently coerced or dropped, so refusals and format failures remain analyzable outcomes.

Execution is checkpointed and resumable at `(item, model)` granularity: each cell writes its
scored record independently, a completed cell is never re-called on resume, and a cell that
errors is caught, written to a per-run error log, and retried on the next resume pass — so
transient provider failures self-heal without corrupting completed work. This per-cell error
handling is what let long panel runs recover from mid-run interruptions without re-billing
finished cells (§5.4). The test suite comprises **276 tests**
<!-- source: 00-PORTFOLIO/20260712-fable-codex-full-handoff.md §status -->
and is mock-first: no test issues a live API call. Transcripts are recorded fixtures, so the
suite exercises the full parse–classify–score pipeline deterministically and offline.

## 5.2 Model access

All measurement runs use a single commercial API-aggregation gateway, **OpenRouter**, as the
sanctioned path. One key routes every vendor family in the panel through a uniform interface,
which removes the need to hold separate first-party credentials per vendor and lets a
cross-vendor panel run as one job. Every model — SUT, judge, and classifier — is pinned by an
explicit provider slug (§5.3), so a run configuration names exact model builds rather than
mutable aliases.

The backend adds two robustness layers over the raw gateway. First, provider-preference
routing plus an empty-response retry: an empty `200` is treated like a transient failure and
retried with capped exponential backoff up to **N=3** attempts, because a nominally
successful but empty completion is a common provider-side truncation mode rather than a real
refusal. Second, a per-request maximum-token cap. We learned that the gateway can return an
HTTP 402 "requires more credits" error that is not true balance depletion but a per-request
token *reservation* against the account balance; capping the requested maximum tokens
(default 32,768) <!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §status -->
removes these spurious reservation failures.

We also run per-SUT reliability probes before committing a model to the panel, and two
probe outcomes materially shaped the roster. One candidate SUT returned empty content on
**45 of 50** probe calls and was dropped before the panel in favor of a probe-clean
replacement <!-- source: 00-PORTFOLIO/20260709-p0-pilot-report.md §3 -->; the empty-content
retry (above) was added in direct response. Separately, the intended third-family
tie-breaker candidate, `grok-4`, probed **0 of 10** with HTTP 404 and was dropped in favor of
`mistralai/mistral-large-2512` as the tie-breaking family
<!-- source: 00-PORTFOLIO/20260712-fable-codex-full-handoff.md §2 -->. These are model-by-provider availability findings, not
harness defects, and we record them because they are exactly the kind of operational friction
a reproduction should expect.

## 5.3 System-under-test panel

The full panel comprises six SUTs, pinned by slug
<!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §Panel composition -->:

| # | SUT slug | family |
|---|---|---|
| 1 | `anthropic/claude-sonnet-4` | anthropic |
| 2 | `deepseek/deepseek-chat` | deepseek |
| 3 | `google/gemini-2.5-pro` | google |
| 4 | `meta-llama/llama-3.3-70b-instruct` | meta |
| 5 | `mistralai/mistral-large-2512` | mistral |
| 6 | `openai/gpt-4.1` | openai |

The roster is chosen for frontier coverage across vendor families and capability tiers, from
two frontier models through a strong open mid-tier down to smaller open models. We
deliberately *retain* SUTs whose family also supplies the item generator and SUTs whose family
supplies a judge, rather than excluding them: excluding them would silently shrink the panel
and forfeit frontier coverage, so instead the home-advantage and self-preference risks these
overlaps create are handled explicitly by the disclosure machinery described in the
methodology section (dual full-panel / panel-minus-generator-family reporting, judge-family
exclusion in the tie-breaker). Nothing in this setup section reads those disclosures; it only
records that the overlaps are intentional and are addressed there.

The two judges form a frozen, cross-family pair — **`openai/gpt-4.1-mini`** and
**`google/gemini-2.5-flash`** — both distinct from the item-generator family
<!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §Panel composition -->. The turn-state
classifier is **`openai/gpt-5.6-terra`**, kept distinct from the judge pair and from the
escalation/tie-breaker candidates so that classification, scoring, and adjudication never
collapse onto a single model
<!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §Panel composition -->.

## 5.4 Runs and cost

**Pilot (P0).** The pilot ran 3 cross-vendor SUTs × 5 items/design × 10 designs = **150
records** at **\$0.63** total, with 0 schema errors
<!-- source: 00-PORTFOLIO/20260709-p0-pilot-report.md §1 -->. Its purpose was to shake out
mechanics and scale on the real gateway with genuinely different models under one judge pair;
it deliberately used cross-vendor SUTs that avoid both the judge families and the
item-generator family so the mechanics signal was unconfounded
<!-- source: 00-PORTFOLIO/20260709-p0-pilot-report.md §SUT panel -->. A preceding
single-vendor integration pilot on the same gateway ran 4 records over 30 calls at \$0.0619
and established the cross-vendor, native multi-turn transport before the P0 scale-up
<!-- source: 00-PORTFOLIO/20260709-openrouter-pilot-report.md §Result -->.

**Full panel.** The full panel ran all six SUTs across **344 items**, producing
**2,064 / 2,064 records** with **0 coverage gaps** over **18,598 calls** at a total of
**\$48.7450**, with **0 schema errors** (and 0 judge defects, 0 classifier defects) in the
completed run <!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §Panel composition -->.
The full-coverage panel was completed after an intermediate 94%-coverage render whose
remaining cells were blocked by the reservation-style 402 (§5.2); a credit top-up plus the
token cap unblocked them, and no item was edited from model performance at any point
<!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §status -->.

Total live spend across the pilot and full panel is therefore ≈ **\$49.50**
(≈ \$0.63 + \$48.75; the integration pilot's \$0.06 is within rounding)
<!-- source: 00-PORTFOLIO/20260709-p0-pilot-report.md §1 --><!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §Panel composition -->.
The operative point is a feasibility one: administering a pre-registered, gated,
tradition-specific benchmark family across six frontier and open models — with a two-judge
cross-family panel and a separate classifier — costs *tens of dollars*, not hundreds or
thousands. We regard this affordability, at this scale and coverage, as a finding the paper
may assert.

**Exploratory MVP-A1.** In a separately registered lane, we fixed 60 PUBLIC items, three
inexpensive SUTs, and two inexpensive cross-family judges. The completed snapshot contains
180/180 item×SUT executions and 480/480 logical units from each judge. All 1,715 attempts
have paired custody finishes; conservative exposure was \$0.551363883 under a \$5.00 NTE.
One malformed GPT-4.1 Nano unit required its single authorized exact replay. Three nominal
HTTP-200 responses lacked provider cost metadata; each was discarded, booked at the
registered maximum without returned-model/token claims, and recovered by one exact-payload
retry. **Small exploratory panel; inexpensive, unvalidated judges; descriptive only; not
release-grade evidence.**
<!-- source: 00-PORTFOLIO/20260713-mvp-a1-descriptive-analysis.md §1 -->

## 5.5 Capability battery

The capability-wash gate compares behavioral-accordance rankings against a general-capability
ranking, so it needs an external capability signal that is independent of the benchmark. We
use six pinned public benchmarks — **MMLU-Pro**, **GPQA-Diamond**, **SWE-bench Verified**,
**GAIA**, **RULER**, and **MRCR** — and form a composite by min-max normalizing each
benchmark across the panel and averaging each model's available normalized cells
<!-- source: 00-PORTFOLIO/20260711-capability-battery-scores-SOURCES.md §top -->. Only the
relative capability ordering is load-bearing; the composite is a within-panel rank signal, not
an absolute capability estimate.

Every cell is read from public provider or leaderboard sources at panel time (snapshot
**2026-07-11**) and recorded with per-cell provenance in an auditable sourcing file; no cell is
fabricated, and unavailable cells are held `null` with a documented reason
<!-- source: 00-PORTFOLIO/20260711-capability-battery-scores-SOURCES.md §top -->. That file also
records the material caveats a reader needs to weigh the composite: one model's cells are drawn
from the closest published build where its exact panel build had no separate numbers (a
substitution flagged as conservative for ordering); GAIA figures come from different agent
scaffolds and are treated as low-confidence; SWE-bench figures come from provider and
third-party harnesses that differ; and RULER has a comparable composite for only one panel
model, so it is effectively non-load-bearing for cross-model ranking
<!-- source: 00-PORTFOLIO/20260711-capability-battery-scores-SOURCES.md §Cross-cutting caveats -->.
Coverage is uneven across the panel (from 2/6 to 5/6 benchmarks per model)
<!-- source: 00-PORTFOLIO/20260711-capability-battery-scores-SOURCES.md §Score matrix -->, and
because the panel is small the gate reads a permutation p-value alongside the rank correlation
and treats the ordering, not any exact coefficient, as the output — a limitation we
pre-registered rather than discovered
<!-- source: 00-PORTFOLIO/20260711b-o4-panel-report.md §G3 power limitation -->.
