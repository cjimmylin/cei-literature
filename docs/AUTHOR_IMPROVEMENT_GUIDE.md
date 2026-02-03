# Author Data Improvement Guide

**Date:** January 24, 2026
**Purpose:** Actionable improvements to enhance author data completeness and connectivity

---

## Quick Reference: Issues Found

| Issue | Count | Severity | Fix Time |
|-------|-------|----------|----------|
| Missing wikilinks in body | 89 | **HIGH** | 4-6 hrs |
| "others" truncation | 8 | **MEDIUM** | 2-3 hrs |
| Abbreviated names | 2 | **LOW** | 15 min |
| Missing from CSV | 10 | **MEDIUM** | 1-2 hrs |

---

## Issue 1: Missing Author Wikilinks (89 papers)

### The Problem
89 papers have author names in the frontmatter but NO wikilinks to author profiles in the body text. This breaks the knowledge graph connection between papers and `/Authors/` directory profiles.

### Current State
```markdown
---
authors: "Amodei, Dario; Olah, Chris; Steinhardt, Jacob; Christiano, Paul; Schulman, John;"
---

# Concrete Problems in AI Safety

This paper addresses safety challenges in AI development...
```

### Target State
```markdown
---
authors: "Amodei, Dario; Olah, Chris; Steinhardt, Jacob; Christiano, Paul; Schulman, John;"
---

# Concrete Problems in AI Safety

This paper addresses safety challenges in AI development. The research by [[Amodei, Dario]],
[[Olah, Chris]], [[Steinhardt, Jacob]], [[Christiano, Paul]], and [[Schulman, John]]
identifies concrete problems in AI safety...
```

### How to Fix

#### Option A: Manual Process (Best for understanding)
1. Open paper file
2. Read the abstract/introduction
3. Insert author wikilinks naturally in first 1-2 paragraphs
4. Use format: `[[LastName, FirstName]]` to match author directory naming
5. Save file

#### Option B: Batch Script (Fastest, needs verification)
```python
# Pseudo-code for batch linking
for paper in papers:
    authors = paper.frontmatter['authors']
    author_list = parse_authors(authors)

    # Insert after first paragraph or in introduction
    insertion_point = find_first_paragraph(paper.body)
    mention_text = f"Research by {', '.join([f'[[{a}]]' for a in author_list])}"

    paper.body = insert_at(paper.body, insertion_point, mention_text)
    write_paper(paper)
```

#### Validation Checklist
- [ ] Each author in frontmatter has a corresponding wikilink in body
- [ ] Wikilinks use correct format: `[[LastName, FirstName]]`
- [ ] Wikilinks appear in natural context (introduction/abstract area)
- [ ] No duplicate wikilinks for same author
- [ ] YAML frontmatter still valid after edit

