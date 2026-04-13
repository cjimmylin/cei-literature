# Expert 06 — Reproducibility / FAIR Data Review

**Perspective:** Reproducibility and FAIR data compliance
**Scope:** LICENSE, CITATION.cff, .zenodo.json, data-availability statement, dashboard URLs
**Paper version:** v2.2-preliminary

---

## (a) FAIR Compliance Assessment

### Findable

**Adequate but incomplete.** The data-availability statement lists three dashboard URLs (v1-v3) and references a Zenodo deposit. However:

- **F1 (Globally unique persistent identifier):** No DOI exists yet. The Zenodo placeholder reads "[DOI pending]." Without a DOI, the dataset is not findable through standard scholarly infrastructure (DataCite, OpenAIRE, Google Dataset Search). This is the single largest FAIR gap.
- **F2 (Rich metadata):** `.zenodo.json` has title, description, keywords, and related identifiers. Missing: author/creator metadata (see section c below), version field, and a structured file manifest.
- **F3 (Metadata includes identifier of data):** Cannot be satisfied until the DOI is minted.
- **F4 (Searchable registry):** Zenodo satisfies this once deposited. GitHub Pages dashboards are indexed by Google but are not in any dataset registry.

**Recommendation:** Add `version: "2.2-preliminary"` and `creators` array to `.zenodo.json` before deposit. Register the Zenodo record (even as a draft/pre-publication deposit) to obtain a reserved DOI that can be cited in the manuscript.

### Accessible

**Strong.** All three dashboards are live on GitHub Pages (HTTPS, no authentication). The LICENSE file clearly states MIT for code and CC-BY-4.0 for data. Zenodo guarantees long-term access once deposited. No issues here.

One gap: the `repository-code` field in CITATION.cff points to the main `cei-literature` repo, which is the full vault. If reviewers clone that repo expecting the NormEval replication package, they will find a 2,000+ paper vault instead. Consider pointing to a dedicated NormEval replication repo or a subfolder path.

### Interoperable

**Partially met.** The feature matrix lives inside dashboard `data.js` files as JavaScript constants, not as a standalone CSV/JSON. A reviewer who wants to re-analyze the 54x26 matrix must either scrape the dashboard or wait for the Zenodo deposit.

- **I1 (Formal language):** `data.js` is JavaScript, not a community standard like CSV, JSON-LD, or Parquet.
- **I2 (FAIR vocabularies):** No schema.org or Dublin Core metadata in the HTML dashboards. The `.zenodo.json` uses Zenodo's own schema, which maps to DataCite — acceptable.
- **I3 (References to other data):** `related_identifiers` in `.zenodo.json` link to all three dashboards. Good.

**Recommendation:** Include a standalone `normeval-matrix.csv` and `trial-results.json` in the Zenodo deposit. These two files alone would dramatically improve interoperability.

### Reusable

**Mixed.** The dual-license structure (MIT + CC-BY-4.0) is well-chosen and clearly documented. The third-party disclaimer in LICENSE is responsible. However:

- **R1.1 (Clear license):** Met. LICENSE file is unambiguous.
- **R1.2 (Provenance):** The data-availability statement describes provenance (API-administered vs. in-context-elicited), but `.zenodo.json` does not include provenance metadata distinguishing the two data tiers. A reviewer downloading the Zenodo package would not know which trial results are empirical and which are simulated without reading the paper.
- **R1.3 (Domain-relevant standards):** No PSYCH-DS or other behavioral-science data standard is followed. For a benchmark evaluation paper this is not unusual, but noting it.

**Recommendation:** Add a `data_provenance.md` or column in the trial CSV marking each result row as `administered` or `elicited-simulated`.

---

## (b) Should the Zenodo DOI Be Placeholder or Pre-Deposited?

**Pre-deposit before submission.** Rationale:

1. Zenodo allows "reserve DOI" on a draft record without publishing. The DOI is immediately citable. This costs nothing and satisfies F1/F3.
2. Reviewers increasingly expect to click through to data. A "[DOI pending]" placeholder signals the data may never materialize.
3. The `v2.2-preliminary` label is appropriate for a pre-publication deposit. Zenodo supports versioning; a `v3.0` record can supersede it once cross-vendor data is real.
4. Even if the paper is rejected or revised, the Zenodo record stands as a citable artifact and can be updated.

**Workflow:** Create draft Zenodo record, reserve DOI, insert DOI into data-availability statement and CITATION.cff, then publish the Zenodo record when the paper is submitted.

---

## (c) Does `.zenodo.json` Need Author Metadata?

**Yes, critically.** The current `.zenodo.json` has no `creators` field. Zenodo requires `creators` for upload; the current file would fail validation at deposit time. DataCite schema (which Zenodo maps to) mandates at least one creator with `name`.

Required addition:

```json
"creators": [
  {
    "name": "Lin, Jimmy",
    "orcid": "XXXX-XXXX-XXXX-XXXX",
    "affiliation": "Center for Ethical Intelligence"
  }
]
```

Also missing: `version` field. Should be `"2.2-preliminary"` per the labeling rule in the briefing. The `notes` field already says "SKELETON" — this must be updated before deposit.

---

## (d) Is `v2.2-preliminary` Correctly Reflected Across All Metadata Files?

**No. Three of four files are inconsistent:**

| File | Current version label | Correct? |
|------|-----------------------|----------|
| `data-availability-normeval-v2.md` | No version label in YAML frontmatter or body text | Missing |
| `LICENSE` | No version reference (appropriate — licenses are version-agnostic) | N/A |
| `CITATION.cff` | No `version:` field; `date-released: 2026-04-13` but no preliminary flag | Missing |
| `.zenodo.json` | No `version` field; `notes` says "SKELETON" | Missing |

**Specific gaps:**

1. **CITATION.cff** needs `version: "2.2-preliminary"` added. The CFF 1.2.0 schema supports this field. Without it, anyone citing via `CITATION.cff` cannot distinguish v2.2-preliminary from the final release.
2. **`.zenodo.json`** needs `"version": "2.2-preliminary"` added. Also needs the description updated to mention the preliminary/simulated status of cross-vendor data, consistent with the briefing's labeling rule.
3. **`data-availability-normeval-v2.md`** should state the version explicitly, e.g., "This statement accompanies NormEval v2.2-preliminary." The filename itself still says `v2` — consider whether a `v2.2` copy is needed or whether the body text suffices.
4. The **dashboard v4 URL** (`cei-normeval-dashboard-v4`) is not yet listed in any of these files. Per the briefing, it should be added once deployed. The `.zenodo.json` `related_identifiers` array and the data-availability statement both need updating.

---

## Priority Actions (Ranked)

1. **Add `creators` to `.zenodo.json`** — blocks deposit entirely
2. **Add `version: "2.2-preliminary"` to both `.zenodo.json` and `CITATION.cff`** — consistency with briefing labeling rule
3. **Reserve Zenodo DOI via draft deposit** — satisfies F1/F3, replaces placeholder in paper
4. **Bundle standalone CSV/JSON in Zenodo deposit** — largest interoperability improvement
5. **Add provenance column to trial data** — reusability for downstream researchers
6. **Update `repository-code` in CITATION.cff** to point to a NormEval-specific repo or path
7. **Add v4 dashboard URL** to `.zenodo.json` and data-availability statement once deployed
