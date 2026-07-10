# Capability Battery Scores — Sources (WALKWORTHY §3.3 / O4 panel, G3 capability-wash)

**Snapshot date:** 2026-07-11
**Companion to:** `20260711-capability-battery-scores.json`
**Purpose:** Auditable per-cell sourcing for the 6-model × 6-benchmark capability battery. Scores feed the G3 Spearman-ρ "capability wash" gate. Min-max normalized per benchmark across the panel; only the *relative capability ordering* is load-bearing. All numbers are provider/leaderboard-reported and approximate — **no cell is fabricated; unavailable cells are `null` with a reason.**

Benchmarks (all "higher is better"): `mmlu_pro`, `gpqa_diamond`, `swe_bench_verified`, `gaia`, `ruler`, `mrcr`.

---

## Score matrix (raw published %)

| Model | MMLU-Pro | GPQA-Diamond | SWE-bench Verified | GAIA | RULER | MRCR | Coverage |
|---|---|---|---|---|---|---|---|
| openai/gpt-4.1 | 80.5 | 66.3 | 54.6 | 49.7 | null | 57.2 | 5/6 |
| google/gemini-2.5-pro | 86.2 | 84.0 | 63.8 | 33.3 | null | 94.5 | 5/6 |
| anthropic/claude-sonnet-4 | 83.8 | 75.4 | 72.7 | null | null | null | 3/6 |
| deepseek/deepseek-chat (V3-0324) | 81.2 | 68.4 | 38.8 | 29.4 | null | null | 4/6 |
| mistralai/mistral-large-2512 → *2411* | 69.7 | 48.6 | null | null | 86.0 | null | 3/6 |
| meta-llama/llama-3.3-70b-instruct | 68.9 | 50.5 | null | null | null | null | 2/6 |

---

## Per-model, per-benchmark sourcing

### openai/gpt-4.1
- **MMLU-Pro = 80.5%** — GPT-4.1 announcement / BenchmarkList aggregation. https://benchmarklist.com/models/openai-gpt-4.1/
- **GPQA Diamond = 66.3%** — OpenAI GPT-4.1 announcement / aggregators. https://openai.com/index/gpt-4-1/ *(non-reasoning model, hence lower than Gemini/Claude.)*
- **SWE-bench Verified = 54.6%** — OpenAI dev guide, standard harness. https://www.helicone.ai/blog/gpt-4.1-full-developer-guide
- **GAIA = 49.7%** — HAL Leaderboard (Princeton), GPT-4.1 (April 2025), Generalist-Agent scaffold. https://hal.cs.princeton.edu/model/GPT-4.1%20(April%202025). *Caveat: agent-scaffolded w/ tools, not bare model; OpenAI did not publish a GAIA number.*
- **RULER = null** — HELM Long Context ran only 2 RULER subtasks at 128k (SQuAD 0.88 / HotPotQA 0.70), not a composite comparable to a single panel-wide RULER score. https://crfm.stanford.edu/2025/09/29/helm-long-context.html
- **MRCR = 57.2%** — OpenAI-MRCR, 2-needle @128k, GPT-4.1 model card (via llm-stats). https://openai.com/index/gpt-4-1/

### google/gemini-2.5-pro
- **MMLU-Pro = 86.2%** — PricePerToken MMLU-Pro leaderboard. https://pricepertoken.com/leaderboards/benchmark/mmlu-pro
- **GPQA Diamond = 84.0%** — Gemini 2.5 Pro dev guide / Google announcement (pass@1). https://www.helicone.ai/blog/gemini-2.5-full-developer-guide
- **SWE-bench Verified = 63.8%** — Google Gemini 2.5 Pro report (agentic/custom harness). https://www.helicone.ai/blog/gemini-2.5-full-developer-guide
- **GAIA = 33.3%** — PricePerToken GAIA leaderboard. https://pricepertoken.com/leaderboards/benchmark/gaia. *Caveat: different scaffold from GPT-4.1's HAL number — see apples-to-oranges note.*
- **RULER = null** — No credible RULER number for Gemini 2.5 Pro. The widely-cited 94.4% @128k RULER figure is **Gemini 1.5 Pro** (a different model) and was NOT used.
- **MRCR = 94.5%** — OpenAI-MRCR @128k. https://www.helicone.ai/blog/gemini-2.5-full-developer-guide

