# Author Profile Enrichment Task Tracker

**Created:** 2026-01-24
**Status:** In Progress
**Scope:** A, B, D, and E Authors

---

## Project Overview

Systematic enrichment of author profiles in the CEI Literature Vault, focusing on authors starting with A and B.

### Goals
1. Complete all incomplete/stub author profiles
2. Consolidate duplicate profiles (e.g., "Amanda Askell" vs "Askell, Amanda")
3. Update template with best practices
4. Ensure consistent quality across all profiles

---

## Statistics (Updated 2026-01-24)

| Metric | A Authors | B Authors | D Authors | E Authors | Total |
|--------|-----------|-----------|-----------|-----------|-------|
| **Total Files** | 406 | 247 | 231 | 106 | 990 |
| **Stub Files (<600 bytes)** | 263 | ~152 | 217 | 104 | ~736 |
| **Enriched Files** | 143 | 95 | 14 | 2 | 254 |
| **Duplicates Consolidated** | 23 | 9 | TBD | TBD | 32+ |

---

## Completed Tasks

- [x] Created task.md tracking file
- [x] Updated TEMPLATE.md with best practices (based on Christopher Olah profile)
- [x] Identified and consolidated A author duplicates (23 pairs)
- [x] Identified and consolidated B author duplicates (9 pairs)
- [x] Completed A-Residual-8 (6 high-impact authors)

### A-Residual-8 Completed Authors
1. [x] Amanda McCroskery - Google DeepMind, AI Ethics
2. [x] Amandeep Kumar - Johns Hopkins PhD, Amazon AI Fellow
3. [x] Amandeep Singh - Vector Institute, HumaniBench
4. [x] Amar Gupta - MIT CSAIL, IEEE Life Fellow
5. [x] Ameeta Agrawal - Portland State, NLP/Fairness
6. [x] Amelia Glaese - OpenAI (ex-DeepMind), Sparrow lead

---

## Batch Progress

### A Authors

| Batch | Range | Status | Notes |
|-------|-------|--------|-------|
| A-Residual-1 | Aa-Ad | Complete | From previous session |
| A-Residual-2 | Ae-Ah | Complete | From previous session |
| A-Residual-3 | Ai-Al | Complete | From previous session |
| A-Residual-4 | Al-Am | Complete | From previous session |
| A-Residual-5 | Am-An | Complete | From previous session |
| A-Residual-6 | An-Ap | Complete | From previous session |
| A-Residual-7 | Aq-As | Complete | From previous session |
| A-Residual-8 | At-Az | **Complete** | 6 authors enriched this session |
| A-Consolidation | Duplicates | **Complete** | 23 pairs consolidated |
| A-Review | Full audit | **In Progress** | 263 stubs remaining |

### B Authors

| Batch | Range | Status | Notes |
|-------|-------|--------|-------|
| B-Consolidation | Duplicates | **Complete** | 9 pairs consolidated |
| B-Residual-1 | Ba-Bd | Pending | |
| B-Residual-2 | Be-Bh | Pending | |
| B-Residual-3 | Bi-Bl | Pending | |
| B-Residual-4 | Bm-Bp | Pending | |
| B-Residual-5 | Bq-Bt | Pending | |
| B-Residual-6 | Bu-Bz | Pending | |
| B-Review | Full audit | Pending | |

### D Authors

| Batch | Range | Status | Notes |
|-------|-------|--------|-------|
| D-Batch-1 | D'Al-Dan S | **In Progress** | 30 authors (agent running) |
| D-Batch-2 | Dan P-Dav G | **In Progress** | 30 authors (agent running) |
| D-Batch-3 | Dav H-Deh | **In Progress** | 30 authors (agent running) |
| D-Batch-4 | Del-Dia | **In Progress** | 30 authors (agent running) |
| D-Batch-5 | Dia A-Diy | **In Progress** | 30 authors (agent running) |
| D-Batch-6 | Dja-Dor | **In Progress** | 30 authors (agent running) |
| D-Batch-7 | Dor-Dzi | **In Progress** | 37 authors (agent running) |

### E Authors

| Batch | Range | Status | Notes |
|-------|-------|--------|-------|
| E-Batch-1 | Ebr-Eli H | **In Progress** | 35 authors (agent running) |
| E-Batch-2 | Eli G-Eri X | **In Progress** | 35 authors (agent running) |
| E-Batch-3 | Eri Z-Evg | **In Progress** | 34 authors (agent running) |

---

## Remaining Work

### A Authors (~263 stubs)
Need to scan all A author stubs and enrich with:
- Verified affiliation
- Research interests (specific, not placeholder)
- At least one external link
- Biographical summary

### B Authors (~152 stubs)
Same enrichment required.

---

## Enrichment Template Fields

### Required Fields (YAML)
- `name` - Full name
- `title` - Current position
- `affiliation` - Current institution
- `highest_degree` - Degree, University (Year)
- `research_interests` - List of 3-5 topics
- `website` - Personal/lab website
- `google_scholar` - Profile URL
- `semantic_scholar` - Profile URL

### Optional Fields (YAML)
- `email` - Contact (if public)
- `notable_awards` - List of awards
- `github` - Profile URL
- `twitter` - Profile URL
- `linkedin` - Profile URL
- `orcid`, `arxiv`, `dblp`, `openreview`, `philpapers`, `researchgate`

### Body Sections
1. **Biographical Summary** - 2-3 sentences, third person
2. **Research & Impact** - Current Focus + Significant Achievements
3. **Major Publications** - 2-4 most cited/impactful
4. **Papers in this Vault** - Wikilinks to vault papers
5. **External Links & Profiles** - Organized by category
6. **Notes** - Internal notes for CEI

---

## Session Log

### 2026-01-24 (Current Session)

**Completed:**
- Task.md created
- TEMPLATE.md updated with best practices
- Consolidated 23 A author duplicates
- Consolidated 9 B author duplicates
- Enriched 6 A-Residual-8 authors:
  - Amelia Glaese (OpenAI/DeepMind, Sparrow)
  - Amanda McCroskery (DeepMind, AI Ethics)
  - Ameeta Agrawal (Portland State, NLP)
  - Amar Gupta (MIT CSAIL, IEEE Fellow)
  - Amandeep Kumar (JHU PhD, Amazon Fellow)
  - Amandeep Singh (Vector Institute, HumaniBench)

**In Progress (Interrupted - resume in next session):**
- Batch enrichment of D authors (7 batches were running, ~217 stubs remaining)
- Batch enrichment of E authors (3 batches were running, ~104 stubs remaining)
- B authors: 6 batches pending (~152 stubs)
- A authors: Review pending (~263 stubs)

**Notable Researchers Being Enriched:**
- D: Dario Amodei (Anthropic), Dan Jurafsky (Stanford), Diyi Yang (Stanford), David Krueger (Cambridge), Nouha Dziri
- E: Ethan Perez (Anthropic), Evan Hubinger (Anthropic), Ece Kamar (Microsoft), Emily Sheng (USC)

---

## Quality Checklist

For each enriched profile:
- [ ] All required YAML fields populated
- [ ] Biographical summary is factual and current
- [ ] Research interests match author's actual focus
- [ ] Papers in vault linked correctly
- [ ] External links verified working
- [ ] No duplicate files remain

---

*Last updated: 2026-01-24*
