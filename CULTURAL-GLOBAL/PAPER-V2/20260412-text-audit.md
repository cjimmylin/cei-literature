# Text Audit Report -- Cross-Cultural AI Values Alignment Paper v2

**Date:** 2026-04-12
**Scope:** All 16 text files (9 main body + 5 supplementary + introduction from PAPER/)
**Auditor Perspectives:** P7 Academic Copy Editing, P3 Statistical Communication, P4 Nature Portfolio Compliance

---

## 0. Word Counts

| File | Words |
|------|-------|
| 00-abstract.md | 523 |
| introduction-cultural-global.md (PAPER/) | 12,801 |
| 02-methods.md | 5,483 |
| 03-results-corpus.md | 4,148 |
| 04-results-benchmarks.md | 4,177 |
| 05-results-trials.md | 2,817 |
| 06-results-synthesis.md | 1,544 |
| 07-discussion.md | 3,199 |
| 08-conclusion.md | 1,021 |
| 09-references.md | 2,284 |
| supplementary/S1-methods.md | 1,193 |
| supplementary/S2-results.md | 1,200 |
| supplementary/S3-council.md | 1,325 |
| supplementary/S4-trial-protocols.md | 1,142 |
| supplementary/S5-keyword-lists.md | 539 |
| **Main body total (abstract through conclusion, excl. refs)** | **~35,713** |
| **Supplementary total** | **~5,399** |
| **Grand total (all files)** | **~43,396** |

**NHB note:** Nature Human Behaviour Articles typically accept 5,000--8,000 words for the main text (methods through conclusion), excluding abstract, references, and supplementary. The current main body (~35,700 words excl. abstract and refs, ~23,000 excl. introduction) far exceeds this. The introduction alone (12,801 words) is larger than many full NHB papers.

---

## 1. Terminology Inconsistencies: WEIRD Phrasing

### Standard term: "WEIRD bias"

| Phrasing | File | Line(s) | Verdict |
|----------|------|---------|---------|
| "WEIRD bias" | 00-abstract.md | 11, 13 | OK (standard) |
| "WEIRD bias" | 02-methods.md | 13 | OK |
| "WEIRD bias" | 05-results-trials.md | 109, 149 | OK |
| "WEIRD bias" | 07-discussion.md | 7 | OK |
| "WEIRD dominance" | 07-discussion.md | 15 | OK -- describes numerical overrepresentation ("overwhelming WEIRD dominance, the data reveal...") |
| "WEIRD skew" | Not found in PAPER-V2 files | -- | OK |

**Introduction file (not yet in PAPER-V2):**

| Phrasing | Line | Verdict |
|----------|------|---------|
| "WEIRD bias" | ~47 (Section 1.3) | OK |

**Finding:** Terminology is clean within PAPER-V2. The single "WEIRD dominance" usage in 07-discussion.md:15 is permissible under the stated rule (describing numerical overrepresentation). No "WEIRD skew" found in any PAPER-V2 file.

**CRITICAL: Introduction uses stale numbers.** Introduction (Section 1.3) reports "mean WEIRD score of 63.4" and "56.0% of papers scoring in the High-WEIRD range." All PAPER-V2 files use 64.5 and 59.7%. This is a data version mismatch that MUST be reconciled when the introduction is integrated.

---

## 2. Statistical Claims Catalog

### 2.1 Key Repeated Statistics -- Cross-Section Consistency Check

| Claim | Expected Value | Locations | Status |
|-------|---------------|-----------|--------|
| Paper count | 2,329 | abstract:5, methods:7/20, results-corpus:1, results-benchmarks:1, synthesis:3, discussion:7, conclusion:5 | CONSISTENT |
| Benchmark count | 218 | abstract:7, methods:138/140, results-benchmarks:1/38/46/132, synthesis:3, discussion:43, conclusion:5 | CONSISTENT |
| Item count | 380 | abstract:7, methods:176, results-trials:3/63, synthesis:3, conclusion:5 | CONSISTENT |
| Model count | 10 | abstract:7, methods:197, results-trials:3, synthesis:47 | CONSISTENT |
| Provider count | 3 | abstract:7, methods:197, results-trials:3 | CONSISTENT |
| I:B ratio | 3.75 | abstract:9, results-trials:37/39, synthesis (indirect), S2-results:95 | CONSISTENT |
| Effective N | ~5 | abstract:9 ("N approx 5"), methods:220-221, results-trials:129, synthesis:47 | CONSISTENT |
| RLHF conflict total | 237 | results-trials:63/65, handoff:94 | SEE ISSUE BELOW |
| Mean WEIRD score | 64.5 | abstract:9, methods:115, results-corpus:9, synthesis:3, conclusion:5 | CONSISTENT in V2 |
| High-WEIRD % | 59.7% | abstract:9, results-corpus:9 | CONSISTENT in V2 |
| Non-Western engagement | 6.9% (161 papers) | abstract:9, methods:62, synthesis:3, conclusion:5 | CONSISTENT |
| Precision-adjusted estimate | ~95 papers (4.1%) | abstract:9, conclusion:5 | CONSISTENT |
| Pairwise correlations | Opus--Sonnet 0.952, Opus--Haiku 0.915, Sonnet--Haiku 0.885 | results-trials:111 | Single source -- no cross-check available |
| North America + W. Europe % | 60.1% | abstract:9, results-corpus:22, synthesis:3/47, discussion:7, conclusion:5 | CONSISTENT |
| Zero measurement invariance | 0 of 218 | abstract:9, results-benchmarks:38, synthesis:3, discussion:43, conclusion:5 | CONSISTENT |
| Concept coverage | 3 of 44 (6.8%) | abstract:9, results-benchmarks:62, synthesis:3/11, conclusion:5 | CONSISTENT |
| Five traditions with zero concepts | 5 | abstract:9, results-benchmarks:77, synthesis:3, conclusion:5 | CONSISTENT |

### 2.2 CRITICAL: RLHF Conflict Count Arithmetic Error

**Table 8 (05-results-trials.md:67-76)** itemizes RLHF conflicts:

