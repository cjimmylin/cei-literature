# 00 — Master Assessment & Roadmap (Fable final-window review of the COOKBOOK core, 2026-07-07)

> **Read this first.** Consolidates all six workstream reports (WS-1…WS-6, this folder)
> into one defect register and one prioritized future-work roadmap. Authored by Fable
> inside the closing window; all adjudications here are BINDING under the exit-sequencing
> memo's authority rules. **This document supersedes the session-1 task list in
> `COOKBOOK/20260706-PARKED-opus-reentry-prompt.md`** (the park prompt is otherwise
> unchanged and is still the re-entry vehicle; read it after this).

## 1. Executive verdict

The cookbook's intellectual architecture survives adversarial assessment: the six designs
are sound post-gate, the item bank is approved, the evidence layer is trustworthy under
sampling (0 fabrications in 26 cards; digests trace exactly), the drafting artifacts are
strong, and the sketch portfolio has eight viable concepts. **The two places the cookbook
was silently broken were both in the seams:**

1. **Code↔spec (WS-1): the DUPLEX-P0 runner was believed "one config flag from live" and
   is in fact NOT run-ready** — 12 blocking divergences (G3 on the wrong item population;
   the M3 fallback never wired; G1 baseline/matching/deltas all off-spec; polarity
   reverse-scoring never applied; refusals eating the preserve pole; frames never rendered;
   non-deterministic seeds; missing nulls). Green tests hid all of it because the tests
   encoded the code's reading of the spec, not the spec. A credentialed P0 run before this
   assessment would have produced silently invalid verdicts on the portfolio's
   fork-deciding gate.
2. **Doc↔doc (WS-2/WS-6): the standards layer under-operationalized its central gates**
   (the §6.2 discrimination bar had no test, no clustering unit, no effect-size floor, and
   a correction contradiction between design 01 and everything else) **and the KB's
   embedded design briefs are stale against the shipped designs** (six MAJORs — a builder
   grounding on KB briefs would build the wrong benchmarks).

Both classes are now closed by binding rulings (CS-1…CS-5, the WS-1 dispositions) and a
well-defined Opus fix queue (§3). Nothing found requires Jimmy-level redesign; nothing
found kills a design.

**Finding totals (adjudicated):** 2 near-KILL candidates adjudicated to MAJOR-with-ruling
(both pre-data, hence repairable: the §6.2 bar-as-sample-size-detector; the P0 runner
divergence cluster) · ~30 MAJOR · ~35 MINOR · 5 binding cross-cutting rulings · 0 sustained
KILL. Per-domain verdicts: WS-1 runner NOT-RUN-READY / ENGINE sound-with-2-fixes · WS-2 KB
strong-spine, 4 defect classes · WS-3 sketches all viable, priority set · WS-4 drafts fit
after 1 fix · WS-5 evidence layer TRUSTWORTHY · WS-6 13/16 seams clean, 3 amended.

## 2. The binding rulings issued by this assessment (Opus/Jimmy may not relitigate)

- **CS-1** Canonical discrimination bar: item-level clustering; Welch/bootstrap per pair;
  separated = raw p<0.01 **AND** |standardized Δ| ≥ 0.30; Holm count co-reported; bar
  applies to point-scored tiers only (distributional tiers → JSD headroom); 90% labeled
  convention pending NurValues verification. (WS-6)
- **CS-2** κ floors must carry their Law-4 regime label (0.8 hazard / 0.7 method / 0.6
  crowd-pluralistic). (WS-6)
- **CS-3** Three-state cell taxonomy (live/dead/UNMEASURABLE) + 40%-live PROVISIONAL floor
  = portfolio convention. (WS-6)
- **CS-5** Law-1 capability gate = |r| ≥ 0.40 point-estimate TRIPWIRE with bootstrap CI,
  never a capability-free certificate at n ≤ 9. (WS-6)
- **WS-1 dispositions** D1–D16/ENG-1…4 as graded, including the consolidated P0
  run-precondition checklist (WS-1 §1) — the single authoritative pre-run list.
- **WS-2 adjudications** incl. the SUPERSEDED-banner mandate on all four KB §6 briefs.
- **IB-1…5, PS-1…6** (2026-07-06) unchanged and incorporated by reference.

