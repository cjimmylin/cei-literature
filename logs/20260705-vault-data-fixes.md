# 20260705 — Vault Data Fixes Log

**Session:** Fable Week housekeeper pass
**Date:** 2026-07-05
**Agent:** Sonnet housekeeper
**Task source:** COOKBOOK/20260705-cookbook-session-handoff.md §"Vault data fixes"

---

## Issue 1: Anthropic Sabotage Evaluations PDF (FIXED)

**Stem:** `Anthropic-Sabotage_Evaluations_for_Frontier_Models_2410.13161`

**Verification evidence:**
- Extract file first line: "Non-Perturbative Trivializing Flows for Lattice Gauge Theories" (Gerdes, de Haan, Bondesan, Cheng)
- arXiv confirmed: `https://arxiv.org/abs/2410.13161` = "Non-Perturbative Trivializing Flows for Lattice Gauge Theories"
- Correct arXiv ID for "Sabotage Evaluations for Frontier Models": **2410.21514** (verified via arXiv title match)
- Downloaded PDF title page: "Sabotage Evaluations for Frontier Models / Joe Benton, Misha Wagner..." (69 pages)

**Actions taken:**
1. Moved bad PDF → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/Sabotage_Evaluations_for_Frontier_Models_2410.13161--BAD-CONTENT.pdf`
2. Downloaded correct PDF from `https://arxiv.org/pdf/2410.21514` → kept at original path `AI-Lab-PDFs/Anthropic/Papers/Sabotage_Evaluations_for_Frontier_Models_2410.13161.pdf` (wrong arXiv ID in stem preserved to avoid breaking JSON references)
3. Moved bad extract → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/Anthropic-Sabotage_Evaluations_for_Frontier_Models_2410.13161--BAD-EXTRACT.md`
4. Regenerated extract → `PDF Extracts/AI Labs/Anthropic-Sabotage_Evaluations_for_Frontier_Models_2410.13161.md` (69 pages, 181KB, PyMuPDF 1.26.5)
5. Moved bad vault card → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/AI-Labs-vault-card-Sabotage_Evaluations--BAD-CONTENT.md`
6. Regenerated vault card → `AI Labs/Anthropic/Papers/Sabotage_Evaluations_for_Frontier_Models_2410.13161.md` (69 pages, 181KB)

**Note on stem:** The arXiv ID `2410.13161` in the stem is wrong (belongs to the Lattice Gauge paper). The correct ID is `2410.21514`. Stem was intentionally preserved to avoid updating 9+ JSON reference files. A future cleanup pass should rename the stem and update all references. Vault card has `regenerated` note flagging the correct arXiv ID.

---

## Issue 2: Anthropic Sleeper Agents PDF (FIXED)

**Stem:** `Anthropic-Sleeper_Agents_Training_Deceptive_LLMs_2312.00752`

**Verification evidence:**
- Extract file first line: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces" (Albert Gu, Tri Dao)
- arXiv confirmed: `https://arxiv.org/abs/2312.00752` = "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
- Correct arXiv ID for "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training": **2401.05566** (verified via arXiv title match)
- Downloaded PDF title page: "SLEEPER AGENTS: TRAINING DECEPTIVE LLMS THAT PERSIST THROUGH SAFETY TRAINING / Evan Hubinger, Carson Denison, Jesse Mu..." (71 pages)

**Actions taken:**
1. Moved bad PDF → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/Sleeper_Agents_Training_Deceptive_LLMs_2312.00752--BAD-CONTENT.pdf`
2. Downloaded correct PDF from `https://arxiv.org/pdf/2401.05566` → kept at original path `AI-Lab-PDFs/Anthropic/Papers/Sleeper_Agents_Training_Deceptive_LLMs_2312.00752.pdf` (wrong arXiv ID in stem preserved)
3. Moved bad extract → `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/Anthropic-Sleeper_Agents_Training_Deceptive_LLMs_2312.00752--BAD-EXTRACT.md`
4. Regenerated extract → `PDF Extracts/AI Labs/Anthropic-Sleeper_Agents_Training_Deceptive_LLMs_2312.00752.md` (71 pages, 225KB, PyMuPDF 1.26.5)

