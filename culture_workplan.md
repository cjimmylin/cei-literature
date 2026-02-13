# Exhaustive Cultural Values LLM Benchmark Search — Agent Swarm Plan

## Context

The CEI Literature Vault (846 papers) has strong coverage for **Chinese**, **American/Western**, and **Arabic/Islamic** cultural values benchmarks, but has critical gaps across most of the world's cultures and nationalities. The previous exhaustive search (2026-02-07, 19 agents, 300 papers) was broad-topic-focused — only 5 agents covered non-Western cultures, and those were combined (e.g., "Agents 9-11: Chinese + Islamic + African" in a single report). This search targets **every culture/nationality individually** to find papers that benchmark, evaluate, or measure LLMs' abilities to reflect cultural values.

**Goal:** Find ALL papers that assess cultural values alignment in LLMs — one dedicated agent per cultural region, searching exhaustively across academic databases. Additionally, add a new `cultures_nationalities_list` YAML field to **every paper in the vault** (existing 846 + all new imports).

**Scope:** Cultures and nationalities ONLY (no religious tradition-specific agents).

**New YAML field:**
- **Name:** `cultures_nationalities_list`
- **Format:** Comma-separated string (e.g., `"Chinese, Japanese, Korean"` or `"N/A"`)
- **Placement:** Inserted after `national_ethnic_cultural` in YAML frontmatter
- **Content:** All specific cultures and nationalities discussed, evaluated, or benchmarked in the paper — more granular than `national_ethnic_cultural` (e.g., a cross-cultural paper might list "Chinese, Japanese, Korean, American, German, French" while its `national_ethnic_cultural` is just "Multicultural/Cross-cultural")

---

## Current Coverage Baseline

| Culture/Region | Papers | Benchmarks | Status |
|---|---|---|---|
| Chinese | ~50 | ~13 (CValues, CBBQ, ChineseSafe, CMoralEval, etc.) | Well-covered |
| American/Western | ~52 | ~37 | Well-covered |
| Arabic | ~15 | ~9 (AraTrust, PalmX, MENAValues) | Well-covered |
| Cross-cultural | ~26 | ~19 (CulturalBench, WorldValuesBench, CCD-Bench) | Well-covered |
| Indian | ~11 | ~5 (Indian-BhED, IndiBias, IndiCASA) | Emerging |
| German | ~9 | ~6 | Moderate |
| Japanese | ~7 | ~5 (JETHICS, JBBQ, eJCM) | Emerging |
| French | ~7 | ~2 | Moderate |
| Spanish | ~7 | ~3 | Moderate |
| Iranian/Persian | ~6 | ~2 (ISN, ELAB) | Emerging |
| Korean | ~5 | ~1 (KorNAT) | Minimal |
| Russian | ~5 | ~2 | Emerging |
| Brazilian | ~5 | ~2 | Emerging |
| Italian | ~4 | ~2 | Minimal |
| Indonesian | ~3 | ~1 | Minimal |
| African/Ubuntu | ~19 | ~2 (language benchmarks only) | Philosophy-heavy, benchmark-light |
| **Turkish** | **0** | **0** | **VOID** |
| **Eastern European** | **0** | **0** | **VOID** |
| **Central Asian** | **0** | **0** | **VOID** |
| **Southeast Asian dedicated** | **0-2** | **0** | **VOID** |
| **Latin American** | **0** | **0** | **VOID** |
| **Indigenous/Aboriginal** | **~3** | **0** | **VOID** |
| **Pacific Islander/Caribbean** | **0** | **0** | **VOID** |
| **Scandinavian** | **0** | **0** | **VOID** |

---

## Phase 1: Agent Swarm Search (30 Agents, 6 Waves of 5)

### Wave 1: East Asian Deep Dives (Agents 1-5)

**Agent 1 — Chinese Values (expansion: 2025-2026 only)**
- Focus: NEW Chinese cultural values benchmarks published since Feb 2025
- Queries:
  1. `"Chinese cultural values" LLM benchmark 2025 2026`
  2. `"Chinese social values" alignment evaluation large language model`
  3. `"socialist core values" AI benchmark evaluation`
  4. `C-VARC "Chinese value" corpus language model`
  5. `"Chinese moral reasoning" dataset 2025 2026`
  6. `CDEval CLadder Chinese cultural knowledge LLM benchmark`
  7. `"Chinese safety" generative AI evaluation 2025`
  8. `"Chinese internet" content moderation LLM benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, HuggingFace

**Agent 2 — Japanese Cultural Values**
- Focus: Japanese cultural norms, social values, moral reasoning benchmarks
- Queries:
  1. `"Japanese cultural values" LLM benchmark evaluation`
  2. `"Japanese moral reasoning" dataset language model`
  3. `JETHICS JCommonsenseMorality eJCM extension 2025`
  4. `"Japanese social norms" NLP benchmark evaluation`
  5. `"Japanese safety" benchmark LLM stereotypes bias`
  6. `"Bushido" ethics AI evaluation benchmark`
  7. `JapaneseGLUE ethics safety cultural`
  8. `"Japanese language model" cultural alignment evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Agent 3 — Korean Cultural Values**