| Category | Count |
|----------|-------|
| Individual autonomy default | 51 |
| Secular epistemology | 35 |
| Consequentialist optimization | 31 |
| Anti-authority bias | 8 |
| Gender equality lock | 6 |
| Harm principle absolutism | 2 |
| Other (diverse) | 116 |
| **Sum** | **249** |

The table header says n = 237, but the rows sum to **249**. This is a 12-unit discrepancy.

Meanwhile, S2-results.md reports per-model RLHF conflicts:
- Opus: 277 (62 + 38 + 27 + 20 + 17 + 2 + 116 = **282**, another internal sum error; header says 277)
- Sonnet: 210 (44 + 28 + 24 + 12 + 9 + 1 + 111 = **229**, header says 210)
- Haiku: 216 (32 + 140 = **172**, header says 216, massive gap)

**Diagnosis:** The RLHF conflict counts are internally inconsistent at multiple levels. The main text claims 237 total but the table sums to 249. The supplementary per-model breakdowns also do not sum correctly. These must be reconciled against source data.

### 2.3 MFQ Table Approximations

In 05-results-trials.md:28-37, human baseline values are presented with "~" approximations:

| Value | Status |
|-------|--------|
| Human Liberal Mean ~3.5 (Care/Harm) | NEEDS exact citation -- Graham et al. 2009 Table values |
| Human Liberal Mean ~3.5 (Fairness) | Same |
| Human Conservative Mean ~3.0 (Care/Harm) | Same |
| Non-WEIRD Mean ~3.0 | NEEDS citation -- Atari et al. 2023? |
| Human Liberal Mean ~2.5 (binding foundations) | Same |
| Human Conservative Mean ~3.5 (binding) | Same |
| Non-WEIRD Mean ~3.5 (binding) | Same |
| Human Liberal I:B ratio 1.40 | Stated as approximate -- needs exact source |
| Non-WEIRD I:B ratio 0.86 | Same |

All 14 "~" cells in Table (05-results-trials.md) require exact values with citations.

### 2.4 RLHF Conflict Range in Methods vs. Results

02-methods.md:215 states "RLHF conflict counts varied from 196 to 277" for Tier 1 models.
05-results-trials.md:111 states "Opus 277, Haiku 216, Sonnet 210."
S2-results.md confirms the same per-model numbers.

**The range 196--277 (methods) does not match the actual values 210--277 (results).** The lower bound should be 210 (Sonnet), not 196.

### 2.5 Introduction vs. PAPER-V2 Number Conflicts

The introduction (PAPER/introduction-cultural-global.md) uses numbers from an earlier data run:

| Metric | Introduction value | PAPER-V2 value | Discrepancy |
|--------|-------------------|----------------|-------------|
| Mean WEIRD score | 63.4 | 64.5 | YES |
| High-WEIRD % | 56.0% | 59.7% | YES |
| High-WEIRD count | 1,296 (implied) | 1,221 | YES |

These MUST be harmonized before integration.

---

## 3. Cross-Reference Verification

### 3.1 Figure References

| Reference | File:Line | Resolves? | Notes |
|-----------|-----------|-----------|-------|
| Fig. 1 | results-corpus:9 | YES | world-map-weird.png exists in figures/ |
| Fig. 2 | results-corpus:47 | YES | heatmap-regions-frameworks.png |
| Fig. 3 | results-corpus:55 | YES | dendrogram.png |
| Fig. 4 | results-corpus:89 | YES | correspondence-biplot.png |
| Fig. 5 | results-benchmarks:28 | YES | benchmark-landscape-clusters.png |
| Fig. 6 | results-benchmarks:77 | YES | concept-coverage-gaps.png |
| Fig. 7 | results-trials:22 | YES | cultural-map-position.png |
| Fig. 8 | results-trials:39 | YES | mfq-profile-comparison.png |
| Fig. 9 | results-trials:83 | YES | rlhf-conflict-taxonomy.png |
| Fig. 10 | synthesis:17 | YES | triple-bind-diagram.png |
| Fig. S1 | methods:22 | UNVERIFIED | Referenced in text, needs supp-figures/ check |
| Fig. S2 | methods:115, results-corpus:78 | UNVERIFIED | Referenced in text |
| Fig. S7 | results-corpus:144 | UNVERIFIED | Referenced in text |

**Issue:** Supplementary figure references (S1, S2, S7) need verification against supp-figures/ directory contents.

### 3.2 Table References

| Reference | File | Resolves? | Notes |
|-----------|------|-----------|-------|
| Table 1 (Methods) | 02-methods.md:50 | YES | NW framework scoring instruments |
| Table 1 (Results) | 03-results-corpus.md:24 | CONFLICT | Geographic distribution -- same number as Methods Table 1 |
| Table 2 (Methods) | 02-methods.md:70 | YES | Gold standard validation |
| Table 2 (Results) | 03-results-corpus.md:11 | CONFLICT | WEIRD tier distribution -- same number as Methods Table 2 |
| Table 3 (Methods) | 02-methods.md:91 | YES | Geography resolution |
| Table 3 (Results) | 03-results-corpus.md:113 | CONFLICT | Representation index -- same as Methods Table 3 |
| Table 4 (Methods) | 02-methods.md:178 | YES | Trial battery |
| Table 4 (Results) | 04-results-benchmarks.md:64 | CONFLICT | Concept coverage matrix -- same as Methods Table 4 |
| Table 5 | 04-results-benchmarks.md:160 | YES | Top 10 benchmarks |
| Table 6 | 04-results-benchmarks.md:113 | YES | Benchmark geography -- but appears BEFORE Table 5 in text |
| Table 7 | 05-results-trials.md:9 | YES | Cultural distance profile |
| Table 8 | 05-results-trials.md:65 | YES | RLHF conflict taxonomy |
| Table 9 | 05-results-trials.md:117, 129 | MISSING | Referenced twice but no table body provided |
| Table 10 | 06-results-synthesis.md:27 | YES | Gap compounding |
| S-Table S1 | 02-methods.md:44 | UNVERIFIED | Referenced, not in supplementary |
| S-Table S2 | 02-methods.md:48 | UNVERIFIED | Referenced |
| S-Table S3 | 02-methods.md:144, S1-methods.md:127 | UNVERIFIED | Referenced |
| S-Table S4 | 02-methods.md:226 | UNVERIFIED | Referenced |