### anthropic/claude-sonnet-4  (May-2025 Claude 4 Sonnet — NOT 4.5/4.6)
- **MMLU-Pro = 83.8%** — vals.ai MMLU-Pro (08-08-2025 run), Claude Sonnet 4 (Thinking). https://www.vals.ai/benchmarks/mmlu_pro-08-08-2025
- **GPQA Diamond = 75.4%** — Anthropic Claude 4 announcement, **extended-thinking** figure (70.0% without extended thinking). https://www.anthropic.com/news/claude-4
- **SWE-bench Verified = 72.7%** — Anthropic Claude 4 announcement, bash+file-edit scaffold, no extended thinking (80.2% high-compute parallel variant). https://www.anthropic.com/news/claude-4
- **GAIA = null** — Anthropic did not publish GAIA for Sonnet 4; not on HAL/HF GAIA leaderboards. (Sonnet 4.5 appears at 74.55% but is a *different model* — not used.)
- **RULER = null** — Anthropic does not publish RULER; not in HELM's 10-model set.
- **MRCR = null** — The May-2025 Claude Opus 4 & Sonnet 4 system card does not include MRCR (Anthropic began reporting MRCR only with 4.5/4.6).

### deepseek/deepseek-chat  (resolves to DeepSeek-V3-0324, the current deepseek-chat)
- **MMLU-Pro = 81.2** — DeepSeek-V3-0324 model card. https://huggingface.co/deepseek-ai/DeepSeek-V3-0324
- **GPQA = 68.4** — DeepSeek-V3-0324 model card (reported as "GPQA"; treated as Diamond consistent with DeepSeek's convention). https://huggingface.co/deepseek-ai/DeepSeek-V3-0324
- **SWE-bench Verified = 38.8%** — Third-party OpenHands run of DeepSeek-V3-0324 (OpenHands lead X post); NOT a DeepSeek-published number. https://x.com/xingyaow_/status/1904616829508846060
- **GAIA = 29.4%** — HAL Leaderboard, DeepSeek V3 (March 2025), Generalist-Agent scaffold. https://hal.cs.princeton.edu/model/DeepSeek%20V3%20(March%202025)
- **RULER = null** — DeepSeek-V3 report uses NIAH / LongBench-v2 / FRAMES, not RULER.
- **MRCR = null** — No published OpenAI-MRCR number.
- *Note:* the original Dec-2024 DeepSeek-V3 scored MMLU-Pro 75.9 / GPQA 59.1; the current `deepseek-chat` is the improved 0324 build (81.2 / 68.4), which is what the OpenRouter slug resolves to.

### mistralai/mistral-large-2512  → SUBSTITUTED: Mistral Large 2 / 24.11 (mistral-large-2411)
- **MMLU-Pro = 69.7** — vals.ai / Artificial Analysis for Mistral Large 2411. https://www.vals.ai/models/mistralai_mistral-large-2411
- **GPQA (Diamond) = 48.6** — vals.ai / Artificial Analysis for Mistral Large 2411. https://www.vals.ai/models/mistralai_mistral-large-2411
- **SWE-bench Verified = null** — Not on swebench.com; vals.ai has no SWE-bench Verified number. (Mistral's coding model Devstral scores 46.8% but is a *different model* — not used.)
- **RULER = 86.0 (average)** — NVIDIA RULER leaderboard for Mistral Large 2411 (4K 96.4 … 64K 85.9 … 128K 48.1). https://github.com/NVIDIA/RULER. *Caveat: verify against the repo README before any headline use; the rendered table wasn't directly extractable in-fetch.*
- **MRCR = null** — No published OpenAI-MRCR number.
- **SUBSTITUTION NOTE:** the Dec-2025 `mistral-large-2512` build has no separately-published benchmark numbers; all cells use the closest published version (24.11 / 2411). Assuming 2512 ≥ 2411 in capability, this is conservative and does not invert the panel ordering (Mistral is near the bottom regardless).

### meta-llama/llama-3.3-70b-instruct
- **MMLU-Pro = 68.9** — Meta Llama 3.3 model card / Artificial Analysis (5-shot CoT). https://artificialanalysis.ai/models/llama-3-3-instruct-70b
- **GPQA Diamond = 50.5** — Meta Llama 3.3 model card. https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
- **SWE-bench Verified = null** — No canonical Llama 3.3 70B submission. (SWE-RL paper ~12.2% greedy / ~44.6% majority-vote are research settings, not comparable; a ~54.6% blog figure is uncorroborated — not used.)
- **GAIA = null** — No entry on HAL / HF / Artificial Analysis.
- **RULER = null** — Llama **3.1** 70B has RULER numbers but Llama **3.3** does not; not substituted across versions.
- **MRCR = null** — No published OpenAI-MRCR number.

---

## Cross-cutting caveats (see JSON `caveats[]` for canonical text)

1. **Mistral 2512→2411 substitution** — closest published build; conservative for ranking.
2. **GAIA is apples-to-oranges** — GPT-4.1 (49.7%) & DeepSeek (29.4%) from HAL Generalist-Agent scaffold; Gemini (33.3%) from PricePerToken's leaderboard (unknown scaffold). GAIA is heavily scaffold-dependent, so the GPT-4.1 > Gemini GAIA ordering is **not reliable**. Low-confidence column; contributes only 1 of 5-6 cells per model.
3. **SWE-bench harness variance** — provider self-reported scaffolds (GPT-4.1, Claude) vs Google agentic (Gemini) vs third-party OpenHands (DeepSeek). Ordering (Claude > Gemini > GPT-4.1 > DeepSeek) is stable and matches reputation.
4. **RULER effectively non-load-bearing** — only Mistral Large 2411 has a clean composite (86.0). A single non-null cell cannot inform cross-model ranking; consider dropping RULER from G3 or flagging coverage=1.
5. **MRCR context = 128k** for all reported cells (GPT-4.1 2-needle 57.2%; Gemini 94.5%).
6. **Claude thinking mode** — GPQA 75.4% & MMLU-Pro 83.8% are thinking-enabled; note if the panel runs Sonnet 4 without extended thinking (GPQA drops to 70.0%).
7. **deepseek-chat = V3-0324** (81.2 / 68.4), not the original Dec-2024 V3 (75.9 / 59.1).
8. **n=6 ⇒ ρ is noisy** — report the permutation p-value alongside ρ; treat the *ranking* as the load-bearing output.

---

## Implied capability ranking (min-max normalized per benchmark, mean over each model's available cells; RULER excluded as a single-value column)

| Rank | Model | Normalized composite |
|---|---|---|
| 1 | anthropic/claude-sonnet-4 | 0.873 |
| 2 | google/gemini-2.5-pro | 0.786 |
| 3 | openai/gpt-4.1 | 0.527 |
| 4 | deepseek/deepseek-chat | 0.318 |
| 5 | meta-llama/llama-3.3-70b-instruct | 0.027 |
| 6 | mistralai/mistral-large-2512 (→2411) | 0.023 |

**Sanity read:** two frontier models on top (Claude ≈ Gemini), GPT-4.1 a clear mid (strong knowledge, non-reasoning → weaker GPQA/MRCR relative to frontier), DeepSeek-V3 the strongest open model, and the two smaller/older open models (Llama 3.3 70B, Mistral Large) at the bottom — consistent with general capability reputation. The Claude > Gemini flip is partly an artifact of Claude's coverage excluding GAIA (its weakest-measured area is simply unmeasured) and its strong SWE-bench; the frontier pair should be read as roughly co-equal. The frontier-vs-open gap and the bottom two are robust.