- Focus: Korean social values, moral norms, cultural alignment
- Queries:
  1. `"Korean cultural values" LLM benchmark evaluation`
  2. `KorNAT Korean alignment expansion 2025`
  3. `"KMMLU" Korean cultural knowledge moral evaluation`
  4. `"Korean moral values" language model evaluation`
  5. `"Korean social norms" AI benchmark dataset`
  6. `"Korean fairness" bias benchmark LLM`
  7. `"Korean language model" safety cultural alignment`
  8. `"Ko-LLM" Open Korean benchmark cultural evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Agent 4 — Taiwanese, Hong Kong, Singaporean Chinese-language Values**
- Focus: Distinct from mainland China — Taiwanese, HK, and Singaporean cultural specificity
- Queries:
  1. `"Taiwan" OR "Taiwanese" cultural values LLM benchmark`
  2. `"Hong Kong" cultural values language model evaluation`
  3. `"Singapore" cultural values LLM benchmark evaluation`
  4. `"traditional Chinese" cultural knowledge LLM evaluation`
  5. `"Taiwan MMLU" OR "TMMLU" cultural benchmark`
  6. `"Singlish" OR "RabakBench" Singapore cultural`
  7. `SeaEval Singapore benchmark cultural`
  8. `"Sinophone" cultural variation LLM alignment`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Agent 5 — Mongolian + Minor East Asian**
- Focus: Mongolian cultural values, plus Tibetan, Uyghur cultural benchmarks
- Queries:
  1. `"Mongolian" cultural values LLM benchmark evaluation`
  2. `"Mongolian language" model evaluation benchmark`
  3. `"Tibetan" cultural values AI benchmark`
  4. `"Uyghur" language cultural values LLM`
  5. `"Central East Asian" cultural values AI evaluation`
  6. `"Inner Mongolia" OR "Outer Mongolia" language model`
  7. `"minority language" Chinese cultural benchmark LLM`
  8. `"Okinawan" OR "Ryukyuan" cultural values AI`
- Databases: arXiv, Semantic Scholar, Google Scholar

---

### Wave 2: South & Southeast Asian Deep Dives (Agents 6-10)

**Agent 6 — Indian Cultural Values (expansion)**
- Focus: Indian cultural values beyond bias — dharmic concepts, caste, regional diversity
- Queries:
  1. `"Indian cultural values" LLM benchmark 2025 2026`
  2. `"Indian moral values" AI evaluation dataset`
  3. `PARIKSHA "Indian knowledge" benchmark LLM`
  4. `"Indian social norms" AI evaluation cultural`
  5. `"Hindi" OR "Tamil" OR "Bengali" cultural values LLM`
  6. `"Indian caste" bias values LLM evaluation`
  7. `"Indic language" cultural benchmark evaluation LLM`
  8. `AI4Bharat "Indian" evaluation benchmark cultural`
- Databases: arXiv, Semantic Scholar, Google Scholar, HuggingFace

**Agent 7 — Thai Cultural Values**
- Focus: Thai cultural norms, Thai-language LLM evaluation
- Queries:
  1. `"Thai cultural values" LLM benchmark evaluation`
  2. `ThaiCLI "Thai cultural linguistic intelligence"`
  3. `"Thai language model" safety ethics benchmark`
  4. `"Thai social norms" AI evaluation dataset`
  5. `"Thai-H6" OR "ThaiLLM" leaderboard evaluation`
  6. `"Thai dialect" cultural values LLM`
  7. `"Typhoon" Thai LLM cultural evaluation`
  8. `"Thailand" moral values AI benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, HuggingFace

