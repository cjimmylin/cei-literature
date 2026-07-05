# The Benchmark Landscape in Numbers: A Cross-Corpus Statistical Portrait

**What this is.** Four completed CEI sub-projects — NormEval (normative ethics), Moral
Psychology, Religious Values, and Cultural/Global Values — each built a feature matrix
that scores a population of candidate benchmarks against a project-specific rubric.
Together they characterize **965 benchmark records** (54 + 292 + 401 + 218). This chapter
cross-tabulates those four matrices into one landscape view so a future benchmark
designer can see the shape of the field — where the mass sits, how much of it clears a
quality bar, how recent it is, and which traditions are covered — before committing to a
design.

**How to read the numbers.** Every figure below is either (a) **computed** directly from
the four source JSON matrices by script (stated as "computed"), or (b) **copied** from
the project's own 2026-07-05 digest with a citation. Where a computed number diverges
from a digest headline, both are shown and the divergence is flagged. The composites are
**not comparable across corpora** — each project weights different sub-scores (see
Caveats) — so cross-corpus reading is by rate and rank, never by raw composite.

**Source matrices (all computed figures derive from these):**

| Corpus | File | Records |
|---|---|---|
| NormEval | `NORM-ETHICS/STATISTICS/20260404-normeval-expanded-feature-matrix.json` | 54 |
| Moral Psych | `MORAL-PSYCH/20260405-full-292-feature-matrix.json` | 292 |
| Religious Values | `RELIGIOUS-VALUES/data/20260404-religious-benchmark-feature-matrix-v2.json` | 401 |
| Cultural/Global | `CULTURAL-GLOBAL/DATA/20260404-benchmark-rankings.json` | 218 |

---

## 1. Per-corpus summary

The four projects use different quality machinery. NormEval and Religious Values apply
**hard gates** (a normative-depth minimum AND public data availability); Moral Psychology
applies **Jenks natural-break tiers** (top / high / med / low); Cultural/Global uses a
**TOPSIS ranking with ELECTRE-III veto** rather than a pass/fail gate. The table records
each on its own terms.

| Corpus | N | Quality metric | "Pass" count (rate) | Composite (own scale): min / median / max | Year span | 2024+ share |
|---|---|---|---|---|---|---|
| NormEval | 54 | Both hard gates (ND≥40 & public data) | 24 (44.4%) | 22.8 / 49.3 / 77.2 | 2021–2026 | 52/54 (96.3%) |
| Moral Psych | 292 | Jenks top tier / top+high | 48 (16.4%) / 137 (46.9%) | 2.1 / 40.4 / 81.3 | 2015–2026 | 225/292 (77.1%) |
| Religious Values | 401 | Both hard gates (RD≥30 & public data) | 47 (11.7%) | 14.4 / 32.4 / 52.0 | 1970–2026 | 309/401 (77.1%) |
| Cultural/Global | 218 | TOPSIS rank; ELECTRE-III veto | 5 vetoed; effective intersection ≈15 (<7%) | TOPSIS 0.047 / 0.206 / 0.637 | not in matrix | n/a in matrix |

*All counts, rates, composite quantiles, and year spans in this table are **computed** from
the four matrices. The NormEval gate count (24) matches the digest's "24 pass both gates"
(NormEval digest). Moral Psych tiers 48/89/72/83 match the digest's Jenks tier counts
(Moral Psych digest). Religious Values gate count 47 matches "47 pass both gates"
(Religious Values digest). Cultural/Global's "<7% intersection" and "5 vetoed" are copied
from the Cultural digest; the 218 records carry no year field in this matrix, so no 2024+
share is computable here (the digest reports growth from 12 papers in 2023 to 129 in 2025).*

**Component-score distributions (computed, each on its own project scale):**

