# Competitive Analysis — Council of Seven Experts

**Date:** 2026-03-15
**Prepared by:** Council of 7 virtual domain experts
**Subject:** CEI Literature Vault (CEI-Lit-WS) — Competitive Positioning in the AI Ethics Literature Landscape
**Status:** Strategic analysis — for internal planning

---

## 1. Executive Summary

The CEI Literature Vault (CEI-Lit-WS) is a specialized academic literature database containing **2,043 papers** on AI ethics, housed in an Obsidian-based knowledge management system. It combines bibliographic metadata imported from Zotero with a **7-stage automated classification pipeline** that scores every paper across **27+ ethical, philosophical, and cultural dimensions** — including 5 normative ethics frameworks, 8 moral psychology theories, and 14 religious traditions — each rated on a 0–100 confidence scale.

**Core Finding:** CEI-Lit-WS occupies a unique and currently uncontested niche in the competitive landscape. No existing database — from mega-scale platforms like OpenAlex (271M+ works) to curated bibliographies like PhilPapers — combines medium-scale paper collection with deep multi-dimensional ethical classification. The vault's closest competitors either offer massive scale with shallow metadata (Tier 1 databases) or deep curation at tiny scale (Tier 6 research datasets).

### Top 3 Strengths

1. **Unmatched classification depth.** 27+ scored dimensions per paper (normative ethics, moral psychology, religious traditions, cultural values, data nature) — no competitor offers even 5 comparable classification axes.
2. **Full-text infrastructure.** 92% PDF collection rate (1,886/2,043), ~2,487 structured text extracts enabling keyword-based scoring beyond abstract-only analysis.
3. **Integrated analytical dashboards.** 21 dashboard versions with 40+ chart types across 11 analytical tabs — purpose-built for exploring the ethical dimensions of AI research.

### Top 3 Gaps

1. **No PRISMA-style methodology.** No documented inclusion/exclusion criteria, search strategy, or reproducibility protocol — a critical weakness for academic credibility.
2. **Non-standard metadata.** Obsidian YAML frontmatter is not interoperable with Dublin Core, MARC, RDF, or any library standard. No ORCID, no ROR, no persistent identifiers beyond Zotero keys.
3. **Bus factor of 1.** Single-maintainer project with no preservation plan, no community governance, and no institutional backing.

---

## 2. The Council — Expert Profiles

### Expert 1: Systematic Review Methodologist

| Attribute | Detail |
|-----------|--------|
| **Lens** | PRISMA compliance, reproducibility, inclusion/exclusion rigor |
| **Key Question** | "Could a researcher replicate this collection?" |
| **One-Sentence Verdict** | The vault has impressive scale and classification depth, but without a documented search protocol, it cannot be cited as a systematic review — it's a curated bibliography with unusually rich annotations. |

### Expert 2: Library & Information Scientist

| Attribute | Detail |
|-----------|--------|
| **Lens** | Metadata standards, findability, interoperability |
| **Key Question** | "Can this data interoperate with institutional infrastructure?" |
| **One-Sentence Verdict** | The 50+ YAML fields represent a genuinely novel metadata schema for AI ethics, but the complete absence of standard identifiers (ORCID, ROR, Dublin Core, MARC) makes institutional integration nearly impossible without a translation layer. |

### Expert 3: AI Ethics Scholar

| Attribute | Detail |
|-----------|--------|
| **Lens** | Domain coverage, philosophical depth, normative framework representation |
| **Key Question** | "Does this capture the field's intellectual breadth?" |
| **One-Sentence Verdict** | The five-framework normative classification (virtue, deontological, utilitarian, care, contractarian) plus 10 ethics perspectives is the most granular philosophical tagging I've seen in any AI ethics bibliography — the field needs this. |

### Expert 4: Moral Psychologist

| Attribute | Detail |
|-----------|--------|
| **Lens** | Behavioral science representation, empirical grounding |
| **Key Question** | "Are the moral psychology theories adequately represented?" |
| **One-Sentence Verdict** | Tracking 8 distinct moral psychology theories (MFT, Schwartz, Trolley, Kohlberg, Dual Process, Intuitionist, Dyadic, Identity) with confidence scores is unprecedented in bibliometric tools — the coverage is comprehensive for the field's major schools. |

### Expert 5: Comparative Religion & Culture Scholar

| Attribute | Detail |
|-----------|--------|
| **Lens** | Cross-cultural coverage, tradition fidelity, Western bias |
| **Key Question** | "Does this avoid tokenistic representation of non-Western traditions?" |
| **One-Sentence Verdict** | Scoring 14 religious traditions individually — including Shinto, Jainism, Baha'i, Zoroastrianism, Ubuntu, and Indigenous — goes far beyond the Christian/Islamic binary that typifies Western AI ethics discourse, though keyword-based detection has inherent limits for traditions with less English-language presence. |

### Expert 6: Bibliometrician / Data Scientist

| Attribute | Detail |
|-----------|--------|
| **Lens** | Analytics depth, citation networks, quantitative rigor |
| **Key Question** | "How do the analytics compare to established bibliometric tools?" |
| **One-Sentence Verdict** | The dashboard infrastructure (21 versions, 40+ chart types) rivals commercial tools for its specific domain, but the complete absence of citation data — available freely from OpenAlex and Semantic Scholar — is a glaring gap that limits bibliometric analysis. |

### Expert 7: Digital Humanities & Infrastructure Scholar

| Attribute | Detail |
|-----------|--------|
| **Lens** | Sustainability, architecture, open access, longevity |
| **Key Question** | "Will this outlast its creator?" |
| **One-Sentence Verdict** | The Markdown-based architecture (plain text + YAML) is inherently durable, but without institutional hosting, a DOI, a preservation partner, or community governance, this is a personal research tool at risk of abandonment. |

---

## 3. Competitor Inventory

### Tier 1 — General Mega-Databases

These platforms index tens to hundreds of millions of scholarly works across all disciplines. They are not competitors in classification depth — they are competitors in discoverability and reach.

| Database | Scale | Access | API | Classification Depth | AI Ethics Coverage |
|----------|-------|--------|-----|---------------------|-------------------|
| **OpenAlex** | 271M+ works | Open | Yes (free) | Topics (L0–L3 hierarchy, ~65K topics) | Broad; no ethics-specific taxonomy |
| **Semantic Scholar** | 220M+ papers | Open | Yes (free, rate-limited) | TLDR summaries, citation intents, influence scores | AI safety/alignment clusters identified |
| **Scopus** | 80M+ records | Subscription | Yes (paid) | ASJC subject areas (~330 codes) | Limited to "Ethics" ASJC code |
| **Web of Science** | 180M+ records | Subscription | Yes (paid) | WoS Categories (~250) | "Ethics" category; no sub-classification |
| **Google Scholar** | Unknown (largest) | Free | No official API | None | None — search only |
| **Dimensions.ai** | 140M+ publications | Freemium | Yes (paid) | Fields of Research (ANZSRC), SDGs | SDG mapping touches ethics tangentially |
| **Lens.org** | 260M+ records | Freemium | Yes (free tier) | Patent + scholarly linkage | Patent-to-paper ethics mapping possible |

### Tier 2 — Conference Proceedings & Domain Databases

| Database | Scale | Access | API | Classification Depth | Differentiator |
|----------|-------|--------|-----|---------------------|---------------|
| **AIES** (AAAI/ACM) | ~500–600 papers | Open (proceedings) | Via ACM DL API | Conference tracks only | Premier AI ethics venue |
| **FAccT** (ACM) | ~500–700 papers | Open (proceedings) | Via ACM DL API | Conference tracks + themes | Fairness/accountability focus |
| **ACM Digital Library** | 3M+ articles | Subscription | Yes | ACM CCS classification | Broad CS coverage |
| **IEEE Xplore** | 6M+ articles | Subscription | Yes | IEEE thesaurus | Engineering-focused |

### Tier 3 — Curated Bibliographies

| Database | Scale | Access | API | Classification Depth | Differentiator |
|----------|-------|--------|-----|---------------------|---------------|
| **PhilPapers** | ~1–3K AI ethics entries (2.7M total) | Open | Limited | Philosophical taxonomy (~5,800 categories) | Philosophy-centric; deep in normative theory |
| **U of Toronto Annotated Bib** | ~800–900 entries | Open | No | Thematic annotations | Hand-annotated by librarians |
| **AlgorithmWatch** | 160+ entries | Open | No | Policy/governance tags | European focus; journalistic |
| **Worldwide AI Ethics** | 200+ entries | Open | No | Topical categories | Broad but shallow |

