#!/usr/bin/env python3
"""
Comprehensive unit tests for the ethics_scoring module.

Run with:
    cd CEI-Lit-WS && ../.venv/bin/python -m pytest PYTHON/test_ethics_scoring.py -v
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from ethics_scoring import (
    DEFAULT_THRESHOLD,
    ETHICS_FIELDS,
    FIELD_KEYWORDS,
    compute_all_scores,
    compute_score,
    count_matches,
    get_pinned_score,
    is_ethics_yes,
    parse_ethics_value,
    safe_yaml_set_int,
    score_paper,
)


# =====================================================================
# 1. parse_ethics_value
# =====================================================================

class TestParseEthicsValue(unittest.TestCase):
    """Test all input types handled by parse_ethics_value."""

    def test_yes_returns_80(self):
        self.assertEqual(parse_ethics_value("Yes"), 80)
        self.assertEqual(parse_ethics_value("yes"), 80)
        self.assertEqual(parse_ethics_value("YES"), 80)

    def test_no_returns_0(self):
        self.assertEqual(parse_ethics_value("No"), 0)
        self.assertEqual(parse_ethics_value("no"), 0)

    def test_unknown_returns_0(self):
        self.assertEqual(parse_ethics_value("Unknown"), 0)
        self.assertEqual(parse_ethics_value("unknown"), 0)

    def test_empty_string_returns_0(self):
        self.assertEqual(parse_ethics_value(""), 0)

    def test_none_returns_0(self):
        self.assertEqual(parse_ethics_value(None), 0)

    def test_int_passthrough(self):
        self.assertEqual(parse_ethics_value(75), 75)
        self.assertEqual(parse_ethics_value(0), 0)
        self.assertEqual(parse_ethics_value(100), 100)

    def test_string_int(self):
        self.assertEqual(parse_ethics_value("75"), 75)
        self.assertEqual(parse_ethics_value("0"), 0)

    def test_float_truncated(self):
        self.assertEqual(parse_ethics_value(0.0), 0)
        self.assertEqual(parse_ethics_value(55.9), 55)

    def test_na_returns_0(self):
        self.assertEqual(parse_ethics_value("N/A"), 0)
        self.assertEqual(parse_ethics_value("n/a"), 0)

    def test_quoted_values_stripped(self):
        self.assertEqual(parse_ethics_value('"Yes"'), 80)
        self.assertEqual(parse_ethics_value("'No'"), 0)

    def test_garbage_string_returns_0(self):
        self.assertEqual(parse_ethics_value("foobar"), 0)


# =====================================================================
# 2. is_ethics_yes
# =====================================================================

class TestIsEthicsYes(unittest.TestCase):
    """Test threshold behavior with legacy and new values."""

    def test_yes_above_default_threshold(self):
        # "Yes" -> 80 >= 50
        self.assertTrue(is_ethics_yes("Yes"))

    def test_no_below_threshold(self):
        self.assertFalse(is_ethics_yes("No"))

    def test_int_at_threshold(self):
        self.assertTrue(is_ethics_yes(50))

    def test_int_below_threshold(self):
        self.assertFalse(is_ethics_yes(49))

    def test_custom_threshold(self):
        # 80 >= 90 is False
        self.assertFalse(is_ethics_yes("Yes", threshold=90))
        # 80 >= 80 is True
        self.assertTrue(is_ethics_yes("Yes", threshold=80))

    def test_zero_threshold(self):
        # Everything except 0 should pass with threshold=0
        self.assertTrue(is_ethics_yes(0, threshold=0))
        self.assertTrue(is_ethics_yes("No", threshold=0))

    def test_none_below_threshold(self):
        self.assertFalse(is_ethics_yes(None))

    def test_default_threshold_is_50(self):
        self.assertEqual(DEFAULT_THRESHOLD, 50)


# =====================================================================
# 3. compute_score — virtue_ethics
# =====================================================================

class TestComputeScoreVirtue(unittest.TestCase):
    """Strong match -> high score, FP reduces, title bonus adds 20."""

    def test_strong_match_high_score(self):
        text = "This paper discusses virtue ethics and eudaimonia in AI systems."
        score = compute_score(text, "Some Title", "virtue_ethics")
        # "virtue ethics" (strong) + "eudaimonia" (strong) = 2*15 = 30
        # "virtue" also matches medium once in "virtue ethics" -> but strong already matched
        # Let's just assert it's reasonably high
        self.assertGreaterEqual(score, 30)

    def test_title_bonus_adds_20(self):
        text = "This paper discusses eudaimonia."
        score_no_title = compute_score(text, "Some Paper", "virtue_ethics")
        score_with_title = compute_score(text, "Virtue in AI", "virtue_ethics")
        self.assertEqual(score_with_title - score_no_title, 20)

    def test_fp_reduces_score(self):
        text = "virtual reality character recognition character encoding"
        score = compute_score(text, "No Match", "virtue_ethics")
        # FP matches: "virtual", "character recognition", "character encoding" = 3 * -10 = -30
        # Clamped to 0
        self.assertEqual(score, 0)

    def test_strong_minus_fp(self):
        text = "virtue ethics and virtual reality character recognition"
        score = compute_score(text, "No Match", "virtue_ethics")
        # strong: "virtue ethics" = 15, medium: "virtue" matches in "virtue ethics" = 5
        # fp: "virtual" = -10, "character recognition" = -10
        # 15 + 5 - 20 = 0 (or close, depends on exact matching)
        self.assertLessEqual(score, 20)


# =====================================================================
# 4. compute_score — deontological_ethics
# =====================================================================

class TestComputeScoreDeont(unittest.TestCase):
    """Tests for deontological ethics scoring."""

    def test_strong_deont_keywords(self):
        text = "This paper examines deontological ethics and the categorical imperative."
        score = compute_score(text, "Some Title", "deontological_ethics")
        # "deontolog..." (strong) + "categorical imperative" (strong) = 2*15 = 30
        self.assertGreaterEqual(score, 30)

    def test_kantian_title_bonus(self):
        text = "This paper examines duty and obligation in AI."
        score_plain = compute_score(text, "AI Systems", "deontological_ethics")
        score_titled = compute_score(text, "Kantian AI Ethics", "deontological_ethics")
        self.assertEqual(score_titled - score_plain, 20)

    def test_fp_rule_based_system(self):
        text = "a rule-based system for rule-based extraction with rule-based method"
        score = compute_score(text, "No Match", "deontological_ethics")
        # FP matches reduce score; medium "rule-based" may also match but FP should dominate
        # Result should be low
        self.assertLessEqual(score, 10)


# =====================================================================
# 5. compute_score — utilitarian_ethics
# =====================================================================

class TestComputeScoreUtil(unittest.TestCase):
    """FP-heavy ML text should score low despite 'utility' mentions."""

    def test_ml_text_low_score(self):
        text = (
            "We maximize accuracy using a utility function. "
            "The utility score and utility class are computed. "
            "We maximize performance and maximize reward."
        )
        score = compute_score(text, "ML Performance Paper", "utilitarian_ethics")
        # medium: "utility" x3 = 15, "maximize" (not followed by FP?) check patterns
        # fp: "utility function", "utility score", "utility class" = -30
        # fp: "maximize accuracy", "maximize performance", "maximize reward" = -30
        # Net is very negative -> clamped to 0
        self.assertLessEqual(score, 10)

    def test_genuine_utilitarian_high(self):
        text = (
            "A utilitarian approach to AI ethics, drawing on consequentialism "
            "and the greatest good principle from Bentham."
        )
        score = compute_score(text, "Some Title", "utilitarian_ethics")
        # strong: "utilitarian" + "consequentialis..." + "greatest good" + "bentham" = 4*15 = 60
        self.assertGreaterEqual(score, 50)

    def test_paper_mill_fp(self):
        text = "A paper mill producing textiles near the windmill on mill creek."
        score = compute_score(text, "No Match", "utilitarian_ethics")
        # fp: "paper mill", "textile mill", "windmill", "mill creek" = 4 * -10 = -40
        # medium: "mill" matches multiple times
        # Net should be low or zero
        self.assertLessEqual(score, 10)


# =====================================================================
# 6. compute_score — ethics_overall
# =====================================================================

class TestComputeScoreEthicsOverall(unittest.TestCase):
    """Title containing 'ethics' + body matches -> high score."""

    def test_ethics_title_and_body(self):
        text = (
            "This paper examines AI ethics and algorithmic fairness. "
            "We consider ethical implications and moral reasoning in AI systems."
        )
        score = compute_score(text, "AI Ethics: A Review", "ethics_overall")
        # strong: "ai ethics", "algorithmic fairness", "ethical implications", "moral reasoning"
        # title bonus: 20
        # Should be high
        self.assertGreaterEqual(score, 50)

    def test_bias_in_ethics_context(self):
        text = (
            "We study bias in machine learning models and its impact on fairness "
            "and discrimination in algorithmic systems."
        )
        score = compute_score(text, "Bias in ML", "ethics_overall")
        # strong lookahead patterns should match "bias" + "fairness", "discrimination" + "algorithm"
        # title bonus for "bias": 20
        self.assertGreaterEqual(score, 20)

    def test_statistical_bias_fp(self):
        text = "We address selection bias, inductive bias, and sampling bias in our estimation."
        score = compute_score(text, "Estimation Methods", "ethics_overall")
        # Only FP matches, no strong matches
        self.assertLessEqual(score, 5)


# =====================================================================
# 7. compute_score — no match
# =====================================================================

class TestComputeScoreNoMatch(unittest.TestCase):
    """Empty or irrelevant text should yield 0."""

    def test_empty_text(self):
        for field in ETHICS_FIELDS:
            self.assertEqual(compute_score("", "", field), 0)

    def test_irrelevant_text(self):
        text = "The cat sat on the mat. Weather today is sunny."
        for field in ETHICS_FIELDS:
            self.assertEqual(compute_score(text, "Cats and Weather", field), 0)


# =====================================================================
# 8. compute_score — clamping
# =====================================================================

class TestComputeScoreClamping(unittest.TestCase):
    """Score never exceeds 100 or goes below 0."""

    def test_never_exceeds_100(self):
        # Pack text with many strong matches
        text = " ".join([
            "virtue ethics eudaimonia phronesis arete aristotelian ethics "
            "aristotelian virtue moral character moral virtue virtue-based "
            "virtue theory character ethics"
        ] * 5)
        score = compute_score(text, "Virtue Ethics Study", "virtue_ethics")
        self.assertLessEqual(score, 100)

    def test_never_below_0(self):
        # Pack text with FP terms only
        text = " ".join([
            "virtual character recognition character encoding character set "
            "character level character-level character embedding unicode character"
        ] * 5)
        score = compute_score(text, "No Match", "virtue_ethics")
        self.assertGreaterEqual(score, 0)

    def test_massive_fp_clamped_to_0(self):
        text = " ".join(["utility function utility score utility class"] * 20)
        score = compute_score(text, "No Match", "utilitarian_ethics")
        self.assertEqual(score, 0)


# =====================================================================
# 9. safe_yaml_set_int — replacement works
# =====================================================================

class TestSafeYamlSetInt(unittest.TestCase):
    """Field replacement works, returns unquoted int, handles quoted strings."""

    def test_basic_replacement(self):
        fm = "title: Some Paper\nethics_overall: Yes\ntags: [a, b]\n"
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 75)
        self.assertTrue(replaced)
        self.assertIn("ethics_overall: 75", new_fm)
        self.assertNotIn("Yes", new_fm)

    def test_replaces_quoted_string(self):
        fm = 'ethics_overall: "Yes"\n'
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 80)
        self.assertTrue(replaced)
        self.assertIn("ethics_overall: 80", new_fm)

    def test_replaces_int_value(self):
        fm = "virtue_ethics: 30\n"
        new_fm, replaced = safe_yaml_set_int(fm, "virtue_ethics", 65)
        self.assertTrue(replaced)
        self.assertIn("virtue_ethics: 65", new_fm)

    def test_value_is_unquoted_int(self):
        fm = "ethics_overall: Yes\n"
        new_fm, _ = safe_yaml_set_int(fm, "ethics_overall", 75)
        # Should be "ethics_overall: 75" not "ethics_overall: '75'" or '"75"'
        self.assertRegex(new_fm, r"ethics_overall: 75\b")
        self.assertNotIn('"75"', new_fm)
        self.assertNotIn("'75'", new_fm)

    def test_preserves_other_fields(self):
        fm = "title: Test\nethics_overall: Yes\nvirtue_ethics: No\n"
        new_fm, _ = safe_yaml_set_int(fm, "ethics_overall", 60)
        self.assertIn("title: Test", new_fm)
        self.assertIn("virtue_ethics: No", new_fm)
        self.assertIn("ethics_overall: 60", new_fm)

    def test_float_value_truncated(self):
        fm = "ethics_overall: Yes\n"
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 75.9)
        self.assertTrue(replaced)
        self.assertIn("ethics_overall: 75", new_fm)


# =====================================================================
# 10. safe_yaml_set_int — field missing
# =====================================================================

class TestSafeYamlSetIntNoField(unittest.TestCase):
    """Returns original text + was_replaced=False when field missing."""

    def test_missing_field(self):
        fm = "title: Test\ntags: [a, b]\n"
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 75)
        self.assertFalse(replaced)
        self.assertEqual(new_fm, fm)

    def test_similar_field_name_no_match(self):
        fm = "my_ethics_overall: Yes\n"
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 75)
        # "my_ethics_overall" should not match "ethics_overall" at line start
        self.assertFalse(replaced)
        self.assertEqual(new_fm, fm)

    def test_empty_frontmatter(self):
        fm = ""
        new_fm, replaced = safe_yaml_set_int(fm, "ethics_overall", 75)
        self.assertFalse(replaced)
        self.assertEqual(new_fm, "")


# =====================================================================
# 11. count_matches
# =====================================================================

class TestCountMatches(unittest.TestCase):
    """Basic regex counting."""

    def test_single_pattern_multiple_hits(self):
        text = "virtue ethics is about virtue and more virtue"
        count, terms = count_matches(text, [r"\bvirtue\b"])
        self.assertEqual(count, 3)
        self.assertEqual(len(terms), 3)
        self.assertTrue(all(t == "virtue" for t in terms))

    def test_no_matches(self):
        count, terms = count_matches("nothing here", [r"\bvirtue\b"])
        self.assertEqual(count, 0)
        self.assertEqual(terms, [])

    def test_multiple_patterns(self):
        text = "virtue ethics and eudaimonia"
        count, terms = count_matches(text, [r"\bvirtue\b", r"\beudaimonia\b"])
        self.assertEqual(count, 2)
        self.assertIn("virtue", terms)
        self.assertIn("eudaimonia", terms)

    def test_case_insensitive(self):
        # count_matches lowercases the text
        text = "VIRTUE Ethics"
        count, terms = count_matches(text, [r"\bvirtue ethics\b"])
        self.assertEqual(count, 1)

    def test_empty_text(self):
        count, terms = count_matches("", [r"\bvirtue\b"])
        self.assertEqual(count, 0)

    def test_empty_patterns(self):
        count, terms = count_matches("some text", [])
        self.assertEqual(count, 0)


# =====================================================================
# 12. compute_all_scores
# =====================================================================

class TestComputeAllScores(unittest.TestCase):
    """Returns dict with all 4 fields."""

    def test_returns_all_fields(self):
        result = compute_all_scores("Test Title", "Some abstract", "Some extract")
        self.assertIsInstance(result, dict)
        for field in ETHICS_FIELDS:
            self.assertIn(field, result)
            self.assertIsInstance(result[field], int)

    def test_all_scores_in_range(self):
        result = compute_all_scores(
            "AI Ethics and Virtue Ethics",
            "This paper examines utilitarian and deontological perspectives.",
            "We discuss virtue ethics, kantian ethics, and consequentialism.",
        )
        for field in ETHICS_FIELDS:
            self.assertGreaterEqual(result[field], 0)
            self.assertLessEqual(result[field], 100)

    def test_empty_inputs(self):
        result = compute_all_scores("", "", "")
        for field in ETHICS_FIELDS:
            self.assertEqual(result[field], 0)

    def test_ethics_text_scores_high(self):
        result = compute_all_scores(
            "AI Ethics Survey",
            "A comprehensive survey of AI ethics, algorithmic fairness, and responsible AI.",
            "",
        )
        self.assertGreaterEqual(result["ethics_overall"], 50)

    def test_field_keywords_structure(self):
        """Verify FIELD_KEYWORDS has expected structure."""
        for field in ETHICS_FIELDS:
            self.assertIn(field, FIELD_KEYWORDS)
            self.assertIn("strong", FIELD_KEYWORDS[field])
            self.assertIn("medium", FIELD_KEYWORDS[field])
            self.assertIn("fp", FIELD_KEYWORDS[field])


# =====================================================================
# Bonus: score_paper with pin override
# =====================================================================

class TestScorePaper(unittest.TestCase):
    """Test score_paper respects pinned scores."""

    @patch("ethics_scoring.get_pinned_score")
    @patch("ethics_scoring.load_extract", return_value="")
    def test_pin_overrides_computed(self, _mock_extract, mock_pin):
        mock_pin.side_effect = lambda fn, field: 5 if field == "virtue_ethics" else None
        result = score_paper(
            "2024-Test-Paper.md",
            "Virtue Ethics in AI",
            "A study of virtue ethics and eudaimonia.",
            extract="virtue ethics aristotelian virtue",
        )
        # virtue_ethics should be pinned at 5 regardless of text
        self.assertEqual(result["virtue_ethics"], 5)
        # Other fields should be computed normally
        self.assertIsInstance(result["ethics_overall"], int)

    @patch("ethics_scoring.get_pinned_score", return_value=None)
    def test_no_pin_uses_computed(self, _mock_pin):
        result = score_paper(
            "2024-Test-Paper.md",
            "Virtue Ethics in AI",
            "A study of virtue ethics and eudaimonia.",
            extract="virtue ethics aristotelian virtue",
        )
        # Without pin, virtue_ethics should reflect text content
        self.assertGreater(result["virtue_ethics"], 0)


if __name__ == "__main__":
    unittest.main()
