# Expert 12 — Meta-Critique / Sprint Historian

**Role:** Sprint continuity auditor, plan-vs-execution alignment reviewer
**Scope:** Verify S18 council item dispositions, sprint tracker alignment, and Appendix K adequacy for v2.2-preliminary

---

## (a) The 4 MUST-DO Items from S18 Council — Are They Addressed in v2.2?

The S18 council identified four MUST-DO verdicts:

1. **A1 Dashboard URLs (12/12 MUST):** Fully resolved. Abstract, conclusion, and new data-availability statement all edited with v1/v2/v3 URLs. Grep-verified. The briefing correctly lists v4 as an additive task (add once deployed). No gap.

2. **A5 FAIR/Zenodo (11/12 MUST):** Partially addressed. The reproducibility scaffolding (LICENSE, CITATION.cff, .zenodo.json skeleton) was completed in S18 Day 2. However, the actual deposit assembly, DOI acquisition, and Data Availability Statement insertion remain open. The sprint tracker still shows all A5 sub-items unchecked. The v2.2 briefing lists "Zenodo deposit finalization" under Priority 3 safe work. **Status: structurally started, substantively incomplete.** This is correctly flagged as active.

3. **A6 Word Count (6 MUST + 3 SHOULD):** Not started and now PAUSED. The briefing correctly lists "Word count compression" under PAUSED items. However, the sprint tracker still lists A6 as ACTIVE (not paused). This is a **tracker-briefing misalignment**: the briefing says paused (because compression depends on what content stays, which depends on cross-vendor reframe), but the tracker's Action Item Status Map never explicitly paused A6. The sprint tracker Day 1 calendar still shows "A6 (compression start)" as planned. Recommendation: the tracker should be updated to mark A6 as PAUSED with a note that compression targets cannot be set until the Paper A vs. A+B structure and cross-vendor content decisions are made.

4. **A7 Prompt Release (9/12 MUST):** Scoped down to Anthropic-only prompts. Prompt sourcing report completed. Appendix K skeleton is listed under Priority 3 safe work. The briefing correctly identifies this as active but partial. The S18 handoff notes "PARTIAL completeness, LOW blocker risk for Anthropic scope." **However, the 9 sub-items from Expert 7's original spec (Codex wrapper config, GPT-5 variations, carbon/cost reporting) are meaningless in an Anthropic-only scope.** The v2.2 plan needs to explicitly redefine what Appendix K contains for the preliminary version vs. the full version.

**Verdict:** 1 of 4 fully resolved. 3 are in various states of partial completion, all correctly identified as active or scoped-down. The A6 tracker status is stale.

---

## (b) SHOULD-DO and DEFER Items — Correctly Listed as Paused?

| Item | Council Verdict | Briefing Status | Correct? |
|------|----------------|-----------------|----------|
| A2 Gemini T>0 | SHOULD-DO (5/12) | Paused | Yes |
| A4 IRR study | SHOULD-DO (7/12) | Not mentioned in briefing pause list | **Ambiguous** |
| A8 2+1 profiles | SHOULD-DO (6/12) | Paused | Yes |
| A3 Paper identity | DEFER-WITH-FRAMING (6/12) | Paused (except completed section 6.1) | Yes |
| T1-T5 replication | DEFER-TO-FUTURE (7/12) | Not in sprint | Yes |

**A4 is the concern.** The IRR study (feature-scoring inter-rater reliability) was voted SHOULD-DO by 7/12 experts. The sprint tracker lists it as ACTIVE (not paused). The briefing does not mention it under paused items, nor under Priority 3 safe work. The S18 handoff lists it under Priority 1 ("if using LLM raters") but also under Priority 2 (blocked). The user's directive to pause "any more model analyses" could be read to include LLM-based IRR raters but not human raters. A4 needs explicit triage: if human raters are available, it is model-independent and should proceed; if the fallback 3-LLM panel is the only option, it is model-dependent and paused. The current documents are silent on this distinction.

---

## (c) Sprint Tracker Calendar Alignment with Session 19

The tracker's Day 1 (2026-04-13) planned: "Launch A1, A5 (deposit prep), A6 (compression start), A3 (reframe), vendor disclosure letters."

What actually happened by S18 end: A1 done, A3 partially done (section 6.1 only), A5 scaffolding only, A6 not started, vendor disclosure letters not started. The progress log entries already document the pivot.

