#!/usr/bin/env python3
"""
Unit tests for moral_psych_scoring.py

Run with:
    cd CEI-Lit-WS && ../.venv/bin/python -m pytest PYTHON/test_moral_psych_scoring.py -v
"""

import unittest
import sys
from pathlib import Path

# Ensure the PYTHON/ directory is on the path
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
sys.path.insert(0, str(_SCRIPT_DIR.parent / ".agent" / "lib"))

from moral_psych_scoring import (
    compute_mp_score,
    compute_all_mp_scores,
    derive_moral_psychology_string,
    parse_moral_psychology_string,
    parse_mp_value,
    is_mp_detected,
    insert_mp_fields_before_moral_psychology,
    update_existing_mp_fields,
    MP_FIELDS,
    FIELD_DISPLAY_NAMES,
    DEFAULT_THRESHOLD,
)


# =====================================================================
# 1. SCORING ENGINE TESTS
# =====================================================================

class TestComputeMpScore(unittest.TestCase):
    """Tests for compute_mp_score() core behavior."""

    def test_empty_text_returns_zero(self):
        for field in MP_FIELDS:
            self.assertEqual(compute_mp_score("", "", field), 0)

    def test_strong_match_gives_at_least_15(self):
        text = "This paper uses Moral Foundations Theory to study ethics."
        score = compute_mp_score(text, "", "mp_mft")
        self.assertGreaterEqual(score, 15)

    def test_multiple_strong_matches_accumulate(self):
        text = "moral foundations and MFT and MFQ scores"
        score = compute_mp_score(text, "", "mp_mft")
        # 3 strong matches -> at least 45
        self.assertGreaterEqual(score, 45)

    def test_fp_keywords_reduce_score(self):
        # FP keywords subtract from raw score.
        # Use a text with a strong match + FP present to see reduction.
        text_no_fp = "We study the trolley problem in ethics"
        text_with_fp = "We study the trolley problem in ethics. The dilemma is common."
        score_no_fp = compute_mp_score(text_no_fp, "", "mp_trolley")
        score_with_fp = compute_mp_score(text_with_fp, "", "mp_trolley")
        # "dilemma" alone (without moral/trolley context in lookahead) is FP,
        # but here "trolley" IS in text, so the FP negative lookahead won't match.
        # Use a different theory where FP clearly applies.
        # Test Schwartz: "Achievement" without Schwartz context is FP
        text_schwartz = "The Schwartz Theory of values covers Achievement and Power."
        text_schwartz_fp = "Achievement in ML benchmarks was remarkable."
        score_s = compute_mp_score(text_schwartz, "", "mp_schwartz")
        score_fp = compute_mp_score(text_schwartz_fp, "", "mp_schwartz")
        self.assertGreater(score_s, score_fp)

    def test_title_bonus_adds_20(self):
        # Use medium-only keywords so the strong-floor doesn't mask the bonus.
        # "five foundations" is medium for MFT.
        text = "We discuss five foundations of morality."
        score_no_title = compute_mp_score(text, "A Study of Something", "mp_mft")
        score_with_title = compute_mp_score(text, "Moral Foundations in AI", "mp_mft")
        self.assertEqual(score_with_title - score_no_title, 20)

    def test_score_clamped_at_100(self):
        # Stuff the text with many strong keywords
        text = " ".join(
            ["moral foundations MFT MFQ MFTC care/harm sanctity/degradation "
             "loyalty/betrayal authority/subversion liberty/oppression "
             "fairness/cheating binding foundation individualizing foundation"]
            * 5
        )
        score = compute_mp_score(text, "Moral Foundations Theory", "mp_mft")
        self.assertLessEqual(score, 100)

    def test_score_clamped_at_zero(self):
        # Only FP keywords, no strong/medium
        text = "The foundation model was trained using a research foundation grant."
        score = compute_mp_score(text, "", "mp_mft")
        self.assertEqual(score, 0)


# =====================================================================
# 2. THEORY-SPECIFIC FALSE POSITIVE TESTS
# =====================================================================