**Agent 8 — Vietnamese Cultural Values**
- Focus: Vietnamese cultural norms, Vietnamese-language LLM evaluation
- Queries:
  1. `"Vietnamese cultural values" LLM benchmark evaluation`
  2. `VMLU "Vietnamese language understanding" benchmark`
  3. `"Vietnamese" ethics AI evaluation dataset`
  4. `"Vietnamese moral values" language model evaluation`
  5. `"Vietnamese social norms" LLM alignment`
  6. `"Vietnamese cultural knowledge" AI benchmark`
  7. `"Vietnamese language model" safety cultural`
  8. `"ViLLM" OR "PhoGPT" Vietnamese cultural evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 9 — Indonesian & Malay Cultural Values**
- Focus: Indonesian Pancasila values, Malay cultural norms, Javanese/Sundanese
- Queries:
  1. `"Indonesian cultural values" LLM benchmark evaluation`
  2. `IndoMMLU "Indonesian" cultural knowledge benchmark`
  3. `"Pancasila values" AI ethics benchmark Indonesia`
  4. `MalayMMLU "Malay cultural" evaluation LLM`
  5. `"Indonesian moral reasoning" LLM dataset`
  6. `SeaEval "Indonesian" OR "Malay" cultural benchmark`
  7. `"Javanese" OR "Sundanese" cultural knowledge AI`
  8. `"SEA-LION" Indonesian Malay cultural evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar, HuggingFace

**Agent 10 — Filipino, Cambodian, Myanmar, Laotian**
- Focus: Remaining Southeast Asian nations
- Queries:
  1. `"Filipino cultural values" LLM benchmark evaluation`
  2. `"Cambodian" OR "Khmer" cultural values AI benchmark`
  3. `"Myanmar" OR "Burmese" cultural values LLM`
  4. `"Laotian" OR "Lao" cultural values AI evaluation`
  5. `"Tagalog" moral norms AI benchmark dataset`
  6. `SEACrowd "Southeast Asian" cultural benchmark`
  7. `"Philippine" cultural values AI ethics benchmark`
  8. `"ASEAN" cultural values LLM evaluation benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

---

### Wave 3: Middle Eastern, Persian, Turkish & Central Asian (Agents 11-15)

**Agent 11 — Arabic Cultural Values (expansion: non-Islamic focus)**
- Focus: Pan-Arab cultural norms (not religion-specific), country-specific Arab benchmarks
- Queries:
  1. `"Arab cultural values" LLM benchmark 2025 2026`
  2. `"Saudi" OR "Emirati" OR "Qatari" cultural values LLM`
  3. `"Egyptian cultural values" AI benchmark evaluation`
  4. `"Moroccan" OR "Tunisian" OR "Algerian" cultural values LLM`
  5. `"Lebanese" OR "Jordanian" cultural values AI`
  6. `"MENA" values benchmark LLM cultural`
  7. `"Gulf" cultural norms AI evaluation benchmark`
  8. `"Arabic dialect" cultural values LLM evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 12 — Iranian/Persian Cultural Values (expansion)**
- Focus: Persian cultural norms, Iranian social values
- Queries:
  1. `"Iranian cultural values" LLM benchmark 2025 2026`
  2. `"Persian" language model cultural evaluation benchmark`
  3. `ELAB "Persian" LLM safety evaluation`
  4. `"Iranian social norms" AI evaluation dataset`
  5. `"FarsEval" OR "PeKA" Persian knowledge benchmark`
  6. `"Persian language" cultural knowledge LLM`
  7. `"Iranian" moral values AI evaluation benchmark`
  8. `"Farsi" cultural sensitivity LLM evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 13 — Turkish & Turkic Cultural Values**
- Focus: Turkish cultural norms, Turkic language family
- Queries:
  1. `"Turkish cultural values" LLM benchmark evaluation`
  2. `TurkBench "Turkish LLM" evaluation benchmark`
  3. `TurkishMMLU OR "TR-MMLU" cultural evaluation`
  4. `"Turkish social norms" AI benchmark dataset`
  5. `"Turkish language model" safety ethics cultural`
  6. `"Azerbaijani" OR "Turkmen" cultural values LLM`
  7. `"Turkish cultural sensitivity" AI evaluation`
  8. `"Anatolian" cultural values AI benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, HuggingFace

