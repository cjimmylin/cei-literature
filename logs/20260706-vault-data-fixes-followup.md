# 20260706 — Vault Data Fixes Follow-up Log

**Session:** Fable Week core-track queue item 5 (vault-fix leftovers)
**Date:** 2026-07-06
**Continues from:** `logs/20260705-vault-data-fixes.md` Issues 3, 4, 5

---

## Part A — Web-Verify: Source Hypotheses for Blocked Issues

### A1 — Issue 3: Simple Probes / Sycophancy (Stem: `Anthropic-Simple_Probes_Detect_Sycophancy_2406.09569`)

**Hypothesis tested:** Is the intended source the Anthropic alignment blog post "Simple probes can catch sleeper agents" (April 2024)?

**Web verification:**

The Anthropic alignment blog post "Simple probes can catch sleeper agents" (published April 23, 2024) exists and was verified at:
- Canonical URL: https://www.anthropic.com/research/probes-catch-sleeper-agents
- Authors: Monte MacDiarmid, Timothy Maxwell, Nicholas Schiefer, Jesse Mu, Jared Kaplan, David Duvenaud, Sam Bowman, Alex Tamkin, Ethan Perez, Mrinank Sharma, Carson Denison, Evan Hubinger
- Topic: "defection probes" — linear classifiers detecting when sleeper-agent models will defect, achieving >99% AUROC on Gemini 1.0-style backdoor models
- This is a **non-arXiv blog post** (no arXiv ID)

**Critical finding — stem name is a DOUBLE error:**

The vault stem says "Simple_Probes_**Sycophancy**" but the only matching blog post is about **sleeper agents**, not sycophancy. There is no Anthropic paper (arXiv or blog) specifically titled "simple probes detect sycophancy." The closest third-party paper on probes + sycophancy is "Linear Probe Penalties Reduce LLM Sycophancy" (arXiv:2412.00967, Papadatos & Freedman, December 2024 — not Anthropic).