### Affected Files (First 20)
1. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2010-Project-GurbaniDB.md`
2. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2015-Clifford-Moral Foundations Vignettes.md`
3. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Amodei-Concrete Problems in AI Safety.md`
4. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Bolukbasi-Man is to Computer Programmer as Woman is to.md`
5. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Purzycki-Cross-cultural dataset for the evolution of.md`
6. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2016-Purzycki-Religious Belief and the Moral Circle.md`
7. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Awad-The Moral Machine experiment.md`
8. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Behzadan-TrolleyMod v1.0.md`
9. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Crone-The Socio-Moral Image Database (SMID).md`
10. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Dixon-Measuring and Mitigating Unintended Bias in Text.md`
11. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Kiritchenko-Examining Gender and Race Bias in Two Hundred.md`
12. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Noothigattu-A Voting-Based System for Ethical Decision Making.md`
13. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Zhao-Finding Answers from the Word of God.md`
14. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Zhao-Gender Bias in Contextualized Word Embeddings.md`
15. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2018-Zhao-Learning Gender-Neutral Word Embeddings.md`
16. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-Basile-SemEval-2019 Task 5.md`
17. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-De-Arteaga-Bias in Bios.md`
18. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-He-Unlearn Dataset Bias in Natural Language.md`
19. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-Ibrohim-Multi-label Hate Speech and Abusive Language.md`
20. `/Users/jimmy.lin/Documents/CEI-Literature-Vault/papers/2019-Jigsaw-Jigsaw Unintended Bias in Toxicity Classification.md`

*(See AUTHOR_COMPLETENESS_ASSESSMENT.md for complete list of all 89 papers)*

---

## Issue 2: "others" and "et al" Truncation (8 papers)

### The Problem
Author lists are incomplete, using placeholder text like "others" or "et al" instead of full names.

### Current State
```
Authors: Bai, Yuntao; Jones, Andy; others
```

### Target State
```
Authors: Bai, Yuntao; Jones, Andy; Christiano, Paul; Leike, Jan; Brown, Tom; ...
```

### Affected Papers

1. **2016-Purzycki-Religious Belief and the Moral Circle.md**
   - Current: `Purzycki, B. G.; others, and`
   - Action: Need to find original paper and expand with full names
   - Note: Also has abbreviated name issue (B. G. should be Benjamin Grant)

2. **2018-Crone-The Socio-Moral Image Database (SMID).md**
   - Current: `Crone, Deon; others`
   - Action: Check PDF or DOI for full author list

3. **2021-Hendrycks-Aligning AI with Shared Human Values.md**
   - Current: `Hendrycks, Dan; Burns, Collin; Basart, Steven; Critch, Andrew; Li, Jerry; Song, Dawn; Steinhardt, Jacob; others`
   - Action: Remove "others" and add remaining authors (check arxiv:2012.02413)

4. **2022-Bai-Training a Helpful and Harmless Assistant with.md**
   - Current: `Bai, Yuntao; Jones, Andy; others`
   - Action: Check Anthropic paper for full author list

5. **2022-Ganguli-Red Teaming Language Models to Reduce Harms.md**
   - Current: `Ganguli, Deep; others`
   - Action: Check Anthropic paper or arXiv for full author list

6. **2022-Hendrycks-X-Risk Analysis for AI Research.md**
   - Current: `Hendrycks, Dan; others`
   - Action: Check paper for full author list

7. **2022-Röttger-Multilingual HateCheck.md**
   - Current: `Röttger, Paul; others`
   - Action: Check ACL 2022 paper for full author list

8. **2023-Alyemny-FatwaSet.md**
   - Current: `Alyemny, A.; others`
   - Action: Expand abbreviated name, add other authors

### How to Fix

1. **Locate the original paper** (PDF, arXiv, or ACL Anthology)
2. **Extract complete author list** from paper metadata
3. **Update Base.md CSV** in Author column with full names
4. **Update paper markdown** frontmatter if authors field exists
5. **Verify format**: Use semicolon separator, "LastName, FirstName" format

### Research Sources
- **arXiv**: Search by DOI or paper title
- **ACL Anthology**: For NLP papers
- **DOI.org**: Resolve DOI to original source
- **Google Scholar**: Search for paper and view author list
- **Authors' institutional websites**: Some list all publications with co-authors

---

## Issue 3: Abbreviated Author Names (2 papers)

### The Problem
Author names appear abbreviated, making it difficult to create proper wikilinks or identify researchers.

### Affected Papers

1. **2016-Purzycki-Religious Belief and the Moral Circle.md**
   - Current: `Purzycki, B. G.; others, and`
   - Should be: `Purzycki, Benjamin Grant`
   - Action: Simple name expansion

2. **2022-Bago-Situational factors shape moral judgments in the.md**
   - Current: Contains `M. J` abbreviation
   - Action: Find full name from paper

### How to Fix

1. Search the paper PDF for full author names
2. Look for author affiliations/bios which usually have full names
3. Check Google Scholar profile for the author
4. Update Base.md CSV Author field
5. Update paper markdown if authors field uses abbreviated names

---

## Issue 4: CSV Data Missing (10 papers)

### The Problem
10 papers exist in `/papers/` but don't have entries in `Base.md` CSV.

### Affected Papers

| File | Authors | Status |
|------|---------|--------|
| 2019-He-Unlearn Dataset Bias in Natural Language.md | He, He; Zha, Sheng; Wang, Haohan | Missing from CSV |
| 2020-Gehman-RealToxicityPrompts.md | Gehman, Samuel; Gururangan, Suchin; Sap, Maarten; Choi, Yejin; Smith, Noah A. | Missing from CSV |
| 2020-Kumar-Evaluating Aggression Identification in Social.md | Kumar, Ritesh; Ojha, Atul Kr.; Malmasi, Shervin; Zampieri, Marcos | Missing from CSV |
| 2020-Zampieri-SemEval-2020 Task 12.md | Zampieri, Marcos; Nakov, Preslav; Rosenthal, Sara; Atanasova, Pepa; Karadzhov, Georgi; Mubarak, Hamd | Missing from CSV |
| 2021-Barikeri-REDDITBIAS.md | Barikeri, Soumya; Lauscher, Anne; Vulić, Ivan; Glavaš, Goran | Missing from CSV |
| 2021-Cercas Curry-ConvAbuse.md | Cercas Curry, Amanda; Abercrombie, Gavin; Rieser, Verena | Missing from CSV |
| 2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md | Levy, Shahar; Lazar, Koren; Stanovsky, Gabriel | Missing from CSV |
| 2021-Wang-SemEval-2021 Task 5 Toxic Spans Detection.md | Wang, Zhen; Fan, Hongjie; Liu, Junfei | Missing from CSV |
| 2022-Chalkidis-FairLex.md | Chalkidis, Ilias; Pasini, Tommaso; Zhang, Sheng; Tomada, Letizia; Schwemer, Sebastian Felix; Søgaard | Missing from CSV |
| 2022-Hu-"I'm sorry to hear that".md | Hu, Minda; Li, Muzhi; Wang, Yasheng; King, Irwin | Missing from CSV |

### How to Fix

These papers have complete metadata in their markdown files but need to be added to Base.md CSV.

1. Extract metadata from markdown frontmatter
2. Find DOI or additional information from PDF
3. Add new row to Base.md with all available columns
4. Run `/import-papers` or equivalent to sync with vault

---

## Recommended Implementation Order

### Phase 1: Quick Wins (15 minutes)
- [ ] Expand 2 abbreviated author names (Issue 3)

### Phase 2: High Impact (4-6 hours)
- [ ] Add wikilinks to 89 papers (Issue 1)
  - Option: Script batch addition + manual verification
  - Or: Prioritize highly-cited papers first (easier to find full author lists)

### Phase 3: Data Consistency (1-2 hours)
- [ ] Add 10 missing papers to Base.md CSV (Issue 4)

### Phase 4: Completeness (2-3 hours)
- [ ] Expand "others" in 8 papers (Issue 2)
  - Prioritize recent papers first (more likely to have accessible metadata)

---

## Validation Checklist

After implementing improvements, verify:

- [ ] All papers have authors field in frontmatter
- [ ] No author names contain "others" or "et al"
- [ ] No author names are abbreviated (except legitimate ones like "Jr.", "Sr.", "II")
- [ ] 100% of papers have at least one author wikilink in body
- [ ] All wikilinks use correct format: `[[LastName, FirstName]]`
- [ ] All 10 missing papers appear in Base.md CSV
- [ ] YAML frontmatter is valid in all modified files
- [ ] Author directory in `/Authors/` matches referenced names

---

## Tools & Resources

### Academic Databases
- **arXiv.org**: For CS/ML preprints - https://arxiv.org
- **ACL Anthology**: For NLP papers - https://aclanthology.org
- **DOI.org**: Universal DOI resolver - https://doi.org
- **Google Scholar**: https://scholar.google.com
- **Semantic Scholar**: https://semanticscholar.org
- **DBLP Computer Science Bibliography**: https://dblp.uni-trier.de

### Vault-Specific Scripts
```bash
# Check for papers with incomplete data
grep -r "authors:" papers/ | grep -i "others\|et al"

# Find papers without wikilinks in body
for f in papers/*.md; do
  if ! grep -q "\[\[" "$f"; then
    echo "$f has no wikilinks"
  fi
done

# Validate YAML frontmatter
python3 PYTHON/yaml_frontmatter_utils.py --validate papers/
```

---

## Notes

- Always use `yaml_frontmatter_utils.py` when modifying frontmatter to avoid corruption
- When adding wikilinks, ensure they appear in natural language context
- For papers with many authors, consider listing key authors with wikilinks
- When expanding "others", verify the source (PDF, institutional website, or DOI)
- Keep commit messages clear: "Add author wikilinks to 5 papers" or "Expand author list in ETHICS paper"

---

**Last Updated:** 2026-01-24
**Analyzer:** Claude Code
**Next Review:** After implementing Priority 1 & 2 fixes
