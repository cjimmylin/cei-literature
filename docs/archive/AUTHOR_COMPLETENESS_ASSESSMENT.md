# Author Data Completeness Assessment

**Date:** January 24, 2026
**Scope:** First 100 papers from `/papers/` directory
**Total papers analyzed:** 100
**Total papers in vault:** 580
**Total papers in Base.md CSV:** 535

---

## Executive Summary

This assessment evaluates the completeness and quality of author data across the CEI Literature Vault. The analysis identifies papers with incomplete author information, abbreviated names, and missing metadata connections.

### Key Findings

| Category | Count | Percentage | Status |
|----------|-------|-----------|--------|
| Papers with "others" or "et al" | 8 | 8.0% | ⚠️ Needs expansion |
| Papers with abbreviated names | 2 | 2.0% | ⚠️ Needs expansion |
| Papers missing author wikilinks | 89 | 89.0% | ⚠️ Major gap |
| Papers with CSV data missing | 10 | 10.0% | ⚠️ Inconsistent |
| **Papers with complete author data** | **~1** | **~1.0%** | ✓ Minimal |

---

## Category 1: Papers with "others" or "et al" (8 papers)

Papers with incomplete author lists using "et al" or "others" placeholders. These papers have truncated author information that should be expanded.

### Affected Papers

1. **2016-Purzycki-Religious Belief and the Moral Circle.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Purzycki-Religious Belief and the Moral Circle.md`
   - Title: Religious Belief and the Moral Circle: Cross-Cultural Dataset
   - Year: 2016
   - CSV Authors: `Purzycki, B. G.; others, and`
   - Issue: Uses abbreviated name + "others" placeholder

2. **2018-Crone-The Socio-Moral Image Database (SMID).md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Crone-The Socio-Moral Image Database (SMID).md`
   - Title: The Socio-Moral Image Database (SMID): A Novel Stimulus Set for the Study of Social Morality
   - Year: 2018
   - CSV Authors: `Crone, Deon; others`
   - Issue: Incomplete author list

3. **2021-Hendrycks-Aligning AI with Shared Human Values.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2021-Hendrycks-Aligning AI with Shared Human Values.md`
   - Title: Aligning AI with Shared Human Values: The ETHICS Benchmark
   - Year: 2020
   - CSV Authors: `Hendrycks, Dan; Burns, Collin; Basart, Steven; Critch, Andrew; Li, Jerry; Song, Dawn; Steinhardt, Jacob; others`
   - Issue: "others" placeholder after listing 7 authors

4. **2022-Bai-Training a Helpful and Harmless Assistant with.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Bai-Training a Helpful and Harmless Assistant with.md`
   - Title: Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback
   - Year: 2022
   - CSV Authors: `Bai, Yuntao; Jones, Andy; others`
   - Issue: Truncated after 2 authors

5. **2022-Ganguli-Red Teaming Language Models to Reduce Harms.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Ganguli-Red Teaming Language Models to Reduce Harms.md`
   - Title: Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned
   - Year: 2022
   - CSV Authors: `Ganguli, Deep; others`
   - Issue: Minimal author info before "others"

6. **2022-Hendrycks-X-Risk Analysis for AI Research.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Hendrycks-X-Risk Analysis for AI Research.md`
   - Title: X-Risk Analysis for AI Research
   - Year: 2022
   - CSV Authors: `Hendrycks, Dan; others`
   - Issue: Only first author listed

7. **2022-Röttger-Multilingual HateCheck.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Röttger-Multilingual HateCheck.md`
   - Title: Multilingual HateCheck: Functional Tests for Hate Speech Detection Models in 16 Languages
   - Year: 2022
   - CSV Authors: `Röttger, Paul; others`
   - Issue: Only first author listed

8. **2023-Alyemny-FatwaSet.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2023-Alyemny-FatwaSet.md`
   - Title: FatwaSet: Large-scale Dataset for Islam Fatwa Question Answering
   - Year: 2023
   - CSV Authors: `Alyemny, A.; others`
   - Issue: Abbreviated first name + "others" placeholder

---

## Category 2: Papers with Abbreviated Author Names (2 papers)

Papers where author names are abbreviated (e.g., "J. Smith" instead of full name). This format makes it difficult to create proper author wikilinks and track researcher profiles.

### Affected Papers

1. **2016-Purzycki-Religious Belief and the Moral Circle.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Purzycki-Religious Belief and the Moral Circle.md`
   - Title: Religious Belief and the Moral Circle: Cross-Cultural Dataset
   - Year: 2016
   - Abbreviated names: `B. G` (Purzycki, B. G.)
   - CSV Authors: `Purzycki, B. G.; others, and`
   - Impact: Cannot reliably link to author page without full first name

2. **2022-Bago-Situational factors shape moral judgments in the.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Bago-Situational factors shape moral judgments in the.md`
   - Title: Situational factors shape moral judgments in the trolley dilemma in Eastern, Southern and Western cultures
   - Year: 2019
   - Abbreviated names: `M. J` (appears in author list)
   - CSV Authors: `Bago, Bence; Kovacs, Marton; Protzko, John; Kekecs, Zoltan; Nagy, Tamas; Hoekstra, Rink; Li, Manyu; Musser, Erica D.; ...`
   - Impact: Truncation in CSV export cuts off full author information