### Tier 4 — Risk & Incident Databases

| Database | Scale | Focus | Classification | Differentiator |
|----------|-------|-------|---------------|---------------|
| **MIT AI Risk Repository** | 1,600+ risks | AI risks (not papers) | 2-axis risk taxonomy (cause + domain) | Risk decomposition, not literature |
| **AI Incident Database** (AIID) | 962+ incidents | Real-world AI failures | Incident type, severity, sector | Incident tracking, not academic |

### Tier 5 — Discovery & Aggregation Tools

| Tool | Function | Scale | Classification | Differentiator |
|------|----------|-------|---------------|---------------|
| **Connected Papers** | Citation graph visualization | Per-query | None (uses S2 data) | Visual exploration, not database |
| **MAIEI** (Montreal AI Ethics) | Newsletter + research digest | 100s of digests | Topical curation | Community engagement, not DB |

### Tier 6 — Published Research Datasets

| Dataset | Scale | Focus | Classification | Citation |
|---------|-------|-------|---------------|---------|
| **Responsible AI Measures** | 257 papers | RAI measurement | 6 ethical dimensions, metrics taxonomy | Nature, 2025 |
| **Jobin et al. 2019** | 84 documents | AI ethics guidelines | 11 ethical principles | Nature Machine Intelligence |
| **Fjeld et al. 2020** | 36 documents | Principled AI | 8 key themes, 47 sub-themes | Berkman Klein |
| **Hagendorff 2020** | 22 documents | AI ethics guidelines | 21 ethical issues | Minds & Machines |

---

## 4. The Comparison Matrix

### 4.1 Scale & Coverage (Bibliometrician Lens)

| Database | Total Scale | AI Ethics Papers | Year Range | Geographic Scope | Language Coverage |
|----------|------------|-----------------|------------|-----------------|------------------|
| OpenAlex | 271M+ | Est. 15–30K | All years | Global | Multilingual |
| Semantic Scholar | 220M+ | Est. 10–25K | All years | Global | Multilingual |
| Scopus | 80M+ | Est. 8–15K | 1788– | Global | English-dominant |
| Web of Science | 180M+ | Est. 5–12K | 1900– | Global | English-dominant |
| Google Scholar | Unknown | Unknown | All years | Global | Multilingual |
| AIES | ~500–600 | ~500–600 | 2018– | Global | English |
| FAccT | ~500–700 | ~500–700 | 2018– | Global | English |
| PhilPapers | 2.7M | ~1–3K | All years | Global | English-dominant |
| MIT AI Risk Repo | 1,600 risks | N/A (risks) | 2024– | Global | English |
| AIID | 962 incidents | N/A (incidents) | 2011– | Global | English |
| Jobin 2019 | 84 docs | 84 | Pre-2019 | Global | Multilingual |
| Fjeld 2020 | 36 docs | 36 | Pre-2020 | Global | English |
| Responsible AI | 257 papers | 257 | Pre-2025 | Global | English |
| **CEI-Lit-WS** | **2,043** | **2,043** | **~2012–2026** | **Global** | **English-dominant** |

**Analysis:** CEI-Lit-WS sits in the middle tier by scale — 3–10x larger than curated bibliographies (Tier 3/6) but 100–10,000x smaller than mega-databases (Tier 1). Its value proposition is not scale but classification density per paper.

### 4.2 Classification Depth (AI Ethics Scholar + Moral Psychologist Lenses)

| Database | Ethics Binary | Normative Frameworks | Ethics Perspectives | Moral Psychology | Religious Traditions | Cultural Values | Data Nature | Total Dims |
|----------|--------------|---------------------|--------------------|-----------------|--------------------|----------------|-------------|-----------|
| OpenAlex | — | — | — | — | — | — | — | ~3 (topics) |
| Semantic Scholar | — | — | — | — | — | — | — | ~2 (TLDR, influence) |
| Scopus | — | — | — | — | — | — | — | ~1 (ASJC) |
| PhilPapers | ✓ | ✓ (via taxonomy) | Partial | — | — | — | — | ~5–8 |
| AIES/FAccT | — | — | Track labels | — | — | — | — | ~3–5 |
| MIT AI Risk Repo | — | — | Risk taxonomy | — | — | — | — | ~2 (cause × domain) |
| Jobin 2019 | — | — | 11 principles | — | — | — | — | ~11 |
| Fjeld 2020 | — | — | 8 themes, 47 subs | — | — | — | — | ~47 |
| Resp. AI Measures | — | — | 6 dimensions | — | — | — | Metrics | ~7 |
| **CEI-Lit-WS** | **✓ (0–100)** | **5 (0–100 each)** | **10 categories** | **8 (0–100 each)** | **14 (0–100 each)** | **20+ cultures** | **3 binary + desc** | **~50+** |

**Analysis:** CEI-Lit-WS provides **5–25x more classification dimensions** than the next most detailed competitor (Fjeld 2020 at ~47 sub-themes, PhilPapers at ~5–8). Critically, CEI-Lit-WS uses **continuous confidence scores** (0–100) rather than binary labels, enabling threshold-based analysis.

### 4.3 Metadata Richness (Library & Information Scientist Lens)

| Database | Standard IDs | Author IDs | Venue Norm. | Citation Data | Full-Text | Structured Extracts | Export Formats |
|----------|-------------|-----------|------------|--------------|-----------|--------------------|--------------|
| OpenAlex | DOI, PMID, MAG | ORCID, S2 | Yes | Yes (OA) | No | No | JSON, CSV, API |
| Semantic Scholar | DOI, arXiv, PMID | S2 Author ID | Yes | Yes | No | TLDR | JSON, API |
| Scopus | DOI, EID, PMID | Scopus Author ID | Yes | Yes | No | Abstracts | XML, CSV, RIS |
| Web of Science | DOI, UT, PMID | ResearcherID | Yes | Yes | No | Abstracts | Tab, BibTeX, RIS |
| PhilPapers | DOI (partial) | PhilPapers profiles | Yes | No | No | No | BibTeX |
| AIES/FAccT | DOI | ACM profiles | Yes | Via ACM | Some | No | BibTeX |
| Jobin 2019 | — | — | — | — | — | — | Supplementary table |
| **CEI-Lit-WS** | **DOI, arXiv (partial)** | **Wikilink profiles** | **Partial** | **No** | **92% PDFs** | **~2,487 extracts** | **YAML/Markdown** |

**Analysis:** CEI-Lit-WS has a unique strength in full-text infrastructure (92% PDF collection + structured extracts) but a critical weakness in standard identifiers. The Obsidian wikilink system (`"[[Author Name]]"`) is not interoperable with ORCID, Scopus Author IDs, or any institutional system.

### 4.4 Analytics & Visualization (Bibliometrician Lens)

| Database | Dashboards | Chart Types | Citation Analysis | Co-authorship | Trend Analysis | Custom Views |
|----------|-----------|------------|------------------|--------------|---------------|-------------|
| OpenAlex | Via Kibana/custom | Basic via API | Yes (full) | Yes | Yes | API-powered |
| Semantic Scholar | Author pages | Influence graphs | Yes (full) | No | Research trends | Limited |
| Scopus | SciVal integration | 20+ | Yes (full) | Yes | Yes | SciVal |
| Web of Science | InCites integration | 20+ | Yes (full) | Yes | Yes | InCites |
| VOSviewer (tool) | Network viz | Bibliometric maps | Yes | Yes | Yes | Full |
| PhilPapers | Category browsers | None | No | No | No | Search only |
| Jobin 2019 | Static figures | ~5 | No | No | Limited | No |
| **CEI-Lit-WS** | **21 versions** | **40+ types** | **No** | **No** | **Yes** | **11 tabs** |

**Dashboard Tab Inventory (v13):**

| Tab | Content |
|-----|---------|
| Overview | High-level stats, distribution charts, key metrics |
| Normative Ethics | 6 subtabs: per-framework analysis, co-occurrence, trends |
| Moral Psychology | 5 subtabs, 13 analytics including theory co-occurrence |
| Religious Values | 11 subtabs: individual tradition analysis per tradition |
| Countries & Languages | Co-occurrence matrix, culture timelines, benchmark gaps |
| AI Labs | 14 lab profiles, 350+ papers, model-level tracking |
| Ethics Perspectives | 10-category breakdown with temporal trends |
| Benchmarks & Datasets | Data nature classification analytics |
| Cultural–Ethics (CE) | Dedicated subtab |
| Cross-Origin (CO) | Dedicated subtab |
| Principlism | Dedicated subtab |