**CRITICAL ISSUES:**
1. **Table numbering collision:** Tables 1-4 are used in BOTH 02-methods.md and 03-results-corpus.md / 04-results-benchmarks.md. The paper has duplicate Table 1, duplicate Table 2, duplicate Table 3, and duplicate Table 4.
2. **Table 5 and 6 out of order:** Table 6 (benchmarks:113) appears before Table 5 (benchmarks:160) in the text.
3. **Table 9 missing:** Referenced at results-trials:117 and :129 but no table body exists.

### 3.3 Section References

| Reference | File:Line | Resolves? | Notes |
|-----------|-----------|-----------|-------|
| Section 2.2.3 | methods:26 | YES | |
| Section 2.2.4 | methods:32 | YES | |
| Section 2.2.5 | methods:48, 66, 255 | YES | |
| Section 2.4 | introduction:8 | NO -- refers to v1 structure | The introduction references "Section 2.4" for tradition depth but PAPER-V2 methods has different numbering |
| Section 2.4.4 | methods:213, results-trials:103 | YES | |
| Section 2.5 | methods:228, 233 | YES | |
| Section 2.6 | methods:101, 228 | YES | |
| Section 2.7 | methods:255, S3-council:65 | YES | |
| Section 2.8 | methods:209 | YES | |
| Sections 3--5 | methods:62 | PARTIALLY | Sections are numbered 3-8, not 3-5 |
| Section 3.2.3 | introduction:12 | NO | V1 numbering -- no Section 3.2.3 in PAPER-V2 |
| Section 4 | methods:22 | YES | |
| Section 4.3 | synthesis:11 | YES | |
| Section 4.6 | S3-council:11 | YES | |
| Section 4.7 | results-benchmarks:155 | YES | |
| Section 5.3 | results-trials:145 | YES | |
| Section 5.4 | synthesis:19 | YES | But 5.4 = RLHF Conflict Taxonomy, not knowledge gap |
| Section 5.5 | synthesis:21 | YES | |
| Section 6 | synthesis:title | YES | |
| Section 7.2 | discussion:61 | YES | |
| Section 7.7 | S3-council:29, discussion:59 | YES | |
| Section 7.9 | S3-council:55 | YES | |
| Section 3.7 | discussion:121, results-corpus:147 | YES | |
| Section 3.2 | results-corpus:47 | AMBIGUOUS | Could mean 3.2 or Section 2 gold standard |

**Issues with introduction cross-references:** The introduction uses v1 section numbers (2.4, 3.2.3, Section 3) that do not match PAPER-V2 structure.

---

## 4. Citation Verification

### 4.1 In-Text Citations Found in Main Body (not in 09-references.md)

The following citations appear in the main text but are MISSING from the reference list:

| Citation | File | Notes |
|----------|------|-------|
| Vandenberg and Lance 2000 | 04-results-benchmarks.md:40 | MI reference |
| Chen 2007 | 04-results-benchmarks.md:40 | MI reference |
| International Test Commission 2017 | 04-results-benchmarks.md:56 | Guidelines reference |
| Madaio et al. 2020 | introduction:112 | Organizational fieldwork |
| Eickhoff 2026 | 04-results-benchmarks.md:99 | UbuntuGuard |
| Ogunremi 2025 | 04-results-benchmarks.md:99 | Decolonizing NLP |
| Lahmar 2025 | 04-results-benchmarks.md:87 | IslamTrust |
| Farsi 2025 | 04-results-benchmarks.md:87 | MELAC |
| Xiong 2025 | 04-results-benchmarks.md:91 | BuddhismEval |
| Wong 2024 (HBC) | 04-results-benchmarks.md:91/186 | Humanistic Buddhism -- distinct from Wong 2024 in refs? |
| Ray 2025 | 04-results-benchmarks.md:95/164 | Indigenous Knowledge Systems |
| Neira-Davila 2025 | 04-results-benchmarks.md:95/185 | Indigenous Latin American |
| Agarwal 2025 | 04-results-benchmarks.md:103 | Fluent but Foreign |
| Rao 2025 | 04-results-benchmarks.md:181 | NormAd -- as "Rao et al. 2025" |
| Rahman 2025 | 04-results-benchmarks.md:182 | CCD-Bench |
| Catapang 2023 | 04-results-benchmarks.md:183 | EMoTES-3K |
| Keutzer 2025 | 04-results-benchmarks.md:184 | MITRA-zh-eval |
| Held 2006 | 03-results-corpus.md:134 | Care ethics -- IS in refs |

Note: Held 2006 IS present in references. The benchmark-specific citations (Lahmar, Farsi, Xiong, Ray, Neira-Davila, Agarwal, Rao, Rahman, Catapang, Keutzer, Eickhoff, Ogunremi) are extensively cited in Section 4 but none appear in 09-references.md. This is a **major gap** -- approximately 15 benchmark references are missing.

### 4.2 Orphaned References (in reference list but not cited in main/supp text)

The following appear in 09-references.md but were NOT found cited in any PAPER-V2 file:

