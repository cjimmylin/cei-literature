#!/usr/bin/env python3
"""
Unit tests for religious_scoring.py

Run with:
    cd CEI-Lit-WS && ../.venv/bin/python -m pytest PYTHON/test_religious_scoring.py -v
"""

import unittest
import sys
from pathlib import Path

# Ensure the PYTHON/ directory is on the path
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
sys.path.insert(0, str(_SCRIPT_DIR.parent / ".agent" / "lib"))

from religious_scoring import (
    compute_rv_score,
    compute_all_rv_scores,
    score_paper_rv,
    derive_religious_values_string,
    derive_religious_values_list_string,
    parse_religious_values_string,
    parse_rv_value,
    is_rv_detected,
    get_rv_pinned_score,
    insert_rv_fields_between_religious_values,
    update_existing_rv_fields,
    RV_FIELDS,
    FIELD_DISPLAY_NAMES,
    DEFAULT_THRESHOLD,
)


# =====================================================================
# 1. SCORING ENGINE TESTS
# =====================================================================

class TestComputeRvScore(unittest.TestCase):
    """Tests for compute_rv_score() core behavior."""

    def test_empty_text_returns_zero(self):
        for field in RV_FIELDS:
            self.assertEqual(compute_rv_score("", "", field), 0)

    def test_strong_match_gives_at_least_50(self):
        """Strong-floor: any strong match → minimum 50."""
        text = "This paper analyzes Islamic perspectives on AI."
        score = compute_rv_score(text, "", "rv_islam")
        self.assertGreaterEqual(score, 50)

    def test_multiple_strong_matches_accumulate(self):
        text = "Islam and Muslim perspectives on the Quran and Hadith"
        score = compute_rv_score(text, "", "rv_islam")
        self.assertGreaterEqual(score, 60)

    def test_medium_matches_add_5_each(self):
        text = "The mosque serves the ummah community with halal guidelines."
        score_medium = compute_rv_score(text, "", "rv_islam")
        # 3 medium matches = 15 points, below threshold without strong
        self.assertLess(score_medium, 50)

    def test_title_bonus_adds_20(self):
        text = "A study of halal practices."  # medium only
        score_no_title = compute_rv_score(text, "A Study of Something", "rv_islam")
        score_with_title = compute_rv_score(text, "Islamic Ethics in AI", "rv_islam")
        self.assertEqual(score_with_title - score_no_title, 20)

    def test_score_clamped_at_100(self):
        text = " ".join(
            ["Islam Muslim Quran Qur'an Hadith Sharia Fatwa IslamicPCQA FatwaSet QASiNa"] * 5
        )
        score = compute_rv_score(text, "Islamic AI Ethics", "rv_islam")
        self.assertLessEqual(score, 100)

    def test_score_clamped_at_zero(self):
        text = "This paper studies machine learning optimization."
        score = compute_rv_score(text, "", "rv_islam")
        self.assertEqual(score, 0)


# =====================================================================
# 2. FALSE POSITIVE TESTS
# =====================================================================

