# WCF-Benchmark-v2 — Session 8 addendum: minimax-m3 epochs×3 on the frontier core

> Live OpenRouter run (owner-authorized 2026-07-17). EXPLORATORY / NON-QUOTABLE;
> rubric conformity on bank v2.4, not accuracy. Resolves the one dangling
> comparison carried from session 7.

## The question

Session 7 measured **minimax-m3 = 80.45 on the 66-item frontier core from a
single draw** (roster-main), while the trio gpt-5-mini / qwen / claude-haiku-4.5
were measured **epochs-averaged (×3)**. Single-draw carries wider per-item noise
than an epochs-averaged mean, so "minimax 80.45 > gpt-5-mini 78.39" was **not a
comparable ordering** (s7 report §Phase-4-track-3). This run grades minimax
under the identical frozen config so the two means are comparable.

## Config (identical to the s7 epochs-core run — verified from the .eval header)

- Task `wcf_frontier_core` (66 `-N-` items), `--epochs 3` → 198 samples.
- Grader panel = median of gemini-2.5-flash + deepseek-chat + mistral-small-2603
  (the v2.2 DEFAULT_GRADER), `excellence_gate=true`, grader temperature 0.0.
- Grader retry wrapper `GRADER_ATTEMPTS=3` (last-match `GRADE: N` parser).
- SUT `openrouter/minimax/minimax-m3`.
- **Audit: 0/198 unscored; 1/198 quorum drop (n_valid<3, single gemini
  transient absorbed by the wrapper).**

## Result — the top of tier-1 is a dead heat

Epochs-averaged core means (per-item averaged over 3 epochs before any statistic):

| SUT | core mean (66 items, epochs×3) | SE |
|---|---|---|
| **minimax-m3** | **79.63** | 1.60 |
| gpt-5-mini | 78.39 | 2.17 |
| qwen3.7-plus | 75.33 | 1.64 |
| claude-haiku-4.5 | 72.48 | 1.63 |

Paired per-item (epochs-averaged), MDD80 = 2.80×SE of the paired differences
(s7 convention; scale is bank v2.4, not cross-bank quotable):

| Pair | gap | SE | MDD80 | verdict |
|---|---|---|---|---|
| minimax − gpt-5-mini | +1.24 | 2.06 | 5.78 | **ns** |
| minimax − qwen | +4.30 | 1.66 | 4.64 | ns |
| minimax − haiku | +7.14 | 2.00 | 5.59 | **SIG** |

## Reading

1. **minimax-m3 and gpt-5-mini are statistically tied at the top of the
   frontier core** (gap +1.24 ≪ MDD80 5.78). The s7 single-draw lead **dissolves
   under comparable epochs measurement** — 80.45 single-draw → 79.63 epochs
   (a mild single-draw over-estimate, as expected from the wider single-draw
   noise). There is no resolved minimax-over-gpt-5-mini ordering.
2. **minimax > haiku is resolved and significant** (+7.14, SIG), mirroring the
   session-7 headline gpt-5-mini > haiku (+5.90, SIG). Two different top-tier
   models now clear haiku on this core by a significant margin — the frontier
   core separates the very top from haiku consistently, regardless of which
   top model is the reference.
3. Per-design (minimax): aggravate 73.3 (the hardest core slice) < complicit
   86.3 < steadfast 88.4 — the aggravation-calculus items remain the core's
   discriminating floor.

## Bottom line

The tier-1 frontier is a **three-way top cluster** — minimax-m3 ≈ gpt-5-mini,
both ns vs each other and both clearing haiku (minimax SIG; gpt-5-mini SIG per
s7) — with qwen a half-step below (ns vs both). The only *resolved* within-core
orderings remain the gpt-5-mini > haiku and now minimax > haiku gaps; the top
two are not separable at this power. Resolving minimax-vs-gpt-5-mini would need
more per-item information (more epochs or a harder-core expansion), not more
SUTs.

_Stats: `analysis/20260717-session8-minimax-core-stats.json`. Log:
`logs/20260717-session8-minimax-epochs-core/`. Bank v2.4 · panel
median(gemini-2.5-flash, deepseek-chat, mistral-small-2603) · parser last-match
GRADE: N · excellence_gate=true · GRADER_ATTEMPTS=3._