| Reference | Notes |
|-----------|-------|
| Abdalla & Abdalla 2021 | Grey Hoodie Project |
| Adams & Balfour 2024 | Pluralistic alignment |
| Alyemny 2023a, 2023b | FatwaSet |
| Apicella et al. 2020 | Beyond WEIRD |
| Benzecri 1992 | Correspondence analysis |
| Chouldechova 2017 | Fair prediction |
| Ciston 2023 | ML datasets |
| Couldry & Mejias 2019 | Data colonialism |
| Deckker & Sumanasekara 2025 | Buddhist AI |
| Deng 2024 | Chinese AI governance |
| Dobbe & Marda 2024 | AI governance Global South |
| Gilligan 1982 | Different Voice |
| Gorian & Osman 2024 | Saudi/UAE ethics |
| Greenacre 2017 | Correspondence analysis |
| Grosfoguel 2013 | Epistemic racism |
| Gudynas 2011 | Buen Vivir |
| Gyekye 1997 | African philosophy |
| Hanna et al. 2020 | Critical race methodology |
| Harvey 2000 | Buddhist ethics |
| Hofstede 2001 | Culture's Consequences |
| Hongladarom 2020 | Buddhist AI ethics |
| Hou 2023 | Confucian AI |
| Hwang & Yoon 1981 | TOPSIS -- cited only in S1-methods |
| Islam 2022 | Anekantavada |
| Kamali 2008 | Maqasid |
| Keown 2005 | Buddhist ethics |
| Kleinberg et al. 2016 | Fair risk scores |
| Kukutai & Taylor 2016 | Indigenous data sovereignty |
| Kushwaha 2026 | Syadvada AI |
| Li 2006, 2014 | Confucian harmony |
| Macas 2010 | Sumak kawsay |
| MacIntyre 1981 | After Virtue |
| Menkiti 1984 | African personhood |
| Metz 2007 | African moral theory |
| Miao 2026 | Buddhist AI compassion |
| Mokoena 2024 | Ubuntu AI ethics |
| Munn 2023 | Five tests |
| Nagel 1986 | View from Nowhere |
| Praeg 2014 | Report on Ubuntu |
| Qian 2023 | Chinese moral stories |
| Quijano 2000 | Coloniality |
| Ramose 1999 | Ubuntu philosophy |
| Ranganathan 2022 | Hindu philosophy |
| Roy & Bouyssou 1993 | ELECTRE III -- cited only in S1-methods |
| Sandel 1982 | Liberalism |
| Selbst et al. 2019 | Fairness abstraction |
| Smith 2012 | Decolonizing methodologies |
| So 2024 | Confucian AI training |
| Suliman 2024 | Ubuntu AI governance |
| Tacheva & Ramasubramanian 2023 | AI empire |
| Talat et al. 2022 | ML ethical judgments |
| Usmonov 2025 | AI fatwas |
| van de Vijver & Leung 1997 | Cross-cultural methods |
| van Norren 2020 | Ubuntu AI ethics |
| Varshney 2024 | Decolonial AI alignment |
| Villalba 2013 | Buen Vivir |
| Walsh 2010 | Buen Vivir |
| Wiredu 1996 | Cultural universals |
| Yao & Lu 2023 | Chinese AI ethics |
| Zhang & Dafoe 2019 | American AI attitudes |
| Zimerman & Tomsett 2023 | Cross-cultural fairness |
| Zuboff 2019 | Surveillance capitalism |

**Finding:** Many of these orphaned references were likely cited in the introduction (which is the v1 introduction, not yet integrated). Others may have been cited in an earlier draft but removed during the v2 rewrite. The reference list needs thorough pruning and updating to match the final combined text.

---

## 5. Anti-Essentialization Check

### 5.1 PAPER-V2 Files

Searched for patterns: "[tradition] holds", "[tradition] says", "[tradition] believes", "[culture] values".

**Results within PAPER-V2 text files:** Only one match found, and it is a META-REFERENCE to the anti-essentialization rule itself:

- S3-council.md:37 -- "never 'Islam holds X' or 'Confucianism says X'" (describing the rule, not violating it)

**No violations found in PAPER-V2 main body or supplementary files.** The anti-essentialization protocol has been well enforced.

### 5.2 Introduction File (PAPER/)

No violations of the "[tradition] holds/says/believes" pattern found in the introduction.

The introduction does use acceptable formulations:
- "A Confucian ethicist would insist..." (line 6)
- "An Ubuntu-oriented philosopher might argue..." (line 6)
- "A scholar of Islamic ethics would ask..." (line 6)
- "A practitioner of buen vivir would find..." (line 7)

These are person-framed rather than tradition-framed and comply with the protocol.

---

## 6. Missing NHB Submission Components

Nature Human Behaviour requires the following elements. Status for this manuscript:

| Component | Status | Notes |
|-----------|--------|-------|
| Title page with all authors | MISSING | No author list anywhere |
| Corresponding author designation | MISSING | |
| Abstract (150 words, unstructured) | NON-COMPLIANT | Current is 523 words, structured with bold headers |
| Introduction | PRESENT (in PAPER/) | But not yet in PAPER-V2 directory |
| Methods | PRESENT | |
| Results | PRESENT | |
| Discussion | PRESENT | |
| References | PRESENT | But incomplete (see Section 4) |
| Figure legends | PARTIALLY PRESENT | Captions exist but not in NHB format |
| Data availability statement | MISSING | Required by NHB |
| Code availability statement | MISSING | Required by NHB |
| Ethics statement / IRB | MISSING | Required -- self-administration to LLMs may need IRB exemption statement |
| Competing interests declaration | MISSING | Required |
| Author contributions (CRediT) | MISSING | Required by NHB |
| Acknowledgments | MISSING | Required |
| Extended Data (distinct from Supplementary) | NOT STRUCTURED | NHB distinguishes Extended Data (peer-reviewed, up to 10 items) from Supplementary Information |
| Reporting Summary checklist | MISSING | NHB requires completed checklist |
| Life sciences reporting summary | LIKELY N/A | Social sciences -- but NHB may require specific checklist |
| ORCID for all authors | MISSING | |
| Supplementary Information cover page | MISSING | |

---

## 7. Abstract Assessment

**Current state:** 523 words, structured with four bold section headers (Background, Methods, Results, Conclusions) plus Keywords line.

**NHB requirement:** 150 words maximum, single unstructured paragraph, no headers, no keywords in abstract.

**Gap:** The abstract must be cut by approximately 70% (from 523 to 150 words). The structured format must be converted to a single flowing paragraph. Keywords should be moved to a separate keywords field per NHB template.