**Agent 14 — Central Asian Cultural Values**
- Focus: Kazakhstan, Uzbekistan, Kyrgyzstan, Tajikistan, Mongolia (cultural, not East Asian lens)
- Queries:
  1. `"Kazakh" cultural values LLM benchmark evaluation`
  2. `"Uzbek" cultural values AI benchmark`
  3. `"Kyrgyz" cultural values LLM evaluation`
  4. `"Central Asian" cultural values AI ethics benchmark`
  5. `"Tajik" cultural values AI evaluation`
  6. `"Kazakh language model" cultural evaluation`
  7. `"Central Asian languages" LLM benchmark evaluation`
  8. `"Silk Road" cultural values AI ethics benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 15 — Hebrew/Israeli Cultural Values**
- Focus: Israeli cultural norms, Hebrew-language LLM evaluation
- Queries:
  1. `"Israeli cultural values" LLM benchmark evaluation`
  2. `"Hebrew" language model cultural evaluation benchmark`
  3. `HeQ "Hebrew" question answering cultural`
  4. `"Israeli social norms" AI evaluation benchmark`
  5. `"Hebrew LLM" safety cultural alignment`
  6. `"Israel" bias fairness benchmark LLM`
  7. `"Hebrew NLP" cultural values evaluation`
  8. `"Israeli" moral values AI benchmark evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

---

### Wave 4: African & Latin American (Agents 16-20)

**Agent 16 — Sub-Saharan African Cultural Values (Ubuntu + beyond)**
- Focus: African communal ethics operationalized, African cultural norms as benchmarks
- Queries:
  1. `"Ubuntu" ethics benchmark AI LLM evaluation`
  2. `"African cultural values" benchmark LLM evaluation`
  3. `"African communitarian" ethics AI benchmark`
  4. `"South African" cultural values LLM benchmark`
  5. `"Nigerian" OR "Kenyan" OR "Ghanaian" cultural values LLM`
  6. `"decolonial" AI ethics benchmark Africa`
  7. `"African moral philosophy" benchmark LLM evaluation`
  8. `"African proverbs" moral reasoning AI benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, AfricaNLP proceedings

**Agent 17 — African Languages + Cultural Knowledge**
- Focus: Language-specific African cultural knowledge benchmarks
- Queries:
  1. `"Yoruba" OR "Igbo" cultural values AI benchmark`
  2. `"Hausa" cultural knowledge LLM benchmark`
  3. `"Swahili" cultural values AI evaluation`
  4. `"Amharic" OR "Ethiopian" cultural values LLM benchmark`
  5. `AfriCulture "African cultural knowledge" benchmark`
  6. `AfricaNLP 2025 2026 cultural values benchmark`
  7. `"Zulu" OR "isiXhosa" cultural values AI`
  8. `"West African" OR "East African" moral norms LLM`
  9. `IrokoBench AfroBench AfriMTE cultural evaluation`
  10. `"Wolof" OR "Kinyarwanda" OR "Shona" cultural AI`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Agent 18 — Brazilian & Portuguese-Speaking Cultural Values**
- Focus: Brazilian cultural norms, Portuguese-language LLM evaluation
- Queries:
  1. `"Brazilian cultural values" LLM benchmark evaluation`
  2. `"Portuguese" language model cultural evaluation benchmark`
  3. `"Brazilian moral values" AI benchmark dataset`
  4. `BenchMoral "Portuguese" moral foundations benchmark`
  5. `"Brazilian social norms" LLM evaluation`
  6. `"Lusophone" cultural values AI benchmark`
  7. `"Brazilian" bias fairness LLM benchmark`
  8. `"Portuguese-speaking" cultural values LLM evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 19 — Latin American Cultural Values (non-Brazilian)**
- Focus: Mexican, Argentine, Colombian, Chilean, Peruvian, and pan-Latin American values
- Queries:
  1. `"Latin American" cultural values LLM benchmark evaluation`
  2. `"Mexican" cultural values AI benchmark`
  3. `"Argentine" OR "Colombian" cultural values LLM`
  4. `"buen vivir" ethics AI evaluation benchmark`
  5. `"Latin American indigenous" values AI benchmark`
  6. `"Quechua" OR "Aymara" OR "Guarani" cultural values AI`
  7. `"LAAI" Latin American AI ethics evaluation`
  8. `"decolonial" Latin America AI values benchmark`
  9. `"Chilean" OR "Peruvian" cultural values LLM`
  10. `"Caribbean" cultural values LLM benchmark evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 20 — Indigenous & Aboriginal Cultural Values (Global)**
- Focus: Maori, Aboriginal Australian, First Nations, Native American, Inuit
- Queries:
  1. `"Indigenous" cultural values AI LLM benchmark`
  2. `"Maori" tikanga AI evaluation benchmark`
  3. `"Aboriginal Australian" cultural values AI`
  4. `"Native American" values AI benchmark evaluation`
  5. `"First Nations" cultural values LLM evaluation`
  6. `"Inuit" values ethics AI benchmark`
  7. `"indigenous data sovereignty" AI ethics benchmark`
  8. `"Te Reo Maori" AI language model evaluation`
  9. `"CARE" OR "OCAP" indigenous AI governance`
  10. `"indigenous knowledge systems" AI evaluation benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar

