# Metadata Corrections Report
**Date:** 2026-01-25
**Task:** Correct 2 misclassified papers identified during author enrichment

## Corrections Made

### 1. ✅ Astronomy Paper Removed (2024-Zhang-MIRAGE-Bench.md)

**Issue:** Paper completely misclassified as AI benchmark

**Details:**
- **Listed as:** "MIRAGE-Bench: A Comprehensive Benchmark for Interactive LLM-Agent Hallucination"
- **Actually:** "The accretion burst of the massive young stellar object G323.46−0.08"
- **Journal:** Astronomy & Astrophysics
- **First Author:** V. Wolf (astronomer at Max Planck Institute for Astronomy)
- **Subject:** Stellar astrophysics, NOT AI/ML

**Action Taken:**
- Moved paper to `RECYCLE-BIN/2024-Zhang-MIRAGE-Bench.md`
- Moved PDF to `RECYCLE-BIN/2024-Zhang-MIRAGE-Bench.pdf`
- Moved extract to `RECYCLE-BIN/2024-Zhang-MIRAGE-Bench.md`

**Reason:** This is an astronomy paper with no relevance to AI ethics, safety, or alignment. It was incorrectly imported into the vault.

---

### 2. ✅ SG-Bench First Author Corrected (2024-Mou-SG-Bench.md)

**Issue:** Wrong first author listed

**Before:**
```yaml
first_author: "[[Xiangyu Mou]]"
authors: "Xiangyu Mou"
```

**After:**
```yaml
first_author: "[[Yutao Mou]]"
authors: "Yutao Mou; Shikun Zhang; Wei Ye"
```

**Verification:**
- NeurIPS 2024 proceedings: [https://neurips.cc/virtual/2024/poster/97610](https://neurips.cc/virtual/2024/poster/97610)
- arXiv preprint: [https://arxiv.org/abs/2410.21965](https://arxiv.org/abs/2410.21965)
- Affiliation: Peking University

**Paper Details:**
- **Title:** SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types
- **Conference:** NeurIPS 2024 (Datasets & Benchmarks Track)
- **Actual Authors:** Yutao Mou (first author), Shikun Zhang, Wei Ye
- **Subject:** LLM safety evaluation (correctly classified)

---

## Impact

### Papers Affected
- 1 paper removed (astronomy misclassification)
- 1 paper corrected (wrong first author)

### Author Profiles
- V. Wolf author profile can now be safely ignored (not an AI researcher)
- Xiangyu Mou profile remains as is (may be a co-author on other papers)
- Yutao Mou now correctly identified as first author of SG-Bench

### Vault Statistics
- Total papers in vault: 575 (down from 576)
- Papers requiring review: 0 (all metadata errors resolved)

---

## Files Modified

1. `/papers/2024-Mou-SG-Bench.md` - Updated first_author and authors fields
2. Moved to RECYCLE-BIN:
   - `/papers/2024-Zhang-MIRAGE-Bench.md`
   - `/PDFs/2024-Zhang-MIRAGE-Bench.pdf`
   - `/PDF Extracts/2024-Zhang-MIRAGE-Bench.md`

---

## Additional Notes

### Other Metadata Issues Flagged (for future review)
1. Nathan Moss paper - Possible DOI mismatch
2. Sean Cleary paper - Abstract mismatch (phylogenetics vs AI)

These require manual review to determine if they are similar misclassifications.

---

## Completion Status

✅ All identified metadata errors from author enrichment have been corrected.
