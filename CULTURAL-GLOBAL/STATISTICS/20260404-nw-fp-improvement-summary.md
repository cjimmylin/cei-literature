# Non-Western Framework FP Improvement Summary

**Date:** 2026-04-04
**Agent:** B (P3 scorer FP improvement)

## Changes Made

### 1. FP Patterns Added to `nonwestern_scoring.py`

**Confucian (5 new patterns):**
- Named Chinese NLP benchmarks: ACLUE, C3Bench, AncientBench, WYWEB, Fuxi, etc.
- `chinese benchmark/corpus/dataset/evaluation/nlp` without Confucian philosophy terms
- `classical chinese understanding/language/comprehension/text/nlp`
- `chinese moral norm/scenario/dilemma` without Confucian concepts
- `chinese culture/cultural benchmark/evaluation/test`

**Buddhist (5 new patterns):**
- `buddhist corpus/parallel/translation/text mining`
- `humanistic buddhism corpus`
- Pali/Buddhist/Tibetan corpus+NLP co-occurrence
- Buddhism in bias/stereotype/sentiment analysis studies
- `thai benchmark/dataset/nlp/corpus/evaluation`

**Ubuntu (3 new patterns):**
- Ubuntu + cloud/container/docker/agentbench computing context
- Ubuntu + command line/shell/bash/setup computing context
- Ubuntu + benchmark/dataset without philosophical engagement terms

**Dharmic (5 new patterns):**
- Hindu/Vedic/Sanskrit corpus/NLP/sentiment/dataset
- Bhagavad Gita/Upanishad/Vedas + NLP/corpus/topic model
- Jain as author surname (`jain et al`, `jain (2024)`)

**Indigenous (3 new patterns):**
- `indigenous language(s) NLP/corpus/benchmark/translation`
- Indigenous languages + NLP context without ethics/sovereignty terms
- `low-resource language/indigenous` + NLP context

**Buen Vivir:** Comment noting inherent precision limitation (only 6 detections total).

### 2. Scoring Logic Changes

**Strong-match floor graduated thresholds:**
- OLD: Any strong match → floor at 50
- NEW: 
  - FP-dominated (fp_count >= 2*strong_count AND fp_count >= 3) → NO floor
  - Single strong match, no medium/title corroboration → floor at 30
  - 2+ strong matches OR medium/title corroboration → floor at 50

This change targets the dominant FP pattern: papers that mention a tradition name once in passing.

## Results: Old vs New Detection Counts

| Framework | OLD (>=50) | NEW (>=50) | Change | Old Precision | New Precision (sampled) |
|-----------|-----------|-----------|--------|--------------|------------------------|
| nw_confucian | 80 | 38 | -42 | 0.160 | 0.364 |
| nw_ubuntu | 26 | 23 | -3 | 0.500 | 0.579 |
| nw_islamic_ethics | 30 | 23 | -7 | 0.706 | 1.000 |
| nw_buddhist | 26 | 22 | -4 | 0.188 | 0.333 |
| nw_dharmic | 19 | 18 | -1 | 0.200 | 0.250 |
| nw_indigenous_relational | 53 | 49 | -4 | 0.583 | 0.675 |
| nw_buen_vivir | 9 | 8 | -1 | 0.167 | 0.167 |
| **Total any framework** | **223** | **161** | **-62** | **0.358 mean** | **0.481 mean** |

## True Positive Verification

- **0 true positives dropped** across all 7 frameworks
- 2 Indigenous papers were below 50 both before and after (Halmai=45, Blayone=35)
- All 8 Confucian TPs, 3 Buddhist TPs, 11 Ubuntu TPs, 2 Dharmic TPs, 12 Islamic TPs, 1 Buen Vivir TPs retained

## YAML Validation

All 2,329 papers valid after YAML write.

## Dashboard

`data.js` regenerated (174.4 KB, 16 constants).

## Mean Precision Improvement

- Old mean precision: 0.358
- New mean precision: 0.481 (+34% relative improvement)
- Weighted by detection count: larger improvement driven by Confucian (biggest FP source)
