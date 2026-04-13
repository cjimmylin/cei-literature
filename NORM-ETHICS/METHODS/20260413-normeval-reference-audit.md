# NormEval Reference List Audit

**Date:** 2026-04-13
**Scope:** All PAPER-v2/ markdown files (main body + introduction + supplements)
**References file:** `references-normeval-v2.md` — 179 entries, 441 lines

---

## Summary

| Metric | Count |
|--------|-------|
| Unique citation keys used in paper | 123 |
| Reference entries in references file | 175 |
| **Missing refs (cited but no entry)** | **10** |
| **Orphaned refs (entry but never cited)** | **62** |

---

## Missing References (10) — NEED ENTRIES ADDED

These citation keys appear in the text but have no corresponding entry in `references-normeval-v2.md`. They will cause broken references in any formatted output.

| Key | Likely Paper | Found In |
|-----|-------------|----------|
| `[Du2025]` | Du et al. — 196 research ethics dilemmas | methods §3.1 |
| `[IslamicLegalBench2026]` | Islamic legal bench, 718 items, 7 jurisprudence schools | methods §3.1 |
| `[IslamicMMLU2026]` | Islamic MMLU, 10,013 MCQ items | methods §3.1, results-landscape |
| `[Kittay1999]` | Kittay — care ethics / dependency work | supplement (care ethics) |
| `[Nunnally1994]` | Nunnally — Psychometric Theory (classic reference) | limitations §6.1 |
| `[Snarey1985]` | Snarey — cross-cultural Kohlberg | supplement |
| `[Wei2025b]` | Wei et al. — AMAeval (distinct from Wei2025 MedEthicsQA) | results-landscape, methods |
| `[Xu2026]` | Xu et al. — probing ethical framework representations | methods §3.1 |
| `[Zhang2026]` | Zhang et al. — RLVR moral reasoning | methods §3.1 |
| `[Zheng2024]` | Zheng et al. — likely Chatbot Arena or ethics eval | supplement |

**Action required:** Add entries for all 10. Most can be found via Semantic Scholar title search. This is independent of model runs and can be done now.

---

## Orphaned References (62) — IN FILE BUT NEVER CITED

These entries exist in `references-normeval-v2.md` but are not cited anywhere in the paper (main body, introduction, or supplements). They may be:
- Remnants from the v1 paper that were pruned from text but not from the reference list
- "Background reading" entries that were never formally cited
- Cross-vendor references that will become relevant when Paper B content is re-integrated

**Full list (62 entries):**

```
[Agarwal2024] [Anthropic2024] [Bai2022] [BeauchampChildress2019] [Biderman2023]
[Brown2020] [Chakraborty2025] [Chhabra2024] [Coleman2025] [DeepSeek2025]
[Delphi2022] [Embretson2000] [Emelin2021] [Ethayarajh2020] [Ethayarajh2022]
[Foot1967] [Forbes2020] [Gallegos2024] [Gao2023] [Garcia2024]
[Graham2009] [Graham2013] [Hilliard2025] [Hui2025] [Ji2024]
[Jiao2025] [Kant1785] [Keshmirian2025] [Kohlberg1981] [Liang2024]
[Liu2024] [Lu2025] [Mill1863] [Nadeem2025] [Neuman2025a]
[Noddings1984] [OpenAI2023] [Ouyang2022] [Perez2022] [Rao2023]
[Rauh2024] [Ray2023] [Rest1999] [Rismani2025b] [Rottger2024]
[Rottger2025] [Sap2020] [Scherrer2023] [Schwartz2012] [Seror2024]
[Sorensen2024] [Sorensen2025] [Sorin2024] [Srivastava2022] [Takemoto2024]
[Thomson1985] [Touvron2023] [Weidinger2022] [Yu2024] [ZaimBinAhmad2025]
[Zhou2024] [Ziems2024]
```

**Recommendation:** Do NOT delete these now. When the paper structure is finalized (post-model-runs, Paper A vs. Paper A+B), prune orphaned refs that are truly unused. Some (e.g., `[Kant1785]`, `[Mill1863]`, `[Noddings1984]`, `[Kohlberg1981]`) are canonical philosophical references that may be cited in the comprehensive introduction or discussion once the cross-vendor sections return. Others (e.g., `[DeepSeek2025]`, `[OpenAI2023]`, `[Touvron2023]`) are vendor/model references that belong in Paper B.

---

## Notes

- This audit only checked `[AuthorYYYY]` citation key format. Inline citations like "Hendrycks et al. (2021)" without bracket keys were not checked.
- The comprehensive introduction (`introduction-comprehensive-normeval-v2.md`) was included in the scan. Most of the 123 cited keys originate there.
- 62 orphaned entries = 35% of the reference list. This is high but expected for a paper that underwent major v1→v2 expansion followed by cross-vendor section additions that may have been written as prose without formal citation keys.

---

*Filed: 2026-04-13 | CEI-Lit-WS/NORM-ETHICS/METHODS/*