---

### Wave 5: European Deep Dives (Agents 21-25)

**Agent 21 — Eastern European Cultural Values**
- Focus: Polish, Ukrainian, Czech, Hungarian, Romanian, Balkan, Baltic
- Queries:
  1. `"Polish" cultural values LLM benchmark evaluation`
  2. `PLCC "Polish linguistic cultural competency" benchmark`
  3. `"Ukrainian" cultural values AI benchmark`
  4. `"Czech" OR "Slovak" cultural values LLM evaluation`
  5. `CUS-QA "Czech Ukrainian Slovak" benchmark`
  6. `"Hungarian" cultural values AI benchmark`
  7. `"Romanian" OR "Bulgarian" cultural values LLM`
  8. `"Balkan" OR "Serbian" OR "Croatian" cultural values AI`
  9. `"Baltic" OR "Lithuanian" OR "Latvian" cultural values LLM`
  10. `"Eastern European" moral values LLM benchmark`
- Databases: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Agent 22 — Russian Cultural Values (expansion)**
- Focus: Russian cultural norms, post-Soviet cultural identity
- Queries:
  1. `"Russian cultural values" LLM benchmark 2025 2026`
  2. `"Russian moral psychology" AI benchmark evaluation`
  3. `RuMMLU "Russian" cultural knowledge evaluation`
  4. `"Russian language model" safety cultural evaluation`
  5. `"Russian social norms" LLM alignment benchmark`
  6. `"post-Soviet" cultural values AI evaluation`
  7. `"Russian cultural types" LLM evaluation`
  8. `MERA "Russian" evaluation benchmark cultural`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 23 — Scandinavian & Nordic Cultural Values**
- Focus: Swedish, Norwegian, Danish, Finnish, Icelandic
- Queries:
  1. `"Scandinavian" OR "Nordic" cultural values LLM benchmark`
  2. `"Swedish" cultural values AI evaluation`
  3. `"Norwegian" OR "Danish" cultural values LLM`
  4. `"Finnish" cultural values AI benchmark evaluation`
  5. `"Icelandic" cultural values LLM evaluation`
  6. `"Nordic" social norms LLM alignment`
  7. `ScandEval cultural values ethics evaluation`
  8. `"Sami" OR "Saami" cultural values AI`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 24 — Mediterranean & Southern European Cultural Values**
- Focus: Greek, Portuguese, Catalan, Basque + Southern European niche
- Queries:
  1. `"Greek" cultural values LLM benchmark evaluation`
  2. `"Portuguese" cultural values AI benchmark (NOT "Brazilian")`
  3. `"Catalan" OR "CaBBQ" cultural values LLM`
  4. `"Basque" cultural values AI evaluation`
  5. `"Mediterranean" cultural values LLM benchmark`
  6. `"Swiss" cultural values LLM evaluation`
  7. `EsBBQ "Spanish bias" benchmark evaluation`
  8. `"Southern European" moral values LLM evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 25 — Western European Expansion (Dutch, Belgian, Austrian)**
- Focus: Smaller Western European nations not yet covered
- Queries:
  1. `"Dutch" cultural values LLM benchmark evaluation`
  2. `"Belgian" OR "Flemish" cultural values AI`
  3. `"Austrian" cultural values LLM benchmark`
  4. `"Irish" cultural values AI evaluation benchmark`
  5. `EuroLLM cultural evaluation benchmark European`
  6. `"MMLU-ProX" European languages cultural evaluation`
  7. `"European" cultural values LLM alignment benchmark`
  8. `"British" OR "UK" cultural values LLM evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

---

### Wave 6: Cross-Cultural Instruments + Meta-Search + Verification (Agents 26-30)

**Agent 26 — Cross-Cultural Survey Instruments Applied to LLMs**
- Focus: WVS, Hofstede, GLOBE, Pew, Schwartz adaptations for LLMs
- Queries:
  1. `"World Values Survey" LLM evaluation country-specific`
  2. `GlobalOpinionQA extension 2025 2026 country`
  3. `"Hofstede cultural dimensions" LLM benchmark evaluation`
  4. `LLM-GLOBE "GLOBE framework" cultural clusters`
  5. `"Pew Research" "Global Attitudes" LLM evaluation`
  6. `"Schwartz values" cross-cultural LLM benchmark`
  7. `"Inglehart-Welzel" cultural map LLM AI evaluation`
  8. `"Afrobarometer" OR "Eurobarometer" LLM evaluation`
  9. `"Moral Foundations" cross-cultural by country LLM`
  10. `"Gallup World Poll" AI alignment evaluation`
