# Expert 09 — Figure/Table Design Review

**Perspective:** Figure and table design, caption accuracy, cross-reference integrity
**Date:** 2026-04-13 | **Scope:** Paper v2.2-preliminary figure audit

---

## A. Inventory of PNG Figures in `PAPER-v2/figures/`

12 PNG files exist (8 main, 4 supplementary):

| File | Type per Spine | Section | Contains Simulated Data? |
|------|----------------|---------|--------------------------|
| fig1-tradition-heatmap.png | Heatmap (54x5) | 4.1 | No |
| fig2-framework-difficulty.png | Grouped bar | 4.3 | No |
| fig3-nd-vs-pe-scatter.png | Bubble scatter | 4.1 | No |
| fig4-data-availability.png | Stacked bar | 4.1 | No |
| fig5-trial-accuracy-discriminative.png | Paired bar | 4.3 | No |
| fig6-ih-ib-scaling.png | Grouped bar | 4.6 | **YES** |
| fig7-cross-vendor-heatmap.png | Heatmap (8x8) | 4.6 | **YES** |
| fig8-knowledge-judgment-divergence.png | Dumbbell | 4.6 | **YES** |
| figS1-pca-clusters.png | Supplement | App. I | No |
| figS2-temporal-trends.png | Supplement | App. I | No |
| figS5-provider-radar.png | Supplement | -- | **YES** |
| figS6-cbr-by-model.png | Supplement | -- | **YES** |

**Numbering gap:** figS3 and figS4 do not exist. The supplement jumps from figS2 to figS5. This is either intentional (figures were removed) or a numbering error. Recommend renumbering figS5 to figS3 and figS6 to figS4 before submission, or adding a note explaining the gap.

---

## B. Briefing Cross-Check: Which Figures Are Simulated?

The briefing flags fig7, fig8, figS5, and figS6 as simulated, and states fig1-fig6 are Anthropic-only and safe.

**Finding: The briefing is incorrect about Figure 6.** The spine describes fig6 as "IH/IB scaling across 9 models + reference lines" (section 4.6). The cross-vendor results text references Figure 6 for findings F1 (three ethical profiles, 9 models) and F7 (persuasion resistance across 9 models). Both findings include GPT-5, GPT-5-mini, and Gemini data -- all simulated. Figure 6 therefore contains simulated cross-vendor data and MUST receive the `[simulated]` flag.

**Corrected list of figures requiring `[simulated]` flags:**

| Figure | Rationale |
|--------|-----------|
| **fig6-ih-ib-scaling.png** | Shows IH/IB for 9 models including GPT-5, GPT-5-mini, 4 Gemini |
| **fig7-cross-vendor-heatmap.png** | 8x8 pairwise agreement matrix includes all simulated models |
| **fig8-knowledge-judgment-divergence.png** | Knowledge vs. judgment divergence measured across 9 models |
| **figS5-provider-radar.png** | Provider comparison radar -- cross-vendor by definition |
| **figS6-cbr-by-model.png** | Cognitive bias rate by model, includes non-Anthropic models |

Five figures require the flag, not four.

---

## C. Text-to-Figure Cross-Reference Audit

| Text Reference | Location | Figure Exists? | Status |
|----------------|----------|----------------|--------|
| Figure 1 (tradition heatmap) | results-landscape, intro | Yes | OK |
| Figure 2 (framework difficulty) | methods, results-trials, discussion | Yes | OK |
| Figure 3 (ND vs PE scatter) | results-landscape | Yes | OK |
| Figure 4 (data availability) | results-landscape | Yes | OK |
| Figure 5 (accuracy vs discrim.) | results-trials | Yes | OK |
| Figure 6 (IH/IB scaling) | results-crossvendor F1, F7 | Yes | OK |
| Figure 7 (agreement matrix) | results-crossvendor F6 | Yes | OK |
| Figure 8 (knowledge-judgment) | results-crossvendor F4, discussion | Yes | OK |
| Figure S1 (PCA clusters) | appendix-I | Yes | OK |
| Figure S2 (feature heatmap) | appendix-I | Yes | OK |
| Figure S5 (provider radar) | **Not referenced in any body/supplement text** | Yes | ORPHAN |
| Figure S6 (CBR by model) | **Not referenced in any body/supplement text** | Yes | ORPHAN |

**Finding: figS5 and figS6 are orphaned.** No markdown file in PAPER-v2/ references "Figure S5", "Figure S6", "figS5", or "figS6". These figures exist in the directory but are unreachable from body or supplement text. They must either be (a) referenced from the appropriate appendix section (likely Appendix D, which covers T6-T15 cross-vendor trials), or (b) removed from the figures directory if they are redundant with main-body figures.

**No missing figures detected.** Every figure referenced in body text (Figures 1-8, S1, S2) has a corresponding PNG in the figures directory.

---

## D. Recommended Caption Amendments

For each simulated figure, the v2.2-preliminary labeling rule requires the inline flag `[simulated -- awaits external validation]`. Recommended caption wording:

**Figure 6.** Instrumental Harm (IH) and Impartial Beneficence (IB) scores across nine models and three vendors. Dashed lines indicate reference population ranges from Kahane et al. (2012). `[Simulated -- GPT-5, GPT-5-mini, and all Gemini model responses were generated via in-context elicitation by a Claude agent, not via direct API access. Awaits external validation.]`

**Figure 7.** Pairwise item-level agreement matrix for eight models on 114 cross-vendor items (T6-T15). Values indicate percentage agreement; color intensity encodes agreement strength. `[Simulated -- non-Anthropic model responses (GPT-5, GPT-5-mini, Gemini 2.5 Flash/Flash-Lite/Pro, Gemini 3.1 Pro) were generated via in-context elicitation. Awaits external validation.]`

**Figure 8.** Knowledge-judgment divergence across benchmark types. Each row represents one trial (T6-T15); endpoints show minimum and maximum pairwise agreement across the nine-model set. Knowledge benchmarks cluster near 100% agreement while judgment benchmarks span 71-100%. `[Simulated -- includes in-context-elicited responses for non-Anthropic models. Awaits external validation.]`

**Figure S5.** Provider comparison radar showing composite ethical profile dimensions by vendor. `[Simulated -- non-Anthropic provider profiles derived from in-context-elicited data. Awaits external validation.]`

**Figure S6.** Cognitive bias rate (CBR) by individual model on T14 items. `[Simulated -- non-Anthropic model CBR values derived from in-context-elicited responses. Awaits external validation.]`

---

## E. Summary of Issues (Priority-Ordered)

1. **[HIGH] Figure 6 omitted from simulated flag list.** The briefing incorrectly classifies fig6 as Anthropic-only. It shows 9 models across 3 vendors. Must be added to the flagged set.
2. **[HIGH] figS5 and figS6 are orphaned.** No text reference points to them. Add references in Appendix D or the cross-vendor results section.
3. **[MEDIUM] Supplementary figure numbering gap.** figS3 and figS4 are missing. Renumber figS5/S6 to figS3/S4, or document the gap.
4. **[LOW] Caption standardization.** All five simulated figures should use identical bracketed disclosure language for consistency. The wording above can serve as a template.