**No vault card in `AI Labs/Anthropic/Papers/` for this paper** — only the extract file existed.

**Note on stem:** arXiv ID `2312.00752` is wrong (belongs to Mamba). Correct ID is `2401.05566`. Stem preserved to avoid reference breakage.

---

## Issue 3: Anthropic Simple Probes Detect Sycophancy PDF (BLOCKED)

**Stem:** `Anthropic-Simple_Probes_Detect_Sycophancy_2406.09569`

**Verification evidence:**
- Extract file first line: "Speech ReaLLM — Real-time Streaming Speech Recognition with Multimodal LLMs by Teaching the Flow of Time" (Seide et al., Meta)
- arXiv confirmed: `https://arxiv.org/abs/2406.09569` = "Speech ReaLLM -- Real-time Streaming Speech Recognition..."
- The arXiv ID `2406.09569` is definitively WRONG for this paper.

**Correct source:** Unknown. Extensive search across:
- arXiv search: "simple probes detect sycophancy", "probes sycophancy anthropic", "simple linear probe sycophancy LLM"
- Semantic Scholar API
- Anthropic research page
- Several 2406.XXXXX candidate IDs checked
None returned the correct paper. This may be a non-arXiv Anthropic internal report or blog post, or the paper title may differ significantly from the stem name.

**Actions NOT taken (BLOCKED):**
- Bad PDF NOT moved (no correct replacement available)
- Bad extract NOT modified
- Vault card: no vault card exists in `AI Labs/Anthropic/Papers/` for this paper

**Follow-up needed:**
- Locate correct source for "Simple Probes Detect Sycophancy" (check Anthropic blog, GitHub, or alternative arXiv title)
- Once source confirmed: move bad PDF → RECYCLE-BIN, download correct, regenerate extract

---

## Issue 4: Google DeepMind Gemini Safety PDF (BLOCKED)

**Stem:** `Google DeepMind-Gemini_Safety_arxiv_2403.04312`

**Verification evidence:**
- Extract file first line: "arXiv:2403.04312v2 [math.NT] 10 Aug 2024 — DISTRIBUTION OF POWER RESIDUES OVER SHIFTED SUBFIELDS AND MAXIMAL CLIQUES IN GENERALIZED PALEY GRAPHS" (Greg Martin, Chi Hoi Yip)
- arXiv confirmed: `https://arxiv.org/abs/2403.04312` = "Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs" (number theory paper)
- The arXiv ID `2403.04312` is definitively WRONG for any Gemini safety paper.

**Correct source:** Unknown. Search results for "gemini safety evaluation google deepmind 2024" did not identify a specific arXiv paper matching the intended "Gemini Safety" content. This may be:
1. A Google DeepMind technical report not on arXiv
2. Part of the Gemini 1.0 technical report (arXiv:2312.11805) safety sections
3. A paper with a substantially different title

**Actions NOT taken (BLOCKED):**
- Bad PDF NOT moved (no correct replacement available)
- Bad extract NOT modified
- Bad vault card at `AI Labs/Google DeepMind/Papers/Gemini_Safety_arxiv_2403.04312.md` NOT modified

**Follow-up needed:**
- Identify the intended Gemini Safety paper (check Google AI Blog or DeepMind research page)
- Once source confirmed: move bad PDF → RECYCLE-BIN, download correct, regenerate extract and vault card

---

## Issue 5: CCAI/Sycophancy Card Filename Swap (DOCUMENTED ONLY)

**File:** `COOKBOOK/30-EVIDENCE/20260705-ailabs-cards/Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548.card.md`