class TestFalsePositives(unittest.TestCase):
    """Verify that known FP-prone words do NOT trigger detection."""

    def test_achievement_alone_does_not_trigger_schwartz(self):
        text = "Achievement in machine learning benchmarks has been remarkable."
        score = compute_mp_score(text, "Achievement in ML", "mp_schwartz")
        self.assertLess(score, 50)

    def test_power_alone_does_not_trigger_schwartz(self):
        text = "Power consumption of large language models is increasing."
        score = compute_mp_score(text, "Power Usage in LLMs", "mp_schwartz")
        self.assertLess(score, 50)

    def test_security_alone_does_not_trigger_schwartz(self):
        text = "Security vulnerabilities in AI systems require attention."
        score = compute_mp_score(text, "AI Security Analysis", "mp_schwartz")
        self.assertLess(score, 50)

    def test_sim_does_not_trigger_intuitionist(self):
        text = "We use a SIM card for connectivity. The simulation ran smoothly."
        score = compute_mp_score(text, "SIM-Based Testing", "mp_intuitionist")
        self.assertLess(score, 50)

    def test_rest_does_not_trigger_kohlberg(self):
        text = "The rest of the participants were excluded. REST API design."
        score = compute_mp_score(text, "REST API Architecture", "mp_kohlberg")
        self.assertLess(score, 50)

    def test_reed_does_not_trigger_identity(self):
        text = "Reed et al. conducted a study on neural networks."
        score = compute_mp_score(text, "Reed Neural Architecture", "mp_identity")
        self.assertLess(score, 50)

    def test_graham_without_moral_context_does_not_trigger_mft(self):
        text = "Graham developed a new optimization algorithm for training."
        score = compute_mp_score(text, "Graham's Algorithm", "mp_mft")
        self.assertLess(score, 50)

    def test_dilemma_alone_does_not_trigger_trolley(self):
        text = "The prisoner's dilemma is a classic game theory problem."
        score = compute_mp_score(text, "Game Theory Dilemma", "mp_trolley")
        self.assertLess(score, 50)

    def test_dual_process_in_cognitive_science_does_not_trigger(self):
        text = "Dual process theory explains memory and attention in cognitive science."
        score = compute_mp_score(text, "Dual Process in Cognition", "mp_dual_process")
        self.assertLess(score, 50)

    def test_dyad_alone_does_not_trigger_dyadic(self):
        text = "We studied dyad interactions in online learning environments."
        score = compute_mp_score(text, "Dyad Communication", "mp_dyadic")
        self.assertLess(score, 50)

    def test_identity_alone_does_not_trigger_identity(self):
        text = "Identity verification systems use biometric data."
        score = compute_mp_score(text, "Identity Systems", "mp_identity")
        self.assertLess(score, 50)


# =====================================================================
# 3. TRUE POSITIVE TESTS
# =====================================================================

class TestTruePositives(unittest.TestCase):
    """Verify that genuine theory references trigger detection >= 50."""

    def test_moral_foundations_theory_triggers_mft(self):
        text = "This study applies Moral Foundations Theory to AI ethics."
        score = compute_mp_score(text, "", "mp_mft")
        self.assertGreaterEqual(score, 50)

    def test_trolley_problem_triggers_trolley(self):
        text = "The trolley problem is central to ethical decision-making in autonomous vehicles."
        score = compute_mp_score(text, "", "mp_trolley")
        self.assertGreaterEqual(score, 50)

    def test_kohlberg_triggers_kohlberg(self):
        text = "Kohlberg's stages of moral development inform our framework."
        score = compute_mp_score(text, "", "mp_kohlberg")
        self.assertGreaterEqual(score, 50)

    def test_schwartz_theory_triggers_schwartz(self):
        text = "We use the Schwartz Theory of Basic Human Values as a lens."
        score = compute_mp_score(text, "", "mp_schwartz")
        self.assertGreaterEqual(score, 50)

    def test_social_intuitionist_model_triggers_intuitionist(self):
        text = "The Social Intuitionist Model proposes that moral intuitions precede reasoning."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_dyadic_morality_triggers_dyadic(self):
        text = "Dyadic Morality suggests all moral judgment involves an agent and a patient."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertGreaterEqual(score, 50)

    def test_moral_identity_triggers_identity(self):
        text = "Moral identity is the degree to which being moral is central to one's self-concept."
        score = compute_mp_score(text, "", "mp_identity")
        self.assertGreaterEqual(score, 50)

    def test_dual_process_with_moral_triggers_dual_process(self):
        text = "Dual process theory applied to moral cognition shows utilitarian reasoning is effortful."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 4. DERIVED STRING TESTS
# =====================================================================

