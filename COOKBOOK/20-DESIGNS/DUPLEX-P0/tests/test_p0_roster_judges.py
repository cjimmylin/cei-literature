"""Roster loading + cross-family judge routing (§3.5 / KB07)."""
import os

from conftest import CONFIG_ROSTER
from runner.roster import load_roster, enabled_models, all_models, vendor_of
from runner.judges import assign_judges, judge_neutrality_check


def test_roster_loads_and_enables_the_right_vendors():
    roster = load_roster(CONFIG_ROSTER)
    enabled = enabled_models(roster)
    ids = {m["id"] for m in enabled}
    # Anthropic (3) + OpenAI (2) enabled; Gemini (4) present-but-disabled
    assert "claude-opus-4-6" in ids
    assert "claude-sonnet-4-6" in ids
    assert "claude-3-5-haiku-20241022" in ids
    assert "openai/gpt-5-codex" in ids and "openai/gpt-5-mini" in ids  # OpenRouter-prefixed (verified)
    assert len(enabled) == 5
    assert not any(m["vendor"] == "google" for m in enabled)


def test_roster_gemini_present_but_disabled():
    roster = load_roster(CONFIG_ROSTER)
    gem = [m for m in all_models(roster) if m["vendor"] == "google"]
    assert len(gem) == 4
    assert all(m["enabled"] is False for m in gem)
    assert roster["vendors"]["google"]["enabled"] is False


def test_haiku_flagged_retired():
    roster = load_roster(CONFIG_ROSTER)
    haiku = next(m for m in all_models(roster) if m["id"] == "claude-3-5-haiku-20241022")
    assert "RETIRED" in str(haiku.get("status", ""))
    assert "note" in haiku


def test_assign_judges_are_always_cross_vendor():
    roster = load_roster(CONFIG_ROSTER)
    # subject = anthropic -> judges only from openai (gemini disabled)
    for jid in assign_judges("anthropic", roster):
        assert vendor_of(roster, jid) == "openai"
    # subject = openai -> judges from anthropic (judge_eligible only: opus + sonnet)
    an_judges = assign_judges("openai", roster)
    assert set(an_judges) == {"claude-opus-4-6", "claude-sonnet-4-6"}
    for jid in an_judges:
        assert vendor_of(roster, jid) == "anthropic"


def test_assign_judges_eligibility_fallback():
    roster = load_roster(CONFIG_ROSTER)
    # without the judge_eligible filter, Haiku 3.5 (not judge-eligible) is included
    all_an = assign_judges("openai", roster, require_judge_eligible=False)
    assert "claude-3-5-haiku-20241022" in all_an


def test_judge_neutrality_flip_test():
    # neutral judge: equal scores for pro/con -> neutral True
    neutral = judge_neutrality_check(lambda t: 0.8, "pro trace", "con trace", tol=0.05)
    assert neutral["neutral"] is True
    assert neutral["flip_delta"] == 0.0
    # biased judge: favours whichever trace says 'pro'
    biased = judge_neutrality_check(
        lambda t: 0.9 if "pro" in t else 0.2, "pro trace", "con trace", tol=0.05
    )
    assert biased["neutral"] is False
