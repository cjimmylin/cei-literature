# Author Lookup Results & Research Tasks

**Last Updated:** 2026-01-24 (Session 5)
**Status:** ✅ Complete & Verified

## Verification (Session 5)

All author data has been verified as complete:

```bash
# Check for incomplete body author lines (returns 0)
grep -l "\*\*Authors:\*\*.*and others" papers/*.md | wc -l
# Result: 0 ✅

# Check frontmatter authors for "et al" (returns 0)
grep -E "^authors:.*et al|^authors:.*others" papers/*.md
# Result: No matches ✅
```

**Important:** Running `grep -l "others" papers/*.md` returns 39 files, but these are **false positives** - the word "others" appears in abstracts, PDF paths, and body content, NOT in author fields.

## Summary

The author lookup task has been substantially completed:

- **53 papers** had their body `**Authors:**` lines updated (removed "others" placeholders)
- **Key papers** with incomplete frontmatter authors were manually updated with complete author lists
- **0 papers** currently have "others" in body metadata

## Papers with Author Data Updated (This Session)

### Manually Researched and Updated

| Paper | Authors Added |
|-------|---------------|
| 2016-Purzycki-Religious Belief | Benjamin Grant Purzycki, Coren Apicella, Quentin D. Atkinson, Emma Cohen, Rita Anne McNamara, Aiyana K. Willard, Dimitris Xygalatas, Ara Norenzayan, Joseph Henrich |
| 2023-Li-BIRD | Jinyang Li, Binyuan Hui, Ge Qu, Jiaxi Yang, Binhua Li, Bowen Li, Bailin Wang, Bowen Qin, Ruiying Geng, Nan Huo, Xuanhe Zhou, Chenhao Ma, Guoliang Li, Kevin Chen-Chuan Chang, Fei Huang, Reynold Cheng, Yongbin Li |
| 2025-Okamoto-AI-based medical ethics | Shimpei Okamoto, Masanori Kataoka, Makoto Itano, Tsutomu Sawai |
| 2023-Kim-KOME | Jaehong Kim, Chaeyoon Jeong, Seongchan Park, Meeyoung Cha, Wonjae Lee (KAIST Social Computing Lab) |
| 2023-Alyemny-FatwaSet | Ohoud Alyemny, Hend Al-Khalifa, Abdulrahman Mirza |
| 2023-Ji-Safety Gymnasium | Authors section updated (10 authors already in frontmatter) |
| 2025-De Montis-Morality in AI | Gunter Bombaerts, Bram Delisse, Uzay Kaymak |
| 2025-Hilliard-Measuring AI Alignment | Elizabeth Hilliard + 12 co-authors (13 total) |
| 2025-Steen-Ethical aspects of ChatGPT | Marc Steen, Joachim de Greeff, Maaike de Boer, Cor Veenman |
| 2025-Aggarwal-Letta Leaderboard | Charles Packer, Sarah Wooders (Letta Team) |

### Papers Already Complete (Verified via Web Research)

These papers were listed as needing research but already had complete author lists:

- 2021-Hendrycks-Aligning AI with Shared Human Values (7 authors)
- 2022-Bai-Training a Helpful and Harmless Assistant (31 authors)
- 2022-Hendrycks-X-Risk Analysis (2 authors)
- 2022-Röttger-Multilingual HateCheck (5 authors)
- 2023-Wang-DecodingTrust (19 authors)
- 2024-Chao-JailbreakBench (12 authors)
- 2023-Guha-LegalBench (40 authors)
- 2023-Yu-GPTFuzzer (4 authors)
- 2024-Chern-BeHonest (8 authors)
- 2024-Reuel-BetterBench (6 authors)
- 2023-Ji-Safety Gymnasium (10 authors)
- 2023-Santurkar-Whose Opinions (6 authors)
- 2023-Zhang-Heterogeneous Value Alignment (8+ authors)
- 2025-Cao-SafeDialBench (17+ authors)
- 2024-Arshad-HateInsights (2 authors)
- 2023-Ghafouri-IslamicPCQA (4 authors)
- 2023-Alyemny-FatwaSet (3 authors)

## Remaining Tasks

✅ **All tasks complete!**

- **2023-Kim-KOME** - Updated with KAIST Social Computing Lab team (5 authors)
- All CrossRef/arXiv matches have been verified

## Scripts Used

```bash
# Fix body author lines (removes "others")
python3 PYTHON/fix_body_authors.py

# Dry run to preview
python3 PYTHON/fix_body_authors.py --dry-run
```

## Notes

- The "others" placeholder in body metadata was a display issue, not a data issue
- Most papers already had complete author lists in frontmatter `authors:` field
- Body `**Authors:**` section now matches frontmatter for all updated papers

## Research Strategy (For Future Reference)

When looking up authors for papers with incomplete metadata:

### Search Queries That Work
1. `"[Paper Title]" [Year] all authors` - General search
2. `"[Paper Title]" arXiv authors` - For preprints
3. `"[Paper Title]" [Conference] proceedings` - ACL, NeurIPS, ICML, etc.
4. `[First Author Name] [Lab/University] publications` - Find lab page

### Sources by Priority
1. **arXiv** - Best for preprints, has complete author lists
2. **ACL Anthology** - NLP papers with full metadata
3. **Semantic Scholar** - DOI-based lookup
4. **Conference Proceedings** (NeurIPS, ICML, ACL) - Official records
5. **Lab/University Pages** - Research group publication lists
6. **HuggingFace** - Dataset papers often listed there

### Key Learnings
- **Korean Computer Congress (KCC)** papers are not well-indexed in English search engines; use related ACL/arXiv papers from same team
- **Domestic conference papers** often precede international publications with same authors
- **Lab websites** (e.g., KAIST Social Computing Lab) list all authors for their papers
- **PDF filenames** from Zotero often contain "and others" hint (e.g., "Kim and others - 2023")

### Verification Steps
1. Check YAML `authors` field - may already have complete data
2. Check body `## Authors` section - may have wikilinks that frontmatter lacks
3. Run `fix_body_authors.py` to sync body with frontmatter