- Databases: arXiv, Semantic Scholar, Google Scholar

**Agent 27 — HuggingFace + PapersWithCode Cultural Datasets**
- Focus: Dataset hub searches for culture-specific evaluation sets
- Queries:
  1. `site:huggingface.co/datasets "cultural values" ethics moral benchmark`
  2. `site:huggingface.co "cultural" "benchmark" "LLM" evaluation`
  3. `HuggingFace datasets tag:cultural-awareness`
  4. `PapersWithCode "cultural" "values" benchmark dataset leaderboard`
  5. `PapersWithCode "ethics" "cultural" evaluation dataset`
  6. `HuggingFace "moral" "benchmark" "cultural" evaluation`
  7. `site:paperswithcode.com "cultural values" LLM benchmark`
  8. `HuggingFace datasets multilingual ethics cultural`
- Databases: HuggingFace, PapersWithCode, Google Scholar

**Agent 28 — Conference Workshops 2025-2026 (Culture-Specific)**
- Focus: Recent workshop proceedings for culture-specific NLP
- Queries:
  1. `C3NLP workshop 2025 2026 "cross-cultural" NLP`
  2. `ArabicNLP 2025 cultural values benchmark`
  3. `AfricaNLP 2025 2026 cultural values ethics`
  4. `"SoutheastAsianNLP" OR "AACL" cultural values benchmark`
  5. `"LREC-COLING" 2024 2025 cultural values evaluation`
  6. `ACL 2025 "cultural alignment" workshop proceedings`
  7. `"SemEval" 2025 2026 cultural values task`
  8. `NeurIPS 2025 "Pluralistic Alignment" workshop cultural`
  9. `"NAACL" 2025 cultural values LLM papers`
  10. `EMNLP 2025 cultural benchmark evaluation`
- Databases: ACL Anthology, Google Scholar, arXiv

**Agent 29 — Citation Graph Traversal (Culture-Specific Seeds)**
- Focus: Forward/backward citations from 20 culture-specific seed papers
- Seed papers: CValues, CDEval, KorNAT, JETHICS, AraTrust, INDIC-BIAS, IrokoBench, CulturalBench, LLM-GLOBE, CCD-Bench, NormAd, MENAValues, ELAB, WorldValuesBench, GlobalOpinionQA, BLEnD, FORK, SeaEval, Mind the Gap, CultureLLM
- Method: Semantic Scholar API citation traversal (forward + backward)
- Rate limit: 10s delay between API calls

**Agent 30 — Gap Audit & Verification**
- Focus: Check all agents' results against UNESCO regions + verify 20 random papers
- Tasks:
  1. Cross-reference compiled results against UNESCO cultural region list
  2. For any region with ZERO results: run 5 targeted searches
  3. Spot-check 20 random papers (arXiv pages exist, DOIs resolve, venues correct)
  4. Produce gap audit report: `logs/YYYYMMDD-cultural_coverage_gap_audit.md`
  5. Document confirmed voids (cultures with genuinely zero LLM benchmark work)

---

## Phase 2: Deduplication & Master List

### Step 1: Collect Agent Reports
- Each agent writes: `logs/20260213-cultural_search_agent_NN_REGION.md`
- Format follows existing template (see `logs/20260207-Agent9_11_NonWestern_Ethics_Report.md`)
- Each entry includes: Full Citation, arXiv, DOI, Framework, Dataset Details, Code/Data, LLMs Tested, Implementation Readiness, Cultural Focus

### Step 2: Three-Layer Deduplication
1. **Between agents:** arXiv ID exact match, DOI exact match, fuzzy title SequenceMatcher >= 0.90
2. **Against vault (846 papers):** Match on arXiv ID, DOI, normalized title
3. **Against previous master list (300 papers):** Catch papers from prior search that weren't imported

### Step 3: Compile Master List
- Output: `logs/20260213-CULTURAL_SEARCH_MASTER_LIST.md`
- Additional fields vs previous format: `Cultural Focus`, `Language(s)`