**Analysis:** CEI-Lit-WS's dashboard infrastructure is remarkably developed for a single-maintainer project. The 21 iterative versions represent genuine analytical evolution, not cosmetic changes. However, the absence of citation network analysis — available for free from OpenAlex and Semantic Scholar — is a significant gap that limits bibliometric utility.

### 4.5 Reproducibility & Standards (Methodologist Lens)

| Database | Search Protocol | Inclusion Criteria | PRISMA | Version Control | Validation | Methodology Paper |
|----------|----------------|-------------------|--------|----------------|-----------|------------------|
| OpenAlex | N/A (comprehensive) | Coverage-based | N/A | API versioning | Community audits | Priem et al. 2022 |
| Semantic Scholar | N/A (comprehensive) | Coverage-based | N/A | API versioning | Quality metrics | Lo et al. 2020 |
| Jobin 2019 | Documented | Documented | Yes | Supplementary | Manual review | Published |
| Fjeld 2020 | Documented | Documented | Partial | Supplementary | Expert review | Published |
| Resp. AI Measures | Documented | Documented | Yes | GitHub | Inter-rater | Nature, 2025 |
| **CEI-Lit-WS** | **Not documented** | **Not documented** | **No** | **Git tracked** | **Automated (500+ tests)** | **No** |

**Analysis:** This is CEI-Lit-WS's most significant competitive weakness. The vault has robust technical validation (500+ unit tests, automated YAML validation, enhanced paper validation) but no systematic review methodology documentation. A researcher cannot answer: "What databases were searched? What date ranges? What inclusion/exclusion criteria? How were papers selected?"

### 4.6 Infrastructure & Sustainability (Digital Humanities Scholar Lens)

| Database | Hosting | Preservation | Governance | License | Community | Longevity Risk |
|----------|---------|-------------|-----------|---------|-----------|---------------|
| OpenAlex | OurResearch (nonprofit) | AWS infrastructure | Board + community | CC0 | Active | Low |
| Semantic Scholar | AI2 (nonprofit) | Institutional | AI2 team | Open API | Active | Low |
| Scopus | Elsevier (commercial) | Corporate | Corporate | Proprietary | Passive | Low |
| Web of Science | Clarivate (commercial) | Corporate | Corporate | Proprietary | Passive | Low |
| PhilPapers | APA/academic | University hosting | Editorial board | Open access | Moderate | Low–Medium |
| AIID | Partnership on AI | Cloud hosting | Community | CC BY-SA | Active | Low–Medium |
| MIT AI Risk Repo | MIT (academic) | University hosting | Research team | Open | Research | Medium |
| **CEI-Lit-WS** | **Local + GitHub** | **None formal** | **Single maintainer** | **Not specified** | **None** | **High** |

**Analysis:** CEI-Lit-WS's architecture (Markdown + YAML + Git) is inherently durable — the data can be read with any text editor in 50 years. But without institutional hosting, a DOI, a preservation partner (Zenodo, Internet Archive), or even a stated license, the project is at high risk of disappearing if the maintainer moves on.

---

## 5. Expert Assessments

### 5.1 Expert 1: Systematic Review Methodologist

#### Strengths

1. **Impressive scale for a curated collection.** At 2,043 papers, CEI-Lit-WS is 3–10x larger than any published curated AI ethics bibliography (Jobin: 84, Fjeld: 36, Resp. AI Measures: 257, Toronto: ~800). This isn't a reading list — it's a research infrastructure.

2. **Automated, reproducible classification.** The 7-stage pipeline with 500+ unit tests means classification is deterministic and repeatable. Unlike Fjeld 2020 (expert-coded) or Jobin 2019 (manual tagging), re-running the pipeline on the same corpus produces identical results. This is a significant methodological advantage.

3. **Continuous confidence scoring.** The migration from binary Yes/No to 0–100 scores is methodologically sophisticated. It acknowledges that "Is this paper about ethics?" is not a binary question — it's a spectrum. The 42 user-reviewed pins for ethics scoring show human-in-the-loop calibration.

4. **Full-text analysis.** Scoring from structured extracts (~2,487 files, 25K char truncation) rather than abstracts alone provides much richer signal. Most bibliographic tools work on titles and abstracts only.

#### Weaknesses

1. **No search protocol.** This is the single most damaging gap. A systematic review requires: (a) databases searched, (b) search strings used, (c) date ranges, (d) inclusion/exclusion criteria, (e) PRISMA flow diagram. CEI-Lit-WS has none of these documented. The collection appears to originate from a Zotero library, but the selection methodology is opaque.

2. **No inter-rater reliability.** The keyword-based classification pipeline has 500+ unit tests, but no inter-rater agreement metrics (Cohen's kappa, Krippendorff's alpha). How well do the automated classifications agree with expert human judgment? The 1,097 disagreements noted for ethics scoring (after migration to 0–100) suggest significant divergence from prior classifications, but the resolution process isn't documented as a formal reliability study.

3. **No sampling frame.** What is the denominator? How many AI ethics papers exist in the literature? Without this, we can't assess coverage. Is 2,043 papers 20% of the field or 2%?

4. **No stated update cadence.** Systematic reviews require periodic updates. CEI-Lit-WS appears to be updated continuously, which is good for currency but makes it hard to cite a stable version.

#### Competitive Position

CEI-Lit-WS cannot currently be cited as a systematic review. It is best described as a **curated, annotated bibliography with automated multi-dimensional classification** — a novel contribution that sits between traditional bibliographies and systematic reviews. Adding PRISMA documentation would elevate it significantly.

#### Recommendations

1. **Write a retrospective PRISMA-style methodology document.** Even if the original collection wasn't PRISMA-compliant, documenting the actual process (Zotero collection → classification pipeline → enrichment) adds credibility.
2. **Compute inter-rater reliability** for at least 200 papers across key dimensions (ethics_overall, normative frameworks, moral psychology). Use the 42 user-reviewed pins as seed data.
3. **Define the target population.** Use OpenAlex/Semantic Scholar topic queries to estimate the total number of AI ethics papers published (likely 10K–30K), and state CEI-Lit-WS's coverage percentage.
4. **Create versioned snapshots.** Tag Git releases (v1.0, v2.0) so researchers can cite a stable point in time.

---

### 5.2 Expert 2: Library & Information Scientist

#### Strengths

1. **Exceptionally rich metadata schema.** With 50+ YAML fields per paper, CEI-Lit-WS captures more structured information per record than any database I've evaluated. The fields span bibliographic (Zotero-origin), classification (7-stage pipeline), enrichment (key_contribution, significance, paper_summary), and file linking (local_pdf, pdf_extract) — a comprehensive information architecture.

2. **Author authority files.** 11,439 author profiles with wikilink cross-referencing function as a local name authority — analogous to VIAF or LCNAF at small scale. This is unusual and valuable for disambiguation.

3. **Structured vocabulary control.** The classification fields use controlled vocabularies: 10 ethics perspectives, 7 research topics, 14 religious traditions, 8 moral psychology theories, 20+ cultural categories. This is genuine vocabulary control, not free-text tagging.

4. **Full-text linking.** The `local_pdf` and `pdf_extract` fields create a three-layer information architecture: metadata → full text → structured extract. This is more integrated than most institutional repositories.

#### Weaknesses

1. **No standard metadata format.** The YAML frontmatter schema is entirely custom. No Dublin Core, no MARC, no MODS, no DataCite. An institutional repository, library catalog, or data aggregator cannot ingest these records without a custom parser.

2. **No persistent identifiers.** No ORCID for authors. No ROR for institutions. No ISNI. The Zotero `key` field is a local identifier, not a PID. DOIs are optional (not required), and arXiv IDs are extracted but not normalized.

3. **No linked data.** The wikilink system (`"[[Dario Amodei]]"`) is Obsidian-specific. It cannot be dereferenced outside the vault. A JSON-LD or RDF representation would enable SPARQL queries and integration with the Linked Open Data ecosystem.

4. **No export pipeline.** The data is locked in Markdown/YAML. There's no BibTeX export, no CSV export, no API. A researcher who wants to use CEI-Lit-WS data in R, Python, or Excel must write their own parser.

5. **Non-standard field names.** `ethics_overall`, `mp_mft`, `rv_islam` — these are meaningful within the vault but opaque to outsiders. No alignment with ANZSRC Fields of Research, Library of Congress Subject Headings, or any external thesaurus.

#### Competitive Position

CEI-Lit-WS is a highly original metadata schema that has no direct analog in library science. It is more akin to a **domain-specific research database** (like PhilPapers or the Protein Data Bank) than a traditional bibliography. Its value is in the classification layer, not in bibliographic standards compliance.