Session 19 (also 2026-04-13) is launching a dashboard v4 + paper v2.2-preliminary council. This is NOT reflected anywhere in the sprint tracker calendar, which still shows the original pre-pivot plan. The tracker needs a new entry acknowledging that the sprint has been restructured around the v2.2-preliminary framing, with dashboard v4 and 10 missing references as the active deliverables.

**The calendar is stale.** Days 2-14 are the original plan and no longer operative. The tracker's "Progress Log" section is being used correctly for actuals, but the calendar table gives a false impression of what is planned.

---

## (d) S18 "Resolved" Items That May Need Revisiting

Three items were marked resolved in S18 that deserve scrutiny under v2.2-preliminary framing:

1. **A9 Elicitation disclosure (section 6.1):** Marked complete, and the disclosure text is described as honest. However, the v2.2 briefing introduces a new labeling regime: every cross-vendor figure/table gets `[simulated -- awaits external validation]` inline flags. The existing section 6.1 disclosure may need to cross-reference these inline markers so the reader understands the two-layer flagging system (inline tags + limitations narrative). Minor revision, not a rewrite.

2. **A1 Dashboard URLs:** Complete for v1/v2/v3. But v2.2 introduces v4 as a new deliverable. The data-availability statement will need updating once v4 is deployed. This is acknowledged in the briefing ("add v4 once deployed") but should be tracked as an open sub-item of A1, not assumed done.

3. **A3 section 6.1 exploratory positioning:** The inserted paragraph positions the paper as exploratory. Under v2.2-preliminary, the framing shifts further: cross-vendor results are not just exploratory but explicitly simulated. The exploratory-positioning paragraph and the elicitation-disclosure paragraph in the same section need to be read together for coherence. No one has checked whether the two paragraphs (inserted independently by different agents) create a consistent narrative or redundant/conflicting framings.

---

## (e) Is the Appendix K Plan Adequate for the Prompt-Provenance Gap?

The S18 handoff identifies a significant gap: the root CLAUDE.md (the system prompt that shaped Opus trial behavior) is NOT git-tracked. The prompt sourcing report rates Anthropic prompt completeness as PARTIAL. The assessment prompts for Sonnet and Haiku require "post-hoc reconstruction with explicit disclosure."

The Appendix K plan as currently described is a skeleton with placeholder sections. This is inadequate for v2.2-preliminary for three reasons:

1. **Provenance chain is broken.** The system prompt that governed trial behavior cannot be verified as identical to the current version. Appendix K must state this explicitly, with the git commit hash of the closest recoverable version and a disclosure of what may have changed.

2. **Reconstruction vs. archival distinction is missing.** The plan says "labelled reconstruction and gaps disclosure" but does not specify what format this takes. Best practice: each prompt in the appendix should carry a provenance tag: `[verbatim archive]`, `[git-recovered, commit HASH]`, or `[reconstructed, see disclosure]`. Without this taxonomy, a reviewer cannot assess which prompts are trustworthy.

3. **Cross-vendor prompts are undefined.** When external model runs eventually happen, those prompts will need to be archived in Appendix K too. The skeleton should reserve sections for non-Anthropic prompts with `[pending external administration]` placeholders, so the appendix structure is stable across the preliminary-to-final transition.

**Recommendation:** Appendix K should be promoted from Priority 3 to Priority 2. It is the primary transparency mechanism for the prompt-provenance gap, and a reviewer evaluating the v2.2-preliminary will look here first when assessing whether the Anthropic-only results are reproducible.

---

## Summary of Findings

| Check | Status |
|-------|--------|
| 4 MUST-DOs addressed? | 1/4 fully done; 3/4 partial but correctly tracked (except A6 tracker is stale) |
| SHOULD/DEFER correctly paused? | Mostly yes; A4 (IRR) disposition is ambiguous |
| Sprint calendar aligned with S19? | No -- calendar is pre-pivot; S19 council not reflected |
| Any "resolved" items need revisiting? | 3 minor: A9 cross-ref to inline flags, A1 v4 sub-item, A3+A9 coherence check |
| Appendix K adequate? | No -- needs provenance taxonomy, git-recovery disclosure, and cross-vendor placeholders |

**Word count:** ~1,340