**Recommendation:** Draft a 150-word version that preserves the "triple bind" framing and the three key numbers (2,329/218/380). The current abstract reads well as a standalone summary but is categorically non-compliant with NHB format.

---

## 8. Additional Issues Identified

### 8.1 Table Numbering System is Broken

Tables 1-4 appear in BOTH the Methods (Section 2) and Results (Sections 3-4), creating duplicate numbers:
- Table 1: Methods (NW frameworks) AND Results-Corpus (geographic distribution)
- Table 2: Methods (gold standard) AND Results-Corpus (WEIRD tiers)
- Table 3: Methods (geography pipeline) AND Results-Corpus (representation index)
- Table 4: Methods (trial battery) AND Results-Benchmarks (concept coverage)

Additionally, Tables 5 and 6 appear out of order in 04-results-benchmarks.md (Table 6 at line 113, Table 5 at line 160).

Table 9 is referenced (results-trials:117, :129) but has no content.

**Action required:** Renumber all tables sequentially from Table 1 through the paper.

### 8.2 Section Numbering Gap

There is no Section 1 (Introduction) file in PAPER-V2. The numbering jumps from 00-abstract.md to 02-methods.md. The introduction exists in PAPER/ with Section 1 numbering but has not been moved to PAPER-V2. This creates section-reference mismatches.

### 8.3 MENA Classification Inconsistency

02-methods.md:101 classifies MENA as part of the "Ambiguous" category:
> "Ambiguous (East Asia, MENA, Southeast Asia, Eastern Europe and Central Asia)"

03-results-corpus.md:34 classifies MENA as "Global South" in Table 1.

These are contradictory. The methods section groups MENA with "Ambiguous" but the results table assigns it to "Global South."

### 8.4 "Sections 3--5" Reference

02-methods.md:62 says "precision-adjusted estimates are reported alongside raw counts throughout the results sections (Sections 3--5)." But the results sections are 3, 4, 5, AND 6. This should read "Sections 3--6."

### 8.5 Supplementary S2 Reference to "Fig. S2" / "Fig. S7"

- results-corpus.md:78 references "Fig. S2 in the supplementary materials" (silhouette analysis)
- results-corpus.md:144 references "Fig. S7 in the supplementary materials" (geographic visualization)

Neither S2-results.md nor any supplementary file provides these figures. The supp-figures/ directory exists but its contents were not enumerated.

### 8.6 Synthesis Section References Incorrect Section Numbers

06-results-synthesis.md:11 says "the optimization target was constructed within a normative universe where that position is the unmarked default (Section 5)." Section 5 is results-trials, which is correct.

06-results-synthesis.md:19 says "the benchmarks most used for LLM evaluation... frame moral reasoning as individual welfare calculation: GlobalOpinionQA... (Section 4.1)." Section 4.1 is correct.

These are fine. But:
06-results-synthesis.md:3 refers to "fewer than 15% of surveyed countries" -- the actual text in results-trials says "fewer than 15% of the global population" (05-results-trials.md:22). "Surveyed countries" vs. "global population" is a factual difference.

### 8.7 Opus RLHF Conflict Count Discrepancy

- 02-methods.md:215 says Tier 1 RLHF counts range from "196 to 277"
- 05-results-trials.md:111 says "Opus 277, Haiku 216, Sonnet 210"
- The minimum is 210 (Sonnet), not 196

### 8.8 "Five entire traditions" Wording Inconsistency

- abstract:9 lists "Islamic, Dharmic, Buddhist, Indigenous, Buen Vivir" (5 traditions)
- conclusion:5 lists the same 5
- results-benchmarks.md:77 says "Four entire traditions---Islamic ethics, Dharmic ethics, Buddhist ethics, and Indigenous relational ethics---have zero measured concepts. Buen Vivir, with zero as well, brings the total to five"

These are consistent in substance but the two-step phrasing in results-benchmarks is slightly misleading on first read (says "four" then corrects to "five").

### 8.9 Gwagwa et al. Reference Has Encoding Error

09-references.md:85:
> `Gwagwa, A., Kraemer-Mbula, E., Rizk, N.,"; I., & De Beer, J. (2022).`

The `"; I.` appears to be a corrupted author name (likely `Rutenberg, I.` or similar). This needs correction.

### 8.10 "Table 2" Collision Between Methods and Results

02-methods.md defines "Table 2" as the gold standard validation table.
03-results-corpus.md:11 also defines "Table 2" as the WEIRD tier distribution table.
A reader encountering "Table 2" in the text would not know which is meant.

---

## 9. Summary of Critical Issues

| Priority | Issue | Section |
|----------|-------|---------|
| P0 | RLHF conflict count arithmetic error (237 vs 249 sum) | 2.2 |
| P0 | Table numbering collisions (Tables 1-4 duplicated) | 8.1 |
| P0 | ~15 benchmark citations missing from reference list | 4.1 |
| P0 | Abstract 523 words vs NHB 150-word limit | 7 |
| P0 | Missing NHB components (CRediT, data/code availability, ethics, etc.) | 6 |
| P1 | Introduction uses stale numbers (63.4 vs 64.5, 56.0% vs 59.7%) | 2.5 |
| P1 | MENA classified as both "Ambiguous" and "Global South" | 8.3 |
| P1 | Table 9 referenced but missing | 3.2 |
| P1 | Tables 5 and 6 out of order | 3.2 |
| P1 | RLHF range 196-277 in methods vs actual 210-277 | 8.7 |
| P1 | Per-model RLHF sub-category sums do not match totals (S2-results) | 2.2 |
| P1 | Gwagwa et al. reference has encoding corruption | 8.9 |
| P1 | "Sections 3--5" should be "Sections 3--6" | 8.4 |
| P1 | Synthesis says "15% of surveyed countries" vs trials "15% of global population" | 8.6 |
| P2 | ~50 orphaned references need pruning or re-citation | 4.2 |
| P2 | MFQ table has 14 approximate ("~") values needing exact citations | 2.3 |
| P2 | Introduction section cross-references use v1 numbering | 3.3 |
| P2 | Word count far exceeds NHB limits (~35K vs 5-8K) | 0 |
| P2 | Supplementary figures S1, S2, S7 referenced but not verified | 3.1 |
| P3 | Section 1 (Introduction) not yet in PAPER-V2 | 8.2 |