---

## Category 3: Papers Missing Author Wikilinks in Body (89 papers)

**Critical Finding:** 89 out of 100 papers (89%) are missing author wikilinks in their body text. This means the author files in `/Authors/` directory are not being referenced from individual papers.

### Sample of Affected Papers (first 20 shown)

Papers should contain wikilinks like `[[Author Name]]` in their body text to reference author profiles, but currently have zero wikilinks:

1. **2010-Project-GurbaniDB.md** - Authors: `Project, The Sikher`
2. **2015-Clifford-Moral Foundations Vignettes.md** - Authors: `Clifford, Scott; Iyengar, Vijeth; Cabeza, Raúl; Sinnott-Armstrong, Walter`
3. **2016-Amodei-Concrete Problems in AI Safety.md** - Authors: `Amodei, Dario; Olah, Chris; Steinhardt, Jacob; Christiano, Paul; Schulman, John;`
4. **2016-Bolukbasi-Man is to Computer Programmer as Woman is to.md** - Authors: `Bolukbasi, Tolga; Chang, Kai-Wei; Zou, James; Saligrama, Venkatesh; Kalai, Adam`
5. **2016-Purzycki-Cross-cultural dataset for the evolution of.md** - Authors: `Purzycki, Benjamin Grant; Apicella, Coren; Atkinson, Quentin D.; Cohen, Emma; Mc...`
6. **2016-Purzycki-Religious Belief and the Moral Circle.md** - Authors: `Purzycki, B. G.; others, and`
7. **2018-Awad-The Moral Machine experiment.md** - Authors: `Awad, Edmond; Dsouza, Sohan; Kim, Richard; Schulz, Jonathan; Henrich, Joseph; Sh...`
8. **2018-Behzadan-TrolleyMod v1.0.md** - Authors: `Behzadan, Vahid; Minton, James; Munir, Arslan`
9. **2018-Crone-The Socio-Moral Image Database (SMID).md** - Authors: `Crone, Deon; others`
10. **2018-Dixon-Measuring and Mitigating Unintended Bias in Text.md** - Authors: `Dixon, Lucas; Li, John; Sorensen, Jeffrey; Thain, Nithum; Vasserman, Lucy`
11. **2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred.md** - Authors: `Kiritchenko, Svetlana; Mohammad, Saif M.`
12. **2018-Noothigattu-A Voting-Based System for Ethical Decision Making.md** - Authors: `Noothigattu, Ritesh; Gaikwad, Snehalkumar 'Neil' S.; Awad, Edmond; Dsouza, Sohan`
13. **2018-Zhao-Finding Answers from the Word of God.md** - Authors: `Zhao, Helen Jiahe; Liu, Jiamou`
14. **2018-Zhao-Gender Bias in Contextualized Word Embeddings.md** - Authors: `Zhao, Jieyu; Zhou, Yichao; Li, Zeyu; Wang, Wei; Chang, Kai-Wei`
15. **2018-Zhao-Learning Gender-Neutral Word Embeddings.md** - Authors: `Zhao, Jieyu; Zhou, Yichao; Li, Zeyu; Wang, Wei; Chang, Kai-Wei`
16. **2019-Basile-SemEval-2019 Task 5.md** - Authors: `Basile, Valerio; Bosco, Cristina; Fersini, Elisabetta; Nozza, Debora; Patti, Viv...`
17. **2019-De-Arteaga-Bias in Bios.md** - Authors: `De-Arteaga, Maria; Romanov, Alexey; Wallach, Hanna; Chayes, Jennifer; Borgs, Chr...`
18. **2019-He-Unlearn Dataset Bias in Natural Language.md** - Authors: `He, He; Zha, Sheng; Wang, Haohan`
19. **2019-Ibrohim-Multi-label Hate Speech and Abusive Language.md** - Authors: `Ibrohim, Muhammad Okky; Budi, Indra`
20. **2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification.md** - Authors: `Jigsaw, Kaggle /`

*(Full list of 89 papers available - showing sample above)*

### Impact Analysis

- The `/Authors/` directory contains ~2,936 author files
- However, these author profiles are not connected to papers via wikilinks
- This breaks the knowledge graph that could show: paper → authors → research collaborations → related papers
- Example missing connection: `[[Amodei, Dario]]` in the Concrete Problems in AI Safety paper would link to the author profile directory

---

## Category 4: CSV Data Missing (10 papers)

Papers that have author information in the markdown files but are missing from the Base.md CSV. This indicates inconsistency between data sources.

### Affected Papers

1. **2019-He-Unlearn Dataset Bias in Natural Language.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-He-Unlearn Dataset Bias in Natural Language.md`
   - File Authors: `He, He; Zha, Sheng; Wang, Haohan`
   - Status: CSV entry missing entirely

2. **2020-Gehman-RealToxicityPrompts.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2020-Gehman-RealToxicityPrompts.md`
   - File Authors: `Gehman, Samuel; Gururangan, Suchin; Sap, Maarten; Choi, Yejin; Smith, Noah A.`
   - Status: CSV entry missing entirely

