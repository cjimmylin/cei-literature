# Research Paper Discovery Workflow Learnings

**Created:** 2026-01-25
**Updated:** 2026-01-25 (Session 19)
**Sessions:** 12, 13, 14, 16-19 (Consequentialist, Deontological, Virtue, Deontic)
**Purpose:** Consolidated learnings for future LLM sessions on academic paper discovery and import

---

## Overview

This document captures the workflow, solutions, and best practices learned during a session focused on finding and importing academic papers on consequentialist/utilitarian ethics for AI values alignment.

## Successful Workflow Pattern

### Phase 1: Vault Inventory
Before searching externally, check existing vault contents:
```bash
# Search existing papers for topic keywords
grep -l "utilitarian\|consequentialist" papers/*.md

# Check existing tags in frontmatter
grep "newtags.*Utilitarian" papers/*.md
```

### Phase 2: Web Search Strategy
Use multiple search queries with specific academic terms:
1. `"consequentialist ethics" "AI alignment" 2024 2025` - Recent papers
2. `"utilitarian ethics" LLM "moral reasoning"` - LLM-specific
3. `"trolley problem" "large language model"` - Classic dilemmas
4. `"moral foundations theory" AI benchmark` - Psychology frameworks
5. `site:arxiv.org "utilitarian" "language model"` - Preprint focus

### Phase 3: Source Prioritization
Order of preference for PDF availability:
1. **arXiv** - Always open access (`arxiv.org/abs/XXX` → `arxiv.org/pdf/XXX.pdf`)
2. **ACL Anthology** - NLP papers (`aclanthology.org/XXX/` → `aclanthology.org/XXX.pdf`)
3. **OpenReview** - ML conferences (`openreview.net/forum?id=XXX` → `openreview.net/pdf?id=XXX`)
4. **Nature/Springer** - Often open access for ethics papers
5. **PNAS/Science** - Usually paywalled, mark as PENDING

### Phase 4: Paper Entry Creation
YAML frontmatter template for ethics papers:
```yaml
---
Human View:
Human View Date:
Human View note:
Not AI:
key: AUTHOR2024VENUE
type: journalArticle|conferencePaper|preprint
short_title: "Short Title"
year: 2024
first_author: "[[First Author]]"
authors: "First Author; Second Author; Third Author"
doi: 10.xxxx/xxxxx
url: "https://..."
external_pdf: "https://direct-pdf-url"
publication: "Journal or Conference Name"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: Yes|N/A
newtags: "Utilitarianism, Deontology, LLM Evaluation, AI Ethics"
key_contribution: "One-sentence description of main contribution"
significance: "One-sentence on why this matters"
tags:
pdf_extract:
abstract: "Full abstract text"
paper_summary:
local_pdf:
ethics_overall: Yes
virtue_ethics: Yes|No
deontological_ethics: Yes|No
utilitarian_ethics: Yes|No
is_benchmark: Yes|No
is_eval: Yes|No
is_dataset: Yes|No
data_description: "Description of any datasets used/created"
data_metrics: "Metrics used for evaluation"
---
```

### Phase 5: PDF Download
```bash
# Download PDF
curl -L -o "PDFs/<filename>.pdf" "<pdf_url>"

# Verify it's actually a PDF (not HTML error page)
file "PDFs/<filename>.pdf"
ls -lh "PDFs/<filename>.pdf"

# If HTML instead of PDF, move to recycle bin
mv "PDFs/<filename>.pdf" "RECYCLE-BIN/"
```

### Phase 6: PDF Extraction
```bash
# IMPORTANT: Set PYTHONPATH for module imports
cd "/Users/jimmy.lin/Documents/CEI-Literature-Vault"
PYTHONPATH="/Users/jimmy.lin/Documents/CEI-Literature-Vault" python3 \
  .agent/skills/extract_pdf_text/scripts/extract.py \
  --verbose --force "<paper-name-without-extension>"
```

---

## Common Issues and Solutions

### Issue 1: Paywall Restrictions
**Symptoms:** `curl` returns HTML instead of PDF, 403/401 errors
**Affected Sources:** PNAS, Science, Elsevier, Wiley, SSRN (some)
**Solution:**
- Mark `local_pdf: "PENDING - paywall restricted"` in frontmatter
- Add to `Paper log/` for manual download later
- Check alternative sources (PMC, ResearchGate, author pages, PsyArXiv)

### Issue 2: PYTHONPATH ModuleNotFoundError
**Symptoms:** `ModuleNotFoundError: No module named 'PYTHON'`
**Cause:** Script run from wrong directory or missing path
**Solution:** Always set PYTHONPATH explicitly:
```bash
PYTHONPATH="/Users/jimmy.lin/Documents/CEI-Literature-Vault" python3 script.py
```

### Issue 3: Duplicate Paper Detection
**Symptoms:** Write tool fails with "File already exists"
**Solution:** Always check with Glob before creating:
```bash
ls papers/*AuthorLastName*.md
```