**Problem:** The card filename says CCAI (2310.13548) but the card content (confirmed in §1 Gist) is the Sycophancy paper ("Towards Understanding Sycophancy in Language Models", Sharma et al., ICLR 2024). arXiv:2310.13548 is indeed the Sycophancy paper, not CCAI. The CCAI paper has a different arXiv ID (2310.04086 or similar).

**The card file already documents this error** in a "NOTE ON FILE NAMING" block in its §1 Gist section.

**Reference map (files that cite the CCAI card stem):**
1. `COOKBOOK/30-EVIDENCE/20260705-card-index.json` — 5 references (stem in 4 arrays + 1 full entry with path)
2. `COOKBOOK/30-EVIDENCE/20260705-ailabs-shortlist.json` — 1 entry
3. `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/ai-lab-practices-part3.json` — 1 entry
4. `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/saturation-discrimination-part2.json` — 1 entry
5. `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/validity-psychometrics-part2.json` — 1 entry
6. `COOKBOOK/30-EVIDENCE/20260705-dossier-assignments/normative-ethics-part5.json` — 1 entry
7. `COOKBOOK/30-EVIDENCE/20260705-batches/L007.json` — 1 entry
8. `COOKBOOK/30-EVIDENCE/20260705-reader-batches.json` — 1 entry
9. `COOKBOOK/30-EVIDENCE/20260705-ailabs-listing.json` — 1 entry (+ 1 entry for Sycophancy with correct stem)
10. `COOKBOOK/30-EVIDENCE/20260705-dossiers/parts/saturation-discrimination-part2.md` — inline citation `[Anthropic-Collective_Constitutional_AI_Democratizing_AI_Alignment_2310.13548]`
11. `COOKBOOK/00-KNOWLEDGEBASE/13-ai-lab-alignment-practices.md` — abbreviated citation `[Anthropic-Collective_Constitutional_AI]`

**Decision:** DO NOT RENAME the card file. The reference count (11 files) is too high for safe batch editing in a housekeeper pass. The card's self-documenting note in §1 Gist adequately flags the mismatch for any reader.

**Follow-up needed:** A dedicated stem-rename pass (scripted, tested on a copy) that:
1. Renames the card file to `Anthropic-Towards_Understanding_Sycophancy_in_LMs_2310.13548.card.md`
2. Updates all 11+ reference files with the new stem
3. Verifies dossier citations resolve to the new file

---

## Summary

| Issue | Status | Action |
|-------|--------|--------|
| Sabotage Evaluations PDF (2410.13161 → 2410.21514) | **FIXED** | PDF replaced, extract+vault card regenerated |
| Sleeper Agents PDF (2312.00752 → 2401.05566) | **FIXED** | PDF replaced, extract regenerated |
| Simple Probes PDF (2406.09569 → ?) | **BLOCKED** | Correct source not identified |
| Gemini Safety PDF (2403.04312 → ?) | **BLOCKED** | Correct source not identified |
| CCAI/Sycophancy card swap | **DOCUMENTED** | 11-file reference map; rename deferred to scripted pass |

## Files Modified

- `AI-Lab-PDFs/Anthropic/Papers/Sabotage_Evaluations_for_Frontier_Models_2410.13161.pdf` — replaced
- `AI-Lab-PDFs/Anthropic/Papers/Sleeper_Agents_Training_Deceptive_LLMs_2312.00752.pdf` — replaced
- `PDF Extracts/AI Labs/Anthropic-Sabotage_Evaluations_for_Frontier_Models_2410.13161.md` — replaced
- `PDF Extracts/AI Labs/Anthropic-Sleeper_Agents_Training_Deceptive_LLMs_2312.00752.md` — replaced
- `AI Labs/Anthropic/Papers/Sabotage_Evaluations_for_Frontier_Models_2410.13161.md` — replaced
- `RECYCLE-BIN/AI-Lab-PDFs-bad-2026-07-05/` — 5 files (2 bad PDFs, 2 bad extracts, 1 bad vault card)
- `logs/20260705-vault-data-fixes.md` — this file (new)