**Possible explanations (in order of likelihood):**
1. The vault entry was intended to be the "Simple probes can catch sleeper agents" blog post, and the stem was mis-labeled "Sycophancy" instead of "Sleeper_Agents". The arXiv ID 2406.09569 was also wrong (it's "Speech ReaLLM").
2. The entry was mis-created by combining two different things: the "simple probes" concept from the sleeper agents post + the "sycophancy" theme from arXiv:2310.13548 (Sharma et al.). Both involve Anthropic + probes/linear-classifiers.

**Verdict:** DOUBLE ERROR — both the topic label ("Sycophancy") and the arXiv ID (2406.09569) are wrong. The likely intended source is the Anthropic blog post about sleeper agents.

**Confidence:** HIGH that the correct source is the sleeper-agents blog post. HIGH that there is no separate "simple probes + sycophancy" Anthropic paper.

**Recommendation for Jimmy:**
- Confirm the intended source is https://www.anthropic.com/research/probes-catch-sleeper-agents
- If yes: move bad PDF → RECYCLE-BIN, replace extract with correct content, rename stem to `Anthropic-Simple_Probes_Catch_Sleeper_Agents_2024-04-23` (no arXiv ID — use date)
- If a separate "simple probes + sycophancy" paper exists from another source, provide the URL/arXiv ID for lookup

**Status: BLOCKED (needs Jimmy sign-off on the correct source before any file changes)**

---

### A2 — Issue 4: Gemini Safety (Stem: `Google DeepMind-Gemini_Safety_arxiv_2403.04312`)

**Hypothesis tested:** Is the intended source arXiv 2403.13793 "Evaluating Frontier Models for Dangerous Capabilities"?

**Web verification:**

arXiv 2403.13793 confirmed at https://arxiv.org/abs/2403.13793:
- **Title:** "Evaluating Frontier Models for Dangerous Capabilities"
- **Authors:** Mary Phuong, Matthew Aitchison, + 25 others (27 total, all Google DeepMind)
- **Submitted:** March 20, 2024; revised April 5, 2024
- **Abstract:** Introduces "dangerous capability" evaluations across four domains: (1) persuasion and deception; (2) cyber-security; (3) self-proliferation; (4) self-reasoning. Piloted on **Gemini 1.0** models. No strong dangerous capabilities found; early warning signs flagged.

**Assessment:** This is a strong match for "Gemini Safety":
- It is a Google DeepMind paper
- It explicitly evaluates Gemini 1.0 models
- It covers safety / dangerous capabilities — aligning with "Gemini Safety" framing
- Publication date (March 2024) is consistent with when this type of entry would be created

**Alternative considered:** The Gemini 1.0 Technical Report (arXiv:2312.11805) also contains safety evaluation sections, but that is a broader technical report, not a dedicated safety paper. The "Evaluating Frontier Models" paper is the dedicated safety evaluation work and is a better fit for the stem name "Gemini_Safety".

**Verdict:** arXiv 2403.13793 is the correct source with HIGH confidence.

**Confidence:** HIGH.

**Recommendation for Jimmy:**
- Confirm the intended source is https://arxiv.org/abs/2403.13793 ("Evaluating Frontier Models for Dangerous Capabilities", Phuong et al., 2024)
- If yes: move bad PDF → RECYCLE-BIN, download correct PDF from `https://arxiv.org/pdf/2403.13793`, regenerate extract and vault card
- Correct arXiv ID to use: 2403.13793 (the current stem has 2403.04312 which is the Paley graphs number-theory paper)

**Status: BLOCKED (needs Jimmy sign-off before any file changes)**

---

## Part B — CCAI↔Sycophancy Stem Rename (Issue 5): EXECUTED

**Script:** `COOKBOOK/PYTHON/20260706-rename-ccai-sycophancy-stem.py`

**Dry-run:** Run first — output confirmed 13 reference files with expected counts, 0 extra files (beyond the script itself, which was auto-excluded), card file showing 2 stem replacements + 1 note-block update, card rename would proceed.

**Apply:** Executed with `--apply`. Full apply output:

### Files Changed

| File | Replacements | Notes |
|------|-------------|-------|
| `30-EVIDENCE/20260705-card-index.json` | 6 | Includes array entries (×4) + dict key + path field |
| `30-EVIDENCE/20260705-ailabs-shortlist.json` | 2 | stem + extract_path fields |
| `30-EVIDENCE/20260705-dossier-assignments/ai-lab-practices-part3.json` | 2 | |
| `30-EVIDENCE/20260705-dossier-assignments/saturation-discrimination-part2.json` | 2 | |
| `30-EVIDENCE/20260705-dossier-assignments/validity-psychometrics-part2.json` | 2 | |
| `30-EVIDENCE/20260705-dossier-assignments/normative-ethics-part5.json` | 2 | |
| `30-EVIDENCE/20260705-batches/L007.json` | 2 | |
| `30-EVIDENCE/20260705-reader-batches.json` | 2 | |
| `30-EVIDENCE/20260705-ailabs-listing.json` | 2 | stem + extract_path fields |
| `30-EVIDENCE/20260705-dossiers/parts/saturation-discrimination-part2.md` | 1 | inline citation |
| `00-KNOWLEDGEBASE/13-ai-lab-alignment-practices.md` | 1 | abbreviated form |
| `10-LITERATURE/20260705-lit-spotcheck-report.md` | 1 | **EXTRA (not in original log map)** |
| `10-LITERATURE/alignment-methods-overview.md` | 2 | **EXTRA (not in original log map)** |
| Card file (content) | 2 + 1 note | 2 stem replacements + NOTE block update |
| Card file (rename) | — | File renamed |

**Total: 13 reference files + 1 card file = 14 files touched; 29 replacements total**

### Extra Files Found

Grep of the full `COOKBOOK/` tree found 2 extra files beyond the 11-file log map:
1. `COOKBOOK/10-LITERATURE/20260705-lit-spotcheck-report.md` — 1 occurrence of abbreviated form (in a sycophancy-verification row)
2. `COOKBOOK/10-LITERATURE/alignment-methods-overview.md` — 2 occurrences (1 abbreviated + 1 `(sycophancy)` variant)

Both extra files were updated.

### Collision Reconciliation

**Collision guard result:** No exact collision. The new stem `Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548` is clear.

**Near-match in `ailabs-listing.json`:** A pre-existing entry `Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548v2` was found. This is a distinct key (base vs v2 suffix). The two entries in `ailabs-listing.json` after apply:
- `Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548` → renamed to `Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548` (base, card exists)
- `Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548v2` (pre-existing, no card file — extract only)

**Recommendation for Jimmy:** Determine which is authoritative; if both represent the same paper, the v2 entry may be redundant and could be removed from `ailabs-listing.json` in a future cleanup pass.

### Validation Results

- **JSON validity:** ALL 9 modified JSON files validate cleanly (`json.load` OK)
- **Remnant check:** CLEAN (zero active citations remain with old stem or old abbreviated form under `COOKBOOK/`)
  - The script file `COOKBOOK/PYTHON/20260706-rename-ccai-sycophancy-stem.py` contains OLD_STEM as string literals (intentional — it defines the pattern to search for) and is excluded from the active-citation check
  - The card file line 19 contains the old stem in a historical "previously mis-filed under" note (intentional preservation)
- **Card file state:** New card exists at correct path; old card is gone

### Card Note Block

The card's `§1 Gist` NOTE ON FILE NAMING was updated from:
> "NOTE ON FILE NAMING: This extract is filed under the stem ... but the actual paper is..."

To:
> "NOTE ON FILE NAMING (CORRECTED 2026-07-06): This extract was previously mis-filed under the stem 'Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548' but has been renamed to the correct stem 'Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548'. The actual paper is..."

The `§11 UNKNOWN` note was also updated from "The extract is filed under..." to "This file was previously mis-filed under... (CORRECTED 2026-07-06)."

---

## Open Items / Blocked

| Item | Status | Next Action |
|------|--------|-------------|
| Issue 3: Simple Probes PDF source | BLOCKED — needs Jimmy sign-off | Confirm source = https://www.anthropic.com/research/probes-catch-sleeper-agents; then PDF/extract/card replacement |
| Issue 4: Gemini Safety PDF source | BLOCKED — needs Jimmy sign-off | Confirm source = arXiv:2403.13793; then PDF/extract/card replacement |
| ailabs-listing.json v2 near-match | LOW PRIORITY | Determine if `...2310.13548v2` entry is redundant vs base entry; remove if so |
| Issue 1/2 stem corrections | DEFERRED | Sabotage (2410.13161→2410.21514) and Sleeper Agents (2312.00752→2401.05566) stems still have wrong arXiv IDs in names; full stem rename (9+ JSON files each) deferred from prior session |

---

## Files Modified This Session

- `COOKBOOK/PYTHON/20260706-rename-ccai-sycophancy-stem.py` — new script (dry-run + apply)
- `COOKBOOK/30-EVIDENCE/20260705-ailabs-cards/Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548.card.md` — renamed from CCAI stem + note corrected
- `COOKBOOK/30-EVIDENCE/20260705-card-index.json` — 6 replacements
- `COOKBOOK/30-EVIDENCE/20260705-ailabs-shortlist.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-ailabs-listing.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-reader-batches.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-batches/L007.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/ai-lab-practices-part3.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/saturation-discrimination-part2.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/validity-psychometrics-part2.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/normative-ethics-part5.json` — 2 replacements
- `COOKBOOK/30-EVIDENCE/20260705-dossiers/parts/saturation-discrimination-part2.md` — 1 replacement
- `COOKBOOK/00-KNOWLEDGEBASE/13-ai-lab-alignment-practices.md` — 1 replacement
- `COOKBOOK/10-LITERATURE/20260705-lit-spotcheck-report.md` — 1 replacement (extra)
- `COOKBOOK/10-LITERATURE/alignment-methods-overview.md` — 2 replacements (extra)
- `logs/20260706-vault-data-fixes-followup.md` — this file (new)

---

## Addendum (orchestrator verification pass, 2026-07-06)

Adversarial check of the scripted rename surfaced an **incomplete-replacement gap**: the
rename script matched the bare stem and bare abbreviation but NOT the annotated citation
form `[Anthropic-Collective_Constitutional_AI (Sycophancy)]` used in dossier/lit prose.
Because `20260705-card-index.json` no longer contains the old stem, those citations had
become unresolvable. Completed the fix (7 annotated citations → new stem) in the **living
reference** files only:

- `COOKBOOK/30-EVIDENCE/20260705-dossiers/20260705-ai-lab-practices-dossier.md` (2)
- `COOKBOOK/30-EVIDENCE/20260705-dossiers/parts/ai-lab-practices-part3.md` (3)
- `COOKBOOK/10-LITERATURE/alignment-methods-overview.md` (2)

**Reverted** `COOKBOOK/10-LITERATURE/20260705-lit-spotcheck-report.md` to its committed
2026-07-05 state (Report Immutability #3): it is a point-in-time audit snapshot, and the
mechanical rename had wrongly re-pointed a **CCAI-content** row ("constitution claim … BBQ
bias lowered") at the Sycophancy card, destroying the very mismatch that audit row
documented. Its two old-stem citations are intentional historical record.

**Remaining old-stem strings (all intentional, none are broken live citations):**
- the card's own dated "NOTE ON FILE NAMING" history block;
- the 2026-07-05 session handoff's bug description;
- descriptive prose in `normative-ethics-part5.md` ("the sycophancy card (mis-filed under
  Collective_Constitutional_AI)") — accurate provenance note, not a `[stem]` citation;
- the immutable spot-check report (above).

Verification: zero bracketed old-stem citations remain in living reference material; all
modified JSON parse; new stem present in `card-index.json`.

---

## Issue 4 RESOLVED (2026-07-06) — Gemini Safety PDF replaced (Jimmy-approved)

Downloaded arXiv **2403.13793** "Evaluating Frontier Models for Dangerous Capabilities"
(Phuong et al., Google DeepMind, 81pp); verified the title page before mutating anything.
Following the Issue-1/2 pattern (stem preserved to avoid breaking references):

- Bad files → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-06/` (`--BAD-CONTENT`/`--BAD-EXTRACT`): the old
  PDF (was arXiv 2403.04312 = a Paley-graphs number-theory paper), extract, and vault card.
- Correct PDF installed at the original stem path `AI-Lab-PDFs/Google DeepMind/Papers/
  Gemini_Safety_arxiv_2403.04312.pdf` (external storage; not git-tracked).
- Regenerated extract + vault card (PyMuPDF 1.26.5, 81pp) with a `regenerated:` frontmatter note
  flagging the correct arXiv ID/title. Stem still embeds the wrong ID 2403.04312 — a future pass may
  rename the stem + update references, as with Sabotage/Sleeper.

**Remaining vault-fix blocker:** Issue 3 ("Simple Probes / Sycophancy", stem 2406.09569) is a topic
conflation (candidate blog post is about sleeper agents) — still awaiting Jimmy's decision on the
intended source before any replacement.

---

## Issue 3 RESOLVED (2026-07-06) — Simple Probes: sleeper-agents blog, stem renamed (Jimmy-approved)

Jimmy confirmed the intended source is the Anthropic blog **"Simple probes can catch sleeper agents"**
(2024-04-23, MacDiarmid et al.) and that the stem name was wrong. The prior stem was doubly wrong:
arXiv 2406.09569 = "Speech ReaLLM" (unrelated), and the topic is sleeper-agent *defection probes*, not
sycophancy. Followed the CCAI precedent (rename, not stem-preserve, since the whole name was wrong):

- Fetched + archived the blog article text (title, date, authors, all sections) via WebFetch; generated
  a 2-page text PDF via **fpdf2** (per the CLAUDE.md PDF rule) at the new stem path.
- Renamed stem `Simple_Probes_Detect_Sycophancy_2406.09569` → `Simple_Probes_Catch_Sleeper_Agents_2024`
  across all 6 references: 5 COOKBOOK/30-EVIDENCE JSONs (reader-batches, ailabs-listing, run-state, L011,
  ailabs-shortlist) + the AI-Labs README row (rewritten — title, blog link, description).
- Bad Speech-ReaLLM PDF + extract → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-06/`. New extract + a NEW vault
  card written (none existed before) with `source_url`, a `regenerated:` note, and the archived content.
- Verified: new stem resolves; JSON all valid; zero old-stem remnants in living CEI-Lit-WS material.

**Remaining (historical, intentionally left):** `logs/20260202-pdf_migration_*.json` still contains the
old stem — a historical migration record, not a live citation. Both vault-fix blockers (Issues 3 & 4)
are now RESOLVED; nothing outstanding on the vault-data-fixes track.