class TestDeriveMoralPsychologyString(unittest.TestCase):
    """Tests for derive_moral_psychology_string()."""

    def test_all_below_threshold_returns_na(self):
        scores = {f: 10 for f in MP_FIELDS}
        self.assertEqual(derive_moral_psychology_string(scores), "N/A")

    def test_single_theory_detected(self):
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_mft"] = 75
        result = derive_moral_psychology_string(scores)
        self.assertEqual(result, "Moral Foundations Theory")

    def test_multiple_theories_comma_separated(self):
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_mft"] = 80
        scores["mp_trolley"] = 60
        result = derive_moral_psychology_string(scores)
        self.assertIn("Moral Foundations Theory", result)
        self.assertIn("Trolley / Dilemmas (Psych)", result)
        self.assertIn(", ", result)

    def test_order_follows_mp_fields(self):
        scores = {f: 100 for f in MP_FIELDS}
        result = derive_moral_psychology_string(scores)
        names = [n.strip() for n in result.split(",")]
        expected_order = [FIELD_DISPLAY_NAMES[f] for f in MP_FIELDS]
        self.assertEqual(names, expected_order)

    def test_exactly_at_threshold_is_detected(self):
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_kohlberg"] = 50
        result = derive_moral_psychology_string(scores)
        self.assertEqual(result, "Cognitive Developmental")

    def test_just_below_threshold_not_detected(self):
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_kohlberg"] = 49
        result = derive_moral_psychology_string(scores)
        self.assertEqual(result, "N/A")


# =====================================================================
# 5. PARSE / BACKWARD COMPAT TESTS
# =====================================================================

class TestParseMpValue(unittest.TestCase):
    """Tests for parse_mp_value() backward compatibility."""

    def test_none_returns_zero(self):
        self.assertEqual(parse_mp_value(None), 0)

    def test_int_returns_same(self):
        self.assertEqual(parse_mp_value(75), 75)

    def test_string_int_returns_int(self):
        self.assertEqual(parse_mp_value("42"), 42)

    def test_na_returns_zero(self):
        self.assertEqual(parse_mp_value("N/A"), 0)

    def test_empty_string_returns_zero(self):
        self.assertEqual(parse_mp_value(""), 0)

    def test_unknown_returns_zero(self):
        self.assertEqual(parse_mp_value("Unknown"), 0)

    def test_float_returns_int(self):
        self.assertEqual(parse_mp_value(42.7), 42)

    def test_quoted_na_returns_zero(self):
        self.assertEqual(parse_mp_value('"N/A"'), 0)


class TestIsMpDetected(unittest.TestCase):
    """Tests for is_mp_detected()."""

    def test_above_threshold_true(self):
        self.assertTrue(is_mp_detected(75))

    def test_below_threshold_false(self):
        self.assertFalse(is_mp_detected(25))

    def test_at_threshold_true(self):
        self.assertTrue(is_mp_detected(50))

    def test_just_below_threshold_false(self):
        self.assertFalse(is_mp_detected(49))

    def test_none_false(self):
        self.assertFalse(is_mp_detected(None))


# =====================================================================
# 6. YAML INSERTION TESTS
# =====================================================================

class TestInsertMpFields(unittest.TestCase):
    """Tests for insert_mp_fields_before_moral_psychology()."""

    def _make_fm(self):
        return (
            'title: "A Test Paper"\n'
            'author: "Smith"\n'
            'moral_psychology: "N/A"\n'
            'tags: ["ethics"]\n'
        )

    def test_inserts_8_fields_before_moral_psychology(self):
        fm = self._make_fm()
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_mft"] = 75
        scores["mp_trolley"] = 60

        new_fm, success = insert_mp_fields_before_moral_psychology(fm, scores)
        self.assertTrue(success)

        # All 8 mp_ fields should appear
        for field in MP_FIELDS:
            self.assertIn(f"{field}:", new_fm)

        # mp_ fields should appear BEFORE moral_psychology:
        first_mp_pos = new_fm.index("mp_mft:")
        moral_psych_pos = new_fm.index("moral_psychology:")
        self.assertLess(first_mp_pos, moral_psych_pos)

    def test_updates_moral_psychology_value(self):
        fm = self._make_fm()
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_mft"] = 75

        new_fm, success = insert_mp_fields_before_moral_psychology(fm, scores)
        self.assertTrue(success)
        self.assertIn('moral_psychology: "Moral Foundations Theory"', new_fm)

    def test_derived_string_na_when_all_below(self):
        fm = self._make_fm()
        scores = {f: 10 for f in MP_FIELDS}

        new_fm, success = insert_mp_fields_before_moral_psychology(fm, scores)
        self.assertTrue(success)
        self.assertIn('moral_psychology: "N/A"', new_fm)

    def test_preserves_surrounding_fields(self):
        fm = self._make_fm()
        scores = {f: 0 for f in MP_FIELDS}

        new_fm, _ = insert_mp_fields_before_moral_psychology(fm, scores)
        self.assertIn('title: "A Test Paper"', new_fm)
        self.assertIn('tags: ["ethics"]', new_fm)

    def test_returns_false_when_no_moral_psychology_line(self):
        fm = 'title: "No MP field"\nauthor: "Jones"\n'
        scores = {f: 0 for f in MP_FIELDS}

        new_fm, success = insert_mp_fields_before_moral_psychology(fm, scores)
        self.assertFalse(success)


