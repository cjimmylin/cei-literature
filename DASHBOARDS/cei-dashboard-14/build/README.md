# Dashboard v14: build inputs and provenance

The v14 dashboard (published 2026-10-18 at `cjimmylin/cei-dashboard-14`) was first built from a
scratch overlay that never reached the vault. Everything it needs is now in the repo, and
`python3 PYTHON/build_vault_dashboard_14.py` rebuilds it from the vault alone.

## Files

| File | What it is |
|------|------------|
| `benchmark_survey_candidates.json` | The benchmark-survey "Yes" entries the generator reads: 1,072 since the 2026-10-19 merges (`logs/20261018-duplicate-merge.md` removed 8 entries for retired notes, `logs/20261019c-ethics66-scores-and-fixes.md` 1 more; originally 1,081) (`ib` flag, benchmark name, what it measures, models, availability). 985 (originally 986) are the v13 candidates, rebuilt from v13's published `data.js` plus the tracked `logs/benchmark_survey_*batches/results_agent_*.json` (797 matched a batch entry; 189 rebuilt from v13's output alone, with empty `reasoning`/`how_measures`). 87 (originally 95) come from the new-paper review below (`"source": "v14 new-paper review"`). The original consolidated survey log was never committed. |
| `normative_v2_all_classifications.json` | Normative v2 review, 266 entries, output of `PYTHON/consolidate_normative_v2.py` on the tracked `logs/normative_v2_batches/` (unchanged since February; new papers were not reviewed for it). |
| `overlay_v14.json` | The values v14 assigned to the 402 papers added after v13, now written into the notes by `PYTHON/apply_v14_classifications.py` (fill-only-empty). |
| `likely_duplicates.txt` | Note pairs the review flagged as probably the same paper (not merged). |
| `new-paper-review/` | Verbatim results of the per-paper review of those 402 papers (8 batches of about 50), plus the reviewers' instructions. |

## How the 402 new papers were classified (2026-10-18)

Papers added after v13: 325 cultural/religious/Global South papers (2026-04-04) and 77 alignment
papers (July, INNOVATION). Their notes lacked most classification fields.

- **Vault scorers** (deterministic): `ethics_scoring.score_paper` for the five framework scores
  (16 papers missing them), `moral_psych_scoring.score_paper_mp` for `mp_*` + `moral_psychology`
  (235), `religious_scoring.score_paper_rv` for `rv_*` (235) + `religious_values_list` (60).
- **Parsed**: first/last author from `authors`, `url` from arXiv id / DOI, `CONF-CC` from
  `add_conference_field_cc.classify_phase1` (local rules only; OpenAlex/Semantic Scholar unreachable).
- **Per-paper review** (`new-paper-review/`): cultures and languages under the vault's 2026-03-12
  cultural rules (`logs/20260312-cultural_language_agent_instructions.md`, names checked against
  `consolidate_cultural_language.ALLOWED_CULTURES`), a benchmark-survey decision with its fields,
  a stated venue (used when it beats an arXiv-only "Preprint"), and models evaluated
  (`LLM_assessed`, 61 papers).
- One hand correction: AraQA's venue, cut at 80 characters by the merge step, is recorded as
  `JAC-ECC 2023`.

## Caveats

- About 80% of the new papers had no PDF extract, so many labels rest on a title and abstract.
- The cultural vocabulary has no Pacific, Māori or PNG category: those papers came out as N/A,
  Multicultural/Cross-cultural or Australian/Aboriginal, inconsistently. Islamic-studies papers map
  to Arabic, Taiwan to Chinese, Bengali to Indian.
- Benchmark categories of the 986 v13 candidates are pinned to v13's published categories by the
  build script, because the 189 rebuilt entries lack the text the keyword categoriser needs.
  The 95 new ones are categorised by the generator's own `classify_entry`.
- "Models evaluated" counts for v13-era candidates run about 10% below v13's (892 vs 991 mentions):
  the model text of the 189 rebuilt entries survived only partly.
- The review flagged 13 likely duplicate note pairs (`likely_duplicates.txt`); they were left as they are.

## Check

Rebuilding from the vault after the write-back reproduces the published v14 per-paper data
except where the vault is now more correct: 6 venue years and 4 author lists fixed by the
2026-10-18 frontmatter repair (e.g. `EMNLP 2025` → `EMNLP 2014`), 1 title and 33 abstracts no
longer truncated, and the AraQA venue above.