---

## Phase 2: Cross-Review

**Date:** 2026-04-12
**Perspectives:** P2 (Anti-Essentialization), P9 (Non-Western Philosophy Content), P6 (Narrative Structure)
**Scope:** Cross-review of Phase 1 text audit + content expansion blueprint

---

### CR-1. Anti-Essentialization Review of Expansion Blueprint

Each expansion point in the content expansion blueprint was reviewed for essentialization violations (using "[tradition] holds/believes" instead of "scholars within X argue").

#### APPROVED Expansions

| Expansion | Verdict | Notes |
|-----------|---------|-------|
| 5.3 CC8 item-level examples (+195 words) | APPROVED | Model self-description; no tradition-level claims. The *guanxi* example says "Guanxi carries obligations that are not optional" -- this describes a conceptual feature, not a cultural monolith claim. Acceptable. |
| 5.5 CC10 walk-through scenarios (+240 words) | APPROVED | Perspectives attributed to frameworks ("Islamic," "Ubuntu," "Indigenous"), not to peoples. The phrasing "the Indigenous position that..." is borderline but acceptable in context since it describes one articulated perspective within a multi-perspective scenario, not a claim about all Indigenous peoples. |
| 5.7 Islamic ethics sentence | APPROVED | Uses "scholars within Islamic jurisprudence argue." Fully compliant. |
| 5.7 Confucian ethics sentence | APPROVED | Uses "scholars within Confucian philosophy argue." Compliant. |
| 5.7 Ubuntu ethics sentence | APPROVED | Uses "scholars within Ubuntu philosophy argue." Compliant. |
| 5.7 Buddhist ethics sentence | APPROVED | Uses "scholars within Buddhist philosophy argue." Compliant. |
| 5.7 Dharmic ethics sentence | APPROVED | Uses "scholars within Dharmic traditions argue." Compliant. |
| 6.2 Ubuntu cycle illustration (+205 words) | APPROVED | Uses "Scholars within Ubuntu philosophy have argued" and cites Metz 2007 and Gyekye 1997. Compliant. |
| 6.3 Interpretive sentence (+85 words) | APPROVED | Structural argument about model behavior. N/A for anti-essentialization. |
| 6.4 Closing sentence (+53 words) | APPROVED | Structural argument. N/A. |
| 7.5 MI pipeline (+500 words) | APPROVED | Entirely methodological. No tradition-specific claims. |
| 7.6 Open questions (+110 words) | APPROVED | Uses "tradition-internal scholars." Framed as open questions. Compliant. |
| 7.7 EU AI Act/UNESCO (+210 words) | APPROVED | Uses conditional formulations ("a risk framework grounded in Ubuntu communal ethics *might*..."). Critiques governance instruments, not cultures. Compliant. |
| 7.9 Limitations (+195 words) | APPROVED | Uses "scholars within oral traditions" and "scholars positioned within each tradition." Compliant. |

#### FLAGGED (Not Rejected, Requires Minor Revision)

| Expansion | Issue | Recommended Fix |
|-----------|-------|-----------------|
| 7.2 Alignment architecture implications (+355 words) | The phrase "A Confucian-relational alignment approach would require the model to represent relational context as a first-class variable" is acceptable as a design implication of a *framework*, not a claim about Chinese people. However, "An Islamic-jurisprudential approach would require the model to reason through established interpretive methods" could be read as implying a monolithic method. Islamic jurisprudence contains multiple schools (*madhahib*) with divergent methods. | Add qualifier: "An Islamic-jurisprudential approach -- drawing on methods recognized across the major *madhahib* -- would require..." or simply "An alignment approach informed by Islamic jurisprudence would require..." |
| 7.2 (continued) | The Indigenous paragraph uses "scholars within Indigenous knowledge systems call 'data sovereignty'" with a proper citation (Carroll et al. 2020). Compliant. No change needed. | -- |

#### Summary: 13 of 14 expansion points fully APPROVED. 1 flagged for minor qualifier addition (7.2 Islamic-jurisprudential). Zero rejections.

---

### CR-2. Introduction Rewrite Scope Validation

#### 2a. Section 1.5 (Research Questions) -- Three-Study Framing

**CONFIRMED: Needs revision.** The blueprint correctly identifies that RQs 1-5 map to Study 1 (corpus) and partially Study 2, but no RQ addresses Study 3 (model behavior trials) or the Triple Bind synthesis. The blueprint's recommendation to add RQ6 (model behavior) and RQ7 (Triple Bind) is sound and necessary. Without these, the introduction promises a corpus study but the paper delivers three studies. This is a coherence gap that readers and reviewers will catch.

**Additional concern (P6 narrative structure):** The five existing RQs are organized under description/explanation/evaluation. RQ6 and RQ7 should be framed under a fourth category -- perhaps "Interaction" or "Integration" -- to signal the paper's distinctive contribution (the three-layer compounding argument). Simply appending RQs 6-7 to the existing list without a structural label will make them feel tacked on.

#### 2b. Section 1.7 (Roadmap) -- Paper Structure Match

**CONFIRMED: Must be rewritten.** The current roadmap says "Sections 4 through 7 present results organized by research question" -- but PAPER-V2 uses Sections 3-5 for Studies 1-3, Section 6 for synthesis, Section 7 for discussion, and Section 8 for conclusion. The blueprint's proposed roadmap mapping is correct and should be implemented.

#### 2c. "Triple Bind" Introduction Timing

**CONFIRMED: Must be introduced earlier.** The term "Triple Bind" appears in the paper's title but is never used in the 12,801-word introduction. It first appears in Section 6 (06-results-synthesis.md). The blueprint recommends adding 2-3 sentences to the end of Section 1.1. This is the right location -- the "Triple Bind" is the paper's central thesis and must be previewed in the opening section. Delaying it to Section 6 makes it look like a post-hoc label rather than an organizing framework.

