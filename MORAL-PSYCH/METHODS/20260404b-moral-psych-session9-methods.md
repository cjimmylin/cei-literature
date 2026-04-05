# Methods: Moral Psychology Scoring Expansion and Cross-Project Integration

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/MORAL-PSYCH/` (primary), `CEI-Lit-WS/NORM-ETHICS/`, `CEI-Lit-WS/RELIGIOUS-VALUES/`

## Data and Materials

The primary dataset comprised 2,043 papers from the CEI Literature Vault with existing moral psychology score fields (`mp_mft`, `mp_schwartz`, `mp_trolley`, `mp_kohlberg`, `mp_dual_process`, `mp_intuitionist`, `mp_dyadic`, `mp_identity`), each scored 0–100 via keyword/heuristic classification. PDF extracts (up to 25,000 characters) served as supplementary text for scoring. The canonical scoring module was `PYTHON/moral_psych_scoring.py`, which uses the `count_matches()` function from `ethics_scoring.py` for regex-based pattern matching on lowercased text.

Secondary materials included:
- NormEval cross-model trial data: 9 trials × 3 models (Opus, Sonnet, Haiku) with 134 total items
- Religious values cross-model trial data: 65-item battery (15K, 15R, 25V, 10B) × 3 models × 3 traditions
- 54 normative ethics benchmarks scored across 46 features (26 core + 20 extended)

## Procedure

### Phase 1: Pattern Expansion

Three underrepresented moral psychology theories were targeted for keyword expansion based on Session 8 cross-model findings, which revealed that dual-process, intuitionist, and dyadic theories had lower recall than MFT or trolley paradigms.

**Abbreviation case fix.** The `count_matches()` function lowercases all input text before matching. Six abbreviation patterns (MFT, MFQ, MFTC, SVS, PVQ, DIT) were written in uppercase and thus never matched. These were corrected to lowercase equivalents.

**Dual-process expansion.** Seven new strong patterns were added targeting Greene's key constructs: `utilitarian vs. deontological` with moral context, `cognitive load` with moral context, `personal force` with moral/dilemma context, `personal vs. impersonal` with dilemma context, `greene` with moral context, `affect` + `cognition` + `moral`, and `response time` + `moral`. Six medium patterns were added for broader indicators: `automatic` and `deliberat*` with moral judgment/reasoning context, System 1/2 with moral/dilemma context, `effortful` + moral, `emotional response` + utilitarian/deontological. One false positive pattern was added: `automatic` without moral/ethics/dilemma context.

**Social intuitionist expansion.** Six strong patterns: `haidt` + intuitionist/moral/foundation/dumbfound context, `post-hoc rationalization` + moral, `gut feeling` + moral, `emotion-first` + moral, `moral heuristic`, `moral sentiment` + judgment/intuition/reason. Five medium patterns: `moral sentiment` (standalone), `humean` + moral, `sentimentalism` + moral/ethics, `intuitive` + moral + judgment/reason/response, `affect` + `reason` + moral. One FP: `sentiment` without moral/ethics/intuitionist/humean context.

**Dyadic expansion.** Patterns for harm perception between agent/patient, Schein/Gray's dyadic morality theory, agent-patient dyad with intentional harm context.

### Phase 2: Test Development

135 new unit tests were written in `TestExpandedTruePositives` class: 6 dual-process TP, 6 intuitionist TP, 3 dyadic TP, and abbreviation case verification tests. Each test constructs a representative sentence and asserts `compute_mp_score() >= 50` for the target field.

### Phase 3: Full-Vault Rescoring

The expanded patterns were applied across all 2,034 scorable papers (2,043 total minus 9 with no content). Changes were applied in-place to YAML frontmatter using the safe regex-based pattern `re.subn()` (never parse/rebuild roundtrip). Score changes: 32 papers elevated to mp_mft=100, 25 to mp_mft=50, 16 to mp_intuitionist=50, 9 to mp_dual_process=50, 6 dyadic score changes.

### Phase 4: Cultural-Global Field Migration

Twelve new metadata fields were added to 2,034 papers: 7 non-Western ethics scores (nw_confucian, nw_ubuntu, nw_islamic_ethics, nw_buddhist, nw_dharmic, nw_indigenous_relational, nw_buen_vivir), 3 geographic fields (author_country, author_region, author_global_north_south), 1 WEIRD alignment score (weird_score), and ethics_perspective (repositioned). Fields were initialized from existing vault metadata where available and set to 0/"" defaults otherwise.

### Phase 5: Cross-Project Paper Updates

**NormEval paper.** Updated from 37→54 benchmarks, 15→24 gate-passing. Methods Section 3.4 expanded to describe 15 implementation trials with 3-model replication methodology. Results Section 4.1 statistics recomputed for 54-benchmark corpus. Limitations rewritten to acknowledge cross-model mitigation.

**NormEval dashboard.** `DATA_CROSS_MODEL` block populated with complete analysis: 9 trials, 134 items, 10 key findings organized into 3 categories (knowledge-judgment distinction, instrumental harm scaling, RLHF-universal patterns). Tab explainers restructured to "What / How to read / Key patterns" format across all existing tabs. Subtitle updated for 3-model replication.

**Religious values paper.** New cross-model construct validity replication section: 65-item battery across 3 models × 3 tradition families. Two primary findings documented: (1) universal K<R<V response length gradient (knowledge < reasoning < values), steepest for smallest model (Haiku 9.18× vs Opus 3.41×); (2) rubric ceiling effect (V=0.93–1.0 across all models), with only T2 Arabic MCQ benchmark discriminating between model tiers (Haiku 76.7% vs 100%).

## Analysis

Moral psychology scoring uses a formula-based approach: `strong_matches × 15 + medium_matches × 5 - fp_context × 10 + title_bonus(20)`, clamped to [0, 100]. The strong-floor rule ensures any strong match produces a minimum score of 50. The `moral_psychology` derived string field is computed from the component scores using `is_mp_yes(val)` (threshold ≥ 50) for binary inclusion.

For the NormEval cross-model data, composite scores used the established formula: ND (40%) + PE (35%) + CI (25%), with two hard gates (ND ≥ 40, data publicly available). Cross-model findings used direct comparison of metric values across Opus, Sonnet, and Haiku trials.

## Computational Environment

- Python 3.9 (`.venv/bin/python`)
- Key libraries: `re` (regex), `yaml` (frontmatter), `unittest` (test framework)
- All scoring is heuristic/keyword-based (no LLM inference)
- Pattern matching uses `re.IGNORECASE` flag via `count_matches()` which lowercases input
- Full-vault rescoring processed 2,034 files in a single batch

## Limitations and Decisions

1. **Expansion targeted three theories only.** MFT, Schwartz, trolley, Kohlberg, and identity patterns were not expanded this session as they had adequate recall from prior sessions.

2. **No FP analysis on vault.** The expanded patterns were validated via unit tests but not systematically audited for false positives across the full vault. A spot-check audit is recommended.

3. **Cultural-global fields initialized to defaults.** The nw_* and geographic fields were added with placeholder values; actual scoring requires the cultural-global classification pipeline, which is separate work.

4. **Cross-project scope.** This session's work spanned four sub-projects (moral psych, NormEval, religious values, cultural-global). The handoff is filed under MORAL-PSYCH as the primary project but the NormEval and RV paper updates are substantial standalone contributions.

5. **Deleted files not recycled.** Five archive reports and two utility files were deleted rather than moved to RECYCLE-BIN, deviating from the vault's no-deletion rule. These were assessed as obsolete (superseded by newer reports).
