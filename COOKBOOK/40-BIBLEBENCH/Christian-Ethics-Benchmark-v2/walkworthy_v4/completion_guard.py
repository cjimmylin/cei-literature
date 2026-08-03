"""v4-A 2(b) — empty/truncated-completion exclusion, BOTH halves (20260731o §6.2).

Defect: 26 of 525 v4-C axis samples (5.0 pct) carried empty final completion text;
only 3 were routed unscorable — the rest were SCORED on empty text, including 14
d08 passing guardrail verdicts, manufacturing most of d08's apparent judge
disagreement. The gpt5/deepseekr1 empties carry stop_reason max_tokens with the
whole 8192 budget spent on reasoning; gemini's carry stop_reason unknown.

Half (a) — scoring side: `check_completion` classifies a stored SUT output before
any judge call; empty and budget-truncated completions route to unscorable with an
explicit exclusion reason (they are SUT-side attrition, disclosed as counts, and
never reach a judge). Consumers: tools/rescore/rescore.py and every v4-line scorer.

Half (b) — administration side: `escalated_cap` is the one-shot re-administration
policy. When a generation stops on max_tokens with an empty (or truncated) visible
completion, the runner re-administers ONCE at an escalated output cap so the answer
stops being lost to reasoning-budget exhaustion. B1 must not launch without this
policy wired into its runner (20260731o §7 item 3).

Pinned v3 components are not modified; this module is v4.0-line code (spec
20260731j §5.1) and is import-only from the pinned tree's perspective.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

# stop_reason spellings observed across providers in the v4-C/v4-T run trees.
_BUDGET_STOP_REASONS = {"max_tokens", "length", "model_length"}

# spec §4.3 output caps: 8192 (reasoning SUTs) / 4096. The escalation ceiling is
# one doubling above the reasoning cap — a second doubling has no evidence base
# and re-administration is deliberately single-shot.
ESCALATION_FACTOR = 2
ESCALATION_CEILING = 16384

# marker key recorded wherever a completion was excluded pre-judge (audit
# trail). Underscore-prefixed: consumers that split verdict keys from meta keys
# on the "_" prefix (tools/rescore/rescore.py) route it into _judge_meta.
COMPLETION_EXCLUDED = "_completion_excluded"


@dataclass(frozen=True)
class CompletionCheck:
    status: str                # "ok" | "empty" | "truncated"
    scorable: bool             # False -> route to unscorable, never judge
    reason: Optional[str]      # human-readable exclusion reason, None when ok


def check_completion(text: Optional[str], stop_reason: Optional[str] = None) -> CompletionCheck:
    """Classify a stored SUT completion before scoring/judging.

    - empty/whitespace text -> "empty" (unscorable), whatever the stop_reason
      (covers gpt5/deepseekr1 max_tokens empties AND gemini stop_reason-unknown
      empties).
    - non-empty text that stopped on a budget stop_reason -> "truncated"
      (unscorable): the visible answer is cut mid-generation and judging partial
      text is exactly the §6.2 defect.
    - otherwise -> "ok" (scorable).
    """
    stripped = (text or "").strip()
    sr = (stop_reason or "").strip().lower() or None
    if not stripped:
        detail = f" (stop_reason={sr})" if sr else ""
        return CompletionCheck("empty", False, "empty completion" + detail)
    if sr in _BUDGET_STOP_REASONS:
        return CompletionCheck("truncated", False,
                               f"truncated at output cap (stop_reason={sr})")
    return CompletionCheck("ok", True, None)


def excluded_meta(check: CompletionCheck, cap_escalated: bool = False) -> dict:
    """The audit record a consumer stores in place of a judge verdict.

    All keys are underscore-prefixed (see COMPLETION_EXCLUDED note).
    """
    return {
        COMPLETION_EXCLUDED: check.status,
        "_completion_reason": check.reason,
        "_cap_escalated": bool(cap_escalated),
        "_attempts": 0,
    }


def escalated_cap(stop_reason: Optional[str], text: Optional[str],
                  current_cap: int,
                  ceiling: int = ESCALATION_CEILING) -> Optional[int]:
    """Administration half: decide the single re-administration cap.

    Returns the new max_tokens for a ONE-time re-run when the completion was lost
    (or cut) to budget exhaustion, else None. Never escalates past `ceiling`, and
    never re-escalates a run already at or above it (single-shot by design).
    """
    check = check_completion(text, stop_reason)
    if check.status == "ok":
        return None
    sr = (stop_reason or "").strip().lower()
    if sr not in _BUDGET_STOP_REASONS:
        # empty for a non-budget reason (e.g. gemini stop_reason unknown): a
        # bigger cap has no mechanism to help; re-administration policy for
        # those is a plain retry at the SAME cap, signalled by current_cap.
        return current_cap if check.status == "empty" else None
    if current_cap >= ceiling:
        return None
    return min(current_cap * ESCALATION_FACTOR, ceiling)