**P6 recommendation:** The Triple Bind should also appear in Section 1.4 (The Gap), where the three-dimensional gap is already described. The three dimensions of the gap (no WEIRD instrument, no NW framework taxonomy, no empirical baseline) map imperfectly onto the Triple Bind's three layers (WEIRD scholarship, broken benchmarks, monocultural models). This is a potential source of reader confusion. The introduction should either (a) explicitly connect the three gap dimensions to the three bind layers, or (b) acknowledge that the gap framing and the Triple Bind framing are complementary but distinct.

#### 2d. "20-Member Council" References

**CONFIRMED: No issue in the introduction text itself.** The introduction uses "twelve-member expert council" consistently. However, the v1 abstract (PAPER/00-abstract.md, line 7) still says "A 20-member expert council" and the v1 methodology (PAPER/03-methodology.md, line 131) says "A 20-member interdisciplinary expert council." These are in the PAPER/ directory (v1), not PAPER-V2/, so they are not in the active manuscript. But when the introduction is migrated from PAPER/ to PAPER-V2/, the accompanying v1 abstract must NOT be carried over -- the PAPER-V2/00-abstract.md already uses "12-member." The blueprint correctly identified no issue, but the migration step needs care.

#### 2e. Additional Introduction Issue -- Literature Review Duplication

The introduction file (PAPER/introduction-cultural-global.md) contains Section 2 (Literature Review) starting at line 81, running through at least line 150 (where reading was cut off). PAPER-V2/02-methods.md starts at Section 2 (Methods). If the introduction is migrated as-is, there will be a conflict: the introduction's Section 2 (Literature Review) will collide with PAPER-V2's Section 2 (Methods). The literature review content must either be folded into the introduction proper (making Section 1 longer) or renumbered.

---

### CR-3. Text Audit P0 Issue Validation

#### 3a. RLHF Conflict Count Arithmetic (249 vs 237)

**VERIFIED: Real arithmetic error.** Independent summation of Table 8 rows: 51 + 35 + 31 + 8 + 6 + 2 + 116 = 249. The header states n = 237. The 12-unit discrepancy is confirmed.

The per-model breakdowns in S2-results.md are even more severely inconsistent:

| Model | Header Total | Row Sum | Discrepancy |
|-------|-------------|---------|-------------|
| Opus | 277 | 62+38+27+20+17+2+116 = 282 | +5 |
| Sonnet | 210 | 44+28+24+12+9+1+111 = 229 | +19 |
| Haiku | 216 | 32+140 = 172 | -44 |

Haiku's breakdown is catastrophically incomplete -- only 2 of 7 categories are listed, and they sum to 172, not 216. This suggests the Haiku per-category data was never fully generated or was truncated.

**Cross-check:** The Opus-Sonnet-Haiku totals (277 + 210 + 216 = 703) should relate to the aggregate 237 (or 249) somehow, but 703/3 = 234.3, which is close to 237 but not exact. If 237 represents *unique* conflicts (not per-model totals), the relationship is unclear from the text. The methods text also says "196 to 277" as the RLHF range but the actual minimum is 210 (Sonnet), confirming a third inconsistency.

**Assessment:** This requires computational reproduction from source data. The audit correctly flagged this as P0.

#### 3b. Table Numbering Collisions

**VERIFIED.** All four collisions confirmed by grep:

- Table 1: methods.md:50 (NW framework instruments) AND results-corpus.md:24 (geographic distribution)
- Table 2: methods.md:70 (gold standard validation) AND results-corpus.md:11 (WEIRD tiers)
- Table 3: methods.md:91 (geography pipeline) AND results-corpus.md:113 (representation index)
- Table 4: methods.md:178 (trial battery) AND results-benchmarks.md:64 (concept coverage)

Additionally confirmed: Table 6 (benchmarks.md:113) appears BEFORE Table 5 (benchmarks.md:160), creating an out-of-order presentation.

Table 9 is referenced at results-trials.md:117 and :129 but has no table body. This is a missing artifact.

**Recommendation:** Renumber all tables sequentially. Methods Tables 1-4 become Tables 1-4; Results-Corpus Tables become 5-7; Results-Benchmarks Tables become 8-10 (fixing the 5/6 order swap); Results-Trials Tables become 11-12; Synthesis Table becomes 13. Table 9 (the missing one) must either be created or its references removed.

#### 3c. Missing Citations (Sample Verification)

**VERIFIED (sample of 5).** Checked against 09-references.md:

| Citation | In main text? | In references? | Status |
|----------|--------------|----------------|--------|
| Vandenberg and Lance 2000 | YES (benchmarks:40) | NO | MISSING |
| Lahmar 2025 (IslamTrust) | YES (benchmarks:87) | NO | MISSING |
| Xiong 2025 (BuddhismEval) | YES (benchmarks:91) | NO | MISSING |
| Ray 2025 (Indigenous KS) | YES (benchmarks:95, 164) | NO | MISSING |
| Agarwal 2025 (Fluent but Foreign) | YES (benchmarks:103) | NO | MISSING |

All 5 sampled missing citations are confirmed missing. The audit's count of ~15 missing benchmark references is credible and likely conservative (the full benchmark section cites many works not in the reference list).

---

### CR-4. Terminology Decisions

**VERIFIED.** "WEIRD dominance" appears only at 07-discussion.md:15, in the phrase "overwhelming WEIRD dominance, the data reveal..." This describes quantitative overrepresentation (numerical dominance in the corpus) and is the correct term for that context. All other instances use "WEIRD bias." The audit's recommendation to retain "WEIRD dominance" only at this location is correct.

**Additional terminology note (P9):** The phrase "WEIRD skew" does not appear in any PAPER-V2 file, which is good -- "skew" implies mere statistical imbalance whereas the paper argues for structural exclusion. The terminology is disciplined.

---

### CR-5. Additional Issues Found by Cross-Review

#### 5a. MENA Classification Inconsistency (P9 Concern)

