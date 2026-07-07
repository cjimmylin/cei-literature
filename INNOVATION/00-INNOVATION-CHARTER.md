# INNOVATION — Charter

**Created:** 2026-07-07 · **Author:** Fable 5 (final Fable-window session; window closes ~2026-07-11)
**Status:** Fable design layer COMPLETE; execution is post-window Opus work per `07-opus-handoff.md`

## Why this folder exists

The CEI vault measures values in AI systems exceptionally well — 2,400+ curated papers, a benchmark-design cookbook, ten-plus benchmark families. But outer alignment is a six-stage pipeline (specify → train → oversee → aggregate → evaluate → deploy), and the vault's depth is concentrated in one stage (evaluate) while the field's 2025–26 movement happened everywhere else. This folder is the corrective: a Fable-authored map of where the field went, what the vault is missing, and ten concrete research programs that convert CEI's existing assets into contributions across the whole pipeline.

**The thesis in one line:** CEI's comparative advantage is measurement science and normative-tradition depth; the field's new frontiers (spec adherence, no-gold oversight, value drift, emergent misalignment, tradition-aware aggregation) all lack serious instruments — so CEI should instrument them.

## Document map

| Doc | What it is | Read when |
|-----|-----------|-----------|
| `00-INNOVATION-CHARTER.md` | this file | first, any session |
| `01-field-map-2026.md` | narrative: pipeline model, field history 2022–26, state of each front, CEI's position, five falsifiable bets (B1–B5) | planning any new work |
| `02-gap-atlas.md` | the master gap register: G-01…G-23 with corpus evidence and severity × tractability × CEI-fit ratings; cross-refs to pre-existing gap registers | deciding what to work on |
| `03-newest-ideas-scan.md` | 23 frontier concepts, tiered by how much they should change CEI's behavior | orienting on any 2025–26 topic |
| `04-missing-literature.md` | ~112-item acquisition list (98 verified-absent), mapped to gap IDs, `/download-pdf`-ready | vault housekeeping cycles |
| `05-research-programs/` | `00-portfolio-overview.md` (selection logic, waves, prerequisites) + ten briefs RP-01…RP-10, each with hypotheses, methods, Opus tasks, kill criteria | starting any program |
| `06-deliverables-roadmap.md` | cross-portfolio outputs: publications ladder P1–P8, datasets, standards, tools, vault-internal items V1–V4 | deciding what to ship next |
| `07-opus-handoff.md` | the post-window execution queue with tier assignments and acceptance criteria | first post-Fable session |

## Provenance & epistemic status

- Corpus evidence: two Sonnet survey agents over `papers/` + `COOKBOOK/` (2026-07-07).
- Field evidence: eight parallel Opus web sweeps (mid-2025→2026-07-07) across specification, oversight, social choice, reward models, deliberative alignment, emergent misalignment, agentic/multi-agent, and lab publications. Sweep agents verified top-anchor citations by fetch; secondary items are search-confirmed only. `04-missing-literature.md` flags ~25 unverifiable-this-session arXiv IDs with ⚠ — **confirm at download, and do not cite ⚠ items in external prose until confirmed.**
- Judgment calls (gap ratings, program selection, hypotheses, kill criteria): Fable, main loop, this session. They are considered opinions, not settled facts — the falsifiable bets in `01` §6 exist so future sessions can check whether the map was right.

## Operating rules for this folder

1. **Report immutability applies** (root CLAUDE.md Rule 3): these documents are dated snapshots. Updates = new dated files (e.g., `20270115-gap-atlas-revision.md`), never in-place rewrites. Exception: `07-opus-handoff.md` is a living queue and may be checkbox-updated in place.
2. **Kill criteria are binding.** Each RP brief pre-registers its kill/downgrade conditions. Opus sessions execute them mechanically; softening a kill criterion requires a Fable-tier (or Jimmy) ruling — same succession discipline as the FRUITBENCH governance protocols.
3. **Scope isolation:** this folder addresses the values-alignment *field*; it uses BibleBench families as instruments (per portfolio overview §"Relationship") but does not modify them. Changes to COOKBOOK/BibleBench stay in their own governance lanes.
4. **The judge-corruption caveat (G-09) travels with everything:** any INNOVATION output using LLM judges cites and addresses it in methods.

## What Jimmy owes (the standing gates)

API keys (Anthropic + OpenAI minimum; Gemini valuable as third judge family) → unblocks Wave 1. GPU-inference budget sign-off → unblocks RP-04/RP-09 open-weight lanes. Human panels → unblocks RP-08 Phase B (and improves several others). Licensing decision on evidence-card corpus release (roadmap D6).
