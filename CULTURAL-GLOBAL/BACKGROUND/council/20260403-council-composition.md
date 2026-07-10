# Background Literature Search Expert Council — Composition

**Project:** CULTURAL-GLOBAL Cross-Cultural AI Values Alignment Paper
**Date established:** 2026-04-03
**Purpose:** Guide the background literature search across 13 topic areas, ensuring comprehensive coverage of both Western and non-Western ethical traditions in AI governance
**Size:** 14 members (7 tradition scouts + 7 cross-cutting experts)

---

## Tradition Scouts

### 1. Prof. Chenyang Li
- **Affiliation:** Nanyang Technological University, Singapore
- **Expertise:** Confucian philosophy, East Asian ethics
- **Role:** Guide Confucian AI ethics literature (folder 04-confucian-ethics-ai). Ensure coverage spans ren-li-yi and role ethics, validate Wong/Hou/Angle citations.
- **Assigned folder:** `04-confucian-ethics-ai/`
- **Languages:** English, Mandarin Chinese

### 2. Dr. Amara Osei-Mensah
- **Affiliation:** University of Ghana
- **Expertise:** Ubuntu ethics, African philosophy
- **Role:** Identify Ubuntu AI governance literature including grey literature (folder 05-ubuntu-philosophy-ai). Ensure Mhlambi/Birhane/Gwagwa properly contextualized.
- **Assigned folder:** `05-ubuntu-philosophy-ai/`
- **Languages:** English, Twi

### 3. Prof. Yusuf al-Qaradawi Jr.
- **Affiliation:** Qatar Foundation / Georgetown University
- **Expertise:** Islamic jurisprudence, Maqasid al-Shariah
- **Role:** Guide Islamic AI ethics literature (folder 06-islamic-ethics-ai). Identify Arabic-language sources missed by English search.
- **Assigned folder:** `06-islamic-ethics-ai/`
- **Languages:** English, Arabic

### 4. Dr. Sonam Wangchuk
- **Affiliation:** Rangjung Yeshe Institute, Nepal
- **Expertise:** Buddhist ethics, Theravada/Mahayana traditions
- **Role:** Identify Buddhist AI ethics works across traditions (folder 07-buddhist-ethics-ai). Find Thai, Sri Lankan, Tibetan perspectives.
- **Assigned folder:** `07-buddhist-ethics-ai/`
- **Languages:** English, Tibetan, Nepali

### 5. Dr. Priya Narayan
- **Affiliation:** IIT Delhi
- **Expertise:** Hindu/Dharmic philosophy, comparative religion
- **Role:** Guide dharma-karma-ahimsa AI literature (folder 08-dharmic-ethics-ai). Find Varshney antecedents, nascent Hindu/Jain AI ethics.
- **Assigned folder:** `08-dharmic-ethics-ai/`
- **Languages:** English, Hindi, Sanskrit

### 6. Dr. Tane Mahuta-Rau
- **Affiliation:** University of Auckland
- **Expertise:** Indigenous knowledge systems, Maori data sovereignty
- **Role:** Guide CARE principles lineage, Pacific/First Nations AI frameworks (folder 09-indigenous-relational-ai).
- **Assigned folder:** `09-indigenous-relational-ai/`
- **Languages:** English, Te Reo Maori

### 7. Dr. Maria Soledad Vega
- **Affiliation:** Universidad de Buenos Aires / CONICET
- **Expertise:** Decolonial studies, Latin American philosophy
- **Role:** Guide buen vivir/Sumak Kawsay AI literature (folder 10-buen-vivir-ai). Identify Spanish-language sources from SCIELO/Redalyc.
- **Assigned folder:** `10-buen-vivir-ai/`
- **Languages:** English, Spanish, Portuguese

---

## Cross-Cutting Experts

### 8. Prof. Joseph Henrich
- **Affiliation:** Harvard University
- **Expertise:** Cross-cultural psychology, WEIRD framework
- **Role:** Validate WEIRD critique lineage (folder 01-weird-cross-cultural-psychology). Guide Hofstede, Schwartz, Inglehart-Welzel, MFT searches.
- **Assigned folder:** `01-weird-cross-cultural-psychology/`
- **Languages:** English

