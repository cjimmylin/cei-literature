# WCF-Bench Scoring Walkthrough Design

**Date:** 2026-07-14
**Status:** APPROVED AND IMPLEMENTED
**Artifact:** `00-OVERVIEW/20260714-wcf-bench-scoring-walkthrough.html`

## Purpose and boundary

The artifact explains one permitted OPEN-scoring path—from public item metadata through the exploratory reporting funnel—without reproducing any raw bank stem, response, rubric criteria, gold, anchors, or judge prose. It permanently carries:

> **EXPLORATORY MANUSCRIPT PREVIEW · SINGLE-JUDGE · NON-QUOTABLE**

The values are observed descriptive aggregates under the declared Westminster standard. They are not validated final scores, rankings, universal moral scores, or measurements of generic ethics.

## Approved experience

- Six native-button stages form a keyboard-accessible overview, with Previous/Next controls, ArrowLeft/ArrowRight navigation, visible status text, and one dominant active panel.
- Print CSS exposes the complete six-stage sequence without interaction.
- Responsive CSS supports widths at and below 320px, system light/dark preferences, visible focus, and reduced motion.
- Inline HTML/CSS/SVG and minimal vanilla JavaScript keep the page self-contained and offline; there are no external resources or network requests.

## Approved content model

1. Public metadata identifies `COMP-C9-001`, COMPLICIT, Track A, T2, OPEN, and the Llama SUT.
2. The blind-prompt view shows only safe system/scenario paraphrases and explicitly lists withheld rubric, gold, anchors, contestedness, and judge logic.
3. Persisted response evidence is represented only by a safe paraphrase.
4. OPEN scoring, `correct_refusal`, `failure=false`, coverage, and errors remain separate channels.
5. The sole `google/gemini-2.5-flash` judge uses two passes after one SUT call. Permitted KP labels, dimensions, weights, verdicts, and awards show the exact Matter/Manner/End derivation without sensitive prose.
6. Matter `0.7778` is the headline cell score; it is never the three-dimension mean. The funnel records Llama `0.3878`, `213/222` numeric, 9 errors, design-stratified 95% CI `[0.3425, 0.4357]`, then pooled `0.6656` over `607/666` numeric. Errors are missing, never zero.

The closing legend distinguishes mechanical ORDINAL/ANCHOR, state-machine EPISODE, and separately reported/no-headline CONTESTED routes. A visually separate deferred overlay states that cross-family judges, humans, perturbations, and G1–G7 were not run in PPP-1.

## Non-effects

This explanation changes no empirical evidence, accepted paper packet, panel, manifest, gate, ruling, budget, execution-plan milestone, or benchmark/release progress. It grants no paid-call, credential, quotation, publication, release, T4, G6, rerun, or other authority.