| Corpus | Component scales (min / median / max) |
|---|---|
| NormEval | ND 15.2 / 55.4 / 87.0 · PE 12.0 / 66.5 / 95.0 · CI 12.0 / 25.8 / 80.0 |
| Moral Psych | PD 0.0 / 43.0 / 92.5 · PE 3.0 / 41.9 / 97.2 · CI 6.2 / 26.2 / 85.0 |
| Religious Values | RD 13.0 / 19.0 / 68.0 · PE 18.0 / 57.5 / 80.0 · CI 7.5 / 15.0 / 25.0 |

The shape is consistent across projects: the **quality/depth axis** (ND / PD / RD) and the
**community-impact axis** (CI) both sit low and left-skewed, while the **practical-execution
axis** (PE) — data, code, harness, licence — runs higher. Benchmarks tend to be
*runnable* long before they are *deep*. Religious Values shows this most starkly: median RD
of 19.0 against median PE of 57.5, and a CI axis whose maximum (25.0) is below the other
projects' medians.

**Year distributions (computed):**

- **NormEval:** 2021×1, 2023×1, 2024×16, 2025×30, 2026×6. A recency spike — 96% is 2024+.
- **Moral Psych:** a long tail back to 2015, then 2022×14, 2023×32, 2024×73, 2025×138,
  2026×14. The 2023–2026 window holds 257/292 (88.0%, computed; matches digest's "9.5×
  volume growth vs pre-2020").
- **Religious Values:** back to 1970×1, rising through 2022×22, 2023×39, 2024×103,
  2025×192, 2026×14.
- **Cultural/Global:** the rankings matrix has no per-record year; the digest reports a
  "tenfold rise" 12 (2023) → 129 (2025).

---

## 2. Cross-corpus comparison: availability, quality, recency

The single most useful cross-read is what fraction of each landscape is (a) publicly
available, (b) quality-gate/tier-passing, and (c) recent (2024+). Each is measured with
that corpus's own field, so the *definitions* differ (see footnotes) — but the *pattern*
is comparable.

| | NormEval | Moral Psych | Religious Values | Cultural/Global |
|---|---|---|---|---|
| N | 54 | 292 | 401 | 218 |
| (a) Publicly available | 36/54 (66.7%) | not separable in this matrix† | 231/401 (57.6%) | ordinal only‡ |
| (b) Gate / tier passing | 24/54 (44.4%) | 48/292 top (16.4%); 137 top+high (46.9%) | 47/401 (11.7%) | 5 vetoed; ≈15 (<7%) usable |
| (c) Recent (2024+) | 52/54 (96.3%) | 225/292 (77.1%) | 309/401 (77.1%)§ | not in matrix |

*(a), (b), (c) are **computed** except where noted.*
- **†** The Moral Psych matrix stores only composites (PD/PE/CI/COMPOSITE); public
  availability is folded into the PE sub-score (B3 feature) and is not separable from this
  file. It is therefore left blank rather than guessed.
- **‡** Cultural/Global encodes availability as an ordinal `data_availability` dimension
  (0–5), computed **mean 3.19 / median 5.0**, not a clean public/not-public split; the
  digest notes its TOPSIS #1 (Ray) has "zero data availability."
- **§** Religious Values 2024+ is **computed as 309/401 (77.1%)** from the v2 matrix. The
  Religious Values digest reports "**73% of all 401 candidates date from 2024–2026**." The
  gap (77.1% computed vs 73% digest) reflects the digest's note that the v2 feature-matrix
  is a *pre-reclassification snapshot*; **use 73% for reporting** and treat 77.1% as the
  raw-matrix figure. Among gate-passers specifically, **28/47 (59.6%)** date from 2024+
  (computed; matches digest).

**Reading the columns.** Availability is the great filter: it is high (≥57%) wherever it is
measurable, and it is what most of the gate attrition is actually made of. In NormEval, 18
of 54 fail *only* on data availability (digest); in Religious Values the data gate alone
eliminates ~77% of the corpus (digest). Quality-gate rates fall as corpora grow — 44% of
54 (NormEval) down to 11.7% of 401 (Religious Values) — the volume-quality inversion
examined in §4. Recency is uniformly high: three of the four corpora are ~77–96% post-2024,
confirming these are young, fast-growing literatures.

---

## 3. Coverage tables

Each project maps its landscape onto a different taxonomy of traditions/theories. These
tables show where the mass concentrates and where the voids are.

### 3a. NormEval — normative traditions (A1 engagement, computed)

Per-benchmark tradition scores are 0–100; "any" = score > 0, "substantive" = score ≥ 50.

| Tradition | Any engagement | Substantive (≥50) |
|---|---|---|
| Utilitarian | 43 | 30 |
| Deontological | 40 | 29 |
| Virtue | 28 | 18 |
| Care | 13 | 2 |
| Contractarian | 10 | 4 |

*Computed; matches the NormEval digest exactly.* Care ethics collapses from 13 "any" to
just **2 substantive** — the digest's binomial test rejects the 20%-expected null at
p < 0.001. The consequentialist/deontological pair dominates; the western canon's
"relational" wing (care, contractarian) is decorative. Separately, on reasoning depth the
digest reports **only 10/54 (18.5%) test moral reasoning** vs judgment; the matrix's raw
A3 field breaks this as reasoning-process 10, both-judgment-and-reasoning 13,
judgment-only 31 (computed) — the digest's 10/54 counts the reasoning-process-only bucket.

### 3b. Moral Psychology — theory × tier (computed)

| Theory | Total | Top | High | Med | Low | Top+High rate |
|---|---:|---:|---:|---:|---:|---:|
| Moral Foundations (MFT) | 67 | 18 | 31 | 13 | 5 | 73% |
| Schwartz Values | 51 | 5 | 25 | 15 | 6 | 59% |
| Trolley / sacrificial | 36 | 13 | 6 | 12 | 5 | 53% |
| Islamic | 22 | 3 | 5 | 5 | 9 | 36% |
| Kohlberg | 18 | 6 | 5 | 5 | 2 | 61% |
| Buddhist | 16 | 1 | 1 | 3 | 11 | 13% |
| Ubuntu | 13 | 0 | 0 | 2 | 11 | 0% |
| Confucian | 13 | 0 | 0 | 0 | 13 | 0% |
| Moral Identity | 7 | 2 | 3 | 0 | 2 | 71% |
| Intuitionist | 4 | 1 | 3 | 0 | 0 | 100% |
| Indigenous | 4 | 0 | 0 | 0 | 4 | 0% |
| Dyadic | 3 | 0 | 2 | 0 | 1 | 67% |

*Computed (benchmarks with multiple theory tags are counted in each row, so totals sum
above 292).* MFT alone holds **18 of 48 top-tier slots** at a 73% top+high rate; Ubuntu,
Confucian, and Indigenous together contribute **30 candidates and zero top-or-high
benchmarks**. The digest's headline — western traditions ~62% quality vs zero-quality
non-western traditions at 0% — is visible directly in the tier columns.

### 3c. Religious Values — tradition (D5) × gate passage (computed)

| Tradition (D5) | Candidates | Gate-passers |
|---|---:|---:|
| Christianity | 117 | 6 |
| Islam | 113 | 28 |
| Jainism | 47 | 0 |
| *Unknown (unassigned)* | 30 | 0 |
| Hinduism | 25 | 4 |
| Indigenous Spirituality | 16 | 0 |
| Confucianism | 14 | 1 |
| Buddhism | 14 | 6 |
| Judaism | 9 | 0 |
| Sikhism | 6 | 2 |
| Ubuntu Philosophy | 4 | 0 |
| Taoism / Zoroastrianism / Shinto | 2 each | 0 |

*Computed from the v2 matrix.* **Flag:** the Religious Values digest warns that the v2
matrix is a *pre-reclassification snapshot* carrying a 30-record "Unknown" bucket, and that
the paper's Table 3 (manually verified) differs — e.g. Hinduism 43/5, Buddhism 31/3,
Jainism 59/0 in the paper vs 25/4, 14/6, 47/0 computed here. **Use the paper's Table 3 for
reporting; the computed numbers above are the raw matrix.** Both agree on the load-bearing
finding: **Islam supplies 28 of 47 gate-passers (59.6%)** while eight traditions (Judaism,
Jainism, Taoism, Shinto, Ubuntu, Indigenous, Baha'i, Zoroastrianism) have zero viable
benchmarks (digest).

### 3d. Cultural/Global — dimensional scores (computed means across 218)

| Dimension (weight) | Mean | Median | Max |
|---|---:|---:|---:|
| Alignment relevance (.20) | 0.76 | 0.0 | 4.0 |
| Cross-cultural scope (.20) | 11.67 | 9.0 | 40.0 |
| Non-western coverage (.15) | 0.40 | 0.0 | 5.0 |
| LLM administrability (.12) | 2.28 | 2.0 | 4.0 |
| Psychometric quality (.10) | 0.29 | 0.0 | 1.0 |
| Evaluation depth (.10) | 1.94 | 0.5 | 11.0 |
| Data availability (.08) | 3.19 | 5.0 | 5.0 |
| Epistemic provenance (.05) | 1.46 | 1.0 | 3.0 |

*Computed.* The two lowest-scoring dimensions are **non-western coverage (median 0.0)** and
**psychometric quality (median 0.0, max 1.0)** — precisely the two things a *cross-cultural*
benchmark exists to deliver. Administrability and data availability, by contrast, sit high.
This is the same runnable-but-shallow signature seen in §1, now at the level of an entire
"cultural" sub-field.

---

## 4. Quality vs volume

Every project's core finding is a variant of the same claim: **the population is large and
growing fast, but the quality-passing fraction is small and, where measurable, shrinking as
volume rises.** The four headline statistics, restated verbatim from the digests:

- **NormEval — 24/54 gates, 10/54 reasoning.** 24 of 54 benchmarks pass both hard gates;
  only **10/54 (18.5%)** test moral reasoning rather than judgment (44/54 judgment-only,
  binomial p < 0.001). Critically, gate passage reflects *sociology, not quality*: there is
  no significant ND difference between gate-passers and gate-failers (Mann-Whitney
  U = 287, p = 0.605), and median ND is actually *higher* among the data-unavailable (58.8)
  than the available (53.0) (NormEval digest).
- **Moral Psych — 48/292 top tier, 58% validity Level 1–2.** Only **48 of 292 (16.4%)**
  reach the top Jenks tier; construct-validity assessment under full coverage puts **58% at
  Level 1 or 2** (up from 17% in the 55-benchmark subsample — a 3.4× jump). Quality rate by
  period is *flat despite 9.5× volume growth*: pre-2020 75% → 2020–22 48% → 2023–26 46%,
  while top-tier-only rate falls 50% → 37% → 13%. And quality predicts *convergence*, not
  discrimination (r = −0.83) (Moral Psych digest).
- **Religious Values — 45 gate-passers, 27.7% reasoning.** The PRISMA flow yields **45
  gate-passers** (47 pass both gates, 2 removed post-review); the two gates together
  eliminate **354/401 (88.3%)**. Only **27.7% (13/47)** of gate-passers test genuine
  theological reasoning rather than factual recall (binomial p = 0.0015). On the 24-dimension
  values-relevance rubric, mean A3 = 30.0/100, significantly below midpoint (Cohen's
  d = −1.23) (Religious Values digest). *(Note: the matrix's broader `gate_theological` flag
  is set on 37/401 records, computed — a looser construct than the 13/47 deep-reasoning
  assessment; the 13/47 is authoritative.)*
- **Cultural/Global — <7% substance × usability, 0/218 invariance.** Of 218 benchmarks,
  the culturally-substantive **AND** LLM-administrable intersection is **≈15 (<7%)**, and
  **precisely zero of 218 report measurement invariance testing** — the psychometric
  prerequisite for any valid cross-cultural comparison. Effective usable N ≈ 3.4 of 10
  nominal model slots (Cultural digest).

**The composite pattern.** Read together (and remembering the composites are not
cross-comparable), the same funnel appears four times: a **broad candidate pool**, a
**data-availability filter** that removes roughly a third to three-quarters, a **depth/
reasoning filter** that removes most of the survivors, and a **residue of ~10–50 genuinely
usable benchmarks per sub-field**. Volume growth is concentrated post-2024 in every corpus,
but the quality-passing *rate* does not rise with it — in Moral Psychology it demonstrably
falls. For a designer, the actionable read is that the field's scarcity is not in *topics*
or *quantity* but in **depth, non-western coverage, and psychometric validity** — the three
axes that sit at or near floor in every table above.

---

## 5. Caveats

**(1) The corpora overlap.** These are four overlapping samples of one underlying benchmark
literature, not four disjoint populations. Matching by normalized short-title across all
four matrices (computed; punctuation/stop-words stripped) finds **170 titles appearing in
≥2 corpora, 35 in ≥3, and 4 in all four**. Of 965 total records, only **737 titles are
distinct** — i.e. roughly **228 records (~24%) are re-characterizations of a benchmark
already scored by another project** (this includes a small number of within-corpus
short-title collisions, so treat 228 as an upper bound and ~170+ cross-corpus duplicates as
the firmer floor). Pairwise, the largest overlaps are Religious↔Cultural (85 shared
titles), Moral-Psych↔Cultural (66), and Moral-Psych↔Religious (53); NormEval, the smallest
and most sharply scoped corpus, overlaps least (5–27 per pair). **Do not sum the four Ns as
though they were independent** — the true count of distinct benchmarks characterized is
closer to ~737 than 965. Shared benchmarks (e.g. *Aligning AI with Shared Human Values /
ETHICS*, *CVC*, *IslamTrust*, *Moral Machine*, *One Model Many Morals*) can and do receive
different tiers under different rubrics.

**(2) Composites are not comparable across corpora.** Each project weights different
sub-scores into its COMPOSITE: NormEval = ND/PE/CI; Moral Psych = PD×0.50 + PE×0.30 +
CI×0.20; Religious Values = RD×0.40 + PE×0.35 + CI×0.25; Cultural/Global uses an
eight-dimension TOPSIS closeness coefficient on an entirely different (ordinal) feature set.
A NormEval COMPOSITE of 77.2 and a Religious Values COMPOSITE of 52.0 are both "the top of
their landscape" but are *not the same quantity* and cannot be ranked against each other.
Cross-corpus comparison in this chapter is therefore always by **rate, rank, or coverage** —
never by raw composite value.

**(3) Characterizations are single-project ratings.** Every score here is one project's
rubric applied by one project's scorers (in several cases LLM-assisted self-administration
by the Claude family, per each digest's disclosure). Where a benchmark appears in two
matrices, the two ratings are independent single-rater judgments, not a validated consensus.
Gate/tier thresholds (ND≥40, RD≥30, Jenks breaks, ELECTRE veto) are design choices, not
external standards. Treat these tables as a **navigational map of the landscape's shape**,
not as a certified quality register of individual benchmarks.

**(4) Field-specific measurement caveats carry over.** Each digest documents its own limits —
NormEval's cross-vendor results are elicited, not API-direct; Moral Psychology's absolute
model values are hypothesis-generating; Religious Values' external search was English-only
(401 is a lower bound); Cultural/Global's keyword precision is ~0.48 (about half of
non-western "detections" are terminological mentions). Those caveats bound the underlying
scores that feed every table above.

---

*Figures marked "computed" were produced by scripting summaries directly over the four
source JSON matrices (no hand-transcription from raw JSON). Figures marked as from a
"digest" are copied verbatim from the corresponding file in
`COOKBOOK/30-EVIDENCE/20260705-digests/`. Where the two diverged — Religious Values' 2024+
share (77.1% computed vs 73% digest) and its per-tradition D5 counts (raw matrix vs paper
Table 3) — both are reported and the digest/paper figure is flagged as authoritative for
reporting.*