### Step 4: Cross-Verification (Agent 30)
- 20 random papers verified: arXiv exists, DOI resolves, venue/year correct
- Target: 0% hallucination rate

---

## Phase 3: Import Pipeline

Follows established workflow:

1. **Create paper .md files** — YAML frontmatter with `DATE_ADDED: 20260213`, `national_ethnic_cultural:` pre-populated from agent cultural focus
2. **PDF download** — `PYTHON/batch_download_pdfs.py` with 15-strategy waterfall from `PYTHON/comprehensive_pdf_finder.py`
3. **Text extraction** — `PYTHON/batch_extract_pdfs.py`
4. **Classification** — All 7 stages (classify_ethics → classify_cultural_religious → etc.)
5. **LLM Assessment enrichment** — `generate_llm_assessment_batches.py` + agent swarm
6. **Validation** — `../.venv/bin/python PYTHON/validate_all_papers.py`

---

## Phase 4: `cultures_nationalities_list` Field Enrichment (ALL Papers)

Add the new `cultures_nationalities_list` field to **every paper** in the vault — both the existing 846 and all newly imported papers. This is a comprehensive enrichment pass using the proven agent swarm pattern.

### 4.1 Field Specification

```yaml
# Example for a cross-cultural paper:
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Chinese, Japanese, Korean, American, German, French"

# Example for a single-culture paper:
national_ethnic_cultural: "Indian"
cultures_nationalities_list: "Indian"

# Example for a paper with no cultural focus:
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
```

**Granularity rules:**
- List every specific culture, nationality, or ethnic group the paper discusses, evaluates, or benchmarks
- Use the culture/nationality name (e.g., "Chinese", "Japanese", "Nigerian"), not the broad region (e.g., NOT "East Asian" unless the paper specifically discusses East Asia as a cultural unit)
- For cross-cultural papers, list ALL cultures individually (e.g., "Chinese, Japanese, Korean, American" not just "Multicultural")
- Use "N/A" if the paper has no cultural/national focus
- Separate entries with ", " (comma-space)
- Quote the entire value: `cultures_nationalities_list: "Chinese, Japanese"`

### 4.2 Batch Generation Script

**New script:** `PYTHON/generate_culture_list_batches.py`

Purpose: Scan all papers, identify those missing `cultures_nationalities_list`, split into balanced batches for agent processing.

```
Input:  papers/*.md (all papers in vault)
Output: logs/20260213-culture_list_batch_01.json ... batch_NN.json
        logs/20260213-culture_list_manifest.json
```

Each batch JSON contains ~20-25 papers with their:
- File path
- Title (from filename)
- `national_ethnic_cultural` value (existing classification — serves as hint)
- Abstract (first 500 chars, from YAML `abstract` field or body `## Abstract` section)

### 4.3 Agent Swarm Enrichment

**Pattern:** Same as LLM Assessment enrichment (proven at scale for 846 papers)

- **Total batches:** ~40 (846 papers ÷ ~22 per batch)
- **Agents per wave:** 5
- **Waves:** 8 (40 ÷ 5)
- **Each agent's task:**
  1. Read the paper's title, abstract, body text, and existing `national_ethnic_cultural` tag
  2. If PDF extract exists, scan it for country/culture mentions
  3. Determine ALL cultures and nationalities discussed in the paper
  4. Output: `{"file": "papers/2024-Author-Title.md", "cultures_nationalities_list": "Chinese, Korean, American"}`
- **Agent output:** `logs/20260213-culture_list_agent_NN.json`

**Extraction heuristics for agents:**
- Check title for culture/country names
- Check abstract for explicit country mentions, language names, survey populations
- Check body for benchmark names with known cultural associations (e.g., JBBQ → Japanese, KorNAT → Korean)
- Cross-reference the existing `national_ethnic_cultural` field but go MORE granular
- For papers with `national_ethnic_cultural: "N/A"` — still check if they mention specific populations (e.g., "we surveyed 500 American participants")

### 4.4 Consolidation Script

**New script:** `PYTHON/consolidate_culture_lists.py`

```
Input:  logs/20260213-culture_list_manifest.json → all agent JSON files
Output: logs/20260213-culture_list_consolidation.json
Action: Insert cultures_nationalities_list field into each paper's YAML
```

**YAML insertion method (safe regex — NEVER parse/rebuild):**
```python
# Insert after national_ethnic_cultural line
content, count = re.subn(
    r'^(national_ethnic_cultural:.*?)$',
    rf'\1\ncultures_nationalities_list: "{value}"',
    content,
    count=1,
    flags=re.MULTILINE
)
```