The audit flagged this at 8.3 but it deserves escalation. Methods (02-methods.md:101) classifies MENA as "Ambiguous" but the results table (03-results-corpus.md:34) classifies it as "Global South." This is not just a labeling inconsistency -- it affects the paper's substantive claims about Global North vs. Global South representation. If MENA's 113 papers move from "Global South" to "Ambiguous," the Global South share drops materially. The paper's narrative depends on this classification. **Recommend: Escalate from P1 to P0 and resolve explicitly in the methods section with a justification for whichever classification is chosen.**

#### 5b. Orphaned Non-Western Philosophy References (P9 Concern)

The audit found ~50 orphaned references. Many of these are the paper's most important non-Western philosophy citations: Gyekye 1997 (African philosophy), Menkiti 1984 (African personhood), Metz 2007 (African moral theory), Ramose 1999 (Ubuntu), Wiredu 1996 (cultural universals), Li 2006/2014 (Confucian harmony), Kamali 2008 (Maqasid), Harvey 2000 and Keown 2005 (Buddhist ethics), Ranganathan 2022 (Hindu philosophy), Gudynas 2011 and Villalba 2013 (Buen Vivir), Kukutai & Taylor 2016 (Indigenous data sovereignty).

These references are likely cited in the introduction's literature review (Section 2 of the PAPER/ file, which was not fully scanned). When the introduction is migrated, most should resolve. However, there is a risk that the v2 rewrite dropped citations from the main body that the v1 had. **Recommend: After introduction migration, re-run orphaned reference check. Any non-Western philosophy reference that remains orphaned should be re-cited somewhere, because the removal of these citations from a paper about cross-cultural inclusion would be self-undermining.**

#### 5c. "Sections 3--5" Should Be "Sections 3--6" (P6 Concern)

The audit flagged methods.md:62 saying "Sections 3--5" when results span Sections 3-6. This is a narrative structure error: it excludes the Triple Bind synthesis (Section 6) from the results umbrella, which contradicts the paper's argument that the synthesis is empirical (not just interpretive). **Recommend: Change to "Sections 3--6."**

#### 5d. Synthesis "15% of Surveyed Countries" vs. "15% of Global Population" (P6 Concern)

The audit correctly flagged this at 8.6. "Surveyed countries" and "global population" are different denominators with different implications. If the trials cover fewer than 15% of surveyed countries, that is a coverage claim. If the trials represent fewer than 15% of the global population, that is a representativeness claim. These are not interchangeable. **Recommend: Verify the original statistic in 05-results-trials.md and align the synthesis language.**

#### 5e. Introduction Section 1.6 Contributions -- Missing Study 3 (P6 Concern)

The blueprint correctly identifies that the four listed contributions omit the model behavior study (Study 3) and the Triple Bind synthesis. This is a major narrative gap: the paper's most novel contribution (demonstrating that models compound the biases of scholarship and benchmarks into a self-reinforcing cycle) is not claimed in the contribution section. **Recommend: Add contributions 5 (model behavior audit) and 6 (Triple Bind synthesis) as the blueprint proposes.**

#### 5f. Blueprint Word Count Arithmetic

The blueprint's Section 8 shows Section 7 additions summing to +1,370 but the target delta in Section 1 says +1,601. This means the blueprint is ~231 words short of its own target for Section 7. The blueprint acknowledges this shortfall and suggests expanding 7.2 by ~150 words. This is acceptable but should be tracked.

---

### CR-6. Prioritized Action List

#### P0 (Must Fix Before Any Submission)

1. **RLHF conflict counts**: Reproduce from source data. Reconcile Table 8 (249 vs 237), all three per-model breakdowns in S2-results.md, and the methods range (196 vs 210). This is computational, not editorial.
2. **Table renumbering**: Assign unique sequential numbers to all tables (Methods 1-4, Results 5-13). Fix the Table 5/6 order swap. Create or remove Table 9.
3. **Missing citations**: Add all ~15 benchmark references (Lahmar, Farsi, Xiong, Wong HBC, Ray, Neira-Davila, Agarwal, Rao, Rahman, Catapang, Keutzer, Eickhoff, Ogunremi, Vandenberg & Lance, Chen, ITC 2017) to 09-references.md.
4. **MENA classification**: Resolve "Ambiguous" vs "Global South" with explicit justification in methods.

#### P1 (Must Fix Before Peer Review)

5. **Introduction migration**: Move introduction to PAPER-V2/, resolving: (a) Section 2 literature review collision with 02-methods.md, (b) stale numbers (63.4 to 64.5, 56.0% to 59.7%), (c) v1 section cross-references (2.4, 3.2.3).
6. **Triple Bind early introduction**: Add to Section 1.1 or 1.2 per blueprint.
7. **RQ expansion**: Add RQ6 (model behavior) and RQ7 (Triple Bind) with Study mapping table.
8. **Contribution expansion**: Add contributions 5-6 per blueprint.
9. **Roadmap rewrite**: Map onto Sections 2-8 per blueprint.
10. **Methods RLHF range**: Change "196 to 277" to "210 to 277."
11. **"Sections 3--5"**: Change to "Sections 3--6."
12. **Synthesis "countries" vs "population"**: Align with source.
13. **Gwagwa et al. encoding error**: Fix corrupted author name.
14. **7.2 Islamic jurisprudence qualifier**: Add *madhahib* acknowledgment per CR-1 flag.

#### P2 (Should Fix Before Submission)

15. **Execute all blueprint expansions** (Sections 5, 6, 7): ~2,253 words of drafted prose, all anti-essentialization approved.
16. **Orphaned references**: After introduction migration, re-run check. Prune genuinely unused; re-cite essential non-Western philosophy references.
17. **Abstract compression**: 523 words to 150 words for NHB compliance (if NHB is the target venue).
18. **MFQ approximate values**: Replace 14 "~" cells with exact values and citations.
19. **Supplementary figures S1, S2, S7**: Verify existence in supp-figures/ directory.
20. **NHB submission components**: Data/code availability, ethics statement, CRediT, competing interests, etc.

---

*Phase 2 cross-review complete.*