class TestUpdateExistingMpFields(unittest.TestCase):
    """Tests for update_existing_mp_fields()."""

    def _make_fm_with_mp(self):
        lines = ['title: "A Test Paper"', 'author: "Smith"']
        for field in MP_FIELDS:
            lines.append(f"{field}: 0")
        lines.append('moral_psychology: "N/A"')
        lines.append('tags: ["ethics"]')
        return "\n".join(lines) + "\n"

    def test_updates_existing_mp_values(self):
        fm = self._make_fm_with_mp()
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_mft"] = 80
        scores["mp_kohlberg"] = 55

        new_fm = update_existing_mp_fields(fm, scores)
        self.assertIn("mp_mft: 80", new_fm)
        self.assertIn("mp_kohlberg: 55", new_fm)
        self.assertIn("mp_schwartz: 0", new_fm)

    def test_updates_derived_moral_psychology_string(self):
        fm = self._make_fm_with_mp()
        scores = {f: 0 for f in MP_FIELDS}
        scores["mp_dyadic"] = 70

        new_fm = update_existing_mp_fields(fm, scores)
        self.assertIn('moral_psychology: "Dyadic Morality"', new_fm)


# =====================================================================
# 7. CATEGORY ALIAS TESTS
# =====================================================================

class TestParseMoralPsychologyString(unittest.TestCase):
    """Tests for parse_moral_psychology_string() alias resolution."""

    def test_schwartz_alias(self):
        result = parse_moral_psychology_string("Schwartz")
        self.assertEqual(result, ["Value Pluralism / Schwartz"])

    def test_kohlberg_alias(self):
        result = parse_moral_psychology_string("Kohlberg")
        self.assertEqual(result, ["Cognitive Developmental"])

    def test_na_returns_empty(self):
        result = parse_moral_psychology_string("N/A")
        self.assertEqual(result, [])

    def test_none_returns_empty(self):
        result = parse_moral_psychology_string(None)
        self.assertEqual(result, [])

    def test_empty_string_returns_empty(self):
        result = parse_moral_psychology_string("")
        self.assertEqual(result, [])

    def test_canonical_name_unchanged(self):
        result = parse_moral_psychology_string("Moral Foundations Theory")
        self.assertEqual(result, ["Moral Foundations Theory"])

    def test_multiple_comma_separated(self):
        result = parse_moral_psychology_string("Schwartz, Kohlberg")
        self.assertEqual(result, ["Value Pluralism / Schwartz", "Cognitive Developmental"])

    def test_dual_process_alias(self):
        result = parse_moral_psychology_string("Dual Process Theory (Moral Cognition)")
        self.assertEqual(result, ["Dual Process Theory"])

    def test_social_intuitionist_alias(self):
        result = parse_moral_psychology_string("Social Intuitionist")
        self.assertEqual(result, ["Social Intuitionist Model"])

    def test_trolley_alias_variants(self):
        result1 = parse_moral_psychology_string("Trolley / Dilemmas")
        self.assertEqual(result1, ["Trolley / Dilemmas (Psych)"])

        result2 = parse_moral_psychology_string("Trolley/Dilemmas (Psych)")
        self.assertEqual(result2, ["Trolley / Dilemmas (Psych)"])

    def test_value_pluralism_slash_variant(self):
        result = parse_moral_psychology_string("Value Pluralism/Schwartz")
        self.assertEqual(result, ["Value Pluralism / Schwartz"])

    def test_dedup_repeated_alias(self):
        result = parse_moral_psychology_string("Schwartz, Value Pluralism/Schwartz")
        self.assertEqual(result, ["Value Pluralism / Schwartz"])


# =====================================================================
# 8. EXPANDED TRUE POSITIVE TESTS (underrepresented theories)
# =====================================================================