### Issue 4: HTML Masquerading as PDF
**Symptoms:** PDF file exists but extraction fails
**Detection:**
```bash
file "PDFs/filename.pdf"  # Should say "PDF document"
head -c 100 "PDFs/filename.pdf"  # Should start with %PDF
```
**Solution:** Delete fake PDF and mark as PENDING

---

## Key Classification Fields for Ethics Papers

| Field | Values | Use When |
|-------|--------|----------|
| `ethics_overall` | Yes/No | Paper discusses AI ethics |
| `utilitarian_ethics` | Yes/No | Consequentialist framework used |
| `deontological_ethics` | Yes/No | Rule-based ethics discussed |
| `virtue_ethics` | Yes/No | Character-based ethics discussed |
| `moral_psychology` | Yes/N/A | Human moral cognition studied |
| `is_benchmark` | Yes/No | Creates evaluation benchmark |
| `is_eval` | Yes/No | Evaluates LLM moral reasoning |

---

## Papers Found This Session (11 Total)

### Successfully Downloaded (7 PDFs)
1. Jiao 2025 - LLM Ethics Benchmark Three-Dimensional Assessment (Nature Scientific Reports)
2. Serafimova 2020 - Whose Morality Which Rationality (Nature Humanities)
3. Tennant 2025 - Moral Alignment for LLM Agents (arXiv)
4. Ji 2024 - MoralBench Moral Evaluation of LLMs (arXiv/ACM SIGKDD)
5. Zhou 2024 - Rethinking Machine Ethics (NAACL Findings)
6. Sorin 2024 - Ethical Alignment of LLMs in Healthcare (medRxiv)
7. Mahajan 2025 - Mapping Moral Reasoning in LLMs (AIES)

### Pending Download (4 - Paywall)
1. Cheung 2025 - Large Language Models Show Amplified Cognitive Biases (PNAS)
2. Myers 2024 - People Expect Artificial Moral Advisors (Cognition)
3. McGee 2024 - How Ethical Is Utilitarian Ethics (SSRN/Business Ethics)
4. Zhang 2022 - Artificial Intelligence and Moral Dilemmas (JESP)

---

## Search Terms That Worked Well

**High-yield queries:**
- "LLM moral reasoning benchmark"
- "trolley problem artificial intelligence"
- "utilitarian deontological AI"
- "moral foundations theory LLM"
- "ethical alignment language model"

**Venues with relevant papers:**
- AIES (AAAI/ACM Conference on AI, Ethics, and Society)
- NAACL/ACL Findings
- Nature Scientific Reports / Humanities & Social Sciences
- arXiv cs.CL and cs.AI
- medRxiv (healthcare AI ethics)

---

## Future Session Recommendations

1. **Start with vault search** - Many relevant papers may already exist
2. **Use Glob before Write** - Prevent duplicate creation errors
3. **Verify PDFs immediately** - Catch paywall redirects early
4. **Set PYTHONPATH** - Required for extraction scripts
5. **Create Paper Log** - Track all findings including pending downloads
6. **Update SESSION_HISTORY.md** - Maintain audit trail of changes
7. **Update CLAUDE.md counts** - Keep statistics current

---

---

## Deontological/Deontic Ethics Search Strategy (Session 17)

### High-Yield Search Queries

```
# Kantian Ethics for AI
"Kantian ethics" AI alignment "categorical imperative"
"Kantian deontology" fairness metrics machine learning
"categorical imperative" LLM moral reasoning

# Deontic Logic
"deontic logic" AI machine ethics formal reasoning
"deontic temporal logic" verification AI ethics
"non-monotonic deontic logic" autonomous agents

# Duty-Based Ethics
"duty-based ethics" LLM alignment
"non-consequentialist" AI ethics moral reasoning
"moral obligations" LLM reasoning deontology
"rule-based ethics" artificial intelligence alignment

# Cross-Framework Comparison
"consequentialist deontological" LLM moral reasoning
"utilitarian Kantian" AI ethics comparison
```

### Key Venues for Deontological Ethics Papers

| Venue | Type | Access | Notes |
|-------|------|--------|-------|
| **Philosophical Studies** | Journal | Often paywalled | Top philosophy journal |
| **AI and Ethics** | Journal | Springer (mixed) | Dedicated AI ethics |
| **Ethics and Information Technology** | Journal | Often paywalled | Springer |
| **AIES** (AAAI/ACM) | Conference | Open access | Best for formal ethics |
| **FAccT** | Conference | Open access | Fairness + accountability |
| **PhilArchive** | Preprint | Open access | Philosophy preprints |
| **PhilPapers** | Archive | PDF varies | Links to sources |
| **CMU KiltHub** | Repository | Open access | CMU research outputs |

### PDF Access Patterns for Philosophy Papers

| Source | URL Pattern | Success Rate |
|--------|-------------|--------------|
| **PhilArchive** | `philarchive.org/archive/XXXXX` | 85% |
| **PhilPapers** | `philpapers.org/archive/XXXXX.pdf` | 70% |
| **CMU Faculty** | `*.tepper.cmu.edu/*.pdf` | 90% |
| **AAAI/AIES** | `ojs.aaai.org/index.php/AIES/article/download/*` | 95% |
| **Springer OA** | `link.springer.com/content/pdf/DOI.pdf` | 50% (if OA) |