class TestFalsePositives(unittest.TestCase):
    """Verify that known FP-prone words do NOT trigger detection."""

    def test_ubuntu_linux_does_not_trigger_ubuntu(self):
        text = "We deployed the model on Ubuntu Linux 22.04 server."
        score = compute_rv_score(text, "Ubuntu Server Deployment", "rv_ubuntu")
        self.assertLess(score, 50)

    def test_ubuntu_operating_system_does_not_trigger(self):
        text = "The Ubuntu operating system was used for all experiments."
        score = compute_rv_score(text, "", "rv_ubuntu")
        self.assertLess(score, 50)

    def test_dharma_alone_does_not_trigger_buddhism(self):
        text = "Dharma practices in Hindu tradition are diverse."
        score = compute_rv_score(text, "", "rv_buddhism")
        self.assertLess(score, 50)

    def test_karma_reddit_does_not_trigger_buddhism(self):
        text = "Reddit karma score system for social media moderation."
        score = compute_rv_score(text, "", "rv_buddhism")
        self.assertLess(score, 50)

    def test_kami_alone_does_not_trigger_shinto(self):
        text = "The kami interface was redesigned for better usability."
        score = compute_rv_score(text, "", "rv_shinto")
        self.assertLess(score, 50)

    def test_indigenous_alone_does_not_trigger(self):
        text = "Indigenous plants were catalogued using machine learning."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertLess(score, 50)

    def test_ahimsa_without_jain_does_not_trigger_jainism(self):
        text = "The principle of ahimsa is central to Indian philosophy."
        score = compute_rv_score(text, "", "rv_jainism")
        self.assertLess(score, 50)

    def test_atman_without_hindu_context_does_not_trigger_hinduism(self):
        text = "The atman concept was studied in the context of philosophy."
        score = compute_rv_score(text, "", "rv_hinduism")
        # atman is in FP list without Hindu context
        self.assertLess(score, 50)


# =====================================================================
# 3. TRUE POSITIVE TESTS
# =====================================================================

class TestTruePositives(unittest.TestCase):
    """Verify that genuine religion references trigger detection >= 50."""

    def test_islam_triggers(self):
        text = "This study examines Islamic perspectives on AI ethics."
        score = compute_rv_score(text, "", "rv_islam")
        self.assertGreaterEqual(score, 50)

    def test_christianity_triggers(self):
        text = "Christian ethics and Biblical values in artificial intelligence."
        score = compute_rv_score(text, "", "rv_christianity")
        self.assertGreaterEqual(score, 50)

    def test_buddhism_triggers(self):
        text = "Buddhist perspectives on AI moral reasoning and the Eightfold Path."
        score = compute_rv_score(text, "", "rv_buddhism")
        self.assertGreaterEqual(score, 50)

    def test_judaism_triggers(self):
        text = "Jewish ethics and Talmudic reasoning applied to AI decisions."
        score = compute_rv_score(text, "", "rv_judaism")
        self.assertGreaterEqual(score, 50)

    def test_hinduism_triggers(self):
        text = "Hindu philosophy and Vedic values in technology design."
        score = compute_rv_score(text, "", "rv_hinduism")
        self.assertGreaterEqual(score, 50)

    def test_sikhism_triggers(self):
        text = "Sikh values and Guru Granth Sahib guide ethical AI."
        score = compute_rv_score(text, "", "rv_sikhism")
        self.assertGreaterEqual(score, 50)

    def test_confucianism_triggers(self):
        text = "Confucian values and the Analects inform AI governance."
        score = compute_rv_score(text, "", "rv_confucianism")
        self.assertGreaterEqual(score, 50)

    def test_taoism_triggers(self):
        text = "Taoist philosophy and wu wei applied to AI alignment."
        score = compute_rv_score(text, "", "rv_taoism")
        self.assertGreaterEqual(score, 50)

    def test_shinto_triggers(self):
        text = "Shinto perspectives on robot consciousness and sacred technology."
        score = compute_rv_score(text, "", "rv_shinto")
        self.assertGreaterEqual(score, 50)

    def test_jainism_triggers(self):
        text = "Jain philosophy of anekantavada and non-violence in AI."
        score = compute_rv_score(text, "", "rv_jainism")
        self.assertGreaterEqual(score, 50)

    def test_bahai_triggers(self):
        text = "The Baha'i faith offers perspectives on global AI governance."
        score = compute_rv_score(text, "", "rv_bahai")
        self.assertGreaterEqual(score, 50)

    def test_zoroastrianism_triggers(self):
        text = "Zoroastrian ethics from the Avesta apply to AI decisions."
        score = compute_rv_score(text, "", "rv_zoroastrianism")
        self.assertGreaterEqual(score, 50)

    def test_ubuntu_philosophy_triggers(self):
        text = "Ubuntu philosophy and African ethics inform AI values."
        score = compute_rv_score(text, "", "rv_ubuntu")
        self.assertGreaterEqual(score, 50)

    def test_indigenous_spirituality_triggers(self):
        text = "Indigenous ethical frameworks and data sovereignty guide responsible AI."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 4. DERIVED STRING TESTS