class TestExpandedTruePositives(unittest.TestCase):
    """Verify expanded patterns detect underrepresented theories."""

    # ── Dual Process ──
    def test_utilitarian_vs_deontological_judgment_triggers_dual_process(self):
        text = "We examine the utilitarian vs deontological judgment patterns in moral dilemmas."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    def test_cognitive_load_moral_triggers_dual_process(self):
        text = "Under cognitive load, participants shifted from deontological to utilitarian moral judgments."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    def test_response_time_moral_triggers_dual_process(self):
        text = "Response time analysis showed that moral judgments favoring utilitarian outcomes took longer."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    def test_greene_moral_triggers_dual_process(self):
        text = "Building on Greene's work on moral cognition, we tested dual-process predictions."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    def test_personal_force_dilemma_triggers_dual_process(self):
        text = "Personal force scenarios in moral dilemma experiments elicit stronger deontological responses."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    def test_affect_cognition_moral_triggers_dual_process(self):
        text = "The tension between affect and cognition in moral decision-making."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertGreaterEqual(score, 50)

    # ── Intuitionist ──
    def test_post_hoc_rationalization_moral_triggers_intuitionist(self):
        text = "Post-hoc rationalization of moral judgments suggests reasoning follows intuition."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_gut_feeling_moral_triggers_intuitionist(self):
        text = "A gut feeling drives the initial moral assessment before deliberation."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_moral_sentiment_judgment_triggers_intuitionist(self):
        text = "Moral sentiment guides judgment before any explicit reasoning occurs."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_haidt_intuitionist_triggers_intuitionist(self):
        text = "Following Haidt's intuitionist framework, we examine how moral intuitions shape responses."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_moral_heuristic_triggers_intuitionist(self):
        text = "The moral heuristic account proposes fast-and-frugal moral judgments."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    def test_emotion_first_moral_triggers_intuitionist(self):
        text = "An emotion-first account of moral cognition where affect precedes reasoning."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertGreaterEqual(score, 50)

    # ── Dyadic ──
    def test_harm_perception_moral_triggers_dyadic(self):
        text = "Harm perception between a moral agent and patient drives moral judgment."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertGreaterEqual(score, 50)

    def test_schein_moral_triggers_dyadic(self):
        text = "Schein and Gray's theory of dyadic morality posits that moral cognition requires agent and patient."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertGreaterEqual(score, 50)

    def test_agent_patient_harm_triggers_dyadic(self):
        text = "The agent-patient dyad where intentional harm defines the moral violation."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertGreaterEqual(score, 50)

    # ── Abbreviation case fix verification ──
    def test_mft_abbreviation_lowercase_triggers(self):
        text = "We applied the MFT and MFQ instruments to evaluate LLM moral reasoning."
        score = compute_mp_score(text, "", "mp_mft")
        self.assertGreaterEqual(score, 50)

    def test_pvq_abbreviation_lowercase_triggers(self):
        text = "We administered the PVQ and SVS to 10 language models."
        score = compute_mp_score(text, "", "mp_schwartz")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 9. EXPANDED FALSE POSITIVE TESTS
# =====================================================================

class TestExpandedFalsePositives(unittest.TestCase):
    """Verify expanded patterns do NOT trigger on non-moral contexts."""

    def test_automatic_without_moral_no_dual_process(self):
        text = "Automatic speech recognition systems process audio in real time."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertLess(score, 50)

    def test_gut_without_moral_no_intuitionist(self):
        text = "Gut microbiome analysis reveals dietary patterns in populations."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertLess(score, 50)

    def test_harm_without_dyadic_context_no_dyadic(self):
        text = "Harm reduction in drug policy has shown positive outcomes."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertLess(score, 50)

    def test_sentiment_analysis_no_intuitionist(self):
        text = "Sentiment analysis of movie reviews showed positive trends."
        score = compute_mp_score(text, "", "mp_intuitionist")
        self.assertLess(score, 50)

    def test_patient_doctor_no_dyadic(self):
        text = "Patient care in hospital settings requires empathetic communication."
        score = compute_mp_score(text, "", "mp_dyadic")
        self.assertLess(score, 50)

    def test_greene_without_moral_no_dual_process(self):
        text = "Greene published a study on bacterial genetics and antibiotic resistance."
        score = compute_mp_score(text, "", "mp_dual_process")
        self.assertLess(score, 50)


if __name__ == "__main__":
    unittest.main()