### Authors to Track for Deontological AI Ethics

| Author | Affiliation | Focus |
|--------|-------------|-------|
| John Hooker | CMU | Modal logic for machine ethics |
| Tae Wan Kim | CMU | Kantian machine ethics |
| William D'Alessandro | Oxford | Deontology and AI safety |
| Ava Thomas Wright | - | Deontic logic for rightful machines |
| Marija Slavkovik | Bergen | Machine ethics, deontic logic |

### Key Concepts to Search

- **Categorical Imperative** - Kant's universal law formulation
- **Deontic Logic** - Logic of obligations, permissions, prohibitions
- **Non-monotonic reasoning** - Handling conflicting rules
- **Practical wisdom (phronesis)** - Aristotelian context-sensitivity
- **Moral agency** - Whether AI can be moral agents
- **Formal verification** - Proving ethical properties

---

## Consequentialist/Utilitarian Ethics Search Strategy (Session 19)

### High-Yield Search Queries

```
# Core Consequentialist Ethics for AI
"consequentialist ethics" AI "values alignment" LLM 2024 2025
"utilitarian moral reasoning" "large language models" artificial intelligence
"normative ethics" "machine ethics" AI alignment consequentialism
"expected utility maximization" AI safety alignment

# RLHF and Value Learning
"RLHF" "reinforcement learning human feedback" utilitarian ethics alignment
"reward modeling" consequentialism AI ethics
"preference learning" AI alignment utilitarianism

# Computational Ethics
"computational ethics" consequentialism AI "moral decision making"
"moral uncertainty" AI alignment consequentialism

# Cross-Framework Comparison
"utilitarian deontological" LLM moral reasoning comparison
"consequentialist virtue ethics" AI alignment
```

### Key Papers Found (Session 19)

| Paper | Focus | PDF Source | Notes |
|-------|-------|------------|-------|
| Zhi-Xuan - Beyond Preferences | Expected utility critique | arXiv | MIT/Berkeley collaboration |
| Stenseke - Computational Complexity | Tractability of ethics | arXiv | All normative theories analyzed |
| Chaudhari - RLHF Deciphered | RLHF critical analysis | arXiv | ACM Computing Surveys |
| Barman - RLHF Values | Epistemic pluralism | arXiv | Philosophy & Technology |
| Kneer - Value Forks | AI/human different ethics | PhilArchive | ACM FAccT empirical study |
| Vishwanath - Machine Ethics vs Alignment | AI is utilitarian by design | CEUR-WS | NAIS conference |
| Benavoli - AI Safety Uncertainty | Non-Archimedean utilities | arXiv | Safety-focused |

### Authors to Track for Consequentialist AI Ethics

| Author | Affiliation | Focus |
|--------|-------------|-------|
| Tan Zhi-Xuan | MIT | Preference learning, value alignment |
| Jakob Stenseke | Lund University | Computational complexity of ethics |
| Kristian Gonzalez Barman | Ghent University | RLHF pluralism |
| Markus Kneer | Zurich | Experimental philosophy, AI ethics |
| Marija Slavkovik | Bergen | Machine ethics (appears in multiple papers) |
| Paula Boddington | Oxford/London | Normative ethics for AI |

### PDF Access Patterns for Ethics Papers

| Source | Success Rate | Notes |
|--------|--------------|-------|
| **arXiv** | 95% | Best source for preprints |
| **PhilArchive** | 85% | Philosophy papers |
| **AAAI/AIES** | 90% | Conference proceedings |
| **MDPI** | 80% | Often open access |
| **Nature Scientific Reports** | 80% | Often open access |
| **Springer books** | 20% | Usually paywalled |
| **IOS Press** | 20% | Usually paywalled |
| **ScienceDirect** | 30% | Usually paywalled |

### Key Insights from Session 19

1. **AI is inherently utilitarian**: Multiple papers argue AI systems are utilitarian by design due to optimization objectives (Vishwanath, Della Foresta)

2. **Expected utility insufficient**: Strong arguments that standard utility theory is inadequate for alignment (Zhi-Xuan, Benavoli)

3. **Computational complexity matters**: Stenseke's analysis shows all normative frameworks face tractability issues when implemented computationally

4. **RLHF value encoding unclear**: Papers by Barman and Chaudhari question whose values are encoded in RLHF

5. **Value forks exist**: Kneer's empirical study (N=1029) shows people expect AI to behave differently than humans in moral dilemmas

---

## Related Documentation

- [SESSION_HISTORY.md](SESSION_HISTORY.md) - Full session records
- [PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) - PDF download strategies
- [WORKFLOWS.md](WORKFLOWS.md) - Standard vault workflows
- [YAML_SAFEGUARDS.md](../YAML_SAFEGUARDS.md) - Safe YAML editing practices