## 3. The Opus fix queue (supersedes park-prompt session 1)

**Session A — P0 runner rebuild (the new session 1; 1–2 sessions).**
Execute WS-1 §1's consolidated checklist: G3 package (PS-2 + D1 + D2 + IB-2 sensitivity),
G1 package (D3–D7 + content-axis wiring + three-state cells), D8 frames + X3 gap statistic,
D9 polarity-at-scorer, D10 refusal reclassification, D11 hashlib seeds + resume test,
D12 null baselines, IB-1a/IB-3a/IB-5 analysis wiring, D14 fail-loud. Method requirement:
**every fix lands with a spec-quoting test** (the A1/A2 discipline) — not a test of the new
code, a test of the spec sentence. Deliverable: updated suite green + a checklist-evidence
table appended to the pilot-report lane.

**Session B — KB fix pass + small fixes (1 session).**
The WS-2 vehicle: `00-KNOWLEDGEBASE/20260707-kb-addendum-fable-assessment.md` (CS rulings,
X2-probe operationalization, MDES mandate, envelope rename, primary-divergence rule,
registered conventions) + four SUPERSEDED banners + the point-fix list (KB09 caveats, KB10
VOID/45-47, KB11 caveat-at-use, landscape #14 verbatim fix, dated perishables, etc.) +
the verification list (NurValues card ✓still-open, Boddington/MEC stem, ConflictScope
extract pull, CCAI-rename residue; Stiennon CLOSED by WS-5 — source confirmed) + WS-5's
E-1/E-2/E-3 card fixes and the E-4 vault backfill + WS-4's fixes (02-sheets novelization
instruction ¶, 04 sizing floors, 05 instrument guard).

**Session C — ENGINE pre-P1 fixes (half session; may fold into A or B).**
ENG-1 factor-visibility (all 6 factors render + per-factor surface-diff test) and ENG-2
distinct-cells + id-uniqueness (+ regenerate `out/`, README disclosure). BLOCKS CRUX P1
instance generation and therefore the validation survey. ENG-3/4 at P1 build proper.

**Then the park prompt's original sequence resumes:** credentials → P0 (now genuinely
run-ready) → surveys on greenlight → CRUX P1 after prose-enrichment+ENG fixes.

## 4. Future-work source list (beyond fixes — the "ways to improve" the user asked for)

1. **Sketch build order** (WS-3): S5 BARGAIN → S2 BACKBONE → S8 LEVER → S4 TEND → S3
   QUORUM → S7 CHORUS (rises if CRUX branch fires) → S1 DRIFT; S6 stays merged into 01.
2. **The verdict-vs-coherence axis** (WS-2/KB08): the dropped answer-key-free,
   contamination-resistant scoring family — the best un-built idea in the KB. Candidate
   addition to FRAMESHIFT P2 or a standalone sketch S12.
3. **`source_depth` tagging** for cards built on abstract-only records (WS-5 E-5 pattern).
4. **Standing audit order:** every gate-computing artifact gets an A1/A2 code-vs-spec
   audit by a non-building agent before its first real run (WS-1 §3); every derived doc
   (KB briefs, drafts) gets a SUPERSEDED banner check whenever its parent design changes.
5. **MDES/power statements** become part of every design's first live-run prereg (F18).

## 5. Jimmy's list (unchanged by this assessment, consolidated)

Credentials (Anthropic key, Codex OAuth, Google decision) · survey greenlights (G3
mini-norm, CRUX P1) · recruitment (G3 humans, 04 boards, 05 partners/panels, TC panels
etc.) · CORINTHLOVE c–f commit approval · S9–S11 import sign-off + virtue-account pick ·
WS-4 §4 confirm-list. **Nothing in this assessment added a Jimmy-blocking item** — every
fix is Opus-executable.

## 6. Report index

WS-1 code-vs-spec (runner NOT-RUN-READY; ENGINE 2 fixes) · WS-2 knowledgebase (4 defect
classes, fix vehicle) · WS-3 sketch triage (priority order + S9–S11 ruling) · WS-4 drafts
deep-read (1 MAJOR; Jimmy confirm-list) · WS-5 evidence audit (TRUSTWORTHY; 5 small fixes)
· WS-6 consistency sweep (CS-1…CS-5). Grading and authority conventions in README.md.