# =====================================================================

class TestDeriveReligiousValuesString(unittest.TestCase):
    """Tests for derive_religious_values_string()."""

    def test_all_below_threshold_returns_na(self):
        scores = {f: 10 for f in RV_FIELDS}
        self.assertEqual(derive_religious_values_string(scores), "N/A")

    def test_single_tradition_returns_name(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75
        result = derive_religious_values_string(scores)
        self.assertEqual(result, "Islam")

    def test_multiple_traditions_returns_multiple_religions(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 80
        scores["rv_christianity"] = 60
        result = derive_religious_values_string(scores)
        self.assertEqual(result, "Multiple Religions")

    def test_exactly_at_threshold_is_detected(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_judaism"] = 50
        result = derive_religious_values_string(scores)
        self.assertEqual(result, "Judaism")

    def test_just_below_threshold_not_detected(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_judaism"] = 49
        result = derive_religious_values_string(scores)
        self.assertEqual(result, "N/A")


class TestDeriveReligiousValuesListString(unittest.TestCase):
    """Tests for derive_religious_values_list_string()."""

    def test_all_below_returns_na(self):
        scores = {f: 10 for f in RV_FIELDS}
        self.assertEqual(derive_religious_values_list_string(scores), "N/A")

    def test_single_tradition(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75
        result = derive_religious_values_list_string(scores)
        self.assertEqual(result, "Islam")

    def test_multiple_traditions_comma_separated(self):
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 80
        scores["rv_christianity"] = 60
        result = derive_religious_values_list_string(scores)
        self.assertIn("Islam", result)
        self.assertIn("Christianity", result)
        self.assertIn(", ", result)

    def test_order_follows_rv_fields(self):
        scores = {f: 100 for f in RV_FIELDS}
        result = derive_religious_values_list_string(scores)
        names = [n.strip() for n in result.split(",")]
        expected_order = [FIELD_DISPLAY_NAMES[f] for f in RV_FIELDS]
        self.assertEqual(names, expected_order)


# =====================================================================
# 5. PARSE / BACKWARD COMPAT TESTS
# =====================================================================

class TestParseRvValue(unittest.TestCase):
    """Tests for parse_rv_value() backward compatibility."""

    def test_none_returns_zero(self):
        self.assertEqual(parse_rv_value(None), 0)

    def test_int_returns_same(self):
        self.assertEqual(parse_rv_value(75), 75)

    def test_string_int_returns_int(self):
        self.assertEqual(parse_rv_value("42"), 42)

    def test_na_returns_zero(self):
        self.assertEqual(parse_rv_value("N/A"), 0)

    def test_empty_string_returns_zero(self):
        self.assertEqual(parse_rv_value(""), 0)

    def test_unknown_returns_zero(self):
        self.assertEqual(parse_rv_value("Unknown"), 0)

    def test_float_returns_int(self):
        self.assertEqual(parse_rv_value(42.7), 42)

    def test_quoted_na_returns_zero(self):
        self.assertEqual(parse_rv_value('"N/A"'), 0)


class TestIsRvDetected(unittest.TestCase):
    """Tests for is_rv_detected()."""

    def test_above_threshold_true(self):
        self.assertTrue(is_rv_detected(75))

    def test_below_threshold_false(self):
        self.assertFalse(is_rv_detected(25))

    def test_at_threshold_true(self):
        self.assertTrue(is_rv_detected(50))

    def test_just_below_threshold_false(self):
        self.assertFalse(is_rv_detected(49))

    def test_none_false(self):
        self.assertFalse(is_rv_detected(None))


# =====================================================================
# 6. YAML INSERTION TESTS
# =====================================================================

class TestInsertRvFields(unittest.TestCase):
    """Tests for insert_rv_fields_between_religious_values()."""

    def _make_fm(self):
        return (
            'title: "A Test Paper"\n'
            'author: "Smith"\n'
            'religious_values: "N/A"\n'
            'religious_values_list: "N/A"\n'
            'mp_mft: 0\n'
        )

    def test_inserts_14_fields_between_rv_and_rvl(self):
        fm = self._make_fm()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertTrue(success)

        # All 14 rv_ fields should appear
        for field in RV_FIELDS:
            self.assertIn(f"{field}:", new_fm)

        # rv_ fields should appear AFTER religious_values: but BEFORE religious_values_list:
        rv_pos = new_fm.index("religious_values:")
        first_rv_field_pos = new_fm.index("rv_islam:")
        rvl_pos = new_fm.index("religious_values_list:")
        self.assertLess(rv_pos, first_rv_field_pos)
        self.assertLess(first_rv_field_pos, rvl_pos)

    def test_updates_religious_values_with_single(self):
        fm = self._make_fm()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertTrue(success)
        self.assertIn('religious_values: "Islam"', new_fm)

    def test_updates_religious_values_with_multiple(self):
        fm = self._make_fm()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75
        scores["rv_christianity"] = 60

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertTrue(success)
        self.assertIn('religious_values: "Multiple Religions"', new_fm)

    def test_updates_religious_values_list_with_all_detected(self):
        fm = self._make_fm()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 75
        scores["rv_christianity"] = 60

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertTrue(success)
        self.assertIn('religious_values_list: "Islam, Christianity"', new_fm)

    def test_derived_string_na_when_all_below(self):
        fm = self._make_fm()
        scores = {f: 10 for f in RV_FIELDS}

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertTrue(success)
        self.assertIn('religious_values: "N/A"', new_fm)
        self.assertIn('religious_values_list: "N/A"', new_fm)

    def test_preserves_surrounding_fields(self):
        fm = self._make_fm()
        scores = {f: 0 for f in RV_FIELDS}

        new_fm, _ = insert_rv_fields_between_religious_values(fm, scores)
        self.assertIn('title: "A Test Paper"', new_fm)
        self.assertIn('mp_mft: 0', new_fm)

    def test_returns_false_when_no_religious_values_list_line(self):
        fm = 'title: "No RV field"\nauthor: "Jones"\n'
        scores = {f: 0 for f in RV_FIELDS}

        new_fm, success = insert_rv_fields_between_religious_values(fm, scores)
        self.assertFalse(success)


class TestUpdateExistingRvFields(unittest.TestCase):
    """Tests for update_existing_rv_fields()."""

    def _make_fm_with_rv(self):
        lines = ['title: "A Test Paper"', 'author: "Smith"', 'religious_values: "N/A"']
        for field in RV_FIELDS:
            lines.append(f"{field}: 0")
        lines.append('religious_values_list: "N/A"')
        lines.append('mp_mft: 0')
        return "\n".join(lines) + "\n"

    def test_updates_existing_rv_values(self):
        fm = self._make_fm_with_rv()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 80
        scores["rv_buddhism"] = 55

        new_fm = update_existing_rv_fields(fm, scores)
        self.assertIn("rv_islam: 80", new_fm)
        self.assertIn("rv_buddhism: 55", new_fm)
        self.assertIn("rv_christianity: 0", new_fm)

    def test_updates_derived_religious_values(self):
        fm = self._make_fm_with_rv()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_hinduism"] = 70

        new_fm = update_existing_rv_fields(fm, scores)
        self.assertIn('religious_values: "Hinduism"', new_fm)
        self.assertIn('religious_values_list: "Hinduism"', new_fm)

    def test_updates_multiple_religions(self):
        fm = self._make_fm_with_rv()
        scores = {f: 0 for f in RV_FIELDS}
        scores["rv_islam"] = 70
        scores["rv_christianity"] = 60

        new_fm = update_existing_rv_fields(fm, scores)
        self.assertIn('religious_values: "Multiple Religions"', new_fm)
        self.assertIn('religious_values_list: "Islam, Christianity"', new_fm)


# =====================================================================
# 7. TRADITION ALIAS TESTS
# =====================================================================

class TestParseReligiousValuesString(unittest.TestCase):
    """Tests for parse_religious_values_string() alias resolution."""

    def test_ubuntu_alias(self):
        result = parse_religious_values_string("Ubuntu")
        self.assertEqual(result, ["Ubuntu Philosophy"])

    def test_indigenous_alias(self):
        result = parse_religious_values_string("Indigenous")
        self.assertEqual(result, ["Indigenous Spirituality"])

    def test_na_returns_empty(self):
        result = parse_religious_values_string("N/A")
        self.assertEqual(result, [])

    def test_none_returns_empty(self):
        result = parse_religious_values_string(None)
        self.assertEqual(result, [])

    def test_empty_string_returns_empty(self):
        result = parse_religious_values_string("")
        self.assertEqual(result, [])

    def test_canonical_name_unchanged(self):
        result = parse_religious_values_string("Islam")
        self.assertEqual(result, ["Islam"])

    def test_multiple_comma_separated(self):
        result = parse_religious_values_string("Islam, Christianity")
        self.assertEqual(result, ["Islam", "Christianity"])

    def test_multiple_religions_meta_excluded(self):
        result = parse_religious_values_string("Multiple Religions")
        self.assertEqual(result, [])

    def test_bahai_alias(self):
        result = parse_religious_values_string("Bahai")
        self.assertEqual(result, ["Baha'i"])

    def test_daoism_alias(self):
        result = parse_religious_values_string("Daoism")
        self.assertEqual(result, ["Taoism"])

    def test_shintoism_alias(self):
        result = parse_religious_values_string("Shintoism")
        self.assertEqual(result, ["Shinto"])


# =====================================================================
# 8. CROSS-TRADITION ISOLATION TESTS
# =====================================================================

class TestCrossTraditionIsolation(unittest.TestCase):
    """Ensure traditions don't bleed into each other."""

    def test_islam_does_not_trigger_christianity(self):
        text = "Islamic perspectives on AI ethics in the Quran."
        score = compute_rv_score(text, "", "rv_christianity")
        self.assertLess(score, 50)

    def test_hinduism_does_not_trigger_buddhism(self):
        text = "Hindu philosophy and Vedic values in Bhagavad Gita."
        score = compute_rv_score(text, "", "rv_buddhism")
        self.assertLess(score, 50)

    def test_confucianism_does_not_trigger_taoism(self):
        text = "Confucian values and the Analects inform governance."
        score = compute_rv_score(text, "", "rv_taoism")
        self.assertLess(score, 50)

    def test_ubuntu_does_not_trigger_indigenous(self):
        text = "Ubuntu philosophy and African ethics inform AI values."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertLess(score, 50)


# =====================================================================
# 9. DEMOGRAPHICS FALSE-POSITIVE FILTER TESTS (Phase 1)
# =====================================================================

class TestDemographicsFPFilter(unittest.TestCase):
    """Verify demographics context demotes identity keywords."""

    def test_islamophobia_paper_does_not_trigger_islam(self):
        """Bias/hate-speech study mentioning 'Muslim' should NOT trigger Islam."""
        text = (
            "We built a hate speech detection model for offensive language. "
            "Muslim and Islamic stereotypes were among the protected attributes. "
            "Bias detection in NLP models shows demographic bias against Muslim communities."
        )
        score = compute_rv_score(text, "Islamophobia Detection in NLP", "rv_islam")
        self.assertLess(score, 50)

    def test_antisemitism_nlp_does_not_trigger_judaism(self):
        """Anti-semitism bias study should NOT trigger Judaism."""
        text = (
            "This study examines anti-semitic hate speech detection. "
            "Jewish stereotypes appear as protected attributes in bias benchmarks. "
            "Offensive language classification and toxicity detection models."
        )
        score = compute_rv_score(text, "Anti-Semitic Hate Speech Detection", "rv_judaism")
        self.assertLess(score, 50)

    def test_religious_bias_benchmark_does_not_trigger(self):
        """Bias benchmark paper mentioning multiple religions should NOT trigger."""
        text = (
            "We evaluate stereotype bias across demographic groups: Muslim, Christian, "
            "Hindu, Buddhist, and Jewish. Protected attributes include religion. "
            "Toxicity detection and offensive content classification."
        )
        score_islam = compute_rv_score(text, "Bias in Language Models", "rv_islam")
        score_chr = compute_rv_score(text, "Bias in Language Models", "rv_christianity")
        self.assertLess(score_islam, 50)
        self.assertLess(score_chr, 50)

    def test_genuine_islamic_ethics_still_triggers(self):
        """Paper with Quran/Hadith theological terms should still trigger Islam."""
        text = (
            "This paper examines Islamic ethics through the lens of the Quran and Hadith. "
            "Muslim scholars have debated sharia implications for AI governance."
        )
        score = compute_rv_score(text, "Islamic Ethics in AI", "rv_islam")
        self.assertGreaterEqual(score, 50)

    def test_genuine_biblical_theology_still_triggers(self):
        """Paper with Biblical theological terms should still trigger Christianity."""
        text = (
            "Christian ethics as found in Biblical teaching inform AI governance. "
            "The Gospel message and Protestant theological tradition. "
            "Hate speech is mentioned once in passing."
        )
        score = compute_rv_score(text, "Christian AI Ethics", "rv_christianity")
        self.assertGreaterEqual(score, 50)

    def test_demographics_without_enough_context_does_not_demote(self):
        """Only 1 demographics pattern should NOT trigger demotion."""
        text = (
            "This study explores Islamic perspectives on technology. "
            "Some stereotypes about AI exist."
        )
        score = compute_rv_score(text, "", "rv_islam")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 10. INDIGENOUS SPIRITUALITY EXPANSION TESTS (Phase 2)
# =====================================================================

class TestIndigenousExpansion(unittest.TestCase):
    """Verify expanded Indigenous keywords work correctly."""

    def test_indigenous_knowledge_systems_triggers(self):
        text = "This paper discusses indigenous knowledge systems and their role in AI governance."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)

    def test_data_sovereignty_with_indigenous_triggers(self):
        text = "Indigenous data sovereignty and data governance frameworks for ethical AI."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)

    def test_tikanga_triggers(self):
        text = "Tikanga principles guide the ethical design of AI systems in Aotearoa."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)

    def test_kaitiakitanga_triggers(self):
        text = "Kaitiakitanga as a framework for responsible data stewardship."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)

    def test_maori_with_ai_context_triggers(self):
        text = "Maori perspectives on data sovereignty and AI governance in New Zealand."
        score = compute_rv_score(text, "Maori Data Sovereignty", "rv_indigenous")
        self.assertGreaterEqual(score, 50)

    def test_indigenous_plants_does_not_trigger(self):
        """Biological use of 'indigenous' should be penalized."""
        text = "Indigenous plant species were catalogued using machine learning."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertLess(score, 50)

    def test_indigenous_alone_without_context_no_longer_penalized(self):
        """Generic 'indigenous' without biological context should not be FP-penalized."""
        text = "This paper explores indigenous perspectives on community values."
        score = compute_rv_score(text, "", "rv_indigenous")
        # Should be low but not penalized — no strong/medium match, no FP
        self.assertEqual(score, 0)

    def test_inuit_with_knowledge_triggers(self):
        text = "Inuit knowledge systems and ethical frameworks for AI in the Arctic."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreater(score, 0)

    def test_decolonize_with_ai_triggers(self):
        text = "Decolonizing AI requires indigenous ethical frameworks and data sovereignty."
        score = compute_rv_score(text, "", "rv_indigenous")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 11. MINORITY TRADITION EXPANSION TESTS (Phase 3)
# =====================================================================

class TestMinorityTraditionExpansion(unittest.TestCase):
    """Verify expanded keywords for Baha'i, Zoroastrianism, Shinto, Jainism."""

    def test_bahai_bahaullah_triggers(self):
        text = "Baha'u'llah's teachings on unity and justice inform AI ethics."
        score = compute_rv_score(text, "", "rv_bahai")
        self.assertGreater(score, 0)

    def test_bahai_kitab_i_aqdas_triggers(self):
        text = "The Kitab-i-Aqdas provides ethical principles for governance."
        score = compute_rv_score(text, "", "rv_bahai")
        self.assertGreater(score, 0)

    def test_zoroastrianism_ahura_mazda_triggers(self):
        text = "Ahura Mazda's principles of truth and righteousness in ethics."
        score = compute_rv_score(text, "", "rv_zoroastrianism")
        self.assertGreater(score, 0)

    def test_zoroastrianism_gathas_triggers(self):
        text = "The Gathas contain ethical teachings relevant to modern technology."
        score = compute_rv_score(text, "", "rv_zoroastrianism")
        self.assertGreater(score, 0)

    def test_shinto_shintoism_triggers(self):
        text = "Shintoism offers perspectives on technology and nature."
        score = compute_rv_score(text, "", "rv_shinto")
        self.assertGreaterEqual(score, 50)

    def test_shinto_misogi_triggers(self):
        text = "The practice of misogi and ritual purification in Japanese culture."
        score = compute_rv_score(text, "", "rv_shinto")
        self.assertGreater(score, 0)

    def test_shinto_japanese_spirituality_triggers(self):
        text = "Japanese spirituality and sacred spaces in the digital age."
        score = compute_rv_score(text, "", "rv_shinto")
        self.assertGreater(score, 0)

    def test_jainism_aparigraha_triggers(self):
        text = "The Jain principle of aparigraha (non-possessiveness) applied to data."
        score = compute_rv_score(text, "", "rv_jainism")
        self.assertGreaterEqual(score, 50)

    def test_jainism_syadvada_triggers(self):
        text = "Syadvada (the Jain theory of conditional predication) in AI reasoning."
        score = compute_rv_score(text, "", "rv_jainism")
        self.assertGreaterEqual(score, 50)


# =====================================================================
# 12. USER PINS TESTS (Phase 4)
# =====================================================================

class TestUserPins(unittest.TestCase):
    """Verify user pins mechanism."""

    def test_get_rv_pinned_score_returns_none_for_unknown(self):
        """Unknown paper+field returns None."""
        result = get_rv_pinned_score("nonexistent-paper.md", "rv_islam")
        self.assertIsNone(result)

    def test_score_paper_rv_returns_dict_for_all_fields(self):
        """score_paper_rv returns scores for all 14 fields."""
        scores = score_paper_rv("test.md", "Test Paper", "No religion here", "")
        self.assertEqual(set(scores.keys()), set(RV_FIELDS))

    def test_score_paper_rv_genuine_paper(self):
        """score_paper_rv detects genuine Islamic content."""
        scores = score_paper_rv(
            "test.md",
            "Islamic Ethics in AI",
            "This paper examines Islamic perspectives and the Quran",
            ""
        )
        self.assertGreaterEqual(scores["rv_islam"], 50)


if __name__ == "__main__":
    unittest.main()