#### Recommendations

1. **Add ORCID identifiers** for authors where available. The existing 11,439 author profiles could be enriched via the ORCID public API.
2. **Create a Dublin Core crosswalk.** Map the core Zotero fields (title, author, year, DOI, type) to DC elements. This enables basic interoperability without changing the vault.
3. **Build a JSON-LD export.** Represent each paper as a schema.org `ScholarlyArticle` with custom extensions for the classification fields. This is the minimum viable linked data.
4. **Publish a data dictionary.** The `paper-metadata-schema.md` is a good start — formalize it as a citable standard with a DOI.
5. **Add BibTeX/CSV export scripts.** Even simple CSV export of key fields would dramatically increase accessibility.

---

### 5.3 Expert 3: AI Ethics Scholar

#### Strengths

1. **Five normative frameworks with continuous scoring.** Virtue ethics, deontological ethics, utilitarian ethics, care ethics, and contractarian ethics — each scored 0–100. This is the most granular normative classification I've seen in any AI ethics database. PhilPapers has a rich philosophical taxonomy, but it doesn't score papers against specific frameworks. Jobin 2019 identified 11 principles (transparency, justice, etc.) but didn't map to meta-ethical traditions.

2. **Ten ethics perspectives beyond frameworks.** AI Safety & Alignment, Bias & Fairness, Toxicity & Hate Speech, Moral Reasoning & Psychology, Truthfulness & Factuality, Privacy & Surveillance, Human Rights & Social Justice, Responsible AI, Machine Ethics, Value Alignment — this captures the applied ethics landscape comprehensively.

3. **Cross-cutting cultural and religious dimensions.** Most AI ethics databases treat ethics as a universal, Western-secular discourse. CEI-Lit-WS's 14 religious tradition scores + 20+ cultural categories explicitly acknowledge that ethical reasoning in AI is culturally situated. This is philosophically important and practically rare.

4. **Data nature classification.** Tracking which papers introduce benchmarks, evaluations, or datasets (and extracting data_metrics) addresses a real need — researchers constantly ask "what benchmarks exist for evaluating AI ethics?"

5. **AI lab tracking.** 14 labs with 350+ papers and model-level documentation provides unique insight into how specific organizations' research relates to ethical concerns.

#### Weaknesses

1. **Western-canon normative bias.** The five frameworks (virtue, deontological, utilitarian, care, contractarian) are all from the Western philosophical tradition. Where is Confucian role ethics? Ubuntu ethics? Buddhist ethics? Islamic jurisprudence (usul al-fiqh)? The religious_values scores partially address this, but religious tradition ≠ normative ethical framework. A Confucian approach to AI alignment is a normative ethics position, not merely a "religious value."

2. **Keyword-based classification ceiling.** The scoring formula (`strong_matches × 15 + medium_matches × 5 - fp_context × 10 + title_bonus(20)`) is transparent and reproducible, but it has inherent limits. A paper that discusses Kantian ethics without ever using the word "Kant," "duty," or "deontological" — perhaps framing it as "rule-based moral reasoning" — will score 0 on deontological_ethics. This is a recall problem.

3. **Limited philosophical nuance.** The system can detect *that* a paper discusses virtue ethics but not *which version* (Aristotelian? MacIntyrean? Feminist?). Similarly, "utilitarianism" encompasses act, rule, preference, and negative utilitarianism — the scoring doesn't distinguish these.

4. **Scale gap.** At ~2,043 papers, CEI-Lit-WS likely captures 10–20% of the AI ethics literature. The field has grown exponentially since 2018; a query on OpenAlex for "AI ethics" returns 15K+ results. Significant work in non-English languages, regional conferences, and non-CS venues is likely missing.

5. **No citation impact integration.** A paper's influence on the field cannot be assessed without citation data. The most-cited AI ethics papers (Bender et al. 2021, Gebru et al. 2021, Floridi et al. 2018) may or may not be in the vault, but their citation networks are not represented.

#### Competitive Position

CEI-Lit-WS is the only database that answers questions like: "How many AI ethics papers engage with care ethics *and* Moral Foundations Theory?" or "Which papers discuss Islamic perspectives on AI benchmarking?" No mega-database can answer these questions without extensive manual annotation. This is a genuine, defensible niche.

#### Recommendations