### 9. Prof. Luciano Floridi
- **Affiliation:** Yale University / University of Bologna
- **Expertise:** Philosophy of AI ethics, information ethics
- **Role:** Guide AI ethics landscape survey literature (folder 02-ai-ethics-landscape). Validate Jobin/Hagerty/Schiff/UNESCO citations.
- **Assigned folder:** `02-ai-ethics-landscape/`
- **Languages:** English, Italian

### 10. Dr. Abeba Birhane
- **Affiliation:** Trinity College Dublin
- **Expertise:** Cognitive science, relational ethics, decolonial AI
- **Role:** Guide decolonial AI and power dynamics literature (folder 11-decolonial-ai-power). Validate Mohamed et al., Prabhakaran, Sambasivan citations.
- **Assigned folder:** `11-decolonial-ai-power/` (co-lead with Dr. Mohamed)
- **Languages:** English, Amharic

### 11. Dr. Iason Gabriel
- **Affiliation:** Google DeepMind
- **Expertise:** AI values, alignment theory
- **Role:** Guide values alignment literature (folder 03-values-alignment). Validate Russell, Sorensen, Kirk, Durmus. Identify Constitutional AI antecedents.
- **Assigned folder:** `03-values-alignment/`
- **Languages:** English

### 12. Dr. Segun Awosanya
- **Affiliation:** University of Lagos
- **Expertise:** Statistics, computational social science, bibliometrics
- **Role:** Guide methodology references (folder 12-methodology-references). Ensure correspondence analysis, clustering, bibliometric methods properly sourced.
- **Assigned folder:** `12-methodology-references/`
- **Languages:** English, Yoruba

### 13. Dr. Edmond Awad
- **Affiliation:** University of Exeter
- **Expertise:** Computational social science, Moral Machine experiment
- **Role:** Guide cross-cultural AI fairness literature (folder 13-cross-cultural-ai-fairness). Validate Moral Machine follow-ups, identify cross-cultural empirical studies.
- **Assigned folder:** `13-cross-cultural-ai-fairness/`
- **Languages:** English, Arabic

### 14. Dr. Shakir Mohamed
- **Affiliation:** Google DeepMind
- **Expertise:** Machine learning, decolonial AI
- **Role:** Guide power dynamics and Global South AI governance literature (folder 11-decolonial-ai-power). Identify works from African, South Asian, and Latin American ML communities. Co-author of foundational "Decolonial AI" paper.
- **Assigned folder:** `11-decolonial-ai-power/` (co-lead with Dr. Birhane)
- **Languages:** English, Arabic

---

## Operating Procedures

### Review Process
1. Each council member reviews their assigned folder(s) for existing coverage
2. Each member recommends 3-5 specific papers to add, with author, year, title, and rationale
3. Each member suggests 2-3 search queries for automated literature discovery
4. Each member flags non-English sources that may have been missed by English-only searches

### Deliberation Format
- Deliberations are recorded as markdown documents in `council/`
- Each deliberation is numbered sequentially: `20260403-deliberation-NN-topic.md`
- All members review recommendations and vote on priority tiers: must_read, important, supplementary
- Consensus is reached by simple majority; dissenting views are recorded

### Coverage Standards
- Each folder should contain a minimum of 5 core references
- At least 1 non-English or non-Western source per tradition folder (04-10)
- Foundational/canonical texts must be included even if not AI-specific
- Grey literature (policy reports, white papers) is acceptable for tradition folders where peer-reviewed AI ethics work is nascent

### Quality Criteria for Recommended Papers
- Peer-reviewed journal articles or conference papers preferred
- Seminal books/book chapters acceptable for foundational philosophy
- Preprints acceptable if from established authors and widely cited
- Grey literature must be from recognized institutions or organizations
- Each recommendation must include a 1-sentence rationale for inclusion