**Edge cases:**
- If `national_ethnic_cultural` is a YAML list (multi-line), insert after the last list item
- If paper already has `cultures_nationalities_list` (idempotency), replace it instead of inserting
- Use `value.replace('"', "'")` for values containing quotes (per YAML safety rules)

### 4.5 Validation

```bash
../.venv/bin/python PYTHON/validate_all_papers.py
```

Verify:
- All papers still pass validation
- No mismatched quotes introduced
- Spot-check 20 papers manually for accuracy of culture list

---

## Phase 5: Reports & Dashboard Update

1. **Regenerate vault overview report** — `PYTHON/generate_vault_overview_report.py`
2. **Regenerate dashboard** — `PYTHON/generate_vault_dashboard.py` (add cultural coverage visualization using new `cultures_nationalities_list` field)
3. **New cultural coverage report** — Document before/after paper counts by culture, leveraging the new granular field
4. **Update GitHub Pages dashboards** — Push to `cjimmylin/cei-dashboard` + `cei-dashboard-llm`
5. **Update `classify_cultural_religious.py`** — Add new `CULTURAL_PATTERNS` entries for any newly discovered cultures not in the current 25-pattern list (e.g., Turkish, Mongolian, Polish, etc.)

---

## Critical Files

| File | Purpose |
|---|---|
| `PYTHON/extract_and_dedup_papers.py` | Dedup script to extend with new agent reports |
| `PYTHON/classify_cultural_religious.py` | Cultural classification (add new patterns for newly discovered cultures) |
| `PYTHON/comprehensive_pdf_finder.py` | 15-strategy PDF waterfall |
| `PYTHON/batch_download_pdfs.py` | Parallel PDF download |
| `PYTHON/batch_extract_pdfs.py` | PDF text extraction |
| `PYTHON/validate_all_papers.py` | YAML validation |
| `PYTHON/generate_vault_dashboard.py` | Dashboard generation |
| `PYTHON/generate_vault_overview_report.py` | Overview report |
| `.agent/lib/yaml_utils.py` | Canonical YAML utilities |
| `.agent/lib/pdf_utils.py` | PDF path helpers |
| `PYTHON/generate_culture_list_batches.py` | **NEW** — Batch generator for culture list enrichment |
| `PYTHON/consolidate_culture_lists.py` | **NEW** — Consolidation script for culture list field insertion |
| `PYTHON/generate_llm_assessment_batches.py` | Template for batch generation pattern (reuse structure) |
| `PYTHON/consolidate_llm_assessments.py` | Template for consolidation pattern (reuse structure) |

---

## Execution Summary

| Step | Agents | Estimated Duration |
|---|---|---|
| Wave 1: East Asian | 5 agents (A1-A5) | ~45 min |
| Wave 2: South/SE Asian | 5 agents (A6-A10) | ~45 min |
| Wave 3: ME/Central Asian | 5 agents (A11-A15) | ~45 min |
| Wave 4: Africa/LatAm | 5 agents (A16-A20) | ~45 min |
| Wave 5: European | 5 agents (A21-A25) | ~45 min |
| Wave 6: Cross-cultural + Verify | 5 agents (A26-A30) | ~60 min |
| Dedup + Master list | Script | ~30 min |
| Import + PDF + Classify | Batch pipeline | ~2 hours |
| Culture list enrichment (846 + new) | ~40 agents, 8 waves | ~3 hours |
| Reports + Dashboard | Scripts | ~30 min |
| **Total** | **~70 agents** | **~10-11 hours** |

---

## Expected Outcomes

- **Estimated new papers:** 40-100 (narrower scope than broad search, but deeper per-culture)
- **Strongest yields expected:** Thai (ThaiCLI), Vietnamese (VMLU), Indonesian (IndoMMLU), Turkish (TurkBench), Korean (KMMLU-Pro), Eastern European (PLCC, CUS-QA)
- **Likely confirmed voids:** Central Asian, Pacific Islander, Caribbean, Sami — genuinely zero LLM cultural benchmark work exists

---

## Verification

After full pipeline completion:
1. `../.venv/bin/python PYTHON/validate_all_papers.py` — all papers pass
2. Verify ALL papers have `cultures_nationalities_list` field: `grep -rL "cultures_nationalities_list" papers/` should return empty
3. Spot-check 20 papers: culture list matches paper content
4. Before/after culture distribution comparison
5. Gap audit report confirms no major culture was missed
6. Dashboard shows updated cultural coverage with granular breakdown from new field