3. **2020-Kumar-Evaluating Aggression Identification in Social.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2020-Kumar-Evaluating Aggression Identification in Social.md`
   - File Authors: `Kumar, Ritesh; Ojha, Atul Kr.; Malmasi, Shervin; Zampieri, Marcos`
   - Status: CSV entry missing entirely

4. **2020-Zampieri-SemEval-2020 Task 12.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2020-Zampieri-SemEval-2020 Task 12.md`
   - File Authors: `Zampieri, Marcos; Nakov, Preslav; Rosenthal, Sara; Atanasova, Pepa; Karadzhov, Georgi; Mubarak, Hamd`
   - Status: CSV entry missing entirely

5. **2021-Barikeri-REDDITBIAS.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2021-Barikeri-REDDITBIAS.md`
   - File Authors: `Barikeri, Soumya; Lauscher, Anne; Vulić, Ivan; Glavaš, Goran`
   - Status: CSV entry missing entirely

6. **2021-Cercas Curry-ConvAbuse.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2021-Cercas Curry-ConvAbuse.md`
   - File Authors: `Cercas Curry, Amanda; Abercrombie, Gavin; Rieser, Verena`
   - Status: CSV entry missing entirely

7. **2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md`
   - File Authors: `Levy, Shahar; Lazar, Koren; Stanovsky, Gabriel`
   - Status: CSV entry missing entirely

8. **2021-Wang-SemEval-2021 Task 5 Toxic Spans Detection.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2021-Wang-SemEval-2021 Task 5 Toxic Spans Detection.md`
   - File Authors: `Wang, Zhen; Fan, Hongjie; Liu, Junfei`
   - Status: CSV entry missing entirely

9. **2022-Chalkidis-FairLex.md**
   - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Chalkidis-FairLex.md`
   - File Authors: `Chalkidis, Ilias; Pasini, Tommaso; Zhang, Sheng; Tomada, Letizia; Schwemer, Sebastian Felix; Søgaard`
   - Status: CSV entry missing entirely

10. **2022-Hu-"I'm sorry to hear that".md**
    - Path: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2022-Hu-"I'm sorry to hear that".md`
    - File Authors: `Hu, Minda; Li, Muzhi; Wang, Yasheng; King, Irwin`
    - Status: CSV entry missing entirely

---

## Overall Statistics

### Data Completeness Score

```
Perfect Author Records:      1 / 100  (1.0%)
With Minor Issues:          11 / 100  (11.0%)  [abbreviated names or "others"]
With Major Issues:          89 / 100  (89.0%)  [missing wikilinks]
Missing from CSV:           10 / 100  (10.0%)
─────────────────────────────────────────────
Estimated Complete:         ~1 / 100  (1.0%)
```

### Data Quality Metrics

| Metric | Value |
|--------|-------|
| Average authors per paper | ~4-5 |
| Papers with full author lists | ~92 |
| Papers with "others" truncation | 8 (8%) |
| Papers with abbreviated names | 2 (2%) |
| Papers with wikilinks to authors | 11 (11%) |
| Papers missing wikilinks entirely | 89 (89%) |
| Wikilink coverage | 11.0% |

---

## Recommendations

### Priority 1: Add Author Wikilinks (89 papers)
- **Impact:** High - Connects author profiles to papers
- **Effort:** Medium - Systematic batch process
- **Estimated Time:** 4-6 hours
- **Action:** Generate author wikilinks in paper body text linking to `/Authors/` directory files

Example transformation:
```markdown
# Before
This paper studies hate speech detection by examining multiple perspectives.

# After
This paper studies hate speech detection. The research by [[Mathew, Binny]] and [[Biemann, Chris]]
examines multiple perspectives on explainability in hate speech classification...
```

### Priority 2: Expand "others" Entries (8 papers)
- **Impact:** Medium - Better author attribution
- **Effort:** High - Requires research for each paper
- **Estimated Time:** 2-3 hours
- **Action:** Look up full author lists from original publications and update CSV and markdown files

### Priority 3: Expand Abbreviated Names (2 papers)
- **Impact:** Low - Only affects 2 papers
- **Effort:** Low - Straightforward research
- **Estimated Time:** 15 minutes
- **Action:** Expand "B. G." to "Benjamin Grant" and similar abbreviations

### Priority 4: Sync CSV with Markdown Files (10 papers)
- **Impact:** Medium - Ensure data consistency
- **Effort:** Medium - Add missing entries to CSV
- **Estimated Time:** 1-2 hours
- **Action:** Add the 10 papers missing from CSV to Base.md

---

## Appendix: File Locations

**Configuration files:**
- Base.md: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Base.md`
- Papers directory: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/`
- Authors directory: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/Authors/`

**Related documentation:**
- CLAUDE.md: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/CLAUDE.md`
- LLM_CONTEXT.md: `/Users/jimmy.lin/Documents/CEI-Literature-Vault/LLM_CONTEXT.md`

---

**Report generated:** 2026-01-24
**Analysis scope:** First 100 papers
**Total vault size:** 580 papers