1. **Add non-Western normative frameworks** as classification dimensions: Confucian role ethics, Ubuntu communalism, Buddhist ethics, Islamic usul al-fiqh, Indigenous relational ethics. These could start as 0–100 scores analogous to rv_* fields.
2. **Implement semantic similarity scoring** using sentence embeddings (e.g., from Semantic Scholar's SPECTER) to catch papers that discuss frameworks without using canonical keywords.
3. **Scale to 5K+ papers** with a focused expansion targeting: (a) non-English publications, (b) regional conferences (AACL, AfricaNLP), (c) law and policy journals, (d) philosophy journals beyond PhilPapers top hits.
4. **Add citation data from OpenAlex** (free, CC0) to enable citation-aware analytics.
5. **Publish the classification schema** as a citable contribution to AI ethics methodology.

---

### 5.4 Expert 4: Moral Psychologist

#### Strengths

1. **Eight moral psychology theories tracked.** MFT, Schwartz Value Survey, Trolley/Dilemmas, Kohlberg, Dual Process (Greene), Social Intuitionist, Dyadic Morality (Gray), and Moral Identity — this covers the major schools comprehensively. I'm not aware of any other AI ethics database that tracks moral psychology theories at all, let alone eight of them.

2. **Continuous confidence scoring.** The 0–100 scale with strong-floor guarantee (any strong match → minimum 50) is well-designed. It captures the difference between a paper that mentions "moral foundations" once in passing (score: 5–15) and one that is centrally about MFT (score: 72+).

3. **False-positive handling.** The explicit FP deductions for generic terms ("achievement," "power," "security," "agent," "identity," "system") show sophisticated awareness of the vocabulary overlap between moral psychology and general CS terminology. This is a real problem — "dual process" means something entirely different in operating systems than in moral psychology.

4. **154 papers detected.** The moral psychology detection (as of dashboard v12) identified 154 papers across the 8 theories. This represents roughly 7.5% of the vault — a plausible base rate for moral psychology content in an AI ethics collection.

#### Weaknesses

1. **Missing recent theories.** The 8 theories are well-established but don't include: (a) Moral Foundations Theory's extensions (additional foundations: liberty/oppression, efficiency/waste), (b) Moral Disengagement (Bandura), (c) Moral Licensing, (d) Moral Injury, (e) Ethical Fading (Bazerman). These are active in the AI ethics literature (e.g., "moral disengagement in autonomous weapons" papers).

2. **No empirical method classification.** Moral psychology papers vary widely in methodology: self-report surveys (SVS, MFQ), behavioral experiments (trolley paradigms), neuroimaging (Greene's fMRI work), computational modeling, text analysis. The vault doesn't classify methodology, which limits its utility for psychologists looking for specific study types.

3. **Keyword precision limits.** The term "moral intuition" could refer to Haidt's Social Intuitionist Model or to a philosopher's use of "intuition" in reflective equilibrium. The negative lookbehind fix (`(?<!moral )`) for "moral intuition" vs. other uses of "intuition" is a good example of the precision challenges inherent in keyword matching.

4. **No effect size or sample data.** For empirical moral psychology papers, key metadata includes sample size, country of participants, effect sizes, and instruments used. These are not captured in the current schema.

#### Competitive Position

CEI-Lit-WS is the **only** database that systematically classifies AI ethics papers against moral psychology theories. This is an entirely novel contribution. PhilPapers doesn't track psychology at all. Scopus and Web of Science don't cross-classify computer science papers against psychological theories. This is a blue ocean.

#### Recommendations

1. **Add Moral Disengagement** (Bandura) as a 9th moral psychology dimension — it's directly relevant to discussions of autonomous weapons, algorithmic harm, and responsibility displacement in AI.
2. **Add methodology classification** for moral psychology papers: survey, experiment, neuroimaging, computational model, philosophical analysis, text analysis.
3. **Consider partnering with moral psychology labs** (e.g., YourMorals.org, MoralFoundations.org) to validate the classification accuracy via expert coding.
4. **Track moral psychology instruments** mentioned in papers: MFQ (Moral Foundations Questionnaire), SVS (Schwartz Values Survey), DIT (Defining Issues Test), PVQ (Portrait Values Questionnaire).

---

### 5.5 Expert 5: Comparative Religion & Culture Scholar

#### Strengths

1. **14 religious traditions scored individually.** Islam, Christianity, Buddhism, Judaism, Hinduism, Sikhism, Confucianism, Taoism, Shinto, Jainism, Baha'i, Zoroastrianism, Ubuntu, and Indigenous traditions — each with a 0–100 confidence score. This is extraordinarily comprehensive. Most AI ethics databases don't mention religion at all. Those that do typically group everything as "religious perspectives" — a monolithic category that erases the vast differences between traditions.

2. **Demographics FP filter.** The distinction between papers *about* a religious tradition in AI ethics and papers that merely mention a tradition in a demographics or bias context (e.g., "anti-Muslim bias in NLP") is a genuine methodological challenge. The demographics-identity keyword split that demotes bias/NLP papers (Islam -66, Christianity -31, Judaism -17 FPs removed) shows thoughtful handling of this problem.

3. **Indigenous keyword expansion.** Moving from 7 to 37 Indigenous detections (tikanga, kaitiakitanga, Maori+AI, data sovereignty, decolonize+AI) reflects genuine engagement with Indigenous perspectives, not just tokenistic inclusion.

4. **Minority tradition coverage.** Baha'i (+5), Zoroastrianism (+6), Shinto (+1 strong, +4 medium), Jainism (+4 medium) — these are traditions rarely represented in any AI governance database. Their inclusion signals that this is not just a Christian/Islamic/Buddhist project.

5. **20+ cultural categories.** Chinese, Japanese, Korean, Indian, African/Ubuntu, Arabic, Hebrew, Persian, Indigenous, Latin American, Southeast Asian, and more — the cultural dimension complements the religious dimension and allows cross-tabulation (e.g., "Japanese + Buddhist" vs. "Japanese + Shinto").

#### Weaknesses

1. **English-language detection bias.** Keyword-based scoring in English inherently favors traditions with large English-language scholarly output. Christianity, Islam, and Buddhism have extensive English-language AI ethics literature. Shinto, Jainism, and Zoroastrianism do not. The low detection counts for minority traditions may reflect not the absence of relevant work but the absence of relevant work *in English*.

2. **Tradition vs. culture conflation.** "Ubuntu" appears as both a religious tradition (rv_ubuntu) and a cultural value (national_ethnic_cultural: "African/Ubuntu"). This is conceptually confusing. Ubuntu is a philosophical concept (not a religion), Confucianism is debated as philosophy vs. religion, and Indigenous traditions are enormously diverse (Maori ≠ Navajo ≠ Aboriginal Australian).

3. **No denominational granularity.** "Christianity" encompasses Catholic social teaching, Orthodox theology, Protestant ethics, Evangelical perspectives, liberation theology, and Quaker peace testimony — radically different positions on AI. "Islam" encompasses Sunni, Shi'a, Ibadi, Sufi, and Salafi perspectives. The 0–100 score for "rv_christianity" doesn't capture this internal diversity.

4. **Western academic framing.** The classification system itself is a Western academic construct — taxonomizing traditions into named categories is a Western methodological choice. Some Indigenous knowledge systems resist categorization into "religious" vs. "cultural" vs. "ethical."

5. **No practitioner validation.** Have representatives of these traditions reviewed how their tradition is classified? A Sikh scholar might object to how Sikhism is characterized; a Maori elder might object to "Indigenous" as a catch-all category.

#### Competitive Position

No other AI ethics database comes close to this level of religious and cultural classification. PhilPapers has a "Philosophy of Religion" category but doesn't cross-classify with AI. The sister project Tapestry (1,405 AI governance statements) includes religious bodies but doesn't score individual traditions at the document level. CEI-Lit-WS's religious values scoring is a **unique scholarly contribution** — publishable in its own right.

#### Recommendations

1. **Add denominational sub-scoring** for at least Christianity (Catholic, Protestant, Orthodox) and Islam (Sunni, Shi'a), since these have visibly different AI ethics positions.
2. **Separate "Ubuntu" from religious traditions** — it's a philosophical/ethical concept, not a religion. Create a "philosophical traditions" dimension alongside normative frameworks.
3. **Seek practitioner review.** Invite scholars from 5–6 traditions to review 20 papers each and validate the classification. This is both methodologically necessary and respectful.
4. **Expand non-English paper coverage.** Partner with regional databases to find AI ethics papers in Arabic, Chinese, Japanese, Hindi, and other languages where religious-ethical traditions are discussed in non-English scholarship.
5. **Document the "tradition vs. culture" boundary** explicitly — acknowledge the Western academic framing and its limitations.

---

### 5.6 Expert 6: Bibliometrician / Data Scientist

#### Strengths

1. **21 dashboard versions with genuine analytical evolution.** This isn't vanity versioning. Tracking the progression from v4 through v13 reveals genuine analytical deepening: v7b added network graph node coloring, v7b2 introduced normative ethics subtabs, v7e split religious values by tradition, v8 consolidated into a unified analytics platform, v8b added 10 new charts (co-occurrence matrix, culture/language timelines), v12 added moral psychology bug-fix rescoring, v13 promoted CE/CO/Principlism to dedicated subtabs. Each version answered new research questions.

2. **40+ chart types across 11 tabs.** The chart diversity includes: distribution histograms, temporal trend lines, co-occurrence matrices, heatmaps, treemaps, radar charts, network graphs (with 5-mode coloring), stacked bar charts, and more. This rivals commercial bibliometric visualization tools like VOSviewer for the specific domain.

3. **Split data architecture.** The "fat data, thin client" design (Python pre-computes cross-tabs, JavaScript only renders) is architecturally sound and enables future scaling.

4. **14 AI lab tracking.** Analyzing 350+ papers by lab with model-level documentation enables research questions that mega-databases can't answer: "How has OpenAI's research evolved from GPT-2 safety concerns to GPT-4 alignment?"

5. **Automated classification pipeline.** 6 scripts, 7 stages, 500+ unit tests. The scoring formula is transparent and reproducible.

#### Weaknesses

1. **No citation data.** This is the most significant analytical gap. Citation data is freely available from OpenAlex (CC0) and Semantic Scholar (free API). Without it, CEI-Lit-WS cannot compute: h-index by topic, citation networks, influential paper identification, co-citation analysis, bibliographic coupling, burst detection, or any of the standard bibliometric analyses.

2. **No co-authorship network.** With 11,439 author profiles and semicolon-separated author lists, the data exists to construct co-authorship networks — but no analysis has been done. This is low-hanging fruit.

3. **No venue normalization.** The `publication_title` / `container-title` field is not normalized. "NeurIPS," "Neural Information Processing Systems," and "Advances in Neural Information Processing Systems" may appear as separate venues. This limits venue-based analytics.

4. **No statistical validation of the classification pipeline.** The 500+ unit tests verify code correctness, not classification accuracy. What is the precision and recall of the ethics_overall scorer? Of the normative framework detectors? Of the moral psychology classifiers? Without ground-truth validation, the confidence scores are self-referential.

5. **No temporal evolution analysis.** Despite having year data for all 2,043 papers, the dashboards don't (as far as documented) show the evolution of ethical discourse — e.g., "When did 'alignment' overtake 'fairness' as the dominant ethics keyword?" or "What is the growth rate of care ethics papers?"

#### Competitive Position

CEI-Lit-WS's dashboards are more analytically sophisticated than any competitor's visualization of AI ethics data. But the absence of citation analysis — the bread and butter of bibliometrics — means the vault cannot replace or complement tools like VOSviewer, CiteSpace, or Bibliometrix for standard bibliometric purposes. It is best positioned as a **classification-first, visualization-rich, domain-specific analytical tool** that complements (not replaces) citation-based bibliometrics.

#### Recommendations

1. **Integrate OpenAlex citation data.** The OpenAlex API is free and CC0. For each paper with a DOI, fetch: cited_by_count, referenced_works, related_works. This single integration would unlock citation analysis.
2. **Build co-authorship networks.** The 11,439 author profiles + semicolon-separated author lists provide the raw data. Use a simple edge list (author_i, author_j, paper_key) and visualize with force-directed graphs.
3. **Normalize venue names.** Map `publication_title` to a canonical venue list (top 50 venues would cover most papers).
4. **Validate classification accuracy.** Sample 200 papers, have 2 expert coders classify them, compute Cohen's kappa for each dimension.
5. **Add temporal trend analytics** to the dashboard: keyword frequency over time, framework popularity curves, emerging topic detection.

---

### 5.7 Expert 7: Digital Humanities & Infrastructure Scholar

#### Strengths

1. **Plain text architecture.** Markdown + YAML + Git is the most durable data format in digital humanities. No database server to maintain, no proprietary format to decode, no vendor lock-in. A researcher in 2076 can open these files with any text editor.

2. **Git version control.** Every change is tracked, diffable, and reversible. The Git history is a complete provenance record. This is better than most institutional databases, which overwrite records without version history.

3. **Obsidian as interface layer.** Using Obsidian as a read-write interface over plain text files is an inspired architectural choice. It provides: wikilink navigation, full-text search, graph visualization, community plugins — all without altering the underlying data format. If Obsidian disappears, the data survives.

4. **Automated safety systems.** The NO FILE DELETIONS rule (mv to RECYCLE-BIN), YAML safety patterns (regex-based editing, never parse/rebuild round-trip), report immutability (never overwrite, always date-prefix) — these are hard-won operational safeguards that protect data integrity.

5. **Classification pipeline as code.** The 7-stage pipeline is versioned Python code. This is better than manual classification (irreproducible) or commercial tools (opaque). Any future maintainer can read, modify, and re-run the pipeline.

#### Weaknesses

1. **Bus factor of 1.** This is the existential risk. Single maintainer, no institutional backing, no community governance, no succession plan. If the maintainer is hit by a bus (the canonical example), the project stops.

2. **No DOI or persistent identifier.** The dataset itself has no DOI. It cannot be cited persistently. A Zenodo deposit would solve this in 30 minutes.

3. **No stated license.** Without a license, the default is "all rights reserved." Is this open data? Open source? CC-BY? CC-BY-SA? Researchers cannot legally reuse the data without knowing.

4. **No community contribution pathway.** There is no way for external researchers to contribute corrections, additions, or improvements. No issue tracker for data quality, no pull request workflow for new papers, no community forum.

5. **No institutional preservation partner.** Not deposited in Zenodo, Figshare, Dryad, Internet Archive, or any institutional repository. The GitHub repository is not a preservation strategy — GitHub can delete repositories, change terms of service, or cease operations.

6. **GitHub Pages dependency.** The dashboards are hosted on GitHub Pages (`cjimmylin.github.io/cei-dashboard-13/`). This is convenient but not archival. GitHub Pages is a free service with no preservation guarantee.

#### Competitive Position

CEI-Lit-WS has the best possible *format* for longevity (plain text) but the worst possible *governance* for longevity (single maintainer, no institution). The irony is stark: the data is more durable than most commercial databases, but the project is more fragile than almost any institutional effort.

#### Recommendations

1. **Deposit on Zenodo** (today). Get a DOI. Enable versioned snapshots. This takes 30 minutes and immediately makes the project citable and preservable.
2. **State a license.** CC-BY-4.0 is standard for academic datasets. Add a LICENSE file to the repository.
3. **Write a data management plan.** Where does the data go if the maintainer can't continue? Who has repository access? What is the minimum viable maintenance plan?
4. **Seek an institutional home.** A university library, a research center, or a nonprofit (like OurResearch or Partnership on AI) could provide hosting, DOI minting, and continuity.
5. **Open community contributions.** Enable GitHub Issues for data quality reports. Consider a "contributor" tier where vetted researchers can submit new papers via pull requests.
6. **Archive dashboards** with the Internet Archive's Wayback Machine or download them as static snapshots alongside each data release.

---

## 6. Gap Analysis

### 6.1 What Competitors Do That CEI-Lit-WS Does Not

| # | Capability | Who Has It | Impact | Difficulty to Add |
|---|-----------|-----------|--------|------------------|
| 1 | **Citation network analysis** | OpenAlex, S2, Scopus, WoS | High — core bibliometric function | Low (OpenAlex API is free) |
| 2 | **Co-authorship networks** | Scopus, WoS, VOSviewer | Medium — reveals research communities | Low (data exists in vault) |
| 3 | **ORCID author identification** | OpenAlex, S2, Scopus | Medium — institutional interoperability | Medium (API lookups needed) |
| 4 | **Standard metadata export** | All Tier 1 databases | High — blocks institutional adoption | Medium (crosswalk scripts) |
| 5 | **PRISMA-compliant methodology** | Jobin 2019, Fjeld 2020, Resp. AI | High — blocks academic citation | Medium (documentation task) |
| 6 | **DOI/persistent identifier** | All established databases | High — blocks preservation | Very Low (Zenodo deposit) |
| 7 | **Open license** | OpenAlex, S2, AIID | Medium — blocks reuse | Very Low (add LICENSE) |
| 8 | **REST API** | OpenAlex, S2, Scopus, WoS | Medium — enables programmatic access | High (engineering effort) |
| 9 | **Community governance** | OpenAlex, AIID, PhilPapers | Medium — sustainability | Medium (institutional partnership) |
| 10 | **Multilingual coverage** | OpenAlex, S2, Google Scholar | Medium — scope limitation | High (language expertise) |
| 11 | **Real-time update pipeline** | OpenAlex, S2 | Low — freshness vs. curation | High (automation investment) |
| 12 | **Statistical validation** | Resp. AI Measures (Nature 2025) | High — classification credibility | Medium (expert coding study) |
| 13 | **Venue normalization** | OpenAlex, S2, Scopus | Low–Medium — analytics gap | Low (mapping table) |

### 6.2 What CEI-Lit-WS Does That No Competitor Does

| # | Unique Capability | Nearest Competitor | Gap From Nearest |
|---|------------------|-------------------|-----------------|
| 1 | **5 normative framework scores (0–100)** | PhilPapers (taxonomy only, no scores) | PhilPapers categorizes but doesn't score; no other DB tracks all 5 |
| 2 | **8 moral psychology theory scores** | None | No competitor tracks moral psychology theories in AI papers |
| 3 | **14 religious tradition scores** | None | No competitor scores individual religious traditions in AI literature |
| 4 | **92% full-text PDF collection** | S2 (full-text access via GROBID) | S2 has text but no structured extracts; CEI has curated extracts |
| 5 | **~2,487 structured text extracts** | None at this scale for AI ethics | Unique infrastructure for full-text analysis |
| 6 | **21 dashboard versions / 40+ chart types** | VOSviewer (general bibliometrics) | CEI dashboards are domain-specific with ethics-aware analytics |
| 7 | **7-stage automated pipeline (500+ tests)** | Resp. AI Measures (manual coding) | Automated vs. manual; reproducible vs. one-time |
| 8 | **14 AI lab tracking (350+ papers)** | None | No competitor maps papers to AI labs with model-level detail |
| 9 | **Continuous confidence scoring (0–100)** | None for multi-dimensional ethics | Binary labels are universal; confidence scores are novel |
| 10 | **20+ cultural value categories** | None | No competitor systematically tags cultural context in AI papers |

**Summary:** CEI-Lit-WS's competitive moat is entirely in **classification depth** and **analytical infrastructure**. No competitor comes close on these dimensions. The gaps are in **scale**, **standards compliance**, and **institutional sustainability** — areas where competitors have massive structural advantages.

---

## 7. Positioning

### 7.1 The 2×2 Matrix: Scale × Classification Depth

```
                        Classification Depth
                    Shallow ──────────────────── Deep
                    │                              │
        Large  ─────┤  OpenAlex    Scopus          │
        (10K+)      │  Sem. Scholar  WoS           │
                    │  Google Scholar               │
                    │  Dimensions   Lens.org        │
                    │                   [EMPTY]     │◄── Opportunity
                    │                              │
        Medium ─────┤  AIES        PhilPapers      │
        (500-5K)    │  FAccT       Toronto Bib     │
                    │  ACM DL                      │
                    │              ★ CEI-Lit-WS ★   │◄── Unique position
                    │                              │
        Small  ─────┤  AlgorithmWatch  Fjeld 2020  │
        (<500)      │  MAIEI       Jobin 2019      │
                    │  Worldwide   Resp. AI Meas.  │
                    │  MIT Risk Repo  Hagendorff   │
                    │                              │
                    └──────────────────────────────┘

Scale = number of papers/entries
Classification Depth = number of structured analytical dimensions per entry
```

### 7.2 Positioning Statement

> **CEI-Lit-WS is the only AI ethics literature database that combines medium-scale paper coverage (2,043 papers) with deep multi-dimensional ethical classification (27+ scored dimensions per paper).** It occupies a niche that no general mega-database (which prioritize scale over domain depth) and no curated bibliography (which prioritize precision over analytical breadth) currently fills. Its unique value proposition is not "more papers" or "better metadata" — it is the ability to answer research questions that require cross-dimensional ethical analysis at corpus scale: "How does normative framework usage correlate with moral psychology theory engagement across religious traditions?"

### 7.3 Three Competitive Moats

1. **Classification schema complexity.** The 50+ field schema with 27+ scored dimensions took 120+ development sessions to build and refine. Replicating the keyword dictionaries, FP handling, scoring formulas, and unit tests would require months of domain-expert effort. This is not easily copied.

2. **Full-text infrastructure.** 1,886 PDFs + 2,487 structured extracts enable scoring beyond abstracts. Assembling this collection required 13-strategy PDF acquisition waterfall, bot-bypass strategies, and manual downloads. The extract quality (25K char structured text) is superior to generic GROBID output.

3. **Analytical dashboard ecosystem.** 21 dashboard versions embody accumulated domain knowledge about what questions researchers ask about AI ethics. The chart designs, tab organization, and cross-tabulation choices reflect 120+ sessions of iterative refinement. A competitor would need to replicate not just the code but the research intuition.

---

## 8. Strategic Recommendations

### 8.1 High Priority (3–6 months)

These actions address the vault's most critical weaknesses while requiring moderate effort.

#### 8.1.1 Write PRISMA Methodology Documentation
- **What:** Document the actual collection process retrospectively (databases searched, date ranges, selection criteria, Zotero workflow)
- **Why:** Without this, CEI-Lit-WS cannot be cited in systematic reviews — the dominant form of AI ethics meta-analysis
- **Effort:** 2–3 days of writing
- **Impact:** Transforms the vault from "personal bibliography" to "citable research resource"

#### 8.1.2 Integrate Citation Data via OpenAlex
- **What:** For each paper with a DOI, fetch cited_by_count, referenced_works, and related_works from the OpenAlex API (free, CC0)
- **Why:** Unlocks citation analysis, influence measurement, and co-citation networks — the most-requested bibliometric analyses
- **Effort:** 1 script + 1 API batch run (~2 days engineering)
- **Impact:** Closes the single biggest analytical gap vs. all Tier 1 competitors

#### 8.1.3 Zenodo Deposit + DOI
- **What:** Deposit a versioned snapshot of the dataset (YAML metadata + classification fields, no PDFs) on Zenodo
- **Why:** Creates a persistent identifier, enables citation, establishes preservation
- **Effort:** 30 minutes for initial deposit; 1 hour per versioned release
- **Impact:** Immediately makes the project citable, preservable, and discoverable

#### 8.1.4 Add ORCID Integration
- **What:** Enrich author profiles with ORCID identifiers via the ORCID public API
- **Why:** Connects the vault to the global scholarly identity infrastructure
- **Effort:** 1 script + batch lookup (~1 day engineering)
- **Impact:** Medium — enables institutional interoperability and author disambiguation

#### 8.1.5 State a License
- **What:** Add a LICENSE file (recommended: CC-BY-4.0 for data, MIT for code)
- **Why:** Without a license, no one can legally reuse the data
- **Effort:** 5 minutes
- **Impact:** Removes a fundamental barrier to adoption

### 8.2 Medium Priority (6–12 months)

These actions strengthen the vault's competitive position and expand its utility.

#### 8.2.1 JSON-LD / BibTeX Export
- **What:** Build export scripts that convert YAML frontmatter to: (a) JSON-LD using schema.org ScholarlyArticle vocabulary, (b) BibTeX for citation managers, (c) CSV for spreadsheet analysis
- **Why:** The vault's data is currently locked in Obsidian-specific format
- **Effort:** 3–5 days engineering
- **Impact:** Dramatically increases accessibility for researchers who don't use Obsidian

#### 8.2.2 Classification Validation Study
- **What:** Sample 200 papers, recruit 2–3 domain experts, have them classify against the same dimensions. Compute inter-rater reliability (Cohen's kappa) and compare with automated pipeline scores
- **Why:** The pipeline has 500+ unit tests but no external validation. A validation study is the standard for establishing classification credibility
- **Effort:** 2–4 weeks (recruitment + coding + analysis)
- **Impact:** High — transforms the pipeline from "automated heuristic" to "validated classification system"

#### 8.2.3 Scale to 5,000+ Papers
- **What:** Systematic expansion targeting: (a) papers from OpenAlex/S2 topic queries not already in vault, (b) non-English publications, (c) law and policy journals, (d) regional AI conferences
- **Why:** At 2,043 papers, coverage is estimated at 10–20% of the field. 5K+ would reach 30–50%
- **Effort:** Ongoing; depends on automation level
- **Impact:** Strengthens the "medium scale" positioning and improves coverage claims

#### 8.2.4 Cross-Link with AIID and MIT AI Risk Repository
- **What:** Map CEI-Lit-WS papers to related AI incidents (AIID) and risk categories (MIT)
- **Why:** Creates a unique paper → risk → incident pathway that no single database offers
- **Effort:** 1–2 weeks (matching + verification)
- **Impact:** Creates novel analytical capability and partnership opportunities

#### 8.2.5 Co-Authorship Network Analysis
- **What:** Extract co-authorship edges from the author lists, build network graphs, identify research communities
- **Why:** The data already exists (11,439 author profiles) — this is low-hanging analytical fruit
- **Effort:** 2–3 days engineering
- **Impact:** Adds a standard bibliometric analysis that users expect

#### 8.2.6 Venue Normalization
- **What:** Create a canonical venue mapping (top 50 venues + catch-all) and normalize publication_title
- **Why:** Enables venue-based analytics (which journals publish the most AI ethics research?)
- **Effort:** 1 day
- **Impact:** Low–Medium — enables a standard analysis

### 8.3 Aspirational (12+ months)

These actions would transform CEI-Lit-WS from a research tool into a community infrastructure.

#### 8.3.1 REST API
- **What:** Build a lightweight API (FastAPI or similar) that exposes the classification data
- **Why:** Enables programmatic access, third-party integrations, and widget embedding
- **Effort:** 2–4 weeks engineering + hosting costs
- **Impact:** Transforms the vault from static dataset to queryable service

#### 8.3.2 Community Curation Model
- **What:** Enable external contributions via: (a) GitHub Issues for data quality reports, (b) pull requests for new papers, (c) expert reviewer roles for classification validation
- **Why:** Addresses the bus factor of 1 and creates a sustainability pathway
- **Effort:** Organizational (governance design + community management)
- **Impact:** High — the difference between "personal project" and "community resource"

#### 8.3.3 Multilingual Paper Coverage
- **What:** Systematic discovery and inclusion of AI ethics papers in Chinese, Arabic, Japanese, Korean, Hindi, and other languages
- **Why:** The current English-dominant collection underrepresents non-Western ethical perspectives
- **Effort:** High (requires language expertise + translation + expanded keyword lists)
- **Impact:** High — would make the religious/cultural classification dimensions much more meaningful

#### 8.3.4 Semantic Similarity Classification
- **What:** Supplement keyword-based scoring with sentence embedding similarity (using SPECTER or similar) to catch papers that discuss frameworks without canonical keywords
- **Why:** Addresses the recall problem in keyword-based classification (a paper about "rule-based moral reasoning" should score on deontological_ethics)
- **Effort:** Medium (model integration + threshold calibration)
- **Impact:** Medium–High — improves classification recall without sacrificing precision

#### 8.3.5 Institutional Partnership
- **What:** Partner with a university library, research center, or nonprofit to provide: institutional hosting, DOI minting, preservation guarantees, and governance structure
- **Why:** Addresses the bus factor and sustainability risk
- **Effort:** Organizational (relationship-building + negotiation)
- **Impact:** Transformative — converts a personal project into an institutional resource

---

## 9. Council Consensus Summary

### 9.1 Final Ratings

| Assessment Area | Rating (1–5) | Consensus Note |
|----------------|-------------|---------------|
| **Classification Depth** | ★★★★★ (5/5) | Unmatched. 27+ scored dimensions per paper. No competitor offers even 5 comparable axes. |
| **Domain Coverage** | ★★★★☆ (4/5) | Strong for English-language AI ethics. Gaps in non-English, non-CS venues, and recent work (scale ceiling at 2K). |
| **Analytical Infrastructure** | ★★★★½ (4.5/5) | 21 dashboard versions with genuine analytical depth. Missing citation networks. |
| **Metadata Standards** | ★★☆☆☆ (2/5) | Rich but non-standard. No Dublin Core, no ORCID, no RDF. Custom YAML schema. |
| **Reproducibility** | ★★★☆☆ (3/5) | Pipeline is reproducible (deterministic, tested). Collection methodology is not documented. |
| **Sustainability** | ★★☆☆☆ (2/5) | Excellent format durability (plain text + Git). Critical governance risk (bus factor 1, no DOI, no license). |
| **Academic Citability** | ★★☆☆☆ (2/5) | Cannot be cited as systematic review. No DOI, no methodology paper, no versioned releases. |
| **Interoperability** | ★★☆☆☆ (2/5) | No standard exports (BibTeX, CSV, JSON-LD). Obsidian wikilinks are not interoperable. |
| **Innovation** | ★★★★★ (5/5) | Genuinely novel contribution. The multi-dimensional ethical classification schema has no precedent. |
| **Competitive Position** | ★★★★☆ (4/5) | Unique niche with no direct competitor. Strong moat in classification depth. Vulnerable on sustainability. |

### 9.2 Overall Verdict

The Council unanimously agrees on the following assessment:

**CEI-Lit-WS is a genuinely innovative research infrastructure that has no direct competitor.** Its multi-dimensional ethical classification system — spanning normative ethics, moral psychology, religious traditions, cultural values, and data nature — represents a novel contribution to AI ethics methodology. The 7-stage automated pipeline, 21-version dashboard ecosystem, and 92% full-text collection rate demonstrate exceptional engineering for a single-maintainer project.

**However, the vault's impact is severely constrained by three fixable gaps:**

1. **It cannot be cited** (no DOI, no methodology paper, no versioned releases)
2. **It cannot be integrated** (no standard metadata, no exports, no API)
3. **It may not survive** (bus factor 1, no institution, no license, no preservation plan)

**The strategic imperative is clear:** The classification depth is the moat. The infrastructure and sustainability gaps are the vulnerabilities. The highest-ROI actions are the fastest to implement: Zenodo deposit (30 min), license file (5 min), PRISMA documentation (2–3 days), and OpenAlex citation integration (2 days). These four actions alone would transform CEI-Lit-WS from a personal research tool into a citable, preservable, analytically complete research infrastructure.

The Council's final position: **CEI-Lit-WS has built something no one else has. The urgent task is not to build more — it is to make what exists findable, citable, and durable.**

---

## Appendix A: Complete YAML Field Inventory

### A.1 Zotero Fields (Core Bibliographic Metadata)

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `key` | String | Yes | `2KFZELQU` |
| `type` | String | Yes | `journalArticle`, `conferencePaper`, `preprint` |
| `title` / `short_title` | String | One required | `"Concrete Problems in AI Safety"` |
| `year` | Integer | Yes | `2016` |
| `first_author` | Wikilink | Yes | `"[[Dario Amodei]]"` |
| `authors` | String | Recommended | `"Dario Amodei; Chris Olah; Jacob Steinhardt"` |
| `url` | URL | Recommended | `"https://arxiv.org/abs/1606.06565"` |
| `external_pdf` | URL | Optional | `"https://arxiv.org/pdf/1606.06565.pdf"` |
| `abstract` | String | Recommended | Plain text abstract |
| `DOI` | String | Optional | `"10.1145/1234567"` |
| `publication_title` | String | Optional | `"Neural Information Processing Systems"` |

### A.2 Ethics Classification Fields (Stage 1–3)

| Field | Type | Range | Script |
|-------|------|-------|--------|
| `ethics_overall` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `virtue_ethics` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `deontological_ethics` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `utilitarian_ethics` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `care_ethics` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `contractarian_ethics` | Integer | 0–100 | `classify_ethics.py` / `ethics_scoring.py` |
| `ethics_perspective` | String | 10 categories | `classify_ethics_perspective.py` |
| `research_topic` | String | 7 categories | `classify_non_ethics_topics.py` |

### A.3 Cultural & Religious Fields (Stage 5)

| Field | Type | Range | Script |
|-------|------|-------|--------|
| `national_ethnic_cultural` | String/List | 20+ categories | `classify_cultural_religious.py` |
| `religious_values` | String/List | Derived | `classify_cultural_religious.py` |
| `rv_islam` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_christianity` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_buddhism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_judaism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_hinduism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_sikhism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_confucianism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_taoism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_shinto` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_jainism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_bahai` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_zoroastrianism` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_ubuntu` | Integer | 0–100 | `religious_values_scoring.py` |
| `rv_indigenous` | Integer | 0–100 | `religious_values_scoring.py` |
| `religious_values_list` | List | Derived | `religious_values_scoring.py` |

### A.4 Moral Psychology Fields (Stage 6)

| Field | Type | Range | Script |
|-------|------|-------|--------|
| `mp_mft` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_schwartz` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_trolley` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_kohlberg` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_dual_process` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_intuitionist` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_dyadic` | Integer | 0–100 | `moral_psych_scoring.py` |
| `mp_identity` | Integer | 0–100 | `moral_psych_scoring.py` |
| `moral_psychology` | String | Derived | `moral_psych_scoring.py` |

### A.5 Data Nature Fields (Stage 7)

| Field | Type | Values | Script |
|-------|------|--------|--------|
| `is_benchmark` | String | Yes/No/N/A/Unknown | `classify_data_nature.py` |
| `is_eval` | String | Yes/No/N/A/Unknown | `classify_data_nature.py` |
| `is_dataset` | String | Yes/No/N/A/Unknown | `classify_data_nature.py` |
| `data_description` | String | Auto-generated | `classify_data_nature.py` |
| `data_metrics` | String | Auto-extracted | `classify_data_nature.py` |

### A.6 Enrichment & Metadata Fields

| Field | Type | Source |
|-------|------|--------|
| `key_contribution` | String | Manual / LLM |
| `significance` | String | Manual / LLM |
| `paper_summary` | String | Automated |
| `local_pdf` | Wikilink | PDF acquisition |
| `pdf_extract` | Path | Text extraction |
| `newtags` | String (comma-sep) | `generate_newtags.py` |
| `tags` | List | Obsidian |
| `Human View` | String | Manual review |
| `Human View Date` | Date | Manual review |
| `Human View note` | String | Manual review |
| `Not AI` | String | Manual flagging |
| `LLM_assessed` | String | LLM pipeline |
| `DATA_URL` | String | Data link |

**Total: 50+ structured fields per paper.**

---

## Appendix B: Competitor URL Reference

| Database | URL |
|----------|-----|
| OpenAlex | openalex.org |
| Semantic Scholar | semanticscholar.org |
| Scopus | scopus.com |
| Web of Science | webofscience.com |
| Google Scholar | scholar.google.com |
| Dimensions.ai | dimensions.ai |
| Lens.org | lens.org |
| ACM Digital Library | dl.acm.org |
| IEEE Xplore | ieeexplore.ieee.org |
| PhilPapers | philpapers.org |
| AlgorithmWatch | algorithmwatch.org |
| AI Incident Database | incidentdatabase.ai |
| MIT AI Risk Repository | airisk.mit.edu |
| Connected Papers | connectedpapers.com |
| MAIEI | montrealethics.ai |
| Zenodo | zenodo.org |
| ORCID | orcid.org |
| VOSviewer | vosviewer.com |

---

## Appendix C: Dashboard Version History

| Version | Session | Key Changes |
|---------|---------|-------------|
| v4 | Early | Baseline dashboard |
| v5–v5f | Various | Iterative improvements |
| v6–v6d | Various | Feature additions |
| v7 | ~108 | Base multi-tab dashboard |
| v7b | 108 | Network graph with 5-mode node coloring |
| v7b2 | 111 | Normative Ethics tab (6 subtabs) |
| v7c | 112 | Moral Psychology tab overhaul (5 subtabs, 13 analytics) |
| v7e | 110 | Religious Values tab split (11 individual tradition subtabs) |
| v8 | 113 | Consolidation of v7b2 + v7c + v7e into unified platform |
| v8b | 116 | Countries & Languages enrichment (+10 new charts) |
| v9 | — | Incremental |
| v10 | — | Incremental |
| v11 | ~118 | Previous baseline |
| v12 | 119 | Moral psych bug-fix rescoring; generated by `generate_vault_dashboard_8.py` |
| v13 | 124 | Promoted CE/CO/Principlism to dedicated subtabs (9→11 tabs); generated by `generate_vault_dashboard_9.py` |

**Dashboard deployments on GitHub Pages:**
- `cjimmylin.github.io/cei-dashboard-3/`
- `cjimmylin.github.io/cei-dashboard-4/`
- `cjimmylin.github.io/cei-dashboard-8b/`
- `cjimmylin.github.io/cei-dashboard-13/`
- `cjimmylin.github.io/cei-eval-dashboard/`

---

*Report generated 2026-03-15. Data reflects vault state as of session 124 (2,043 papers, dashboard v13).*
*This report is a historical snapshot per CEI-Lit-WS report immutability policy — do not overwrite.*
