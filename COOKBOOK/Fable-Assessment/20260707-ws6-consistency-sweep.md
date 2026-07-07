# WS-6 — Cross-Layer Consistency Sweep + Canonical Discrimination-Bar Ruling (Fable, 2026-07-07)

**Method:** an Opus agent extracted every shared numeric standard and term-of-art across
L1 (KB standards docs) / L2 (the six designs) / L3 (operational protocols + preregs), with
verbatim quotes; Fable adjudicated the divergences. Full 17-row matrix in the agent record;
this report keeps the verdicts and the rulings.

## Confirmed CONSISTENT (no action)

X1–X6 semantics across all restatements · Seven Laws mapping · four-way refusal taxonomy ·
canary/contamination composite + <10% obfuscation-ID · 10%-fine-tune probe · ceiling ≠ 1.0 ·
bootstrap B=2,000 / seed 20260707-family pinning in the preregs · CRUX N-arithmetic
(post-correction; the reconciliation lives in the adjudication memo §06-C2 — noted so a
CRUX-prereg-only auditor knows where to find it).

Two citation-hygiene notes: the discrimination bar lives at **KB04 §6 item 2** (everyone
cites "§6.2" as shorthand — harmless, now on record); the ≥10-reps rule is **KB03 §5**.

## The contradictions, adjudicated

### CS-1 (was WS-6 #1 + WS-2a F1–F5 cluster) — the discrimination bar. RULING: canonical operationalization pinned.

The portfolio's central gate ("≥90% of pairs at p<0.01") was cited identically everywhere
but was not one rule: design 01 adds Holm/Bonferroni; KB04/02–06/P0-G2a are raw; no doc
names the test, the clustering unit, or an effect-size floor; and the number's sole
exemplar (NurValues, 91.7% at p<0.001) is absent from the verified literature layer.

**BINDING ruling (pre-data; applies vault-wide unless a design registers stricter):**
1. **Unit:** reps collapse to per-item model means first; items are the clustering unit.
   Rep-level pseudo-replication is prohibited (it makes the bar anti-conservatively easy).
2. **Test:** per-pair Welch t on item-level mean differences (cluster bootstrap acceptable
   substitute), per manipulation.
3. **Separated** = p < 0.01 (raw, preserving the P0 protocol's registered 33/36 arithmetic)
   **AND |standardized mean difference| ≥ 0.30**. The effect-size floor is what stops the
   bar from being a sample-size detector (WS-2a F3) — significance alone no longer counts.
4. **Sensitivity report:** the Holm-corrected separated-count is reported alongside, always.
   Design 01's stricter Holm-gated rule stands as a registered design-local choice,
   labeled as stricter-than-canonical.
5. **Scope:** the bar applies to point-scored tiers only. Distributional/contested tiers
   use the JSD-vs-ceiling headroom criterion (generalizing CRUX's registered form) — this
   dissolves the KB04 §6.2 ↔ contested-band incoherence (WS-2a F5).
6. **Provenance:** until the NurValues card is verified against its source, the 90% figure
   is labeled *pre-registered convention*, not *evidence-derived* (WS-2a F4). Verification
   is a one-card WS-5-style task for the next Opus session.

### CS-2 (was #2) — judge/IRR κ floors vary (0.6 / 0.7 / 0.8) unlabeled. RULING: regime labeling.

The spread is defensible under KB01 Law 4 (clear-cut hazards vs pluralistic constructs) but
no design says which regime licenses its number. Ruling: each design adds one line citing
its Law-4 regime — 0.8 = clear-cut/hazard gold; 0.7 = method-application/derivation scoring;
0.6 = crowd or pluralistic-adjacent judgments. A floor without its regime label is a defect
in future reviews.

### CS-3 (was #3) — dead-cell taxonomy diverged. RULING: back-propagate.

The P0 protocol's three-state coding (live / dead / UNMEASURABLE) and its 40%-live-fraction
PROVISIONAL floor exist only at L3. Ruling: adopt both as the portfolio convention via the
KB addendum (below); the 40% floor is registered as convention (it has no external source).

### CS-4 (was #4) — G3 protocol↔code: already resolved (PS-2). Standing check: the next
Opus session verifies the gates.py patch LANDED before any live P0 run (it has not yet —
it is in the WS-1 blocking package).

### CS-5 — Law-1 capability gate (with WS-2a F6/F9, WS-4-6). RULING: operationalized.

"~40%" / "r<0.40" / "kill threshold from Law 1" are one standard at three precision levels,
and at panel n=5–9 the r has near-vacuous CIs. Ruling: **point |Pearson r| ≥ 0.40 between
the benchmark score and capability PC1 (or the design's stated capability proxy) across the
model panel = red-flag TRIGGER → the axis's discrimination claim is suspended and a
re-scope review convenes; always reported with a bootstrap CI; below-threshold is never
certified as "capability-free" at n ≤ 9.** It is a tripwire, not a test. All docs cite this
operationalization henceforth (CRUX P3-d, 05 P3 gate, KB01 Law 1, KB04 §6-3).

## Delivery vehicle for the KB-layer changes

One new file — `00-KNOWLEDGEBASE/20260707-kb-addendum-fable-assessment.md` — carrying CS-1,
CS-2's regime table, CS-3's taxonomy, CS-5's operationalization, plus the WS-2 KB
corrections; KB01/KB04 (living docs) get a one-line header pointer to it. Opus-executable;
specified in the WS-2 report and the master roadmap.
